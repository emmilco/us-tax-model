#!/usr/bin/env python3
"""Exclude archived blank/skip replies from class M numeric assertions (BUG-0123).

Read-only by default; --apply reclassifies derived log sections and removes only
the corresponding fixture expectations. Raw responses and model provenance stay
unchanged. Originals are archived with hashes before any write.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import classm as M
import families
from taxyear import Y

ROOT = Path(M.ROOT)
BLANK = {"", "blank", "skip", "skipped", "none", "n/a"}


def is_blank(value):
    return str(value).strip().strip("$").replace(",", "").lower() in BLANK


def raw_cases(tail):
    out = {}
    for part in re.split(r"(?m)^### ", tail)[1:]:
        case, _, body = part.partition("\n")
        body = body.strip()
        if not body.startswith("```yaml\n") or not body.endswith("```"):
            raise ValueError(f"{case}: cannot identify the archived response fences")
        out[case] = M.extract(body[len("```yaml\n"):-3].strip())
    return out


def fixture_key(handle, case, doc):
    """Resolve the recorded handle, rejecting ambiguous or unrecognized mappings."""
    if handle in case["expect"]:  # entry-level documents use full evaluator keys
        return handle
    if "[" in handle:
        return handle  # may already have been dropped by a prior ruling
    lines = doc["lines"]
    if doc.get("parameters") is not None:  # shared-definition instance
        matches = [k for k in case["expect"] if k.endswith("." + handle)]
        if len(matches) > 1:
            raise ValueError(f"ambiguous definition handle {handle}")
        if matches:
            return matches[0]
    candidates = [l["id"] for l in lines
                  if handle in (str(l["printed"]), f"{l['printed']} ({l['id']})")]
    if len(candidates) == 1:
        return candidates[0]
    raise ValueError(f"cannot map {case['id']} / {handle} to a declared line")


def reclassify(text, cases, doc):
    head, sep, rest = text.partition("\n## Lines\n")
    body, sep2, tail = rest.partition("\n## Raw responses\n")
    if not sep or not sep2:
        raise ValueError("log has no Lines or Raw responses section")
    answers = raw_cases(tail)
    parts = body.split("\n### ")
    removed, changed = [], 0
    for i in range(1, len(parts)):
        title, _, content = parts[i].partition("\n")
        bits = title.split(" — ")
        if len(bits) < 3 or bits[0] not in answers:
            continue
        cid, handle = bits[:2]
        row = answers[cid].get(handle)
        if row is None or not is_blank(row["value"]):
            continue
        if cid not in cases:
            raise ValueError(f"{cid}: no matching fixture case")
        key = fixture_key(handle, cases[cid], doc)
        if key in cases[cid]["expect"]:
            cases[cid]["expect"].pop(key)
            removed.append((cid, key))
        if not content.startswith("Status: **SKIPPED**"):
            content = ("Status: **SKIPPED**\n\nModel: blank\n"
                       f"Work: {row.get('work', '')}\n\n"
                       "No numeric assertion or class M credit: the model left this line blank.\n\n")
            parts[i] = title + "\n" + content
            changed += 1
    for cid in {cid for cid, _ in removed}:
        cases[cid]["evidence_note"] += "; BUG-0123: archived skipped replies excluded from M assertions"
    return head + sep + "\n### ".join(parts) + sep2 + tail, removed, changed


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    writes, removed, changed = {}, [], 0
    for fixture in sorted((ROOT / "fixtures" / Y).glob("classm*.json")):
        family = fixture.stem.partition(".")[2] or families.DEFAULT
        fx = json.loads(fixture.read_text())
        before = json.dumps(fx, sort_keys=True)
        for log in sorted((ROOT / "reviews" / Y / "classm").glob("*.md")):
            fid, log_family = families.split_stem(log.stem)
            if log_family != family:
                continue
            cases = {c["id"].removesuffix("." + family) if family != families.DEFAULT else c["id"]: c
                     for c in fx["cases"] if c["id"].startswith(f"classm.{fid}.")}
            result, dropped, updated = reclassify(log.read_text(), cases, M.load_form(fid))
            removed.extend(dropped)
            changed += updated
            if updated:
                writes[log] = result
        if json.dumps(fx, sort_keys=True) != before:
            writes[fixture] = json.dumps(fx, indent=2) + "\n"
    if args.apply and writes:
        archive = ROOT / ".classm" / "archive" / "blank-assertions-2026-10-24"
        manifest = {}
        for path in writes:
            relative = path.relative_to(ROOT)
            original = path.read_bytes()
            dest = archive / relative
            if dest.exists():
                raise ValueError(f"refusing to overwrite archived original: {dest}")
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(original)
            manifest[str(relative)] = hashlib.sha256(original).hexdigest()
        (archive / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        for path, text in writes.items():
            path.write_text(text)
    action = "excluded" if args.apply else "to exclude"
    print(f"class M skipped audit: {len(removed)} numeric assertions {action}; {changed} log sections reclassified")
    return 0 if args.apply or not writes else 1


if __name__ == "__main__":
    raise SystemExit(main())
