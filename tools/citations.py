#!/usr/bin/env python3
"""Check, and for a new year relocate, the page numbers of citation locators.

A locator such as `p. 17, Step 1, "Any age and permanently and totally disabled"`
names pages, then a heading (its anchor: the first phrase after the pages), then
any quotes. Page numbers move from year to year; the anchor and quotes mostly do
not. This tool reads every locator in the year's data (forms, tables, params,
ambiguity register, interviews), splits it into segments at top-level `;` (a
segment may name another document first: `i4562 p. 4, Part I`), and, for each
segment that names pages of an archived PDF:

  check (default, in check-all)
      every quote must appear on the cited pages (it may run on to the next
      page), and the anchor must appear on one of them, both compared after
      normalizing case, whitespace, quotes, dashes and line-end hyphenation,
      with `...` splitting a quote into parts that must all appear. An anchor
      that is not printed text (a section name such as "Schedule 1", a
      paraphrase) needs a ruling in reviews/<year>/citations.json, keyed by
      document and anchor, as does a quote the extracted text cannot show
      verbatim (a worksheet box read out of order); a ruling no finding uses is
      reported.

      On a computed line (a form line whose atom is not input, param or copy)
      every segment of the line's own locator must also carry a credential
      that places the cited text: pages (checked as above), a quote (which
      must appear somewhere in the document), or one printed line number of a
      form document ("Schedule 8812 (2025), line 10"), verified by finding
      that number as a standalone token on the same line of the form's
      archived text as three consecutive words of the project line's label
      (fewer words when the label is shorter). A span of lines ("lines 1–18"),
      a list of lines, a segment that is only the document's title, or one
      that names no line, quote or page is rejected; so is a line number on
      an instruction booklet, which needs a page. The rejected segments are
      listed under "Locators to rewrite" in the report.

      Writes reports/<year>/citations.md; exits 1 on any unruled page
      finding. The computed-line findings are counted and listed but fail the
      check only with --strict, which check-all passes.

  --relocate --from <year>
      for a year whose locators were just copied from <year> (year_diff.py
      --adopt), find each segment's quotes (or else its anchor) in this year's
      archived text and rewrite the segment's page numbers in place where they
      moved. Shifts are learnt from nearby quotes printed on one page; a move
      must keep the anchor as it stood on the <year> page (printed there, so
      printed on the new page, not only in force from a page before), and a
      segment that more than one nearby shift places, or none, is listed for
      review. Segments left over are tried again with the shifts of the other
      left-over segments. A draft with a cover page and no quote evidence moves
      by the cover. Writes reports/<year>/relocation_from_<from>.md, marking the
      segments left for review that the check passes unmoved. The rewrite is an
      ordinary diff to read before committing.
      Without --from (run again): a segment the check passes stays where it is;
      the rest are relocated with the shifts of the segments that do not pass.
      Relocating the result of a relocation changes nothing.

  --self-test (in check-all)
      move every page number of this year's (checked) locators by +2, then by
      -1, then by +1 before each document's middle and +2 from it (an inserted
      page), relocate, and report how many come back to the authored pages; then
      relocate again with half the quote evidence a page early and the rest in
      place; exits 1 if any is placed on a page other than its authored one (a
      segment left for review is not a failure). Archive one document without
      quote evidence again as a draft with a cover page: each segment must move
      by one page. Rewrite two page lists folded into one locator, the
      second's old number the first's new one; exits 1 unless each is rewritten in
      its own place. Then plant locators on a computed line: a
      span of lines must be reported and a correct form-line locator must
      verify; exits 1 otherwise.
"""

import argparse
import collections
import glob
import html
import io
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
import archive_text  # noqa: E402
from archive_text import DRAFT_COVER  # noqa: E402

RULINGS = ROOT / "reviews" / Y / "citations.json"
REPORT = ROOT / "reports" / Y / "citations.md"
RULINGS_PAGE = ROOT / "reports" / Y / "citations.html"
INPUT_QUOTES = ROOT / "reviews" / Y / "input_quotes.json"
INPUT_QUOTES_REPORT = ROOT / "reports" / Y / "input_quotes.md"

PAGES_RE = r"(\d+(?:\s*[–—-]\s*\d+)?(?:(?:,\s*|\s+and\s+)\d+(?:\s*[–—-]\s*\d+)?)*)"
SEGMENT_RE = re.compile(r"^(?:(?P<doc>[a-z][a-z0-9-]*)\s+)?(?P<pp>pp?\.)\s*" + PAGES_RE + r"(?P<rest>.*)$", re.S)


# ---------- text ----------

def norm(text):
    # a soft hyphen is printed only where a word breaks at a line end: join the word across it
    text = re.sub("­\\s*", "", unicodedata.normalize("NFKC", text))
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    # one quotation mark for all (a locator may nest single quotes where the page prints
    # double), dashes as hyphens, list bullets and the flow-chart arrow glyph dropped
    text = text.translate(str.maketrans({"‘": "'", "’": "'", "“": "'", "”": "'", '"': "'",
                                         "–": "-", "—": "-", "−": "-", "•": " ", "䊲": " "}))
    text = re.sub(r"(?:\s*\.){3,}(?=\s)", " ", text)  # leader dots of a worksheet entry
    text = re.sub(r"\s*-\s+|\s+-\s*", "-", text)  # "Chart \u2014 Line 18a" as "Chart\u2014Line 18a"
    return re.sub(r"\s+", " ", text).lower().strip()


def parts_of(quote):
    """The pieces of a quote that must each appear: `...` and `[...]` mark omissions."""
    pieces = (norm(p).strip(" ,.;:") for p in re.split(r"\.\s?\.\s?\.|…|\[[^\]]*\]", quote))
    return [p for p in pieces if p]


class Archive:
    def read(self, doc, key):
        """One archived text layer of a document (`cols_file` or `text_file`), a draft's
        cover and watermarks removed (tools/archive_text.py)."""
        return archive_text.read(self.sources, self.docs[doc], key)

    def has_cover(self, doc):
        """Whether the document is a draft whose first page is the IRS cover notice."""
        d = self.docs.get(doc)
        return bool(d) and archive_text.has_cover(self.sources, d)

    def __init__(self, year=Y, sources=None):
        self.sources = Path(sources) if sources else ROOT / "sources" / str(year)
        self.docs = archive_text.manifest(self.sources)
        self.cache = {}

    def pages(self, doc):
        """Normalized pages of a PDF's two text layers (reading order, layout), or None."""
        if doc not in self.cache:
            d = self.docs.get(doc)
            layers = []
            if d and d["file"].endswith(".pdf"):
                for key in ("cols_file", "text_file"):
                    if key in d:
                        pages = self.read(doc, key).split("\f")
                        layers.append([norm(p) for p in pages])
            self.cache[doc] = layers or None
        return self.cache[doc]

    def raw_page(self, doc, page):
        """One page of a PDF's reading-order text, as extracted."""
        d = self.docs[doc]
        pages = self.read(doc, "cols_file" if "cols_file" in d else "text_file").split("\f")
        return pages[page - 1] if 0 < page <= len(pages) else ""

    def _raw_layers(self, doc):
        d = self.docs.get(doc)
        if not d:
            return []
        return [self.read(doc, key) for key in ("cols_file", "text_file") if key in d]

    def whole(self, doc):
        """The normalized text of each layer of any archived document, or None."""
        key = ("whole", doc)
        if key not in self.cache:
            layers = [norm(t) for t in self._raw_layers(doc)]
            self.cache[key] = layers or None
        return self.cache[key]

    def lines(self, doc):
        """Each layer of any archived document as its normalized lines of text
        (the lines of the extraction, not the printed line numbers), or None."""
        key = ("lines", doc)
        if key not in self.cache:
            layers = [[norm(row) for row in t.split("\n")] for t in self._raw_layers(doc)]
            self.cache[key] = layers or None
        return self.cache[key]


