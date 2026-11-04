#!/usr/bin/env python3
"""Summarize the paid-call cost ledger (.transcription/costs.jsonl, written by transcribe.call_model).

Usage: costs.py [--by day,family,kind,form] [--since YYYY-MM-DD] [--ledger PATH] [--json]

Each group shows calls, failures, prompt characters, the reported cost (Claude) and the
estimated cost (prices.json; reported cost where the transport reports one). A call whose
model has no cited price counts in "unpriced" and adds nothing to the estimate.
"""
import argparse, json, os, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import transcribe  # noqa: E402

KEYS = {"day": lambda r: r.get("timestamp", "")[:10],
        "family": lambda r: families.family_of(r.get("model_requested") or "-"),
        "kind": lambda r: r.get("kind") or "-",
        "form": lambda r: r.get("subject") or "-",
        "model": lambda r: r.get("model_requested") or "-"}


def read(path):
    rows, bad = [], 0
    if not os.path.exists(path):
        return rows, bad
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                bad += 1   # a torn last line from an interrupted writer
    return rows, bad


def summarize(rows, by):
    groups = defaultdict(lambda: {"calls": 0, "failed": 0, "prompt_chars": 0, "reported_usd": 0.0,
                                  "estimated_usd": 0.0, "unpriced": 0, "seconds": 0.0})
    for r in rows:
        g = groups[tuple(KEYS[k](r) for k in by)]
        g["calls"] += 1
        g["failed"] += r.get("outcome") != "ok"
        g["prompt_chars"] += r.get("prompt_chars") or 0
        g["reported_usd"] += r.get("cost_usd") or 0
        if r.get("estimated_cost_usd") is None:
            g["unpriced"] += 1
        else:
            g["estimated_usd"] += r["estimated_cost_usd"]
        g["seconds"] += r.get("duration_s") or 0
    return dict(sorted(groups.items()))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--by", default="day,family,kind", help="comma-separated: " + ", ".join(KEYS))
    ap.add_argument("--since", help="only calls on or after this UTC date")
    ap.add_argument("--ledger", default=os.path.join(transcribe.RAW, transcribe.LEDGER_NAME))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    by = [k.strip() for k in a.by.split(",") if k.strip()]
    unknown = [k for k in by if k not in KEYS]
    if unknown:
        ap.error("unknown grouping: " + ", ".join(unknown))
    rows, bad = read(a.ledger)
    if a.since:
        rows = [r for r in rows if r.get("timestamp", "")[:10] >= a.since]
    groups = summarize(rows, by)
    if a.json:
        print(json.dumps([{**dict(zip(by, k)), **v} for k, v in groups.items()], indent=1))
        return
    head = (by or ["group"]) + ["calls", "failed", "prompt chars", "reported $", "estimated $", "unpriced", "minutes"]
    print("| " + " | ".join(head) + " |")
    print("|" + " --- |" * len(head))
    total = summarize(rows, []).get(())
    lines = list(groups.items()) if by else []
    if total:
        lines.append((("total",) + ("",) * (len(by) - 1) if by else ("total",), total))
    for key, g in lines:
        print("| " + " | ".join(list(key) + [str(g["calls"]), str(g["failed"]), f"{g['prompt_chars']:,}",
                                          f"{g['reported_usd']:.2f}", f"{g['estimated_usd']:.2f}", str(g["unpriced"]),
                                          f"{g['seconds'] / 60:.1f}"]) + " |")
    if bad:
        print(f"\n{bad} unreadable ledger line(s) skipped", file=sys.stderr)


if __name__ == "__main__":
    main()
