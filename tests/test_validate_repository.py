"""Exercise structural invariants; do not use these tests to score video quality."""

from pathlib import Path
import runpy
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATORS = runpy.run_path(str(ROOT / "scripts" / "validate_repository.py"))
validate_timelines = VALIDATORS["validate_timelines"]
validate_links = VALIDATORS["validate_links"]

VALID = """# 文本案例

## 交锋

目标时长：8 秒。

### 片段 1（8 秒）

```text
3D国漫CGI，两名虚构修士。
0-3秒：甲踏近，乙格挡。
3-6秒：甲收剑，乙侧退。
6-8秒：双方脱离。
```
"""


class TimelineTests(unittest.TestCase):
    def test_valid_and_3d_style_line(self):
        self.assertEqual(validate_timelines(VALID), ([], 1, 1))

    def test_en_dash(self):
        self.assertEqual(validate_timelines(VALID.replace("-", "–")), ([], 1, 1))

    def test_two_segments_sum_to_target(self):
        second = VALID.split("### 片段 1", 1)[1]
        text = VALID.replace("目标时长：8 秒。", "目标时长：16 秒。")
        text += "\n### 片段 2" + second
        self.assertEqual(validate_timelines(text), ([], 1, 2))

    def test_reject_invalid_timelines(self):
        mutations = {
            "gap": ("3-6秒", "4-6秒"),
            "overlap": ("3-6秒", "2-6秒"),
            "zero": ("3-6秒", "3-3秒"),
            "backwards": ("3-6秒", "3-2秒"),
            "wrong_end": ("6-8秒", "6-7秒"),
            "wrong_total": ("目标时长：8 秒。", "目标时长：9 秒。"),
            "wrong_number": ("片段 1", "片段 2"),
            "missing_target": ("目标时长：8 秒。", ""),
            "broken_fence": ("```text", "```"),
            "missing_action": ("3-6秒：甲收剑，乙侧退。", "3-6秒："),
            "zero_duration": ("片段 1（8 秒）", "片段 1（0 秒）"),
        }
        for name, (old, new) in mutations.items():
            with self.subTest(name=name):
                self.assertIn(old, VALID)
                self.assertTrue(validate_timelines(VALID.replace(old, new, 1))[0])

    def test_reject_missing_segments(self):
        self.assertTrue(validate_timelines("## 空案例\n目标时长：8 秒。\n")[0])

    def test_reject_no_timeline(self):
        text = VALID.replace("0-3秒：甲踏近，乙格挡。\n", "")
        text = text.replace("3-6秒：甲收剑，乙侧退。\n", "")
        text = text.replace("6-8秒：双方脱离。\n", "")
        self.assertTrue(validate_timelines(text)[0])

    def test_reject_empty_corpus(self):
        self.assertTrue(validate_timelines("# 只有标题\n")[0])

    def test_repository_examples(self):
        content = (ROOT / "examples" / "behavior-regression.md").read_text(encoding="utf-8")
        errors, cases, segments = validate_timelines(content)
        self.assertEqual(errors, [])
        self.assertGreater(cases, 0)
        self.assertGreaterEqual(segments, cases)


class LinkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="xianxia-links-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.document = self.root / "SKILL.md"

    def write(self, text):
        self.document.write_text(text, encoding="utf-8")

    def test_valid_nested_reference(self):
        directory = self.root / "references"
        directory.mkdir()
        (directory / "example.md").write_text("# 示例\n", encoding="utf-8")
        self.write("[例](references/example.md)")
        self.assertEqual(validate_links(self.root), ([], 1))

    def test_missing_reference(self):
        self.write("[例](missing.md)")
        self.assertTrue(validate_links(self.root)[0])

    def test_directory_is_not_file(self):
        (self.root / "references").mkdir()
        self.write("[例](references)")
        self.assertTrue(validate_links(self.root)[0])

    def test_escape_outside_repository(self):
        self.write("[例](../outside.md)")
        self.assertTrue(validate_links(self.root)[0])

    def test_external_links_are_not_claimed_verified(self):
        self.write("[外部](https://example.invalid/a#missing)")
        self.assertEqual(validate_links(self.root), ([], 0))

    def test_same_document_heading_and_missing_heading(self):
        self.write("## 段落\n[页内](#段落) [错名](#已改名)")
        errors, checked = validate_links(self.root)
        self.assertEqual(checked, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn("#已改名", errors[0])

    def test_cross_document_heading_rename_is_detected(self):
        target = self.root / "reference.md"
        target.write_text("## 动作接续\n", encoding="utf-8")
        self.write("[接续](reference.md#动作接续)")
        self.assertEqual(validate_links(self.root), ([], 1))
        target.write_text("## 已更名\n", encoding="utf-8")
        self.assertIn("本地章节不存在", validate_links(self.root)[0][0])

    def test_encoded_heading_and_path(self):
        (self.root / "two words.md").write_text("## 中文\n", encoding="utf-8")
        self.write("[跳转](two%20words.md#%E4%B8%AD%E6%96%87)")
        self.assertEqual(validate_links(self.root), ([], 1))

    def test_duplicate_headings_and_numbered_collision(self):
        self.write("## Same\n## Same\n## Same-1\n"
                   "[一](#same) [二](#same-1) [三](#same-1-1) [缺](#same-2)")
        errors, checked = validate_links(self.root)
        self.assertEqual(checked, 4)
        self.assertEqual(len(errors), 1)
        self.assertIn("#same-2", errors[0])

    def test_fenced_examples_are_not_headings_or_links(self):
        for fence in ("```", "~~~~"):
            with self.subTest(fence=fence):
                self.write(f"{fence}md\n## 隐藏\n[示范](missing.md)\n{fence}\n"
                           "## 可见\n[正确](#可见) [错误](#隐藏)")
                errors, checked = validate_links(self.root)
                self.assertEqual(checked, 2)
                self.assertEqual(len(errors), 1)
                self.assertIn("#隐藏", errors[0])

    def test_formatted_heading_punctuation_and_closing_hashes(self):
        self.write("## **动作**、`Force` 与 _回应_！ ##\n[跳转](#动作force-与-回应)")
        self.assertEqual(validate_links(self.root), ([], 1))

    def test_local_analysis_notes_do_not_change_repository_result(self):
        reference = self.root / "references" / "public.md"
        reference.parent.mkdir()
        reference.write_text("# 公开规则\n", encoding="utf-8")
        self.write("[规则](references/public.md)")
        baseline = validate_links(self.root)
        for directory in (".git", ".local-evidence", "__pycache__",
                          "research/.local-evidence"):
            note = self.root / directory / "report.md"
            note.parent.mkdir(parents=True)
            note.write_text("[临时图片](missing.png)", encoding="utf-8")
        self.assertEqual(baseline, ([], 1))
        self.assertEqual(validate_links(self.root), baseline)

    def test_existing_local_only_note_cannot_be_a_published_reference(self):
        for directory in (".git", ".local-evidence", "__pycache__"):
            with self.subTest(directory=directory):
                target = self.root / directory / "report.md"
                target.parent.mkdir()
                target.write_text("# 仅本机资料\n", encoding="utf-8")
                self.write(f"[资料]({directory}/report.md)")
                errors, checked = validate_links(self.root)
                self.assertEqual(checked, 1)
                self.assertEqual(len(errors), 1)
                self.assertIn(f"{directory}/report.md", errors[0])

    def test_nested_reference_cannot_depend_on_local_image(self):
        target = self.root / ".local-evidence" / "frame.png"
        target.parent.mkdir()
        target.write_bytes(b"local fixture")
        article = self.root / "research" / "review.md"
        article.parent.mkdir()
        article.write_text("![画面](../.local-evidence/frame.png)", encoding="utf-8")
        self.write("[记录](research/review.md)")
        errors, checked = validate_links(self.root)
        self.assertEqual(checked, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn("../.local-evidence/frame.png", errors[0])

    def test_similar_directory_name_is_still_checked(self):
        directory = self.root / ".local-evidence-guide"
        directory.mkdir()
        (directory / "public.md").write_text("[缺失规则](missing.md)", encoding="utf-8")
        self.write("[指南](.local-evidence-guide/public.md)")
        errors, checked = validate_links(self.root)
        self.assertEqual(checked, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing.md", errors[0])

    def test_repository_local_links(self):
        errors, checked = validate_links(ROOT)
        self.assertEqual(errors, [])
        self.assertGreater(checked, 0)


if __name__ == "__main__":
    unittest.main()
