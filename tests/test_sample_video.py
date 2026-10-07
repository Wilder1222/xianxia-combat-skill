"""Test timing, evidence boundaries and real extraction with a lossless fixture."""

from fractions import Fraction
import argparse
import importlib.util
import json
from pathlib import Path
import runpy
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / "scripts" / "sample_video.py"))
select_frames = MODULE["select_frames"]
verify_extraction = MODULE["verify_extraction"]
sample_video = MODULE["sample_video"]
EvidenceError = MODULE["EvidenceError"]
BASE = Fraction(1, 1000)
FRAMES = [{"pts": pts, "duration": 100} for pts in (3000, 3100, 3400, 3500, 3900)]


class SelectionTests(unittest.TestCase):
    def test_invalid_cli_times_return_argument_errors(self):
        for value in ("nan", "inf", "1/0", "not-time"):
            with self.subTest(value=value), self.assertRaises(argparse.ArgumentTypeError):
                MODULE["parse_seconds"](value)

    def test_variable_rate_nonzero_origin_and_half_open_interval(self):
        self.assertEqual(select_frames(FRAMES, BASE, Fraction("0.1"), Fraction("0.5"), 1, 60),
                         ([1, 2], 2))

    def test_stride_counts_actual_frames_not_nominal_fps(self):
        self.assertEqual(select_frames(FRAMES, BASE, Fraction(0), Fraction(1), 2, 60),
                         ([0, 2, 4], 5))

    def test_refuses_truncation_and_out_of_range_requests(self):
        for start, end, stride, limit in [(0, 1, 1, 4), (0, 2, 1, 60), (-1, 1, 1, 60),
                                           (1, 0, 1, 60), (0, 1, 0, 60), (0, 1, 1, 121),
                                           (Fraction("0.2"), Fraction("0.3"), 1, 60)]:
            with self.subTest(start=start, end=end, stride=stride, limit=limit):
                with self.assertRaises(EvidenceError):
                    select_frames(FRAMES, BASE, Fraction(start), Fraction(end), stride, limit)

    def test_missing_duplicate_or_regressive_timestamps_are_not_invented(self):
        for pts in ([None, 3100], [3000, 3000], [3100, 3000], ["3000", 3100]):
            frames = [{"pts": value, "duration": 100} for value in pts]
            with self.subTest(pts=pts), self.assertRaises(EvidenceError):
                select_frames(frames, BASE, Fraction(0), Fraction("0.1"), 1, 60)

    def test_unknown_last_frame_duration_is_not_guessed_from_fps(self):
        frames = [{"pts": pts} for pts in (3000, 3100)]
        with self.assertRaises(EvidenceError):
            select_frames(frames, BASE, Fraction(0), Fraction("0.2"), 1, 60)

    def test_extraction_pts_are_independently_checked(self):
        log = "config in time_base: 1/1000\nn: 0 pts: 3100 pts_time:3.1\nn: 1 pts: 3400 pts_time:3.4"
        verify_extraction(log, [3100, 3400], BASE)
        for changed in (log.replace("3100", "3101"), log.replace("1/1000", "1/100"), ""):
            with self.subTest(log=changed), self.assertRaises(EvidenceError):
                verify_extraction(changed, [3100, 3400], BASE)


READY = all(shutil.which(tool) for tool in ("ffmpeg", "ffprobe")) and importlib.util.find_spec("PIL") is not None


