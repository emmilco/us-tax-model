#!/usr/bin/env python3
"""Fail unless the agent-run ledger's rows carry their required fields.

    check_agent_runs.py [--file PATH] [--pending PATH]
                                          validate research/costs/agent_runs.jsonl (or PATH)
    check_agent_runs.py --self-test

A row dated on or after CUTOFF must have `model` (a non-empty string), `class` ("mechanical" or
"judgment"), `year` (an integer tax year) and `jurisdiction` ("us" or "ny"). Earlier rows are exempt, but
a `year` or `jurisdiction` they do carry must still be well formed. Every line must be a JSON object
with a `date` (YYYY-MM-DD).

It also warns, without failing, when the hook's untracked pending file (<git common dir>/agent-runs/pending.jsonl,
tools/claude_hooks/agents.py) holds finished rows dated before yesterday: rows that tools/agent_runs_fold.py, run
by tools/check_all.sh on next or in the main worktree on main, has not yet moved into the ledger.
"""
import argparse
import datetime
import json
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "claude_hooks"))
import agents  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "research" / "costs" / "agent_runs.jsonl"
CUTOFF = "2026-11-10"
CLASSES = ("mechanical", "judgment")
JURISDICTIONS = ("us", "ny")


def problems(text, cutoff=CUTOFF):
    """A list of "line N: ..." messages for the ledger text."""
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as ex:
            out.append(f"line {n}: not JSON ({ex.msg})")
            continue
        if not isinstance(row, dict):
            out.append(f"line {n}: not a JSON object")
            continue
        date = row.get("date")
        if not isinstance(date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            out.append(f"line {n}: `date` must be YYYY-MM-DD")
            continue
        year, jur = row.get("year"), row.get("jurisdiction")
        if "year" in row and (not isinstance(year, int) or isinstance(year, bool)):
            out.append(f"line {n}: `year` must be an integer, got {year!r}")
        if "jurisdiction" in row and jur not in JURISDICTIONS:
            out.append(f"line {n}: `jurisdiction` must be one of {', '.join(JURISDICTIONS)}, got {jur!r}")
        if date < cutoff:
            continue
        if not isinstance(row.get("model"), str) or not row["model"]:
            out.append(f"line {n}: `model` is required on rows dated {cutoff} or later")
        if row.get("class") not in CLASSES:
            out.append(f"line {n}: `class` must be one of {', '.join(CLASSES)} on rows dated {cutoff} or later")
        for key in ("year", "jurisdiction"):
            if key not in row:
                out.append(f"line {n}: `{key}` is required on rows dated {cutoff} or later")
    return out


def stale_pending(path, today=None):
    """The number of finished rows in the pending file at path dated before yesterday (0 when it is absent)."""
    cutoff = ((today or datetime.date.today()) - datetime.timedelta(days=1)).isoformat()
    try:
        rows = agents.read_rows(str(path))
    except (OSError, json.JSONDecodeError):
        return 0
    return sum(1 for r in rows if agents.is_finished(r) and str(r.get("date", "")) < cutoff)


def self_test():
    ok = {"date": "2026-11-10", "model": "claude-sonnet-5-5", "class": "mechanical", "year": 2025, "jurisdiction": "us"}
    line = lambda r: json.dumps(r) + "\n"
    old = {"date": "2026-11-09", "package": "p"}

    def check(label, text, want):
        got = problems(text)
        if bool(got) != want:
            sys.exit(f"check_agent_runs self-test: {label}: expected {'problems' if want else 'none'}, got {got}")
        return got

    check("complete row", line(ok), False)
    check("older row without any field is exempt", line(old), False)
    check("blank lines are ignored", "\n" + line(ok), False)
    for missing in ("model", "class", "year", "jurisdiction"):
        got = check(f"missing {missing}", line({k: v for k, v in ok.items() if k != missing}), True)
        if f"`{missing}`" not in got[0]:
            sys.exit(f"check_agent_runs self-test: missing {missing} reported as {got}")
    check("year as a string", line({**ok, "year": "2025"}), True)
    check("year as a boolean", line({**ok, "year": True}), True)
    check("unknown jurisdiction", line({**ok, "jurisdiction": "ca"}), True)
    check("unknown class", line({**ok, "class": "other"}), True)
    check("malformed field on an exempt row", line({**old, "year": "x"}), True)
    check("torn line", '{"date": "2026-11-10"', True)
    check("no date", line({k: v for k, v in ok.items() if k != "date"}), True)
    if not problems(line(old), cutoff="2026-11-09"):
        sys.exit("check_agent_runs self-test: a row on the cutoff date must be checked")
    with tempfile.TemporaryDirectory() as d:
        path = Path(d, "agent_runs.jsonl")
        path.write_text(line(old) + line(ok))
        if main(["--file", str(path)]) != 0:
            sys.exit("check_agent_runs self-test: a valid file must pass")
        path.write_text(line(old) + line({**ok, "jurisdiction": "ca"}))
        if main(["--file", str(path)]) != 1:
            sys.exit("check_agent_runs self-test: an invalid file must fail")
        pending = Path(d, "pending.jsonl")
        done = {**ok, "tool_uses": 1}
        today = datetime.date(2026, 11, 12)
        if stale_pending(pending, today) != 0:
            sys.exit("check_agent_runs self-test: an absent pending file must give no warning")
        pending.write_text(line(done) + line({**done, "date": "2026-11-11"}) + line({**ok, "date": "2026-11-01"})
                           + line({**done, "date": "2026-11-12"}))
        if stale_pending(pending, today) != 1:
            sys.exit("check_agent_runs self-test: only finished pending rows dated before yesterday are stale")
        path.write_text(line(ok))
        if main(["--file", str(path), "--pending", str(pending)]) != 0:
            sys.exit("check_agent_runs self-test: stale pending rows must warn, not fail")
    print("check_agent_runs self-test OK")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", default=str(LEDGER))
    ap.add_argument("--pending", default=None, help="the hook's pending file (default: the clone's)")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        self_test()
        return 0
    pending = a.pending or agents.pending(str(ROOT))
    stale = stale_pending(pending) if Path(pending).resolve() != LEDGER.resolve() else 0
    if stale:
        print(f"warning: {pending} holds {stale} finished agent-run row(s) dated before yesterday; fold them into the "
              "ledger with tools/agent_runs_fold.py (on next, or in the main worktree on main) or a check-all run there",
              file=sys.stderr)
    found = problems(Path(a.file).read_text(encoding="utf-8"))
    for p in found:
        print(f"{a.file}: {p}", file=sys.stderr)
    if found:
        return 1
    print(f"agent runs OK (rows dated {CUTOFF} or later carry model, class, year, jurisdiction)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
