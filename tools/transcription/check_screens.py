#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Standing screen review (T-088), offline, in check-all.

Every scope screen (a yes/no input that lines name as a refusal gate) must have a current screen review: the hash of
the prompt screen_review.py would send now (the screen's question, each gated line's English and refusal, and the
pages they cite) must equal the `prompt_sha` recorded in reviews/<year>/screens/screen_review.json. A screen whose
question, gated lines or citations changed is `stale` and is rerun with
`python3 tools/transcription/screen_review.py --screens <id>`. A current review whose verdict is not COVERS is
`unruled` until its findings are adjudicated and ruled in reviews/<year>/screens/rulings.json under
"unruled:<screen>" with the `prompt_sha` of the review it rules (so a rerun needs a new ruling).

The hash a screen is current against is its subject: the prompt without the gate condition shown for a screen whose
input is gated (gates.py), recorded as `subject_sha` (an older record's `prompt_sha`, the same hash for an ungated
screen). Gating a screen's input therefore does not make its review stale.

A choose-guard gate (gates.py, keyed `gate:<condition>`) is reviewed by the same tool and recorded in the same file.
Its review is current while its subject (gates.subject: the condition's wording and line, each gate line and gated
input with their English and wording, citations included) equals the recorded `subject_sha`; the prompt's own text is
not part of it, so a change to the review prompt applies at each gate's next real change. A ruling of a gate's review
names the `prompt_sha` recorded with that review.

Screens that were stale or unruled when the check was introduced form the baseline (tools/baseline_check.py), each
held while its prompt is unchanged.

    check_screens.py [--baseline]
"""
import hashlib
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from screen_review import load_lines, screens, screen_subject, encoded_english, OUT  # noqa: E402
import gates  # noqa: E402
from transcribe import ROOT, manifest  # noqa: E402
from taxyear import Y  # noqa: E402
import baseline_check  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the screens of New York lines, reviews/ny/<year>/screens/)
import pending  # noqa: E402

RECORD = Path(OUT) / "screen_review.json"
RULINGS = Path(OUT) / "rulings.json"
REPORT = jurisdiction.ypath("reports", Y, "screen_currency.md")


def findings():
    lines = load_lines()
    mani = manifest()
    reviewed = {r["screen"]: r for r in json.loads(RECORD.read_text())} if RECORD.exists() else {}
    rulings = json.loads(RULINGS.read_text()).get("rulings", {}) if RULINGS.exists() else {}
    out = []
    waiting = pending.listed("screens")
    for screen in sorted(waiting & set(reviewed)):
        out.append({"kind": "pending", "line": screen, "form": lines[screen][0] if screen in lines else "?", "subject": "-",
                    "detail": f"reviewed but still listed as pending; remove it from {pending.name()}"})
    for screen, gated in screens(lines).items():
        sha = screen_subject(screen, gated, lines, mani)
        form = lines[screen][0]
        r = reviewed.get(screen)
        if not r and screen in waiting:
            print(f"  pending: {screen}: never reviewed (listed in {pending.name()})")
        elif not r or (r.get("subject_sha") or r.get("prompt_sha")) != sha:
            why = "never reviewed" if not r else "question, gated lines or their citations changed since the review"
            out.append({"kind": "stale", "line": screen, "form": form, "subject": sha,
                        "detail": f"{why}; rerun screen_review.py --screens {screen}"})
        elif r.get("verdict") != "COVERS":
            ruling = rulings.get(f"unruled:{screen}")
            # A ruling judges one review: it names the prompt hash of the review it ruled. A ruling of an earlier
            # review does not accept this one; the finding then has its own key, and the old ruling goes stale.
            kind = "rerun" if isinstance(ruling, dict) and ruling.get("prompt_sha") not in (None, r.get("prompt_sha")) else "unruled"
            out.append({"kind": kind, "line": screen, "form": form, "subject": sha,
                        "detail": f"verdict {r.get('verdict')} with {len(r.get('findings') or [])} finding(s); "
                                  f"adjudicate and rule with prompt_sha {str(r.get('prompt_sha'))[:12]}"})
    out.extend(gate_findings(lines, reviewed, rulings))
    return out


def gate_findings(lines, reviewed, rulings):
    """The currency of each choose-guard gate's screen review, and recorded gate reviews whose gate is gone."""
    out = []
    current = gates.units(lines)
    for key, unit in current.items():
        sha = gates.subject(unit, lines, encoded_english)
        form = gates.unit_form(unit, lines)
        r = reviewed.get(key)
        if not r or r.get("subject_sha") != sha:
            why = "never reviewed" if not r else "the condition's wording, the gated lines or their citations changed since the review"
            out.append({"kind": "stale", "line": key, "form": form, "subject": sha,
                        "detail": f"{why}; rerun screen_review.py --screens {key}"})
        elif r.get("verdict") != "COVERS":
            ruling = rulings.get(f"unruled:{key}")
            kind = "rerun" if isinstance(ruling, dict) and ruling.get("prompt_sha") not in (None, r.get("prompt_sha")) else "unruled"
            out.append({"kind": kind, "line": key, "form": form, "subject": sha,
                        "detail": f"verdict {r.get('verdict')} with {len(r.get('findings') or [])} finding(s); "
                                  f"adjudicate and rule with prompt_sha {str(r.get('prompt_sha'))[:12]}"})
    for key in sorted(k for k in reviewed if k.startswith("gate:") and k not in current):
        out.append({"kind": "orphan", "line": key, "form": "-", "subject": key,
                    "detail": "a recorded gate review whose gate no longer exists; remove it from screen_review.json"})
    return out


def check(rebaseline=False):
    forms = baseline_check.load_forms(Path(ROOT) / "canonical" / Y)
    return baseline_check.run(
        "screens", forms, findings(), RULINGS, REPORT, "Standing screen review",
        "Generated by `tools/transcription/check_screens.py` (T-088). `stale`: the screen's review prompt changed since "
        "it was reviewed (for a gate, its subject changed). `unruled`: a current review found NARROW, WIDE, SOURCE or UNCLEAR "
        "cases not yet ruled. `orphan`: a recorded gate review whose gate is gone.", rebaseline)


if __name__ == "__main__":
    os.chdir(ROOT)
    sys.exit(check(rebaseline="--baseline" in sys.argv))
