#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Second transcription of pinned tables: a model that sees only the archived layout text of the
pages a table comes from transcribes it, and the transcription is compared cell by cell with the
project's table. The committed artifact is reviews/2025/tables/<job>.json: the table's hash,
every comparison, and a ruling under each disagreement (written with --rule).

Isolation is that of tools/transcription (README): claude -p with no tools, no settings, no
session persistence and a task-only system prompt; the response is parsed as YAML and compared;
it drives no write path.

    python3 tools/transcription/transcribe_tables.py --job class_lives
    python3 tools/transcription/transcribe_tables.py --job macrs_mq --dry-run
    python3 tools/transcription/transcribe_tables.py --job class_lives --from-response
    python3 tools/transcription/transcribe_tables.py --job class_lives --rule rulings.json   # {"<key>": "Ruling: ..."}
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "transcription"))
from transcribe import call_model  # noqa: E402

ARCHIVE = ROOT / "sources" / "2025"
LOGS = ROOT / "reviews" / "2025" / "tables"
WORK = ROOT / ".transcription" / "tables"
SYSTEM = ("You transcribe tables from IRS publications from the text given to you. "
          "You have no tools and no other sources. Output only the YAML requested.")

JOBS = {
    "class_lives": {
        "table": "tables/2025/class_lives.yaml",
        "doc": "p946",
        "pages": list(range(99, 109)),
        "ask": (
            "Below is the layout text (pdftotext -layout) of pages 99 to 108 of IRS Publication 946 (2025), "
            "Appendix B, Tables B-1 and B-2, Table of Class Lives and Recovery Periods. Transcribe every row that "
            "has an asset class number (such as 00.11 or 57.0). For each, give: asset_class (as printed), "
            "class_life (the number in the Class Life column, or null if none is printed for that class), "
            "gds (the number in the GDS (MACRS) column), ads (the number in the ADS column), and footnotes: a list "
            "of footnote numbers printed as superscripts in that row, each with the column it is attached to "
            "(description, class_life, gds or ads). A superscript in this text is printed as a digit joined to "
            "the end of a number or word, so read it with care: for example a GDS of 7 with footnote 4 may appear "
            "as 74. Do not include the lettered paragraphs A to F at the end of Table B-2. Output YAML only: "
            "a list under the key rows, each item {asset_class, class_life, gds, ads, footnotes: [{number, column}]}."
        ),
    },
    "macrs_mq": {
        "table": "tables/2025/macrs_gds.yaml",
        "doc": "p946",
        "pages": [71, 72, 73],
        "ask": (
            "Below is the layout text of pages 71 to 73 of IRS Publication 946 (2025), Appendix A, Tables A-1 to A-5 "
            "(MACRS, 3- to 20-year property). Transcribe two columns exactly as printed: the 7-year column of Table A-3 "
            "(mid-quarter convention, placed in service in second quarter) and the 20-year column of Table A-2 "
            "(mid-quarter convention, placed in service in first quarter). For each, list every year and its rate as "
            "printed (a decimal string without the % sign, keeping every printed digit, such as \"17.85\" or \"7.000\"). "
            "Output YAML only: {a3_7year: [{year, rate}], a2_20year: [{year, rate}]}."
        ),
    },
}


def extract_yaml(text):
    """The last fenced YAML block of a response, or the whole response when it has none."""
    blocks = re.findall(r"```(?:ya?ml)?\s*\n(.*?)```", text, re.S)
    return blocks[-1] if blocks else text


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def excerpt(job):
    pages = (ARCHIVE / f"{job['doc']}.txt").read_text(encoding="utf-8").split("\f")
    return "\n".join(f"=== page {n} ===\n{pages[n - 1]}" for n in job["pages"])


def ours(name):
    if name == "class_lives":
        rows = json.loads(subprocess.run([sys.executable, str(ROOT / "tools" / "extract_class_lives.py"), "--json"],
                                         capture_output=True, text=True, check=True).stdout)
        out = {}
        for r in rows:
            marks = {m.split()[0] for m in r["marks"] if "footnote" in m}
            out[r["code"]] = {"class_life": r["life"], "gds": r["gds"], "ads": r["ads"],
                              "footnoted": sorted(marks | ({"ads"} if r.get("ads_footnote") else set()))}
        return out
    t = yaml.safe_load((ROOT / JOBS[name]["table"]).read_text())["table"]["rows"]
    pick = {("y7", "mq2"): "a3_7year", ("y20", "mq1"): "a2_20year"}
    out = {}
    for r in t:
        p, c, y = r["keys"]
        if (p, c) in pick:
            out[f"{pick[(p, c)]}/{y}"] = Fraction(r["value"]["num"], r["value"]["den"])
    return out


