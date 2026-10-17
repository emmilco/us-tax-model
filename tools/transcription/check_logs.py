#!/usr/bin/env python3
"""Fail unless every form has a transcription-agreement log and a render-comparison log,
each with no open ruling, current source hashes, and rulings that agree with its sidecar. Runs offline in check-all; the logs
themselves are produced deliberately by transcribe.py and render_compare.py (network steps)."""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rulings  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FORMS = os.path.join(ROOT, "forms", "2025")
LOGS = os.path.join(ROOT, "reviews", "2025", "transcription")
m = json.load(open(os.path.join(ROOT, "sources", "2025", "manifest.json")))
docs = {d["id"]: d for d in (m["documents"] if isinstance(m, dict) else m)}

forms = sorted(f[:-5] for f in os.listdir(FORMS) if f.endswith(".yaml"))


def classm_forms():
    """Documents class M covers (as `classm-jobs` builds them): a form with a printed computed
    line; a keyed collection with a computed line other than a year constant (worked per entry);
    a shared definition (worked per instance)."""
    import yaml
    out = []
    for fid in forms:
        d = yaml.safe_load(open(os.path.join(FORMS, fid + ".yaml"), encoding="utf-8"))
        if "def" in d:
            out.append(fid); continue
        d = d.get("form")
        if not d or "lines" not in d:
            continue
        if d.get("collection"):
            if any(l["expr"].get("op") not in ("input", "param") for l in d["lines"]):
                out.append(fid)
        elif any(not str(l["printed"]).startswith("(") and l["expr"].get("op") != "input" for l in d["lines"]):
            out.append(fid)
    return out


def check(kind, logs, optional_env, expected=None):
    """One log per form under `logs`; no open ruling; every source hash current."""
    problems = []
    for fid in (expected if expected is not None else forms):
        path = os.path.join(logs, fid + ".md")
        if not os.path.exists(path):
            problems.append(f"{fid}: no {kind} log"); continue
        text = open(path, encoding="utf-8").read()
        if "Ruling: open" in text:
            problems.append(f"{fid}: open ruling(s) in the {kind} log")
        for row in re.findall(r"^\| (\S+) \| [^|]* \| [^|]* \| [^|]* \| ([0-9a-f]{64}) \|(?: [^|]* \| ([0-9a-f]{64}|-) \|)?$", text, flags=re.M):
            doc_id, sha, cols_sha = row
            if doc_id in docs and docs[doc_id]["text_sha256"] != sha:
                problems.append(f"{fid}: {kind} log was made against a different snapshot of {doc_id}")
            if doc_id in docs and cols_sha and cols_sha != "-" and docs[doc_id].get("cols_sha256") != cols_sha:
                problems.append(f"{fid}: {kind} log was made against a different reading-order text of {doc_id}")
    allow_missing = os.environ.get(optional_env) == "1"
    missing = [p for p in problems if p.endswith(f"no {kind} log")]
    hard = [p for p in problems if not p.endswith(f"no {kind} log")]
    for p in hard:
        print(p, file=sys.stderr)
    total = len(expected if expected is not None else forms)
    if missing:
        print(f"{kind} logs: {total - len(missing)}/{total} forms logged; missing: " + ", ".join(p.split(':')[0] for p in missing))
    elif not hard:
        print(f"{kind} logs OK ({total} forms, no open rulings, snapshots current)")
    return bool(hard or (missing and not allow_missing))


failed = check("transcription", LOGS, "TRANSCRIPTION_LOGS_OPTIONAL")
failed = check("render", os.path.join(ROOT, "reviews", "2025", "render"), "RENDER_LOGS_OPTIONAL") or failed
failed = check("classm", os.path.join(ROOT, "reviews", "2025", "classm"), "CLASSM_LOGS_OPTIONAL", classm_forms()) or failed
failed = bool(rulings.check()) or failed
if failed:
    sys.exit(1)
