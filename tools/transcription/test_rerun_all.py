#!/usr/bin/env python3
"""Offline tests of rerun_all.py's usage-limit breaker; no model is called (subprocess.run is replaced)."""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rerun_all as RA

LIMIT = ('Traceback (most recent call last):\nRuntimeError: codex exited 1: {"type":"turn.started"}\n'
         '{"type":"error","message":"You’ve hit your usage limit. Upgrade to Pro"}\n')


def proc(code, stdout="", stderr=""):
    return SimpleNamespace(returncode=code, stdout=stdout, stderr=stderr)


class UsageLimitBreaker(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.calls = []

    def fake(self, outcomes):
        """subprocess.run returning outcomes[form] for each tool call, recording the forms called."""
        def run(cmd, **kw):
            form = cmd[cmd.index("--form") + 1] if "--form" in cmd else cmd[cmd.index("--doc") + 1]
            self.calls.append(form)
            return outcomes.get(form, proc(0, "agree"))
        return run

    def main(self, forms, outcomes, model="gpt-6-astra", extra=()):
        summary = os.path.join(self.temp.name, "summary.json")
        argv = ["rerun_all.py", "--kinds", "transcription", "--jobs", "1", "--no-carry", "--summary", summary, *extra]
        if model:
            argv += ["--model", model]
        out = io.StringIO()
        with patch.object(sys, "argv", argv), patch.object(RA, "forms_for", return_value=forms), \
                patch.object(RA.subprocess, "run", side_effect=self.fake(outcomes)), contextlib.redirect_stdout(out):
            with self.assertRaises(SystemExit) as done:
                RA.main()
        return done.exception.code, out.getvalue(), json.loads(Path(summary).read_text())

    def test_first_usage_limit_stops_the_family_and_lists_the_jobs_to_rerun(self):
        code, out, summary = self.main(["a", "b", "c", "d"], {"b": proc(1, "", LIMIT)})
        self.assertEqual(self.calls, ["a", "b"])            # no call after the first usage-limit failure
        self.assertEqual(code, 1)
        skipped = sorted(r["form"] for r in summary if r.get("skipped") == "usage limit")
        self.assertEqual(skipped, ["c", "d"])
        self.assertIn("2 not run after a usage limit", out)
        self.assertIn("gpt transcription (3): b, c, d", out)
        self.assertIn("rerun_all.py --kinds transcription --forms b,c,d", out)
        self.assertIn("--model gpt-6-astra", out)

    def test_an_ordinary_failure_does_not_open_the_breaker(self):
        code, out, summary = self.main(["a", "b", "c"], {"a": proc(1, "", "RuntimeError: codex exited 1: HTTP 504"),
                                                         "b": proc(1, "", "Input exceeds the maximum length")})
        self.assertEqual(self.calls, ["a", "b", "c"])
        self.assertEqual(code, 1)
        self.assertNotIn("usage limit", out.lower().replace("not run after a usage limit", ""))
        self.assertFalse(any(r.get("skipped") for r in summary))

    def test_resume_reuse_still_runs_after_the_breaker_opens(self):
        # With --resume each job first tries its saved response (--from-response, no model call).
        def run(cmd, **kw):
            form = cmd[cmd.index("--form") + 1]
            self.calls.append((form, "--from-response" in cmd))
            if form == "a" and "--from-response" not in cmd:
                return proc(1, "", LIMIT)
            if form == "c" and "--from-response" in cmd:
                return proc(0, "reused")
            return proc(1, "", "no saved response") if "--from-response" in cmd else proc(0, "agree")
        summary = os.path.join(self.temp.name, "summary.json")
        argv = ["rerun_all.py", "--kinds", "transcription", "--jobs", "1", "--no-carry", "--resume", "--model",
                "gpt-6-astra", "--summary", summary]
        with patch.object(sys, "argv", argv), patch.object(RA, "forms_for", return_value=["a", "b", "c"]), \
                patch.object(RA.subprocess, "run", side_effect=run), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit):
                RA.main()
        self.assertEqual(self.calls, [("a", True), ("a", False), ("b", True), ("c", True)])
        rows = {r["form"]: r for r in json.loads(Path(summary).read_text())}
        self.assertTrue(rows["c"]["reused"])
        self.assertEqual(rows["b"].get("skipped"), "usage limit")

    def test_other_families_continue(self):
        breaker = RA.Breaker()
        breaker.trip("gpt", "transcription a")
        with patch.object(RA.subprocess, "run", side_effect=self.fake({})):
            gpt = RA.run("transcription", "x", "gpt-6-astra", carry=False, breaker=breaker)
            claude = RA.run("transcription", "y", "claude-opus-5-5", carry=False, breaker=breaker)
            deepseek = RA.run("transcription", "z", "deepseek-flash", carry=False, breaker=breaker)
        self.assertEqual(gpt.get("skipped"), "usage limit")
        self.assertEqual((claude["exit"], deepseek["exit"]), (0, 0))
        self.assertEqual(self.calls, ["y", "z"])

    def test_usage_limit_messages_of_each_transport(self):
        for text in ("You’ve hit your usage limit. Upgrade to Pro", "Claude AI usage limit reached|1762300000",
                     "5-hour limit reached ∙ resets 3pm", "You've hit your limit · resets 3pm",
                     'deepseek HTTP 402: {"error":{"message":"Insufficient Balance"}}'):
            self.assertRegex(text, RA.USAGE_LIMIT)
        for text in ("deepseek HTTP 429: rate limited", "codex exited 1: HTTP 504", "claude exited 1: timeout",
                     "Input exceeds the maximum length of 1048576 characters", "output token limit"):
            self.assertNotRegex(text, RA.USAGE_LIMIT)


if __name__ == "__main__":
    unittest.main()