@unittest.skipUnless(READY, "需要 ffmpeg、ffprobe 和 Pillow 才能运行真实抽帧测试")
class ExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from PIL import Image
        cls.temp = tempfile.TemporaryDirectory(prefix="xianxia-sampling-test-")
        cls.folder = Path(cls.temp.name)
        cls.colors = [(index * 20, 200 - index * 10, 40 + index * 15) for index in range(10)]
        for index, color in enumerate(cls.colors):
            Image.new("RGB", (64, 48), color).save(cls.folder / f"input-{index:02d}.png")
        cls.source = cls.folder / "非零起点-可变帧率.mkv"
        command = [shutil.which("ffmpeg"), "-hide_banner", "-loglevel", "error", "-nostdin", "-n",
                   "-framerate", "10", "-i", str(cls.folder / "input-%02d.png"),
                   "-vf", "select=eq(n\\,0)+eq(n\\,1)+eq(n\\,4)+eq(n\\,5)+eq(n\\,9),setpts=PTS+3/TB",
                   "-fps_mode", "passthrough", "-c:v", "ffv1", str(cls.source)]
        subprocess.run(command, check=True, capture_output=True, timeout=30)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_actual_vfr_frames_retain_pixels_pts_and_review_boundary(self):
        from PIL import Image
        output = self.folder / "完整逐帧"
        manifest = sample_video(self.source, output, Fraction(0), Fraction(1))
        self.assertEqual([record["pts"] for record in manifest["frames"]], [3000, 3100, 3400, 3500, 3900])
        self.assertEqual([record["relative_seconds"] for record in manifest["frames"]], [0, 0.1, 0.4, 0.5, 0.9])
        self.assertEqual(manifest["status"], "artifacts_created")
        self.assertFalse(any(manifest["review"].values()))
        self.assertEqual(manifest["source"]["sha256"], MODULE["sha256"](self.source))
        for record, original in zip(manifest["frames"], (0, 1, 4, 5, 9)):
            with Image.open(output / record["path"]) as frame:
                self.assertEqual(frame.size, (64, 48))
                self.assertEqual(frame.getpixel((32, 24)), self.colors[original])
            self.assertEqual(record["sha256"], MODULE["sha256"](output / record["path"]))
        self.assertTrue((output / "contact-sheet.jpg").is_file())
        self.assertEqual(json.loads((output / "manifest.json").read_text(encoding="utf-8")), manifest)

    def test_focused_stride_keeps_true_frame_indices(self):
        manifest = sample_video(self.source, self.folder / "局部采样", Fraction("0.1"), Fraction("0.6"), 2)
        self.assertEqual(manifest["window_frame_count"], 3)
        self.assertEqual([record["source_frame_index"] for record in manifest["frames"]], [1, 3])
        self.assertEqual([record["source_pts_seconds"] for record in manifest["frames"]], [3.1, 3.5])
        self.assertEqual(manifest["sampling_mode"], "frame_stride")

    def test_rotation_and_non_square_pixels_preserve_encoded_grid(self):
        from PIL import Image
        pattern = self.folder / "orientation.png"
        with Image.new("RGB", (64, 48), "blue") as frame:
            frame.paste("red", (0, 0, 32, 24))
            frame.save(pattern)
        base = self.folder / "orientation-base.mov"
        source = self.folder / "orientation-rotated.mov"
        ffmpeg = shutil.which("ffmpeg")
        common = [ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin", "-n"]
        subprocess.run(common + ["-loop", "1", "-framerate", "2", "-i", str(pattern),
                                 "-frames:v", "2", "-vf", "setsar=2/1", "-c:v", "png", str(base)],
                       check=True, capture_output=True, timeout=30)
        subprocess.run(common + ["-display_rotation:v:0", "90", "-i", str(base), "-c", "copy", str(source)],
                       check=True, capture_output=True, timeout=30)
        output = self.folder / "方向与像素比例"
        manifest = sample_video(source, output, Fraction(0), Fraction(1))
        probe = json.loads((output / "probe.json").read_text(encoding="utf-8"))
        video = next(s for s in probe["metadata"]["streams"] if s["codec_type"] == "video")
        self.assertEqual(video["sample_aspect_ratio"], "2:1")
        self.assertTrue(any(abs(s.get("rotation", 0)) == 90 for s in video.get("side_data_list", [])))
        self.assertEqual(manifest["sampled_frame_count"], 2)
        for record in manifest["frames"]:
            with Image.open(output / record["path"]) as frame, Image.open(pattern) as expected:
                self.assertEqual(frame.size, (64, 48))
                self.assertEqual(frame.convert("RGB").tobytes(), expected.tobytes())
        self.assertFalse(any(manifest["review"].values()))

    def test_existing_directory_is_preserved(self):
        output = self.folder / "已有资料"
        output.mkdir()
        marker = output / "keep.txt"
        marker.write_text("keep", encoding="utf-8")
        with self.assertRaises(EvidenceError):
            sample_video(self.source, output, Fraction(0), Fraction(1))
        self.assertEqual(marker.read_text(encoding="utf-8"), "keep")
        self.assertEqual(list(output.iterdir()), [marker])

    def test_high_depth_color_metadata_is_retained_without_review_claim(self):
        source = self.folder / "tagged-pq.mkv"
        subprocess.run([shutil.which("ffmpeg"), "-hide_banner", "-loglevel", "error", "-nostdin", "-n",
                        "-f", "lavfi", "-i", "color=gray:size=64x48:rate=2:duration=1",
                        "-vf", "format=yuv420p10le,setparams=range=limited:color_primaries=bt2020:color_trc=smpte2084:colorspace=bt2020nc",
                        "-c:v", "ffv1", "-pix_fmt", "yuv420p10le", "-color_range", "tv",
                        "-colorspace", "bt2020nc", "-color_primaries", "bt2020",
                        "-color_trc", "smpte2084", str(source)],
                       check=True, capture_output=True, timeout=30)
        output = self.folder / "色彩元数据"
        manifest = sample_video(source, output, Fraction(0), Fraction(1))
        probe = json.loads((output / "probe.json").read_text(encoding="utf-8"))
        video = next(s for s in probe["metadata"]["streams"] if s["codec_type"] == "video")
        self.assertEqual(video["pix_fmt"], "yuv420p10le")
        self.assertEqual(video["color_range"], "tv")
        self.assertEqual(video["color_space"], "bt2020nc")
        self.assertEqual(video["color_primaries"], "bt2020")
        self.assertEqual(video["color_transfer"], "smpte2084")
        self.assertEqual(manifest["status"], "artifacts_created")
        self.assertFalse(any(manifest["review"].values()))

    def test_over_limit_fails_before_creating_partial_evidence(self):
        output = self.folder / "超限"
        with self.assertRaises(EvidenceError):
            sample_video(self.source, output, Fraction(0), Fraction(1), limit=4)
        self.assertFalse(output.exists())

    def test_corrupt_input_does_not_produce_success_manifest(self):
        source = self.folder / "broken.mp4"
        source.write_bytes(b"not a video")
        output = self.folder / "损坏"
        with self.assertRaises(EvidenceError):
            sample_video(source, output, Fraction(0), Fraction(1))
        self.assertFalse(output.exists())

    def test_playlist_is_not_misrepresented_by_one_file_hash(self):
        linked = self.folder / "playlist-source.mkv"
        shutil.copyfile(self.source, linked)
        source = self.folder / "playlist.ffconcat"
        source.write_text(f"ffconcat version 1.0\nfile '{linked.name}'\n", encoding="utf-8")
        output = self.folder / "播放列表"
        with self.assertRaisesRegex(EvidenceError, "需要单文件视频"):
            sample_video(source, output, Fraction(0), Fraction(1))
        self.assertFalse(output.exists())

    def test_source_change_after_extraction_invalidates_existing_frames(self):
        source = self.folder / "changed-after-extraction.mkv"
        shutil.copyfile(self.source, source)
        output = self.folder / "源文件变更"
        original_verify = sample_video.__globals__["verify_extraction"]

        def verify_then_change(*args):
            original_verify(*args)
            with source.open("ab") as stream:
                stream.write(b"source changed after decoding")

        with patch.dict(sample_video.__globals__, {"verify_extraction": verify_then_change}):
            with self.assertRaisesRegex(EvidenceError, "源文件发生变化"):
                sample_video(source, output, Fraction(0), Fraction(1))
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["status"], "failed")
        self.assertTrue(list((output / "frames").glob("*.png")))
        self.assertFalse(any(manifest["review"].values()))
        self.assertFalse((output / "report.md").exists())
        self.assertFalse((output / "contact-sheet.jpg").exists())

    def test_verification_failure_marks_created_artifacts_failed(self):
        output = self.folder / "验证失败"
        def fail(*_):
            raise EvidenceError("test timestamp mismatch")
        with patch.dict(sample_video.__globals__, {"verify_extraction": fail}):
            with self.assertRaises(EvidenceError):
                sample_video(self.source, output, Fraction(0), Fraction(1))
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["status"], "failed")
        self.assertFalse(any(manifest["review"].values()))
        self.assertFalse((output / "report.md").exists())


if __name__ == "__main__":
    unittest.main()
