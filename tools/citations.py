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

  --relocate
      for a year whose locators were carried over from an earlier year, find
      each segment's quotes (or else its anchor) in this year's archived text
      and rewrite the segment's page numbers in place where they moved; a
      segment that cannot be placed on one page range is listed for review.
      The rewrite is an ordinary diff to read before committing.

  --self-test (in check-all)
      move every page number of this year's (checked) locators by +2, then by
      -1, relocate, and report how many come back to the authored pages; exits
      1 if any is placed on a page other than its authored one (a segment left
      for review is not a failure). Then plant locators on a computed line: a
      span of lines must be reported and a correct form-line locator must
      verify; exits 1 otherwise.
"""

import argparse
import collections
import glob
import html
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

RULINGS = ROOT / "reviews" / Y / "citations.json"
REPORT = ROOT / "reports" / Y / "citations.md"
RULINGS_PAGE = ROOT / "reports" / Y / "citations.html"

PAGES_RE = r"(\d+(?:\s*[–—-]\s*\d+)?(?:(?:,\s*|\s+and\s+)\d+(?:\s*[–—-]\s*\d+)?)*)"
SEGMENT_RE = re.compile(r"^(?:(?P<doc>[a-z][a-z0-9-]*)\s+)?(?P<pp>pp?\.)\s*" + PAGES_RE + r"(?P<rest>.*)$", re.S)


# ---------- text ----------

def norm(text):
    text = unicodedata.normalize("NFKC", text).replace("­", "")
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
    def __init__(self, year=Y, sources=None):
        self.sources = Path(sources) if sources else ROOT / "sources" / str(year)
        docs = json.loads((self.sources / "manifest.json").read_text())["documents"]
        self.docs = {d["id"]: d for d in docs}
        self.cache = {}

    def pages(self, doc):
        """Normalized pages of a PDF's two text layers (reading order, layout), or None."""
        if doc not in self.cache:
            d = self.docs.get(doc)
            layers = []
            if d and d["file"].endswith(".pdf"):
                for key in ("cols_file", "text_file"):
                    if key in d:
                        pages = (self.sources / d[key]).read_text(encoding="utf-8").split("\f")
                        layers.append([norm(p) for p in pages])
            self.cache[doc] = layers or None
        return self.cache[doc]

    def raw_page(self, doc, page):
        """One page of a PDF's reading-order text, as extracted."""
        d = self.docs[doc]
        pages = (self.sources / d.get("cols_file", d["text_file"])).read_text(encoding="utf-8").split("\f")
        return pages[page - 1] if 0 < page <= len(pages) else ""

    def _raw_layers(self, doc):
        d = self.docs.get(doc)
        if not d:
            return []
        return [(self.sources / d[key]).read_text(encoding="utf-8")
                for key in ("cols_file", "text_file") if key in d]

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


def place(layers, pages, anchor, quotes, shift):
    """The pages a segment belongs on this year, or None to leave it for review:
    the old pages moved by the local shift, if every quote and the anchor fit
    there; otherwise, for a segment citing one page, the page that alone prints
    its first quote, if the rest fits. A heading alone does not say how far past
    it the cited text lies, one quote does not say where a range of pages starts,
    and a segment with neither quote nor anchor has nothing to find: none of these
    is placed without the shift (the last not at all)."""
    keys = [parts_of(q) for q in quotes if parts_of(q)]
    has_anchor = bool(anchor_keys(anchor))
    if not keys and not has_anchor:
        return None

    def fits(moved):
        return min(moved) >= 1 and all(on_pages(layers, moved, k, spill=True) for k in keys) and \
            (not has_anchor or anchor_on(layers, moved, anchor))

    if shift is not None and fits([p + shift for p in pages]):
        return [p + shift for p in pages]
    hits = pages_with(layers, keys[0]) if keys and len(pages) == 1 else []
    return hits if len(hits) == 1 and fits(hits) else None


def local_shift(evidence, page):
    """The shift most common among the (up to) five pieces of evidence nearest
    `page`, or None without evidence."""
    if not evidence:
        return None
    near = sorted(evidence, key=lambda e: (abs(e[0] - page), e[0]))[:5]
    return collections.Counter(s for _, s in near).most_common(1)[0][0]


def collect():
    items = []
    for path in data_files():
        for doc, locator, line in citations(path):
            for seg in segments(doc, locator):
                items.append((path, line, locator, seg))
    return items


