#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Extract the 2025 New York State and New York City Tax Tables from the archived web page
(sources/ny/<year>/ny_it201_tax_tables.html; the tables exist only on the web, IT-201-I p. 12,
Line 39, "visit www.tax.ny.gov and search: table") into tables/ny/<year>/ny_tax_table.yaml and
ny_city_tax_table.yaml, in the shape of the federal Tax Table (tables/<year>/tax_table.yaml).

Each table is an HTML <table> whose <caption> is "New York State Tax Table" or "New York City Tax
Table"; each data row has five cells: at least, but less than, and the tax for "Single or Married
filing separately", "Married filing jointly*" (with a qualifying surviving spouse) and "Head of a
household". Amounts are whole dollars; spaces inside a number ("62, 050") are removed.

Checks (also run by --check, which re-extracts and compares with the committed files):
  - the bands are contiguous from $0 and end at $65,000 (the tables' printed limit:
    "$65,000 or more—compute your New York State tax using New York State tax rate schedule");
  - each band's tax, in each column, agrees with the rate schedule (params/ny/<year>.yaml,
    ny.rs.* and ny.city.*) applied at the band's midpoint and rounded half-up to the dollar; a
    band that does not is listed (a conjecture to test, as for the federal table: the source
    does not state how the tables were built).

The snapshot is read as published (its hash checked against the manifest); nothing in it is run.

    extract_ny_tax_table.py [--check]
