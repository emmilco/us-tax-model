#!/usr/bin/env python3
"""Fail unless every form has a transcription-agreement log and a render-comparison log from
every required model family (families.json), each with no open ruling, current source hashes, an
unchanged subject (what the review judged: subjects.py), and rulings that agree with its sidecar.
An optional family's logs may be missing; those present are held to the same source and subject
checks, and their open rulings are counted and printed without failing the run. A log whose family
is in neither list fails. Counts are printed per kind and family. Runs offline in check-all; the logs
themselves are produced deliberately by transcribe.py and render_compare.py (network steps).

When reports/<year>/second_family.md exists (compare_families.py), its summary line is printed.

Optional human reading logs (reviews/<year>/human/) earn H only with a current receipt,
MATCH and reason, and exact contents committed by the named reader. Incomplete, stale or
negative readings are pending without failing this check. Malformed/duplicate records and
invalid identity or committed authorship remain failures (owner amendment 2026-10-24)."""
import json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings  # noqa: E402
import subjects  # noqa: E402
import compare_families  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
FORMS = os.path.join(ROOT, "forms", Y)
REVIEWS = os.path.join(ROOT, "reviews", Y)
SECOND_FAMILY_REPORT = os.path.join(ROOT, "reports", Y, "second_family.md")
m = json.load(open(os.path.join(ROOT, "sources", Y, "manifest.json")))
docs = {d["id"]: d for d in (m["documents"] if isinstance(m, dict) else m)}

forms = sorted(f[:-5] for f in os.listdir(FORMS) if f.endswith(".yaml"))


# Documents class M cannot work because no return has an entry of them, with the reason; each is
# printed on every run so the gap stays visible.
CLASSM_NO_ENTRIES: dict[str, str] = {}


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
    for fid, why in CLASSM_NO_ENTRIES.items():
        if fid in out:
            out.remove(fid)
            print(f"classm: {fid} not expected: {why}")
    return out


def check(kind, logs, optional_env, expected=None, family=families.DEFAULT, required=True):
    """One log per form of the family under `logs`; no open ruling; every source hash current;
    the subject it reviewed (subjects.py) unchanged. For an optional family a missing log is
    allowed and open rulings are counted, not failed."""
    problems, open_counts = [], {}
    tag = f"{kind} logs [{family}{'' if required else ', optional'}]"
    for fid in (expected if expected is not None else forms):
        path = os.path.join(logs, families.stem(fid, family) + ".md")
        if not os.path.exists(path):
            problems.append(f"{fid}: no {kind} log"); continue
        text = open(path, encoding="utf-8").read()
        if family != families.DEFAULT and os.path.exists(os.path.join(logs, fid + ".md")):
            quality = compare_families.compare(kind, fid, family)["quality"]
            if quality["state"] == "pending":
                note = f"{fid}: second-family review not eligible: " + "; ".join(quality["blockers"])
                if required:
                    problems.append(note)
                else:
                    print(f"[{family}, optional] {note}")
        if "Ruling: open" in text:
            open_counts[fid] = text.count("Ruling: open")
            if required:
                problems.append(f"{fid}: open ruling(s) in the {kind} log")
        subject = re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", text, flags=re.M)
        if not subject:
            problems.append(f"{fid}: the {kind} log records no subject hash (tools/transcription/subjects.py)")
        elif subject.group(1) != subjects.current(kind, fid, Y):
            what = {"transcription": "form", "render": "rendered English", "classm": "computation"}[kind]
            problems.append(f"{fid}: the {kind} log reviewed an earlier {what} of {fid}; rerun the review")
        for row in re.findall(r"^\| (\S+) \| [^|]* \| [^|]* \| [^|]* \| ([0-9a-f]{64}) \|(?: [^|]* \| ([0-9a-f]{64}|-) \|)?$", text, flags=re.M):
            doc_id, sha, cols_sha = row
            if doc_id in docs and docs[doc_id]["text_sha256"] != sha:
                problems.append(f"{fid}: {kind} log was made against a different snapshot of {doc_id}")
            if doc_id in docs and cols_sha and cols_sha != "-" and docs[doc_id].get("cols_sha256") != cols_sha:
                problems.append(f"{fid}: {kind} log was made against a different reading-order text of {doc_id}")
    allow_missing = os.environ.get(optional_env) == "1" or not required
    missing = [p for p in problems if p.endswith(f"no {kind} log")]
    hard = [p for p in problems if not p.endswith(f"no {kind} log")]
    for p in hard:
        print(f"[{family}] {p}", file=sys.stderr)
    total = len(expected if expected is not None else forms)
    logged = total - len(missing)
    if not required:
        opened = (f"; open rulings in {len(open_counts)} log(s): " + ", ".join(f"{f} ({n})" for f, n in sorted(open_counts.items()))) if open_counts else "; no open rulings"
        state = "" if hard else "; snapshots and subjects current"
        print(f"{tag}: {logged}/{total} forms logged" + (f" ({', '.join(sorted(set(forms) - {p.split(':')[0] for p in missing}) if expected is None else sorted(set(expected) - {p.split(':')[0] for p in missing}))})" if 0 < logged <= 8 else "") + opened + state)
    elif missing:
        print(f"{tag}: {logged}/{total} forms logged; missing: " + ", ".join(p.split(':')[0] for p in missing))
    elif not hard:
        print(f"{tag} OK ({total} forms, no open rulings, snapshots and subjects current)")
    return bool(hard or (missing and not allow_missing))


