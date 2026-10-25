#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exercise the reading -> saved verdict -> signed log -> evidence-report path.

All invented verdicts and git signatures live in a temporary repository. The real
human-review directory is never used. Pass --prepare-browser DIR to keep a sandbox
for the browser smoke test instead of running the tests.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def init_git(dest):
    subprocess.run(["git", "init", "--quiet", str(dest)], check=True)
    subprocess.run(["git", "config", "user.name", "Review Test Reader"], cwd=dest, check=True)
    subprocess.run(["git", "config", "user.email", "review-test@example.invalid"], cwd=dest, check=True)
    # The isolated fixture repo must never invoke the owner's signing key or hooks.
    subprocess.run(["git", "config", "commit.gpgsign", "false"], cwd=dest, check=True)
    subprocess.run(["git", "config", "core.hooksPath", str(dest / "empty-hooks")], cwd=dest, check=True)


def sandbox(dest):
    dest.mkdir(parents=True, exist_ok=True)
    for folder in ("tools", "engine/dist", "forms", "params", "interview"):
        shutil.copytree(ROOT / folder, dest / folder, ignore=shutil.ignore_patterns("__pycache__", ".venv"))
    for folder in ("node_modules", "canonical", "fixtures", "sources", "rendered"):
        (dest / folder).symlink_to(ROOT / folder, target_is_directory=True)
    shutil.copy2(ROOT / "years.json", dest / "years.json")
    reports = dest / "reports" / "2025"
    reports.mkdir(parents=True)
    shutil.copy2(ROOT / "reports/2025/engine_differential.json", reports / "engine_differential.json")
    (dest / ".human-review").mkdir()
    if (ROOT / ".human-review/2.html").exists():
        shutil.copy2(ROOT / ".human-review/2.html", dest / ".human-review/2.html")
        (dest / ".human-review/pages").symlink_to(ROOT / ".human-review/pages", target_is_directory=True)
    (dest / ".review-test-sandbox").write_text("Synthetic human readings only.\n")
    init_git(dest)


if __name__ == "__main__" and "--in-sandbox" not in sys.argv:
    if "--prepare-browser" in sys.argv:
        dest = Path(sys.argv[sys.argv.index("--prepare-browser") + 1])
        sandbox(dest)
        print(dest)
        sys.exit(0)
    with tempfile.TemporaryDirectory(prefix="tax-human-review-test-") as temp:
        dest = Path(temp)
        sandbox(dest)
        result = subprocess.run([sys.executable, str(dest / "tools/human_review/test_review.py"), "--in-sandbox", "--year", "2025"], cwd=dest)
        sys.exit(result.returncode)

# Never create invented human evidence in the working repository.
if not (ROOT / ".review-test-sandbox").exists() or "--in-sandbox" not in sys.argv:
    raise RuntimeError("tests require the isolated review sandbox")
sys.argv.remove("--in-sandbox")
sys.path.insert(0, str(ROOT / "tools/human_review"))
import logs  # noqa: E402
import packet  # noqa: E402
import reading  # noqa: E402
import serve  # noqa: E402


