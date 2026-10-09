#!/usr/bin/env python3
"""Validate local reference targets and example timelines, not creative quality."""

from pathlib import Path
import os
import re
import sys
import unicodedata
from urllib.parse import unquote


LOCAL_ONLY_DIRECTORIES = {".git", ".local-evidence", "__pycache__", "dist"}


def in_local_only_directory(relative_path):
    return any(os.path.normcase(part) in LOCAL_ONLY_DIRECTORIES
               for part in relative_path.parts)


def validate_timelines(content):
    errors = []
    cases_checked = 0
    segments_checked = 0
    for case in re.split(r"^## ", content, flags=re.M)[1:]:
        title = case.splitlines()[0]
        target = re.search(r"^目标时长：(\d+) 秒。$", case, re.M)
        if not target:
            if re.search(r"^### 片段|^```text$", case, re.M):
                errors.append(f"{title}：有片段但缺少目标时长")
            continue
        cases_checked += 1
        target_seconds = int(target.group(1))
        parts = re.split(r"^### 片段 ", case, flags=re.M)[1:]
        if not parts:
            errors.append(f"{title}：缺少片段")
        total = 0
        for index, part in enumerate(parts, start=1):
            header = re.match(r"(\d+)（(\d+) 秒）\n", part)
            if not header:
                errors.append(f"{title}：片段标题无法解析")
                continue
            number, duration = map(int, header.groups())
            segments_checked += 1
            if number != index:
                errors.append(f"{title}：片段编号不连续")
            if duration <= 0:
                errors.append(f"{title}：片段时长必须大于零")
            total += duration
            blocks = re.findall(r"^```text\n(.*?)^```\s*$", part, re.M | re.S)
            if len(blocks) != 1:
                errors.append(f"{title}片段{number}：必须有一个完整提示词块")
                continue
            time_rows = [line for line in blocks[0].splitlines()
                         if re.match(r"^\d+(?:[–-]|\s*秒)", line)]
            if not time_rows:
                errors.append(f"{title}片段{number}：缺少时间轴")
            cursor = 0
            for row in time_rows:
                window = re.match(r"^(\d+)[–-](\d+)秒：(.+)$", row)
                if not window:
                    errors.append(f"{title}片段{number}：时间窗无法解析")
                    continue
                start, end = map(int, window.groups()[:2])
                if start != cursor or end <= start:
                    errors.append(f"{title}片段{number}：{start}-{end} 不连续或非正时长")
                cursor = end
            if cursor != duration:
                errors.append(f"{title}片段{number}：末端 {cursor} 不等于 {duration} 秒")
        if total != target_seconds:
            errors.append(f"{title}：片段合计 {total} 不等于目标 {target_seconds} 秒")
    if not cases_checked:
        errors.append("未发现可检查的时间轴案例")
    return errors, cases_checked, segments_checked


def without_fenced_code(content):
    """Exclude backtick/tilde fenced examples from navigation checks."""
    lines = []
    fence = None
    for line in content.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if (marker and marker[1][0] == fence[0]
                    and len(marker[1]) >= len(fence) and not marker[2].strip()):
                fence = None
            lines.append("")
        elif marker:
            fence = marker[1]
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines)


def heading_anchors(content):
    """Repository ATX headings, not a general-purpose Markdown renderer."""
    anchors = set()
    for line in without_fenced_code(content).splitlines():
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*$", line)
        if not match:
            continue
        title = re.sub(r"\s+#+$", "", match[1])
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", title)
        title = re.sub(r"<[^>]+>", "", title)
        # Strip common inline formatting; preserve underscores inside words.
        title = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", title)
        title = title.replace("`", "").replace("*", "").replace("~", "")
        base = "".join(c for c in title.strip().lower()
                       if c in " -_" or unicodedata.category(c)[0] in "LNM")
        base = base.replace(" ", "-")
        anchor = base
        suffix = 0
        while anchor in anchors:
            suffix += 1
            anchor = f"{base}-{suffix}"
        anchors.add(anchor)
    return anchors


def validate_links(root):
    root = Path(root).resolve()
    errors = []
    checked = 0
    anchors = {}
    for file in root.rglob("*.md"):
        if in_local_only_directory(file.relative_to(root)):
            continue
        content = file.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", without_fenced_code(content)):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            path, separator, fragment = target.partition("#")
            checked += 1
            resolved = (file.parent / unquote(path)).resolve() if path else file
            if not resolved.is_relative_to(root) or not resolved.is_file():
                errors.append(f"{file.relative_to(root)}：本地引用不可用 {target}")
            elif in_local_only_directory(resolved.relative_to(root)):
                errors.append(f"{file.relative_to(root)}：本地引用指向不发布的目录 {target}")
            elif separator and fragment and resolved.suffix.lower() == ".md":
                if resolved not in anchors:
                    anchors[resolved] = heading_anchors(resolved.read_text(encoding="utf-8"))
                if unquote(fragment) not in anchors[resolved]:
                    errors.append(f"{file.relative_to(root)}：本地章节不存在 {target}")
    return errors, checked


def main():
    root = Path(__file__).resolve().parents[1]
    link_errors, links = validate_links(root)
    content = (root / "examples" / "behavior-regression.md").read_text(encoding="utf-8")
    time_errors, cases, segments = validate_timelines(content)
    errors = link_errors + time_errors
    if errors:
        print("\n".join(errors))
        return 1
    print(f"通过：{links} 个本地引用，{cases} 个时间轴案例，{segments} 个片段。")
    print("检查范围为引用和时长结构，不代表攻防语义或实际视频质量通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
