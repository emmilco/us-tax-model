#!/usr/bin/env python3
"""Where a year's archived documents print what the tools read by page: tools/layouts/<year>.json.

    layouts.py --check [--year N]          (check-all) each range's pages are where its words are printed
    layouts.py --propose --from 2025 --to 2026
    layouts.py --self-test                 (check-all)

Each layout names a document and its page ranges (1-based PDF pages, as `pages: [first, last]`),
each with the printed words that place it: `first`, printed on the range's first page (the
lowest page that prints them); `last`, printed on its last page (the highest page that prints
them); `last_before`, printed on the page after it (the lowest page that prints them; the range
ends the page before); `each`, a list of words whose lowest pages are the range's pages. A
range with no `first` starts at page 1, one with neither `last` nor `last_before` ends at 999
(the end of the document). Words are compared as tools/citations.py compares quotes (case,
dashes, quotes and spacing normalized). `fields` are a layout's other values for the year (column
coordinates, the last row of a table, a document id), which no printed words place.

A tool reads its layout with `get(name)`; a year with no file, or no entry, exits naming the file
and this tool, so a tool never reads another year's pages.

--check fails when a range's pages are not where its words are printed in the year's archive,
or its document is not archived. --propose writes tools/layouts/<to>.json from the from-year's
file: every range placed again by its words in the to-year's archive (years in the words moved),
and the fields carried, each listed for review; a range whose words are not printed, or whose
document has no edition archived, is left out and listed, and the file is not written unless
--partial is given.
"""
import argparse
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import taxyear  # noqa: E402
import citations as C  # noqa: E402
import year_diff  # noqa: E402

DIR = ROOT / "tools" / "layouts"
END = 999


def path_of(year):
    return DIR / f"{year}.json"


_LOADED = {}


def get(name, year=None):
    """The layout `name` of the year (taxyear's by default); exits naming the file when there is none."""
    year = year or taxyear.YEAR
    p = path_of(year)
    if p not in _LOADED:
        _LOADED[p] = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    if name not in _LOADED[p]:
        sys.exit(f"{name}: no layout for {year} in {p.relative_to(ROOT)}; place its pages with "
                 f"`python3 tools/layouts.py --propose --from {year - 1} --to {year}` and review them")
    return _LOADED[p][name]


def pages_of(entry, rng):
    """Every page of a named range [first, last]."""
    first, last = entry["ranges"][rng]["pages"]
    return list(range(first, last + 1))


def place(layers, r, shift=0):
    """[first, last] of a range found by its words in a document's layers, or a reason it is not placed."""
    def hits(words):
        return C.pages_with(layers, C.parts_of(year_diff.year_shifted(words, shift)))
    if "each" in r:
        found = []
        for w in r["each"]:
            h = hits(w)
            if not h:
                return f"“{w}” is not printed"
            found.append(h[0])
        return [min(found), max(found)] if sorted(set(found)) == list(range(min(found), max(found) + 1)) else \
            f"the pages of {r['each']} are not consecutive: {sorted(set(found))}"
    first = 1
    if "first" in r:
        h = hits(r["first"])
        if not h:
            return f"“{r['first']}” is not printed"
        first = h[0]
    last = END
    if "last" in r:
        h = hits(r["last"])
        if not h:
            return f"“{r['last']}” is not printed"
        last = h[-1]
    elif "last_before" in r:
        h = hits(r["last_before"])
        if not h:
            return f"“{r['last_before']}” is not printed"
        last = h[0] - 1
    if last < first:
        return f"its words place it at pages {first} to {last}"
    return [first, last]


def check(year, arch=None, out=print):
    p = path_of(year)
    if not p.exists():
        out(f"layouts: no {p.relative_to(ROOT)}; nothing to check")
        return 0
    arch = arch or C.Archive(str(year))
    bad, n = [], 0
    for name, entry in json.loads(p.read_text(encoding="utf-8")).items():
        layers = arch.pages(entry["doc"])
        if not layers:
            bad.append(f"{name}: no {year} edition of {entry['doc']} archived")
            continue
        for rng, r in entry["ranges"].items():
            n += 1
            got = place(layers, r)
            if got != r["pages"]:
                bad.append(f"{name}.{rng}: pages {r['pages']}, " + (f"its words place it at {got}" if isinstance(got, list) else got))
    out(f"layouts {year}: {n} page ranges, {len(bad)} not where their words are printed")
    for b in bad:
        out(f"  FAIL {b}")
    return 1 if bad else 0


