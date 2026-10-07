#!/usr/bin/env python3
"""Create timestamped frame evidence from a local clip; never grade its content."""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys


class EvidenceError(ValueError):
    pass


def run(command, *, cwd=None, quiet=False):
    try:
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=120)
    except subprocess.TimeoutExpired as exc:
        raise EvidenceError("工具运行超过 120 秒；请使用较短的本地视频。") from exc
    if result.returncode or (quiet and result.stderr.strip()):
        raise EvidenceError(f"{Path(command[0]).name} 运行失败：{result.stderr[-1500:]}")
    return result


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def seconds(value):
    return round(float(value), 9)


def parse_seconds(value):
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError("请输入有限的秒数。") from exc


def select_frames(frames, time_base, start, end, stride, limit):
    """Use exact PTS, not nominal FPS; the interval is relative to the first frame."""
    if start < 0 or end <= start:
        raise EvidenceError("需要 0 <= start < end；区间左闭右开。")
    if stride < 1 or not 1 <= limit <= 120:
        raise EvidenceError("stride 必须为正整数，max-frames 必须在 1–120 之间。")
    if time_base <= 0 or not frames:
        raise EvidenceError("没有可用的视频帧或时间基。")
    pts = [frame.get("pts") for frame in frames]
    if any(type(value) is not int for value in pts):
        raise EvidenceError("视频帧缺少整数 PTS，不能可靠定位。")
    if any(right <= left for left, right in zip(pts, pts[1:])):
        raise EvidenceError("视频帧时间戳重复或倒退，不能可靠定位。")
    last_duration = frames[-1].get("duration", frames[-1].get("pkt_duration", 0))
    last_duration = last_duration if isinstance(last_duration, int) and last_duration > 0 else 0
    available_end = (pts[-1] + last_duration - pts[0]) * time_base
    if end > available_end:
        raise EvidenceError(f"end 超出可确认的视频范围（{seconds(available_end)} 秒）；"
                            "末帧时长缺失时不推算其持续时间。")
    window = [index for index, value in enumerate(pts)
              if start <= (value - pts[0]) * time_base < end]
    selected = window[::stride]
    if not selected:
        raise EvidenceError("请求区间内没有显示时间戳对应的帧。")
    if len(selected) > limit:
        raise EvidenceError(f"需要 {len(selected)} 帧，超过上限 {limit}；"
                            "缩短区间、增大 stride 或显式提高 max-frames，不能静默截断。")
    return selected, len(window)