def on_pages(layers, pages, quote_parts, spill):
    """Whether every part appears in the text of `pages` (in one layer); with `spill`
    the text runs on into the page after the last, but the first part must start
    on a cited page."""
    for layer in layers:
        cited = " ".join(layer[p - 1] for p in pages if 0 < p <= len(layer))
        if all(q in cited for q in quote_parts):
            return True
        if spill:
            nxt = max(pages) + 1
            ext = cited + " " + (layer[nxt - 1] if nxt <= len(layer) else "")
            first = ext.find(quote_parts[0])
            if 0 <= first < len(cited) and all(q in ext[first:] for q in quote_parts):
                return True
    return False


def pages_with(layers, quote_parts):
    """Pages (1-based) on which every part appears, in either layer."""
    return sorted({i + 1 for layer in layers for i, t in enumerate(layer) if all(q in t for q in quote_parts)})


# ---------- locators ----------

def page_list(text):
    out = []
    for part in re.split(r",\s*|\s+and\s+", text.strip()):
        r = re.match(r"^(\d+)\s*[–—-]\s*(\d+)$", part.strip())
        if r:
            out += list(range(int(r.group(1)), int(r.group(2)) + 1))
        elif part.strip().isdigit():
            out.append(int(part))
    return out


OPEN = {'"': '"', "“": "”", "'": "'"}


def split_top(text):
    """Split a locator into segments at `;` outside quotes, and each segment into
    plain text and quotes. A single quote opens a quote only at the start of a word
    and closes only before the end, punctuation or a conjunction, so apostrophes
    inside a quote are kept."""
    segments, current, quotes, buf = [], [], [], []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c in OPEN and (i == 0 or not text[i - 1].isalnum()):
            close = OPEN[c]
            if close == "'":
                m = re.compile(r"'(?=\s*(?:$|[,;:)]|and\b|or\b|in\b|\(|\"))").search(text, i + 1)
                j = m.start() if m else -1
            else:
                j = text.find(close, i + 1)
            if j > i + 1:
                quotes.append(text[i + 1:j])
                buf.append("\x00")
                i = j + 1
                continue
        if c == ";":
            segments.append(("".join(buf), quotes))
            buf, quotes = [], []
            i += 1
            continue
        buf.append(c)
        i += 1
    segments.append(("".join(buf), quotes))
    return segments


def anchor_of(rest):
    """The first plain phrase after the pages: up to a comma, colon, parenthesis or quote."""
    head = re.split(r"[,:(\x00]", rest.lstrip(" ,"), maxsplit=1)[0].strip(" .")
    return head


IN_FORCE = 2  # pages before the cited one on which the heading in force may be printed


def anchor_keys(anchor):
    """What may be printed for an anchor, most specific first: the anchor itself;
    of a compound ("Lines 6 to 8", "Steps 1 and 4", "lines 4a-5b") its first member;
    and that member with a plural "Lines"/"Steps" read as the singular heading."""
    first = re.split(r"\s+(?:and|to|through)\s+|\s*[\u2013\u2014]\s+|(?<=\d)-(?=\d)|(?<=\d[a-z])-(?=\d)", anchor, maxsplit=1, flags=re.I)[0]
    first = first.rstrip("-")
    single = re.sub(r"^(Line|Step|Part|Column|Box)s\b", r"\1", first, flags=re.I)
    keys = []
    for k in (anchor, first, single):
        pk = parts_of(k)
        if pk and pk not in keys:
            keys.append(pk)
    return keys


def anchor_on(layers, pages, anchor):
    """Whether the anchor is printed on the cited pages, or is a heading still in
    force there: printed at most IN_FORCE pages before the first."""
    reach = list(range(max(1, min(pages) - IN_FORCE), min(pages))) + list(pages)
    return any(on_pages(layers, [p], k, spill=False) for k in anchor_keys(anchor) for p in reach)


def segments(doc, locator):
    """(doc, pages, anchor, quotes, span) per segment that names pages; span is the
    (start, end) of the page list within the locator, for rewriting."""
    out = []
    offset = 0
    text = locator
    for plain, quotes in split_top(text):
        stripped = plain.lstrip()
        lead = len(plain) - len(stripped)
        m = SEGMENT_RE.match(stripped)
        seg_doc = doc
        if m and m.group("doc"):
            seg_doc = m.group("doc")
        if m and (not m.group("doc") or True):
            pages = page_list(m.group(3))
            # locate the page list in the original locator: the n-th "p." after offset
            pos = text.find(m.group("pp"), offset)
            num = re.compile(r"pp?\.\s*" + PAGES_RE).match(text, pos)
            span = (num.start(1), num.end(1)) if num else None
            out.append((seg_doc, pages, anchor_of(m.group("rest")), quotes, span))
        # advance past this segment in the original text
        semi = _segment_end(text, offset)
        offset = semi + 1
    return out


def _segment_end(text, start):
    """Index of the top-level `;` ending the segment that starts at `start` (or len)."""
    i, n = start, len(text)
    while i < n:
        c = text[i]
        if c in OPEN and (i == 0 or not text[i - 1].isalnum()):
            close = OPEN[c]
            if close == "'":
                m = re.compile(r"'(?=\s*(?:$|[,;:)]|and\b|or\b|in\b|\(|\"))").search(text, i + 1)
                j = m.start() if m else -1
            else:
                j = text.find(close, i + 1)
            if j > i + 1:
                i = j + 1
                continue
        if c == ";":
            return i
        i += 1
    return n


# ---------- data ----------

def data_files(year=Y):
    y = str(year)
    files = sorted(glob.glob(str(ROOT / "forms" / y / "*.yaml"))) + sorted(glob.glob(str(ROOT / "tables" / y / "*.yaml")))
    files += [str(ROOT / "params" / f"{y}.yaml"), str(ROOT / "ambiguities" / f"{y}.yaml")]
    files += sorted(f for f in glob.glob(str(ROOT / "interview" / "*.yaml")) if re.search(rf"(^|-){y}\.yaml$", os.path.basename(f)))
    return files


def citations(path):
    """(doc, locator, line) for every mapping with `doc` and `locator`, with the
    1-based line of the locator scalar in the file."""
    out = []
    def walk(node):
        if isinstance(node, yaml.MappingNode):
            keys = {k.value: v for k, v in node.value if isinstance(k, yaml.ScalarNode)}
            if "doc" in keys and "locator" in keys and isinstance(keys["locator"], yaml.ScalarNode):
                out.append((keys["doc"].value, keys["locator"].value, keys["locator"].start_mark.line + 1))
            for _, v in node.value:
                walk(v)
        elif isinstance(node, yaml.SequenceNode):
            for v in node.value:
                walk(v)
    walk(yaml.compose(open(path, encoding="utf-8")))
    return out


def form_files(year=Y):
    return sorted(glob.glob(str(ROOT / "forms" / str(year) / "*.yaml")))


COMPUTED_EXEMPT = {"input", "param", "copy"}


