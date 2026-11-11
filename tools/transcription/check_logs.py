#!/usr/bin/env python3
"""Fail unless every form has a transcription-agreement log and a render-comparison log from
every required model family (families.json), each with no open ruling, current source hashes, an
unchanged subject (what the review judged: subjects.py; per compared line for a transcription or
render log whose form changed or that holds line-scoped reviews, subjects.log_state), and rulings
that agree with its sidecar.
An optional family's logs may be missing; those present are held to the same source and subject
checks, and their open rulings are counted and printed without failing the run. A stale optional log
(a changed subject or source snapshot) fails only when it would earn second-family credit if it were
current (compare_families.eligible_when_current); one that would not is reported as stale-ineligible
and does not fail, since a review is rerun only where it can earn credit. A log whose family
is in neither list fails. Counts are printed per kind and family. Runs offline in check-all; the logs
themselves are produced deliberately by transcribe.py and render_compare.py (network steps).

Only active families (families.json `active`) are checked as above. An inactive family's logs are history:
counted and printed, never required and never failed for staleness, open rulings or eligibility. Their
integrity is still checked, for every family, by rulings.check() below (each ruling in a log equals its
sidecar's) and by `review_store.py check` (every record present and named by its hash).

Optional human reading logs (reviews/<year>/human/) earn H only with a current receipt,
MATCH and reason, and exact contents committed by the named reader. Incomplete, stale or
negative readings are pending without failing this check. Malformed/duplicate records and
invalid identity or committed authorship remain failures (owner amendment 2026-10-24)."""
import json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings  # noqa: E402
import review_store  # noqa: E402
import subjects  # noqa: E402
import compare_families  # noqa: E402
import pending  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the New York documents and reviews/ny/<year>/)
FORMS = str(jurisdiction.ypath("forms", Y))
REVIEWS = str(jurisdiction.ypath("reviews", Y))
docs = {}
# A New York log also records the federal pages it was given (a federal line's interface and its source).
for _sources in jurisdiction.read_dirs("sources", Y):
    m = json.load(open(os.path.join(str(_sources), "manifest.json")))
    docs.update({d["id"]: d for d in (m["documents"] if isinstance(m, dict) else m)})
# Documents whose first review of a kind is not yet run (pending.py; New York only): reported, not failed.
PENDING = pending.load()

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


def transcription_forms():
    """Forms the transcription review covers: transcribe.py makes no model call for a form with no
    source-defined computed target whose adapter contract is checked separately, so none is expected."""
    import transcribe
    import adapter_contracts
    out = []
    for fid in forms:
        doc = transcribe.load_form(fid)
        targets = transcribe.exported_lines(doc) + [l for l in doc["lines"]
            if l["printed"] not in transcribe.HELPER_PRINTED and l["expr"].get("op") != "input"]
        if not targets and adapter_contracts.excluded_ids(fid, Y):
            print(f"transcription: {fid} not expected: no source-defined computed target (adapter contract checked separately)")
            continue
        out.append(fid)
    return out


def log_text(kind, logs, fid, family):
    """A form's log: as the review store assembles it (rulings.read_log), else a plain log file in `logs`
    (a test's), else None."""
    text = rulings.read_log(kind, fid, family)
    if text is None:
        path = os.path.join(logs, families.stem(fid, family) + ".md")
        text = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    return text


