#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Standing section completeness review, offline, in check-all.

Sampled reviews (samples.py). A form's subject is the hash of the prompt completeness_review.py would send now,
without the system prompt (the form's cited pages, its encoding list and the HANDLED ELSEWHERE list). Its record in
reviews/<year>/completeness/completeness.json holds the samples run against one subject.

- A form whose subject differs from its record's (or that has none) is `due`: listed, not failed. It is reviewed
  before the next release with `completeness_review.py --forms <id>`.
- Each claim of a current sample is `unruled:<form>#<k>.<n>` (sample k, claim n, both from 1) until
  reviews/<year>/completeness/rulings.json rules it, or it carries a ruling (below). Unruled claims fail check-all.
- A claim whose item and normalised quote equal those of a ruled claim of the same form and subject carries that
  ruling (samples.carry_key); the report names the ruling it carries.
- A ruling is an object:

    {"class": "real gap" | "covered" | "out of scope" | "presentation" | "wrong", "evidence": "...",
     "subject_sha": "<the record's subject_sha>",
     "bug": "BUG-NNNN"  (real gap),  "line": "<line id>"  (covered),  "gate": "<line id>"  (out of scope, when a refusal covers it)}

  A ruling whose subject_sha differs from the current record's is not accepted (the claim is unruled again and
  the mismatch is an error). A `PENDING-n` bug id is an error until a real BUG-NNNN replaces it.
- A sample whose response did not parse is listed and does not count toward the milestone.

`--release` is the release gate (tools/release.sh): it also fails on every due form and every form short of the
milestone's samples. Forms with no cited instruction pages, or whose prompt exceeds the size limit, are not reviewed
and are named in the output. A New York form listed as pending (pending.py) is reported, not failed.

    check_completeness.py [--release] [--baseline] [--self-test]
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
from completeness_review import prompt_for, read_records, MAX_CHARS, OUT  # noqa: E402
from transcribe import ROOT, manifest  # noqa: E402
from taxyear import Y  # noqa: E402
import baseline_check  # noqa: E402
import samples  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the New York forms, reviews/ny/<year>/, reports/ny/<year>/)
import pending  # noqa: E402

RECORD = Path(OUT) / "completeness.json"
RULINGS = Path(OUT) / "rulings.json"
REPORT = jurisdiction.ypath("reports", Y, "completeness.md")
CLASSES = ("real gap", "covered", "out of scope", "presentation", "wrong")
NEEDS = {"real gap": "bug", "covered": "line"}


def validate(key, ruling, line_ids, sha=None):
    """The errors of one ruling object (empty when it is well formed). `sha` is the current record's subject_sha
    for the ruling's form, or None when the form has no current record."""
    if not isinstance(ruling, dict):
        return [f"{key}: a ruling is an object with class and evidence"]
    errs = []
    cls = ruling.get("class")
    if cls not in CLASSES:
        errs.append(f"{key}: class must be one of {', '.join(CLASSES)}")
    if not str(ruling.get("evidence", "")).strip():
        errs.append(f"{key}: evidence is required")
    got = ruling.get("subject_sha")
    if not got:
        errs.append(f"{key}: subject_sha is required (the record's subject_sha)")
    elif sha is not None and got != sha:
        errs.append(f"{key}: not accepted, subject_sha {str(got)[:8]} differs from the current record's {sha[:8]}; rule it again")
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


def key_of(form, k, n):
    return f"unruled:{form}#{k}.{n}"


def validate_all(rulings, line_ids, shas=None):
    shas = shas or {}
    return [e for k, r in sorted(rulings.items()) for e in validate(k, r, line_ids, shas.get(form_of(k)))]


def accepted(rulings, shas):
    """The rulings whose subject_sha matches the current record of their form (all others count as unruled)."""
    return {k: r for k, r in rulings.items()
            if not isinstance(r, dict) or r.get("subject_sha") == shas.get(form_of(k))}


def carried(found, rulings):
    """{key: ruling} for unruled claims that carry a ruling: a claim of the same form whose item and normalised
    quote are equal and which has its own (accepted) ruling. The carried ruling names its source."""
    own = {}
    for f in found:
        k = "unruled:" + f["line"]
        if f["kind"] == "unruled" and k in rulings:
            own.setdefault((f["form"], f["carry"]), k)
    out = {}
    for f in found:
        k = "unruled:" + f["line"]
        src = own.get((f["form"], f.get("carry")))
        if f["kind"] == "unruled" and k not in rulings and src:
            r = rulings[src]
            out[k] = {**r, "carried_from": src} if isinstance(r, dict) else r
    return out


