#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Check tables/<year>/auto_limit.yaml and auto_limit_first_nobonus.yaml, offline, in check-all,
against three printings of the limits for passenger automobiles acquired after September 27,
2017: Pub. 946 (PDF layout text, p. 59), Pub. 946 (HTML edition) and Pub. 463 (PDF layout
text, p. 28). Each printing gives, by year placed in service, the 1st-, 2nd-, 3rd- and
4th-and-later-year limits, the first with a footnote mark joined to it, and the footnotes give
the first-year limit without the special depreciation allowance. Every cell of the project's
tables must equal every printing that shows it; writes reports/<year>/auto_limits.md.

The year is used for paths only: a year with neither table has nothing to check; a
year whose tables lack an archived printing of that year fails, naming the missing
editions; a printing that does not carry its table's opening words (PRINTINGS, read from
the 2025 editions) fails, naming them, until they are read from that year's edition.

    check_auto_limits.py --self-test     (in check-all) missing editions and openings are reported, not raised
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
import archive_text  # noqa: E402
ARCHIVE = ROOT / "sources" / Y
REPORT = ROOT / "reports" / Y / "auto_limits.md"
TABLES = [ROOT / "tables" / Y / "auto_limit.yaml", ROOT / "tables" / Y / "auto_limit_first_nobonus.yaml"]
# Each printing: (name, archived text file, where its table starts)
PRINTINGS = [
    ("Pub. 946 (PDF)", "p946.txt", "tomobiles (Including Trucks and Vans) Acquired Af-"),
    ("Pub. 946 (HTML)", "p946-html.txt", "Maximum Depreciation Deduction for Passenger Automobiles (Including Trucks and Vans) Acquired After September 27, 2017"),
    ("Pub. 463 (PDF)", "p463.txt", "and Vans) Acquired After September 27,"),
]


def cents(text):
    return int(text.replace("$", "").replace(",", "")) * 100


def parse(text):
    """{year: (first, second, third, later, footnote)} and {footnote: no-allowance limit} from one printing."""
    rows, notes = {}, {}
    row = re.compile(r"(?<!\d)(20\d\d)(?:[–-](20\d\d))?\s*\|?\s*\$?(\d{1,2}),(\d{3}) ?(\d)\s*\|?\s*\$?([\d,]+)\s*\|?\s*\$?([\d,]+)\s*\|?\s*\$?([\d,]+)")
    for m in row.finditer(text):
        first = cents(f"{m.group(3)},{m.group(4)}")
        years = range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1)
        for y in years:
            rows.setdefault(y, (first, cents(m.group(6)), cents(m.group(7)), cents(m.group(8)), int(m.group(5))))
    # A footnote is its digit (at the end of a line after a column gap, alone on a line, or joined to "If you
    # elected") followed by its amount: "... deduction is $X" (Pub. 946) or "$X if the passenger automobile" (Pub. 463).
    for m in re.finditer(r"(?:^|\n|\||[ \t]{3})[ \t]*(\d)[ \t]*(?=\n|If you elected|\$)", text):
        amount = re.search(r"deduction is \$([\d,]+)|\$([\d,]+)(?= if the passenger)", text[m.end():m.end() + 700])
        if amount:
            notes.setdefault(int(m.group(1)), cents(amount.group(1) or amount.group(2)))
    return rows, notes


def window(text, start, length=6000):
    i = text.index(start)
    return text[i:i + length]


