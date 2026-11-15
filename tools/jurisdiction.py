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
    interview_dir(year)     interview/<year>/        or interview/ny/<year>/
    catalog()               tools/sources/<year>.json or tools/sources/ny/<year>.json

The tax year is taxyear.py's (the newest year in years.json unless --year N), for both jurisdictions.
New York publishes its forms for a year after the IRS does, so a year can have federal data and no
New York data. In New York mode a year qualifies if it has New York definitions (forms/ny/<year>/) or
a New York catalog (tools/sources/ny/<year>.json): require_year() exits naming what is missing, and is
called on import for the year taxyear resolved when taxyear was imported first. A New York-only tool
calls ny_only(), which makes New York its jurisdiction without the flag and refuses --jurisdiction us.

Whether check-all checks New York for a year is a separate matter: New York has adopted the year when
years.json lists it under `ny_adopted`, which requires its definitions (forms/ny/<year>/). For any other
year check-all skips its New York steps and says so, so a federal year can be adopted before New York
publishes (plan decision D1). ny_status() answers; from the shell:

    jurisdiction.py --ny-status [--year N]   prints whether check-all checks New York for the year:
                                             exit 0 checked, 3 skipped (the reason printed), 2 a bad list
    jurisdiction.py --self-test
"""

import json
import os
import sys
import tempfile
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
        return value, True
    return "us", False


J, EXPLICIT = _resolve()
NY = J == "ny"
J_ARGS = ["--jurisdiction", J] if NY else []


def has_year(year):
    """Whether New York has data for a tax year: its definitions or its source catalog."""
    return (ROOT / "forms" / "ny" / str(year)).is_dir() or (ROOT / "tools" / "sources" / "ny" / f"{year}.json").exists()


def no_year(year, tool=None):
    """The message for a year New York has no data for."""
    known = sorted(p.stem for p in (ROOT / "tools" / "sources" / "ny").glob("*.json"))
    return (f"{tool + ': ' if tool else ''}--jurisdiction ny --year {year}: New York has no data for {year} "
            f"(neither forms/ny/{year}/ nor tools/sources/ny/{year}.json exists; New York years: "
            f"{', '.join(known) or 'none'}). A New York year starts with its catalog, written when New York "
            f"publishes that year's forms (tools/README.md, \"New York years\").")


def require_year(year, tool=None):
    """In New York mode, exit unless New York has data for the year (federally, nothing to check)."""
    if NY and not has_year(year):
        sys.exit(no_year(year, tool))


def ny_status(year, root=ROOT):
    """(checked, reason) for a tax year: checked is True when years.json lists the year under `ny_adopted`,
    and reason is then ''; otherwise reason says why check-all skips New York. Exits when the list names a
    year with no New York definitions, or is missing or malformed."""
    data = json.loads((Path(root) / "years.json").read_text())
    listed = data.get("ny_adopted")
    if not isinstance(listed, list) or not all(isinstance(y, int) and 1900 <= y <= 2099 for y in listed):
        sys.exit(f"years.json: 'ny_adopted' must be a list of four-digit years, got {listed!r}")
    has_forms = (Path(root) / "forms" / "ny" / str(year)).is_dir()
    if int(year) in listed:
        if not has_forms:
            sys.exit(f"years.json lists {year} under ny_adopted, but forms/ny/{year}/ does not exist: "
                     f"New York is adopted with its definitions")
        return True, ""
    shown = ", ".join(str(y) for y in sorted(listed)) or "none"
    reason = f"New York has not adopted {year} (years.json ny_adopted: {shown})"
    if has_forms:
        reason += f"; forms/ny/{year}/ exists, so add {year} to ny_adopted to check it"
    return False, reason


def ny_only(tool):
    """For a tool that works on New York data only: New York mode without the flag; --jurisdiction us refused."""
    global J, NY, J_ARGS
    if EXPLICIT and not NY:
        sys.exit(f"{tool}: New York only; --jurisdiction {J} is not supported")
    J, NY, J_ARGS = "ny", True, ["--jurisdiction", "ny"]
    if "taxyear" in sys.modules:
        require_year(sys.modules["taxyear"].YEAR, tool)


if NY and "taxyear" in sys.modules:
    require_year(sys.modules["taxyear"].YEAR)


def ypath(top, year, *rest):
    """A per-year directory (or a file under it) of the current jurisdiction."""
    base = ROOT / top / "ny" / str(year) if NY else ROOT / top / str(year)
    if NY and top == "reviews" and os.environ.get("NY_REVIEWS_ROOT"):
        base = Path(os.environ["NY_REVIEWS_ROOT"])  # tests: a temporary New York review tree
    return base.joinpath(*rest) if rest else base


def params_file(year):
    return ROOT / "params" / ("ny" if NY else "") / f"{year}.yaml" if NY else ROOT / "params" / f"{year}.yaml"


def register_file(year):
    return ROOT / "ambiguities" / "ny" / f"{year}.yaml" if NY else ROOT / "ambiguities" / f"{year}.yaml"


def interview_dir(year):
    return (ROOT / "interview" / "ny" if NY else ROOT / "interview") / str(year)


def catalog(year):
    return (ROOT / "tools" / "sources" / "ny" if NY else ROOT / "tools" / "sources") / f"{year}.json"


def label():
    """How a report names its data: '' federally, ' (New York)' for New York."""
    return " (New York)" if NY else ""


# The review tools (tools/transcription/) review one jurisdiction's documents at a time, but a New
# York line reads federal lines, so they read across both trees. A document's own files are found
# by its id (New York ids start `ny_`, which the build enforces), whatever the mode; the documents a
# mode reviews are those of its own jurisdiction; the documents it can read are the federal ones,
# plus the New York ones in New York mode. Federally every one of these is the federal path alone.

def is_ny(doc_id):
    return str(doc_id).startswith("ny_")


def mine(doc_id):
    """Whether a document belongs to the jurisdiction under review."""
    return is_ny(doc_id) == NY


def doc_dir(top, year, doc_id):
    """The per-year directory holding a document's file: <top>/ny/<year>/ for a New York document."""
    return ROOT / top / "ny" / str(year) if is_ny(doc_id) else ROOT / top / str(year)


