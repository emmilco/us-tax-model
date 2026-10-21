#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""In check-all: every second-transcription log of a pinned table (reviews/<year>/tables/*.json, written by
transcribe_tables.py) must be for the table as it is now (its hash) and have a ruling under every
disagreement; and every table that has a job must have a log."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
sys.path.insert(0, str(ROOT / "tools" / "transcription"))
from transcribe_tables import JOBS  # noqa: E402

failures = []
for name, job in sorted(JOBS.items()):
    path = ROOT / "reviews" / Y / "tables" / f"{name}.json"
    if not path.exists():
        failures.append(f"{name}: no log")
        continue
    log = json.loads(path.read_text())
    now = hashlib.sha256((ROOT / job["table"]).read_bytes()).hexdigest()
    if log["table_sha256"] != now:
        failures.append(f"{name}: {job['table']} changed after its second transcription")
    open_ = [r["key"] for r in log["results"] if r["status"] != "AGREE" and "ruling" not in r]
    if open_:
        failures.append(f"{name}: open disagreements {open_}")
    print(f"table transcription {name}: {len(log['results'])} compared, {sum(r['status'] == 'AGREE' for r in log['results'])} agree, {len(open_)} open")
for f in failures:
    print("FAIL " + f)
sys.exit(1 if failures else 0)