def check(kind, logs, optional_env, expected=None, family=families.DEFAULT, required=True):
    """One log per form of the family under `logs`; no open ruling; every source hash current;
    the subject it reviewed (subjects.py) unchanged. For an optional family a missing log is
    allowed and open rulings are counted, not failed."""
    problems, open_counts, tolerated = [], {}, []
    tag = f"{kind} logs [{family}{'' if required else ', optional'}]"
    waiting = PENDING.get(kind, set()) if required else set()
    for fid in (expected if expected is not None else forms):
        text = log_text(kind, logs, fid, family)
        if text is None:
            if fid in waiting:
                print(f"{tag}: {fid}: pending, no review yet (listed in {pending.name()})"); continue
            problems.append(f"{fid}: no {kind} log"); continue
        if fid in waiting:
            problems.append(f"{fid}: has a {kind} log but is still listed as pending; remove it from {pending.name()}")
        quality = None
        if family != families.DEFAULT and log_text(kind, logs, fid, families.DEFAULT) is not None:
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
        stale = []
        state = review_store.state(kind, fid, family, Y)  # from the index: per line, __rest__, foreign interfaces
        if state is review_store.NO_INDEX:
            state = subjects.log_state(kind, fid, Y, text)
        if state:
            stale.append(state)
        for row in re.findall(r"^\| (\S+) \| [^|]* \| [^|]* \| [^|]* \| ([0-9a-f]{64}) \|(?: [^|]* \| ([0-9a-f]{64}|-) \|)?$", text, flags=re.M):
            doc_id, sha, cols_sha = row
            if doc_id in docs and docs[doc_id]["text_sha256"] != sha:
                stale.append(f"{kind} log was made against a different snapshot of {doc_id}")
            if doc_id in docs and cols_sha and cols_sha != "-" and docs[doc_id].get("cols_sha256") != cols_sha:
                stale.append(f"{kind} log was made against a different reading-order text of {doc_id}")
        if stale and not required:
            eligible, blockers = (compare_families.eligible_when_current(quality) if quality is not None
                                  else (False, [f"no {families.DEFAULT} log to compare with"]))
            if not eligible:
                print(f"[{family}, optional] {fid}: stale-ineligible, not a failure ({'; '.join(stale)}); "
                      f"not eligible for second-family credit even if current: {'; '.join(blockers)}")
                tolerated.append(fid)
                stale = []
        problems += [f"{fid}: {s}" for s in stale]
    allow_missing = os.environ.get(optional_env) == "1" or not required
    missing = [p for p in problems if p.endswith(f"no {kind} log")]
    hard = [p for p in problems if not p.endswith(f"no {kind} log")]
    for p in hard:
        print(f"[{family}] {p}", file=sys.stderr)
    total = len(expected if expected is not None else forms)
    waited = sum(1 for fid in (expected if expected is not None else forms)
                 if fid in waiting and log_text(kind, logs, fid, family) is None)
    logged = total - len(missing) - waited
    if not required:
        opened = (f"; open rulings in {len(open_counts)} log(s): " + ", ".join(f"{f} ({n})" for f, n in sorted(open_counts.items()))) if open_counts else "; no open rulings"
        state = "" if hard else "; snapshots and subjects current" + (
            f" except {len(tolerated)} stale-ineligible ({', '.join(tolerated)})" if tolerated else "")
        print(f"{tag}: {logged}/{total} forms logged" + (f" ({', '.join(sorted(set(forms) - {p.split(':')[0] for p in missing}) if expected is None else sorted(set(expected) - {p.split(':')[0] for p in missing}))})" if 0 < logged <= 8 else "") + opened + state)
    elif missing:
        print(f"{tag}: {logged}/{total} forms logged; missing: " + ", ".join(p.split(':')[0] for p in missing))
    elif not hard and waited:
        print(f"{tag} OK for {logged}/{total} forms logged, {waited} pending (no open rulings, snapshots and subjects current)")
    elif not hard:
        print(f"{tag} OK ({total} forms, no open rulings, snapshots and subjects current)")
    return bool(hard or (missing and not allow_missing))


def check_families(kind, logs):
    """Every log under `logs` belongs to a family named in families.json."""
    known = set(families.load(kind)["required"]) | set(families.load(kind)["optional"])
    bad = []
    for form, fam in rulings.forms_with_logs(kind):
        if fam not in known:
            f = families.stem(form, fam) + ".index.json"
            bad.append(f"{form}: the {kind} log {f} names a model family {fam!r} not listed in tools/transcription/families.json")
    for p in bad:
        print(p, file=sys.stderr)
    return bool(bad)


def check_kind(kind, expected=None):
    """Every active required family's logs of a kind, then every active optional family's; an inactive
    family's logs are counted as history; logs of unlisted families fail."""
    logs = os.path.join(REVIEWS, kind)
    env = {"transcription": "TRANSCRIPTION_LOGS_OPTIONAL", "render": "RENDER_LOGS_OPTIONAL", "classm": "CLASSM_LOGS_OPTIONAL"}[kind]
    fams = families.load(kind)
    failed = check_families(kind, logs)
    for fam in fams["required"]:
        if fams["active"].get(fam, False):
            failed = check(kind, logs, env, expected, fam, required=True) or failed
    for fam in fams["optional"]:
        if fams["active"].get(fam, False):
            failed = check(kind, logs, env, expected, fam, required=False) or failed
    for fam in fams["required"] + fams["optional"]:
        if not fams["active"].get(fam, False):
            logged = sum(1 for _, f in rulings.forms_with_logs(kind) if f == fam)
            print(f"{kind} logs [{fam}, inactive]: {logged} log(s) kept as history; not checked for currency "
                  f"(set \"active\" in tools/transcription/families.json to check them again)")
    return failed


def check_human():
    """Validate record integrity; optional unfinished readings earn no H and do not fail."""
    if jurisdiction.NY:
        print("human logs: none for New York (human reading packets cover the federal documents)")
        return False
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


def main():
    failed = check_kind("transcription", transcription_forms())
    failed = check_kind("render") or failed
    failed = check_kind("classm", classm_forms()) or failed
    failed = check_human() or failed
    failed = bool(rulings.check()) or failed
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    # A render log's subject is the hash of its rendered file: judge it on what the current build renders to.
    import build_fresh
    build_fresh.require(rendered=True)
    main()
