"""Verify detached installation, private-file exclusion, and safe rebuilding."""

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("plugin_support", ROOT / "scripts/plugin_support.py")
SUPPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUPPORT)


class PluginPackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "source"
        self.root.mkdir()
        for name, data in SUPPORT.package_files(ROOT).items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

    def test_detached_package_excludes_private_files_and_resolves_links(self):
        for name in (".local-evidence/private.md", ".git/config", "references/cache.pyc"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("private sentinel", encoding="utf-8")
        package, receipt = SUPPORT.build(self.root)
        detached = Path(self.temporary.name) / "installed"
        shutil.copytree(package, detached)
        shutil.rmtree(self.root)
        SUPPORT.check(detached)
        self.assertFalse((detached / ".local-evidence").exists())
        self.assertFalse((detached / ".git").exists())
        self.assertNotIn("references/cache.pyc", receipt["sha256"])

    def test_rebuild_rejects_edited_output_and_preserves_it(self):
        package, _ = SUPPORT.build(self.root)
        edited = package / "SKILL.md"
        edited.write_text("manual edit to preserve", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "edited files"):
            SUPPORT.build(self.root)
        self.assertEqual(edited.read_text(encoding="utf-8"), "manual edit to preserve")

    def test_rebuild_updates_changed_authority_and_detects_entry_drift(self):
        SUPPORT.build(self.root)
        source = self.root / "SKILL.md"
        source.write_text(source.read_text(encoding="utf-8").replace("创作和改写", "编排和改写", 1), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Stale generated"):
            SUPPORT.check(self.root)
        SUPPORT.sync(self.root)
        package, _ = SUPPORT.build(self.root)
        self.assertIn("编排和改写", (package / SUPPORT.ENTRY).read_text(encoding="utf-8"))
        SUPPORT.check(package)

    def test_unbundled_reference_fails_before_output_changes(self):
        package, _ = SUPPORT.build(self.root)
        original = (package / "SKILL.md").read_bytes()
        unbundled = self.root / "user-notes.txt"
        unbundled.write_text("not part of the runtime package", encoding="utf-8")
        with (self.root / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\n[unbundled dependency](user-notes.txt)\n")
        with self.assertRaisesRegex(ValueError, "本地引用不可用"):
            SUPPORT.build(self.root)
        self.assertEqual((package / "SKILL.md").read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
