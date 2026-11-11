#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""No new id carries a year (spec 4.3), in check-all.

An id that names a year must be renamed, with everything keyed to it, each time a tax year is adopted. The
ids that carry one are listed, per tax year, in tools/year_ids.json; this check reads every id of the year's
canonical build (both jurisdictions) and fails on

  - an id that carries a year and is not in the year's list: it is to be given a year-free name;
  - a listed id that no longer exists or no longer carries a year: its entry is to be removed, so the list
    only shrinks;
  - a listed id whose recorded kind or class is not what the build shows.

A tax year with no list has an empty one: every id that carries a year is refused.

What is examined. Document ids (forms, worksheets and defs), line ids (inputs and computed lines, a def's
lines included), parameter ids, enum ids and table ids. A dotted id is examined after its leading document
id, which is examined once, as the document. A parameter and the helper line that reads it may share a
name; the name is then one id of both kinds (`computed+param`). A conflict check has no id of its own: it
is keyed by the id of its refusal-gate line. Not examined: ambiguity ids (in `amb.<year>.<slug>` the year
is the edition of the register that recorded the entry), enum values (a year placed in service is data),
fixture case ids (labels of scenarios) and paths.

What carries a year.
  1. Four digits, 1900 to 2099, with no digit on either side: a word of their own (`died_2025`,
     `born_before_2001`) or run into a word (`is2025`, `edu_a2026`, `macrs2025`).
  2. In an id with no dot (document, table, enum): two final digits after a letter or an underscore that
     are the last two digits of the tax year, the year before or the year after (`clcw26` for 2025).

What does not, by rule.
  - A number outside 1900 to 2099, or with more or fewer than four digits: Form 2441, Form 2210, Form 1040,
    Form 8606, an amount of 5000, a rate of 9235.
  - Four digits written as a reference, directly after one of the words in REFERENCE: `f2032`, `form2063`,
    `line2025`, `section1977`.
  - Two digits in a dotted id, where they are line numbers, rates and ages (`line25`, `rate25`, `under_24`);
    a two-digit year inside a line id is therefore not found.
  - Two final digits of an id with no dot that are not within a year of the tax year (`g28` for 2025).
A number that the rules take for a year and that is not one (an amount of 2000) is recorded under
`look_alikes` in the year's list, with what the number is; such an entry fails once it is stale.

    check_year_ids.py [--year N]    the check
    check_year_ids.py --self-test   planted ids of each shape, look-alikes, and each failure of the list
