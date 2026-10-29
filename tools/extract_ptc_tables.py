#!/usr/bin/env python3
"""Pin the Form 8962 tables from the archived 2025 instructions, and check them.

Table 2 (Applicable Figure, i8962 p. 11) becomes `tables/2025/ptc_applicable_figure.yaml`, a keyed table
of Form 8962 line 5 (0 to 401) to a Rate: the printed rows 150 to 399, "less than 150" for every line 5
below 150, and the 0.0850 of the "400 or more" tip for 400 and 401 (line 5 is at most 401).

Tables 1-1 to 1-3 (Federal Poverty Line, i8962 pp. 8 and 9) become `tables/2025/ptc_poverty_line.yaml`,
keyed by the table (Enum ptc_fpl_table) and family size: the printed sizes 1 to 8, and sizes 9 to 20
by each table's footnote ("add $5,380 for each additional person", and so on).

Checks (`--check`, run by check-all): the files are what this extractor writes from the archived text;
every Table 2 row equals the derivation 0 at 150 or less, (p - 150) x 0.0004 to 300, and
0.06 + (p - 300) x 0.00025 half-up to four places above; every printed poverty amount and
increment is also printed in the HHS 2024 poverty guidelines (fr-2024-00796); the footnote extension
reproduces the size-11 examples of the instructions.

    python3 tools/extract_ptc_tables.py [--check]
"""
import argparse
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "2025"
OUT_FIG = ROOT / "tables" / "2025" / "ptc_applicable_figure.yaml"
OUT_FPL = ROOT / "tables" / "2025" / "ptc_poverty_line.yaml"
CAP = 400
MAX_SIZE = 20


def pages(doc, layer="txt"):
    return (SRC / f"{doc}.{layer}").read_text().split("\f")


def applicable_figures():
    page = pages("i8962")[10]
    rows = {}
    for p, fig in re.findall(r"(?<![\d.])(\d{3})\s+(0\.\d{4})(?!\d)", page):
        rows[int(p)] = fig
    if "less than 150" not in page or "If the amount on line 5 is 400 or more, your applicable" not in page:
        raise SystemExit("Table 2: the printed tip or the 'less than 150' row was not found")
    missing = [p for p in range(150, 400) if p not in rows]
    if missing or len([p for p in rows if 150 <= p <= 399]) != 250:
        raise SystemExit(f"Table 2: printed rows missing for {missing[:10]}")
    out = {}
    for p in range(0, CAP + 2):
        fig = "0.0000" if p < 150 else "0.0850" if p >= 400 else rows[p]
        out[p] = fig
    return out


def derived_figure(p):
    if p <= 150:
        return Fraction(0)
    if p <= 300:
        return Fraction(p - 150) * Fraction(4, 10000)
    x = Fraction(6, 100) + Fraction(p - 300) * Fraction(25, 100000)
    return Fraction(int(x * 10000 + Fraction(1, 2)), 10000)


def poverty_lines():
    text = pages("i8962")[7] + pages("i8962")[8]
    tables = {}
    for key, start in (("contiguous", "Table 1-1."), ("alaska", "Table 1-2."), ("hawaii", "Table 1-3.")):
        i = text.find(start)
        if i < 0:
            raise SystemExit(f"{start} not found")
        chunk = text[i:i + 6000]
        found = re.findall(r"(?<!\S)([1-8])\s{3,}\$([\d,]+)(?![\d,])", chunk)
        runs = [found[k:k + 8] for k in range(len(found) - 7) if [int(s) for s, _ in found[k:k + 8]] == list(range(1, 9))]
        if not runs:
            raise SystemExit(f"{start}: sizes 1 to 8 not found in order")
        pairs = runs[0]
        amounts = [int(a.replace(",", "")) for _, a in pairs]
        inc = re.search(r"add\s+\$([\d,]+)\s+for\s+each\s+additional", chunk)
        example = re.search(r"of\s+\$([\d,]+)\s+on\s+Form\s+8962,\s+line\s+4", chunk)
        if len(amounts) != 8 or not inc or not example:
            raise SystemExit(f"{start}: rows, increment or example not found")
        tables[key] = (amounts, int(inc.group(1).replace(",", "")), int(example.group(1).replace(",", "")))
    return tables