def findings(forms, mani, records, release=False):
    """(found, notes, due, shas). `due` lists (form, why) for forms whose subject has no record; `shas` is each
    reviewed form's current subject. With release, due and short forms are findings too."""
    out, notes, due, shas = [], [], [], {}
    for f in forms:
        p = prompt_for(f, mani)
        if p is None:
            notes.append(f"{f['id']}: no cited instruction pages, not reviewed")
            continue
        prompt, _, sha = p
        if len(prompt) > MAX_CHARS:
            notes.append(f"{f['id']}: prompt {len(prompt):,} chars exceeds {MAX_CHARS:,}, not reviewed")
            continue
        r = records.get(f["id"])
        if not r or r.get("subject_sha") != sha:
            why = "never reviewed" if not r else "lines, citations or cited pages changed since its samples"
            due.append((f["id"], why))
            if release:
                out.append({"kind": "due", "line": f["id"], "form": f["id"], "subject": sha,
                            "detail": f"{why}; run completeness_review.py --forms {f['id']}"})
            continue
        shas[f["id"]] = sha
        for k, smp in enumerate(r.get("samples") or [], 1):
            if smp.get("parse_error"):
                notes.append(f"{f['id']}: sample {k} did not parse and does not count")
                continue
            for n, c in enumerate(smp.get("claims") or [], 1):
                out.append({"kind": "unruled", "line": f"{f['id']}#{k}.{n}", "form": f["id"], "subject": sha,
                            "carry": samples.carry_key(c.get("item"), c.get("quote")),
                            "detail": f"{c.get('effect', '?')}: {c.get('page', '?')}: {c.get('quote', '')[:110]}"})
        if release and not samples.satisfied(r):
            out.append({"kind": "short", "line": f["id"], "form": f["id"], "subject": sha,
                        "detail": f"{len(samples.parsed(r))} of {samples.SAMPLES_PER_MILESTONE} sample(s); "
                                  f"run completeness_review.py --forms {f['id']}"})
    return out, notes, due, shas


def check(rebaseline=False, release=False):
    forms = baseline_check.load_forms(Path(ROOT) / "canonical" / Y)
    records = read_records(str(RECORD))
    found, notes, due, shas = findings(forms, manifest(), records, release)
    # A form whose first review is pending (pending.py; New York only) is reported, not failed, until reviewed.
    waiting = pending.listed("completeness")
    errors = [f"{f}: reviewed but still listed as pending; remove it from {pending.name()}" for f in sorted(waiting & set(records))]
    for f in [f for f in found if f["kind"] == "due" and f["form"] in waiting and f["form"] not in records]:
        found.remove(f)
    for form, _ in [d for d in due if d[0] in waiting and d[0] not in records]:
        notes.append(f"{form}: pending, never reviewed (listed in {pending.name()})")
    due = [d for d in due if not (d[0] in waiting and d[0] not in records)]
    line_ids = {l["id"] for f in forms for l in f["lines"]}
    data = json.loads(RULINGS.read_text()) if RULINGS.exists() else {}
    rulings = data.get("rulings", {})
    errors = validate_all(rulings, line_ids, shas) + errors
    for e in errors:
        print(f"  ruling error: {e}")
    for n in notes:
        print(f"  note: {n}")
    for form, why in due:
        print(f"  due at the next release: {form}: {why}")
    good = accepted(rulings, shas)
    carry = carried(found, good)
    if carry:
        print(f"  {len(carry)} claim(s) carry the ruling of an equal claim on the same subject")
    with tempfile.TemporaryDirectory() as tmp:  # run() sees only the accepted and carried rulings
        view = Path(tmp) / RULINGS.name
        view.write_text(json.dumps({**data, "rulings": {**good, **carry}}))
        report = Path(tmp) / "report.md" if release else REPORT   # the release gate leaves reports/ as committed
        status = baseline_check.run(
            "completeness", forms, found, view, report, "Standing section completeness review",
            "Generated by `tools/transcription/check_completeness.py`. `unruled`: a claim of a current sample "
            "(`<form>#<sample>.<claim>`) not yet ruled in rulings.json (or ruled against another subject); a ruling "
            "with `carried_from` is carried from an equal claim. `due` and `short` appear only in release mode.",
            rebaseline)
        if rebaseline:
            data["baseline"] = json.loads(view.read_text())["baseline"]
            RULINGS.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    if due and not release:
        with open(REPORT, "a", encoding="utf-8") as out:
            out.write("\n## Due at the next release\n\n" + "".join(f"- `{f}`: {why}\n" for f, why in due))
    return 1 if errors else status


def self_test():
    ids = {"a.x", "a.gate"}
    S = "abc123"
    good = {"u:f#1": {"class": "real gap", "evidence": "e", "bug": "BUG-0123", "subject_sha": S},
            "u:f#2": {"class": "covered", "evidence": "e", "line": "a.x", "subject_sha": S},
            "u:f#3": {"class": "out of scope", "evidence": "e", "gate": "a.gate", "subject_sha": S},
            "u:f#4": {"class": "presentation", "evidence": "e", "subject_sha": S},
            "u:f#5": {"class": "wrong", "evidence": "e", "subject_sha": S}}
    bad = {"u:f#1": {"class": "real gap", "evidence": "e", "subject_sha": S},
           "u:f#2": {"class": "covered", "evidence": "e", "line": "a.nope", "subject_sha": S},
           "u:f#3": {"class": "out of scope", "evidence": "e", "gate": "a.nope", "subject_sha": S},
           "u:f#4": {"class": "maybe", "evidence": "e", "subject_sha": S},
           "u:f#5": {"class": "wrong", "evidence": " ", "subject_sha": S},
           "u:f#6": "text",
           "u:f#7": {"class": "presentation", "evidence": "e", "subject_sha": "old999"},
           "u:f#8": {"class": "presentation", "evidence": "e"},
           "u:f#9": {"class": "real gap", "evidence": "e", "bug": "PENDING-3", "subject_sha": S}}
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
    import unittest
    from test_samples import SampleTests
    result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(SampleTests))
    return status or (0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    os.chdir(ROOT)
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(check(rebaseline="--baseline" in sys.argv, release="--release" in sys.argv))
