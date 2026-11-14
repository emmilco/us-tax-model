#!/usr/bin/env python3
"""Extract the small printed tables of a tax year from its archived documents, and check them.

    extract_printed_tables.py --check [--year N]              (check-all) every table the year has
    extract_printed_tables.py --write [--table ID ...] [--year N] [--force]
    extract_printed_tables.py --self-test                     (check-all)

Each table is found by the words printed with it, never by page number, so the same reader serves
every year whose edition prints the table as the last one did; a year whose edition does not print
those words fails, naming them.

  dc_rate         Form 2441, line 8: the decimal amount by line 7, printed on the form, or, when the
                  form sends the filer to the instructions, the phaseout schedule of the Instructions
                  for Form 2441 (a column for joint returns and one for the other filing statuses).
                  Formula: the bands tile from $0 to no limit and the rate falls by 0.01 a band.
                  No other printing of the year's table is archived.
  ltc_limit       Form 7206, line 2(b): the long-term care premium limit by age band. Second
                  printings: the Instructions for Form 7206 and the revenue procedure of the year's
                  inflation adjustments.
  savers_rate     Form 8880, line 9: the decimal amount by line 8 and filing status. Formula: the
                  head-of-household thresholds are 3/4 and the other statuses' 1/2 of the joint
                  ones (section 25B(b)(2)), and the last threshold of each column is the parameter
                  savers.agi_limit of the year, when the year has a parameter file.
  rate_schedule   The tax rate tables of section 1(j)(2) in the revenue procedure of the year's
                  inflation adjustments (Tables 1 to 4). Formula: each row's base is the previous
                  base plus the previous rate on the previous bracket's width, to the cent, and
                  each Tax Computation Worksheet row of the year's parameter file (tcw.<status>.b<n>:
                  upper limit, rate, subtraction amount) agrees with the schedule row of its rate.
  auto_limit, auto_limit_first_nobonus
                  The Pub. 946 table of limits for passenger automobiles (the reader of
                  tools/check_auto_limits.py, which checks the result against three printings):
                  the limits of the year placed in service and the six before it, by year of
                  recovery, and the first-year limit without the special allowance for the year
                  and the year six before.

The extractor refuses to write a table that is not well formed (bands that do not tile, an age
band missing, a row out of order) or that a second printing or formula contradicts. --check reads
each table again from the archive and compares it, cell by cell, with the committed file (the
committed file's comments and layout are not compared), then runs the second printings and formulas;
a table whose source has no edition archived for the year fails, naming the edition. --write writes
tables/<year>/<id>.yaml (an existing file only with --force).
"""
import argparse
import json
import re
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import taxyear  # noqa: E402
import archive_text  # noqa: E402
import check_auto_limits  # noqa: E402

YEAR = taxyear.YEAR


class Missing(Exception):
    """A source, or the words a table is found by, is not in the year's archive."""


class Archive:
    def __init__(self, year, sources=None):
        self.year = year
        self.dir = Path(sources) if sources else ROOT / "sources" / str(year)
        self.docs = archive_text.manifest(self.dir) if (self.dir / "manifest.json").exists() else {}

    def text(self, doc, key="text_file"):
        if doc not in self.docs or key not in self.docs[doc]:
            raise Missing(f"no {self.year} edition of {doc} archived")
        return archive_text.read(self.dir, self.docs[doc], key)

    def flat(self, doc, key="cols_file"):
        """The document's reading-order text (else its layout text) on one line."""
        k = key if key in self.docs.get(doc, {}) else "text_file"
        return re.sub(r"\s+", " ", self.text(doc, k))

    def revproc(self):
        """The id of the year's revenue procedure of inflation adjustments: the one whose rate
        tables are "For taxable years beginning in <year>"."""
        for doc in self.docs:
            if doc.startswith("rp-") and f"For taxable years beginning in {self.year}, the tax rate tables" in self.flat(doc):
                return doc
        raise Missing(f"no {self.year} revenue procedure printing the tax rate tables archived")

    def sha(self, doc):
        return self.docs[doc].get("sha256", "")[:12]


def after(text, words, length=4000):
    i = text.find(words)
    if i < 0:
        raise Missing(f"the words “{words}” are not printed")
    return text[i:i + length]


def cents(s):
    s = s.replace("$", "").replace(",", "")
    whole, _, frac = s.partition(".")
    return int(whole) * 100 + (int(frac.ljust(2, "0")) if frac else 0)


