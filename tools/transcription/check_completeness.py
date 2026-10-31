#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Standing section completeness review, offline, in check-all.

Every form with cited instruction pages must have a current completeness review: the hash of the prompt
completeness_review.py would send now (the form's cited pages and its encoding list) must equal the `prompt_sha`
recorded in reviews/<year>/completeness/completeness.json. A form whose lines, citations or cited pages changed is
`stale` (subject: the prompt hash) and is rerun with `python3 tools/transcription/completeness_review.py --forms <id>`.
Each claim of a current review is `unruled:<form>#<n>` (n from 1) until reviews/<year>/completeness/rulings.json
rules it with an object:

    {"class": "real gap" | "covered" | "out of scope" | "presentation" | "wrong", "evidence": "...",
     "prompt_sha": "<the review's prompt_sha>",
     "bug": "BUG-NNNN"  (real gap),  "line": "<line id>"  (covered),  "gate": "<line id>"  (out of scope, when a refusal covers it)}

A ruling carries the `prompt_sha` of the review whose claim it rules; one whose sha differs from the current review's
is not accepted (the claim is unruled again and the mismatch is an error), so a rerun needs new rulings. A
`PENDING-n` bug id is an error until a real BUG-NNNN replaces it.

A response that did not parse is `unparsed` until the form is rerun. Forms with no cited instruction pages, or whose
prompt exceeds the size limit, are not reviewed and are named in the output. Findings that existed when the check
was introduced form the baseline (tools/baseline_check.py).

    check_completeness.py [--baseline] [--self-test]
"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from completeness_review import load_forms, prompt_for, MAX_CHARS, OUT  # noqa: E402
from transcribe import ROOT, manifest  # noqa: E402
from taxyear import Y  # noqa: E402
import baseline_check  # noqa: E402

RECORD = Path(OUT) / "completeness.json"
RULINGS = Path(OUT) / "rulings.json"
REPORT = Path(ROOT) / "reports" / Y / "completeness.md"
CLASSES = ("real gap", "covered", "out of scope", "presentation", "wrong")
NEEDS = {"real gap": "bug", "covered": "line"}


def validate(key, ruling, line_ids, sha=None):
    """The errors of one ruling object (empty when it is well formed). `sha` is the current review's prompt_sha
    for the ruling's form, or None when the form has no current review."""
    if not isinstance(ruling, dict):
        return [f"{key}: a ruling is an object with class and evidence"]
    errs = []
    cls = ruling.get("class")
    if cls not in CLASSES:
        errs.append(f"{key}: class must be one of {', '.join(CLASSES)}")
    if not str(ruling.get("evidence", "")).strip():
        errs.append(f"{key}: evidence is required")
    got = ruling.get("prompt_sha")
    if not got:
        errs.append(f"{key}: prompt_sha is required (the review's prompt_sha)")
    elif sha is not None and got != sha:
        errs.append(f"{key}: not accepted, prompt_sha {str(got)[:8]} differs from the current review's {sha[:8]}; rule it again")
    bug = str(ruling.get("bug", ""))
    if cls == "real gap" and bug.startswith("PENDING-"):
        errs.append(f"{key}: pending bug id {bug}; file the bug and give bug: BUG-NNNN")
    elif cls == "real gap" and not re.fullmatch(r"BUG-\d{4}", bug):
        errs.append(f"{key}: a real gap needs bug: BUG-NNNN")
    if cls == "covered" and ruling.get("line") not in line_ids:
        errs.append(f"{key}: covered needs a line that exists in canonical")
    if ruling.get("gate") is not None and ruling["gate"] not in line_ids:
        errs.append(f"{key}: gate {ruling['gate']!r} does not exist in canonical")
    return errs


def form_of(key):
    return key.split(":", 1)[-1].rsplit("#", 1)[0]


def validate_all(rulings, line_ids, shas=None):
    shas = shas or {}
    return [e for k, r in sorted(rulings.items()) for e in validate(k, r, line_ids, shas.get(form_of(k)))]


def accepted(rulings, shas):
    """The rulings whose prompt_sha matches the current review of their form (all others count as unruled)."""
    return {k: r for k, r in rulings.items()
            if not isinstance(r, dict) or r.get("prompt_sha") == shas.get(form_of(k))}


def findings(forms, mani, reviewed):
    out, notes = [], []
    for f in forms:
        p = prompt_for(f, mani)
        if p is None:
            notes.append(f"{f['id']}: no cited instruction pages, not reviewed")
            continue
        prompt, _, sha = p
        if len(prompt) > MAX_CHARS:
            notes.append(f"{f['id']}: prompt {len(prompt):,} chars exceeds {MAX_CHARS:,}, not reviewed")
            continue
        r = reviewed.get(f["id"])
        if not r or r.get("prompt_sha") != sha:
            why = "never reviewed" if not r else "lines, citations or cited pages changed since the review"
            out.append({"kind": "stale", "line": f["id"], "form": f["id"], "subject": sha,
                        "detail": f"{why}; rerun completeness_review.py --forms {f['id']}"})
        elif r.get("parse_error"):
            out.append({"kind": "unparsed", "line": f["id"], "form": f["id"], "subject": sha,
                        "detail": f"the response was not YAML claims; rerun completeness_review.py --forms {f['id']}"})
        else:
            for n, c in enumerate(r.get("claims") or [], 1):
                out.append({"kind": "unruled", "line": f"{f['id']}#{n}", "form": f["id"], "subject": sha,
                            "detail": f"{c.get('effect', '?')}: {c.get('page', '?')}: {c.get('quote', '')[:110]}"})
    return out, notes


def check(rebaseline=False):
    forms = baseline_check.load_forms(Path(ROOT) / "canonical" / Y)
    reviewed = {r["form"]: r for r in json.loads(RECORD.read_text())} if RECORD.exists() else {}
    found, notes = findings(forms, manifest(), reviewed)
    line_ids = {l["id"] for f in forms for l in f["lines"]}
    data = json.loads(RULINGS.read_text()) if RULINGS.exists() else {}
    rulings = data.get("rulings", {})
    shas = {f["form"]: f["subject"] for f in found if f["kind"] == "unruled"}
    errors = validate_all(rulings, line_ids, shas)
    for e in errors:
        print(f"  ruling error: {e}")
    for n in notes:
        print(f"  note: {n}")
    with tempfile.TemporaryDirectory() as tmp:  # run() sees only the accepted rulings
        view = Path(tmp) / RULINGS.name
        view.write_text(json.dumps({**data, "rulings": accepted(rulings, shas)}))
        status = baseline_check.run(
            "completeness", forms, found, view, REPORT, "Standing section completeness review",
            "Generated by `tools/transcription/check_completeness.py`. `stale`: the form's review prompt changed since "
            "it was reviewed. `unruled`: a claim of a current review not yet ruled in rulings.json (or ruled against "
            "another review's prompt_sha). `unparsed`: the response held no YAML claims.", rebaseline)
        if rebaseline:
            data["baseline"] = json.loads(view.read_text())["baseline"]
            RULINGS.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    return 1 if errors else status


def self_test():
    ids = {"a.x", "a.gate"}
    S = "abc123"
    good = {"u:f#1": {"class": "real gap", "evidence": "e", "bug": "BUG-0123", "prompt_sha": S},
            "u:f#2": {"class": "covered", "evidence": "e", "line": "a.x", "prompt_sha": S},
            "u:f#3": {"class": "out of scope", "evidence": "e", "gate": "a.gate", "prompt_sha": S},
            "u:f#4": {"class": "presentation", "evidence": "e", "prompt_sha": S},
            "u:f#5": {"class": "wrong", "evidence": "e", "prompt_sha": S}}
    bad = {"u:f#1": {"class": "real gap", "evidence": "e", "prompt_sha": S},
           "u:f#2": {"class": "covered", "evidence": "e", "line": "a.nope", "prompt_sha": S},
           "u:f#3": {"class": "out of scope", "evidence": "e", "gate": "a.nope", "prompt_sha": S},
           "u:f#4": {"class": "maybe", "evidence": "e", "prompt_sha": S},
           "u:f#5": {"class": "wrong", "evidence": " ", "prompt_sha": S},
           "u:f#6": "text",
           "u:f#7": {"class": "presentation", "evidence": "e", "prompt_sha": "old999"},
           "u:f#8": {"class": "presentation", "evidence": "e"},
           "u:f#9": {"class": "real gap", "evidence": "e", "bug": "PENDING-3", "prompt_sha": S}}
    pend = validate("k", bad["u:f#9"], ids, S)
    status = 0
    for name, rulings, want in (("good", good, 0), ("bad", bad, 9)):
        got = len(validate_all(rulings, ids, {"f": S}))
        ok = (got == 0) if want == 0 else all(validate(k, r, ids, S) for k, r in rulings.items())
        status = status or (0 if ok else 1)
        print(f"completeness self-test, {name} rulings: {got} error(s), {'as expected' if ok else 'WRONG'}")
    ok = len(pend) == 1 and "pending bug id" in pend[0]
    status = status or (0 if ok else 1)
    print(f"completeness self-test, pending bug id: {'as expected' if ok else 'WRONG'}")
    ok = set(accepted(good, {"f": "other"})) == set() and set(accepted(good, {"f": S})) == set(good)
    status = status or (0 if ok else 1)
    print(f"completeness self-test, sha-mismatched rulings not accepted: {'as expected' if ok else 'WRONG'}")
    from completeness_review import runs, parse
    ok = runs({17, 19, 20, 30}) == [(17, 20), (30, 30)] and runs({1, 5}) == [(1, 1), (5, 5)] and runs({1, 4}) == [(1, 4)]
    status = status or (0 if ok else 1)
    print(f"completeness self-test, page runs: {'as expected' if ok else 'WRONG'}")
    grouped = parse("claims:\n  - item: a.x\n    sentences:\n      - quote: q1\n        page: p1\n      - q2\n    effect: amount")
    ok = (len(grouped) == 1 and [s["quote"] for s in grouped[0]["sentences"]] == ["q1", "q2"]
          and grouped[0]["closest_item"] == "a.x" and grouped[0]["page"] == "p1")
    status = status or (0 if ok else 1)
    print(f"completeness self-test, grouped claims: {'as expected' if ok else 'WRONG'}")
    ok = (parse("```yaml\nclaims:\n  - quote: q\n    page: p\n    effect: amount\n```")[0]["effect"] == "amount"
          and parse("claims: []") == [] and parse("not: [yaml") is None and parse("hello") is None)
    status = status or (0 if ok else 1)
    print(f"completeness self-test, lenient parse: {'as expected' if ok else 'WRONG'}")
    return status


if __name__ == "__main__":
    os.chdir(ROOT)
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(check(rebaseline="--baseline" in sys.argv))
