#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Extract the New York State and New York City household credit tables of a tax year from the archived web
edition of IT-201-I (sources/ny/<year>/ny_it201i-html.html; the PDF's columns are scattered, so the web edition is
read) into tables/ny/<year>/: State table 1 (filing status 1, single) as ny_hh_state_t1, State table 2 (filing
statuses 2, 4 and 5) as one table per people column, ny_hh_state_t2_p1 to _p7, and the City tables 4 and 5 the same
way (ny_hh_city_t4, ny_hh_city_t5_p1 to _p7). Tables 3 and 6 (married filing separately) are not extracted: the
return refuses that status where a credit is allowed. The "over 7" column (Note 3) is not extracted either: the
return refuses more than seven people where a credit is allowed.

Each table is an HTML <table> whose <caption> starts "New York State household credit table N" or "New York City
household credit table N". Its rows are the printed "Over / but not over" bands of federal adjusted gross income in
whole dollars: the first row's "Over" cell is "$ (see Note 2)" (Note 2: "This amount could be 0 or a negative
amount."), so it starts at zero; over X and not over Y is the band [X + 1 cent, Y + 1 cent); the last row is
"Over X" with "No credit is allowed; do not make an entry on Form IT-201, line N" (its full stop printed in some
tables only) across the other cells, the band from X + 1 cent upward with no credit. Bands must be contiguous.
The citation's quote is that sentence with its full stop, as table 1 prints it.

Checks, each stopping the extraction with what it found:
  - the caption, the header cells the citation's locator quotes, the last row's "No credit is allowed" sentence and
    the Notes 1 to 3 the files' comments rely on are printed as expected;
  - a table with columns has the columns 1 to 7 and "over 7" in that order;
  - every amount is whole dollars.
--check re-extracts and compares with the committed files byte for byte; a difference is printed, never written.

The snapshot is read as published (its hash checked against the manifest); nothing in it is run.

    extract_ny_household_tables.py [--check] [--year N]
"""
import argparse
import hashlib
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402

jurisdiction.ny_only("extract_ny_household_tables")
NYDIR = ROOT / "sources" / "ny" / Y
OUT = ROOT / "tables" / "ny" / Y
DOC = "ny_it201i-html"
TOP = 100000000000000  # the open upper bound of the last band, in cents
NOTES = {"Note 1": "For most taxpayers, federal adjusted gross income is the amount from Form IT-201, line 19.",
         "Note 2": "This amount could be 0 or a negative amount.",
         "Note 3": "For each individual over 7, add the amount in this column to the column 7 amount."}
PEOPLE = ("And the number of dependents listed on Form IT-201, item H, plus one for you (and one for your spouse "
          "if Married filing joint return) is:")

# (id, caption start, IT-201 line, the header cells the locator quotes, the title, the last comment line) of each
# printed table. A table whose last comment line has "{n}" has the people columns 1 to 7, one file each.
TABLES = [
    ("ny_hh_state_t1", "New York State household credit table 1", 40,
     ["If your federal adjusted gross income (see Note 1) is over:", "but not over", "enter on Form IT-201, line 40:"],
     "New York State household credit table 1 (Filing status ① only, Single)",
     "One column: the table is for filing status ① only; the line chooses it only for a single filer (the column "
     "lists every status because a tax table must cover them)."),
    ("ny_hh_state_t2", "New York State household credit table 2", 40, [PEOPLE, "Enter on Form IT-201, line 40:"],
     "New York State household credit table 2 (Filing status ②, ④ and ⑤), column {n}",
     "Column {n} of the printed table (that many people: item H dependents plus one for you and one for your spouse "
     "on a joint return); the line chooses the column, the \"over 7\" column (Note 3) is refused where a credit is "
     "allowed."),
    ("ny_hh_city_t4", "New York City household credit table 4", 48,
     ["If your federal adjusted gross income (see Note 1) is:", "enter on Form IT-201, line 48:"],
     "New York City household credit table 4 (Filing status ① only, Single)",
     "One column: the table is for filing status ① only; the line chooses it only for a single filer."),
    ("ny_hh_city_t5", "New York City household credit table 5", 48, [PEOPLE, "Enter on Form IT-201, line 48:"],
     "New York City household credit table 5 (Filing status ②, ④ and ⑤), column {n}",
     "Column {n} of the printed table (that many people); the line chooses the column, the \"over 7\" column "
     "(Note 3) is refused where a credit is allowed."),
]
COLUMN_HEADS = ["1", "2", "3", "4", "5", "6", "7", "over 7 (see Note 3)"]


def text_of(fragment):
    """An HTML fragment as text: tags dropped (a line break as a space), entities decoded, spaces collapsed."""
    fragment = re.sub(r"<br\s*/?>", " ", fragment)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", fragment)).split())


class Tables(HTMLParser):
    """Each <table>: its caption and its rows, a row being [(tag, colspan, text)] of its th and td cells."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tables, self.raw, self.cell, self.in_caption = [], None, None, False

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.tables.append({"caption": "", "rows": []})
        elif not self.tables:
            return
        elif tag == "caption":
            self.in_caption, self.raw = True, ""
        elif tag == "tr":
            self.tables[-1]["rows"].append([])
        elif tag in ("th", "td"):
            self.cell, self.raw = (tag, int(dict(attrs).get("colspan") or 1)), ""
        elif tag == "br" and self.raw is not None:
            self.raw += "<br>"

    def handle_endtag(self, tag):
        if tag == "caption" and self.in_caption:
            self.tables[-1]["caption"], self.in_caption, self.raw = text_of(self.raw), False, None
        elif tag in ("th", "td") and self.cell is not None:
            self.tables[-1]["rows"][-1].append((*self.cell, text_of(self.raw)))
            self.cell, self.raw = None, None

    def handle_data(self, data):
        if self.raw is not None:
            self.raw += data

    def handle_entityref(self, name):
        self.handle_data(f"&{name};")

    def handle_charref(self, name):
        self.handle_data(f"&#{name};")


