#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Check the source catalogs' document titles against the archived documents, offline, in check-all.

Each entry of tools/sources-<year>.json and tools/sources-ny-<year>.json may carry a `title`, the
document's printed title, and a `designation`, the form, schedule or publication number as the document
prints it ("Form 1040", "Schedule A (Form 1040)", "Publication 590-A"), each taken verbatim from its archived
text (the web UI shows "<designation> - <title>" as the name of a question's source). A document with no
printed designation (a statute, a Federal Register notice, a statistics table, a web page) has none. A title or
designation must occur in that document's archived text (sources/<year>/<id>.txt or
.cols.txt; New York under sources/ny/<year>/), compared with every run of whitespace as one space, so a
heading broken across lines still matches. A spreadsheet, which has no text file, is matched against its
archived bytes read as Latin-1 and as UTF-16. In a year listed as adopted in years.json every entry
must have a title; in another year the titles present are checked and missing ones are allowed. A designation
is never required.

    check_source_titles.py               check the year's catalogs (taxyear: --year N, default the newest adopted)
    check_source_titles.py --self-test   (in check-all) a missing, absent or unmatched title or designation is reported
"""
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
import archive_text  # noqa: E402


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def load_catalog(path):
    return json.loads(path.read_text(encoding="utf-8"))


def archived_texts(archive, doc_id, manifests):
    """The archived text of a document, whitespace collapsed: its text layers (read through archive_text), or
    the bytes of a spreadsheet, which has none. `manifests` caches each archive's manifest."""
    if archive not in manifests:
        manifests[archive] = archive_text.manifest(archive) if (archive / "manifest.json").exists() else {}
    entry = manifests[archive].get(doc_id)
    if entry is None:
        return []
    texts = [norm(archive_text.read(archive, entry, key)) for key in archive_text.TEXT_KEYS if key in entry]
    if texts or not str(entry.get("file", "")).endswith((".xls", ".xlsx")):
        return texts
    raw = (archive / entry["file"]).read_bytes()
    return [norm(raw.decode("latin-1")), norm(raw.decode("utf-16-le", errors="ignore"))]


def check(catalogs, required):
    """Problems in `catalogs` ([(catalog path, archive dir)]): every title and designation must occur in its
    document's archived text; with `required`, every entry must have a title."""
    problems = []
    manifests = {}
    for catalog, archive in catalogs:
        if not catalog.exists():
            continue
        for entry in load_catalog(catalog):
            doc_id = entry["id"]
            where = f"{catalog.relative_to(catalog.parents[1])}: {doc_id}"
            for field in ("title", "designation"):
                value = entry.get(field)
                if value is None:
                    if required and field == "title":
                        problems.append(f"{where}: no title")
                    continue
                if not isinstance(value, str) or not norm(value):
                    problems.append(f"{where}: the {field} is empty")
                    continue
                texts = archived_texts(archive, doc_id, manifests)
                if not texts:
                    problems.append(f"{where}: no archived text to check the {field} against")
                elif not any(norm(value) in t for t in texts):
                    problems.append(f"{where}: {field} {value!r} does not occur in the archived text")
    return problems


def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "tools").mkdir()
        archive = root / "sources" / "2025"
        archive.mkdir(parents=True)
        (archive / "fa.txt").write_text("SCHEDULE A\n(Form\n 1040)\nItemized\n   Deductions\n", encoding="utf-8")
        (archive / "fb.cols.txt").write_text("Instructions for Form B\n", encoding="utf-8")
        (archive / "sheet.xls").write_bytes(b"\xd0\xcf" + "Table 1.  All Returns".encode("utf-16-le"))
        (archive / "manifest.json").write_text(json.dumps({"documents": [
            {"id": "fa", "file": "fa.pdf", "text_file": "fa.txt"}, {"id": "fb", "file": "fb.pdf", "cols_file": "fb.cols.txt"},
            {"id": "sheet", "file": "sheet.xls"}]}), encoding="utf-8")
        catalog = root / "tools" / "sources-2025.json"
        rows = [{"id": "fa", "title": "Itemized Deductions", "designation": "SCHEDULE A (Form 1040)"},
                {"id": "fb", "title": "Instructions for Form B", "designation": "Instructions for Form B"},
                {"id": "sheet", "title": "Table 1. All Returns"}]
        catalog.write_text(json.dumps(rows), encoding="utf-8")
        assert check([(catalog, archive)], True) == [], "titles across lines, in .cols.txt and in a spreadsheet match"
        rows += [{"id": "fc"}, {"id": "fa", "title": "Itemised Deductions"}, {"id": "missing", "title": "Gone"}, {"id": "fb", "title": " "},
                 {"id": "fa", "title": "Itemized Deductions", "designation": "Schedule A"}, {"id": "fb", "title": "Instructions for Form B", "designation": ""}]
        catalog.write_text(json.dumps(rows), encoding="utf-8")
        got = check([(catalog, archive)], True)
        expect = ["tools/sources-2025.json: fc: no title",
                  "tools/sources-2025.json: fa: title 'Itemised Deductions' does not occur in the archived text",
                  "tools/sources-2025.json: missing: no archived text to check the title against",
                  "tools/sources-2025.json: fb: the title is empty",
                  "tools/sources-2025.json: fa: designation 'Schedule A' does not occur in the archived text",
                  "tools/sources-2025.json: fb: the designation is empty"]
        assert got == expect, got
        assert check([(catalog, archive)], False) == expect[1:], "an unadopted year may lack titles"
        rows = [{"id": "sheet", "designation": "Table 1."}, {"id": "gone", "designation": "Form G"}]
        catalog.write_text(json.dumps(rows), encoding="utf-8")
        assert check([(catalog, archive)], False) == ["tools/sources-2025.json: gone: no archived text to check the designation against"], "a designation may stand without a title and is checked"
    print("check_source_titles self-test: ok (verbatim across lines, .cols.txt, spreadsheet bytes; missing, unmatched, unarchived and empty titles and designations reported)")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return
    adopted = [str(y) for y in json.loads((ROOT / "years.json").read_text())["adopted"]]
    catalogs = [(ROOT / "tools" / f"sources-{Y}.json", ROOT / "sources" / Y),
                (ROOT / "tools" / f"sources-ny-{Y}.json", ROOT / "sources" / "ny" / Y)]
    problems = check(catalogs, Y in adopted)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(f"check_source_titles: {len(problems)} problem(s)")
    entries = [e for c, _ in catalogs if c.exists() for e in load_catalog(c)]
    n, d = sum(1 for e in entries if e.get("title")), sum(1 for e in entries if e.get("designation"))
    print(f"check_source_titles: {n} titles and {d} designations for {Y} occur verbatim in their archived documents"
          + ("" if Y in adopted else f" ({Y} is not adopted; untitled entries allowed)"))


if __name__ == "__main__":
    main()
