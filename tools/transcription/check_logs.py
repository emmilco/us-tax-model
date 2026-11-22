#!/usr/bin/env python3
"""Fail unless every form is satisfied by a current log from a qualified model family (families.json),
with no open ruling in a current qualified log, current source hashes, an unchanged subject (what the review
judged: subjects.py; per compared line for a transcription or render log whose form changed or that holds
line-scoped reviews, subjects.log_state), and rulings that agree with their sidecars.

A form is satisfied when one qualified family's log is present, current and holds no open ruling; the
qualified families are asked in the order families.json lists them. Every other log of the form is
advisory: an advisory family's logs are counted, their open rulings are counted and printed without
failing the run, and a stale one (a changed subject or source snapshot) fails only when it would earn
credit if it were current (compare_families.eligible_when_current) and its family is callable; one that
would not earn credit anyway, or whose family is not callable, is reported as stale-ineligible and does
not fail, since a review is rerun only where it can earn credit. A log whose family is in neither tier
fails. Counts are printed per kind and tier. Runs offline in check-all; the logs themselves are produced
deliberately by transcribe.py, render_compare.py and classm.py (network steps).

`callable` (families.json) says which families the tools may call; it does not decide whose logs count.
A family that may not be called keeps its logs and their standing, so Claude's current logs go on
satisfying forms while Claude is not called. Integrity is checked for every family, by rulings.check()
below (each ruling in a log equals its sidecar's) and by `review_store.py check` (every record present
and named by its hash).

Optional human reading logs (reviews/<year>/human/) are validated by tools/human_review/logs.py:
malformed or duplicate records, a reader who is not a named person and a committed log whose
author is not its reader fail this check. No tool issues the receipts H credit needs, so every
reading is listed as pending with its verdict, without failing this check."""
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


def log_faults(kind, fid, family, text):
    """(open rulings, staleness) in one form's log: how many rulings it leaves open, and why it no
    longer answers its subject (a changed subject, a source snapshot or reading order that moved on)."""
    opened = text.count("Ruling: open")
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
    return opened, stale


def check(kind, logs, optional_env, expected=None):
    """Every form's logs against the tiers of families.json: satisfied by a qualified family's current log
    with no open ruling; advisory logs counted, and failed only when stale where they would earn credit.
    `optional_env=1` tolerates a form no qualified log satisfies (the New York first reviews)."""
    forms_ = expected if expected is not None else forms
    fams = families.load(kind)
    qualified, advisory = fams["qualified"], fams["advisory"]
    waiting = PENDING.get(kind, set())
    problems, awaited, unsatisfied, satisfied = [], [], [], {}
    for fid in forms_:
        owed, current = [], []
        for fam in qualified:
            text = log_text(kind, logs, fid, fam)
            if text is None:
                owed.append(f"{fam}: no {kind} log")
                continue
            opened, stale = log_faults(kind, fid, fam, text)
            if opened and not stale:
                problems.append(f"{fid}: {fam}: open ruling(s) in the {kind} log")
            if stale:
                owed.append(f"{fam}: " + "; ".join(stale + ([f"{opened} open ruling(s)"] if opened else [])))
            elif opened:
                owed.append(f"{fam}: open ruling(s) in the {kind} log")
            else:
                current.append(fam)
        if fid in waiting:
            if current:
                problems.append(f"{fid}: has a {kind} log but is still listed as pending; remove it from {pending.name()}")
            else:
                awaited.append(fid)
                print(f"{kind} logs: {fid}: pending, no review yet (listed in {pending.name()})")
            continue
        if current:
            satisfied[fid] = current[0]
        else:
            unsatisfied.append((fid, owed))
    for fam in advisory:
        have = opened_n = tolerated = 0
        for fid in forms_:
            text = log_text(kind, logs, fid, fam)
            if text is None:
                continue
            have += 1
            opened, stale = log_faults(kind, fid, fam, text)
            opened_n += opened
            if not stale:
                continue
            if not fams["callable"].get(fam, False) or log_text(kind, logs, fid, families.DEFAULT) is None:
                tolerated += 1
                continue
            try:
                quality = compare_families.compare(kind, fid, fam)["quality"]
                eligible, blockers = compare_families.eligible_when_current(quality)
            except Exception as ex:  # an absent or unreadable comparison cannot earn credit
                eligible, blockers = False, [f"no comparison ({type(ex).__name__}: {ex})"]
            if eligible:
                problems.append(f"{fid}: {fam}: advisory log is stale where it would earn credit: " + "; ".join(stale))
            else:
                tolerated += 1
                print(f"[{kind}, {fam}, advisory] {fid}: stale-ineligible, not a failure ({'; '.join(stale)}); "
                      f"not eligible for credit even if current: {'; '.join(blockers)}")
        if have:
            note = f"{kind} logs [{fam}, advisory]: {have}/{len(forms_)} form(s) logged"
            note += f", {opened_n} open ruling(s)" if opened_n else ", no open rulings"
            note += f", {tolerated} stale-ineligible" if tolerated else ""
            print(note)
    for p in problems:
        print(f"[{kind}] {p}", file=sys.stderr)
    for fid, why in unsatisfied:
        print(f"[{kind}] {fid}: no current qualified log ({'; '.join(why)})", file=sys.stderr)
    total = len(forms_)
    counts = {}
    for fam in satisfied.values():
        counts[fam] = counts.get(fam, 0) + 1
    detail = ", ".join(f"{fam} {n}" for fam, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))
    absent = [fam for fam in qualified if not fams["callable"].get(fam, False)]
    tier = f"[qualified: {', '.join(qualified)}" + (f"; not callable: {', '.join(absent)}]" if absent else "]")
    allow_missing = os.environ.get(optional_env) == "1" or not qualified
    tag = f"{kind} logs"
    if unsatisfied and not allow_missing:
        print(f"{tag}: {len(satisfied)}/{total} forms satisfied" + (f" ({detail})" if detail else "") +
              "; unsatisfied: " + ", ".join(fid for fid, _ in unsatisfied))
    else:
        extra = []
        if awaited:
            extra.append(f"{len(awaited)} pending (no review yet)")
        if unsatisfied:
            extra.append(f"{len(unsatisfied)} unsatisfied tolerated ({optional_env}=1)")
        print(f"{tag}: {len(satisfied)}/{total} forms satisfied" + (f" ({detail})" if detail else "") +
              ("; " + "; ".join(extra) if extra else "") + " " + tier)
    return bool(problems or (unsatisfied and not allow_missing))


def check_families(kind, logs):
    """Every log under `logs` belongs to a family named in families.json."""
    known = set(families.load(kind)["qualified"]) | set(families.load(kind)["advisory"])
    bad = []
    for form, fam in rulings.forms_with_logs(kind):
        if fam not in known:
            f = families.stem(form, fam) + ".index.json"
            bad.append(f"{form}: the {kind} log {f} names a model family {fam!r} not listed in tools/transcription/families.json")
    for p in bad:
        print(p, file=sys.stderr)
    return bool(bad)


def check_kind(kind, expected=None):
    """Every form's logs of one kind against the tiers of families.json."""
    logs = os.path.join(REVIEWS, kind)
    env = {"transcription": "TRANSCRIPTION_LOGS_OPTIONAL", "render": "RENDER_LOGS_OPTIONAL", "classm": "CLASSM_LOGS_OPTIONAL"}[kind]
    failed = check_families(kind, logs)
    failed = check(kind, logs, env, expected) or failed
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