def money(c):
    return f"${c // 100:,}" + (f".{c % 100:02d}" if c % 100 else "")


# ---------- ltc_limit ----------

LTC_KEYS = ["to40", "to50", "to60", "to70", "over70"]


def ltc_bands(pairs):
    """[(lower age, upper age or None, cents)] checked to be the five bands 40 or less, 41-50,
    51-60, 61-70 and 71 or more, in order."""
    want = [(None, 40), (41, 50), (51, 60), (61, 70), (71, None)]
    got = [(lo, hi) for lo, hi, _ in pairs]
    if got != want:
        raise ValueError(f"age bands {got}, expected {want}")
    amounts = [c for _, _, c in pairs]
    if amounts != sorted(amounts) or len(set(amounts)) != 5:
        raise ValueError(f"amounts not increasing: {amounts}")
    return amounts


def ltc_form(arch):
    t = after(arch.flat("f7206"), "Use the person", 1200)
    pairs = []
    for m in re.finditer(r"\$([\d,]+)\s*[—–-]\s*if (?:that person is )?age (\d+)(?: or younger| to (\d+)| or older)", t):
        a, b = int(m.group(2)), m.group(3)
        if "younger" in m.group(0):
            pairs.append((None, a, cents(m.group(1))))
        elif b:
            pairs.append((a, int(b), cents(m.group(1))))
        else:
            pairs.append((a, None, cents(m.group(1))))
    return ltc_bands(pairs), t[t.find("$"):t.find("older") + 5]


def ltc_revproc(arch):
    t = after(arch.flat(arch.revproc(), "text_file"), "Attained Age Before the Close of the Taxable Year", 800)
    pairs = []
    for m in re.finditer(r"(?:(\d+) or less|More than (\d+) but not more than (\d+)|More than (\d+))\s+\$([\d,]+)", t):
        if m.group(1):
            pairs.append((None, int(m.group(1)), cents(m.group(5))))
        elif m.group(2):
            pairs.append((int(m.group(2)) + 1, int(m.group(3)), cents(m.group(5))))
        else:
            pairs.append((int(m.group(4)) + 1, None, cents(m.group(5))))
    return ltc_bands(pairs[:5])


def ltc_instructions(arch):
    t = after(arch.flat("i7206", "text_file"), "Age 40 or younger", 1500)
    pairs = []
    for m in re.finditer(r"Age (\d+) or younger\s*[—–-]\s*\$([\d,]+)|Age (\d+) to (\d+)\s*[—–-]\s*\$([\d,]+)|Age (\d+) or older\s*[—–-]\s*\$([\d,]+)", t):
        if m.group(1):
            pairs.append((None, int(m.group(1)), cents(m.group(2))))
        elif m.group(3):
            pairs.append((int(m.group(3)), int(m.group(4)), cents(m.group(5))))
        else:
            pairs.append((int(m.group(6)), None, cents(m.group(7))))
    return ltc_bands(pairs[:5])


def ltc_limit(arch):
    amounts, quote = ltc_form(arch)
    y = arch.year
    table = {"id": "ltc_limit", "kind": "keyed",
             "title": "Qualified long-term care premium limit by age (Form 7206, line 2(b))", "tax_year": y,
             "cite": {"doc": "f7206", "locator": f"Form 7206 ({y}), line 2(b)", "quote": quote},
             "keys": [{"name": "age", "type": "Enum(ltc_age)"}], "cell": "NonNegDollars",
             "rows": [{"keys": [k], "value": v} for k, v in zip(LTC_KEYS, amounts)]}
    checks = []
    for name, reader in (("Instructions for Form 7206", ltc_instructions), ("the revenue procedure", ltc_revproc)):
        other = reader(arch)
        checks.append((name, [f"{k}: form {money(a)}, printed {money(b)}" for k, a, b in zip(LTC_KEYS, amounts, other) if a != b]))
    return table, checks, ["f7206"], (f"The limit on qualified long-term care premiums for each person covered, by age at "
                                       f"the end of {y}.")


# ---------- savers_rate ----------

