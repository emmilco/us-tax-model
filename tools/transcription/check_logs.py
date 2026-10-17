#!/usr/bin/env python3
"""Fail unless every form has a transcription-agreement log with no open ruling and
current source hashes. Runs offline in check-all; the logs themselves are produced
deliberately by transcribe.py (a network step)."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FORMS = os.path.join(ROOT, "forms", "2025")
LOGS = os.path.join(ROOT, "reviews", "2025", "transcription")
m = json.load(open(os.path.join(ROOT, "sources", "2025", "manifest.json")))
docs = {d["id"]: d for d in (m["documents"] if isinstance(m, dict) else m)}

forms = sorted(f[:-5] for f in os.listdir(FORMS) if f.endswith(".yaml"))
problems, done = [], 0
for fid in forms:
    path = os.path.join(LOGS, fid + ".md")
    if not os.path.exists(path):
        problems.append(f"{fid}: no transcription log"); continue
    text = open(path, encoding="utf-8").read()
    if "Ruling: open" in text:
        problems.append(f"{fid}: open ruling(s) in the log")
    for row in re.findall(r"^\| (\S+) \| [^|]* \| [^|]* \| [^|]* \| ([0-9a-f]{64}) \|$", text, flags=re.M):
        doc_id, sha = row
        if doc_id in docs and docs[doc_id]["text_sha256"] != sha:
            problems.append(f"{fid}: log was made against a different snapshot of {doc_id}")
    done += 1
allow_missing = os.environ.get("TRANSCRIPTION_LOGS_OPTIONAL") == "1"
missing = [p for p in problems if p.endswith("no transcription log")]
hard = [p for p in problems if not p.endswith("no transcription log")]
for p in hard:
    print(p, file=sys.stderr)
if missing:
    print(f"transcription logs: {len(forms) - len(missing)}/{len(forms)} forms logged; missing: " + ", ".join(p.split(':')[0] for p in missing))
if hard or (missing and not allow_missing):
    sys.exit(1)
print(f"transcription logs OK ({len(forms) - len(missing)} forms, no open rulings, snapshots current)")
