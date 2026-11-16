#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Extract the mid-month straight-line tables for real property from the archived Pub. 946
into tables/<year>/macrs_mm.yaml.

Table A-6 (residential rental property, 27.5 years) and Table A-7a (nonresidential real
property, 39 years) give the rate for each month placed in service (columns 1 to 12) and
each year of recovery (rows). A printed range of years ("2–9", "2–39") is one row per year.
Years after the last printed year are written with rate 0 up to year 40, so that every
building placed in service from 1987 (or before) has a row: such a building is fully
depreciated. A rate keeps its printed precision (1.97% is 197/10000, 3.636% is
3636/100000).

Reads the layout text (pdftotext -layout) beside the archived PDF, whose hash is checked
against the manifest.

    python3 tools/extract_realty_tables.py           write the table
    python3 tools/extract_realty_tables.py --check   (in check-all) the committed table equals a fresh extraction,
                                                     and every month column totals exactly 100%
"""
import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
import archive_text  # noqa: E402

ARCHIVE = ROOT / "sources" / Y
OUT = ROOT / "tables" / Y / "macrs_mm.yaml"
VERSION = "0.1"
LAST_ROW = 40
TABLES = {"A-6": "residential", "A-7a": "nonresidential"}
NUM = re.compile(r"\d+\.\d+%?")
ROW = re.compile(r"\s*(\d{1,2})(?:\s*[–-]\s*(\d{1,2}))?\s+(?=\d)")


def rate(text):
    t = text.rstrip("%")
    whole, frac = t.split(".")
    return Fraction(int(whole + frac), 100 * 10 ** len(frac)), {"num": int(whole + frac), "den": 100 * 10 ** len(frac)}


def segment(pages, tag):
    """Lines from the heading "Table <tag>." to the next table heading or the page end."""
    for page in pages:
        lines = page.splitlines()
        for i, line in enumerate(lines):
            if re.match(rf"\s*Table {re.escape(tag)}\.", line):
                seg = []
                for nxt in lines[i:]:
                    if seg and re.match(r"\s*Table A-\d+[a-z]?\.", nxt):
                        break
                    seg.append(nxt)
                return seg
    raise SystemExit(f"Table {tag} not found in the layout text")


def columns(seg):
    """Character centre of each month heading 1 to 12: the first non-blank line after "Year"."""
    for i, line in enumerate(seg):
        if line.strip() == "Year":
            for head in seg[i + 1:]:
                if head.strip():
                    cols = {int(m.group()): (m.start() + m.end()) / 2 for m in re.finditer(r"\d+", head)}
                    if sorted(cols) != list(range(1, 13)):
                        raise SystemExit(f"month headings not read: {head!r}")
                    return cols
    raise SystemExit("no Year heading")


def extract(pages):
    out = {}
    for tag, kind in TABLES.items():
        seg = segment(pages, tag)
        cols = columns(seg)
        last = 0
        for line in seg:
            m = ROW.match(line)
            if not m:
                continue
            first = int(m.group(1))
            end = int(m.group(2) or first)
            got = {}
            for v in NUM.finditer(line, m.end() - 1):
                centre = (v.start() + v.end()) / 2
                month = min(cols, key=lambda k: abs(cols[k] - centre))
                if abs(cols[month] - centre) > 6 or month in got:
                    raise SystemExit(f"Table {tag}: value {v.group()!r} not placed in a month column: {line!r}")
                got[month] = v.group()
            for year in range(first, end + 1):
                for month in range(1, 13):
                    if month in got:
                        out[(kind, month, year)] = rate(got[month])
            last = max(last, end)
        for year in range(1, LAST_ROW + 1):
            for month in range(1, 13):
                if (kind, month, year) not in out:
                    if year <= last and not (year == last or year == last - 1):
                        raise SystemExit(f"Table {tag}: no rate for month {month}, year {year}")
                    out[(kind, month, year)] = (Fraction(0), {"num": 0, "den": 1})
    return out


def check_totals(rates):
    bad = []
    for kind in TABLES.values():
        for month in range(1, 13):
            total = sum(rates[(kind, month, y)][0] for y in range(1, LAST_ROW + 1))
            if total != 1:
                bad.append(f"{kind} month {month}: total {float(total) * 100:.3f}%")
    return bad


def render(rates, entry):
    lines = [
        f"# Mid-month straight-line MACRS tables for real property from the archived Pub. 946 ({Y}), Appendix A.",
        f"# Source: sources/{Y}/p946.pdf sha256 {entry['sha256']}",
        f"# Extractor: tools/extract_realty_tables.py v{VERSION}",
        "# Regenerate with: python3 tools/extract_realty_tables.py",
        "# Table A-6 (residential rental property, 27.5 years) and Table A-7a (nonresidential real property, 39 years).",
        f"# Years after the last printed year are rate 0 to year {LAST_ROW} (fully depreciated). A rate keeps its printed precision.",
        "table:",
        "  id: macrs_mm",
        "  kind: keyed",
        '  title: "MACRS mid-month straight-line tables for real property (Pub. 946, Tables A-6 and A-7a)"',
        f"  tax_year: {Y}",
        "  cite:",
        "    doc: p946",
        '    locator: "pp. 73-74, Table A-6, Residential Rental Property Mid-Month Convention Straight Line—27.5 Years; Table A-7a, Nonresidential Real Property Mid-Month Convention Straight Line—39 Years"',
        '    quote: "Month property placed in service"',
        "  keys:",
        "    - { name: kind, type: Enum(rprop_kind) }",
        "    - { name: month, type: Enum(month) }",
        "    - { name: year, type: Count }",
        "  cell: Rate",
        "  rows:",
    ]
    for kind in TABLES.values():
        for month in range(1, 13):
            for year in range(1, LAST_ROW + 1):
                r = rates[(kind, month, year)][1]
                lines.append(f"    - {{ keys: [{kind}, m{month}, {year}], value: {{ num: {r['num']}, den: {r['den']} }} }}")
    return "\n".join(lines) + "\n"


def main():
    manifest = {d["id"]: d for d in json.loads((ARCHIVE / "manifest.json").read_text())["documents"]}
    entry = manifest["p946"]
    pdf = ARCHIVE / entry["file"]
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != entry["sha256"]:
        raise SystemExit("p946.pdf does not match its manifest hash")
    pages = archive_text.read(ARCHIVE, entry).split("\f")
    rates = extract(pages)
    bad = check_totals(rates)
    text = render(rates, entry)
    if "--check" in sys.argv[1:]:
        problems = list(bad)
        if not OUT.exists():
            problems.append(f"{OUT.relative_to(ROOT)} is missing")
        elif OUT.read_text(encoding="utf-8") != text:
            problems.append(f"{OUT.relative_to(ROOT)} differs from a fresh extraction (rerun the extractor)")
        if problems:
            print("macrs_mm: FAIL\n  " + "\n  ".join(problems))
            raise SystemExit(1)
        print(f"macrs_mm: ok ({len(rates)} rates; every month column totals 100%)")
        return
    if bad:
        raise SystemExit("column totals are not 100%:\n  " + "\n  ".join(bad))
    OUT.write_text(text, encoding="utf-8")
    print(f"macrs_mm: {len(rates)} rates written; every month column totals 100%")


if __name__ == "__main__":
    main()