def savers_rate(arch, params=None):
    t = arch.text("f8880")
    i = t.find("Enter the applicable decimal amount from the table below.")
    if i < 0:
        raise Missing("the words “Enter the applicable decimal amount from the table below.” are not printed in f8880")
    rows = re.findall(r"^\s*(---|\$[\d,]+)\s+(\$[\d,]+|---)\s+0\.(\d)\s+0\.(\d)\s+0\.(\d)", t[i:i + 3000], re.M)
    bands = []
    for over, not_over, *rates in rows:
        bands.append({"over": None if over == "---" else cents(over), "not_over": None if not_over == "---" else cents(not_over),
                      "rates": [{"num": int(r), "den": 10} for r in rates]})
    if not bands or bands[0]["over"] is not None or bands[-1]["not_over"] is not None:
        raise ValueError("the bands do not run from no lower limit to no upper limit")
    for a, b in zip(bands, bands[1:]):
        if a["not_over"] != b["over"] or (a["over"] is not None and a["over"] >= a["not_over"]):
            raise ValueError(f"bands do not tile at {a['not_over']}")
    for col in range(3):
        seq = [b["rates"][col]["num"] for b in bands]
        if seq != sorted(seq, reverse=True) or set(seq) - {5, 2, 1, 0}:
            raise ValueError(f"column {col + 1} rates {seq} are not 0.5, 0.2, 0.1, 0.0 in order")
    # the thresholds of each column: where its rate falls below 0.5, 0.2 and 0.1
    def thresholds(col):
        out = []
        for level in (5, 2, 1):
            out.append(next(b["over"] for b in bands if b["rates"][col]["num"] < level))
        return out
    mfj, hoh, other = thresholds(0), thresholds(1), thresholds(2)
    bad = [f"head of household threshold {money(h)} is not 3/4 of {money(j)}" for j, h in zip(mfj, hoh) if Fraction(h) != Fraction(3 * j, 4)]
    bad += [f"single threshold {money(o)} is not 1/2 of {money(j)}" for j, o in zip(mfj, other) if Fraction(o) != Fraction(j, 2)]
    checks = [("section 25B(b)(2): 3/4 and 1/2 of the joint thresholds", bad)]
    if params and "savers.agi_limit" in params:
        lim = params["savers.agi_limit"]["value"]
        bad = [f"{st}: table {money(t_)}, parameter {money(lim[st])}" for st, t_ in
               (("mfj", mfj[2]), ("hoh", hoh[2]), ("single", other[2]), ("mfs", other[2]), ("qss", other[2])) if lim.get(st) != t_]
        checks.append(("the parameter savers.agi_limit", bad))
    y = arch.year
    table = {"id": "savers_rate", "kind": "rate_bands", "title": "Saver's credit decimal amount (Form 8880, line 9)",
             "tax_year": y, "cite": {"doc": "f8880", "locator": f"Form 8880 ({y}), line 9",
                                     "quote": "Enter the applicable decimal amount from the table below."},
             "columns": [{"key": "mfj", "statuses": ["mfj"]}, {"key": "hoh", "statuses": ["hoh"]},
                         {"key": "other", "statuses": ["single", "mfs", "qss"]}],
             "rate_bands": bands}
    return table, checks, ["f8880"], ("The saver's credit rate (Form 8880, line 9) by line 8 and filing status, as printed. "
                                      "Columns as printed: married filing jointly; head of household; single, married filing "
                                      "separately or qualifying surviving spouse.")


# ---------- rate_schedule ----------

SCHEDULES = [("A", "mfj"), ("B", "hoh"), ("C", "single"), ("D", "mfs")]


def pct(s):
    return {"num": int(s), "den": 100}