def computed_lines(path):
    """(form id, line id, label, doc, locator, file line) for each computed line
    of a form file: a line whose atom is not input, param or copy, with the
    1-based line of its locator scalar."""
    def mapping(node):
        return {k.value: v for k, v in node.value if isinstance(k, yaml.ScalarNode)} \
            if isinstance(node, yaml.MappingNode) else {}
    root = mapping(yaml.compose(open(path, encoding="utf-8")))
    doc = mapping(root.get("form") or root.get("def"))
    form_id = doc["id"].value if "id" in doc else os.path.basename(path)[:-5]
    out = []
    for node in (doc["lines"].value if "lines" in doc else []):
        line = mapping(node)
        op = mapping(line.get("expr")).get("op")
        if op is None or op.value in COMPUTED_EXEMPT:
            continue
        cite = mapping(line.get("cite"))
        if "doc" not in cite or "locator" not in cite:
            continue
        out.append((form_id, line["id"].value, line["label"].value if "label" in line else "",
                    cite["doc"].value, cite["locator"].value, cite["locator"].start_mark.line + 1))
    return out


def rel(path):
    return os.path.relpath(path, ROOT)


# ---------- computed lines ----------

FORM_DOC_RE = re.compile(r"^f(?:w2|\d)")  # a form document, as opposed to instructions or a publication
LINE_RE = re.compile(r"\b(lines?)\s+(\d+[a-z]?)\b", re.I)
TITLE_RE = re.compile(r"^(?:form|schedule|instructions for (?:form|schedule)|publication|pub\.?)\s+[\w.-]+"
                      r"(?:\s*\(form\s+[\w-]+\))?(?:\s*\(\d{4}\))?\.?$", re.I)
# a number preceded by one of these words refers to a line, box, part or amount; it is not the printed number
REF_WORDS = {"line", "lines", "box", "boxes", "form", "forms", "schedule", "schedules", "part", "parts", "step",
             "steps", "column", "columns", "section", "sections", "page", "pages", "chapter", "worksheet", "table",
             "tier", "age", "under", "over", "through", "and", "or", "to", "than", "of", "x", "code", "codes", "no"}
LABEL_WORDS = 3  # consecutive words of the label that must share a line of text with the printed number


def label_grams(label):
    words = re.findall(r"[a-z0-9]+", norm(label))
    n = min(LABEL_WORDS, len(words))
    return [" ".join(words[i:i + n]) for i in range(len(words) - n + 1)] if n else []


def number_in(row, number):
    """Whether `number` is printed as a standalone token on the normalized text
    row: not part of a larger number, a dollar amount, a decimal or a
    percentage, and not preceded by a word that makes it a reference."""
    pat = re.compile(r"(?<![\w$,.\-])" + re.escape(number) + r"(?![\w%]|[.,]\d)")
    for m in pat.finditer(row):
        prev = re.search(r"([a-z]+)\s*$", row[:m.start()])
        if prev and prev.group(1) in REF_WORDS:
            continue
        return True
    return False


def line_beside_label(layers, number, label):
    """Whether some row of a layer prints `number` as a standalone token and
    LABEL_WORDS consecutive words of the label (all of them when it is shorter)."""
    grams = label_grams(label)
    if not grams:
        return False
    for layer in layers:
        for row in layer:
            if number_in(row, number):
                words = " " + " ".join(re.findall(r"[a-z0-9]+", row)) + " "
                if any(f" {g} " in words for g in grams):
                    return True
    return False


def classify(plain, quotes):
    """The credential a page-less segment offers: "quote", ("line", number), or
    the reason it offers none: "span", "list", "title", "none"."""
    text = plain.strip(" ,.")
    if quotes:
        return "quote"
    m = LINE_RE.search(text)  # the first mention decides; a later one is a note
    if m:
        ranged = re.match(r"\s*(?:[–—-]|to\b|through\b)\s*\d", text[m.end():])
        if ranged:
            return "span"
        return "list" if m.group(1).lower() == "lines" else ("line", m.group(2).lower())
    if TITLE_RE.match(text):
        return "title"
    return "none"


NEEDS = {
    "span": "a span of lines places nothing: cite the one printed line this value comes from, or a page with a quote",
    "list": "several lines place nothing: cite the one printed line this value comes from, or a page with a quote",
    "title": "the document's title alone: a printed line number, a quote, or a page locator",
    "none": "no line number, quote or page: a printed line number, a quote, or a page locator",
    "booklet": "a line number on {doc}, not a form: a page (`p. N, <heading>`) with a quote",
    "quote": "the quote was not found in {doc}: quote the text as printed, on a page locator",
    "unplaced": "line {n} of {doc} was not found on a row of its text beside words of the label “{label}”: "
                "cite the printed line whose text the label follows, or add a quote of the line as printed",
    "notext": "{doc} has no archived text: cite a document with one",
}


def check_computed(arch, rows, rulings=frozenset()):
    """Check every segment of each computed line's locator. `rows` are
    (path, form id, line id, label, doc, locator, file line); `rulings` the
    keys of reviews/<year>/citations.json, which excuse a quote here as in the
    page check. Returns the counts and the findings (path, file line, form id,
    line id, locator, segment, need)."""
    counts, findings = collections.Counter(), []
    for path, form_id, line_id, label, doc, locator, file_line in rows:
        counts["computed lines"] += 1
        for plain, quotes in split_top(locator):
            counts["computed-line segments"] += 1
            stripped = plain.strip()
            m = SEGMENT_RE.match(stripped) or re.match(r"^(?P<doc>[a-z][a-z0-9-]*)\s", stripped)
            seg_doc = m.group("doc") if m and m.group("doc") in arch.docs else doc
            if m and "pp" in m.groupdict():
                counts["computed-line segments with pages"] += 1
                continue
            need = None
            kind = classify(plain, quotes)
            if kind == "quote":
                counts["computed-line segments with a quote and no page"] += 1
                whole = arch.whole(seg_doc)
                if whole is None:
                    need = "notext"
                else:
                    missing = [q for q in quotes if parts_of(q) and ("quote", seg_doc, q) not in rulings
                               and not any(all(p in w for p in parts_of(q)) for w in whole)]
                    if missing:
                        need = "quote"
                        counts["quotes without a page not found"] += 1
                    else:
                        counts["quotes without a page found"] += 1
            elif isinstance(kind, tuple):
                counts["form-line locators"] += 1
                if not FORM_DOC_RE.match(seg_doc):
                    need = "booklet"
                    counts["form-line locators on a booklet"] += 1
                else:
                    layers = arch.lines(seg_doc)
                    if layers is None:
                        need = "notext"
                    elif line_beside_label(layers, kind[1], label):
                        counts["form-line locators verified"] += 1
                    else:
                        need = "unplaced"
                        counts["form-line locators not placed"] += 1
            else:
                need = kind
                counts[f"computed-line segments rejected: {kind}"] += 1
            if need:
                n = kind[1] if isinstance(kind, tuple) else ""
                short = label if len(label) <= 60 else label[:57].rstrip() + "…"
                shown = re.sub("\x00", lambda _, it=iter(quotes): f"“{next(it)}”", stripped)
                findings.append((rel(path), file_line, form_id, line_id, locator, shown,
                                 NEEDS[need].format(n=n, doc=seg_doc, label=short)))
    return counts, findings


# ---------- quotes outside computed lines and page locators ----------

