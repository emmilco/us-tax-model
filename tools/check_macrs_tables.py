#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Check tables/<year>/macrs_gds.yaml, offline, in check-all; writes reports/<year>/macrs_tables.md.

Two checks, each independent of the extraction:

  1. Derivation. Every rate is figured from its method and convention: declining
     balance (200% for 3- to 10-year property, 150% for 15- and 20-year) or straight
     line, switching to straight line when that is larger, with the half-year or
     mid-quarter fraction in the first year. Each year is figured on 1 less the printed
     rates of the earlier years and rounded half-up to the table's printed precision;
     the last year is the remainder. A rate that differs is listed. Two columns of the
     official tables depart from this rule (listed in KNOWN with what they show); any
     other difference fails.
  2. Second printing. The half-year rates of Tables A-1 (200% and 150% declining
     balance) are compared with Tables A and B of the Instructions for Form 4562, which
     print them again; any difference fails.

Every column must also total exactly 100%.

The year is used for paths only: a year with no MACRS table has nothing to check; a
year whose table has no archived Form 4562 instructions of that year fails, naming
the missing edition (the table cannot be confirmed by its second printing).

    check_macrs_tables.py --self-test     (in check-all) the missing edition is reported, not raised
"""
from fractions import Fraction as F
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
import archive_text  # noqa: E402
TABLE = ROOT / "tables" / Y / "macrs_gds.yaml"
ARCHIVE = ROOT / "sources" / Y
REPORT = ROOT / "reports" / Y / "macrs_tables.md"

PERIOD = {"y3": 3, "y5": 5, "y7": 7, "y10": 10, "y15": 15, "y20": 20, "y15sl": 15}
FACTOR = {"y3": F(2), "y5": F(2), "y7": F(2), "y10": F(2), "y15": F(3, 2), "y20": F(3, 2), "y15sl": F(0)}
FIRST = {"hy": F(1, 2), "mq1": F(7, 8), "mq2": F(5, 8), "mq3": F(3, 8), "mq4": F(1, 8)}
# Columns of the official tables that depart from the derivation; each is read from the PDF as printed
# and confirmed by the second transcription of the tables (tools/transcription), not by this check.
KNOWN = {
    ("y7", "mq2"): "years 1, 3, 4 and 6 are the derived rate truncated, not rounded, and year 7 is 0.01 below it",
    ("y20", "mq1"): "year 2 is printed 7.000 where the derived rate is 7.008, and later years differ from the derivation by at most 0.007",
}


def load():
    rows = yaml.safe_load(TABLE.read_text(encoding="utf-8"))["table"]["rows"]
    cols = {}
    for r in rows:
        p, c, y = r["keys"]
        cols.setdefault((p, c), {})[y] = (F(r["value"]["num"], r["value"]["den"]), r["value"]["den"])
    return cols


def derive(p, c, printed):
    n, rate, first = PERIOD[p], FACTOR[p] / PERIOD[p], FIRST[c]
    life, left, out = F(n), F(1), {}
    years = sorted(printed)
    for y in years:
        part = first if y == 1 else F(1)
        db = rate * left * part
        sl = left / life * part if life >= 1 else left
        if y == years[-1]:
            out[y] = left
        else:
            den = printed[y][1]
            out[y] = F(int(min(left, max(db, sl)) * den + F(1, 2)), den)
        left -= printed[y][0]
        life -= part
    return out


def second_printing(text):
    """Tables A and B of the Form 4562 instructions (their text): {(period, year): rate}."""
    out = {}
    for tag, factor in (("Table A—", "200"), ("Table B—", "150")):
        start = text.index(tag)
        block = text[start:text.index("Table", start + 10)]
        head = re.search(r"Year\s+(.+)", block).group(1)
        periods = [int(x) for x in re.findall(r"(\d+) years", head)]
        for line in block.splitlines():
            m = re.match(r"(\d{1,2})\s+(.+)$", line)
            if not m or "%" not in m.group(2):
                continue
            year = int(m.group(1))
            cells = list(re.finditer(r"\d+\.\d+%", line))
            positions = [(mm.start() + mm.end()) / 2 for mm in re.finditer(r"\d+ years", "Year" + " " * (len(re.match(r"Year\s+", re.search(r"Year\s+.+", block).group()).group()) - 4) + head)]
            for cell in cells:
                centre = (cell.start() + cell.end()) / 2
                i = min(range(len(positions)), key=lambda k: abs(positions[k] - centre))
                key = {(200, 3): "y3", (200, 5): "y5", (200, 7): "y7", (200, 10): "y10", (150, 15): "y15", (150, 20): "y20"}.get((int(factor), periods[i]))
                if key:
                    whole, frac = cell.group().rstrip("%").split(".")
                    out[(key, year)] = F(int(whole + frac), 100 * 10 ** len(frac))
    return out


def main(archive=ARCHIVE, report=REPORT, out=print):
    if not TABLE.exists():
        print(f"macrs tables: no tables/{Y}/macrs_gds.yaml; nothing to check")
        return 0
    try:
        i4562 = archive_text.read_file(archive / "i4562.txt")
    except FileNotFoundError:
        msg = (f"no {Y} edition of the Instructions for Form 4562 is archived ({archive_text.shown(archive / 'i4562.txt')}): "
               f"tables/{Y}/macrs_gds.yaml cannot be checked against its second printing")
        report.write_text(f"# MACRS percentage tables: derivation and second printing\n\nNot checked: {msg}.\n", encoding="utf-8")
        out(f"macrs tables: FAIL, {msg}")
        return 1
    cols = load()
    lines = ["# MACRS percentage tables: derivation and second printing", "",
             f"Generated by `tools/check_macrs_tables.py` from `tables/{Y}/macrs_gds.yaml`; do not edit by hand.", ""]
    failures = 0
    total = 0
    lines += ["| Period | Convention | Rates | Total | Differ from the derivation |", "| --- | --- | --- | --- | --- |"]
    for (p, c), printed in sorted(cols.items(), key=lambda kv: (list(PERIOD).index(kv[0][0]), list(FIRST).index(kv[0][1]))):
        total += len(printed)
        derived = derive(p, c, printed)
        differ = [y for y in printed if printed[y][0] != derived[y]]
        s = sum(v for v, _ in printed.values())
        if s != 1:
            failures += 1
        note = ", ".join(f"year {y}: {float(printed[y][0]) * 100:g}% printed, {float(derived[y]) * 100:g}% derived" for y in differ)
        if differ and (p, c) not in KNOWN:
            failures += 1
            note += " — FAIL"
        elif differ:
            note += f" — known: {KNOWN[(p, c)]}"
        lines.append(f"| {p} | {c} | {len(printed)} | {float(s) * 100:g}%{'' if s == 1 else ' — FAIL'} | {note or 'none'} |")
    second = second_printing(i4562)
    agree = 0
    lines += ["", "## Second printing (Instructions for Form 4562, Tables A and B)", ""]
    for (p, y), v in sorted(second.items()):
        mine = cols.get((p, "hy"), {}).get(y)
        if mine is None or mine[0] != v:
            failures += 1
            lines.append(f"- {p} year {y}: i4562 {float(v) * 100:g}%, Pub. 946 {'missing' if mine is None else f'{float(mine[0]) * 100:g}%'} — FAIL")
        else:
            agree += 1
    lines.append(f"{agree} half-year rates printed in both agree" + ("" if failures else "."))
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"macrs tables: {total} rates, {agree} confirmed by a second printing, {failures} failing check(s)")
    print(f"report: {report.relative_to(ROOT)}")
    return 1 if failures else 0


def self_test():
    """With an empty archive the check fails naming the missing edition, without a traceback."""
    import tempfile
    if not TABLE.exists():
        print(f"macrs tables self-test: no tables/{Y}/macrs_gds.yaml; skipped")
        return 0
    with tempfile.TemporaryDirectory() as tmp:
        try:
            status = main(archive=Path(tmp), report=Path(tmp) / "report.md", out=lambda _msg: None)
            said = (Path(tmp) / "report.md").read_text(encoding="utf-8")
        except Exception as e:  # noqa: BLE001 - the failure this test guards against
            status, said = None, f"{type(e).__name__}: {e}"
    ok = status == 1 and "i4562" in said
    print("macrs tables self-test, the year's Form 4562 instructions not archived: "
          + ("reported as missing" if ok else f"WRONG ({said[:200]})"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main())