def rate_schedule(arch, params=None):
    rp = arch.revproc()
    text = re.sub(r"\s+", " ", arch.text(rp))
    out = {}
    for letter, status in SCHEDULES:
        t = after(text, f"TABLE {'ABCD'.index(letter) + 1} - Section 1(j)(2)({letter})", 1500)
        t = t[:t.find("TABLE", 10)] if t.find("TABLE", 10) > 0 else t
        first = re.search(r"Not over \$([\d,]+) (\d+)% of the taxable income", t)
        if not first:
            raise ValueError(f"Table {letter}: the first row (“Not over”) is not printed as expected")
        rows = [{"upper": cents(first.group(1)), "base": 0, "rate": pct(first.group(2)), "over": 0}]
        # Each later row runs from "Over $X" to the next. Its figures, in whatever order the two printed
        # columns are read: X; the base, followed by "plus"; the rate; X again ("the excess over"); and,
        # but for the last row, the upper limit.
        chunks = re.split(r"(?=\bOver \$)", t[first.end():])[1:]
        for n, chunk in enumerate(chunks):
            amounts = [(m.group(1), m.group(2) is not None) for m in re.finditer(r"\$ ?([\d,]+(?:\.\d\d)?)( plus)?", chunk)]
            rate = re.search(r"plus (\d+)% of", chunk)
            lo = amounts[0][0] if amounts else None
            bases = [a for a, plus in amounts if plus]
            rest = [a for a, plus in amounts[1:] if not plus]
            if lo in rest:
                rest.remove(lo)
            last = n == len(chunks) - 1
            if not rate or len(bases) != 1 or len(rest) != (0 if last else 1) or f"over ${lo}" not in chunk.replace("$ ", "$")[3:]:
                raise ValueError(f"Table {letter}: the row over ${lo} is not printed as expected")
            rows.append({"upper": None if last else cents(rest[0]), "base": cents(bases[0]), "rate": pct(rate.group(1)),
                         "over": cents(lo)})
        out[status] = rows
    checks = []
    bad = []
    for status, rows in out.items():
        for a, b in zip(rows, rows[1:]):
            want = a["base"] + Fraction(a["rate"]["num"], a["rate"]["den"]) * (a["upper"] - a["over"])
            if b["over"] != a["upper"]:
                bad.append(f"{status}: the row over {money(b['over'])} does not start at {money(a['upper'])}")
            if b["base"] != want:
                bad.append(f"{status}: base {money(b['base'])} over {money(b['over'])}, figured {float(want) / 100:,.2f}")
    checks.append(("each base is the previous base plus the previous rate on the previous bracket", bad))
    if params:
        bad, n = [], 0
        for status, rows in out.items():
            for k in range(1, 6):
                p = f"tcw.{status}.b{k}"
                if f"{p}.rate" not in params:
                    continue
                rate = params[f"{p}.rate"]["value"]
                row = next((r for r in rows if Fraction(r["rate"]["num"], r["rate"]["den"]) == Fraction(rate["num"], rate["den"])), None)
                n += 1
                if row is None:
                    bad.append(f"{p}: no schedule row at {rate['num']}/{rate['den']}")
                    continue
                if f"{p}.upper" in params and params[f"{p}.upper"]["value"] != row["upper"]:
                    bad.append(f"{p}.upper {money(params[f'{p}.upper']['value'])}, schedule {row['upper']}")
                if f"{p}.subtract" in params:
                    want = Fraction(row["rate"]["num"], row["rate"]["den"]) * row["over"] - row["base"]
                    if params[f"{p}.subtract"]["value"] != want:
                        bad.append(f"{p}.subtract {money(params[f'{p}.subtract']['value'])}, rate x over - base {float(want) / 100:,.2f}")
        checks.append((f"the {n} Tax Computation Worksheet rows of the parameter file", bad))
    y = arch.year
    section = re.search(r"SECTION (\d+)\. " + str(y) + r" ADJUSTED ITEMS", text)
    table = {"id": "rate_schedule", "kind": "bracket_schedule", "title": f"{y} Tax Rate Schedules (section 1(j)(2))",
             "tax_year": y, "cite": {"doc": rp, "locator": f"section {section.group(1) if section else '?'}.01, Tables 1-4",
                                     "quote": f"For taxable years beginning in {y}, the tax rate tables under § 1 are as follows"},
             "status_alias": {"qss": "mfj"},
             "schedules": {s: out[s] for s in ("single", "mfj", "mfs", "hoh")}}
    return table, checks, [rp], (f"{y} tax rate schedules (section 1(j)(2)) from the revenue procedure of the year's "
                                 "inflation adjustments. Each row: upper (cents, null for the top row), base, rate, over; "
                                 "tax is base + rate x (amount - over).")


# ---------- auto_limit ----------

def auto_limits(arch):
    name, f, start = check_auto_limits.PRINTINGS[0]
    if "p946" not in arch.docs:
        raise Missing(f"no {arch.year} edition of p946 archived")
    text = archive_text.read_file(arch.dir / f)
    if start not in text:
        raise Missing(f"the words “{start}” are not printed in {f}")
    rows, notes = check_auto_limits.parse(check_auto_limits.window(text, start))
    y = arch.year
    years = list(range(y, y - 7, -1))
    lost = [p for p in years if p not in rows]
    if lost:
        raise ValueError(f"no row for the years placed in service {lost}")
    limit = [{"keys": [f"y{p}", k], "value": rows[p][min(k, 4) - 1]} for p in years for k in range(1, y - p + 2)]
    nobonus = []
    for p in (y, y - 6):
        fn = rows[p][4]
        if fn not in notes:
            raise ValueError(f"no footnote {fn} (first year without the allowance, placed in {p})")
        nobonus.append({"keys": [f"y{p}"], "value": notes[fn]})
    return limit, nobonus


