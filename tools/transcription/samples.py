#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Sampled standing reviews (completeness, screens): when a review is due, how many samples it needs, and which
findings carry an earlier ruling.

A sampled review behaves like a random sample of the gaps in its subject: each run finds a different subset. So a
subject is reviewed by SAMPLES_PER_MILESTONE independent samples, and their findings (the union) are ruled once.

- A record holds one subject (a hash of what is reviewed, without the reviewer's own instructions) and the samples
  run against it. Each sample records the hash of the instructions it ran under (`system_sha`).
- Between releases a record whose subject changed is `due`: reported, not failed. A release is refused while any
  subject is due, short of samples, or holds unruled findings (`--release` of the check scripts).
- A record marked `grandfathered` holds a single review made before sampling; it satisfies the milestone until its
  subject changes.
- A change to the reviewer's instructions does not make a subject due; it applies at the subject's next sample.
- A finding whose item and normalised quote equal those of a ruled finding on the same subject carries that ruling.
"""
import json
import re

SAMPLES_PER_MILESTONE = 1   # parsed samples a subject needs per release (the consolidation charter, section 4)


def parsed(record):
    """The samples of a record whose response parsed."""
    return [s for s in record.get("samples") or [] if not s.get("parse_error")]


def satisfied(record):
    """True when the record's subject needs no further sample this milestone."""
    return bool(record.get("grandfathered")) or len(parsed(record)) >= SAMPLES_PER_MILESTONE


def wanted(record, subject, asked=None):
    """(samples to run, whether that goes beyond the milestone). `asked` is an explicit --samples count."""
    have = len(parsed(record)) if record and record.get("subject_sha") == subject else 0
    full = bool(record and record.get("subject_sha") == subject and record.get("grandfathered"))
    need = 0 if full else max(SAMPLES_PER_MILESTONE - have, 0)
    n = need if asked is None else asked
    return n, n > need


def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def carry_key(item, quote):
    return (str(item), norm(quote))


def unit_findings(key, form, sha, r, why_changed, ok, rerun):
    """The findings of one reviewed unit (a screen, a gate) whose samples each give a verdict: `due` when its record
    is missing or on another subject; one `unruled` (`<key>#<k>`) per parsed sample whose verdict is not `ok`; `short`
    when it lacks the milestone's samples. `rerun` is the command that samples it."""
    if not r or r.get("subject_sha") != sha:
        why = "never reviewed" if not r else why_changed
        return [{"kind": "due", "line": key, "form": form, "subject": sha, "detail": f"{why}; run {rerun}"}]
    out = []
    for k, smp in enumerate(r.get("samples") or [], 1):
        if smp.get("parse_error"):
            print(f"  note: {key}: sample {k} did not parse and does not count")
        elif smp.get("verdict") != ok:
            out.append({"kind": "unruled", "line": f"{key}#{k}", "form": form, "subject": sha,
                        "carry": (smp.get("verdict"), norm(json.dumps(smp.get("findings") or [], sort_keys=True))),
                        "detail": f"verdict {smp.get('verdict')} with {len(smp.get('findings') or [])} finding(s); "
                                  f"adjudicate and rule with subject_sha {sha[:12]}"})
    if not satisfied(r):
        out.append({"kind": "short", "line": key, "form": form, "subject": sha,
                    "detail": f"{len(parsed(r))} of {SAMPLES_PER_MILESTONE} sample(s); run {rerun}"})
    return out


def unit_of(key):
    """The unit of a per-sample ruling key, unruled:<unit>#<k>."""
    return key.split(":", 1)[1].rsplit("#", 1)[0]


def accepted(rulings, shas):
    """The per-sample rulings whose subject_sha is their unit's current subject."""
    return {k: r for k, r in rulings.items() if isinstance(r, dict) and r.get("subject_sha") == shas.get(unit_of(k))}


def carried(found, rulings):
    """{key: ruling} for unruled samples equal (verdict and normalised findings) to a ruled sample of the same unit."""
    own = {}
    for f in found:
        k = "unruled:" + f["line"]
        if f["kind"] == "unruled" and k in rulings:
            own.setdefault((unit_of(k), f["carry"]), k)
    out = {}
    for f in found:
        k = "unruled:" + f["line"]
        src = own.get((unit_of(k), f.get("carry")))
        if f["kind"] == "unruled" and k not in rulings and src:
            out[k] = {**rulings[src], "carried_from": src}
    return out
