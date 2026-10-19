#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Extract the MACRS percentage tables this tool uses from the archived Pub. 946 into
tables/2025/macrs_gds.yaml.

Tables A-1 (half-year) and A-2 to A-5 (mid-quarter, by quarter placed in service) give
the GDS rates for 3-, 5-, 7-, 10-, 15- and 20-year property (200% declining balance,
150% for 15- and 20-year property). Tables A-8 (half-year) and A-9 to A-12 (mid-quarter)
give straight-line rates; only their 15-year column is taken, for qualified improvement
property. A rate keeps its printed precision: 33.33% is 3333/10000, 3.750% is 3750/100000.

Reads the layout text (pdftotext -layout) beside the archived PDF, whose hash is checked
against the manifest; prints nothing but a summary.

    python3 tools/extract_macrs_tables.py
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "sources" / "2025"
OUT = ROOT / "tables" / "2025" / "macrs_gds.yaml"
VERSION = "0.1"

DB = {"A-1": "hy", "A-2": "mq1", "A-3": "mq2", "A-4": "mq3", "A-5": "mq4"}
SL = {"A-8": "hy", "A-9": "mq1", "A-10": "mq2", "A-11": "mq3", "A-12": "mq4"}
DB_COLS = {"3-year": "y3", "5-year": "y5", "7-year": "y7", "10-year": "y10", "15-year": "y15", "20-year": "y20"}
NUM = re.compile(r"\d+\.\d+%?")


def rate(text):
    t = text.rstrip("%")
    whole, frac = t.split(".")
    den = 100 * 10 ** len(frac)
    return {"num": int(whole + frac), "den": den}


def segments(pages, tag):
    """Text from the line naming the table (or its continuation) to the next table heading."""
    out = []
    for page in pages:
        lines = page.splitlines()
        for i, line in enumerate(lines):
            if re.search(rf"Table {re.escape(tag)}\.", line):
                seg = []
                for nxt in lines[i:]:
                    if seg and re.search(r"Table A-\d+[a-z]?\.", nxt) and not re.search(rf"Table {re.escape(tag)}\.", nxt):
                        break
                    seg.append(nxt)
                out.append(seg)
    return out


def columns(seg):
    """Character centres of every column heading: the line after the one reading "Year"."""
    for i, line in enumerate(seg):
        if line.strip() == "Year":
            for head in seg[i + 1:]:
                if head.strip():
                    return {m.group(): (m.start() + m.end()) / 2 for m in re.finditer(r"\d+(?:\.\d+)?(?:-year)?", head)}
    return {}


def rows(seg, cols):
    out = []
    for line in seg:
        m = re.match(r"\s*(\d{1,2})\s+(?=\d)", line)
        if not m:
            continue
        year = int(m.group(1))
        for v in NUM.finditer(line, m.end() - 1):
            centre = (v.start() + v.end()) / 2
            key = min(cols, key=lambda k: abs(cols[k] - centre))
            if abs(cols[key] - centre) <= 6:
                out.append((key, year, rate(v.group())))
    return out


def main():
    manifest = {d["id"]: d for d in json.loads((ARCHIVE / "manifest.json").read_text())["documents"]}
    entry = manifest["p946"]
    pdf = ARCHIVE / entry["file"]
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != entry["sha256"]:
        raise SystemExit("p946.pdf does not match its manifest hash")
    pages = (ARCHIVE / entry["text_file"]).read_text(encoding="utf-8").split("\f")
    table = []
    for tag, conv in DB.items():
        for seg in segments(pages, tag):
            for label, year, r in rows(seg, columns(seg)):
                table.append((DB_COLS[label], conv, year, r))
    for tag, conv in SL.items():
        for seg in segments(pages, tag):
            for label, year, r in rows(seg, columns(seg)):
                if label == "15":
                    table.append(("y15sl", conv, year, r))
    seen = {}
    for period, conv, year, r in table:
        k = (period, conv, year)
        if k in seen and seen[k] != r:
            raise SystemExit(f"conflicting rates for {k}")
        seen[k] = r
    keys = sorted(seen, key=lambda k: (["y3", "y5", "y7", "y10", "y15", "y20", "y15sl"].index(k[0]), ["hy", "mq1", "mq2", "mq3", "mq4"].index(k[1]), k[2]))
    lines = [
        "# MACRS percentage tables (GDS) from the archived Pub. 946 (2025), Appendix A.",
        f"# Source: sources/2025/p946.pdf sha256 {entry['sha256']}",
        f"# Extractor: tools/extract_macrs_tables.py v{VERSION}",
        "# Regenerate with: python3 tools/extract_macrs_tables.py",
        "# Tables A-1 to A-5 (declining balance; all six recovery periods) and the 15-year column of Tables A-8 to A-12",
        "# (straight line, qualified improvement property, period y15sl). A rate keeps its printed precision.",
        "table:",
        "  id: macrs_gds",
        "  kind: keyed",
        '  title: "MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12)"',
        "  tax_year: 2025",
        "  cite:",
        "    doc: p946",
        '    locator: "Appendix A, Tables A-1 to A-5 and A-8 to A-12, pp. 71-81"',
        '    quote: "You must apply the rates in the percentage tables to your property\'s unadjusted basis."',
        "  keys:",
        "    - { name: period, type: Enum(macrs_period) }",
        "    - { name: convention, type: Enum(macrs_convention) }",
        "    - { name: year, type: Count }",
        "  cell: Rate",
        "  rows:",
    ]
    for k in keys:
        r = seen[k]
        lines.append(f"    - {{ keys: [{k[0]}, {k[1]}, {k[2]}], value: {{ num: {r['num']}, den: {r['den']} }} }}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    counts = {}
    for k in keys:
        counts[(k[0], k[1])] = counts.get((k[0], k[1]), 0) + 1
    print(f"macrs_gds: {len(keys)} rates; " + ", ".join(f"{p}/{c}:{n}" for (p, c), n in sorted(counts.items())))


if __name__ == "__main__":
    main()
