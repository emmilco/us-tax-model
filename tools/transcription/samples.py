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
import re

SAMPLES_PER_MILESTONE = 1   # set from the calibration run (phase 2); a subject needs this many parsed samples


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