def snapshot():
    """(the page's HTML, its derived text), each hash checked against the manifest."""
    if not (NYDIR / "manifest.json").exists():
        raise SystemExit(f"no New York archive for {Y}: sources/ny/{Y}/manifest.json does not exist")
    manifest = {d["id"]: d for d in json.loads((NYDIR / "manifest.json").read_text())["documents"]}
    if DOC not in manifest:
        raise SystemExit(f"{DOC} is not archived for {Y} (sources/ny/{Y}/manifest.json)")
    entry = manifest[DOC]
    out = []
    for key, sha in (("file", "sha256"), ("text_file", "text_sha256")):
        raw = (NYDIR / entry[key]).read_bytes()
        if hashlib.sha256(raw).hexdigest() != entry[sha]:
            raise SystemExit(f"{DOC}: {entry[key]} hash mismatch with the manifest")
        out.append(raw.decode("utf-8"))
    return out


def dollars(cell, what):
    s = re.sub(r"[\s$,]", "", cell)
    if not re.fullmatch(r"\d+", s):
        raise SystemExit(f"{what}: not a whole-dollar amount: {cell!r}")
    return int(s)


def bands_of(table_id, rows, line, columns):
    """[(at_least, less_than, [amount per column])] in cents, from the table's data rows."""
    data = [r for r in rows if all(tag == "td" for tag, _, _ in r)]
    none = f"No credit is allowed; do not make an entry on Form IT-201, line {line}."
    bands, at = [], 0
    for i, r in enumerate(data):
        cells = [t for _, _, t in r]
        if i == 0:
            if cells[0] != "$ (see Note 2)":
                raise SystemExit(f"{table_id}: first row starts {cells[0]!r}, not '$ (see Note 2)'")
        elif dollars(cells[0], table_id) * 100 + 1 != at:
            raise SystemExit(f"{table_id}: bands not contiguous at {cells[0]!r}")
        if i == len(data) - 1:
            if [c.rstrip(".") for c in cells[1:]] != [none.rstrip(".")] or r[1][1] != columns + 1:
                raise SystemExit(f"{table_id}: last row is not 'Over X' and {none!r}: {cells}")
            bands.append((at, TOP, [0] * columns))
            break
        if len(cells) != 2 + columns + (1 if columns > 1 else 0):
            raise SystemExit(f"{table_id}: row {i + 1} has {len(cells)} cells")
        upper = dollars(cells[1], table_id) * 100 + 1
        bands.append((at, upper, [dollars(c, table_id) * 100 for c in cells[2:2 + columns]]))
        at = upper
    return bands