"""
import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402

NYDIR = ROOT / "sources" / "ny" / Y
OUT = ROOT / "tables" / "ny" / Y
PARAMS = ROOT / "params" / "ny" / f"{Y}.yaml"
DOC = "ny_it201_tax_tables"
CAPTIONS = {"New York State Tax Table": "ny_tax_table", "New York City Tax Table": "ny_city_tax_table"}
LIMIT = 65000
COLUMNS = [("single", ["single", "mfs"], None),
           ("joint", ["mfj", "qss"], "This column must also be used by a qualifying surviving spouse."),
           ("hoh", ["hoh"], None)]


class Tables(HTMLParser):
    """Collect, per caption, the rows of five data cells."""

    def __init__(self):
        super().__init__()
        self.caption, self.in_caption, self.cell, self.row = None, False, None, None
        self.rows = {}

    def handle_starttag(self, tag, attrs):
        if tag == "caption":
            self.in_caption, self.caption = True, ""
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell = "" if tag == "td" else None

    def handle_endtag(self, tag):
        if tag == "caption":
            self.in_caption = False
            self.caption = " ".join(self.caption.split())
        elif tag == "td" and self.cell is not None and self.row is not None:
            self.row.append(self.cell)
            self.cell = None
        elif tag == "tr" and self.row is not None:
            if len(self.row) == 5 and self.caption in CAPTIONS:
                self.rows.setdefault(self.caption, []).append(self.row)
            self.row = None

    def handle_data(self, data):
        if self.in_caption:
            self.caption += data
        elif self.cell is not None:
            self.cell += data


def number(cell):
    s = re.sub(r"[\s$, ]", "", cell)
    if not re.fullmatch(r"\d+", s):
        raise ValueError(f"not a whole-dollar amount: {cell!r}")
    return int(s)


def snapshot():
    manifest = {d["id"]: d for d in json.loads((NYDIR / "manifest.json").read_text())["documents"]}
    entry = manifest[DOC]
    raw = (NYDIR / entry["file"]).read_bytes()  # the .html snapshot as published (not a text layer)
    if hashlib.sha256(raw).hexdigest() != entry["sha256"]:
        raise SystemExit(f"{DOC}: hash mismatch with the manifest")
    return raw.decode("utf-8"), entry["sha256"]


def extract():
    html, sha = snapshot()
    parser = Tables()
    parser.feed(html)
    out = {}
    for caption, table_id in CAPTIONS.items():
        bands = [[number(c) for c in row] for row in parser.rows.get(caption, [])]
        if not bands:
            raise SystemExit(f"no rows under the caption {caption!r}")
        expect = 0
        for b in bands:
            if b[0] != expect or b[1] <= b[0]:
                raise SystemExit(f"{table_id}: bands not contiguous at {b[0]} (expected {expect})")
            expect = b[1]
        if expect != LIMIT:
            raise SystemExit(f"{table_id}: last band ends at {expect}, not {LIMIT}")
        out[table_id] = bands
    return out, sha


def schedule(params, prefix, group):
    """[(over, upper or None, base, rate)] in whole dollars and Fractions, from params/ny."""
    values, rows, i = params["params"]["values"], [], 1
    while f"{prefix}.{group}.b{i}.over" in values:
        g = lambda k: values[f"{prefix}.{group}.b{i}.{k}"]["value"]  # noqa: E731
        upper = values.get(f"{prefix}.{group}.b{i}.upper")
        rate = values[f"{prefix}.b{i}.rate"]["value"]
        rows.append((Fraction(g("over"), 100), Fraction(upper["value"], 100) if upper else None,
                     Fraction(g("base"), 100), Fraction(rate["num"], rate["den"])))
        i += 1
    return rows


def tax_at(rows, x):
    for over, upper, base, rate in rows:
        if upper is None or x <= upper:
            exact = base + rate * (x - over)
            return int(exact + Fraction(1, 2)) if exact >= 0 else -int(-exact + Fraction(1, 2))
    raise ValueError(x)


def exact_at(rows, x):
    """The exact running tax (the sum of each band's rate times the part of x in it), ignoring the
    printed bases, which are that running tax rounded to the dollar (premise map 4.3)."""
    total = Fraction(0)
    for over, upper, _, rate in rows:
        if x > over:
            total += rate * ((x if upper is None else min(x, upper)) - over)
    return int(total + Fraction(1, 2))


def conjecture(tables):
    if not PARAMS.exists():
        return ["params/ny not written yet: conjecture not tested"], []
    params = yaml.safe_load(PARAMS.read_text())
    lines, unexplained = [], []
    for table_id, prefix in (("ny_tax_table", "ny.rs"), ("ny_city_tax_table", "ny.city")):
        groups = [schedule(params, prefix, g) for g in ("single", "mfj", "hoh")]
        misses, explained = [], 0
        for b in tables[table_id]:
            mid = Fraction(b[0] + b[1], 2)
            for col, rows in enumerate(groups):
                want = tax_at(rows, mid)
                if want != b[2 + col]:
                    if exact_at(rows, mid) == b[2 + col]:
                        explained += 1
                    else:
                        misses.append(f"{b[0]}-{b[1]} {COLUMNS[col][0]}: table {b[2 + col]}, schedule at midpoint {want}")
        lines.append(f"{table_id}: {len(tables[table_id])} bands x 3 columns; at the band midpoint, rounded half-up, "
                     f"{explained} cell(s) differ from the printed schedule by its rounded base and equal the exact "
                     f"running tax; {len(misses)} cell(s) unexplained")
        lines += [f"  {m}" for m in misses[:40]]
        if misses:
            unexplained.append(table_id)
    return lines, unexplained


def render(table_id, bands, sha):
    title = "2025 New York State Tax Table" if table_id == "ny_tax_table" else "2025 New York City Tax Table"
    heading = "2025 New York State Tax Table" if table_id == "ny_tax_table" else "New York City Tax Table"
    quote = ("If your New York adjusted gross income, Form IT-201, line 33 is more than $107,650, you cannot use these tables."
             if table_id == "ny_tax_table" else
             "$65,000 or more—compute your New York City tax using New York City tax rate schedule.")
    out = [f"# {title}, extracted from the archived web page (the tables are published only there).",
           f"# Source: sources/ny/{Y}/{DOC}.html sha256 {sha}",
           "# Extractor: tools/extract_ny_tax_table.py",
           "# Regenerate with: python3 tools/extract_ny_tax_table.py",
           "# Column order in each band's tax list: [single (and married filing separately), joint (and qualifying",
           "# surviving spouse), hoh]. Amounts in cents.",
           "table:",
           f"  id: {table_id}",
           "  kind: tax_table",
           f'  title: "{title}"',
           f"  tax_year: {Y}",
           "  cite:",
           f"    doc: {DOC}",
           f"    locator: '{heading}, \"At least\", \"But less than\", \"Single or Married filing separately\", \"Married filing jointly*\", \"Head of a household\"'",
           f"    quote: \"{quote}\"",
           "  bounds: { at_least: 0, less_than: %d }" % (LIMIT * 100),
           "  columns:"]
    for key, statuses, note in COLUMNS:
        out.append(f"    - {{ key: {key}, statuses: [{', '.join(statuses)}]" + (f', note: "{note}" }}' if note else " }"))
    out.append("  bands:")
    for b in bands:
        out.append(f"    - {{ at_least: {b[0] * 100}, less_than: {b[1] * 100}, tax: [{b[2] * 100}, {b[3] * 100}, {b[4] * 100}] }}")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="re-extract and compare with the committed tables; test the conjecture")
    a = ap.parse_args()
    tables, sha = extract()
    status = 0
    for table_id, bands in tables.items():
        text = render(table_id, bands, sha)
        path = OUT / f"{table_id}.yaml"
        if a.check:
            if not path.exists() or path.read_text() != text:
                print(f"{path.relative_to(ROOT)}: differs from a fresh extraction")
                status = 1
            else:
                print(f"{path.relative_to(ROOT)}: matches a fresh extraction ({len(bands)} bands)")
        else:
            OUT.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
            print(f"wrote {path.relative_to(ROOT)} ({len(bands)} bands)")
    lines, unexplained = conjecture(tables)
    for line in lines:
        print(line)
    return 1 if unexplained else status


if __name__ == "__main__":
    sys.exit(main())