def auto_limit(arch):
    limit, _ = auto_limits(arch)
    y = arch.year
    table = {"id": "auto_limit", "kind": "keyed",
             "title": f"Maximum depreciation deduction for passenger automobiles placed in service {y - 6} to {y} (Pub. 946)",
             "tax_year": y, "cite": None, "keys": [{"name": "placed", "type": "Enum(placed_year)"}, {"name": "year", "type": "Count"}],
             "cell": "NonNegDollars", "rows": limit}
    return table, [("tools/check_auto_limits.py (three printings)", [])], ["p946"], (
        f"Limits on depreciation and the section 179 deduction for passenger automobiles placed in service {y - 6} to {y}, "
        "by year of the recovery period.")


def auto_limit_first_nobonus(arch):
    _, nobonus = auto_limits(arch)
    y = arch.year
    table = {"id": "auto_limit_first_nobonus", "kind": "keyed",
             "title": "First-year limit for passenger automobiles without the special depreciation allowance (Pub. 946, footnotes 1 to 6)",
             "tax_year": y, "cite": None, "keys": [{"name": "placed", "type": "Enum(placed_year)"}], "cell": "NonNegDollars",
             "rows": nobonus}
    return table, [("tools/check_auto_limits.py (three printings)", [])], ["p946"], (
        f"The first-year limit for a passenger automobile placed in service in {y}, and in {y - 6}, when no special "
        "depreciation allowance is claimed (the footnotes of the table in Pub. 946).")


# ---------- dc_rate ----------

DC_TRIPLE = re.compile(r"\$?\s*([\d,]+)\s*[—–-]\s*\$?(No limit|[\d,]+)\s+0?\.(\d\d)\b")


def dc_chain(triples, name):
    """Rate bands from (over, not over, rate) triples: tiling $0 to no limit, the rate falling by
    0.01 a band, each run of bands of one width (the phase-down of section 21(a)(2))."""
    triples = sorted(triples, key=lambda t: t[0])
    if not triples or triples[0][0] != 0 or triples[-1][1] is not None:
        raise ValueError(f"{name}: the bands do not run from $0 to no limit")
    bad = []
    for a, b in zip(triples, triples[1:]):
        if a[1] != b[0]:
            bad.append(f"{name}: the band over {money(b[0])} does not start at {money(a[1])}")
        if b[2] != a[2] - 1:
            bad.append(f"{name}: the rate over {money(b[0])} is .{b[2]:02d}, after .{a[2]:02d}")
    return [{"over": None if i == 0 else lo, "not_over": hi, "rates": [{"num": r, "den": 100}]}
            for i, (lo, hi, r) in enumerate(triples)], bad


def dc_rate(arch):
    """Form 2441 line 8's table, printed on the form, or, when the form sends the filer to the
    instructions' phaseout schedule, in the Instructions for Form 2441 (one column per filing
    status group, joint first)."""
    form = arch.text("f2441")
    if "decimal amount shown below" in form:
        doc, region = "f2441", after(form, "decimal amount shown below", 3000)
        region = region[:region.find("9a")]
        cols = [[(cents(a) if a != "0" else 0, None if b == "No limit" else cents(b), int(r)) for a, b, r in DC_TRIPLE.findall(region)]]
        cols[0] = [(lo, hi, r) for lo, hi, r in cols[0]]
        keys = None
    else:
        doc = "i2441"
        region = after(arch.text("i2441"), "Phaseout Schedule", 8000)
        region = region[:region.find("Line 9b")]
        if "married filing jointly" not in region or "any other filing status" not in region:
            raise Missing("the i2441 phaseout schedule does not print its joint and other columns as expected")
        cols = [[], []]
        for line in region.splitlines():
            found = DC_TRIPLE.findall(line)
            if len(found) not in (0, 2):
                raise ValueError(f"i2441: a phaseout schedule line with {len(found)} bands: {line.strip()[:80]}")
            for c, (a, b, r) in zip(cols, found):
                c.append((cents(a), None if b == "No limit" else cents(b), int(r)))
        keys = [{"key": "mfj", "statuses": ["mfj"]}, {"key": "other", "statuses": ["single", "mfs", "hoh", "qss"]}]
    chains, bad = [], []
    for n, c in enumerate(cols):
        bands, problems = dc_chain(c, f"column {n + 1}")
        chains.append(bands)
        bad += problems
    if len(chains) == 1:
        bands = chains[0]
    else:
        edges = sorted({b["not_over"] for ch in chains for b in ch if b["not_over"] is not None})
        bands, lo = [], None
        for hi in edges + [None]:
            rates = [next(b["rates"][0] for b in ch if (b["not_over"] is None or (hi is not None and hi <= b["not_over"]))
                          and (b["over"] is None or (lo is not None and lo >= b["over"]))) for ch in chains]
            bands.append({"over": lo, "not_over": hi, "rates": rates})
            lo = hi
    y = arch.year
    table = {"id": "dc_rate", "kind": "rate_bands", "title": "Child and dependent care credit decimal amount (Form 2441, line 8)",
             "tax_year": y, "cite": {"doc": doc, "locator": f"Form 2441 ({y}), line 8" if doc == "f2441" else "Line 8, Phaseout Schedule",
                                     "quote": ("Enter on line 8 the decimal amount shown below that applies to the amount on line 7."
                                               if doc == "f2441" else "Use the table that follows to find the decimal amount")}}
    if keys:
        table["columns"] = keys
    table["rate_bands"] = bands
    return table, [("the rate falls by 0.01 a band, the bands tile", bad)], [doc], (
        "The child and dependent care credit rate (Form 2441, line 8) by line 7, as printed; the first band is open below "
        "(line 7 of zero or less takes its rate).")