def extract():
    page, text = snapshot()
    for note, sentence in NOTES.items():
        if f"{note} {sentence}" not in text:
            raise SystemExit(f"{DOC}: '{note} {sentence}' is not printed")
    parser = Tables()
    parser.feed(page)
    out = {}
    for table_id, caption, line, quoted, title, comment in TABLES:
        found = [t for t in parser.tables if t["caption"].startswith(caption + "—")]
        if len(found) != 1:
            raise SystemExit(f"{DOC}: {len(found)} tables captioned {caption!r}")
        t = found[0]
        heads = [c for r in t["rows"] for tag, _, c in r if tag == "th"]
        for q in quoted:
            if q not in heads:
                raise SystemExit(f"{table_id}: header cell {q!r} not printed (headers: {heads})")
        columns = 7 if "{n}" in comment else 1
        if columns > 1 and [h for h in heads if h in COLUMN_HEADS] != COLUMN_HEADS:
            raise SystemExit(f"{table_id}: people columns are not 1 to 7 and 'over 7': {heads}")
        bands = bands_of(table_id, t["rows"], line, columns)
        locator = t["caption"] + ", " + ", ".join(f'"{q}"' for q in quoted)
        for n in range(1, columns + 1):
            tid = f"{table_id}_p{n}" if columns > 1 else table_id
            out[tid] = render(tid, title.format(n=n), comment.format(n=n), locator, line,
                              [(a, b, amounts[n - 1]) for a, b, amounts in bands])
    return out


def render(table_id, title, comment, locator, line, bands):
    out = [f"# {title}, transcribed from the web edition of IT-201-I (the PDF's columns are scattered; sources/ny/{Y}/README.md),",
           "# cell by cell as printed (docs/ny/DECISIONS.md Part D). Bands are the printed 'Over / but not over' rows of federal",
           "# adjusted gross income in cents: over X and not over Y is [X + 1 cent, Y + 1 cent). The first row, from \"(see Note 2)\",",
           "# includes zero and negative income (\"Note 2 This amount could be 0 or a negative amount.\"): the line that reads",
           "# this table looks up federal AGI floored at zero. The last band, open above, is \"No credit is allowed\".",
           f"# {comment}",
           "table:",
           f"  id: {table_id}",
           "  kind: tax_table",
           f'  title: "{title}"',
           f"  tax_year: {Y}",
           "  cite:",
           f"    doc: {DOC}",
           f"    locator: '{locator}'",
           f'    quote: "No credit is allowed; do not make an entry on Form IT-201, line {line}."',
           f"  bounds: {{ at_least: 0, less_than: {TOP} }}",
           "  columns:",
           "    - { key: amount, statuses: [single, mfj, mfs, hoh, qss] }",
           "  bands:"]
    out += [f"    - {{ at_least: {a}, less_than: {b}, tax: [{t}] }}" for a, b, t in bands]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="re-extract and compare with the committed tables byte for byte")
    a = ap.parse_args()
    status = 0
    for table_id, text in extract().items():
        path = OUT / f"{table_id}.yaml"
        if a.check:
            if not path.exists():
                print(f"{path.relative_to(ROOT)}: missing (a fresh extraction has {text.count('at_least: ') - 1} bands)")
                status = 1
            elif path.read_text() != text:
                print(f"{path.relative_to(ROOT)}: differs from a fresh extraction")
                old, new = path.read_text().split("\n"), text.split("\n")
                for i in range(max(len(old), len(new))):
                    if i >= len(old) or i >= len(new) or old[i] != new[i]:
                        print(f"  line {i + 1}: committed {old[i] if i < len(old) else '(none)'!r}")
                        print(f"  line {i + 1}: extracted {new[i] if i < len(new) else '(none)'!r}")
                        break
                status = 1
            else:
                print(f"{path.relative_to(ROOT)}: matches a fresh extraction ({text.count('at_least: ') - 1} bands)")
        else:
            OUT.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
            print(f"wrote {path.relative_to(ROOT)}")
    return status


if __name__ == "__main__":
    sys.exit(main())