def propose(from_year, to_year, partial=False, arch=None, out=print, write=True):
    src = json.loads(path_of(from_year).read_text(encoding="utf-8"))
    arch = arch or C.Archive(str(to_year))
    shift = to_year - from_year
    result, missing, review = {}, [], []
    for name, entry in src.items():
        layers = arch.pages(entry["doc"])
        if not layers:
            missing.append(f"{name}: no {to_year} edition of {entry['doc']} archived")
            continue
        ranges, ok = {}, True
        for rng, r in entry["ranges"].items():
            got = place(layers, r, shift)
            if not isinstance(got, list):
                missing.append(f"{name}.{rng}: {got} in the {to_year} edition of {entry['doc']}")
                ok = False
                continue
            words = {k: (year_diff.year_shifted(v, shift) if isinstance(v, str) else
                         [year_diff.year_shifted(x, shift) for x in v]) for k, v in r.items() if k != "pages"}
            ranges[rng] = {"pages": got, **words}
        if not ok:
            continue
        new = {k: v for k, v in entry.items() if k not in ("ranges", "fields")}
        new["ranges"] = ranges
        if "fields" in entry:
            new["fields"] = entry["fields"]
            review.append(f"{name}: fields carried from {from_year}, to read from the {to_year} edition: {', '.join(entry['fields'])}")
        result[name] = new
    out(f"layouts {from_year} -> {to_year}: {len(result)} of {len(src)} layouts placed")
    for m in missing:
        out(f"  NOT PLACED {m}")
    for r in review:
        out(f"  REVIEW {r}")
    if write and (not missing or partial) and result:
        path_of(to_year).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        out(f"wrote {path_of(to_year).relative_to(ROOT)}")
    return result, missing


def self_test():
    """A planted later edition with a page inserted before the table: the range moves with its
    words; a range whose words are gone is not placed; the 2025 file's ranges are where their words
    are printed (the check)."""
    import archive_text  # noqa: F401
    ok = []
    entry = {"t": {"doc": "d", "what": "w", "ranges": {
        "a": {"pages": [2, 3], "first": "table one begins", "last": "table one continued"},
        "b": {"pages": [4, 999], "first": "part two of the year 2025"},
        "c": {"pages": [1, 3], "last_before": "part two of the year 2025"}}, "fields": {"edge": 5}}}
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        def plant(name, pages):
            d = tmp / name
            d.mkdir()
            (d / "d.txt").write_text("\f".join(pages), encoding="utf-8")
            (d / "manifest.json").write_text(json.dumps({"documents": [{"id": "d", "file": "d.pdf", "text_file": "d.txt"}]}),
                                             encoding="utf-8")
            return C.Archive("2026", sources=d)
        later = plant("later", ["cover", "a new page", "Table one begins here", "table one continued", "Part two of the year 2026"])
        global path_of
        saved = path_of
        path_of = lambda y: tmp / f"{y}.json"  # noqa: E731
        try:
            (tmp / "2025.json").write_text(json.dumps(entry), encoding="utf-8")
            got, missing = propose(2025, 2026, arch=later, out=lambda _m: None, write=False)
            r = got.get("t", {}).get("ranges", {})
            ok.append(("a page inserted: every range moves with its words",
                       not missing and r.get("a", {}).get("pages") == [3, 4] and r.get("b", {}).get("pages") == [5, 999]
                       and r.get("c", {}).get("pages") == [1, 4] and "2026" in r["b"]["first"]))
            gone = plant("gone", ["cover", "something else", "Part two of the year 2026"])
            got, missing = propose(2025, 2026, arch=gone, out=lambda _m: None, write=False)
            ok.append(("words not printed: the layout is not placed", "t" not in got and any("table one begins" in m for m in missing)))
        finally:
            path_of = saved
    said = []
    ok.append(("the 2025 layouts are where their words are printed", check(2025, out=said.append) == 0))
    for name, passed in ok:
        print(f"layouts self-test, {name}: {'as expected' if passed else 'WRONG'}")
    if not ok[-1][1]:
        print("\n".join(said))
    return 0 if all(p for _, p in ok) else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--propose", action="store_true")
    ap.add_argument("--from", dest="from_year", type=int)
    ap.add_argument("--to", dest="to_year", type=int)
    ap.add_argument("--partial", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if a.propose:
        if not (a.from_year and a.to_year):
            ap.error("--propose needs --from and --to")
        _, missing = propose(a.from_year, a.to_year, a.partial)
        return 1 if missing and not a.partial else 0
    return check(taxyear.YEAR)


if __name__ == "__main__":
    sys.exit(main())
