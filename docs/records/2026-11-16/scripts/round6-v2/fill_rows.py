#!/usr/bin/env python3
"""Fill a trial coverage row file: run interview-coverage --rows on it, and for each row the walk reports as asking an
unanswered question, add that question with an answer (OVERRIDES first, else the closed answer: [] for a roster, false,
then 0 if false is rejected). One engine process at a time, sequentially. Prints the answers it added.
Usage: fill_rows.py ROWS.yaml [max_rounds]   (run from the worktree root)"""
import re
import subprocess
import sys

import yaml

path = sys.argv[1]
rounds = int(sys.argv[2]) if len(sys.argv) > 2 else 60
OVERRIDES = {}
ASK = re.compile(r"row (\S+): the walk asks (\S+) \(after")
REJ = re.compile(r"row (\S+): .*?(?:rejects|rejected)[^\n]*?(\S+\.\S+)")
tried = {}
for r in range(rounds):
    out = subprocess.run(["nice", "-n", "15", "node", "engine/dist/main.js", "interview-coverage", "--rows", path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True).stdout
    doc = yaml.safe_load(open(path))
    rows = {x["id"]: x for x in doc["rows"]}
    changed = False
    for line in out.splitlines():
        m = ASK.search(line)
        if m:
            rid, q = m.group(1).rstrip(":"), m.group(2)
            rid = rid.split("row ")[-1]
            if q in rows[rid]["answers"]:
                continue
            v = OVERRIDES.get(q, [] if q.startswith("$") else False)
            rows[rid]["answers"][q] = v
            tried[(rid, q)] = v
            print(f"round {r}: {rid}: + {q} = {v}")
            changed = True
            continue
        if "rejects" in line or "rejected" in line:
            for (rid, q), v in list(tried.items()):
                if rid in line and q in line and v is False:
                    rows[rid]["answers"][q] = 0
                    tried[(rid, q)] = 0
                    print(f"round {r}: {rid}: {q} false rejected, now 0")
                    changed = True
    if not changed:
        print(out[-3000:])
        break
    yaml.safe_dump(doc, open(path, "w"), sort_keys=False, allow_unicode=True, width=120)
