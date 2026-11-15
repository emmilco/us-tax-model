"""The tax year a tool works on: `--year N` anywhere on the command line, or else
the newest year listed as adopted in years.json. A year qualifies if it has
definitions (forms/<year>/) or a source catalog (tools/sources/<year>.json): an
earlier year may be archived only to compare with (tools/year_diff.py).

years.json lists the adopted years per jurisdiction: `adopted` the federal years
(the newest is the default year), `ny_adopted` the years whose New York data
check-all checks. New York publishes after the IRS, so a federal year may be
adopted before New York's; for such a year the New York steps are skipped, and
say so (tools/jurisdiction.py, ny_status). adopted_years() reads either list.

The flag is removed from sys.argv when this module is imported, so a tool's own
argument parser never sees it; import this module before parsing arguments.
A tool that starts another tool or the engine passes YEAR_ARGS on.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _resolve():
    argv = sys.argv
    for i in range(1, len(argv)):
        arg = argv[i]
        if arg == "--year":
            value = argv[i + 1] if i + 1 < len(argv) else ""
            del argv[i:i + 2]
        elif arg.startswith("--year="):
            value = arg[len("--year="):]
            del argv[i]
        else:
            continue
        if not re.fullmatch(r"\d{4}", value):
            sys.exit(f"--year: expected a four-digit year, got '{value}'")
        if not (ROOT / "forms" / value).is_dir() and not (ROOT / "tools" / "sources" / f"{value}.json").exists():
            sys.exit(f"--year {value}: no data for that year (neither forms/{value}/ nor tools/sources/{value}.json exists)")
        return int(value)
    adopted = adopted_years("adopted")
    if not adopted:
        sys.exit("years.json lists no adopted year; pass --year")
    return max(adopted)


def adopted_years(key="adopted", root=ROOT):
    """The years years.json lists under `key` ("adopted", federal; "ny_adopted", New York). Exits when the
    list is missing or holds anything but four-digit years."""
    data = json.loads((Path(root) / "years.json").read_text())
    years = data.get(key)
    if not isinstance(years, list) or not all(isinstance(y, int) and 1900 <= y <= 2099 for y in years):
        sys.exit(f"years.json: '{key}' must be a list of four-digit years, got {years!r}")
    return years


YEAR = _resolve()
Y = str(YEAR)
YEAR_ARGS = ["--year", Y]


def for_year(by_year, what):
    """`by_year[YEAR]`: what a tool knows of one year's printing (page numbers, coordinates),
    keyed by year. A year it has no entry for exits naming `what`, so the tool fails loudly
    rather than reading another year's pages."""
    if YEAR not in by_year:
        sys.exit(f"{what}: known for {', '.join(str(y) for y in sorted(by_year))} only; "
                 f"read the {Y} printing and add it before running for {Y}")
    return by_year[YEAR]
