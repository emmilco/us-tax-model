# SPDX-License-Identifier: Apache-2.0
"""The pages a citation names and the words on them, for the packets.

A line's `cite.locator` is split into segments with tools/citations.py (its grammar: pages,
then a heading, then quotes; or a form document's printed line number). A page segment names
its pages; a form-line segment is placed on the page where the printed number stands beside
words of the label (citations.line_beside_label, page by page); a span, list or title-only
segment places nothing and is flagged. The cited text is then found among the word boxes of
`pdftotext -bbox-layout` and drawn as translucent rectangles on a copy of the page image.
"""
import re
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import citations as C  # noqa: E402
from taxyear import Y  # noqa: E402

ARCHIVE = ROOT / "sources" / Y
PAGES = ROOT / ".human-review" / "pages"
HIGHLIGHTS = PAGES / "hl"
FILL = {"quote": (255, 230, 0, 90), "heading": (255, 140, 0, 90), "line": (0, 170, 90, 80)}
MAX_FALLBACK_PAGES = 4


def tokens(text):
    """The comparable pieces of a text: alphanumeric runs of its normalized form."""
    return re.findall(r"[a-z0-9]+", C.norm(text))


class Words:
    """The words of one archived PDF page with their boxes, in reading order."""

    def __init__(self, doc, page, arch):
        self.doc, self.page = doc, page
        pdf = ARCHIVE / arch.docs[doc]["file"]
        out = subprocess.run(["pdftotext", "-bbox-layout", "-f", str(page), "-l", str(page), str(pdf), "-"],
                             check=True, capture_output=True, text=True).stdout
        root = ElementTree.fromstring(out)
        ns = {"x": "http://www.w3.org/1999/xhtml"}
        pg = root.find(".//x:page", ns)
        self.width = float(pg.get("width")) if pg is not None else 612.0
        self.height = float(pg.get("height")) if pg is not None else 792.0
        self.words = []  # (text, x0, y0, x1, y1, line index)
        for li, line in enumerate(root.iterfind(".//x:line", ns)):
            for w in line.iterfind("x:word", ns):
                self.words.append((w.text or "", float(w.get("xMin")), float(w.get("yMin")),
                                   float(w.get("xMax")), float(w.get("yMax")), li))
        # token stream: each token knows its word; a word ending in a hyphen is joined to the next
        self.toks, self.tok_word = [], []
        i = 0
        while i < len(self.words):
            text = self.words[i][0]
            owners = [i]
            while text.endswith("-") and i + 1 < len(self.words) and self.words[i + 1][5] != self.words[i][5]:
                i += 1
                text = text[:-1] + self.words[i][0]
                owners.append(i)
            for t in tokens(text):
                self.toks.append(t)
                self.tok_word.append(owners)
            i += 1

    def find(self, parts, start=0):
        """Word indexes matching each part (a token list) in order; None if any part is absent."""
        hits, pos = [], start
        for part in parts:
            if not part:
                continue
            at = self._find_seq(part, pos)
            if at < 0:
                at = self._find_seq(part, 0)
            if at < 0:
                return None
            for k in range(at, at + len(part)):
                hits.extend(self.tok_word[k])
            pos = at + len(part)
        return sorted(set(hits))

    def _find_seq(self, part, start):
        n = len(part)
        for i in range(start, len(self.toks) - n + 1):
            if self.toks[i:i + n] == part:
                return i
        return -1

    def rects(self, word_idx):
        """One rectangle per text line of the matched words."""
        by_line = {}
        for i in word_idx:
            t, x0, y0, x1, y1, li = self.words[i]
            r = by_line.setdefault(li, [x0, y0, x1, y1])
            r[0], r[1], r[2], r[3] = min(r[0], x0), min(r[1], y0), max(r[2], x1), max(r[3], y1)
        return list(by_line.values())

    def line_beside_label(self, number, label):
        """Word indexes of the printed line number and the label words on one text band, or None."""
        grams = C.label_grams(label)
        if not grams:
            return None
        for i, (t, x0, y0, x1, y1, li) in enumerate(self.words):
            if not C.number_in(C.norm(t), number):
                continue
            mid = (y0 + y1) / 2
            band = [j for j, w in enumerate(self.words) if w[2] <= mid + 2 and w[4] >= mid - 2]
            band.sort(key=lambda j: self.words[j][1])
            btoks, owners = [], []
            for j in band:
                for tk in tokens(self.words[j][0]):
                    btoks.append(tk)
                    owners.append(j)
            joined = " " + " ".join(btoks) + " "
            for g in grams:
                if f" {g} " in joined:
                    gt = g.split()
                    at = next(k for k in range(len(btoks) - len(gt) + 1) if btoks[k:k + len(gt)] == gt)
                    return sorted({i, *owners[at:at + len(gt)]})
        return None