def read_dirs(top, year):
    """The per-year directories whose documents the current jurisdiction reads: the federal one,
    then (New York) the New York one."""
    return [ROOT / top / str(year)] + ([ROOT / top / "ny" / str(year)] if NY else [])


# A New York review keeps the federal tools' fixed request wording, which speaks of IRS forms and pages,
# and opens with this note instead; nothing in the request after it (catalog, interfaces, pages) is altered,
# so the interface text a request must carry verbatim (input_context.py) is the same as the documents'.
NY_NOTE = (
    "Jurisdiction: New York State. The forms, worksheets and instructions in this request are New York State\n"
    "personal income tax documents (Form IT-201 and its instructions, from the New York State Department of\n"
    "Taxation and Finance), not IRS documents. Wherever the request below says IRS, read it as the New York\n"
    "State tax department and its archived pages. An amount the New York text says to take from the federal\n"
    "return (for example \"federal Form 1040, line 1z\") is a line of another form; where the request lists\n"
    "that federal line, it is referenced by the id listed.\n\n")
NY_SYSTEM = "The documents are New York State personal income tax forms and instructions, not IRS ones."


def preface(prompt):
    """A review request for the jurisdiction: unchanged federally; NY_NOTE first in New York mode."""
    return NY_NOTE + prompt if NY else prompt


def system(text):
    """A review's system prompt for the jurisdiction: unchanged federally; NY_SYSTEM added in New York mode."""
    return f"{text} {NY_SYSTEM}" if NY else text


def _self_test():
    bad = []

    def expect(what, got, want):
        if got != want:
            bad.append(f"{what}: got {got!r}, expected {want!r}")

    def status(listed, forms, year):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "years.json").write_text(json.dumps({"adopted": [2025, 2026], "ny_adopted": listed}))
            for y in forms:
                (root / "forms" / "ny" / str(y)).mkdir(parents=True)
            try:
                return ny_status(year, root)
            except SystemExit as e:
                return ("exit", str(e))

    expect("an adopted year", status([2025], [2025], 2025), (True, ""))
    expect("a year New York has not adopted",
           status([2025], [2025], 2026), (False, "New York has not adopted 2026 (years.json ny_adopted: 2025)"))
    got = status([2025], [2025, 2026], 2026)
    expect("a year with New York definitions, not listed, is skipped and told to add it",
           (got[0], "add 2026 to ny_adopted" in got[1]), (False, True))
    got = status([2025, 2026], [2025], 2026)
    expect("a listed year with no New York definitions exits",
           (got[0], "forms/ny/2026/ does not exist" in got[1]), ("exit", True))
    expect("an empty list", status([], [], 2025), (False, "New York has not adopted 2025 (years.json ny_adopted: none)"))
    got = status(None, [2025], 2025)
    expect("a missing list exits", (got[0], "'ny_adopted' must be a list" in got[1]), ("exit", True))
    got = status(["2025"], [2025], 2025)
    expect("a year written as a string exits", got[0], "exit")
    if bad:
        print("jurisdiction self-test FAILED:\n  " + "\n  ".join(bad), file=sys.stderr)
        return 1
    print("jurisdiction self-test OK: 7 cases of ny_status (adopted, not adopted, data not listed, listed without "
          "data, empty, missing and malformed lists)")
    return 0


def _main():
    sys.path.insert(0, str(ROOT / "tools"))
    import taxyear  # removes --year from sys.argv
    argv = sys.argv[1:]
    if argv == ["--self-test"]:
        return _self_test()
    if argv != ["--ny-status"]:
        sys.exit(f"jurisdiction.py: expected --ny-status [--year N] or --self-test, got {' '.join(argv) or 'nothing'}")
    checked, reason = ny_status(taxyear.YEAR)
    print(f"New York {taxyear.Y}: adopted, checked" if checked else reason)
    return 0 if checked else 3


if __name__ == "__main__":
    sys.exit(_main())
