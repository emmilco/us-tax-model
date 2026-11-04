"""The jurisdiction a tool works on: `--jurisdiction ny` anywhere on the command line, or
else the federal data (`us`, the default). Like taxyear.py, the flag is removed from
sys.argv when this module is imported, so a tool's own argument parser never sees it;
import this module (after taxyear) before parsing arguments.

The New York data sits in a tree of its own beside the federal one (owner decision C1,
docs/ny/DECISIONS.md): sources/ny/<year>/, forms/ny/<year>/, tables/ny/<year>/,
params/ny/<year>.yaml, ambiguities/ny/<year>.yaml, interview/ny/, fixtures/ny/<year>/,
reviews/ny/<year>/ and reports/ny/<year>/. With the default every path is the federal one,
exactly as before, so federal results do not change.

    ypath("forms")          forms/<year>/            or forms/ny/<year>/
    ypath("reports", "x")   reports/<year>/x         or reports/ny/<year>/x
    params_file()           params/<year>.yaml       or params/ny/<year>.yaml
    register_file()         ambiguities/<year>.yaml  or ambiguities/ny/<year>.yaml
    interview_dir()         interview/               or interview/ny/
    catalog()               tools/sources-<year>.json or tools/sources-ny-<year>.json
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JURISDICTIONS = ("us", "ny")


def _resolve():
    argv = sys.argv
    for i in range(1, len(argv)):
        arg = argv[i]
        if arg == "--jurisdiction":
            value = argv[i + 1] if i + 1 < len(argv) else ""
            del argv[i:i + 2]
        elif arg.startswith("--jurisdiction="):
            value = arg[len("--jurisdiction="):]
            del argv[i]
        else:
            continue
        if value not in JURISDICTIONS:
            sys.exit(f"--jurisdiction: expected one of {', '.join(JURISDICTIONS)}, got '{value}'")
        return value
    return "us"


J = _resolve()
NY = J == "ny"
J_ARGS = ["--jurisdiction", J] if NY else []


def ypath(top, year, *rest):
    """A per-year directory (or a file under it) of the current jurisdiction."""
    base = ROOT / top / "ny" / str(year) if NY else ROOT / top / str(year)
    return base.joinpath(*rest) if rest else base


def params_file(year):
    return ROOT / "params" / ("ny" if NY else "") / f"{year}.yaml" if NY else ROOT / "params" / f"{year}.yaml"


def register_file(year):
    return ROOT / "ambiguities" / "ny" / f"{year}.yaml" if NY else ROOT / "ambiguities" / f"{year}.yaml"


def interview_dir():
    return ROOT / "interview" / "ny" if NY else ROOT / "interview"


def catalog(year):
    return ROOT / "tools" / (f"sources-ny-{year}.json" if NY else f"sources-{year}.json")


def label():
    """How a report names its data: '' federally, ' (New York)' for New York."""
    return " (New York)" if NY else ""