def norm(v):
    return None if v in (None, "", "null") else str(v).strip()


def compare(name, theirs):
    mine = ours(name)
    results = []
    if name == "class_lives":
        got = {}
        for r in (theirs or {}).get("rows", []):
            got[str(r.get("asset_class")).strip()] = r
        for code, m in sorted(mine.items()):
            t = got.get(code)
            if t is None:
                results.append({"key": code, "status": "MISSING", "ours": m, "theirs": None})
                continue
            cols = {c.get("column") for c in (t.get("footnotes") or [])}
            tf = sorted({"description" if c == "description" else ("class" if c == "class_life" else c) for c in cols})
            mf = sorted({"description" if x == "description" else ("class" if x == "class" else x) for x in m["footnoted"]})
            same = all(norm(m[k]) == norm(t.get(k)) for k in ("class_life", "gds", "ads")) and bool(tf) == bool(mf)
            results.append({"key": code, "status": "AGREE" if same else "DISAGREE",
                            "ours": m, "theirs": {k: t.get(k) for k in ("class_life", "gds", "ads", "footnotes")}})
        for code in sorted(set(got) - set(mine)):
            results.append({"key": code, "status": "EXTRA", "ours": None, "theirs": got[code]})
    else:
        got = {}
        for col in ("a3_7year", "a2_20year"):
            for r in (theirs or {}).get(col, []):
                got[f"{col}/{int(r['year'])}"] = str(r["rate"])
        for key, v in sorted(mine.items()):
            t = got.get(key)
            tv = Fraction(t) / 100 if t is not None else None
            results.append({"key": key, "status": "MISSING" if t is None else ("AGREE" if tv == v else "DISAGREE"),
                            "ours": f"{float(v) * 100:g}", "theirs": t})
    return results


def log_path(name):
    return LOGS / f"{name}.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True, choices=sorted(JOBS))
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--from-response", action="store_true")
    ap.add_argument("--rule")
    a = ap.parse_args()
    job = JOBS[a.job]
    WORK.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    if a.rule:
        log = json.loads(log_path(a.job).read_text())
        rulings = json.loads(Path(a.rule).read_text())
        for r in log["results"]:
            if r["status"] != "AGREE" and r["key"] in rulings:
                r["ruling"] = rulings[r["key"]]
        log_path(a.job).write_text(json.dumps(log, indent=1, ensure_ascii=False) + "\n")
        open_ = [r["key"] for r in log["results"] if r["status"] != "AGREE" and "ruling" not in r]
        print(f"{a.job}: {len(open_)} open")
        return
    prompt = job["ask"] + "\n\n" + excerpt(job)
    resp_file = WORK / f"{a.job}.response.txt"
    if a.dry_run:
        print(prompt[:3000])
        print(f"... {len(prompt)} characters")
        return
    if a.from_response:
        text = resp_file.read_text(encoding="utf-8")
        meta = json.loads((WORK / f"{a.job}.meta.json").read_text())
    else:
        text, meta = call_model(prompt, a.model, system=SYSTEM)
        resp_file.write_text(text, encoding="utf-8")
        (WORK / f"{a.job}.meta.json").write_text(json.dumps(meta, indent=1))
    theirs = yaml.safe_load(extract_yaml(text))
    results = compare(a.job, theirs)
    old = json.loads(log_path(a.job).read_text()) if log_path(a.job).exists() else {"results": []}
    kept = {r["key"]: r for r in old["results"] if "ruling" in r}
    for r in results:
        k = kept.get(r["key"])
        if k and k["status"] == r["status"] and k.get("ours") == r.get("ours") and k.get("theirs") == r.get("theirs"):
            r["ruling"] = k["ruling"]
    log = {"job": a.job, "table": job["table"], "table_sha256": sha(job["table"]),
           "source": {"doc": job["doc"], "pages": job["pages"], "sha256": sha(f"sources/2025/{job['doc']}.txt")},
           "model": a.model, "model_reported": meta.get("model_reported"), "cost_usd": meta.get("cost_usd"),
           "system_prompt": SYSTEM, "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
           "date": datetime.date.today().isoformat(), "results": results}
    log_path(a.job).write_text(json.dumps(log, indent=1, ensure_ascii=False, default=str) + "\n")
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(f"{a.job}: {counts}; cost {meta.get('cost_usd')} -> {os.path.relpath(log_path(a.job), ROOT)}")


if __name__ == "__main__":
    main()
