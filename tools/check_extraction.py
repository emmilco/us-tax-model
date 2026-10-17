#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Conservation checks on the archived IRS text, offline, in check-all.

The project's encoding and its model reviews read text extracted from the archived
PDFs; these checks make the extraction itself evidence rather than an assumption.
For every archived PDF, per page:

  1. layout vs reading order   The layout text (`<id>.txt`, pdftotext -layout) and the
                               reading-order text (`<id>.cols.txt`, rebuilt here from the
                               same line boxes without hyphen rejoin) carry exactly the
                               same characters. Layout mode spaces, and even interleaves,
                               overlapping strings differently, so words are reported but
                               characters decide.
  2. PDFKit against poppler    An independent reader of the same text layer (Apple's
                               PDFKit through tools/extraction/pdfkit_text.swift). A word
                               PDFKit reads that poppler lacks is evidence of loss and
                               fails the page over the tolerance below. Words poppler
                               reads that PDFKit lacks are counted only: PDFKit skips
                               icon labels and gives up on some pages entirely.
  3. PDF vs HTML               Where the IRS also publishes the document as HTML and the
                               archive holds that snapshot, every word of a page's
                               reading-order text occurs in the HTML text, bar the page furniture in tools/extraction/furniture.txt,
                               numbers, catalog numbers and the pieces of words broken at a
                               line end. Per-page differences that are understood and accepted
                               are listed with their reason in tools/extraction/exceptions.json;
                               the report prints them, and any other difference fails.

Writes reports/2025/extraction.md and exits 1 on any failure.

    check_extraction.py [--no-pdfkit]