def quote_sites(stream, path_label, exempt=frozenset()):
    """Quotes the page check does not reach, in one YAML document: those of a
    locator segment that names no page, and those of a citation's `quote` key.
    Computed lines (their locator at a line in `exempt`) are checked by
    check_computed. Each site is a dict with the owner (the nearest enclosing
    line, parameter or table, keyed by its id), the owner's canonical data
    (`subject`), the document, the quote and its file line."""
    loader = yaml.SafeLoader("")
    root = yaml.compose(stream)
    stem = os.path.basename(path_label).rsplit(".", 1)[0]
    sites = []

    def owner_of(stack):
        for name, node in reversed(stack):
            if isinstance(node, yaml.MappingNode):
                ids = [v.value for k, v in node.value if isinstance(k, yaml.ScalarNode) and k.value == "id"
                       and isinstance(v, yaml.ScalarNode)]
                if ids:
                    return ids[0], node
                if name is not None and len(stack) > 1 and name != "params":
                    return name, node
        return stem, root

    def walk(node, stack, name):
        if isinstance(node, yaml.MappingNode):
            keys = {k.value: v for k, v in node.value if isinstance(k, yaml.ScalarNode)}
            stack = stack + [(name, node)]
            if "doc" in keys and "locator" in keys and isinstance(keys["locator"], yaml.ScalarNode):
                owner, onode = owner_of(stack[:-1])
                subject = json.dumps(loader.construct_object(onode, deep=True), sort_keys=True, default=str)
                doc, locator = keys["doc"].value, keys["locator"].value
                at = keys["locator"].start_mark.line + 1
                if (path_label, at) not in exempt:
                    for plain, quotes in split_top(locator):
                        if quotes and not SEGMENT_RE.match(plain.strip()):
                            m = re.match(r"^([a-z][a-z0-9-]*)\s", plain.strip())
                            for q in quotes:
                                sites.append({"owner": f"{stem}:{owner}", "subject": subject, "doc": doc,
                                              "lead_doc": m.group(1) if m else None, "quote": q,
                                              "file": path_label, "line": at, "via": "locator"})
                if isinstance(keys.get("quote"), yaml.ScalarNode):
                    sites.append({"owner": f"{stem}:{owner}", "subject": subject, "doc": doc, "lead_doc": None,
                                  "quote": keys["quote"].value, "file": path_label,
                                  "line": keys["quote"].start_mark.line + 1, "via": "quote key"})
            for k, v in node.value:
                walk(v, stack, k.value if isinstance(k, yaml.ScalarNode) else None)
        elif isinstance(node, yaml.SequenceNode):
            for v in node.value:
                walk(v, stack, None)
    walk(root, [], None)
    return sites