def plan(arch, items, offset=0):
    """(item, old pages, new pages or None) for every segment on a PDF; `offset`
    moves every old page first (the self-test). Shifts are learnt from segments
    citing one page whose first quote is printed on exactly one page: the old
    page held it, so the difference is the shift. (An anchor proves less: the
    heading in force may be printed a page or two before the cited one.)"""
    evidence = collections.defaultdict(list)
    rows = []
    for item in items:
        _, _, _, (d, pages, anchor, quotes, span) = item
        layers = arch.pages(d)
        if layers is None or span is None:
            continue
        old = [p + offset for p in pages]
        if min(old) < 1:
            continue
        rows.append((item, old, layers))
        lead = parts_of(quotes[0]) if quotes and len(old) == 1 else None
        if lead:
            hits = pages_with(layers, lead)
            if len(hits) == 1:
                evidence[d].append((old[0], hits[0] - old[0]))
    out = []
    for item, old, layers in rows:
        d, _, anchor, quotes, _ = item[3]
        out.append((item, old, place(layers, old, anchor, quotes, local_shift(evidence[d], min(old)))))
    return out


def self_test():
    arch, items = Archive(), collect()
    status = 0
    for offset in (2, -1):
        planned = plan(arch, items, offset)
        back = [(it, old, new) for it, old, new in planned if new == it[3][1]]
        wrong = [(it, old, new) for it, old, new in planned if new is not None and new != it[3][1]]
        none = [(it, old, new) for it, old, new in planned if new is None]
        print(f"self-test, every page moved by {offset:+d}: {len(back)} of {len(planned)} segments relocated to their "
              f"authored pages, {len(wrong)} elsewhere, {len(none)} not placed")
        for (path, line, _, (d, pages, anchor, _, _)), old, new in wrong:
            print(f"  WRONG {rel(path)}:{line} {d} authored p. {_pages_text(pages)}, relocated p. {_pages_text(new)} ({anchor})")
        status = status or (1 if wrong else 0)
    return status or self_test_computed(arch)


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


def relocate():
    arch, items = Archive(), collect()
    planned = plan(arch, items)
    edits = collections.defaultdict(list)
    kept, moved, unplaced = 0, [], []
    for (path, line, locator, (d, pages, anchor, _, span)), old, new in planned:
        if new is None:
            unplaced.append((rel(path), line, d, pages, anchor))
        elif new == pages:
            kept += 1
        else:
            moved.append((rel(path), line, d, pages, new, anchor))
            edits[path].append((line, locator, span, new))
    for path, changes in edits.items():
        _rewrite(path, changes)
    print(f"relocate {Y}: {len(planned)} segments; {kept} in place, {len(moved)} moved, {len(unplaced)} not placed")
    for path, line, d, pages, new, anchor in moved:
        print(f"  moved {path}:{line} {d} p. {_pages_text(pages)} -> p. {_pages_text(new)}: {anchor}")
    for path, line, d, pages, anchor in unplaced:
        print(f"  REVIEW {path}:{line} {d} p. {_pages_text(pages)}: {anchor}")
    return 0


def _rewrite(path, changes):
    """Replace each segment's page list in the file, keeping its separator style."""
    lines = open(path, encoding="utf-8").read().split("\n")
    for line, locator, (a, b), new in changes:
        old_text = locator[a:b]
        dash = next((c for c in "\u2013\u2014-" if c in old_text), "\u2013")
        new_text = _pages_text(new).replace("\u2013", dash)
        tail = locator[max(0, a - 20):a]
        # the locator may be folded over several rows of the file; find the row holding this page list
        for row_no in range(line - 1, min(len(lines), line + 6)):
            row = lines[row_no]
            idx = row.find(tail + old_text) if row_no == line - 1 else row.find(old_text)
            if idx >= 0:
                k = idx + (len(tail) if row_no == line - 1 else 0)
                lines[row_no] = row[:k] + new_text + row[k + len(old_text):]
                break
        else:
            print(f"  could not rewrite {rel(path)}:{line}; edit by hand", file=sys.stderr)
    open(path, "w", encoding="utf-8").write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--relocate", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true", help="fail on computed-line locators to rewrite, not only report them")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if a.relocate:
        return relocate()
    return check(strict=a.strict)


if __name__ == "__main__":
    sys.exit(main())
