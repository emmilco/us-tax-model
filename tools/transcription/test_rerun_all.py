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


def ledger(path, rows=(("transcribe.py", "gpt-6-astra"), ("transcribe.py", "claude-opus-5-5"))):
    """A cost ledger pricing each (tool, model) at $1 per million prompt characters."""
    with open(path, "w", encoding="utf-8") as f:
        for tool, model in rows:
            f.write(json.dumps({"tool": tool, "model_requested": model, "outcome": "ok", "estimated_cost_usd": 1.0,
                                "prompt_chars": 1_000_000, "timestamp": "2026-01-01T00:00:00+00:00"}) + "\n")
    return path


def dry(chars=1000):
    return proc(0, f"x: excerpt 10 chars\nprompt {chars:,} chars -> .transcription/x.preview.prompt.txt\n")


class UsageLimitBreaker(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.calls = []
        self.dry_calls = []
        self.ledger = ledger(os.path.join(self.temp.name, "costs.jsonl"))
        patcher = patch.object(RA, "answered", return_value="no log")
        patcher.start()
        self.addCleanup(patcher.stop)

    def fake(self, outcomes):
        """subprocess.run returning outcomes[form] for each tool call, recording the forms called; a
        --dry-run call (planning) is recorded apart and builds a 1,000-character request."""
        def run(cmd, **kw):
            form = cmd[cmd.index("--form") + 1] if "--form" in cmd else cmd[cmd.index("--doc") + 1]
            if "--dry-run" in cmd:
                self.dry_calls.append(form)
                return dry()
            self.calls.append(form)
            return outcomes.get(form, proc(0, "agree"))
        return run

    def main(self, forms, outcomes, model="gpt-6-astra", extra=()):
        summary = os.path.join(self.temp.name, "summary.json")
        argv = ["rerun_all.py", "--kinds", "transcription", "--jobs", "1", "--no-carry", "--summary", summary,
                "--ledger", self.ledger, *extra]
        if model:
            argv += ["--model", model]
        if model and not RA.families.is_active(RA.families.family_of(model)):
            argv += ["--inactive-family", RA.families.family_of(model), "--inactive-family-reason", "breaker test"]
        out = io.StringIO()
        with patch.dict(os.environ), patch.object(sys, "argv", argv), patch.object(RA, "forms_for", return_value=forms), \
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
        self.assertIn("--inactive-family gpt --inactive-family-reason 'breaker test'", out)

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
            if "--dry-run" in cmd:
                return dry()
            self.calls.append((form, "--from-response" in cmd))
            if form == "a" and "--from-response" not in cmd:
                return proc(1, "", LIMIT)
            if form == "c" and "--from-response" in cmd:
                return proc(0, "reused")
            return proc(1, "", "no saved response") if "--from-response" in cmd else proc(0, "agree")
        summary = os.path.join(self.temp.name, "summary.json")
        argv = ["rerun_all.py", "--kinds", "transcription", "--jobs", "1", "--no-carry", "--resume", "--model",
                "gpt-6-astra", "--inactive-family", "gpt", "--inactive-family-reason", "breaker test",
                "--summary", summary, "--ledger", self.ledger]
        with patch.dict(os.environ), patch.object(sys, "argv", argv), patch.object(RA, "forms_for", return_value=["a", "b", "c"]), \
                patch.object(RA.subprocess, "run", side_effect=run), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit):
                RA.main()
        self.assertEqual(self.calls, [("a", True), ("a", False), ("b", True), ("c", True)])
        rows = {r["form"]: r for r in json.loads(Path(summary).read_text())}
        self.assertTrue(rows["c"]["reused"])
        self.assertEqual(rows["b"].get("skipped"), "usage limit")

    def test_an_inactive_family_is_refused_without_the_override(self):
        argv = ["rerun_all.py", "--kinds", "transcription", "--model", "deepseek-flash", "--dry-run", "--ledger", self.ledger]
        err = io.StringIO()
        with patch.dict(os.environ), patch.object(sys, "argv", argv), patch.object(RA, "forms_for", return_value=["a"]), \
                patch.object(RA.subprocess, "run", side_effect=self.fake({})), contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit) as done:
                RA.main()
        self.assertEqual(done.exception.code, 2)
        self.assertIn("'deepseek' (deepseek-flash) is inactive", err.getvalue())
        self.assertEqual(self.dry_calls + self.calls, [])

    def test_the_override_reaches_each_tool(self):
        seen = []
        fake = self.fake({})
        def run(cmd, **kw):
            env = kw.get("env") or os.environ
            seen.append((env.get(RA.families.OVERRIDE_ENV), env.get(RA.families.OVERRIDE_REASON_ENV)))
            return fake(cmd, **kw)
        self.fake = lambda outcomes: run
        code, out, summary = self.main(["a"], {})
        self.assertEqual((code, self.calls), (0, ["a"]))
        self.assertEqual(set(seen), {("gpt", "breaker test")})  # the dry run and the paid run
        self.assertNotIn(RA.families.OVERRIDE_ENV, os.environ)  # the test's environment is restored

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


