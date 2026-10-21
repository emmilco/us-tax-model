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
      reported. Writes
      reports/<year>/citations.md; exits 1 on any unruled finding.

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
      for review is not a failure).
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

SOURCES = ROOT / "sources" / Y
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
    def __init__(self):
        docs = json.loads((SOURCES / "manifest.json").read_text())["documents"]
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
                        pages = (SOURCES / d[key]).read_text(encoding="utf-8").split("\f")
                        layers.append([norm(p) for p in pages])
            self.cache[doc] = layers or None
        return self.cache[doc]

    def raw_page(self, doc, page):
        """One page of a PDF's reading-order text, as extracted."""
        d = self.docs[doc]
        pages = (SOURCES / d.get("cols_file", d["text_file"])).read_text(encoding="utf-8").split("\f")
        return pages[page - 1] if 0 < page <= len(pages) else ""


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

def data_files():
    files = sorted(glob.glob(str(ROOT / "forms" / Y / "*.yaml"))) + sorted(glob.glob(str(ROOT / "tables" / Y / "*.yaml")))
    files += [str(ROOT / "params" / f"{Y}.yaml"), str(ROOT / "ambiguities" / f"{Y}.yaml")]
    files += sorted(f for f in glob.glob(str(ROOT / "interview" / "*.yaml")) if re.search(rf"(^|-){Y}\.yaml$", os.path.basename(f)))
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


def rel(path):
    return os.path.relpath(path, ROOT)


# ---------- check ----------

def load_rulings():
    if not RULINGS.exists():
        return {}
    data = json.loads(RULINGS.read_text())
    return {("anchor", r["doc"], r["anchor"]): r for r in data.get("anchors", [])} | \
        {("quote", r["doc"], r["quote"]): r for r in data.get("quotes", [])}


def check():
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
    out = [f"# Citation pages, tax year {Y}", "",
           "Generated by `tools/citations.py`: every quote in a page locator must appear on the cited pages",
           "(it may run on to the next page), and the locator's anchor, its first phrase after the pages (of a",
           "compound anchor, its first member), on one of them or as a heading in force up to two pages before.",
           f"An anchor or quote that cannot match printed text carries a ruling in `reviews/{Y}/citations.json`,",
           f"listed with its uses in `reports/{Y}/citations.html`.", ""]
    out += [f"- {k}: {v}" for k, v in sorted(counts.items())]
    out += [f"- findings without a ruling: {len(findings)}", f"- rulings no anchor uses: {len(unused)}", ""]
    if findings:
        out += ["## Findings", ""]
        for path, line, doc, pages, kind, text, found in findings:
            where = f"found on p. {', '.join(map(str, found[:8]))}" if found else "not found in the document"
            out.append(f"- `{path}:{line}` {doc} p. {_pages_text(pages)}, {kind} “{text}”: {where}")
        out.append("")
    if unused:
        out += ["## Unused rulings", ""] + [f"- {k} {d}: “{a}”" for k, d, a in unused] + [""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(out))
    write_rulings_page(arch, rulings, uses)
    print(f"citations: {counts['segments checked']} segments, {counts['quotes']} quotes, {counts['anchors']} anchors "
          f"({counts['quotes ruled']} and {counts['anchors ruled']} ruled); {len(findings)} finding(s), {len(unused)} unused ruling(s)")
    print(f"report: reports/{Y}/citations.md")
    return 1 if findings or unused else 0


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
    return status


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
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if a.relocate:
        return relocate()
    return check()


if __name__ == "__main__":
    sys.exit(main())
