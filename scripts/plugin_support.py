#!/usr/bin/env python3
"""Sync, check, and package the skill without copying local generation evidence."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile

try:
    from validate_repository import validate_links, validate_timelines
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from validate_repository import validate_links, validate_timelines


ROOT = Path(__file__).resolve().parents[1]
ENTRY = "skills/xianxia-combat/SKILL.md"
COMPAT = ".codex-plugin/plugin.json"
MARKETPLACE = ".agents/plugins/marketplace.json"
RUNTIME_SCRIPTS = ("sample_video.py", "validate_repository.py", "plugin_support.py")
RUNTIME_TESTS = ("test_sample_video.py", "test_validate_repository.py", "test_plugin_support.py")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def generated_files(root):
    manifest = read_json(root / "plugin.json")
    source = (root / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", source, re.S)
    if not frontmatter:
        raise ValueError("SKILL.md has no YAML frontmatter")
    entry = (
        f"---\n{frontmatter[1]}\n---\n\n# 仙侠打斗插件入口\n\n"
        "先读取 [主工作流](../../SKILL.md)，再按其中的任务路由选择参考并执行。\n\n"
        "本文件的 `../..` 是插件根目录。主工作流中的 `references/`、`examples/`、"
        "`research/` 和 `scripts/` 均相对插件根目录；命令从插件根目录运行或使用解析后的绝对路径。"
        "主工作流和所有相对引用已随插件打包，不依赖原仓库位置。\n\n"
        "此入口由 `scripts/plugin_support.py sync` 生成，行为规则在主工作流维护。\n"
    )
    compatibility = {key: manifest[key] for key in ("name", "version", "description", "author")}
    compatibility.update({"skills": "./skills/", **manifest["extensions"]["com.openai"]})
    return {ENTRY: entry.encode("utf-8"), COMPAT: json_bytes(compatibility)}


def sync(root):
    for name, data in generated_files(root).items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_bytes() != data:
            path.write_bytes(data)


def check(root):
    manifest = read_json(root / "plugin.json")
    if manifest.get("name") != "xianxia-combat" or not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        raise ValueError("Invalid plugin identity or version")
    marketplace = read_json(root / MARKETPLACE)
    plugins = marketplace.get("plugins", [])
    if marketplace.get("name") != "xianxia-combat-marketplace" or len(plugins) != 1:
        raise ValueError("Unexpected marketplace identity or entries")
    plugin = plugins[0]
    if (plugin.get("name") != manifest["name"]
            or plugin.get("source") != {"source": "local", "path": "./"}
            or plugin.get("policy") != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
            or plugin.get("category") != "Productivity"):
        raise ValueError("Marketplace must resolve this plugin root")
    for name, data in generated_files(root).items():
        if not (root / name).is_file() or (root / name).read_bytes() != data:
            raise ValueError(f"Stale generated file: {name}; run sync")
    errors, _ = validate_links(root)
    timeline_errors, _, _ = validate_timelines((root / "examples/behavior-regression.md").read_text(encoding="utf-8"))
    if errors or timeline_errors:
        raise ValueError("\n".join(errors + timeline_errors))


def package_files(root):
    names = ["plugin.json", COMPAT, MARKETPLACE, "SKILL.md", ENTRY, "README.md"]
    for directory in ("references", "examples", "research"):
        names.extend(path.relative_to(root).as_posix() for path in (root / directory).rglob("*.md"))
    names.extend("scripts/" + name for name in RUNTIME_SCRIPTS)
    names.extend("tests/" + name for name in RUNTIME_TESTS)
    files = {}
    for name in sorted(names):
        path = root / name
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"Package source escapes repository: {name}")
        files[name] = path.read_bytes()
    return files


def verify_previous(output, receipt):
    if not output.exists():
        return
    if output.is_symlink() or not receipt.is_file():
        raise ValueError("Existing output is not a recognized build")
    previous = read_json(receipt)
    if previous.get("name") != "xianxia-combat" or not isinstance(previous.get("sha256"), dict):
        raise ValueError("Invalid previous build receipt")
    actual = {}
    for path in output.rglob("*"):
        if path.is_symlink():
            raise ValueError("Symlink in existing package")
        if path.is_file():
            actual[path.relative_to(output).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != previous["sha256"]:
        raise ValueError("Existing package contains unrecognized or edited files; preserve it and move it aside before rebuilding")


def build(root):
    check(root)
    files = package_files(root)
    parent = root / "dist/codex-plugin"
    output = parent / "xianxia-combat"
    receipt = parent / "build.json"
    for path in (root / "dist", parent, output):
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("Build directory must remain inside this repository")
    verify_previous(output, receipt)
    if output.exists():
        previous_names = set(read_json(receipt)["sha256"])
        if previous_names - set(files):
            raise ValueError("Build layout changed; preserve the old package and move it aside first")
    parent.mkdir(parents=True, exist_ok=True)
    # Check a complete independent tree before touching an existing package.
    with tempfile.TemporaryDirectory(prefix="staging-", dir=parent) as temporary:
        staging = Path(temporary)
        if not staging.resolve().is_relative_to(parent.resolve()):
            raise ValueError("Staging directory escapes build root")
        for name, data in files.items():
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        check(staging)
        _, links = validate_links(staging)
    output.mkdir(parents=True, exist_ok=True)
    for name, data in files.items():
        path = output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    marketplace = read_json(root / MARKETPLACE)
    marketplace["plugins"][0]["source"]["path"] = "./xianxia-combat"
    market_file = parent / MARKETPLACE
    market_file.parent.mkdir(parents=True, exist_ok=True)
    market_file.write_bytes(json_bytes(marketplace))
    digest = {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}
    result = {"name": "xianxia-combat", "version": read_json(root / "plugin.json")["version"],
              "file_count": len(files), "local_references": links, "sha256": digest}
    receipt.write_bytes(json_bytes(result))
    return output, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("sync", "check", "build"))
    command = parser.parse_args().command
    try:
        if command == "sync":
            sync(ROOT)
        elif command == "check":
            check(ROOT)
        else:
            output, result = build(ROOT)
            print(f"Built: {output} ({result['file_count']} files)")
        print("PASS: " + command)
        return 0
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