def check_families(kind, logs):
    """Every log under `logs` belongs to a family named in families.json."""
    known = set(families.load(kind)["required"]) | set(families.load(kind)["optional"])
    bad = []
    if os.path.isdir(logs):
        for f in sorted(os.listdir(logs)):
            if f.endswith(".md"):
                form, fam = families.split_stem(f[:-3])
                if fam not in known:
                    bad.append(f"{form}: the {kind} log {f} names a model family {fam!r} not listed in tools/transcription/families.json")
    for p in bad:
        print(p, file=sys.stderr)
    return bool(bad)


def check_kind(kind, expected=None):
    """Every required family's logs of a kind, then every optional family's; logs of unlisted families fail."""
    logs = os.path.join(REVIEWS, kind)
    env = {"transcription": "TRANSCRIPTION_LOGS_OPTIONAL", "render": "RENDER_LOGS_OPTIONAL", "classm": "CLASSM_LOGS_OPTIONAL"}[kind]
    fams = families.load(kind)
    failed = check_families(kind, logs)
    for fam in fams["required"]:
        failed = check(kind, logs, env, expected, fam, required=True) or failed
    for fam in fams["optional"]:
        failed = check(kind, logs, env, expected, fam, required=False) or failed
    return failed


def second_family_summary():
    """The one-line summary of reports/<year>/second_family.md, when the report exists."""
    if not os.path.exists(SECOND_FAMILY_REPORT):
        print("second-family comparison: no report yet (tools/transcription/compare_families.py)"); return
    for line in open(SECOND_FAMILY_REPORT, encoding="utf-8"):
        if line.startswith("Summary: "):
            print("second-family comparison: " + line[len("Summary: "):].strip()); return
    print(f"second-family comparison: {os.path.relpath(SECOND_FAMILY_REPORT, ROOT)} has no summary line; rerun compare_families.py")


def check_human():
    """Validate record integrity; optional unfinished readings earn no H and do not fail."""
    sys.path.insert(0, os.path.join(ROOT, "tools", "human_review"))
    import logs as human_logs
    result = human_logs.evidence()
    for problem in result["problems"]:
        print("human reading: " + problem, file=sys.stderr)
    for note in result["pending"]:
        print("human reading pending (no H credit): " + note)
    if not result["logs"]:
        print("human logs: none yet")
    elif not result["problems"]:
        print(f"human log integrity OK ({result['logs']} forms; {len(result['lines'])} lines with signed source-reading credit; optional readings may be pending)")
    return bool(result["problems"])


failed = check_kind("transcription")
failed = check_kind("render") or failed
failed = check_kind("classm", classm_forms()) or failed
failed = check_human() or failed
failed = bool(rulings.check()) or failed
second_family_summary()
if failed:
    sys.exit(1)