class ReviewPath(unittest.TestCase):
    def setUp(self):
        shutil.rmtree(ROOT / ".git")
        init_git(ROOT)
        if logs.LOGS.exists():
            shutil.rmtree(logs.LOGS)
        packet._canon = None
        self.recs, self.orphans = packet.plan_item(packet.item(2))
        self.rec = next(r for r in self.recs if r["id"] == "sa.standardraw")
        self.log_path = logs.LOGS / (self.rec["form"] + ".md")
        self.body = {"item": 2, "reader": "Review Test Reader", "date": "2026-10-22", "lines": [{
            "ref": self.rec["ref"], "subject": logs.review_subject(self.rec), "verdict": "MATCH",
            "reason": "Synthetic test verdict. This is not a person's review of the tax rule."}]}

    def commit(self, reader="Review Test Reader"):
        subprocess.run(["git", "add", "reviews"], cwd=ROOT, check=True)
        subprocess.run(["git", "-c", f"user.name={reader}", "commit", "--quiet", "--allow-empty", "-m", "Synthetic review-path test"],
                       cwd=ROOT, check=True)

    def report(self):
        return subprocess.run(["node", str(ROOT / "engine/dist/main.js"), "--year", "2025", "evidence"],
                              cwd=ROOT, capture_output=True, text=True)

    def test_signed_match_reaches_report_without_becoming_worked_values(self):
        serve.save(self.body)
        self.assertEqual(logs.evidence()["lines"], {})
        self.assertTrue(logs.evidence()["pending"])
        self.commit()
        evidence = logs.evidence()
        self.assertFalse(evidence["problems"])
        self.assertIn("sa.standardraw", evidence["lines"])
        self.assertNotIn("sa.standardbase", evidence["lines"])
        self.assertNotIn("sa.extra_age65", evidence["lines"])
        self.assertNotIn("sa.line17", evidence["lines"])
        result = self.report()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = (ROOT / "reports/2025/evidence.md").read_text()
        self.assertIn("H (human source reading): 1", report.splitlines()[2])
        self.assertIn("B (human worked values): 0", report)
        self.assertIn("Review Test Reader", report)
        row = next(line for line in report.splitlines() if line.startswith("| sa.standardraw |"))
        self.assertIn("Review Test Reader", row)

    def test_receipt_rejects_old_browser_page(self):
        self.body["lines"][0]["subject"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "packet changed"):
            serve.save(self.body)
        self.assertFalse(logs.LOGS.exists())

    def test_cross_form_helper_edit_stales_credit_without_blocking_report(self):
        serve.save(self.body)
        self.commit()
        source = ROOT / "forms/2025/sa.yaml"
        original = source.read_bytes()
        try:
            source.write_bytes(original + b"\n# changed dependency\n")
            evidence = logs.evidence()
            self.assertFalse(evidence["problems"])
            self.assertTrue(evidence["pending"])
            self.assertFalse(evidence["lines"])
            result = self.report()
            self.assertEqual(result.returncode, 0, result.stderr)
        finally:
            source.write_bytes(original)

    def test_stale_canonical_data_cannot_make_a_new_packet(self):
        source = ROOT / "forms/2025/sa.yaml"
        original = source.read_text()
        try:
            source.write_text(original.replace("sa.standardbase", "sa.changed_standardbase"))
            with self.assertRaisesRegex(ValueError, "canonical data for sa is stale"):
                reading.Canon()
        finally:
            source.write_text(original)

    def test_old_verdict_is_not_restored_after_receipt_changes(self):
        serve.save(self.body)
        source = ROOT / "forms/2025/sa.yaml"
        original = source.read_bytes()
        try:
            source.write_bytes(original + b"\n# changed dependency\n")
            self.assertEqual(serve.saved_for_item(2)["lines"], [])
        finally:
            source.write_bytes(original)

    def test_mismatch_and_unclear_are_recorded_but_never_credited(self):
        for verdict in ("MISMATCH", "UNCLEAR"):
            self.body["lines"][0]["verdict"] = verdict
            serve.save(self.body)
            self.commit()
            original = self.log_path.read_bytes()
            evidence = logs.evidence()
            self.assertFalse(evidence["lines"])
            self.assertFalse(evidence["problems"])
            self.assertTrue(evidence["pending"])
            result = self.report()
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(self.log_path.read_bytes(), original)

    def test_reason_required_and_model_reader_rejected(self):
        self.body["lines"][0]["reason"] = ""
        with self.assertRaisesRegex(ValueError, "write your reason"):
            serve.save(self.body)
        self.body["reader"] = "GPT model"
        with self.assertRaisesRegex(ValueError, "names a model"):
            serve.save(self.body)

    def test_blank_save_does_not_erase_a_saved_reading(self):
        serve.save(self.body)
        original = self.log_path.read_bytes()
        self.body["lines"][0].update(verdict="", reason="")
        with self.assertRaisesRegex(ValueError, "no completed verdicts"):
            serve.save(self.body)
        self.assertEqual(self.log_path.read_bytes(), original)

    def test_partial_save_preserves_other_completed_lines(self):
        recs, _ = packet.plan_item(packet.item(3))
        body = {"item": 3, "reader": "Review Test Reader", "date": "2026-10-22", "lines": [
            {"ref": r["ref"], "subject": logs.review_subject(r), "verdict": "MATCH", "reason": f"Synthetic test of {r['ref']}"}
            for r in recs[:2]]}
        serve.save(body)
        original_second = serve.saved_for_item(3)["lines"][1]
        body["lines"] = [{**body["lines"][0], "reason": "A changed synthetic reason"}]
        serve.save(body)
        saved = serve.saved_for_item(3)["lines"]
        self.assertEqual(saved[0]["reason"], "A changed synthetic reason")
        self.assertEqual(saved[1], original_second)

    def test_edit_after_signing_has_no_credit(self):
        serve.save(self.body)
        self.commit()
        path = self.log_path
        path.write_text(path.read_text().replace("Synthetic test verdict.", "An edited synthetic test verdict."))
        self.assertFalse(logs.evidence()["lines"])
        self.assertTrue(logs.evidence()["pending"])

    def test_wrong_commit_author_has_no_credit(self):
        serve.save(self.body)
        self.commit("Another Test Reader")
        self.assertTrue(logs.evidence()["problems"])
        self.assertFalse(logs.evidence()["lines"])
        self.assertNotEqual(self.report().returncode, 0)

    def test_duplicate_record_still_blocks_report(self):
        serve.save(self.body)
        text = self.log_path.read_text()
        record = text[text.index("### "):]
        self.log_path.write_text(text + "\n" + record)
        evidence = logs.evidence()
        self.assertTrue(evidence["problems"])
        self.assertFalse(evidence["lines"])
        self.assertNotEqual(self.report().returncode, 0)

    def test_verbatim_multiline_reason_round_trip(self):
        reason = "Synthetic reason with | and **formatting**.\nA second line, preserved exactly."
        self.body["lines"][0]["reason"] = reason
        serve.save(self.body)
        self.assertEqual(serve.saved_for_item(2)["lines"][0]["reason"], reason)

    def test_each_question_shows_its_own_source_and_has_no_folded_tree(self):
        first = self.recs[0]
        pages = serve.line_pages(first)
        self.assertIn(2, pages["f1040"])
        self.assertEqual(set(pages), {"f1040"})
        self.assertEqual(len(self.recs), 14)
        self.assertTrue(all(not r["helpers"] for r in self.recs))
        self.assertFalse(self.orphans)

    def test_review_of_base_amounts_does_not_approve_calculations(self):
        first = self.recs[0]
        self.body["lines"] = [{"ref": first["ref"], "subject": logs.review_subject(first),
                               "verdict": "MATCH", "reason": "Synthetic test of base amounts only"}]
        serve.save(self.body)
        self.commit()
        self.assertEqual(set(logs.evidence()["lines"]), {"sa.standardbase"})

    def test_review_of_final_routing_does_not_approve_upstream_rules(self):
        last = self.recs[-1]
        self.body["lines"] = [{"ref": last["ref"], "subject": logs.review_subject(last),
                               "verdict": "MATCH", "reason": "Synthetic test of the final copy only"}]
        serve.save(self.body)
        self.commit()
        self.assertEqual(set(logs.evidence()["lines"]), {"f1040.line12e"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
