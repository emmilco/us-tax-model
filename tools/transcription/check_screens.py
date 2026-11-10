#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Standing screen review (T-088), offline, in check-all. Sampled reviews (samples.py).

Every scope screen (a yes/no input that lines name as a refusal gate) and every choose-guard gate (gates.py, keyed
`gate:<condition>`) has a record in reviews/<year>/screens/screen_review.json holding the samples run against one
subject. A screen's subject is the prompt screen_review.py would send without the gate condition and without the
system prompt (screen_subject); a gate's is gates.subject (the condition's wording and line, each gate line and gated
input with their English and wording, citations included).

- A unit whose subject differs from its record's (or that has none) is `due`: listed, not failed. It is reviewed
  before the next release with `python3 tools/transcription/screen_review.py --screens <id>`.
- Each current sample whose verdict is not COVERS is `unruled:<unit>#<k>` (k from 1) until its findings are
  adjudicated and ruled in reviews/<year>/screens/rulings.json with the record's `subject_sha`; a ruling with another
  subject_sha is not accepted. A sample whose verdict and normalised findings equal those of a ruled sample of the same
  unit and subject carries that ruling. Unruled samples fail check-all.
- A sample whose verdict did not parse is listed and does not count toward the milestone.
- `orphan`: a recorded gate review whose gate no longer exists (fails).

`--release` is the release gate (tools/release_reviews.sh): it also fails on every due unit and every unit short of the
milestone's samples, and writes no report. Findings that existed when the check was introduced form the baseline
(tools/baseline_check.py), each held while its subject is unchanged.

    check_screens.py [--release] [--baseline]
"""
import json
import tempfile
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from screen_review import load_lines, screens, screen_subject, encoded_english, read_records, OUT  # noqa: E402
import samples  # noqa: E402
import gates  # noqa: E402
from transcribe import ROOT, manifest  # noqa: E402
from taxyear import Y  # noqa: E402
import baseline_check  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the screens of New York lines, reviews/ny/<year>/screens/)
import pending  # noqa: E402

RECORD = Path(OUT) / "screen_review.json"
RULINGS = Path(OUT) / "rulings.json"
REPORT = jurisdiction.ypath("reports", Y, "screen_currency.md")


def unit_findings(key, form, sha, r, why_changed):
    return samples.unit_findings(key, form, sha, r, why_changed, "COVERS", f"screen_review.py --screens {key}")


def findings():
    """(found, shas): every unit's findings, release kinds included, and each unit's current subject."""
    lines = load_lines()
    mani = manifest()
    reviewed = read_records(str(RECORD))
    out, shas = [], {}
    waiting = pending.listed("screens")
    for screen in sorted(waiting & set(reviewed)):
        out.append({"kind": "pending", "line": screen, "form": lines[screen][0] if screen in lines else "?", "subject": "-",
                    "detail": f"reviewed but still listed as pending; remove it from {pending.name()}"})
    for screen, gated in screens(lines).items():
        sha = screen_subject(screen, gated, lines, mani)
        if screen not in reviewed and screen in waiting:
            print(f"  pending: {screen}: never reviewed (listed in {pending.name()})")
            continue
        shas[screen] = sha
        out += unit_findings(screen, lines[screen][0], sha, reviewed.get(screen),
                             "question, gated lines or their citations changed since its samples")
    gf, gshas = gate_findings(lines, reviewed)
    return out + gf, {**shas, **gshas}


def gate_findings(lines, reviewed):
    """(findings, shas) of each choose-guard gate's samples, and recorded gate reviews whose gate is gone."""
    out, shas = [], {}
    current = gates.units(lines)
    for key, unit in current.items():
        sha = shas[key] = gates.subject(unit, lines, encoded_english)
        out += unit_findings(key, gates.unit_form(unit, lines), sha, reviewed.get(key),
                             "the condition's wording, the gated lines or their citations changed since its samples")
    for key in sorted(k for k in reviewed if k.startswith("gate:") and k not in current):
        out.append({"kind": "orphan", "line": key, "form": "-", "subject": key,
                    "detail": "a recorded gate review whose gate no longer exists; remove it from screen_review.json"})
    return out, shas


accepted, carried = samples.accepted, samples.carried


def check(rebaseline=False, release=False):
    forms = baseline_check.load_forms(Path(ROOT) / "canonical" / Y)
    found, shas = findings()
    due = [f for f in found if f["kind"] == "due"]
    if not release:
        found = [f for f in found if f["kind"] not in ("due", "short")]
        for f in due:
            print(f"  due at the next release: {f['line']}: {f['detail']}")
    data = json.loads(RULINGS.read_text()) if RULINGS.exists() else {}
    good = accepted(data.get("rulings", {}), shas)
    carry = carried(found, good)
    if carry:
        print(f"  {len(carry)} sample(s) carry the ruling of an equal sample on the same subject")
    with tempfile.TemporaryDirectory() as tmp:  # run() sees only the accepted and carried rulings
        view = Path(tmp) / RULINGS.name
        view.write_text(json.dumps({**data, "rulings": {**good, **carry}}))
        status = baseline_check.run(
            "screens", forms, found, view, Path(tmp) / "report.md" if release else REPORT, "Standing screen review",
            "Generated by `tools/transcription/check_screens.py` (T-088). `unruled`: a current sample "
            "(`<unit>#<sample>`) found NARROW, WIDE, SOURCE or UNCLEAR cases not yet ruled; a ruling with `carried_from` "
            "is carried from an equal sample. `orphan`: a recorded gate review whose gate is gone. `due` and `short` "
            "appear only in release mode.", rebaseline)
        if rebaseline:
            data["baseline"] = json.loads(view.read_text())["baseline"]
            RULINGS.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    if due and not release:
        with open(REPORT, "a", encoding="utf-8") as out:
            out.write("\n## Due at the next release\n\n" + "".join(f"- `{f['line']}`: {f['detail']}\n" for f in due))
    return status


if __name__ == "__main__":
    os.chdir(ROOT)
    import build_fresh
    build_fresh.require()
    sys.exit(check(rebaseline="--baseline" in sys.argv, release="--release" in sys.argv))
