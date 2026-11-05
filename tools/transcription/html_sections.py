"""Sections of an archived web edition, cut by its headings, for a review request.

A web edition is archived as one page, so a request citing it would otherwise carry the whole text.
Its citations name a heading instead of a page ('New York State tax rate schedule, "If line 38 is:"';
'Tax computation worksheet 2, "4. Recapture Base amount"'), so the request is given the sections those
headings open. The headings are read from the archived HTML (h1 to h6 and table captions) and placed on
the lines of the archived text (`<id>.txt`, the search aid tools/fetch_sources.py derives from the
HTML); the text is used only when the HTML hashes to its manifest entry and re-derives to that text
exactly.

For one locator:
  heading   the longest heading the locator's head (its text before the first `, "`) equals or
            begins, at a word boundary ("Tax computation worksheet 1" is not worksheet 10); every
            heading with that title;
  section   from the heading's line to the line before the next heading of the same or a higher
            rank (a caption, the lowest, ends at the next heading of any rank);
  widening  while a phrase the locator quotes is not in the section, the section of the enclosing
            heading instead;
  context   each enclosing heading's own line and the lead text under it, up to its first
            sub-heading (the filing status a worksheet is for, a rule that introduces its tables).
A locator of several segments (`;`) is cut segment by segment. A segment naming no heading, a quote found nowhere under any heading, or text that does not re-derive,
gives the whole document, as before.

Only the documents in SECTIONED are cut; every other document's pages are given as before.
"""
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fetch_sources import ReadableHTML  # noqa: E402

# The IT-201-I web edition: cited only by heading (its tables and worksheets, which the PDF edition's
# text layers do not keep in order; sources/ny/<year>/README.md).
SECTIONED = frozenset({"ny_it201i-html"})

RANKS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6, "caption": 7}
_OPEN, _CLOSE = "", ""


class _Marked(ReadableHTML):
    """ReadableHTML with a mark where each heading starts, and the heading's text."""

    def __init__(self):
        super().__init__()
        self.headings = []          # [rank, title]
        self._open = []

    def handle_starttag(self, tag, attrs):
        super().handle_starttag(tag, attrs)
        if tag in RANKS and not self.hidden:
            self.parts.append(f"{_OPEN}{len(self.headings)}{_CLOSE}")
            self.headings.append([RANKS[tag], ""])
            self._open.append((tag, len(self.headings) - 1))

    def handle_endtag(self, tag):
        if self._open and self._open[-1][0] == tag:
            self._open.pop()
        super().handle_endtag(tag)

    def handle_data(self, data):
        super().handle_data(data)
        if not self.hidden:
            for _, i in self._open:
                self.headings[i][1] += data


_MARK = re.compile(_OPEN + r"(\d+)" + _CLOSE)


def outline(html, text):
    """[(rank, title, line index)] of the headings, in order, placed on `text`'s lines; None when the
    HTML does not re-derive to `text` exactly."""
    parser = _Marked()
    parser.feed(html)
    raw = "".join(parser.parts).splitlines()
    lines, pending, placed = [], [], {}
    for line in raw:
        marks = [int(m) for m in _MARK.findall(line)]
        plain = " ".join(_MARK.sub("", line).split())
        if not plain:
            pending += marks
            continue
        for i in pending + marks:
            placed[i] = len(lines)
        pending = []
        lines.append(plain)
    if "\n".join(lines) + "\n" != text:
        return None
    out = []
    for i, (rank, title) in enumerate(parser.headings):
        title = " ".join(title.split())
        if title and i in placed:
            out.append((rank, title, placed[i]))
    return out


def _norm(s):
    return " ".join(s.replace("|", " ").split())


def segments(locator):
    """A locator's segments: its parts between top-level semicolons (outside quotes)."""
    out, cur, quoted = [], "", False
    for c in locator:
        if c == '"':
            quoted = not quoted
        if c == ";" and not quoted:
            out.append(cur.strip()); cur = ""
        else:
            cur += c
    return [s for s in out + [cur.strip()] if s]


def _head(locator):
    return locator.split(', "', 1)[0].strip()


def _matches(head, title):
    return title == head or (title.startswith(head) and not title[len(head)].isalnum())


class Sections:
    def __init__(self, heads, lines):
        self.heads, self.lines = heads, lines

    def end(self, k):
        """The line after heading k's section."""
        rank = self.heads[k][0]
        for j in range(k + 1, len(self.heads)):
            r = self.heads[j][0]
            if r <= rank or rank == RANKS["caption"]:
                return self.heads[j][2]
        return len(self.lines)

    def parent(self, k):
        rank = self.heads[k][0]
        for j in range(k - 1, -1, -1):
            if self.heads[j][0] < rank:
                return j
        return None

    def text(self, a, b):
        return _norm(" ".join(self.lines[a:b]))

    def lead(self, k):
        """Heading k's line and the text under it up to its first sub-heading."""
        start = self.heads[k][2]
        stop = self.heads[k + 1][2] if k + 1 < len(self.heads) else len(self.lines)
        return start, max(start + 1, min(stop, self.end(k)))

    def select(self, locator):
        """([(start, end)] line ranges given, [section titles], [(start, end)] of the sections alone,
        without their context) for one locator, or None (no heading named; a quote not found)."""
        head = _head(locator)
        hits = [k for k, (_, t, _) in enumerate(self.heads) if _matches(head, t) or _matches(t, head)]
        if not hits:
            return None
        best = max(len(self.heads[k][1]) for k in hits)
        hits = [k for k in hits if len(self.heads[k][1]) == best]
        quotes = [_norm(q) for q in re.findall(r'"([^"]+)"', locator)]
        ranges, titles, own = [], [], []
        for k in hits:
            j = k
            while j is not None and not all(q in self.text(self.heads[j][2], self.end(j)) for q in quotes):
                j = self.parent(j)
            if j is None:
                continue
            ranges.append((self.heads[j][2], self.end(j)))
            own.append((self.heads[j][2], self.end(j)))
            titles.append(self.heads[j][1])
            p = self.parent(j)
            while p is not None:
                ranges.append(self.lead(p))
                p = self.parent(p)
        return (ranges, titles, own) if ranges else None


def merge(ranges):
    out = []
    for a, b in sorted(ranges):
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return [tuple(r) for r in out]


_CACHE = {}


def load(source_dir, entry, text):
    """The Sections of a manifest entry, or None when its HTML is not the archived one or does not
    re-derive to `text`."""
    path = Path(source_dir) / entry["file"]
    key = (str(path), entry.get("sha256"), hashlib.sha256(text.encode()).hexdigest())
    if key not in _CACHE:
        data = path.read_bytes()
        heads = None
        if hashlib.sha256(data).hexdigest() == entry.get("sha256"):
            heads = outline(data.decode("utf-8"), text)
        _CACHE[key] = Sections(heads, text.splitlines()) if heads else None
    return _CACHE[key]


def cut(source_dir, entry, text, locators):
    """(excerpt text, section titles, [(start, end)] line ranges of the sections without their context)
    of the sections the locators name, or None for the whole document."""
    secs = load(source_dir, entry, text)
    if secs is None or not locators:
        return None
    ranges, titles, own = [], [], []
    for seg in sorted({seg for loc in locators for seg in segments(loc)}):
        got = secs.select(seg)
        if got is None:
            return None
        ranges += got[0]
        own += got[2]
        titles += [t for t in got[1] if t not in titles]
    parts = [f"----- lines {a + 1}–{b} of {len(secs.lines)} -----\n" + "\n".join(secs.lines[a:b])
             for a, b in merge(ranges)]
    return "\n".join(parts), sorted(titles), merge(own)
