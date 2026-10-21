#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""One-time image-grounded audit of the archived IRS text layers.

The conservation checks (check_extraction.py) compare readings of the PDF text
layer with each other and with the HTML publication. This audit reads the rendered
page image instead, with Tesseract, and lists what the image reading finds that the
text layer lacks (text drawn as graphics, a glyph mapped to the wrong character) and
what the text layer has that the image reading lacks (hidden or duplicated text).
OCR misreads digits and ornaments on its own, so the output is a list to adjudicate
against the page once, not a gate: adjudications go in reviews/<year>/extraction/.

    ocr_audit.py [--docs id,id] [--dpi 300] [--jobs 8] --out reviews/<year>/extraction/ocr_audit.md
"""
import argparse
import difflib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
ARCHIVE = ROOT / "sources" / Y
WORD = re.compile(r"[a-z0-9]+(?:['’][a-z]+)?")
MIN_LEN = 3            # shorter tokens are ornaments, line labels or OCR dust
NEAR = 0.85            # similarity at which an OCR word is taken to be a text-layer word misread
DUST = re.compile(r"^(?:[ec0os]+|\d+)$")  # leader dots read as letters, bare numbers


def tokens(text):
    return WORD.findall(text.lower().replace("’", "'").replace("ﬁ", "fi").replace("ﬂ", "fl").replace("­", "-"))


def pages_of(path):
    pages = path.read_text(encoding="utf-8", errors="replace").split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def ocr_page(pdf, page, dpi, tmp):
    base = Path(tmp) / f"p{page:04d}"
    subprocess.run(["pdftoppm", "-r", str(dpi), "-f", str(page), "-l", str(page), "-png", "-singlefile", str(pdf), str(base)], check=True)
    r = subprocess.run(["tesseract", str(base) + ".png", "stdout", "--psm", "3"], capture_output=True, text=True, check=True)
    return r.stdout


def near(word, vocabulary):
    if word in vocabulary:
        return True
    for cand in difflib.get_close_matches(word, vocabulary, n=1, cutoff=NEAR):
        return True
    return False


def fusions(seq):
    """Concatenations of two or three adjacent words: what OCR reads when a form sets
    words tightly along a dotted line."""
    out = set()
    for i in range(len(seq) - 1):
        out.add(seq[i] + seq[i + 1])
        if i + 2 < len(seq):
            out.add(seq[i] + seq[i + 1] + seq[i + 2])
    return out


def unexplained(words, counter_other, seq_other):
    vocab = [w for w in counter_other if len(w) >= MIN_LEN]
    fused = fusions(seq_other)
    return sorted(w for w in words if len(w) >= MIN_LEN and not DUST.match(w) and w not in fused
                  and not any(w == a + b for a in vocab for b in vocab if w.startswith(a) and len(a) >= 2 and len(b) >= 2)
                  and not near(w, vocab))


def audit_document(entry, dpi, jobs):
    pdf = ARCHIVE / entry["file"]
    layer = pages_of(ARCHIVE / entry["text_file"])
    with tempfile.TemporaryDirectory() as tmp:
        with ThreadPoolExecutor(max_workers=jobs) as ex:
            ocr = list(ex.map(lambda p: ocr_page(pdf, p, dpi, tmp), range(1, len(layer) + 1)))
    rows = []
    for i, (lay, img) in enumerate(zip(layer, ocr), 1):
        tl, to = tokens(lay), tokens(img)
        L, O = Counter(tl), Counter(to)
        only_image = unexplained(O, L, tl)
        only_layer = unexplained(L, O, to)
        rows.append({"page": i, "layer_words": sum(L.values()), "image_words": sum(O.values()), "only_image": only_image, "only_layer": only_layer})
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docs", help="comma-separated document ids (default: every archived PDF)")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--out", required=True)
    ap.add_argument("--json", help="also write the raw per-page rows here")
    a = ap.parse_args()
    docs = [d for d in json.loads((ARCHIVE / "manifest.json").read_text())["documents"] if d.get("format", "pdf") == "pdf"]
    if a.docs:
        want = set(a.docs.split(",")); docs = [d for d in docs if d["id"] in want]
    out = ["# Image-grounded audit of the archived text layers", "",
           f"Tesseract {subprocess.run(['tesseract', '--version'], capture_output=True, text=True).stdout.splitlines()[0]} over pages rendered at {a.dpi} dpi with pdftoppm (tools/ocr_audit.py). "
           "Per page, words of at least three characters that the image reading has and the text layer lacks, and the reverse; a word is explained by a text-layer word within edit similarity 0.85, by two or three adjacent words read as one, by leader dots read as letters, or by being a bare number. "
           "OCR noise is expected; each listed page is adjudicated once against the page image.", "",
           "| document | pages | words in layer | words in image | pages with image-only words | pages with layer-only words |", "| --- | --- | --- | --- | --- | --- |"]
    details, raw = [], {}
    for d in docs:
        rows = audit_document(d, a.dpi, a.jobs)
        raw[d["id"]] = rows
        pi = [r for r in rows if r["only_image"]]; pl = [r for r in rows if r["only_layer"]]
        out.append(f"| {d['id']} | {len(rows)} | {sum(r['layer_words'] for r in rows)} | {sum(r['image_words'] for r in rows)} | {len(pi)} | {len(pl)} |")
        details.append(f"## {d['id']}")
        details.append("")
        for r in rows:
            if r["only_image"] or r["only_layer"]:
                details.append(f"- p. {r['page']}: image only {r['only_image'][:15]}{' …' if len(r['only_image']) > 15 else ''}; layer only {r['only_layer'][:15]}{' …' if len(r['only_layer']) > 15 else ''}")
        details.append("")
        print(f"{d['id']}: {len(rows)} pages; image-only on {len(pi)} pages, layer-only on {len(pl)} pages", flush=True)
    out += ["", "## Per page", ""] + details
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text("\n".join(out), encoding="utf-8")
    if a.json:
        Path(a.json).write_text(json.dumps(raw, indent=1), encoding="utf-8")
    print(f"report: {a.out}")


if __name__ == "__main__":
    main()