def write_fig(rows):
    lines = ["# Form 8962 Table 2, Applicable Figure (i8962 p. 11), keyed by Form 8962 line 5.",
             "# Written by tools/extract_ptc_tables.py from sources/2025/i8962.txt; checked by its --check (check-all).",
             "# Rows 150 to 399 as printed; below 150 the row 'less than 150' (and the tip, 150 or less); 400 and 401",
             "# the tip, 'If the amount on line 5 is 400 or more, your applicable figure is 0.0850' (line 5 is at most 401).",
             "table:", "  id: ptc_applicable_figure", "  kind: keyed",
             '  title: "Applicable figure (Form 8962 instructions, Table 2)"', "  tax_year: 2025", "  cite:", "    doc: i8962",
             '    locator: "p. 11, Table 2. Applicable Figure"',
             '    quote: "If the amount on line 5 is 150 or less, your applicable figure is 0.0000."',
             "  keys:", "    - { name: percent, type: Count }", "  cell: Rate", "  rows:"]
    for p, fig in rows.items():
        num = int(fig.replace("0.", "").lstrip("0") or "0")
        lines.append(f"    - {{ keys: [{p}], value: {{ num: {num}, den: 10000 }} }}")
    return "\n".join(lines) + "\n"


def write_fpl(tables):
    lines = ["# Form 8962 Tables 1-1 to 1-3, Federal Poverty Line (i8962 pp. 8 and 9; the 2024 poverty lines, used for 2025),",
             "# keyed by the table and the family size of Form 8962 line 1. Sizes 1 to 8 as printed; 9 to 20 by each table's",
             "# footnote. Written by tools/extract_ptc_tables.py; checked by its --check (check-all), including against the",
             "# HHS 2024 poverty guidelines (sources/2025/fr-2024-00796).",
             "table:", "  id: ptc_poverty_line", "  kind: keyed",
             '  title: "Federal poverty line (Form 8962 instructions, Tables 1-1 to 1-3)"', "  tax_year: 2025", "  cite:", "    doc: i8962",
             '    locator: "p. 8, Line 4, Table 1-1. Federal Poverty Line for the 48 Contiguous States and the District of Columbia; p. 9, Table 1-2. Federal Poverty Line for Alaska; p. 9, Table 1-3. Federal Poverty Line for Hawaii"',
             '    quote: "For 2025, the 2024 federal poverty lines are used for this purpose and are shown below."',
             "  keys:", "    - { name: table, type: Enum(ptc_fpl_table) }", "    - { name: size, type: Count }", "  cell: NonNegDollars", "  rows:"]
    for key, (amounts, inc, _) in tables.items():
        for size in range(1, MAX_SIZE + 1):
            dollars = amounts[size - 1] if size <= 8 else amounts[7] + (size - 8) * inc
            lines.append(f"    - {{ keys: [{key}, {size}], value: {dollars * 100} }}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    figs = applicable_figures()
    bad = [p for p, fig in figs.items() if 150 <= p <= 399 and Fraction(fig) != derived_figure(p)]
    if bad:
        raise SystemExit(f"Table 2 rows differ from the derivation: {bad[:10]}")
    tables = poverty_lines()
    hhs = (SRC / "fr-2024-00796.txt").read_text()
    for key, (amounts, inc, example) in tables.items():
        for x in amounts + [inc]:
            if not re.search(r"(?<![\d,])" + re.escape(f"{x:,}") + r"(?![\d,])", hhs):
                raise SystemExit(f"{key}: ${x:,} is not printed in the HHS 2024 poverty guidelines")
        if amounts[7] + 3 * inc != example:
            raise SystemExit(f"{key}: the footnote extension does not give the size-11 example")
        if any(amounts[s] != amounts[0] + s * inc for s in range(8)):
            raise SystemExit(f"{key}: the printed sizes are not linear in the footnote increment")
    fig_text, fpl_text = write_fig(figs), write_fpl(tables)
    if a.check:
        stale = [p.name for p, t in ((OUT_FIG, fig_text), (OUT_FPL, fpl_text)) if not p.exists() or p.read_text() != t]
        if stale:
            raise SystemExit(f"ptc tables differ from the archived text: {stale}; run tools/extract_ptc_tables.py")
        print("ptc tables: Table 2 (402 rows) and Tables 1-1 to 1-3 (sizes 1 to 20) match i8962, the derivation and the HHS guidelines")
        return
    OUT_FIG.write_text(fig_text)
    OUT_FPL.write_text(fpl_text)
    print(f"wrote {OUT_FIG.relative_to(ROOT)} and {OUT_FPL.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
