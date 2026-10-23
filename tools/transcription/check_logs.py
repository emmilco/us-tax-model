#!/usr/bin/env python3
"""Fail unless every form has a transcription-agreement log and a render-comparison log from
every required model family (families.json), each with no open ruling, current source hashes, an
unchanged subject (what the review judged: subjects.py), and rulings that agree with its sidecar.
An optional family's logs may be missing; those present are held to the same source and subject
checks, and their open rulings are counted and printed without failing the run. A log whose family
is in neither list fails. Counts are printed per kind and family. Runs offline in check-all; the logs
themselves are produced deliberately by transcribe.py and render_compare.py (network steps).

When reports/<year>/second_family.md exists (compare_families.py), its summary line is printed.

Human reading logs (reviews/<year>/human/, written by tools/human_review/serve.py) are checked
when present: current subject, no empty verdict or reason, a reader who is a person, and a
committed file's last author equal to its reader."""
import json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings  # noqa: E402
import subjects  # noqa: E402

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
    known = set(families.load()["required"]) | set(families.load()["optional"])
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
    fams = families.load()
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


HUMAN = os.path.join(ROOT, "reviews", Y, "human")
MODEL_NAME = re.compile(r"claude|gpt|deepseek|model|agent", re.I)


def check_human():
    """Every reviews/<year>/human/<form>.md: its subject (the kind its header names) current; every
    line carries a verdict; the reader is a person; a committed log's last author is that reader.
    A missing log is not a problem: the set of human logs grows as the reading list is read."""
    if not os.path.isdir(HUMAN):
        print("human logs: none yet"); return False
    problems, notes, n = [], [], 0
    for name in sorted(os.listdir(HUMAN)):
        if not name.endswith(".md"):
            continue
        fid, n = name[:-3], n + 1
        rel = os.path.relpath(os.path.join(HUMAN, name), ROOT)
        text = open(os.path.join(HUMAN, name), encoding="utf-8").read()
        kind = re.search(r"^\| subject kind \| (\w+) \|$", text, flags=re.M)
        subject = re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", text, flags=re.M)
        if not kind or not subject:
            problems.append(f"{fid}: the human log records no subject kind and hash (tools/transcription/subjects.py)")
        elif kind.group(1) not in ("transcription", "render", "classm"):
            problems.append(f"{fid}: the human log names an unknown subject kind {kind.group(1)!r}")
        elif not os.path.exists(subjects.path(kind.group(1), fid, Y)):
            problems.append(f"{fid}: the human log's subject ({kind.group(1)}) no longer exists for {fid}")
        elif subject.group(1) != subjects.current(kind.group(1), fid, Y):
            problems.append(f"{fid}: the human log read an earlier {kind.group(1)} of {fid}; the reader must read it again")
        for doc_id, sha, cols_sha in re.findall(r"^\| (\S+) \| [^|]* \| [^|]* \| ([0-9a-f]{64}) \| ([0-9a-f]{64}|-) \|$", text, flags=re.M):
            if doc_id in docs and docs[doc_id]["text_sha256"] != sha:
                problems.append(f"{fid}: human log was made against a different snapshot of {doc_id}")
            if doc_id in docs and cols_sha != "-" and docs[doc_id].get("cols_sha256") != cols_sha:
                problems.append(f"{fid}: human log was made against a different reading-order text of {doc_id}")
        sections = re.findall(r"^### (.*?) — `([^`]+)`\n(.*?)(?=^### |\Z)", text, flags=re.M | re.S)
        if not sections:
            problems.append(f"{fid}: the human log has no lines")
        empty = [lid for _, lid, body in sections if not re.search(r"^Verdict: \*\*(MATCH|MISMATCH|UNCLEAR)\*\*$", body, flags=re.M)]
        if empty:
            problems.append(f"{fid}: {len(empty)} line(s) without a verdict in the human log: " + ", ".join(empty))
        no_reason = [lid for _, lid, body in sections if re.search(r"^Reason:\n\(empty\)", body, flags=re.M)]
        if no_reason:
            problems.append(f"{fid}: {len(no_reason)} line(s) without a reason in the human log: " + ", ".join(no_reason))
        reader = re.search(r"^\| reader \| (.*) \|$", text, flags=re.M)
        reader = reader.group(1).strip() if reader else ""
        if not reader:
            problems.append(f"{fid}: the human log names no reader")
        elif MODEL_NAME.search(reader):
            problems.append(f"{fid}: the human log's reader ({reader!r}) names a model; a human log is signed by a person")
        author = subprocess.run(["git", "log", "-1", "--format=%an", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        if not author:
            notes.append(f"{fid}: human log not yet committed; its commit author must be {reader!r}")
        elif reader and author != reader:
            problems.append(f"{fid}: the human log's last commit author ({author!r}) is not its reader ({reader!r})")
    for p in problems:
        print(p, file=sys.stderr)
    for p in notes:
        print(p)
    if not problems:
        print(f"human logs OK ({n} forms, every line judged, readers are people, subjects current)")
    return bool(problems)


failed = check_kind("transcription")
failed = check_kind("render") or failed
failed = check_kind("classm", classm_forms()) or failed
failed = check_human() or failed
failed = bool(rulings.check()) or failed
second_family_summary()
if failed:
    sys.exit(1)