def main(archive=ARCHIVE, report=REPORT, out=print):
    if not any(t.exists() for t in TABLES):
        print(f"auto limits: no tables/{Y}/auto_limit*.yaml; nothing to check")
        return 0
    if not all(t.exists() for t in TABLES):
        print(f"auto limits: FAIL, {', '.join(str(t.relative_to(ROOT)) for t in TABLES if not t.exists())} missing")
        return 1
    missing = [f for _, f, _ in PRINTINGS if not (archive / f).exists()]
    if missing:
        msg = (f"no {Y} edition archived of {', '.join(archive_text.shown(archive / f) for f in missing)}: "
               f"the {Y} automobile limit tables cannot be checked against their printings")
        report.write_text(f"# Passenger automobile limits: three printings\n\nNot checked: {msg}.\n", encoding="utf-8")
        out(f"auto limits: FAIL, {msg}")
        return 1
    limit = yaml.safe_load(TABLES[0].read_text())["table"]["rows"]
    first_nb = yaml.safe_load(TABLES[1].read_text())["table"]["rows"]
    mine = {(int(r["keys"][0][1:]), r["keys"][1]): r["value"] for r in limit}
    mine_nb = {int(r["keys"][0][1:]): r["value"] for r in first_nb}
    texts = {name: archive_text.read_file(archive / f) for name, f, _ in PRINTINGS}
    unopened = [f"{name} ({f}): \"{start}\"" for name, f, start in PRINTINGS if start not in texts[name]]
    if unopened:
        msg = (f"the {Y} printing does not carry the opening words its table is found by: {'; '.join(unopened)}; "
               f"read them from the {Y} edition into PRINTINGS")
        report.write_text(f"# Passenger automobile limits: three printings\n\nNot checked: {msg}.\n", encoding="utf-8")
        out(f"auto limits: FAIL, {msg}")
        return 1
    prints = {name: window(texts[name], start) for name, _, start in PRINTINGS}
    failures, compared, lines = 0, 0, ["# Passenger automobile limits: three printings", "",
                                        "Generated by `tools/check_auto_limits.py`; do not edit by hand.", ""]
    for name, text in prints.items():
        rows, notes = parse(text)
        bad = []
        for (y, k), v in sorted(mine.items()):
            if y not in rows:
                bad.append(f"{y}: no row")
                continue
            printed = rows[y][min(k, 4) - 1]
            compared += 1
            if printed != v:
                bad.append(f"{y} year {k}: table {v // 100:,}, printed {printed // 100:,}")
        for y, v in sorted(mine_nb.items()):
            fn = rows.get(y, (None,) * 5)[4]
            printed = notes.get(fn)
            compared += 1
            if printed != v:
                bad.append(f"{y} first year without the allowance: table {v // 100:,}, printed {printed if printed is None else f'{printed // 100:,}'} (footnote {fn})")
        failures += len(bad)
        lines.append(f"- {name}: {'every cell agrees' if not bad else 'FAIL: ' + '; '.join(bad)}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"auto limits: {compared} comparisons over three printings, {failures} failing")
    print(f"report: {report.relative_to(ROOT)}")
    return 1 if failures else 0


def self_test():
    """With an empty archive the check fails naming the missing editions, and with editions that
    do not carry the tables' opening words it fails naming them, each without a traceback."""
    import tempfile
    if not any(t.exists() for t in TABLES):
        print(f"auto limits self-test: no tables/{Y}/auto_limit*.yaml; skipped")
        return 0
    results = []
    for case, plant in (("the year's printings not archived", False), ("the printings without their tables' openings", True)):
        with tempfile.TemporaryDirectory() as tmp:
            if plant:
                for _, f, _ in PRINTINGS:
                    (Path(tmp) / f).write_text("A later edition, reworded.\f", encoding="utf-8")
            try:
                status = main(archive=Path(tmp), report=Path(tmp) / "report.md", out=lambda _msg: None)
                said = (Path(tmp) / "report.md").read_text(encoding="utf-8")
            except Exception as e:  # noqa: BLE001 - the failure this test guards against
                status, said = None, f"{type(e).__name__}: {e}"
        ok = status == 1 and all((start if plant else f) in said for _, f, start in PRINTINGS)
        print(f"auto limits self-test, {case}: " + ("reported" if ok else f"WRONG ({said[:200]})"))
        results.append(ok)
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main())
