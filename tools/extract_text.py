#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Reading-order text for an archived IRS PDF, from line boxes.

`pdftotext -layout` keeps a page's geometry, which prints a multi-column page's
columns side by side on each output line. This tool reads the line boxes that
`pdftotext -bbox-layout` reports, finds the page's column gutters from the
horizontal coverage of its lines (two or three columns fall out of the data),
and writes each page in reading order: a line that crosses a gutter (a heading,
a wide caution box) closes the band above it; within a band the columns are
read left to right, each top to bottom. Hyphenated line breaks are rejoined
within a column. Each page is classified so a reader can take reading-order
text for columnar prose and keep the layout text for worksheets and tables:

    prose    two or more columns, most lines are sentences, few lines cross a gutter
    table    most lines are short (numbers, labels, worksheet cells)
    single   one column; the layout text already reads in order
    mixed    regions with different column structures (a table above prose, a title box
             beside a caution); such a page is cut into horizontal bands at full-width gaps,
             each band with its own gutters, and is reclassified from its bands: prose when a
             band is columnar prose and the others are prose or single, single when every
             band is single, mixed otherwise

A line crosses a gutter only when it reaches past both of its edges; a line starting inside
a gutter (an item number set out into it) belongs to the column on its right.

    extract_text.py <file.pdf> --out <file.cols.txt> [--pages <file.pages.json>]