def diagnose(whole, qp):
    """Why a quote is not found in a document's text: the cause in words."""
    flat = lambda t: re.sub(r"[^a-z0-9]", "", t)
    text = " ".join(whole)
    squeezed = flat(text)
    missing = [p for p in qp if not any(p in w for w in whole)] or qp
    if all(flat(p) in squeezed for p in missing):
        return "typography or spacing only (matches once punctuation and spaces are ignored)"
    words = " ".join(missing).split()
    best = 0
    for i in range(len(words)):
        for j in range(len(words), i + best, -1):
            if " ".join(words[i:j]) in text:
                best = j - i
                break
    if best >= max(4, len(words) // 2):
        return f"partly printed (longest matching run {best} of {len(words)} words): a paraphrase or an alteration"
    if best >= 3:
        return f"mostly absent (longest matching run {best} of {len(words)} words): a paraphrase"
    return "absent from the document's text"


def check_input_quotes(arch, sites, rulings=frozenset()):
    """Check each site's quote against the whole text of its document (a segment's
    leading document id, else the citation's). Returns the counts and the findings
    in the form tools/baseline_check.py takes."""
    counts, found, seen = collections.Counter(), [], set()
    for s in sites:
        doc = s["lead_doc"] if s["lead_doc"] in arch.docs else s["doc"]
        qp = parts_of(s["quote"])
        if not qp:
            continue
        counts["quotes checked"] += 1
        counts[f"quotes checked: {s['via']}"] += 1
        whole = arch.whole(doc)
        if whole is None:
            cause = f"{doc} has no archived text"
        elif ("quote", doc, s["quote"]) in rulings:
            counts["quotes ruled in citations.json"] += 1
            continue
        elif any(all(p in w for p in qp) for w in whole):
            counts["quotes matched"] += 1
            continue
        else:
            cause = diagnose(whole, qp)
        counts["quotes unmatched"] += 1
        k = f"{s['owner']} {doc} “{' '.join(s['quote'].split())[:70]}”"
        if k in seen:
            continue
        seen.add(k)
        found.append({"kind": "input-quote", "line": k, "form": s["owner"], "subject": s["subject"],
                      "detail": f"`{s['file']}:{s['line']}` {doc}, {s['via']} “{' '.join(s['quote'].split())}”: {cause}",
                      "cause": cause})
    return counts, found


def input_quotes(strict=False, rebaseline=False):
    import baseline_check
    arch, rulings = Archive(), load_rulings()
    exempt = {(rel(p), row[5]) for p in form_files() for row in computed_lines(p)}
    sites = []
    for path in data_files():
        with open(path, encoding="utf-8") as f:
            sites += quote_sites(f, rel(path), exempt)
    counts, found = check_input_quotes(arch, sites, rulings)
    legend = ("Quotes of citations outside computed lines that no page locator reaches (a locator segment without "
              "pages, a citation's `quote` key) must appear in the cited document. Unmatched quotes are accepted by "
              f"the baseline in `reviews/{Y}/input_quotes.json`; an entry comes due when its own line, parameter "
              "or table changes. " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    status = baseline_check.run("input quotes", [], found, INPUT_QUOTES, INPUT_QUOTES_REPORT,
                                f"Input, parameter and gate citation quotes, tax year {Y}", legend, rebaseline)
    print(f"input quotes: {counts['quotes checked']} checked, {counts['quotes unmatched']} unmatched "
          f"({counts['quotes matched']} matched)")
    return status if strict else 0


# ---------- check ----------

def load_rulings():
    if not RULINGS.exists():
        return {}
    data = json.loads(RULINGS.read_text())
    return {("anchor", r["doc"], r["anchor"]): r for r in data.get("anchors", [])} | \
        {("quote", r["doc"], r["quote"]): r for r in data.get("quotes", [])}


def check(strict=False):
    arch, rulings = Archive(), load_rulings()
    used, uses = set(), collections.defaultdict(list)
    findings, counts = [], collections.Counter()
    for path in data_files():
        for doc, locator, line in citations(path):
            for seg_doc, pages, anchor, quotes, _ in segments(doc, locator):
                layers = arch.pages(seg_doc)
                if layers is None:
                    counts["segments on documents without PDF text"] += 1
                    continue
                counts["segments checked"] += 1
                for q in quotes:
                    qp = parts_of(q)
                    if not qp:
                        continue
                    counts["quotes"] += 1
                    if not on_pages(layers, pages, qp, spill=True):
                        if ("quote", seg_doc, q) in rulings:
                            used.add(("quote", seg_doc, q))
                            uses[("quote", seg_doc, q)].append((rel(path), line, locator, pages))
                            counts["quotes ruled"] += 1
                            continue
                        found = pages_with(layers, qp)
                        findings.append((rel(path), line, seg_doc, pages, "quote", q, found))
                keys = anchor_keys(anchor)
                if not keys:
                    continue
                counts["anchors"] += 1
                if anchor_on(layers, pages, anchor):
                    continue
                key = ("anchor", seg_doc, anchor)
                if key in rulings:
                    used.add(key)
                    uses[key].append((rel(path), line, locator, pages))
                    counts["anchors ruled"] += 1
                    continue
                findings.append((rel(path), line, seg_doc, pages, "anchor", anchor,
                                 next((h for h in (pages_with(layers, k) for k in keys) if h), [])))
    unused = sorted(set(rulings) - used)
    rows = [(path, *item) for path in form_files() for item in computed_lines(path)]
    ccounts, rewrite = check_computed(arch, rows, rulings)
    out = [f"# Citation pages, tax year {Y}", "",
           "Generated by `tools/citations.py`: every quote in a page locator must appear on the cited pages",
           "(it may run on to the next page), and the locator's anchor, its first phrase after the pages (of a",
           "compound anchor, its first member), on one of them or as a heading in force up to two pages before.",
           f"An anchor or quote that cannot match printed text carries a ruling in `reviews/{Y}/citations.json`,",
           f"listed with its uses in `reports/{Y}/citations.html`.", "",
           "On a computed line (atom not input, param or copy) every segment of the line's locator must carry",
           "pages, a quote found in the document, or one printed line number of a form document found on a line",
           "of the form's text beside three consecutive words of the label. The segments that do not are listed",
           "under \"Locators to rewrite\"; they fail the check only with `--strict`.", ""]
    out += [f"- {k}: {v}" for k, v in sorted(counts.items())]
    out += [f"- findings without a ruling: {len(findings)}", f"- rulings no anchor uses: {len(unused)}", ""]
    out += [f"- {k}: {v}" for k, v in sorted(ccounts.items())]
    out += [f"- locators to rewrite: {len(rewrite)}", ""]
    if findings:
        out += ["## Findings", ""]
        for path, line, doc, pages, kind, text, found in findings:
            where = f"found on p. {', '.join(map(str, found[:8]))}" if found else "not found in the document"
            out.append(f"- `{path}:{line}` {doc} p. {_pages_text(pages)}, {kind} “{text}”: {where}")
        out.append("")
    if unused:
        out += ["## Unused rulings", ""] + [f"- {k} {d}: “{a}”" for k, d, a in unused] + [""]
    if rewrite:
        out += ["## Locators to rewrite", "",
                "Segments of computed-line locators that place nothing the check can verify, by form; each gives",
                "the line, the segment as written and what the check needs instead.", ""]
        by_form = collections.defaultdict(list)
        for row in rewrite:
            by_form[row[2]].append(row)
        for form_id in sorted(by_form):
            out += [f"### {form_id} ({len(by_form[form_id])})", ""]
            for path, line, _, line_id, locator, segment, need in by_form[form_id]:
                out.append(f"- `{line_id}` (`{path}:{line}`) — “{segment}” — {need}")
            out.append("")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(out))
    write_rulings_page(arch, rulings, uses)
    print(f"citations: {counts['segments checked']} segments, {counts['quotes']} quotes, {counts['anchors']} anchors "
          f"({counts['quotes ruled']} and {counts['anchors ruled']} ruled); {len(findings)} finding(s), {len(unused)} unused ruling(s)")
    print(f"computed lines: {ccounts['computed lines']} lines, {ccounts['computed-line segments']} segments; "
          f"{ccounts['form-line locators verified']} form-line locators verified, "
          f"{ccounts['form-line locators not placed']} not placed; {len(rewrite)} locator segment(s) to rewrite"
          + ("" if strict else " (reported only; --strict fails on them)"))
    print(f"report: reports/{Y}/citations.md")
    return 1 if findings or unused or (strict and rewrite) else 0


def write_rulings_page(arch, rulings, uses):
    """reports/<year>/citations.html: each ruling with its reason, every locator
    that relies on it, and the cited page's extracted text for comparison."""
    e = html.escape
    rows = []
    for key in sorted(rulings, key=lambda k: (k[0], k[1], k[2])):
        kind, doc, text = key
        r = rulings[key]
        found = uses.get(key, [])
        excerpt = ""
        if found:
            pages = found[0][3]
            raw = arch.raw_page(doc, pages[0])
            if kind == "quote":
                probe = parts_of(text)[0][:25]
                i = norm(raw).find(probe)
                flat = re.sub(r"\s+", " ", raw)
                excerpt = flat[max(0, i - 200):i + 500] if i >= 0 else flat[:700]
            else:
                excerpt = re.sub(r"\s+", " ", raw)[:700]
            excerpt = f"<p class=src>{e(doc)} p. {pages[0]}, extracted text:</p><blockquote>{e(excerpt)}\u2026</blockquote>"
        locs = "".join(f"<li><code>{e(p)}:{n}</code> {e(loc)}</li>" for p, n, loc, _ in found) or "<li>(unused)</li>"
        rows.append(f"""<section class="{e(r.get('status', ''))}">
<h2><span class=kind>{e(kind)}</span> <span class=doc>{e(doc)}</span> \u201c{e(text)}\u201d</h2>
<p class=meta>{e(r.get('kind', ''))} \u00b7 status: <b>{e(r.get('status', ''))}</b> \u00b7 used by {len(found)} locator(s)</p>
<p>{e(r.get('reason', ''))}</p>
<details><summary>Locators</summary><ul>{locs}</ul></details>
{excerpt}
</section>""")
    proposed = sum(1 for r in rulings.values() if r.get("status") == "proposed")
    page = f"""<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>Citation rulings, tax year {Y}</title>
<style>
:root {{ color-scheme: light dark; --ink: #1d1d1f; --muted: #6e6e73; --line: #d2d2d7; --bg: #fff; --tint: #fff8e1; }}
@media (prefers-color-scheme: dark) {{ :root {{ --ink: #f5f5f7; --muted: #a1a1a6; --line: #3a3a3c; --bg: #1c1c1e; --tint: #2c2615; }} }}
body {{ font: 16px/1.5 -apple-system, system-ui, sans-serif; color: var(--ink); background: var(--bg); max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }}
h1 {{ font-size: 1.6rem; margin-bottom: .2rem; }}
.lede {{ color: var(--muted); margin-top: 0; }}
section {{ border-top: 1px solid var(--line); padding: 1rem 0; }}
section.proposed {{ background: linear-gradient(90deg, var(--tint), transparent 60%); padding-left: .75rem; }}
h2 {{ font-size: 1.05rem; margin: 0 0 .3rem; }}
.kind {{ font-size: .75rem; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }}
.doc {{ font-family: ui-monospace, monospace; font-size: .9rem; }}
.meta, .src {{ color: var(--muted); font-size: .85rem; margin: .2rem 0; }}
blockquote {{ margin: .3rem 0 0; padding: .5rem .75rem; border-left: 3px solid var(--line); font-size: .85rem; color: var(--muted); }}
code {{ font-size: .8rem; }}
li {{ margin: .3rem 0; font-size: .9rem; }}
</style>
<h1>Citation rulings, tax year {Y}</h1>
<p class=lede>Generated by <code>tools/citations.py</code> from <code>reviews/{Y}/citations.json</code>. Each ruling lets
an anchor or quote pass the citation check although it cannot be matched as printed text on the cited page.
{len(rulings)} rulings: {proposed} proposed (awaiting the owner), {len(rulings) - proposed} accepted.</p>
{"".join(rows)}
</html>
"""
    RULINGS_PAGE.write_text(page, encoding="utf-8")


def _pages_text(pages):
    if len(pages) > 1 and pages == list(range(pages[0], pages[-1] + 1)):
        return f"{pages[0]}–{pages[-1]}"
    return ", ".join(map(str, pages))


# ---------- relocation ----------

def lead_key(layers, anchor, quotes):
    """The text that locates a segment: its first quote, or else the most specific
    form of its anchor printed anywhere in the document."""
    keys = [parts_of(q) for q in quotes if parts_of(q)]
    if keys:
        return keys[0]
    return next((k for k in anchor_keys(anchor) if pages_with(layers, k)), None)


FIRST, PRINTED, IN_FORCE_ONLY, ABSENT = 3, 2, 1, 0  # how an anchor stands on cited pages, strongest first


def anchor_level(layers, pages, anchor):
    """How the anchor stands on the pages: printed on the first, printed on another
    of them, only a heading in force (printed up to IN_FORCE pages before), absent."""
    def printed_on(p):
        return any(on_pages(layers, [p], k, spill=False) for k in anchor_keys(anchor))
    if printed_on(min(pages)):
        return FIRST
    if any(printed_on(p) for p in pages):
        return PRINTED
    return IN_FORCE_ONLY if anchor_on(layers, pages, anchor) else ABSENT


def passes(layers, pages, anchor, quotes):
    """Whether the check passes a segment's quotes and anchor on its pages (rulings
    aside); a segment with neither has nothing to pass."""
    keys = [parts_of(q) for q in quotes if parts_of(q)]
    if not keys and not anchor_keys(anchor):
        return False
    return all(on_pages(layers, pages, k, spill=True) for k in keys) and \
        (not anchor_keys(anchor) or anchor_on(layers, pages, anchor))


def place(layers, pages, anchor, quotes, shifts, level=PRINTED):
    """The pages a segment belongs on this year, or None to leave it for review.

    Each candidate shift (`shifts`, the
    shifts nearby evidence suggests) moves the old pages, and a move fits if every
    quote is on the moved pages and the anchor stands on them at least as strongly
    as it did on the authored pages (`level`, see anchor_level). A relocation may
    not weaken the evidence of the authored page: a heading printed on it must be
    printed on the new one, not only in force from a page before (nor, of a range,
    only on a later page of it). Exactly one distinct fitting placement is
    accepted; several (the heading printed on two candidate pages) are left for
    review. Without one, a segment citing one page goes to the page that alone
    prints its first quote, if the rest fits. A heading alone does not say how far
    past it the cited text lies, one quote does not say where a range of pages
    starts, and a segment with neither quote nor anchor has nothing to find: none
    of these is placed without a shift (the last not at all)."""
    keys = [parts_of(q) for q in quotes if parts_of(q)]
    has_anchor = bool(anchor_keys(anchor))
    if not keys and not has_anchor:
        return None

    def fits(moved, need=level):
        if min(moved) < 1 or not all(on_pages(layers, moved, k, spill=True) for k in keys):
            return False
        return not has_anchor or anchor_level(layers, moved, anchor) >= need

    found = []
    for s in shifts:
        moved = [p + s for p in pages]
        if moved not in found and fits(moved):
            found.append(moved)
    if found:
        return found[0] if len(found) == 1 else None
    hits = pages_with(layers, keys[0]) if keys and len(pages) == 1 else []
    return hits if len(hits) == 1 and fits(hits) else None


def local_shifts(evidence, page):
    """Candidate shifts for `page`: those among the (up to) five pieces of evidence
    nearest it, most common first (nearest first among equals), then those of the
    nearest evidence at or before it and at or after it, which bracket it when a
    page was inserted or removed in between; empty without evidence."""
    near = sorted(evidence, key=lambda e: (abs(e[0] - page), e[0]))[:5]
    out = [s for s, _ in collections.Counter(s for _, s in near).most_common()]
    before = [e for e in evidence if e[0] <= page]
    after = [e for e in evidence if e[0] >= page]
    for side in (max(before, default=None, key=lambda e: e[0]), min(after, default=None, key=lambda e: e[0])):
        if side is not None and side[1] not in out:
            out.append(side[1])
    return out


def collect():
    items = []
    for path in data_files():
        for doc, locator, line in citations(path):
            for seg in segments(doc, locator):
                items.append((path, line, locator, seg))
    return items


def plan(arch, items, offset=0, source=None, keep=False):
    """(item, old pages, new pages or None) for every segment on a PDF.

    `source` is the archive the locators were written against (the from-year's,
    after copying a year's definitions); None means `arch` itself, a year's own
    locators relocated again, which is done with `keep`: a segment the check passes
    stays, and shifts are learnt only from the segments that do not. `offset` (a
    number, or a function of the item) moves the old pages first, for the self-test.

    Shifts are learnt from segments citing one page whose first quote is printed
    on exactly one page: the old page held it, so the difference is the shift.
    (An anchor proves less: the heading in force may be printed a page or two
    before the cited one.) A document with no such evidence takes the shift of
    the draft cover page, when one of the two archives prints it and the other
    does not. How each anchor stood on its authored pages (anchor_level) is read
    from `source`; when that is unknown (with `keep`, or the anchor not found) the
    anchor must be printed on the new pages."""
    source = source or arch
    move = offset if callable(offset) else (lambda _item: offset)
    rows, result = [], {}
    for item in items:
        _, _, _, (d, pages, anchor, quotes, span) = item
        layers = arch.pages(d)
        if layers is None or span is None:
            continue
        old = [p + move(item) for p in pages]
        if min(old) < 1:
            continue
        i = len(rows)
        lead = parts_of(quotes[0]) if quotes and len(old) == 1 else None
        hits = pages_with(layers, lead) if lead else []
        rows.append((item, old, layers, (old[0], hits[0] - old[0]) if len(hits) == 1 else None))
        if keep and passes(layers, old, anchor, quotes):
            result[i] = old  # passes the check where it is
    had_evidence = {r[0][3][0] for i, r in enumerate(rows) if r[3] and i not in result}

    # Segments the nearby evidence cannot place are tried again with the shifts of the
    # other segments still unplaced (a block of pages that moved by its own amount),
    # until a round places nothing more; so relocating the result again changes nothing.
    while True:
        pending = [i for i in range(len(rows)) if i not in result]
        evidence = collections.defaultdict(list)
        for i in pending:
            if rows[i][3]:
                evidence[rows[i][0][3][0]].append(rows[i][3])
        placed = {}
        for i in pending:
            item, old, layers, _ = rows[i]
            d, authored, anchor, quotes, _ = item[3]
            shifts = local_shifts(evidence[d], min(old))
            if d not in had_evidence and source is not arch and arch.has_cover(d) != source.has_cover(d):
                shifts = [int(arch.has_cover(d)) - int(source.has_cover(d))]
            elif shifts and not any(parts_of(q) for q in quotes) and not (
                    any(p <= min(old) for p, _ in evidence[d]) and any(p >= min(old) for p, _ in evidence[d])):
                # Only a heading, beyond the evidence on one side: a page may have been added
                # or removed between, so a heading printed on the neighbouring pages too
                # places nothing.
                shifts = shifts + [s + k for s in shifts[:1] for k in (-1, 1) if s + k not in shifts]
            level = PRINTED
            src_layers = source.pages(d)
            if not keep and src_layers is not None and anchor_keys(anchor):
                level = anchor_level(src_layers, authored, anchor) or PRINTED
            new = place(layers, old, anchor, quotes, shifts, level)
            if new is not None:
                placed[i] = new
        if not placed:
            break
        result.update(placed)
    return [(item, old, result.get(i)) for i, (item, old, _, _) in enumerate(rows)]


def _report_plan(name, planned):
    """Print how many planned segments came back to their authored pages; 1 if any went elsewhere."""
    back = [p for p in planned if p[2] == p[0][3][1]]
    wrong = [p for p in planned if p[2] is not None and p[2] != p[0][3][1]]
    none = [p for p in planned if p[2] is None]
    print(f"self-test, {name}: {len(back)} of {len(planned)} segments relocated to their "
          f"authored pages, {len(wrong)} elsewhere, {len(none)} not placed")
    for (path, line, _, (d, pages, anchor, _, _)), old, new in wrong:
        print(f"  WRONG {rel(path)}:{line} {d} authored p. {_pages_text(pages)}, relocated p. {_pages_text(new)} ({anchor})")
    return 1 if wrong else 0


def _unique_lead(arch, item):
    """Whether a segment cites one page and its first quote is printed on exactly one page (shift evidence)."""
    d, pages, _, quotes, _ = item[3]
    layers = arch.pages(d)
    lead = parts_of(quotes[0]) if quotes and len(pages) == 1 else None
    return bool(layers and lead and len(pages_with(layers, lead)) == 1)


def self_test():
    arch, items = Archive(), collect()
    # The authored pages are the answer only where the check passes them (all of them in an
    # adopted year; a year just copied holds segments left for review on old pages).
    passing = [it for it in items if arch.pages(it[3][0]) is not None and it[3][4] is not None
               and passes(arch.pages(it[3][0]), *it[3][1:4])]
    if len(passing) < len(items):
        print(f"self-test: {len(passing)} segments the check passes where they stand are relocated")
    items = passing
    status = 0
    for offset in (2, -1):
        status = _report_plan(f"every page moved by {offset:+d}", plan(arch, items, offset)) or status

    # A page inserted mid-document (with the draft cover, as in the TY2026 Schedule C
    # instructions): pages before the middle moved by 1, from the middle on by 2. The
    # evidence near the middle mixes the two shifts; a segment whose heading is printed
    # on its authored page must not be put on the next page, where it is only in force.
    def inserted(item):
        d, pages = item[3][0], item[3][1]
        return 1 if min(pages) <= len(arch.pages(d)[0]) // 2 else 2
    status = _report_plan("a page inserted mid-document (+1, then +2)", plan(arch, items, inserted)) or status

    # Relocating again (--relocate without --from): half of the segments that teach a
    # shift are stale, a page early, as segments left for review after a first run are;
    # the rest, already right, must stay where they are.
    stale = {id(it) for it in [it for it in items if _unique_lead(arch, it) and min(it[3][1]) > 1][::2]}
    planned = plan(arch, items, lambda it: -1 if id(it) in stale else 0, keep=True)
    status = _report_plan("relocated again, half the evidence a page early", planned) or status

    computed, rewrite, cover = self_test_computed(arch), self_test_rewrite(), self_test_cover(arch, items)
    quotes = self_test_input_quotes(arch)
    return status or computed or rewrite or cover or quotes


COVER_TEST_DOC = "f4952"  # cited on several pages at once, by no single-page quote: no shift evidence


def self_test_cover(arch, items):
    """A document with no shift evidence, archived again as an IRS draft with its
    cover page added: every segment the check passes must move by one page."""
    import tempfile
    doc = COVER_TEST_DOC
    mine = [it for it in items if it[3][0] == doc]
    d = arch.docs.get(doc)
    if not mine or not d or any(_unique_lead(arch, it) for it in mine):
        print(f"self-test, a draft cover page added: {doc} is not cited without shift evidence this year; skipped")
        return 0
    layers = arch.pages(doc)
    passing = [it for it in mine if anchor_on(layers, it[3][1], it[3][2])
               and all(on_pages(layers, it[3][1], parts_of(q), spill=True) for q in it[3][3] if parts_of(q))]
    with tempfile.TemporaryDirectory() as tmp:
        entries = {}
        for name, draft in (("old", False), ("new", True)):
            (Path(tmp) / name).mkdir()
            entry = {**d, "draft": draft}
            for key in ("cols_file", "text_file"):
                if key in d:
                    raw = (arch.sources / d[key]).read_text(encoding="utf-8")
                    if draft:
                        raw = f"Caution: DRAFT—NOT FOR FILING\n{DRAFT_COVER}.\f" + raw
                    (Path(tmp) / name / d[key]).write_text(raw, encoding="utf-8")
            entries[name] = entry
            (Path(tmp) / name / "manifest.json").write_text(json.dumps({"documents": [entry]}))
        old, new = Archive(sources=Path(tmp) / "old"), Archive(sources=Path(tmp) / "new")
        planned = plan(new, passing, source=old)
    moved = [p for p in planned if p[2] == [q + 1 for q in p[0][3][1]]]
    print(f"self-test, a draft cover page added to {doc}: {len(moved)} of {len(planned)} passing segments moved by one page")
    for (path, line, _, (_, pages, anchor, _, _)), _, new in planned:
        if new != [q + 1 for q in pages]:
            print(f"  WRONG {rel(path)}:{line} {doc} authored p. {_pages_text(pages)}, relocated "
                  f"{'nowhere' if new is None else 'p. ' + _pages_text(new)} ({anchor})")
    return 0 if planned and len(moved) == len(planned) else 1


def self_test_computed(arch):
    """Plant locators on a computed line of Form 8959: the span must be reported,
    the form-line locator of the line's own number must verify, and one naming
    a line whose label is another's must not."""
    label = "Add lines 1 through 3"
    planted = [("span", "Form 8959 (2025), lines 1–24", True),
               ("form line", "Form 8959 (2025), line 4", False),
               ("wrong line", "Form 8959 (2025), line 7", True),
               ("title", "Form 8959 (2025)", True),
               ("quote", 'Form 8959 (2025), line 4, "Add lines 1 through 3"', False)]
    bad = []
    for name, locator, expect_finding in planted:
        _, found = check_computed(arch, [(ROOT / "self-test", "f8959", "f8959.line4", label, "f8959", locator, 0)])
        if bool(found) != expect_finding:
            bad.append(f"  WRONG planted {name} locator “{locator}” {'reported' if found else 'passed'}")
    print(f"self-test, planted computed-line locators: {len(planted) - len(bad)} of {len(planted)} behaved")
    for b in bad:
        print(b)
    return 1 if bad else 0


def self_test_input_quotes(arch):
    """Plant an input line citing a quote of Form 8959 as printed and one misquoted (in a locator and in a
    `quote` key); only the misquotes are unmatched, and the baseline entry of a misquote comes due when its
    own line changes."""
    import baseline_check
    printed = "Add lines 1 through 3"
    text = lambda quote, extra="": (
        "form:\n  id: f8959\n  lines:\n"
        "    - id: f8959.x\n      expr: {op: input, source: x}\n      cite:\n        doc: f8959\n"
        f"        locator: 'Line 4, \"{quote}\"'{extra}\n")
    run = lambda t: check_input_quotes(arch, quote_sites(io.StringIO(t), "self-test.yaml"))[1]
    miss = "Add lines 1 through 9 and halve"
    bad = []
    if run(text(printed)):
        bad.append("  WRONG a quote as printed was reported")
    wrong = run(text(miss))
    if len(wrong) != 1:
        bad.append("  WRONG a misquoted input line was not reported")
    if len(run(text(printed, f"\n        quote: '{miss}'"))) != 1:
        bad.append("  WRONG a misquoted `quote` key was not reported")
    moved = run(text(miss) + "      label: new\n")
    if wrong and (not moved or baseline_check.subject_hash(moved[0], {}) == baseline_check.subject_hash(wrong[0], {})):
        bad.append("  WRONG a baseline entry did not come due when its line changed")
    print(f"self-test, planted input-line quotes: {4 - len(bad)} of 4 behaved")
    for b in bad:
        print(b)
    return 1 if bad else 0


def relocate(from_year=None):
    """Relocate the year's locators: written for `from_year`'s archive (just copied
    from that year), or else for this year's own (run again: a segment the check
    passes is kept)."""
    arch, items = Archive(), collect()
    if from_year is not None and str(from_year) != str(Y):
        planned = plan(arch, items, source=Archive(from_year))
    else:
        planned = plan(arch, items, keep=True)
    edits = collections.defaultdict(list)
    kept, moved, unplaced = 0, [], []
    for (path, line, locator, (d, pages, anchor, quotes, span)), old, new in planned:
        if new is None:
            # one left for review whose unchanged pages the check passes will not be reported by the check
            unplaced.append((rel(path), line, d, pages, anchor, passes(arch.pages(d), pages, anchor, quotes)))
        elif new == pages:
            kept += 1
        else:
            moved.append((rel(path), line, d, pages, new, anchor))
            edits[path].append((line, locator, span, new))
    for path, changes in edits.items():
        _rewrite(path, changes)
    summary = f"relocate {Y}: {len(planned)} segments; {kept} in place, {len(moved)} moved, {len(unplaced)} not placed"
    out = [summary] + [f"  moved {path}:{line} {d} p. {_pages_text(pages)} -> p. {_pages_text(new)}: {anchor}"
                       for path, line, d, pages, new, anchor in moved]
    out += [f"  REVIEW {path}:{line} {d} p. {_pages_text(pages)}: {anchor}"
            + (" (the check passes it unmoved)" if unmoved_ok else "")
            for path, line, d, pages, anchor, unmoved_ok in unplaced]
    print("\n".join(out))
    if from_year is not None and str(from_year) != str(Y):
        report = ROOT / "reports" / Y / f"relocation_from_{from_year}.md"
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text("\n".join([
            f"# Citation pages relocated from {from_year} to {Y}", "",
            f"Generated by `tools/citations.py --relocate --from {from_year}` when the {from_year} definitions were "
            f"copied to {Y}. Each segment left for review still names its {from_year} pages. Those marked “the "
            "check passes it unmoved” also pass the citation check as they stand, so only this list shows them.",
            "", "```"] + out + ["```", ""]), encoding="utf-8")
        print(f"report: {report.relative_to(ROOT)}")
    return 0


def _scalar_offsets(raw, value, style):
    """Positions in `raw` (a locator scalar as written in the file, quotes included)
    of each character offset of its parsed `value` (one more for the end), or None
    when the two cannot be walked together (an escape sequence, say)."""
    j = 1 if style in ("'", '"') else 0
    pos, i = [], 0
    while i < len(value):
        c = value[i]
        if c.isspace():
            if j >= len(raw) or not raw[j].isspace():
                return None
            while i < len(value) and value[i].isspace():
                pos.append(j)
                i += 1
            while j < len(raw) and raw[j].isspace():
                j += 1
            continue
        if style == '"' and raw[j:j + 1] == "\\":
            return None
        if style == "'" and c == "'":
            if raw[j:j + 2] != "''":
                return None
            pos.append(j)
            i, j = i + 1, j + 2
            continue
        if raw[j:j + 1] != c:
            return None
        pos.append(j)
        i, j = i + 1, j + 1
    return pos + [j]


def _rewrite(path, changes):
    """Replace each segment's page list in the file, keeping its separator style. The
    locator scalar is found by its line, its parsed text walked against the text as
    written (folded over rows, quotes doubled) so that each page list is replaced at
    its own offset; the edits of one locator are applied last to first."""
    text = open(path, encoding="utf-8").read()
    scalars = {}
    def walk(node):
        if isinstance(node, yaml.MappingNode):
            for k, v in node.value:
                if isinstance(k, yaml.ScalarNode) and k.value == "locator" and isinstance(v, yaml.ScalarNode):
                    scalars[v.start_mark.line + 1] = v
                walk(v)
        elif isinstance(node, yaml.SequenceNode):
            for v in node.value:
                walk(v)
    walk(yaml.compose(text))
    by_line = collections.defaultdict(list)
    for line, locator, span, new in changes:
        by_line[line].append((locator, span, new))
    edits = []
    for line, group in by_line.items():
        node = scalars.get(line)
        pos = None
        if node is not None and node.value == group[0][0]:
            raw = text[node.start_mark.index:node.end_mark.index]
            pos = _scalar_offsets(raw, node.value, node.style)
        if pos is None:
            print(f"  could not rewrite {rel(path)}:{line}; edit by hand", file=sys.stderr)
            continue
        for locator, (a, b), new in group:
            old_text = locator[a:b]
            dash = next((c for c in "\u2013\u2014-" if c in old_text), "\u2013")
            edits.append((node.start_mark.index + pos[a], node.start_mark.index + pos[b],
                          _pages_text(new).replace("\u2013", dash)))
    for i, j, new_text in sorted(edits, reverse=True):
        text = text[:i] + new_text + text[j:]
    open(path, "w", encoding="utf-8").write(text)


def self_test_rewrite():
    """Two page lists of one locator folded over rows, each moved by one, the second
    old number equal to the first new one; and a quote doubled in a single-quoted
    scalar before the page list. Both must be rewritten at their own places."""
    import tempfile
    body = ("a:\n  cite:\n    doc: x\n    locator: 'Form X (2026), line 7, \"stop\"; p. 1, Caution; p. 2, Credit Limit\n"
            "      Worksheet, \"you can\u2019t\"; p. 3\u20134, Line\n      7'\n"
            "b:\n  cite:\n    doc: x\n    locator: 'p. 5, Who''s Eligible; p. 6, Lines 1 and 2'\n")
    want = ("a:\n  cite:\n    doc: x\n    locator: 'Form X (2026), line 7, \"stop\"; p. 2, Caution; p. 3, Credit Limit\n"
            "      Worksheet, \"you can\u2019t\"; p. 4\u20135, Line\n      7'\n"
            "b:\n  cite:\n    doc: x\n    locator: 'p. 6, Who''s Eligible; p. 8, Lines 1 and 2'\n")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "t.yaml"
        path.write_text(body, encoding="utf-8")
        changes = []
        for _, locator, line in citations(path):
            for _, pages, _, _, span in segments("x", locator):
                changes.append((line, locator, span, [p + (2 if p == 6 else 1) for p in pages]))
        _rewrite(path, changes)
        got = path.read_text(encoding="utf-8")
    ok = got == want
    print("self-test, rewriting folded multi-segment locators: " + ("correct" if ok else "WRONG:\n" + got))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--relocate", action="store_true")
    ap.add_argument("--from", dest="from_year", type=int,
                    help="with --relocate: the year whose archive the locators were written for (default: this year's)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true", help="fail on computed-line locators to rewrite and on new unmatched input quotes, not only report them")
    ap.add_argument("--rebaseline-input-quotes", action="store_true",
                    help="record the current unmatched input quotes as the baseline (reviews/<year>/input_quotes.json)")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if a.relocate:
        return relocate(a.from_year)
    status = check(strict=a.strict)
    return input_quotes(a.strict, a.rebaseline_input_quotes) or status


if __name__ == "__main__":
    sys.exit(main())
