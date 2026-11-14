#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Tests of the human log validation (logs.py), which check_logs.py and the evidence report share, and of the report on it.

The logs under test are copies of this repository's reviews/<year>/human/ logs with a synthetic reader, in a
temporary repository with its own git history: the repository's own logs and history are never changed.
"""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
READER = "Review Test Reader"


def init_git(dest):
    subprocess.run(["git", "init", "--quiet", str(dest)], check=True)
    subprocess.run(["git", "config", "user.name", READER], cwd=dest, check=True)
    subprocess.run(["git", "config", "user.email", "review-test@example.invalid"], cwd=dest, check=True)
    # The temporary repository must never invoke the owner's signing key or hooks.
    subprocess.run(["git", "config", "commit.gpgsign", "false"], cwd=dest, check=True)
    subprocess.run(["git", "config", "core.hooksPath", str(dest / "empty-hooks")], cwd=dest, check=True)


def sandbox(dest):
    """A repository holding copies of the tools and the engine's build, the build's inputs and outputs linked."""
    shutil.copytree(ROOT / "tools", dest / "tools", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(ROOT / "engine" / "dist", dest / "engine" / "dist")
    for folder in ("node_modules", "canonical", "fixtures", "sources", "rendered", "forms", "params", "interview"):
        (dest / folder).symlink_to(ROOT / folder, target_is_directory=True)
    for name in ("years.json", "package.json"):
        shutil.copy2(ROOT / name, dest / name)
    reviews = dest / "reviews" / "2025"
    reviews.mkdir(parents=True)
    for entry in (ROOT / "reviews" / "2025").iterdir():
        if entry.name != "human":
            (reviews / entry.name).symlink_to(entry, target_is_directory=entry.is_dir())
    (reviews / "human").mkdir()
    reports = dest / "reports" / "2025"
    reports.mkdir(parents=True)
    shutil.copy2(ROOT / "reports" / "2025" / "engine_differential.json", reports / "engine_differential.json")
    init_git(dest)


class HumanLogs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="tax-human-logs-test-")
        cls.dest = Path(cls.temp.name).resolve()
        sandbox(cls.dest)
        sys.path.insert(0, str(cls.dest / "tools" / "human_review"))
        import logs
        cls.logs = logs
        assert logs.ROOT == cls.dest, logs.ROOT

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        human = self.dest / "reviews" / "2025" / "human"
        shutil.rmtree(human)
        human.mkdir()
        shutil.rmtree(self.dest / ".git")
        init_git(self.dest)
        for log in sorted((ROOT / "reviews" / "2025" / "human").glob("*.md")):
            text = log.read_text(encoding="utf-8")
            reader = self.logs.parse_log(text)[0]["reader"]
            (human / log.name).write_text(text.replace(f"| reader | {reader} |", f"| reader | {READER} |"), encoding="utf-8")
        self.sa = human / "sa.md"

    def commit(self, author=READER):
        subprocess.run(["git", "add", "reviews"], cwd=self.dest, check=True)
        subprocess.run(["git", "-c", f"user.name={author}", "commit", "--quiet", "--allow-empty", "-m", "Synthetic human log test"],
                       cwd=self.dest, check=True)

    def report(self):
        return subprocess.run(["node", str(self.dest / "engine/dist/main.js"), "--year", "2025", "evidence"],
                              cwd=self.dest, capture_output=True, text=True)

    def test_committed_logs_are_valid_records_with_every_verdict_pending(self):
        self.commit()
        ev = self.logs.evidence()
        self.assertEqual(ev["problems"], [])
        self.assertEqual(ev["lines"], {})
        self.assertEqual(ev["logs"], len(list((ROOT / "reviews" / "2025" / "human").glob("*.md"))))
        records = sum(len(self.logs.parse_log(p.read_text(encoding="utf-8"))[1]) for p in self.sa.parent.glob("*.md"))
        self.assertEqual(sum(1 for p in ev["pending"] if self.logs.NO_RECEIPT in p), records)
        # The reader's own verdicts stay recorded and reported: a MISMATCH is listed as a finding retained.
        self.assertTrue(any("sa.extra: MISMATCH" in p for p in ev["pending"]))
        result = self.report()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = (self.dest / "reports/2025/evidence.md").read_text()
        self.assertIn("H (human source reading): 0", report)
        self.assertIn("sa.extra: MISMATCH", report)

    def test_a_signed_match_earns_no_credit(self):
        self.commit()
        _, records = self.logs.parse_log(self.sa.read_text(encoding="utf-8"))
        self.assertEqual(records["sa.standardbase"]["verdict"], "MATCH")
        self.assertNotIn("sa.standardbase", self.logs.evidence()["lines"])

    def test_wrong_commit_author_fails_the_report(self):
        self.commit("Another Test Reader")
        ev = self.logs.evidence()
        self.assertTrue(any("commit author 'Another Test Reader' is not the reader" in p for p in ev["problems"]))
        self.assertNotEqual(self.report().returncode, 0)

    def test_duplicate_record_fails_the_report(self):
        text = self.sa.read_text(encoding="utf-8")
        self.sa.write_text(text + "\n" + text[text.index("### "):], encoding="utf-8")
        self.commit()
        self.assertIn("sa: duplicate or malformed line records", self.logs.evidence()["problems"])
        self.assertNotEqual(self.report().returncode, 0)

    def test_reader_must_be_a_named_person(self):
        for reader in ("GPT model", ""):
            self.sa.write_text(self.sa.read_text(encoding="utf-8").replace(f"| reader | {READER} |", f"| reader | {reader} |"), encoding="utf-8")
            self.commit(reader or READER)
            self.assertIn("sa: the reader must be a named person", self.logs.evidence()["problems"])
            self.setUp()

    def test_log_with_no_records_is_a_problem(self):
        text = self.sa.read_text(encoding="utf-8")
        self.sa.write_text(text[:text.index("### ")], encoding="utf-8")
        self.commit()
        self.assertIn("sa: no printed lines were judged", self.logs.evidence()["problems"])

    def test_edit_after_commit_is_pending_not_a_problem(self):
        self.commit()
        self.sa.write_text(self.sa.read_text(encoding="utf-8").replace("exact match", "an edited reason"), encoding="utf-8")
        ev = self.logs.evidence()
        self.assertEqual(ev["problems"], [])
        self.assertIn(f"sa: {READER}: not yet committed with these contents", ev["pending"])

    def test_verbatim_multiline_reason_is_read_whole(self):
        reason = "Synthetic reason with | and **formatting**.\nA second line, preserved exactly."
        text = self.sa.read_text(encoding="utf-8")
        start = text.index("Reason:\n", text.index("`sa.standardbase`")) + len("Reason:\n")
        end = text.index("\n\n### ", start)
        self.sa.write_text(text[:start] + reason + text[end:], encoding="utf-8")
        self.assertEqual(self.logs.parse_log(self.sa.read_text(encoding="utf-8"))[1]["sa.standardbase"]["reason"], reason)


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "tools"))
    import taxyear  # noqa: E402  (removes --year from sys.argv)
    if taxyear.Y != "2025":
        sys.exit(f"human log tests: written for the 2025 logs (reviews/2025/human/); tax year {taxyear.Y} needs its own")
    unittest.main(verbosity=2)