"""
import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "sources" / "2025"
REPORT = ROOT / "reports" / "2025" / "extraction.md"
SWIFT = ROOT / "tools" / "extraction" / "pdfkit_text.swift"
FURNITURE = ROOT / "tools" / "extraction" / "furniture.txt"
EXCEPTIONS = ROOT / "tools" / "extraction" / "exceptions.json"  # {doc: {check: {page: reason}}}, each an accepted, explained difference
PDFKIT_PAGE_TOLERANCE = 3   # words only PDFKit reads, per page, before the page fails
PDFKIT_BLIND_SHARE = 0.2    # PDFKit returning fewer tokens than this share of poppler's is reported as blind on that page
CATALOG = re.compile(r"^\d{4,}[a-z]{1,2}$")  # Cat. No. 24811V and the like

sys.path.insert(0, str(ROOT / "tools"))
import extract_text  # noqa: E402

WORD = re.compile(r"[a-z0-9]+(?:['’][a-z]+)?")


def normal(text):
    return (text.lower().replace("\u2019", "'").replace("\ufb01", "fi").replace("\ufb02", "fl")
            .replace("\u00ad", "-").replace("\u2010", "-").replace("\u2011", "-"))


def tokens(text):
    return WORD.findall(normal(text))


def chars(text):
    return Counter(c for c in normal(text) if c.isalnum())


def pages_of(path):
    pages = path.read_text(encoding="utf-8", errors="replace").split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def pdfkit_pages(pdf):
    out = subprocess.run(["swift", str(SWIFT), str(pdf)], capture_output=True, text=True, check=True).stdout
    pages = out.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def exceptions():
    return json.loads(EXCEPTIONS.read_text(encoding="utf-8")) if EXCEPTIONS.exists() else {}


def excepted(doc_id, check, page):
    return exceptions().get(doc_id, {}).get(check, {}).get(str(page))


def fragments(text):
    """Word pieces on either side of a hyphen: a word broken at a line end, or a hyphenated
    compound the HTML may write as one word (SIM-PLE)."""
    out = set()
    for a, b in re.findall(r"(\w+)-(\w*)", normal(text)):
        out.add(a)
        if b:
            out.add(b)
    return out


def furniture():
    if not FURNITURE.exists():
        return set()
    return {w for line in FURNITURE.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#") for w in tokens(line)}


def check_layout_vs_order(entry, layout, lines):
    pdf = ARCHIVE / entry["file"]
    raw = []
    for width, height, lns in extract_text.bbox_pages(pdf):
        lns, guts = extract_text.analyze(width, lns)
        ordered = extract_text.order(width, height, lns, guts)
        raw.append(" ".join(w for l in ordered for w in l.words))
    if len(raw) != len(layout):
        lines.append(f"- **{entry['id']}** layout vs reading order: layout text has {len(layout)} pages, line boxes give {len(raw)} — FAIL")
        return 1
    diff_pages, spacing = [], 0
    for i, (a, b) in enumerate(zip(layout, raw), 1):
        if chars(a) != chars(b):
            ca, cb = Counter(tokens(a)), Counter(tokens(b))
            diff_pages.append((i, sorted((ca - cb).elements()), sorted((cb - ca).elements())))
        elif Counter(tokens(a)) != Counter(tokens(b)):
            spacing += 1
    accepted = [(i, a, b, excepted(entry["id"], "order", i)) for i, a, b in diff_pages if excepted(entry["id"], "order", i)]
    diff_pages = [d for d in diff_pages if not excepted(entry["id"], "order", d[0])]
    note = f" ({spacing} page(s) differ only in word spacing)" if spacing else ""
    if diff_pages:
        lines.append(f"- **{entry['id']}** layout vs reading order: {len(diff_pages)} page(s) differ in their characters — FAIL")
        for i, a, b in diff_pages[:5]:
            lines.append(f"    - p. {i}: only in layout {a[:8]}; only in reading order {b[:8]}")
    else:
        lines.append(f"- **{entry['id']}** layout vs reading order: {len(layout)} pages, identical characters{note}")
    for i, a, b, why in accepted:
        lines.append(f"    - p. {i} accepted: only in layout {a[:6]}; only in reading order {b[:6]} — {why}")
    return 1 if diff_pages else 0


def check_pdfkit(entry, layout, lines):
    pk = pdfkit_pages(ARCHIVE / entry["file"])
    if len(pk) != len(layout):
        lines.append(f"    - PDFKit: {len(pk)} pages against {len(layout)} — FAIL")
        return 1
    bad, extra, skipped, blind = [], 0, 0, []
    for i, (a, b) in enumerate(zip(layout, pk), 1):
        ca, cb = Counter(tokens(a)), Counter(tokens(b))
        only_pk = cb - ca
        extra += sum(only_pk.values()); skipped += sum((ca - cb).values())
        if sum(cb.values()) < PDFKIT_BLIND_SHARE * sum(ca.values()):
            blind.append(i)
        if sum(only_pk.values()) > PDFKIT_PAGE_TOLERANCE:
            bad.append((i, sorted(only_pk.elements())[:8], sum(only_pk.values())))
    blind_note = f"; PDFKit blind on page(s) {blind}" if blind else ""
    if bad:
        lines.append(f"    - PDFKit: {len(bad)} page(s) where PDFKit reads more than {PDFKIT_PAGE_TOLERANCE} words poppler lacks — FAIL{blind_note}")
        for i, b, d in bad[:5]:
            lines.append(f"        - p. {i} ({d}): only PDFKit {b}")
        return 1
    lines.append(f"    - PDFKit: no page where PDFKit reads words poppler lacks beyond tolerance ({extra} such occurrences; {skipped} words poppler reads that PDFKit skips{blind_note})")
    return 0


def check_html(entry, twin, lines):
    H = set(tokens((ARCHIVE / twin["text_file"]).read_text(encoding="utf-8", errors="replace")))
    allow = furniture()
    cols = pages_of(ARCHIVE / entry["cols_file"])
    missing_pages, accepted, previous = [], [], set()
    for i, page in enumerate(cols, 1):
        # Icon labels (TIP, CAUTION, !) that poppler fuses into a line are not words of the text.
        page = re.sub(r"(?<![A-Za-z])(?:TIP|CAUTION|!)(?![A-Za-z])", " ", page)
        # Words are compared unjoined. A piece left by a hyphen is explained when it is a
        # fragment on this page or the one before (a word broken across pages), completes a
        # fragment into a word the HTML has, or completes one into a hyphenated compound
        # whose halves the HTML has.
        frags = fragments(page) | previous
        previous = fragments(page)
        page_tokens = set(tokens(page))

        def explained(w):
            return (w in frags or any(f + w in H for f in frags)
                    or any(w.startswith(f) and w[len(f):] in H and f in H for f in frags))

        miss = sorted({w for w in page_tokens if w not in H and w not in allow and not w.isdigit() and not CATALOG.match(w) and not explained(w)})
        if miss and excepted(entry["id"], "html", i):
            accepted.append((i, miss, excepted(entry["id"], "html", i)))
        elif miss:
            missing_pages.append((i, miss))
    if missing_pages:
        lines.append(f"    - HTML snapshot `{twin['id']}`: {len(missing_pages)} page(s) carry words absent from the HTML — FAIL")
        for i, miss in missing_pages[:8]:
            lines.append(f"        - p. {i}: {miss[:12]}")
    else:
        lines.append(f"    - HTML snapshot `{twin['id']}`: every word of every page occurs in the HTML text" + (f", {len(accepted)} page(s) excepted" if accepted else ""))
    for i, miss, why in accepted:
        lines.append(f"        - p. {i} accepted: {miss[:6]} — {why}")
    return 1 if missing_pages else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-pdfkit", action="store_true", help="skip the PDFKit cross-reading")
    a = ap.parse_args()
    docs = json.loads((ARCHIVE / "manifest.json").read_text())["documents"]
    html_docs = {d["id"][: -len("-html")]: d for d in docs if d["id"].endswith("-html")}
    body, fails, counts = [], Counter(), Counter()
    for entry in docs:
        if entry.get("format", "pdf") != "pdf":
            continue
        layout = pages_of(ARCHIVE / entry["text_file"])
        counts["pdf"] += 1
        fails["order"] += check_layout_vs_order(entry, layout, body)
        if not a.no_pdfkit:
            counts["pdfkit"] += 1
            fails["pdfkit"] += check_pdfkit(entry, layout, body)
        if entry["id"] in html_docs:
            counts["html"] += 1
            fails["html"] += check_html(entry, html_docs[entry["id"]], body)
    total = sum(fails.values())
    lines = ["# Extraction conservation checks", "",
             "Offline checks that the archived IRS text is a faithful reading of the archived PDFs (tools/check_extraction.py). "
             "Words are compared as lower-case alphanumeric tokens per page, characters where spacing differs. The layout text and the reading-order "
             "text come from the same line boxes and must agree exactly; PDFKit reads the text layer independently of poppler and can only show "
             "what poppler lacks; the HTML snapshot is the IRS's own second publication of the instructions.", "",
             "| check | documents | failing |", "| --- | --- | --- |",
             f"| layout vs reading order | {counts['pdf']} | {fails['order']} |",
             f"| PDFKit against poppler | {counts['pdfkit']} | {fails['pdfkit']} |",
             f"| PDF vs HTML snapshot | {counts['html']} | {fails['html']} |",
             "", "## Per document", ""] + body + [""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"extraction: {counts['pdf']} PDFs checked, {counts['html']} against HTML, {total} failing check(s)")
    print(f"report: {REPORT.relative_to(ROOT)}")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