EXTRACTORS = {"dc_rate": dc_rate, "ltc_limit": ltc_limit, "savers_rate": savers_rate, "rate_schedule": rate_schedule,
              "auto_limit": auto_limit, "auto_limit_first_nobonus": auto_limit_first_nobonus}
NEEDS_PARAMS = {"savers_rate", "rate_schedule"}
# The fields compared with a committed file: the cells and what they are keyed by.
CELLS = ("keys", "rows", "columns", "rate_bands", "schedules", "status_alias", "cell")


# ---------- files ----------

def flow(v):
    """A YAML flow value, as the table files write rows."""
    if v is None:
        return "null"
    if isinstance(v, dict):
        return "{ " + ", ".join(f"{k}: {flow(x)}" for k, x in v.items()) + " }"
    if isinstance(v, list):
        return "[" + ", ".join(flow(x) for x in v) + "]"
    return json.dumps(v, ensure_ascii=False) if isinstance(v, str) and not re.fullmatch(r"[a-z][a-z0-9_]*", v) else str(v)


def render(table, comment, sources):
    out = [f"# {line}" for line in wrap(comment)]
    out.append(f"# Written by tools/extract_printed_tables.py from {', '.join(sources)}; checked by its --check (check-all).")
    out.append("table:")
    for key, v in table.items():
        if v is None:
            continue
        if key in ("rows", "rate_bands", "keys", "columns"):
            out.append(f"  {key}:")
            out += [f"    - {flow(x)}" for x in v]
        elif key == "schedules":
            out.append("  schedules:")
            for st, rows in v.items():
                out.append(f"    {st}:")
                out += [f"      - {flow(r)}" for r in rows]
        elif key == "cite":
            out.append("  cite:")
            out += [f"    {k}: {json.dumps(x, ensure_ascii=False)}" for k, x in v.items()]
        elif isinstance(v, dict):
            out.append(f"  {key}: {flow(v)}")
        else:
            out.append(f"  {key}: {json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}")
    return "\n".join(out) + "\n"


def wrap(text, width=110):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    return lines + [cur] if cur else lines


def params_of(year):
    p = ROOT / "params" / f"{year}.yaml"
    return yaml.safe_load(p.read_text(encoding="utf-8"))["params"]["values"] if p.exists() else None


def extract(tid, arch, params):
    fn = EXTRACTORS[tid]
    return fn(arch, params) if tid in NEEDS_PARAMS else fn(arch)


def compare_cells(committed, table):
    """Differences between the committed table's cells and the extracted ones."""
    bad = []
    for k in CELLS:
        a, b = committed.get(k), table.get(k)
        if a is None and b is None:
            continue
        if a != b:
            if isinstance(a, list) and isinstance(b, list):
                diffs = [f"{k}[{i}]: committed {flow(x)}, extracted {flow(y)}" for i, (x, y) in enumerate(zip(a, b)) if x != y]
                if len(a) != len(b):
                    diffs.append(f"{k}: committed {len(a)} entries, extracted {len(b)}")
                bad += diffs
            elif isinstance(a, dict) and isinstance(b, dict):
                for s in sorted(set(a) | set(b)):
                    if a.get(s) != b.get(s):
                        bad.append(f"{k}.{s}: committed {flow(a.get(s))}, extracted {flow(b.get(s))}")
            else:
                bad.append(f"{k}: committed {flow(a)}, extracted {flow(b)}")
    return bad