"""
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "tools" / "year_ids.json"
KINDS = ("document", "input", "computed", "param", "enum", "table")
CLASSES = ("this_year", "next_year", "prior_year", "offset", "misnomer")
# The distance from the tax year that a class requires of the year an id carries; the other classes
# (a fixed offset, a misnomer) require none.
CLASS_OFFSET = {"this_year": 0, "next_year": 1, "prior_year": -1}
REFERENCE = ("f", "form", "line", "section", "pub")
FOUR = re.compile(r"(?<!\d)(?:19|20)\d\d(?!\d)")
TWO = re.compile(r"(?:[A-Za-z]|_)(\d\d)$")


def years_in(part, tax_year, dotted):
    """The years `part` of an id carries, in order: `part` is an id with no dot, or a dotted id without its
    leading document id."""
    found = []
    for m in FOUR.finditer(part):
        word = re.search(r"[A-Za-z]*$", part[:m.start()]).group()
        if word.lower() not in REFERENCE:
            found.append(int(m.group()))
    if not dotted and not found:
        m = TWO.search(part)
        if m:
            for y in (tax_year - 1, tax_year, tax_year + 1):
                if y % 100 == int(m.group(1)):
                    found.append(y)
    return found


def carriers(ids, tax_year):
    """{id: (kind, [years])} for the ids of `ids` ({id: kind}) that carry a year."""
    documents = {i for i, k in ids.items() if k == "document"}
    out = {}
    for i, kind in ids.items():
        head, dot, rest = i.partition(".")
        part = rest if dot and head in documents else i
        years = years_in(part, tax_year, dotted="." in i)
        if years:
            out[i] = (kind, years)
    return out


def collect(canonical):
    """{id: kind} for every id the canonical build in `canonical` defines, and the problems met reading it.
    An id defined as more than one kind has them joined in the order of KINDS: "computed+param"."""
    kinds, problems = {}, []

    def add(i, kind):
        kinds.setdefault(i, set()).add(kind)

    for path in sorted(Path(canonical).glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if "questions" in data or set(data) in ({"register"}, {"conflicts"}):
            continue  # an interview and the conflict checks name lines; an ambiguity register's ids do not roll
        if set(data) in ({"form"}, {"def"}):
            doc = next(iter(data.values()))
            add(doc["id"], "document")
            for line in doc["lines"]:
                lid = line["id"] if line["id"].startswith(doc["id"] + ".") else f"{doc['id']}.{line['id']}"
                add(lid, "input" if line["expr"].get("op") == "input" else "computed")
        elif set(data) == {"params"}:
            for i in data["params"]["values"]:
                add(i, "param")
            for i in data["params"]["enums"]:
                add(i, "enum")
        else:
            problems.append(f"  {path.name}: not a kind of canonical file this check knows; say in "
                            f"tools/check_year_ids.py whether it defines ids")
    for path in sorted((Path(canonical) / "tables").glob("*.json")):
        add(path.stem, "table")
    return {i: "+".join(k for k in KINDS if k in ks) for i, ks in kinds.items()}, problems


def judge(ids, tax_year, listed):
    """The problems of the ids ({id: kind}) against one tax year's list ({"ids": ..., "look_alikes": ...}),
    and the listed ids that still carry a year."""
    entries, look_alikes = listed.get("ids", {}), listed.get("look_alikes", {})
    found = carriers(ids, tax_year)
    problems = []
    for i in sorted(set(entries) & set(look_alikes)):
        problems.append(f"  {i}: listed both as carrying a year and as a look-alike")
    for i, (kind, years) in sorted(found.items()):
        if i in entries or i in look_alikes:
            continue
        problems.append(f"  {i} ({kind}) carries the year {years[0]}: give it a year-free name (spec 4.3). If the "
                        f"number is not a year, record the id under look_alikes with what the number is")
    for i, entry in sorted(entries.items()):
        if i not in ids:
            problems.append(f"  {i}: listed, but no such id exists; remove its entry")
            continue
        if i not in found:
            problems.append(f"  {i}: listed, but the id carries no year; remove its entry")
            continue
        kind, years = found[i]
        if entry.get("kind") != kind:
            problems.append(f"  {i}: listed as {entry.get('kind')}, but it is {kind}")
        cls = entry.get("class")
        if cls not in CLASSES:
            problems.append(f"  {i}: class {cls!r} is not one of {', '.join(CLASSES)}")
        elif cls in CLASS_OFFSET and tax_year + CLASS_OFFSET[cls] not in years:
            problems.append(f"  {i}: class {cls} means {tax_year + CLASS_OFFSET[cls]}, but the id carries "
                            f"{', '.join(map(str, years))}")
    for i, what in sorted(look_alikes.items()):
        if i not in found:
            problems.append(f"  {i}: a look-alike entry, but no such id is taken for a year-bearing one; remove it")
        elif not (isinstance(what, str) and what.strip()):
            problems.append(f"  {i}: a look-alike entry says what the number is")
    return problems, {i: entries[i] for i in entries if i in found}


def summary(held):
    def counts(field, order):
        n = {v: sum(1 for e in held.values() if e.get(field) == v) for v in order}
        return ", ".join(f"{v} {c}" for v, c in n.items() if c)
    return f"{len(held)} listed ({counts('kind', KINDS)}; {counts('class', CLASSES)})"


def self_test():
    ty = 2025
    bad = []

    def expect(what, got, want):
        if got != want:
            bad.append(f"{what}: got {got}, expected {want}")

    documents = ["f2441", "f2210", "f1040", "f2032", "g28", "s179", "clcw", "x", "wks26", "wks_25", "carry2026"]
    ids = {d: "document" for d in documents}
    year_bearing = {
        # a word of its own; run into a word; a cutoff far from the tax year; after a document that looks like a year
        "x.died_2026": ("input", [2026]), "x.is2026": ("computed", [2026]), "x.edu_a2027": ("input", [2027]),
        "x.born_before_1961": ("input", [1961]), "f2441.paid_2027": ("input", [2027]),
        "x.on_26_2025": ("computed", [2025]), "x.span_2024_2025": ("computed", [2024, 2025]),
        "x.2025": ("computed", [2025]), "x.y2025a": ("computed", [2025]),
        # every other kind
        "ctc.amount_2026": ("param", [2026]), "placed_2025": ("enum", [2025]), "rate_2026": ("table", [2026]),
        "x.max_2025": ("computed+param", [2025]), "ny.it270.cap_2026": ("param", [2026]),
        # two final digits of an id with no dot, within a year of the tax year
        "wks26": ("document", [2026]), "wks_25": ("document", [2025]), "limit24": ("table", [2024]),
        "carry2026": ("document", [2026]),
    }
    look_alikes = {
        # form numbers, by range, in a document id and inside a line id
        "f2441": "document", "f2210": "document", "f1040": "document", "s179": "document",
        "f2441.line16": "computed", "x.ira_8606_line14": "computed", "x.edu_1098t": "input", "x.to1040": "computed",
        "x.use_8995a": "computed", "x.needs1116": "computed", "x.section1202": "computed",
        # four digits in range, written as a reference
        "f2032": "document", "f2032.line1": "computed", "f2441.line2025": "computed", "x.form2063": "input",
        "x.f2063_line2": "computed", "x.section1977": "computed", "x.pub1915": "input", "x.Line2025": "computed",
        # amounts and rates outside the range, or not four digits
        "x.over_5000": "computed", "x.rate9235": "computed", "x.cap_20250": "computed", "x.repay_200": "param",
        "x.w20255": "computed", "x.n120251": "computed",
        # two digits in a dotted id; two final digits far from the tax year; a line of a document that carries a year
        "f1040.line25": "computed", "x.rate25": "param", "x.under_24": "computed", "x.after_jan19": "input",
        "x.line26": "computed+param", "g28": "document", "eic_0": "table", "t5_p1": "table", "limit27": "table",
        "wks26.final_return": "input", "wks26.line25": "computed", "carry2026.line1": "computed",
    }
    ids.update({i: k for i, (k, _) in year_bearing.items()})
    ids.update(look_alikes)
    found = carriers(ids, ty)
    for i, want in year_bearing.items():
        expect(f"{i} carries a year", found.get(i), want)
    for i in look_alikes:
        expect(f"{i} carries no year", found.get(i), None)
    expect("the ids found", sorted(found), sorted(year_bearing))
    # the two-digit window moves with the tax year: g28 is a look-alike only while 28 is not next to it
    expect("g28 for 2027", carriers({"g28": "document"}, 2027), {"g28": ("document", [2028])})
    expect("wks26 for 2028", carriers({"wks26": "document"}, 2028), {})

    def problems(model, listed, year=ty):
        return [p.strip() for p in judge(model, year, listed)[0]]

    model = {"x": "document", "x.died_2025": "input", "x.is2019": "computed", "wks26": "document", "x.line2": "input"}
    full = {"ids": {"x.died_2025": {"kind": "input", "class": "this_year"},
                    "x.is2019": {"kind": "computed", "class": "offset"},
                    "wks26": {"kind": "document", "class": "next_year"}}}
    expect("the list equal to what is found", problems(model, full), [])
    expect("the count line", summary(judge(model, ty, full)[1]),
           "3 listed (document 1, input 1, computed 1; this_year 1, next_year 1, offset 1)")
    new = problems({**model, "x.paid_2026": "input"}, full)
    expect("a new id is refused", len(new), 1)
    expect("a new id is named and told what to do",
           new and new[0].startswith("x.paid_2026 (input) carries the year 2026: give it a year-free name"), True)
    expect("no list for the year refuses every id", len(problems(model, {})), 3)
    renamed = {k: v for k, v in model.items() if k != "x.died_2025"}
    expect("a listed id that is gone", problems(renamed, full), ["x.died_2025: listed, but no such id exists; remove its entry"])
    expect("the list after the rename, one entry shorter",
           problems(renamed, {"ids": {k: v for k, v in full["ids"].items() if k != "x.died_2025"}}), [])
    expect("a listed id that carries no year",
           problems(model, {"ids": {**full["ids"], "x.line2": {"kind": "input", "class": "misnomer"}}}),
           ["x.line2: listed, but the id carries no year; remove its entry"])

    def with_entry(i, **fields):
        return {"ids": {**full["ids"], i: {**full["ids"][i], **fields}}}
    expect("a wrong kind", problems(model, with_entry("x.died_2025", kind="computed")),
           ["x.died_2025: listed as computed, but it is input"])
    expect("an unknown class", len(problems(model, with_entry("x.died_2025", **{"class": "current"}))), 1)
    expect("a class that contradicts the year", problems(model, with_entry("x.died_2025", **{"class": "next_year"})),
           ["x.died_2025: class next_year means 2026, but the id carries 2025"])
    expect("a misnomer may carry any year", problems(model, with_entry("x.died_2025", **{"class": "misnomer"})), [])
    expect("the classes follow the tax year", len(problems(model, full, year=2026)), 2)
    amount = {**model, "x.over_2000": "computed"}
    expect("an amount that reads as a year is refused", len(problems(amount, full)), 1)
    expect("a recorded look-alike is accepted", problems(amount, {**full, "look_alikes": {"x.over_2000": "$2,000"}}), [])
    expect("a look-alike with no reason", len(problems(amount, {**full, "look_alikes": {"x.over_2000": " "}})), 1)
    expect("a stale look-alike", problems(model, {**full, "look_alikes": {"x.over_2000": "$2,000"}}),
           ["x.over_2000: a look-alike entry, but no such id is taken for a year-bearing one; remove it"])
    expect("an id listed twice",
           len(problems(model, {**full, "look_alikes": {"x.died_2025": "nothing"}})), 1)

    # collect() on a planted build: each kind of file, a def's local line ids, and a file it does not know
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "tables").mkdir()

        def write(name, data):
            (root / name).write_text(json.dumps(data), encoding="utf-8")
        line = lambda i, op: {"id": i, "expr": {"op": op}}  # noqa: E731
        write("wks26.json", {"form": {"id": "wks26", "lines": [line("wks26.paid_2026", "input"), line("wks26.line1", "copy")]}})
        write("rate.json", {"def": {"id": "rate", "lines": [line("amount", "input"), line("tax_2025", "choose")]}})
        write("params.json", {"params": {"values": {"ctc.amount_2026": {}, "rate.tax_2025": {}}, "enums": {"placed_year": {"values": ["y2025"]}}}})
        write("conflicts.json", {"conflicts": {"wks26.line1": "text"}})
        write("register.json", {"register": {"entries": [{"id": "amb.2025.slug"}]}})
        write("interview.json", {"questions": [{"input": "wks26.paid_2026"}], "targets": []})
        write("tables/limit_2026.json", {"table": {}})
        got, trouble = collect(root)
        expect("the planted build's ids", got, {
            "wks26": "document", "wks26.paid_2026": "input", "wks26.line1": "computed", "rate": "document",
            "rate.amount": "input", "rate.tax_2025": "computed+param", "ctc.amount_2026": "param", "placed_year": "enum",
            "limit_2026": "table"})
        expect("the planted build reads cleanly", trouble, [])
        expect("the planted build's year-bearing ids", sorted(carriers(got, ty)),
               ["ctc.amount_2026", "limit_2026", "rate.tax_2025", "wks26", "wks26.paid_2026"])
        write("profiles.json", {"profiles": {"single_2025": {}}})
        expect("a file of an unknown kind is reported", len(collect(root)[1]), 1)

    if bad:
        print("year ids self-test FAILED:\n  " + "\n  ".join(bad), file=sys.stderr)
        return 1
    print(f"year ids self-test OK: {len(year_bearing)} planted ids found, {len(look_alikes)} look-alikes passed, "
          f"new, gone, misclassed and look-alike entries each judged, a planted build read")
    return 0


def main():
    if "--self-test" in sys.argv[1:]:
        return self_test()
    sys.path.insert(0, str(ROOT / "tools"))
    import taxyear
    import build_fresh
    if sys.argv[1:]:
        sys.exit(f"check_year_ids: unknown argument {sys.argv[1]!r}\n{__doc__}")
    build_fresh.require()
    ids, problems = collect(ROOT / "canonical" / taxyear.Y)
    listed = json.loads(BASELINE.read_text(encoding="utf-8")).get("years", {}).get(taxyear.Y, {})
    more, held = judge(ids, taxyear.YEAR, listed)
    problems += more
    if problems:
        print(f"year ids ({taxyear.Y}): {len(problems)} problem(s) against tools/year_ids.json:\n" + "\n".join(problems),
              file=sys.stderr)
        return 1
    print(f"year ids ({taxyear.Y}): {len(ids)} ids read, no new id carries a year; {summary(held)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
