#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Move each screen review that is current on the form's own question text to the subject that shows the interview's
wording (screen_review.question_text), so the change of subject definition makes no screen due. No model call;
idempotent.

    migrate_screen_subjects.py [--jurisdiction ny] [--dry-run]

A screen's record moves only when its subject is the hash of the prompt with the line's own question text (expr.source)
where the interview's wording now stands, all else as screen_subject computes it: its samples judged the current
gated lines, pages and question text. The record gets the new subject and `subject_migrated` (the subject it had); its
samples, and its per-sample rulings and baseline entries on the old subject, move with it. A record on any other
subject is left as it is: it is due, and its next sample is run on the interview's wording. Gate records are not
touched (their subjects already hold the interview's wording, gates.subject).

The samples of a moved record were shown the form's question text, not what the filer reads; check_screens.py counts
such records, and each is sampled on the interview's wording at its next change.
"""
import argparse
import datetime
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import jurisdiction  # noqa: E402,F401  (--jurisdiction ny: reviews/ny/<year>/screens/)
import screen_review as S  # noqa: E402
import samples  # noqa: E402
import baseline_check  # noqa: E402


def source_subject(screen, gated, lines, mani):
    """The screen's subject with the line's own question text in place of the interview's wording."""
    source = (lines[screen][1].get("expr") or {}).get("source", "")
    prompt, _ = S.prompt_for(screen, gated, lines, mani, with_gate=False, question=source)
    return hashlib.sha256(prompt.encode()).hexdigest()


def plan(lines, mani, records):
    """{screen: (old subject, new subject)} of the records to move, and {screen: why} of those left."""
    moves, left = {}, {}
    for screen, gated in S.screens(lines).items():
        rec = records.get(screen)
        new = S.screen_subject(screen, gated, lines, mani)
        if not rec:
            left[screen] = "never reviewed"
        elif rec.get("subject_sha") == new:
            left[screen] = "already on the interview's wording"
        elif rec.get("subject_sha") == source_subject(screen, gated, lines, mani):
            moves[screen] = (rec["subject_sha"], new)
        else:
            left[screen] = "due: its record is on another subject"
    return moves, left


def apply(moves, rows, rulings, today):
    """Rewrite the records (rows of screen_review.json) and the rulings file's data in place; the counts moved."""
    n = {"records": 0, "rulings": 0, "baseline": 0}
    for r in rows:
        if r.get("screen") in moves:
            old, new = moves[r["screen"]]
            r["subject_sha"] = new
            r["subject_migrated"] = {"from": old, "date": today}
            n["records"] += 1
    for key, ruling in (rulings.get("rulings") or {}).items():
        unit = samples.unit_of(key) if key.startswith("unruled:") else None
        if unit in moves and isinstance(ruling, dict) and ruling.get("subject_sha") == moves[unit][0]:
            ruling["subject_sha"] = moves[unit][1]
            n["rulings"] += 1
    baseline = rulings.get("baseline") or {}
    for key, h in list(baseline.items()):
        unit = samples.unit_of(key) if key.startswith("unruled:") else None
        if unit in moves and h == baseline_check.subject_hash({"subject": moves[unit][0]}, {}):
            baseline[key] = baseline_check.subject_hash({"subject": moves[unit][1]}, {})
            n["baseline"] += 1
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="report what would move; write nothing")
    a = ap.parse_args()
    import build_fresh
    build_fresh.require(rendered=True)  # the subjects hold the built interview's wording and the rendered English
    record_path = os.path.join(S.OUT, "screen_review.json")
    rulings_path = os.path.join(S.OUT, "rulings.json")
    S.read_records(record_path)  # refuses a file in the single-review format
    rows = json.load(open(record_path, encoding="utf-8")) if os.path.exists(record_path) else []
    rulings = json.load(open(rulings_path, encoding="utf-8")) if os.path.exists(rulings_path) else {}
    moves, left = plan(S.load_lines(), S.manifest(), {r["screen"]: r for r in rows})
    for screen, why in sorted(left.items()):
        print(f"  left: {screen}: {why}")
    n = apply(moves, rows, rulings, datetime.date.today().isoformat())
    print(f"{n['records']} record(s) moved to the interview's wording, {n['rulings']} ruling(s) and "
          f"{n['baseline']} baseline entr(ies) with them; {len(left)} left" + (" (dry run: nothing written)" if a.dry_run else ""))
    if a.dry_run or not moves:
        return
    with open(record_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    if rulings:
        with open(rulings_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(rulings, indent=1) + "\n")


if __name__ == "__main__":
    main()
