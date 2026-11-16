#!/usr/bin/env python3
"""Compare lane V2 check outputs between two steps: fixture FAIL sets and problem lines of the other checks.
Usage: cmp.py BASE_STEP NEW_STEP"""
import re
import sys
from pathlib import Path

D = Path(__file__).parent
a, b = D / sys.argv[1], D / sys.argv[2]
NOISE = re.compile(r"(\d+(\.\d+)? s\b|walked \(|time: |rows of \d+ file|generated return|worker)")


def fails(p):
    if not p.exists():
        return None
    return {l.split()[1].rstrip(":") for l in p.read_text().splitlines() if l.startswith("FAIL")}


def lines(p):
    if not p.exists():
        return None
    return {l.strip() for l in p.read_text().splitlines() if l.strip() and not NOISE.search(l)}


for f in ("test_fixtures", "test_fixtures_ny"):
    x, y = fails(a / f"{f}.txt"), fails(b / f"{f}.txt")
    tail = [l for l in (b / f"{f}.txt").read_text().splitlines() if l.startswith("fixtures:")] if (b / f"{f}.txt").exists() else []
    print(f"== {f}: {tail[-1] if tail else '?'}")
    if x is None or y is None:
        print("  missing"); continue
    for c in sorted(y - x):
        print(f"  NEW FAIL {c}")
    for c in sorted(x - y):
        print(f"  fixed    {c}")
for f in ("interview_coverage", "interview_coverage_ny", "interview_rules", "tick_groups", "walk", "walk_ny"):
    x, y = lines(a / f"{f}.txt"), lines(b / f"{f}.txt")
    print(f"== {f}")
    if x is None or y is None:
        print("  missing"); continue
    for l in sorted(y - x):
        print(f"  + {l[:400]}")
    for l in sorted(x - y):
        print(f"  - {l[:400]}")
for s in ("walk", "walk-ny"):
    x, y = a / s / "SUMMARY.md", b / s / "SUMMARY.md"
    if x.exists() and y.exists():
        xl, yl = set(x.read_text().splitlines()), set(y.read_text().splitlines())
        print(f"== {s}/SUMMARY.md rows changed: {len(yl - xl)}")
        for l in sorted(yl - xl):
            print(f"  + {l[:300]}")
        for l in sorted(xl - yl):
            print(f"  - {l[:300]}")
