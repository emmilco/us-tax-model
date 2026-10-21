#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Extract the Tax Table from the archived IRS PDF into pinned data.

Reads word bounding boxes (pdftotext -bbox-layout) from the archived
`sources/<year>/i1040gi.pdf`, pages 68-79, and emits `tables/<year>/tax_table.yaml`.

The extraction is deterministic: the same PDF bytes and the same script
version produce the same table. Structural claims are validated before
writing: bands tile [0, 100000) with no gaps or overlaps, and every band
has four tax values. Duplicate band keys are rejected unless the duplicate
values are identical (the page-68 sample block repeats real rows).

This is a transcription aid, not an evaluator: the Tax Table midpoint
conjecture is tested separately from the emitted data.
"""

import datetime
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
PDF = ROOT / "sources" / Y / "i1040gi.pdf"
MANIFEST = ROOT / "sources" / Y / "manifest.json"
OUT = ROOT / "tables" / Y / "tax_table.yaml"

FIRST_PAGE, LAST_PAGE = 68, 79  # PDF pages (1-based) of the Tax Table in the 2025 i1040gi; unverified for other years
TOOL_VERSION = "0.1"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_words(xhtml_path):
    """Parse pdftotext -bbox-layout XHTML into (page, x_center, y, text) words."""
    text = xhtml_path.read_text(encoding="utf-8")
    words = []
    page_no = 0
    for m in re.finditer(
        r'<page[^>]*>|<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',
        text,
        re.S,
    ):
        if m.group(0).startswith("<page"):
            page_no += 1
            continue
        x1, y, x2, txt = float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(5)
        txt = txt.strip()
        if txt:
            words.append((page_no, (x1 + x2) / 2.0, y, txt))
    return words


def numeric(tok):
    if not re.fullmatch(r"\d{1,3}(,\d{3})*", tok):
        return None
    return int(tok.replace(",", ""))


def cluster_columns(words):
    """Cluster word xMin positions into vertical column centers.

    Header words, footers and page furniture are ignored by clustering all
    words on the table pages; data columns are the clusters that receive
    numeric tokens repeated on many rows. We instead take a direct route:
    cluster all xMin values within a 2.0 tolerance and keep clusters hit by
    at least 20 words.
    """
    xs = sorted(w[1] for w in words)
    clusters = []  # [center, count]
    for x in xs:
        if clusters and x - clusters[-1][0] <= 6.0:
            c = clusters[-1]
            c[0] += (x - c[0]) / (c[1] + 1)
            c[1] += 1
        else:
            clusters.append([x, 1])
    kept = [c for c in clusters if c[1] >= 50]
    print(f"column clusters (>=50 hits): {len(kept)}")
    for c in kept:
        print(f"  center={c[0]:8.2f} hits={c[1]}")
    return kept


def main():
    if not PDF.exists():
        sys.exit(f"missing {PDF}")
    with tempfile.TemporaryDirectory() as tmp:
        xhtml = Path(tmp) / "tax_table.xhtml"
        subprocess.run(
            ["pdftotext", "-bbox-layout", "-f", str(FIRST_PAGE), "-l", str(LAST_PAGE), str(PDF), str(xhtml)],
            check=True,
        )
        words = extract_words(xhtml)

    # Keep numeric words only; they are the table cells and the example block.
    numeric_words = []
    for page, x, y, tok in words:
        v = numeric(tok)
        if v is not None:
            numeric_words.append((page, x, y, v))

    clusters = cluster_columns(numeric_words)
    centers = [c[0] for c in clusters]  # sorted by construction
    if len(centers) != 18:
        sys.exit(f"expected exactly 18 numeric columns, found {len(centers)}: {centers}")

    n_groups = len(centers) // 6
    groups = []
    for g in range(n_groups):
        groups.append(centers[g * 6 : (g + 1) * 6])

    def col_of(x):
        """Return (group, column) for a word x position, or None."""
        best = None
        for gi, cols in enumerate(groups):
            for ci, cx in enumerate(cols):
                d = abs(x - cx)
                if d <= 8.0 and (best is None or d < best[0]):
                    best = (d, gi, ci)
        return None if best is None else (best[1], best[2])

    # Row anchoring: each row is anchored by its 'at' column token.
    rows = []  # (at, less, s, j, f, h, page, y)
    for page, x, y, v in numeric_words:
        gc = col_of(x)
        if gc is None:
            continue
        gi, ci = gc
        if ci != 0:
            continue
        anchor_y = y
        cells = {}
        for page2, x2, y2, v2 in numeric_words:
            if page2 != page:
                continue
            if abs(y2 - anchor_y) > 8.0:
                continue
            gc2 = col_of(x2)
            if gc2 is None or gc2[0] != gi:
                continue
            ci2 = gc2[1]
            if ci2 == 0:
                continue
            d = abs(y2 - anchor_y)
            if ci2 not in cells or d < cells[ci2][0]:
                cells[ci2] = (d, v2)
        if set(cells) != {1, 2, 3, 4, 5}:
            print(f"warning: incomplete row at page {page} y={anchor_y:.1f}: cols {sorted(cells)}", file=sys.stderr)
            continue
        rows.append((v, cells[1][1], cells[2][1], cells[3][1], cells[4][1], cells[5][1], page, anchor_y))

    # Deduplicate by (at, less); identical duplicates are the page-68 sample.
    by_key = {}
    conflicts = []
    for at, less, s, j, f, h, page, y in rows:
        key = (at, less)
        if key in by_key and by_key[key][:4] != (s, j, f, h):
            conflicts.append((key, by_key[key], (s, j, f, h), page, y))
        else:
            by_key[key] = (s, j, f, h)
    if conflicts:
        for c in conflicts:
            print(f"conflict: {c}", file=sys.stderr)
        sys.exit(f"{len(conflicts)} conflicting duplicate bands; resolve before writing")

    # Expected tiling: 0-5, 5-15, 15-25, 25 by 25 to 3000, 50 by 50 to 100000.
    expected = [(0, 5), (5, 15), (15, 25)]
    b = 25
    while b < 3000:
        expected.append((b, b + 25))
        b += 25
    while b < 100000:
        expected.append((b, b + 50))
        b += 50
    missing = [k for k in expected if k not in by_key]
    extra = [k for k in by_key if k not in set(expected)]
    if missing or extra:
        print(f"missing bands: {missing[:10]} ({len(missing)})", file=sys.stderr)
        print(f"unexpected bands: {extra[:10]} ({len(extra)})", file=sys.stderr)
        sys.exit("tiling mismatch; resolve before writing")

    manifest = json.loads(MANIFEST.read_text())
    src = next(d for d in manifest["documents"] if d["id"] == "i1040gi")

    lines = []
    lines.append(f"# {Y} Tax Table, extracted from the archived IRS PDF.")
    lines.append(f"# Source: sources/{Y}/i1040gi.pdf sha256 {sha256(PDF)}")
    lines.append(f"# Extractor: tools/extract_tax_table.py v{TOOL_VERSION}, {datetime.date.today().isoformat()}")
    lines.append("# Regenerate with: python3 tools/extract_tax_table.py")
    lines.append("# Column order in each band's tax list: [single, joint, mfs, hoh].")
    lines.append("table:")
    lines.append("  id: tax_table")
    lines.append("  kind: tax_table")
    lines.append(f'  title: "{Y} Tax Table"')
    lines.append(f"  tax_year: {Y}")
    lines.append("  cite:")
    lines.append("    doc: i1040gi")
    lines.append(f'    locator: "{Y} Tax Table, pp. {FIRST_PAGE}-{LAST_PAGE}"')
    lines.append('    quote: "See the instructions for line 16 to see if you must use the Tax Table below to figure your tax."')
    lines.append("  columns:")
    lines.append("    - { key: single, statuses: [single] }")
    lines.append("    - { key: joint, statuses: [mfj, qss], note: \"This column must also be used by a qualifying surviving spouse.\" }")
    lines.append("    - { key: mfs, statuses: [mfs] }")
    lines.append("    - { key: hoh, statuses: [hoh] }")
    lines.append("  bands:")
    for at, less in expected:
        s, j, f, h = by_key[(at, less)]
        lines.append(f"    - {{ at_least: {at * 100}, less_than: {less * 100}, tax: [{s * 100}, {j * 100}, {f * 100}, {h * 100}] }}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {OUT} with {len(expected)} bands")
    print(f"rows read from PDF (after dedupe): {len(by_key)}")
    print(f"duplicate rows collapsed: {len(rows) - len(by_key)}")
    for probe in [(0, 5), (25200, 25250), (11900, 11925), (99550, 100000)]:
        if probe in by_key:
            print(f"  band {probe}: {by_key[probe]}")
    print(f"source sha256: {src['sha256']}")


if __name__ == "__main__":
    main()