def page_png(arch, doc, page, dpi, force=False):
    """The shared image of one archived page, rendered once with pdftoppm."""
    PAGES.mkdir(parents=True, exist_ok=True)
    stem = PAGES / f"{doc}-p{page:03d}"
    png = stem.with_suffix(".png")
    if force or not png.exists():
        pdf = ARCHIVE / arch.docs[doc]["file"]
        subprocess.run(["pdftoppm", "-r", str(dpi), "-f", str(page), "-l", str(page), "-png", "-singlefile",
                        str(pdf), str(stem)], check=True)
    return png


def highlight(base_png, words, marks, slug):
    """A copy of the page image with each mark's rectangles filled; marks are (kind, rects)."""
    HIGHLIGHTS.mkdir(parents=True, exist_ok=True)
    out = HIGHLIGHTS / f"{base_png.stem}-{slug}.png"
    im = Image.open(base_png).convert("RGBA")
    sx, sy = im.width / words.width, im.height / words.height
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for kind, rects in marks:
        for x0, y0, x1, y1 in rects:
            d.rectangle([x0 * sx - 2, y0 * sy - 2, x1 * sx + 2, y1 * sy + 2], fill=FILL[kind])
    Image.alpha_composite(im, layer).convert("RGB").save(out)
    return out


class Locator:
    """What one line's citation locates: pages with marks, and segments that locate nothing."""

    def __init__(self, arch, dpi=110, force=False):
        self.arch, self.dpi, self.force = arch, dpi, force
        self._words = {}

    def words(self, doc, page):
        key = (doc, page)
        if key not in self._words:
            self._words[key] = Words(doc, page, self.arch)
        return self._words[key]

    def page_count(self, doc):
        d = self.arch.docs.get(doc)
        if not d or "text_file" not in d:
            return 0
        return len((ARCHIVE / d["text_file"]).read_text(encoding="utf-8").rstrip("\f").split("\f"))

    def locate(self, doc, locator, label="", printed=""):
        """[(doc, page, [(kind, text, found, rects)])] for the pages the locator names, and
        [(segment text, reason)] for the segments that place nothing."""
        pages, flags = {}, []
        for plain, quotes in C.split_top(locator):
            stripped = plain.strip()
            shown = re.sub("\x00", lambda _, it=iter(quotes): f"“{next(it)}”", stripped)
            m = C.SEGMENT_RE.match(stripped)
            seg_doc = m.group("doc") if m and m.group("doc") in self.arch.docs else doc
            if m:
                nums = C.page_list(m.group(3))
                anchor = C.anchor_of(m.group("rest"))
                self._page_segment(pages, seg_doc, nums, anchor, quotes, label, printed)
                continue
            kind = C.classify(plain, quotes)
            if isinstance(kind, tuple):
                page = self._form_line_page(seg_doc, kind[1], label)
                if page is None:
                    flags.append((shown, f"line {kind[1]} of {seg_doc} was not found beside words of the label "
                                         f"(citations.py's line_beside_label rule); the document's pages are offered instead"))
                    continue
                marks = pages.setdefault((seg_doc, page), [])
                w = self.words(seg_doc, page)
                hit = w.line_beside_label(kind[1], label)
                marks.append(("line", f"line {kind[1]} beside “{' '.join(label.split()[:6])}…”", hit is not None,
                              w.rects(hit) if hit else []))
                for q in quotes:
                    self._quote_mark(marks, w, q)
            elif kind == "quote":
                found = False
                for page in self._pages_with(seg_doc, quotes):
                    marks = pages.setdefault((seg_doc, page), [])
                    w = self.words(seg_doc, page)
                    for q in quotes:
                        self._quote_mark(marks, w, q)
                    found = True
                if not found:
                    flags.append((shown, f"the quote was not found on any page of {seg_doc}"))
            else:
                flags.append((shown, {"span": "a span of lines locates no page", "list": "a list of lines locates no page",
                                      "title": "the document's title alone locates no page",
                                      "none": "no page, line number or quote"}[kind]))
        return [(d, p, marks) for (d, p), marks in pages.items()], flags

    def _page_segment(self, pages, doc, nums, anchor, quotes, label, printed):
        if not self.arch.pages(doc):
            for n in nums:
                pages.setdefault((doc, n), []).append(("heading", anchor, False, []))
            return
        for n in nums:
            pages.setdefault((doc, n), [])
        if quotes:
            for q in quotes:
                parts = [tokens(p) for p in C.parts_of(q)]
                placed = False
                for n in nums + [max(nums) + 1]:
                    if n > self.page_count(doc):
                        break
                    w = self.words(doc, n)
                    hit = w.find(parts)
                    if hit:
                        pages.setdefault((doc, n), []).append(("quote", q, True, w.rects(hit)))
                        placed = True
                        break
                if not placed:
                    pages[(doc, nums[0])].append(("quote", q, False, []))
        else:
            keys = C.anchor_keys(anchor)
            placed = False
            for n in nums:
                w = self.words(doc, n)
                for k in keys:
                    hit = w.find([tokens(" ".join(k))])
                    if hit:
                        pages[(doc, n)].append(("heading", anchor, True, w.rects(hit)))
                        placed = True
                        break
                if placed:
                    break
            if not placed:
                pages[(doc, nums[0])].append(("heading", anchor, False, []))
            if printed and label and re.match(r"^\d", printed):
                for n in nums:
                    w = self.words(doc, n)
                    hit = w.line_beside_label(printed, label)
                    if hit:
                        pages[(doc, n)].append(("line", f"line {printed} beside “{' '.join(label.split()[:6])}…”", True, w.rects(hit)))
                        break

    def _quote_mark(self, marks, w, q):
        parts = [tokens(p) for p in C.parts_of(q)]
        hit = w.find(parts)
        marks.append(("quote", q, hit is not None, w.rects(hit) if hit else []))

    def _pages_with(self, doc, quotes):
        layers = self.arch.pages(doc)
        if not layers:
            return []
        found = set()
        for q in quotes:
            found.update(C.pages_with(layers, C.parts_of(q)))
        return sorted(found)[:2]

    def _form_line_page(self, doc, number, label):
        d = self.arch.docs.get(doc)
        if not d or "text_file" not in d:
            return None
        raw = (ARCHIVE / d.get("cols_file", d["text_file"])).read_text(encoding="utf-8").split("\f")
        for i, page in enumerate(raw):
            rows = [C.norm(r) for r in page.split("\n")]
            if C.line_beside_label([rows], number, label):
                return i + 1
        return None

    def image(self, doc, page, marks, slug):
        """The page image for a packet entry: highlighted when any mark located text."""
        base = page_png(self.arch, doc, page, self.dpi, self.force)
        drawn = [(k, rects) for k, _, found, rects in marks if found and rects]
        if not drawn:
            return base
        return highlight(base, self.words(doc, page), drawn, slug)

    def fallback(self, doc):
        """The pages of a document offered when a segment locates none: all of them, when few."""
        n = self.page_count(doc)
        return list(range(1, n + 1)) if 0 < n <= MAX_FALLBACK_PAGES else []