def check(year, arch=None, tables_dir=None, out=print):
    arch = arch or Archive(year)
    tables_dir = Path(tables_dir) if tables_dir else ROOT / "tables" / str(year)
    params = params_of(year)
    failures = 0
    for tid in EXTRACTORS:
        path = tables_dir / f"{tid}.yaml"
        if not path.exists():
            continue
        try:
            table, checks, _src, _c = extract(tid, arch, params)
        except (Missing, ValueError) as e:
            out(f"printed tables: {tid} FAIL, {e}")
            failures += 1
            continue
        committed = yaml.safe_load(path.read_text(encoding="utf-8"))["table"]
        bad = compare_cells(committed, table)
        for name, findings in checks:
            bad += [f"{name}: {f}" for f in findings]
        failures += bool(bad)
        n = sum(len(v) if isinstance(v, list) else sum(len(x) for x in v.values()) for k, v in table.items()
                if k in ("rows", "rate_bands", "schedules"))
        out(f"printed tables: {tid}: {n} rows read from the archive " + (
            "equal the committed table cell by cell; " + ", ".join(name for name, _ in checks) + ": agree" if not bad
            else "FAIL\n  " + "\n  ".join(bad)))
    return 1 if failures else 0


def write(year, ids, force=False, out_dir=None):
    arch, params = Archive(year), params_of(year)
    status = 0
    for tid in ids:
        path = Path(out_dir or ROOT / "tables" / str(year)).resolve() / f"{tid}.yaml"
        if path.exists() and not force:
            print(f"{tid}: {archive_text.shown(path)} exists; --force to replace it")
            status = 1
            continue
        try:
            table, checks, sources, comment = extract(tid, arch, params)
        except (Missing, ValueError) as e:
            print(f"{tid}: not written: {e}")
            status = 1
            continue
        bad = [f"{name}: {f}" for name, fs in checks for f in fs]
        if bad:
            print(f"{tid}: not written: " + "; ".join(bad))
            status = 1
            continue
        if table.get("cite") is None:
            old = ROOT / "tables" / str(year - 1) / f"{tid}.yaml"
            table["cite"] = (yaml.safe_load(old.read_text(encoding="utf-8"))["table"]["cite"] if old.exists() else
                             {"doc": "p946", "locator": "Maximum Depreciation Deduction for Passenger Automobiles"})
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(table, comment, [f"sources/{year}/{s}.pdf (sha256 {arch.sha(s)})" for s in sources]),
                        encoding="utf-8")
        print(f"{tid}: wrote {archive_text.shown(path)}" + ("; the citation's pages are the prior year's: relocate them"
                                                          if tid.startswith("auto_limit") else ""))
    return status