The layout text and the reading-order text of a page carry the same words;
check_extraction.py verifies that and more.
"""
import argparse
import html
import json
import re
import subprocess
import tempfile
from pathlib import Path

TOOL_VERSION = "0.10"
GUTTER_MIN_WIDTH = 8.0     # points of near-empty horizontal space that count as a gutter
GUTTER_COVER_SHARE = 0.08  # a gutter bin may be crossed by at most this share of body lines
BODY_WORDS = 4             # a line with fewer words is a label, a number or a cell
FOOTER_BAND = 0.94         # lines starting below this share of the page height are furniture
TABLE_SHORT_SHARE = 0.5    # a page with more short lines than this is a table
PROSE_SPAN_SHARE = 0.10    # columnar prose has at most this share of body words across gutters


class Line:
    __slots__ = ("x0", "y0", "x1", "y1", "words", "block", "boxes")

    def __init__(self, x0, y0, x1, y1, words, block, boxes=None):
        self.x0, self.y0, self.x1, self.y1, self.words, self.block = x0, y0, x1, y1, words, block
        self.boxes = boxes if boxes is not None else [(x0, x1)] * len(words)


SPLIT_GAP_MIN = 8.0    # points: a gap between two words at least this wide ...
SPLIT_GAP_RATIO = 2.0  # ... and this many times the line's median word gap splits the line
ICON_LABELS = {"TIP", "CAUTION"}  # labels of the margin icons, set on the first line of the paragraph they mark


def split_line(words, boxes, y0, y1, block):
    """One pdftotext line may run across a column gutter or absorb an icon label at the same
    baseline. Split it into separate lines wherever two neighbouring words are much farther
    apart than the line's usual word spacing."""
    gaps = [boxes[i + 1][0] - boxes[i][1] for i in range(len(words) - 1)]
    median = sorted(gaps)[len(gaps) // 2] if gaps else 0.0
    threshold = max(SPLIT_GAP_MIN, SPLIT_GAP_RATIO * max(median, 1.0))
    cuts = {i + 1 for i, g in enumerate(gaps) if g > threshold}
    # An icon label stands alone, as its own paragraph, whichever side of it the text continues.
    for i, w in enumerate(words):
        if w in ICON_LABELS:
            cuts.update({i, i + 1})
    out, start = [], 0
    for cut in sorted(c for c in cuts if 0 < c < len(words)) + [len(words)]:
        seg = words[start:cut]
        tag = f"{block}i" if len(seg) == 1 and seg[0] in ICON_LABELS else str(block)
        out.append(Line(boxes[start][0], y0, boxes[cut - 1][1], y1, seg, tag, boxes[start:cut]))
        start = cut
    return out


def bbox_pages(pdf):
    """[(width, height, [Line])] per page, lines in the order pdftotext reports them,
    split where a line runs across a column gutter."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "bbox.html"
        subprocess.run(["pdftotext", "-bbox-layout", str(pdf), str(out)], check=True)
        text = out.read_text(encoding="utf-8")
    pages = []
    for pm in re.finditer(r'<page width="(-?[\d.]+)" height="(-?[\d.]+)">(.*?)</page>', text, re.S):
        width, height = float(pm.group(1)), float(pm.group(2))
        lines = []
        for bi, bm in enumerate(re.finditer(r"<block[^>]*>(.*?)</block>", pm.group(3), re.S)):
            for lm in re.finditer(r'<line xMin="(-?[\d.]+)" yMin="(-?[\d.]+)" xMax="(-?[\d.]+)" yMax="(-?[\d.]+)">(.*?)</line>', bm.group(1), re.S):
                words, boxes = [], []
                for wm in re.finditer(r'<word xMin="(-?[\d.]+)" yMin="(-?[\d.]+)" xMax="(-?[\d.]+)" yMax="(-?[\d.]+)">([^<]+)</word>', lm.group(5)):
                    words.append(html.unescape(wm.group(5))); boxes.append((float(wm.group(1)), float(wm.group(3))))
                if words:
                    lines.extend(split_line(words, boxes, float(lm.group(2)), float(lm.group(4)), bi))
        pages.append((width, height, lines))
    return pages


def gutters(width, lines):
    """Horizontal intervals almost no body word crosses, between covered regions. Coverage
    is counted from word boxes, so a line that poppler ran across two columns does not
    hide the gutter between them; only a word set across it (a wide heading) does."""
    body = [l for l in lines if len(l.words) >= BODY_WORDS]
    if len(body) < 4:
        return []
    bins = int(width) + 1
    cover = [0] * bins
    for l in body:
        for wx0, wx1 in l.boxes:
            for x in range(max(0, int(wx0)), min(bins, int(wx1) + 1)):
                cover[x] += 1
    limit = GUTTER_COVER_SHARE * len(body)
    covered = [c > limit for c in cover]
    first = next((i for i, c in enumerate(covered) if c), None)
    last = next((i for i in range(bins - 1, -1, -1) if covered[i]), None)
    if first is None:
        return []
    out, start = [], None
    for x in range(first, last + 1):
        if not covered[x] and start is None:
            start = x
        elif covered[x] and start is not None:
            if x - start >= GUTTER_MIN_WIDTH:
                out.append((start, x))
            start = None
    return out


def split_at_gutters(lines, guts):
    """Split a line wherever a gap between two of its words spans a gutter."""
    out = []
    for l in lines:
        cuts = set()
        for g0, g1 in guts:
            if l.x0 < g0 and l.x1 > g1:
                for i in range(len(l.words) - 1):
                    if l.boxes[i][1] <= g0 + 2 and l.boxes[i + 1][0] >= g1 - 2:
                        cuts.add(i + 1)
        if not cuts:
            out.append(l); continue
        start = 0
        for cut in sorted(cuts) + [len(l.words)]:
            out.append(Line(l.boxes[start][0], l.y0, l.boxes[cut - 1][1], l.y1, l.words[start:cut], l.block, l.boxes[start:cut]))
            start = cut
    return out


def analyze(width, lines):
    """The page's lines split at its gutters, and the gutters."""
    guts = gutters(width, lines)
    lines = split_at_gutters(lines, guts)
    return lines, gutters(width, lines)


def place(line, guts):
    """Column index of a line, or None when it crosses a gutter."""
    col = 0
    for g0, g1 in guts:
        mid = (g0 + g1) / 2
        if line.x0 < g0 and line.x1 > g1:
            return None  # reaches past both edges: crosses this gutter
        if line.x0 >= mid or line.x0 >= g0:
            col += 1  # right of the gutter, or starting inside it (an outdented item number)
            continue
        return col
    return col


REJOIN_X_TOLERANCE = 40.0      # points: a continuation line starts near the hyphenated line's left edge
REJOIN_RIGHT_TOLERANCE = 15.0  # points: a line broken at a hyphen reaches the block's right edge


def join_words(lines):
    """Words of consecutive lines as one paragraph: a line ending in a hyphen joins the
    next line without the hyphen when the next word is lower-case (a word broken at
    the line end) and keeps it otherwise (a hyphenated name or number such as 1040-SR).
    A word is only broken on a line that reaches the block's right edge, and its
    continuation sits below and starts near the same left edge; in a table header or an
    index the line below a hyphen may belong to another column or entry, and then the
    hyphen stays."""
    words, pending, prev = [], None, None
    right = max((l.x1 for l in lines), default=0.0)
    for line in lines:
        ws = list(line.words)
        if pending is not None:
            continuation = (prev is not None and line.y0 > prev.y0 and abs(line.x0 - prev.x0) <= REJOIN_X_TOLERANCE
                            and prev.x1 >= right - REJOIN_RIGHT_TOLERANCE)
            if ws and continuation and ws[0][:1].islower():
                words.append(pending[:-1] + ws.pop(0))
            elif ws and continuation:
                words.append(pending + ws.pop(0))
            else:
                words.append(pending)
            pending = None
        if ws and len(ws[-1]) > 1 and ws[-1].endswith("-") and ws[-1][-2].isalpha():
            pending = ws.pop()
        words.extend(ws)
        prev = line
    if pending is not None:
        words.append(pending)
    return " ".join(words)


def paragraphs(lines):
    """Lines already in reading order -> text, one paragraph per source block."""
    out, run = [], []
    for l in lines:
        if run and l.block != run[-1].block:
            out.append(join_words(run)); run = []
        run.append(l)
    if run:
        out.append(join_words(run))
    return "\n".join(out)


def order(width, height, lines, guts):
    body_lines = [l for l in lines if l.y0 < FOOTER_BAND * height]
    footer = sorted((l for l in lines if l.y0 >= FOOTER_BAND * height), key=lambda l: (l.y0, l.x0))
    ordered, band = [], []

    def flush():
        # Within a column, a block's lines stay together, blocks in order of their first line.
        top = {}
        for l in band:
            top[l.block] = min(top.get(l.block, l.y0), l.y0)
        band.sort(key=lambda l: (top[l.block], l.block, l.y0, l.x0))
        for col in range(len(guts) + 1):
            ordered.extend(l for l in band if place(l, guts) == col)
        band.clear()

    for l in sorted(body_lines, key=lambda l: (l.y0, l.x0)):
        if place(l, guts) is None:
            flush(); ordered.append(l)
        else:
            band.append(l)
    flush()
    return ordered + footer


def classify(lines, guts):
    if not lines:
        return "single"
    short = sum(1 for l in lines if len(l.words) < BODY_WORDS) / len(lines)
    if short > TABLE_SHORT_SHARE:
        return "table"
    if not guts:
        return "single"
    body = [l for l in lines if len(l.words) >= BODY_WORDS]
    span_words = sum(len(l.words) for l in body if place(l, guts) is None)
    total = sum(len(l.words) for l in body) or 1
    return "prose" if span_words / total <= PROSE_SPAN_SHARE else "mixed"


BAND_GAP = 3.0         # points of vertical space no line occupies that may separate two bands
BAND_MIN_BODY = 6      # a band with fewer body lines cannot fix its own gutters and joins the band above


def compatible(a, b):
    """Two gutter sets describe the same columns: as many gutters, pairwise overlapping."""
    return len(a) == len(b) and all(g0 < h1 and h0 < g1 for (g0, g1), (h0, h1) in zip(a, b))


def bands(width, lines):
    """A mixed page as horizontal bands, each with its own gutters. The page is cut wherever
    a vertical gap of at least BAND_GAP crosses its full width; a band too small to fix its
    gutters joins the band above, and neighbouring bands with compatible gutters merge, so an
    accidental gap across all columns of one region does not split it."""
    runs, run, bottom = [], [], None
    for l in sorted(lines, key=lambda l: (l.y0, l.x0)):
        if run and l.y0 > bottom + BAND_GAP:
            runs.append(run); run = []
        run.append(l)
        bottom = l.y1 if bottom is None or not run[:-1] else max(bottom, l.y1)
    if run:
        runs.append(run)
    out = []  # [raw lines, determining lines, gutters]; gutters come from the determining lines only
    for run in runs:
        determined = sum(1 for l in run if len(l.words) >= BODY_WORDS) >= BAND_MIN_BODY
        guts = analyze(width, run)[1] if determined else None
        if out and guts is None:
            out[-1][0] = out[-1][0] + run
        elif out and out[-1][2] is not None and compatible(out[-1][2], guts):
            out[-1][0] = out[-1][0] + run
            out[-1][1] = out[-1][1] + run
            out[-1][2] = analyze(width, out[-1][1])[1]
        else:
            out.append([run, run if determined else [], guts])
    parts = []
    for raw, _, guts in out:
        guts = guts if guts is not None else analyze(width, raw)[1]
        parts.append((split_at_gutters(raw, guts), guts))
    return parts


def classify_bands(parts):
    """A banded page reads as prose when at least one band is columnar prose and every other
    band is prose or a single column; as single when every band is a single column (a flow
    chart, a worksheet); otherwise it stays mixed."""
    kinds = {classify(l, g) for l, g in parts}
    if kinds == {"single"}:
        return "single"
    return "prose" if "prose" in kinds and kinds <= {"prose", "single"} else "mixed"


def extract(pdf):
    texts, kinds, columns = [], [], []
    for width, height, raw in bbox_pages(pdf):
        lines, guts = analyze(width, raw)
        kind = classify(lines, guts)
        if kind == "mixed":
            body = [l for l in raw if l.y0 < FOOTER_BAND * height]
            footer = [l for l in raw if l.y0 >= FOOTER_BAND * height]
            parts = bands(width, body)
            ordered = [l for blines, bguts in parts for l in order(width, float("inf"), blines, bguts)]
            ordered += sorted(analyze(width, footer)[0], key=lambda l: (l.y0, l.x0))
            texts.append(paragraphs(ordered))
            kinds.append(classify_bands(parts))
            columns.append(max(len(g) + 1 for _, g in parts))
            continue
        ordered = order(width, height, lines, guts)
        texts.append(paragraphs(ordered))
        kinds.append(kind)
        columns.append(len(guts) + 1 if lines else 0)
    return texts, kinds, columns


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--out", required=True, help="reading-order text, pages separated by form feeds")
    ap.add_argument("--pages", help="JSON: per-page classification, column count and the tool version")
    a = ap.parse_args()
    texts, kinds, columns = extract(Path(a.pdf))
    Path(a.out).write_text("".join(t + "\n\f" for t in texts), encoding="utf-8")
    if a.pages:
        Path(a.pages).write_text(json.dumps({"tool_version": TOOL_VERSION, "pages": kinds, "columns": columns}, indent=1) + "\n", encoding="utf-8")
    counts = {k: kinds.count(k) for k in ("prose", "mixed", "table", "single")}
    print(f"{Path(a.pdf).name}: {len(texts)} pages -> {a.out}; {counts}")


if __name__ == "__main__":
    main()
