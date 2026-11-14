# SPDX-License-Identifier: Apache-2.0
"""Human source readings (reviews/<year>/human/<form>.md), kept separate from hand-calculated fixture values.

check_logs.py and the engine's evidence report share this validation. A log is a record: its header names
the reader, and each `### <printed> — `<line id>`` section holds one line's reading, receipt, verdict and the
reader's reason verbatim. Record problems fail both callers: a reader that is not a named person, a log with no
line records, duplicate or malformed records, and a committed log whose last commit's author is not its reader.

H credit needs a current receipt: the hash, over the reading as displayed and its dependencies, that the
reading tool issued when the line was read. No tool issues receipts (the reading packets and their renderer are
retired), so no receipt can be current and no line earns H. Every record is listed as pending, with its verdict
and its reason as the reader wrote them; the logs are kept as they are.

    logs.py [--year N]      the result as JSON: {"lines": {}, "pending": [...], "problems": [...], "logs": N}
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402

LOGS = ROOT / "reviews" / Y / "human"
MODEL_NAME = re.compile(r"claude|gpt|deepseek|model|agent", re.I)
FIELDS = ("Label", "Reading", "Cite", "Pages", "Helpers folded", "Item", "Review sha256")
NO_RECEIPT = "no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit"


def parse_log(text):
    header = dict(re.findall(r"^\| ([a-z /0-9]+) \| (.*) \|$", text, flags=re.M))
    records = {}
    for m in re.finditer(r"^### (.*?) — `([^`]+)`\n(.*?)(?=^### |\Z)", text, flags=re.M | re.S):
        body = m.group(3)
        fields = dict(re.findall(r"^([A-Z][A-Za-z0-9 ]+): (.*)$", body, flags=re.M))
        reason = re.search(r"^Reason:\n(.*)\Z", body, flags=re.M | re.S)
        verdict = re.fullmatch(r"\*\*(MATCH|MISMATCH|UNCLEAR)\*\*", fields.get("Verdict", ""))
        records[m.group(2)] = {"printed": m.group(1), **{f: fields.get(f, "") for f in FIELDS},
                               "verdict": verdict.group(1) if verdict else "",
                               "reason": reason.group(1).strip() if reason else ""}
    return header, records


def committed_reader(path, reader):
    """Whether the log's exact contents are committed, and a note when not; raises when the last
    commit of the log was authored by someone other than its reader."""
    rel = str(path.relative_to(ROOT))
    old = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True)
    if old.returncode or old.stdout != path.read_bytes():
        return False, "not yet committed with these contents"
    author = subprocess.run(["git", "log", "-1", "--format=%an", "--", rel],
                            cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    if author != reader:
        raise ValueError(f"commit author {author!r} is not the reader {reader!r}")
    return True, ""


def evidence():
    result = {"lines": {}, "pending": [], "problems": [], "logs": 0}
    for path in sorted(LOGS.glob("*.md")):
        result["logs"] += 1
        text = path.read_text(encoding="utf-8")
        header, records = parse_log(text)
        reader = header.get("reader", "").strip()
        problems = []
        if not reader or MODEL_NAME.search(reader):
            problems.append("the reader must be a named person")
        if not records:
            problems.append("no printed lines were judged")
        if len(re.findall(r"^### ", text, flags=re.M)) != len(records):
            problems.append("duplicate or malformed line records")
        pending = []
        for lid, record in records.items():
            pending.append(f"{lid}: {NO_RECEIPT}")
            if record["verdict"] != "MATCH":
                pending.append(f"{lid}: {record['verdict'] or 'empty verdict'}; no H credit; finding retained for investigation")
            if not record["reason"] or record["reason"] == "(empty)":
                pending.append(f"{lid}: no reason in the reader's own words")
        try:
            signed, note = committed_reader(path, reader)
        except ValueError as e:
            problems.append(str(e))
            signed, note = True, ""
        if not signed:
            pending.append(f"{reader}: {note}")
        result["problems"].extend(f"{path.stem}: {p}" for p in problems)
        result["pending"].extend(f"{path.stem}: {p}" for p in pending)
    return result


if __name__ == "__main__":
    print(json.dumps(evidence(), ensure_ascii=False))
