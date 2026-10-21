"""The tax year a tool works on: `--year N` anywhere on the command line, or else
the newest year listed as adopted in years.json.

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
        if not (ROOT / "forms" / value).is_dir():
            sys.exit(f"--year {value}: no data for that year (forms/{value}/ does not exist)")
        return int(value)
    adopted = json.loads((ROOT / "years.json").read_text())["adopted"]
    if not adopted:
        sys.exit("years.json lists no adopted year; pass --year")
    return max(adopted)


YEAR = _resolve()
Y = str(YEAR)
YEAR_ARGS = ["--year", Y]