def verify_extraction(log, expected_pts, time_base):
    """Check decoder filter PTS against independently probed frame metadata."""
    bases = re.findall(r"config in time_base:\s*(\d+/\d+)", log)
    actual_pts = [int(value) for value in re.findall(r"\bn:\s*\d+\s+pts:\s*(-?\d+)\b", log)]
    if not bases or any(Fraction(base) != time_base for base in bases):
        raise EvidenceError("抽帧时间基与探测结果不一致。")
    if actual_pts != expected_pts:
        raise EvidenceError("抽帧实际 PTS 与探测清单不一致。")


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_sheet(folder, records, Image, ImageDraw):
    # Raw PNGs are untouched. Only the index sheet is reduced for inspection.
    with Image.open(folder / records[0]["path"]) as first:
        width, height = first.size
    scale = min(400 / width, 300 / height, 1)
    thumb = (max(1, round(width * scale)), max(1, round(height * scale)))
    columns = min(4, len(records))
    cell_width, cell_height = max(300, thumb[0] + 16), thumb[1] + 54
    rows = (len(records) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height + 32), "#171b22")
    draw = ImageDraw.Draw(sheet)
    draw.text((8, 8), "Sampled frames only | t = seconds from first video frame | PTS = source clock", fill="white")
    for index, record in enumerate(records):
        x, y = (index % columns) * cell_width + 8, (index // columns) * cell_height + 36
        with Image.open(folder / record["path"]) as frame:
            frame.thumbnail(thumb, Image.Resampling.LANCZOS)
            sheet.paste(frame.convert("RGB"), (x, y))
        draw.text((x, y + thumb[1] + 5),
                  f"#{index + 1:03d}  t={record['relative_seconds']:.6f}s  frame={record['source_frame_index']}",
                  fill="white")
        draw.text((x, y + thumb[1] + 22), f"PTS={record['source_pts_seconds']:.6f}s", fill="#b7c2d5")
    sheet.save(folder / "contact-sheet.jpg", quality=92)


def sample_video(source, output, start, end, stride=1, limit=60):
    source, output = Path(source).resolve(), Path(output).resolve()
    if not source.is_file():
        raise EvidenceError("input 必须是已有的本地视频文件。")
    if output.exists():
        raise EvidenceError("输出目录已存在；请提供新目录，已有资料不会被覆盖。")
    if start < 0 or end <= start or stride < 1 or not 1 <= limit <= 120:
        raise EvidenceError("检查时间区间、正整数 stride 和 1–120 的 max-frames。")
    ffmpeg, ffprobe = shutil.which("ffmpeg"), shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        raise EvidenceError("需要 PATH 中已有的 ffmpeg 和 ffprobe。")
    try:
        from PIL import Image, ImageDraw, __version__ as pillow_version
    except ImportError as exc:
        raise EvidenceError("需要当前 Python 环境中的 Pillow。") from exc

    source_hash = sha256(source)
    metadata = json.loads(run([
        ffprobe, "-v", "error", "-protocol_whitelist", "file", "-show_entries",
        "format=start_time,duration,format_name:"
        "stream=index,codec_type,codec_name,width,height,time_base,avg_frame_rate,r_frame_rate,"
        "start_time,duration,nb_frames,sample_aspect_ratio,display_aspect_ratio,"
        "pix_fmt,bits_per_raw_sample,color_range,color_space,color_transfer,color_primaries:"
        "stream_disposition=attached_pic:stream_side_data=rotation",
        "-of", "json", str(source)], quiet=True).stdout)
    if metadata.get("format", {}).get("format_name") in {"hls", "dash", "concat", "image2"}:
        raise EvidenceError("需要单文件视频；不使用依赖其他媒体文件的播放列表或图片序列。")
    video = next((stream for stream in metadata.get("streams", [])
                  if stream.get("codec_type") == "video"
                  and not stream.get("disposition", {}).get("attached_pic")), None)
    if video is None:
        raise EvidenceError("没有可解码的视频轨。")
    time_base = Fraction(video["time_base"])
    decoded = json.loads(run([
        ffprobe, "-v", "error", "-protocol_whitelist", "file", "-err_detect", "explode", "-select_streams", str(video["index"]),
        "-show_frames", "-show_entries", "frame=pts,duration,pkt_duration", "-of", "json", str(source)
    ], quiet=True).stdout).get("frames", [])
    # Retain only timing fields; incidental SEI metadata is not needed for this task.
    frames = [{key: frame[key] for key in ("pts", "duration", "pkt_duration") if key in frame}
              for frame in decoded]
    selected, window_count = select_frames(frames, time_base, start, end, stride, limit)
    first_pts = frames[0]["pts"]
    records = [{"path": f"frames/frame-{number:04d}.png", "source_frame_index": index,
                "pts": frames[index]["pts"],
                "source_pts_seconds": seconds(frames[index]["pts"] * time_base),
                "relative_seconds": seconds((frames[index]["pts"] - first_pts) * time_base)}
               for number, index in enumerate(selected, 1)]
    manifest = {
        "schema_version": 1, "status": "incomplete",
        "source": {"name": source.name, "sha256": source_hash, "bytes": source.stat().st_size},
        "video_stream_index": video["index"], "time_base": str(time_base),
        "time_origin": "first_video_frame", "first_video_pts": first_pts,
        "first_video_pts_seconds": seconds(first_pts * time_base),
        "decoded_frame_count": len(frames),
        "request": {"start_seconds": seconds(start), "end_seconds": seconds(end),
                    "interval": "[start, end)", "stride": stride, "max_frames": limit},
        "window_frame_count": window_count, "sampled_frame_count": len(records),
        "sampling_mode": "every_frame_in_window" if stride == 1 else "frame_stride",
        "image_transform": "No autorotation, spatial scaling, interpolation or retiming; FFmpeg converts decoded pixels to 8-bit RGB (rgb24). No explicit tone mapping or display color management.",
        "review": {"frames_visually_reviewed": False, "original_speed_playback_reviewed": False,
                   "audio_reviewed": False},
        "limitations": ["采样清单只证明抽帧范围；不自动判断接触、受力、连续性或视觉质量。",
                        "静帧不等于原速播放；未审听音轨。stride 大于 1 时可能漏掉短暂接触。",
                        "时间相对于视频首帧，另保留源 PTS；与播放器时间轴可能存在起点差异。",
                        "PNG 保留编码画面方向及像素网格；旋转和非方形像素需结合元数据及播放器核查。",
                        "PNG 为 8 位 RGB 转换，未显式进行 HDR 色调映射或显示色彩管理；不能据此保证高光、色彩或原始位深保真。源色彩标签见 probe.json，缺失标签不推定为 SDR。"],
        "tools": {"ffmpeg": run([ffmpeg, "-version"]).stdout.splitlines()[0],
                  "ffprobe": run([ffprobe, "-version"]).stdout.splitlines()[0], "Pillow": pillow_version},
        "frames": records,
    }
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / "manifest.json", manifest)
    try:
        (output / "frames").mkdir()
        write_json(output / "probe.json", {"metadata": metadata, "video_frames": frames})
        expression = "+".join(f"eq(n\\,{index})" for index in selected)
        result = run([
            ffmpeg, "-hide_banner", "-nostdin", "-n", "-xerror", "-loglevel", "info",
            "-copyts", "-noautorotate", "-protocol_whitelist", "file", "-err_detect", "explode", "-i", str(source),
            "-map", f"0:{video['index']}", "-an", "-sn", "-dn",
            "-vf", f"select={expression},showinfo", "-fps_mode", "passthrough",
            "-frames:v", str(len(records)), "-c:v", "png", "-pix_fmt", "rgb24",
            "frames/frame-%04d.png"], cwd=output)
        verify_extraction(result.stderr, [record["pts"] for record in records], time_base)
        if len(list((output / "frames").glob("*.png"))) != len(records):
            raise EvidenceError("输出帧数与采样清单不一致。")
        for record in records:
            frame_path = output / record["path"]
            with Image.open(frame_path) as frame:
                frame.load()
                record["width"], record["height"] = frame.size
            record["sha256"] = sha256(frame_path)
        if sha256(source) != source_hash:
            raise EvidenceError("分析期间源文件发生变化，本次证据不可合并。")
        make_sheet(output, records, Image, ImageDraw)
        manifest["contact_sheet"] = {"path": "contact-sheet.jpg", "sha256": sha256(output / "contact-sheet.jpg")}
        report = ["# 视频抽帧记录", "", "状态：已创建抽帧资料，尚未完成人工视频审阅。", "",
                  f"源文件 SHA-256：`{source_hash}`", "",
                  f"请求区间：[{seconds(start)}, {seconds(end)}) 秒；以视频首帧为零点。",
                  f"首帧源 PTS：{seconds(first_pts * time_base)} 秒；时间基：{time_base}。",
                  f"区间内 {window_count} 帧，每 {stride} 帧取一帧，实际保存 {len(records)} 帧。", "",
                  "| 图片 | 源帧序号（从 0 开始） | 相对首帧秒数 | 源 PTS 秒数 |",
                  "|---|---|---|---|"]
        report.extend(f"| {record['path']} | {record['source_frame_index']} | {record['relative_seconds']:.9f} | {record['source_pts_seconds']:.9f} |"
                      for record in records)
        report.extend(["", *manifest["limitations"], "", "人工观察：尚未填写。", ""])
        (output / "report.md").write_text("\n".join(report), encoding="utf-8")
        manifest["status"] = "artifacts_created"
        write_json(output / "manifest.json", manifest)
    except Exception as exc:
        manifest["status"] = "failed"
        manifest["error"] = str(exc).replace(str(source), "<input>").replace(str(output), "<output>")[-1800:]
        write_json(output / "manifest.json", manifest)
        raise
    return manifest


def main():
    parser = argparse.ArgumentParser(description="为本地短视频生成可追溯抽帧资料，不自动评判质量。")
    parser.add_argument("input", type=Path, help="本地视频路径")
    parser.add_argument("--out", type=Path, required=True, help="尚不存在的输出目录")
    parser.add_argument("--start", type=parse_seconds, default=Fraction(0), help="相对视频首帧的起始秒数，默认 0")
    parser.add_argument("--end", type=parse_seconds, required=True, help="相对视频首帧的结束秒数，不含该时刻")
    parser.add_argument("--stride", type=int, default=1, help="区间内每 N 帧取一帧，默认逐帧")
    parser.add_argument("--max-frames", type=int, default=60, help="输出上限 1–120，默认 60；超限报错")
    args = parser.parse_args()
    try:
        result = sample_video(args.input, args.out, args.start, args.end, args.stride, args.max_frames)
    except (EvidenceError, OSError, ValueError, KeyError) as exc:
        print(f"未完成：{exc}", file=sys.stderr)
        return 1
    print(f"已创建 {result['sampled_frame_count']} 帧及采样清单：{args.out.resolve()}")
    print("抽帧成功不代表视频已审阅或视觉质量通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