class Guards(unittest.TestCase):
    """The guards before any paid call: once per form per round, line-scoped by default, the cost
    estimate and the owner gate. No model is called (subprocess.run is replaced)."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.ledger = ledger(os.path.join(self.temp.name, "costs.jsonl"))
        self.calls, self.dry_calls = [], []

    def main(self, states, extra=(), dry_out=None, kinds="transcription"):
        """Run rerun_all over the forms of `states` ({form: answered() result}); `dry_out(cmd)` answers dry runs."""
        summary = os.path.join(self.temp.name, "summary.json")

        def run(cmd, **kw):
            form = cmd[cmd.index("--form") + 1] if "--form" in cmd else cmd[cmd.index("--doc") + 1]
            if "--dry-run" in cmd:
                self.dry_calls.append((form, cmd[cmd.index("--lines") + 1] if "--lines" in cmd else None))
                return dry_out(cmd) if dry_out else dry()
            self.calls.append((form, cmd[cmd.index("--lines") + 1] if "--lines" in cmd else None,
                               (kw.get("env") or {}).get(RA.REASON_ENV)))
            return proc(0, "agree")
        argv = ["rerun_all.py", "--kinds", kinds, "--jobs", "1", "--no-carry", "--summary", summary,
                "--ledger", self.ledger, *extra]
        out = io.StringIO()
        with patch.object(sys, "argv", argv), patch.object(RA, "forms_for", return_value=sorted(states)), \
                patch.object(RA, "answered", side_effect=lambda k, f, fam: states[f]), \
                patch.object(RA.subprocess, "run", side_effect=run), contextlib.redirect_stdout(out):
            with self.assertRaises(SystemExit) as done:
                RA.main()
        rows = json.loads(Path(summary).read_text()) if os.path.exists(summary) else None
        return done.exception.code, out.getvalue(), rows

    def test_a_log_that_answers_its_subject_is_not_rerun_unless_forced_with_a_reason(self):
        code, out, rows = self.main({"a": None, "b": "the transcription log reviewed an earlier form of b"})
        self.assertEqual(code, 0)
        self.assertEqual([c[0] for c in self.calls], ["b"])
        self.assertIn("once per form per round: 1 job(s)", out)
        self.assertEqual(self.dry_calls, [("b", "auto")])          # a is not even planned past its state
        self.calls, self.dry_calls = [], []
        code, out, rows = self.main({"a": None}, extra=("--force-rerun", "prompt policy changed"))
        self.assertEqual(self.calls, [("a", None, "prompt policy changed")])  # whole: no stale line to scope to
        self.assertEqual(rows[0]["forced"], "prompt policy changed")
        with patch.object(sys, "argv", ["rerun_all.py", "--force-rerun", " "]), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as done:
                RA.main()
        self.assertEqual(done.exception.code, 2)

    def test_line_scoped_by_default_and_whole_when_the_tool_refuses_or_when_asked(self):
        def refuse_dependent(cmd):
            if "dependent" in cmd and "--lines" in cmd:
                return proc(1, "", "SystemExit: dependent: a form with source partial-input cases is reviewed whole "
                                   "(its cases read every line)")
            return dry()
        stale = "the transcription log is stale for lines changed or not yet reviewed: 3"
        code, out, _ = self.main({"person": stale, "dependent": stale, "new": "no log"}, dry_out=refuse_dependent)
        self.assertEqual(code, 0)
        self.assertEqual(sorted(self.calls), [("dependent", None, None), ("new", None, None), ("person", "auto", None)])
        self.assertIn(("dependent", "auto"), self.dry_calls)
        self.assertIn(("dependent", None), self.dry_calls)
        self.assertNotIn(("new", "auto"), self.dry_calls)          # no log to merge into: whole at once
        self.calls, self.dry_calls = [], []
        self.main({"person": stale}, extra=("--whole",))
        self.assertEqual(self.calls, [("person", None, None)])
        self.calls = []
        self.main({"person": stale}, extra=("--lines", "person.se_line6"))
        self.assertEqual(self.calls, [("person", "person.se_line6", None)])
        self.calls = []
        self.main({"person": stale}, kinds="classm", extra=("--approve-cost", "1"))  # class M: no line scope; unpriced here
        self.assertEqual(self.calls, [("person", None, None)])

    def test_the_estimate_is_printed_and_the_gate_needs_approval_above_the_threshold(self):
        stale = "stale"
        big = lambda cmd: dry(2_000_000)  # $2.00 at $1 per million characters
        code, out, rows = self.main({"a": stale, "b": stale}, dry_out=big)
        self.assertEqual(code, 2)
        self.assertEqual(self.calls, [])                            # nothing paid
        self.assertIn("Cost estimate", out)
        self.assertIn("total $4.00 for 2 job(s); gate $3.00", out)
        self.assertIn("refused: estimated $4.00 exceeds the $3.00 gate; pass --approve-cost 4.00", out)
        self.assertIsNone(rows)
        code, out, _ = self.main({"a": stale, "b": stale}, extra=("--approve-cost", "3.50"), dry_out=big)
        self.assertEqual((code, self.calls), (2, []))
        code, out, _ = self.main({"a": stale, "b": stale}, extra=("--approve-cost", "4"), dry_out=big)
        self.assertEqual(code, 0)
        self.assertEqual(sorted(c[0] for c in self.calls), ["a", "b"])
        self.assertLess(out.index("Cost estimate"), out.index("2 runs"))
        self.calls = []
        code, out, _ = self.main({"a": stale}, dry_out=big)        # $2.00: under the gate
        self.assertEqual((code, [c[0] for c in self.calls]), (0, ["a"]))
        self.calls = []
        code, out, _ = self.main({"a": stale}, extra=("--dry-run",), dry_out=big)
        self.assertEqual((code, self.calls), (0, []))
        self.assertIn("dry run: no model called", out)

    def test_unpriced_calls_need_approval(self):
        ledger(self.ledger, rows=(("render_compare.py", "claude-opus-5-5"),))   # no transcription price
        code, out, _ = self.main({"a": "stale"})
        self.assertEqual((code, self.calls), (2, []))
        self.assertIn("no ledger price", out)
        code, out, _ = self.main({"a": "stale"}, extra=("--approve-cost", "1"))
        self.assertEqual(code, 0)
        self.assertEqual([c[0] for c in self.calls], ["a"])

    def test_prices_are_a_fit_over_recent_calls(self):
        path = os.path.join(self.temp.name, "p.jsonl")
        # Recent calls cost $0.05 plus $0.0001 a character; the five oldest and a failed call are ignored.
        rows = [{"tool": "transcribe.py", "model_requested": "deepseek-flash", "outcome": "ok",
                 "estimated_cost_usd": (99 if i < 5 else 0.05 + 0.0001 * 1000 * (i + 1)), "prompt_chars": 1000 * (i + 1),
                 "timestamp": f"2026-01-{i + 1:02d}T00:00:00+00:00"} for i in range(RA.PRICE_SAMPLE + 5)]
        rows.append({**rows[6], "outcome": "error: x", "estimated_cost_usd": 99})
        Path(path).write_text("".join(json.dumps(r) + "\n" for r in rows))
        fixed, per = RA.prices(path)[("transcribe.py", "deepseek")]
        self.assertAlmostEqual(fixed, 0.05)
        self.assertAlmostEqual(per, 0.0001)
        import spend
        self.assertAlmostEqual(spend.estimate(2000, "transcribe.py", "deepseek-flash", {("transcribe.py", "deepseek"): (fixed, per)}), 0.25)
        self.assertIsNone(spend.estimate(2000, "classm.py", "deepseek-flash", {}))
        self.assertEqual(spend.estimate(0, "classm.py", "deepseek-flash", {}), 0.0)
        self.assertEqual(spend.fit([{"prompt_chars": 10, "estimated_cost_usd": 1.0}, {"prompt_chars": 20, "estimated_cost_usd": 0.5}]),
                         (0.0, 1.5 / 30), "a negative slope falls back to the mean rate")

    def test_the_ledger_row_records_a_forced_reason(self):
        import transcribe as T
        self.assertEqual(RA.REASON_ENV, T.RERUN_REASON_ENV)
        from datetime import datetime, timezone
        raw = os.path.join(self.temp.name, "raw")
        with patch.object(T, "RAW", raw), patch.dict(os.environ, {T.RERUN_REASON_ENV: "owner asked"}):
            T.record_cost(datetime.now(timezone.utc), 1.0, "deepseek-flash", "deepseek", "P", "S", {}, "ok", "transcription", "x")
        with patch.object(T, "RAW", raw), patch.dict(os.environ, {}, clear=False):
            os.environ.pop(T.RERUN_REASON_ENV, None)
            T.record_cost(datetime.now(timezone.utc), 1.0, "deepseek-flash", "deepseek", "P", "S", {}, "ok", "transcription", "y")
        rows = [json.loads(l) for l in Path(raw, T.LEDGER_NAME).read_text().splitlines()]
        self.assertEqual([r.get("rerun_reason") for r in rows], ["owner asked", None])


if __name__ == "__main__":
    unittest.main()
