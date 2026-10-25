# SPDX-License-Identifier: Apache-2.0
"""Human source readings, kept separate from hand-calculated fixture values.

The server, log checker and evidence report share the same receipt and validation.
A receipt covers the printed line, the helpers actually shown, their dependencies,
source snapshots and the tools that produced the reading. Only current MATCH records
whose exact contents have been committed by their named reader earn H credit.
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path

import packet

ROOT = packet.ROOT
LOGS = ROOT / "reviews" / packet.Y / "human"
MODEL_NAME = re.compile(r"claude|gpt|deepseek|model|agent", re.I)
FIELDS = ("Label", "Reading", "Cite", "Pages", "Helpers folded", "Item", "Review sha256")


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


def review_subject(rec):
    """Hash the displayed reading and its source dependencies, including other forms.

    Raw input files are included as well as the displayed record: editing a helper
    invalidates a receipt even before canonical data or the packet is rebuilt.
    """
    c = packet.canon()
    ids = [rec["id"], *rec["helpers"], *rec["leaves"]]
    forms = {c.form_of[lid] for lid in ids if lid in c.form_of}
    paths = [ROOT / "forms" / packet.Y / f"{fid}.yaml" for fid in sorted(forms)]
    paths += [ROOT / "params" / f"{packet.Y}.yaml", ROOT / "interview" / f"questions-{packet.Y}.yaml"]
    if rec["form"] == "tax_table":
        paths.append(ROOT / "tables" / packet.Y / "tax_table.yaml")
    paths += [packet.HERE / f for f in ("reading.py", "packet.py", "pages.py", "logs.py", "steps.py")]
    payload = {k: rec[k] for k in ("ref", "printed", "label", "reading_text", "cite", "helpers", "leaves", "expr")}
    payload["refusals"] = [(where, node.flat(), remedy, cite) for where, node, remedy, cite in rec["refusals"]]
    payload["review_scope"] = {k: rec.get(k) for k in ("credit_lines", "source_cites", "source_window", "question", "title")}
    payload["dependencies"] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    # Include every source snapshot in the manifest. This is deliberately conservative:
    # a changed source requires rebuilding and reading a fresh packet.
    payload["sources"] = packet.manifest()
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def committed_reader(path, reader):
    """A staged or edited reading is pending until the reader signs its exact text."""
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
        header, records = parse_log(path.read_text(encoding="utf-8"))
        reader = header.get("reader", "").strip()
        problems = []
        if not reader or MODEL_NAME.search(reader):
            problems.append("the reader must be a named person")
        if not records:
            problems.append("no printed lines were judged")
        if len(re.findall(r"^### ", path.read_text(encoding="utf-8"), flags=re.M)) != len(records):
            problems.append("duplicate or malformed line records")
        accepted = []
        uncredited = []
        for lid, record in records.items():
            try:
                recs, _ = packet.plan_item(packet.item(int(record["Item"])))
                rec = next(r for r in recs if r["id"] == lid and r["form"] == path.stem)
            except (ValueError, StopIteration, SystemExit):
                uncredited.append(f"{lid}: not a printed line in the current recorded item")
                continue
            if record["Review sha256"] != review_subject(rec):
                uncredited.append(f"{lid}: the reading or a dependency changed; fresh reading required for H credit")
            if record["Helpers folded"] != (", ".join(rec["helpers"]) or "(none)"):
                uncredited.append(f"{lid}: the recorded helper list differs from the packet")
            if record["Reading"] != rec["reading_text"].replace("\n", " "):
                uncredited.append(f"{lid}: the recorded reading differs from the packet")
            if record["verdict"] != "MATCH":
                uncredited.append(f"{lid}: {record['verdict'] or 'empty verdict'}; no H credit; finding retained for investigation")
            if not record["reason"] or record["reason"] == "(empty)":
                uncredited.append(f"{lid}: no reason in the reader's own words")
            accepted.append(rec)
        try:
            signed, note = committed_reader(path, reader)
        except ValueError as e:
            problems.append(str(e))
            signed, note = False, ""
        result["problems"].extend(f"{path.stem}: {p}" for p in problems)
        result["pending"].extend(f"{path.stem}: {p}" for p in uncredited)
        if problems or uncredited:
            continue
        if not signed:
            result["pending"].append(f"{path.stem}: {reader}: {note}")
            continue
        for rec in accepted:
            credit = {"reader": reader, "log": str(path.relative_to(ROOT)), "via": rec["id"]}
            # Only helpers actually expanded in the reading inherit source-reading credit.
            # A referenced printed line is a leaf and has not been read in this packet.
            for lid in rec.get("credit_lines", [rec["id"], *rec["helpers"], *[x for x in rec["leaves"] if c_is_param(x)]]):
                result["lines"].setdefault(lid, []).append(credit)
    return result


def c_is_param(lid):
    return packet.canon().is_param(lid)


if __name__ == "__main__":
    print(json.dumps(evidence(), ensure_ascii=False))
