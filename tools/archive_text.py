#!/usr/bin/env python3
"""The archived text of an IRS document as the project reads it.

An IRS draft (manifest "draft": true) prints a cover notice as its first page and
watermarks on every page ("TREASURY/IRS AND OMB USE ONLY DRAFT", "DRAFT — DO NOT
FILE"), which the text layers join to the neighbouring sentence. Every tool that
reads an archived text layer for its content reads it here: a draft's watermarks
are removed and its cover page left empty, so page numbers stay those of the PDF.
A final edition's text is returned as extracted.

Tools that audit the extraction itself against the printed page or another
extractor (ocr_audit.py, check_extraction.py, extraction/page_review.py) read the
layers as extracted, watermarks included, since the page prints them; tools that
write the layers (fetch_sources.py, extract_text.py) are not readers.

    archive_text.py --self-test     (in check-all) a planted draft is read without its
                                     marks; every content reader of the archive reads here
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DRAFT_COVER = "The draft you are looking for begins on the next page"
DRAFT_MARKS = re.compile(r"TREASURY/IRS AND OMB USE ONLY DRAFT|DRAFT\s*[—–-]\s*DO NOT FILE|\bDRAFT\b")
TEXT_KEYS = ("text_file", "cols_file")


def drop_draft_marks(text, entry):
    """A draft's extracted text without the IRS cover notice and watermarks."""
    if not entry.get("draft"):
        return text
    pages = text.split("\f")
    if pages and DRAFT_COVER in pages[0]:
        pages[0] = ""
    return "\f".join(DRAFT_MARKS.sub(" ", p) for p in pages)


def manifest(sources):
    """{id: entry} of an archive directory (sources/<year>)."""
    data = json.loads((Path(sources) / "manifest.json").read_text(encoding="utf-8"))
    return {d["id"]: d for d in (data["documents"] if isinstance(data, dict) else data)}


def read(sources, entry, key="text_file"):
    """One text layer (`text_file` or `cols_file`) of a manifest entry, a draft's marks removed."""
    return drop_draft_marks((Path(sources) / entry[key]).read_text(encoding="utf-8"), entry)


def shown(path):
    """A path as messages name it: relative to the repository when inside it."""
    path = Path(path)
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def has_cover(sources, entry):
    """Whether a manifest entry is a draft whose first page is the IRS cover notice."""
    if not entry.get("draft") or not entry["file"].endswith(".pdf"):
        return False
    key = "cols_file" if "cols_file" in entry else "text_file"
    return DRAFT_COVER in (Path(sources) / entry[key]).read_text(encoding="utf-8").split("\f")[0]


def read_file(path):
    """An archived file by path (sources/<year>/<file>), read through its manifest entry
    when it is one of a document's text layers; raises FileNotFoundError if it is absent."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    man = path.parent / "manifest.json"
    if man.exists():
        for entry in manifest(path.parent).values():
            if any(entry.get(k) == path.name for k in TEXT_KEYS):
                return drop_draft_marks(text, entry)
    return text


# ---------- self-test ----------

# Read the layers as extracted, by design (see above), or write them.
AS_EXTRACTED = ["tools/ocr_audit.py", "tools/check_extraction.py", "tools/extraction/page_review.py",
                "tools/extract_text.py", "tools/fetch_sources.py", "tools/archive_text.py"]
# A line that opens or reads a file and names a text layer or the archive directory (not its
# manifest, page classification, PDF or spreadsheets), or that names a .txt file under
# sources/: a text layer read past this module. (A line scan: a layer path built in one
# place and read in another escapes it.)
OPENS = re.compile(r"read_text\(|\bopen\(")
LAYER = re.compile(r"text_file|cols_file|\bARCHIVE\b|\bSOURCES\b|self\.sources\b")
NOT_LAYER = re.compile(r"manifest|\.json|pages_file|\.pdf|\.xls")
LAYER_PATH = re.compile(r"(?:[\"']sources[\"']|\bARCHIVE\b|\bSOURCES\b).*\.txt[\"']")


def self_test():
    import tempfile
    status = 0
    page = "Line 1. Enter the amount TREASURY/IRS AND OMB USE ONLY DRAFT from line 3. DRAFT — DO NOT FILE Line 2."
    cover = f"Caution: DRAFT—NOT FOR FILING\n{DRAFT_COVER}."
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "x.txt").write_text(cover + "\f" + page, encoding="utf-8")
        (d / "y.txt").write_text(cover + "\f" + page, encoding="utf-8")
        (d / "manifest.json").write_text(json.dumps({"documents": [
            {"id": "x", "file": "x.pdf", "text_file": "x.txt", "draft": True},
            {"id": "y", "file": "y.pdf", "text_file": "y.txt"}]}))
        for name, got, want_clean in (("read, draft", read(d, manifest(d)["x"]), True),
                                      ("read_file, draft", read_file(d / "x.txt"), True),
                                      ("read_file, final edition", read_file(d / "y.txt"), False)):
            pages = got.split("\f")
            clean = len(pages) == 2 and pages[0] == "" and "DRAFT" not in got
            ok = clean == want_clean
            status = status or (0 if ok else 1)
            print(f"archive-text self-test, {name}: {'as expected' if ok else 'WRONG: ' + repr(got[:120])}")
    # No other tool opens an archived text layer itself.
    direct = []
    for path in sorted(ROOT.glob("tools/**/*.py")):
        name = str(path.relative_to(ROOT))
        if name in AS_EXTRACTED or "/test_" in name:
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            if "archive_text." in line:
                continue
            if (OPENS.search(line) and LAYER.search(line) and not NOT_LAYER.search(line)) or LAYER_PATH.search(line):
                direct.append(f"{name}:{n}: {line.strip()[:100]}")
    for d in direct:
        print(f"  reads an archived text layer past tools/archive_text.py: {d}")
    print(f"archive-text self-test: {len(direct)} direct read(s) of an archived text layer")
    return status or (1 if direct else 0)


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(__doc__)