def self_test():
    """Plant an edition of Form 7206 and its two second printings, and of Form 8880; the readers must
    give the planted tables, refuse a band missing or a column off its formula, and --check must
    fail on a committed cell that differs and on a source not archived."""
    ok = []
    ltc_form_text = ("Use the person's age at the end of the tax year. $500— if that person is age 40 or younger "
                     "$930— if age 41 to 50 $1,860— if age 51 to 60 $4,960— if age 61 to 70 $6,200— if age 71 or older Note")
    rp = ("For taxable years beginning in 2099, the tax rate tables under § 1 are as follows. "
          "Attained Age Before the Close of the Taxable Year Limitation on Premiums 40 or less $500 More than 40 but not "
          "more than 50 $930 More than 50 but not more than 60 $1,860 More than 60 but not more than 70 $4,960 More than 70 $6,200")
    instr = "a. Age 40 or younger — $500 b. Age 41 to 50 — $930 c. Age 51 to 60 — $1,860 d. Age 61 to 70 — $4,960 e. Age 71 or older — $6,200"
    rows = ["---  $24,250  0.5 0.5 0.5", "$24,250  $26,250  0.5 0.5 0.2", "$26,250  $36,375  0.5 0.5 0.1",
            "$36,375  $39,375  0.5 0.2 0.1", "$39,375  $40,250  0.5 0.1 0.1", "$40,250  $48,500  0.5 0.1 0.0",
            "$48,500  $52,500  0.2 0.1 0.0", "$52,500  $60,375  0.1 0.1 0.0", "$60,375  $80,500  0.1 0.0 0.0",
            "$80,500  ---  0.0 0.0 0.0"]
    f8880 = "9 Enter the applicable decimal amount from the table below.\n" + "\n".join(rows) + "\n"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        def plant(name, docs):
            d = tmp / name
            d.mkdir()
            entries = []
            for doc, text in docs.items():
                (d / f"{doc}.txt").write_text(text, encoding="utf-8")
                entries.append({"id": doc, "file": f"{doc}.pdf", "text_file": f"{doc}.txt"})
            (d / "manifest.json").write_text(json.dumps({"documents": entries}), encoding="utf-8")
            return Archive(2099, d)
        good = plant("good", {"f7206": ltc_form_text, "rp-99-1": rp, "i7206": instr, "f8880": f8880})
        table, checks, _s, _c = ltc_limit(good)
        ok.append(("Form 7206 read, both second printings agree",
                   [r["value"] for r in table["rows"]] == [50000, 93000, 186000, 496000, 620000] and not any(b for _, b in checks)))
        table, checks, _s, _c = savers_rate(good, {"savers.agi_limit": {"value": {"mfj": 8050000, "hoh": 6037500, "single": 4025000,
                                                                                  "mfs": 4025000, "qss": 4025000}}})
        ok.append(("Form 8880 read, the formula and the parameter agree", len(table["rate_bands"]) == 10 and not any(b for _, b in checks)))
        bad = plant("bad", {"f7206": ltc_form_text.replace("$1,860— if age 51 to 60 ", ""), "rp-99-1": rp,
                            "i7206": instr.replace("$930", "$931"), "f8880": f8880.replace("$36,375  $39,375", "$36,000  $39,375").replace("$26,250  $36,375", "$26,250  $36,000")})
        try:
            ltc_form(bad)
            ok.append(("a missing age band refused", False))
        except ValueError:
            ok.append(("a missing age band refused", True))
        differs = plant("differs", {"f7206": ltc_form_text, "rp-99-1": rp, "i7206": instr.replace("$930", "$931")})
        ok.append(("a second printing that differs reported", any(b for _, b in ltc_limit(differs)[1])))
        _t, checks, _s, _c = savers_rate(bad)
        ok.append(("a head-of-household threshold off 3/4 reported", any(b for _, b in checks)))
        sched = ("Phaseout Schedule\nIf your filing status is married filing jointly and line 7 is... If your filing status "
                 "is any other filing status and line 7 is...\n$0 – $15,000 .50 $0 – $15,000 .50\n"
                 "15,000 – 100,000 .49 15,000 – 50,000 .49\n100,000 – No limit .48 50,000 – No limit .48\nLine 9b\n")
        two = plant("two", {"f2441": "8 Enter on line 8 the decimal amount that applies. See instructions.", "i2441": sched})
        table, checks, _s, _c = dc_rate(two)
        ok.append(("the care credit's phaseout schedule read as two columns",
                   [[r["num"] for r in b["rates"]] for b in table["rate_bands"]] == [[50, 50], [49, 49], [49, 48], [48, 48]]
                   and not any(b for _, b in checks)))
        tables = tmp / "tables"
        tables.mkdir()
        table, *_ = ltc_limit(good)
        table["rows"][2]["value"] += 100
        (tables / "ltc_limit.yaml").write_text(yaml.safe_dump({"table": table}), encoding="utf-8")
        said = []
        ok.append(("--check fails on a committed cell that differs", check(2099, good, tables, said.append) == 1
                   and "rows[2]" in " ".join(said)))
        said = []
        ok.append(("--check fails, naming it, on a source not archived", check(2099, plant("empty", {}), tables, said.append) == 1
                   and "no 2099 edition of f7206" in " ".join(said)))
    for name, passed in ok:
        print(f"printed tables self-test, {name}: {'as expected' if passed else 'WRONG'}")
    return 0 if all(p for _, p in ok) else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--table", action="append", choices=sorted(EXTRACTORS))
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--out", help="write into this directory instead of tables/<year>/ (a year not yet adopted)")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if a.write:
        return write(YEAR, a.table or list(EXTRACTORS), a.force, a.out)
    return check(YEAR)


if __name__ == "__main__":
    sys.exit(main())
