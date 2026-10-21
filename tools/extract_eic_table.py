#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Extract the Earned Income Credit (EIC) Table from the archived IRS PDF into pinned data.

Reads word boxes (pdftotext -bbox-layout) from `sources/<year>/i1040gi.pdf`, pages 49-60, and
writes one table per number of qualifying children: `tables/<year>/eic_0.yaml` ... `eic_3.yaml`.
Each table has two columns, as printed: "Single, head of household, or qualifying surviving
spouse" (which the table's star note also gives to married filing separately) and "Married
filing jointly".

Every page prints two halves of ten numeric columns (at least, but less than, four credits for
the first status group, four for joint filers), right-aligned at fixed positions. A row is kept
only when every cell of its half is present, so the worked example at the top of page 49 is not
read as data. Rows must tile [$1, $68,700) in $50 steps ($1 to $50 first).

A cell printed as `*`, `**` or `***` refers to a footnote of the form "If the amount you are
looking up from the worksheet is at least $A but less than $B, and you have <n> qualifying
children ..., your credit is $C. If the amount ... is $B or more ... you can't take the credit."
Such a row becomes two bands in that child count's table, split at $B: credit $C below, $0 at
or above (the credit is not available there). The footnote's child count must match the
column of the star.

The extraction is deterministic for the same PDF bytes and script version.
"""

import datetime
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
PDF = ROOT / "sources" / Y / "i1040gi.pdf"
OUT_DIR = ROOT / "tables" / Y
FIRST_PAGE, LAST_PAGE = 49, 60
TOOL_VERSION = "0.1"
# Right edges (points) of the twenty numeric columns, the same on every table page.
EDGES = [76, 109, 133, 157, 180, 204, 228, 251, 275, 301, 342, 375, 399, 423, 446, 470, 494, 517, 541, 567]
EDGE_TOLERANCE = 4.0
ROW_TOLERANCE = 3.0
START, END, STEP = 1, 68700, 50
COUNTS = {"no": 0, "one": 1, "two": 2, "three": 3}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def money(tok):
    return int(tok.replace(",", "")) if re.fullmatch(r"\d{1,3}(,\d{3})*", tok) else None


def read_pages():
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "eic.html"
        subprocess.run(["pdftotext", "-bbox-layout", "-f", str(FIRST_PAGE), "-l", str(LAST_PAGE), str(PDF), str(out)], check=True)
        text = out.read_text(encoding="utf-8")
    pages = []
    for body in re.findall(r"<page[^>]*>(.*?)</page>", text, re.S):
        words = [(float(x1), float(y), w) for x1, y, w in re.findall(
            r'<word xMin="[\d.]+" yMin="([\d.]+)" xMax="([\d.]+)" yMax="[\d.]+">([^<]+)</word>', body)]
        # findall returns (yMin, xMax, word); reorder to (xMax, yMin, word)
        pages.append([(x, y, w) for y, x, w in words])
    return pages


def column(x):
    best = min(range(len(EDGES)), key=lambda i: abs(EDGES[i] - x))
    return best if abs(EDGES[best] - x) <= EDGE_TOLERANCE else None


def rows_of(page_no, words):
    """[(at_least, less_than, [eight cells], page)] for the complete rows of one page."""
    cells = [(column(x), y, w) for x, y, w in words if (money(w) is not None or re.fullmatch(r"\*{1,3}", w))]
    cells = [c for c in cells if c[0] is not None]
    out = []
    for half in (0, 10):
        anchors = [(y, w) for c, y, w in cells if c == half and money(w) is not None]
        for ay, aw in anchors:
            row = {}
            for c, y, w in cells:
                if half <= c < half + 10 and abs(y - ay) <= ROW_TOLERANCE:
                    row.setdefault(c - half, w)
            if len(row) == 10 and money(row[1]) is not None:
                out.append((money(aw), money(row[1]), [row[i] for i in range(2, 10)], page_no))
    return out


def footnotes(pages):
    """{(page, marker): (at_least, threshold, children, credit)}. The marker glyph sits between
    the footnote's lines, so the text is read without it; the footnotes of a page are printed in
    marker order (*, **, ***) and take their markers by position. main() checks every footnote
    against the row and column of its starred cell."""
    notes = {}
    for page_no, words in pages:
        text = " ".join(w for _, _, w in sorted(words, key=lambda t: (round(t[1]), t[0])) if not re.fullmatch(r"\*{1,3}", w))
        found = re.findall(r"If the amount you are looking up from the worksheet is at least \$([\d,]+) but less than "
                           r"\$([\d,]+), and you have (no|one|two|three) qualifying child(?:ren)? who (?:has|have) a? ?valid\s+SSNs?, "
                           r"your credit is \$([\d,]+)\.", text)
        for i, (a, b, n, c) in enumerate(found):
            notes[(page_no, "*" * (i + 1))] = (money(a), money(b), COUNTS[n], money(c))
    return notes


def main():
    if not PDF.exists():
        sys.exit(f"missing {PDF}")
    pages = list(zip(range(FIRST_PAGE, LAST_PAGE + 1), read_pages()))
    rows = [r for page_no, words in pages for r in rows_of(page_no, words)]
    notes = footnotes(pages)

    by_key, conflicts = {}, []
    for at, less, vals, page_no in rows:
        if (at, less) in by_key and by_key[(at, less)][0] != vals:
            conflicts.append(((at, less), by_key[(at, less)], vals))
        by_key[(at, less)] = (vals, page_no)
    if conflicts:
        sys.exit(f"conflicting duplicate rows: {conflicts[:3]}")
    expected = [(START, STEP)] + [(a, a + STEP) for a in range(STEP, END, STEP)]
    missing = [k for k in expected if k not in by_key]
    extra = [k for k in by_key if k not in set(expected)]
    if missing or extra:
        sys.exit(f"tiling mismatch: missing {missing[:5]} ({len(missing)}), unexpected {extra[:5]} ({len(extra)})")

    # bands[k] = [(at_least, less_than, [other, joint])] in dollars
    bands = {k: [] for k in range(4)}
    used = set()
    for at, less in expected:
        vals, page_no = by_key[(at, less)]
        for k in range(4):
            other, joint = vals[k], vals[4 + k]
            stars = [(i, v) for i, v in ((0, other), (1, joint)) if money(v) is None]
            if not stars:
                bands[k].append((at, less, [money(other), money(joint)]))
                continue
            if len(stars) > 1:
                sys.exit(f"row {at}-{less}, {k} children: more than one footnote cell")
            col, marker = stars[0]
            note = notes.get((page_no, marker))
            if note is None:
                sys.exit(f"row {at}-{less} page {page_no}: no footnote text for {marker}")
            n_at, threshold, n_children, credit = note
            if n_at != at or n_children != k or not (at < threshold < less):
                sys.exit(f"footnote {marker} on page {page_no} ({note}) does not fit row {at}-{less}, {k} children")
            used.add((page_no, marker))
            low, high = [money(other), money(joint)], [money(other), money(joint)]
            low[col], high[col] = credit, 0
            bands[k].append((at, threshold, low))
            bands[k].append((threshold, less, high))
    unused = set(notes) - used
    if unused:
        sys.exit(f"footnotes not attached to a cell: {sorted(unused)}")

    status_words = {0: "no qualifying children", 1: "one qualifying child", 2: "two qualifying children", 3: "three or more qualifying children"}
    for k in range(4):
        out = OUT_DIR / f"eic_{k}.yaml"
        lines = [
            f"# {Y} Earned Income Credit (EIC) Table, {status_words[k]} who have valid SSNs, extracted from the archived IRS PDF.",
            f"# Source: sources/{Y}/i1040gi.pdf sha256 {sha256(PDF)}",
            f"# Extractor: tools/extract_eic_table.py v{TOOL_VERSION}, {datetime.date.today().isoformat()}",
            "# Regenerate with: python3 tools/extract_eic_table.py",
            "# Column order in each band's credit list: [single, head of household, qualifying surviving spouse or married",
            "# filing separately; married filing jointly]. A footnoted row is split at the footnote's amount.",
            "table:",
            f"  id: eic_{k}",
            "  kind: tax_table",
            f'  title: "{Y} Earned Income Credit (EIC) Table — {status_words[k]}"',
            f"  tax_year: {Y}",
            "  cite:",
            "    doc: i1040gi",
            f'    locator: "{Y} Earned Income Credit (EIC) Table, pp. 49-60"',
            '    quote: "Then, go to the column that includes your filing status and the number of qualifying children you have who have valid SSNs as defined earlier."',
            f"  bounds: {{ at_least: {START * 100}, less_than: {END * 100} }}",
            "  columns:",
            '    - { key: other, statuses: [single, hoh, qss, mfs], note: "Single, head of household, or qualifying surviving spouse; the star note gives this column to married filing separately." }',
            "    - { key: joint, statuses: [mfj] }",
            "  bands:",
        ]
        for at, less, (o, j) in bands[k]:
            lines.append(f"    - {{ at_least: {at * 100}, less_than: {less * 100}, tax: [{o * 100}, {j * 100}] }}")
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}: {len(bands[k])} bands")
    print(f"rows read: {len(by_key)}; footnotes attached: {len(used)}: {sorted(notes.values())}")


if __name__ == "__main__":
    main()
