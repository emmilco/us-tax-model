#!/usr/bin/env python3
"""Propose a tax year's parameter values from its archived documents.

    propose_params.py --from 2025 --to 2026 [--write] [--compare FILE]
    propose_params.py --from 2026 --to 2025 --params FILE --compare params/2025.yaml
    propose_params.py --self-test                (in check-all)

For every parameter of the from-year's parameter file (params/<from>.yaml, or `--params
FILE` in that format, its citations written against the from-year's archive), the tool
reads the amount from the to-year's edition of the cited document at the place the
citation names. A document whose id changes from year to year (a revenue procedure)
is followed by "next" in the earlier year's catalog (tools/sources/<year>.json).

The places read. Each quote of the citation (in the locator, or the cite's own `quote`)
that prints the value is a place. When the quotes do not print every amount of the
value, and the value is an amount or a percentage, every figure on the cited pages (on
a segment with no pages, anywhere in the document) that prints it is a place too.
Counts and fractions are read only from a quote that prints them as a number.

A text is read as a pattern: its words as printed, punctuation between them optional,
each figure (an amount, a percentage, a decimal rate) a slot, each year moved by the
difference of the tax years, line, column, box, part, step and section numbers and bare
item numbers free (forms are renumbered, so a number is never evidence of the place), an
omission (`...`) a gap of at most 400 characters. The slots that print the value (for a
value per filing status, each status's amount) give the to-year value; a count or 1/N
is a bare number in its slot. A text must print at least three words besides its figures.

The text read at a place is the quote itself when it reads the from-year value, and only
it, wherever it is printed in the from-year document (either text layer). Else, at each
place the quote is printed on the cited pages with the from-year value (its line numbers
as printed: the citation was written for that edition), the narrowest window of printed
words (3, 6, 10 or 16 words each side, a parenthesis it opens closed) that does, together
with the next wider window, which must read the same in the to-year edition, so that a
clause added just past the narrow window declines the reading. Where no window names the
value alone (the rows of a table), the quote or narrowest window is read in order.

In the to-year edition a text is read where every match gives one value ("printed once");
else, when it is printed the same number of times in each text layer of both editions,
from the to-year matches at the positions of the from-year matches that print the
from-year value ("in order"). Where a percentage is printed with its decimal
("7.5% (0.075)") the two must agree.

Status per parameter:
  unchanged      found; every place read gives the from-year value
  changed        found; every place read gives one other value
  not found      with the reason: a place read is not printed in the to-year edition
                 (reworded or gone), or printed there with different figures in more
                 than one place, or the places give different values; no to-year
                 edition of the cited document is archived; no printed text at the cited
                 place names the from-year value alone (a table whose rows repeat the
                 same words); the citation quotes no printed figure of a count or a
                 fraction; the value is not a printed figure (a flag, an enumeration
                 value, a zero)
A place that cannot be read at all (its document has no to-year edition, or no text names
the value alone) is noted on a found record when other places of the citation were read.
A value read from an IRS draft (the manifest's "draft") is marked `draft: true`: a
proposal to re-verify against the final edition.

Nothing is guessed: a parameter whose text cannot be placed is reported, not filled. The
value is read from the document the citation names; a value superseded by a later law
that document does not reflect is read as that document prints it.

Two kinds of parameter are derived by a rule rather than read at their citation, and their
records carry `derived` (the rule) beside the status:
  moves_with_year: N   a Count declared so in the parameter file (a year of birth) is the
                       from-year value plus N for each year between the two tax years. When
                       the citation can also be read in the to-year edition, the reading must
                       agree, or the parameter is declined.
  Tax Computation Worksheet
                       tcw.<status>.b<k>.upper, .rate and .subtract are the to-year's rate
                       table row (section 1(j)(2), the revenue procedure of the year's
                       inflation adjustments, read by extract_printed_tables.rate_schedule)
                       at the worksheet row's rate: its upper limit, its rate, and the rate on
                       its lower limit less its base. The rule is first checked on the from-year
                       (each from-year value must equal the rule applied to the from-year's
                       schedule) and a status whose from-year values do not follow it is
                       declined. A to-year schedule with a different number of rows over the
                       Tax Table boundary (ordinary.table_boundary, its from-year value) than the
                       from-year's is noted on each of that status's records: the worksheet
                       section then needs a row the from-year form lacks.

--write writes reports/<to>/params_proposal_from_<from>.yaml (per parameter: status, the
from-year and proposed values, and the evidence: how the place was found, how it matched,
the to-year document and pages, the from-year text and the to-year text read) and .md (the
counts, the declined by reason, the changed values). --compare FILE scores the proposal
against a parameter file taken as the truth: values equal, different, declined; a
parameter the file has no value for is counted apart.
"""

import argparse
import collections
import json
import re
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import citations as C  # noqa: E402
import year_diff as YD  # noqa: E402

GAP = 400  # characters an omission (`...`) in a quote may stand for

# Printed figures, in normalized text (citations.norm: lower case, one space).
MONEY = r"\(?\$\s?\d{1,3}(?:,\d{3})*(?:\.\d\d)?\)?"
PCT = r"\d+(?:\.\d+)?%"
DEC = r"\(0?\.\d+\)"
FIGURE = re.compile(rf"(?<![\w.,$])(?:{MONEY}|{PCT}|{DEC})")
YEAR_RE = re.compile(r"(?<![\d,.$])((?:19|20)\d\d)(?![\d%]|,\d)")
BARE = re.compile(r"(?<![\w.,$/-])\d{1,3}[a-z]?(?![\w%,]|\.\d)")


# ---------- figures ----------

def money_cents(tok):
    """Cents of a printed amount ("$1,650", "($3,000)", "$5.50"); negative when parenthesized."""
    neg = tok.startswith("(") and tok.endswith(")")
    s = tok.strip("()").lstrip("$").strip().replace(",", "")
    whole, _, frac = s.partition(".")
    cents = int(whole) * 100 + (int(frac.ljust(2, "0")[:2]) if frac else 0)
    return -cents if neg else cents


def figure_kind(tok):
    if "%" in tok:
        return "pct"
    if "$" in tok:
        return "money"
    if tok.startswith("("):
        return "dec"
    return "bare" if tok.isdigit() else "ref"


def figure_value(tok):
    """A printed figure as a number: cents for money, a Fraction for a rate, an int for a bare number."""
    k = figure_kind(tok)
    if k == "money":
        return money_cents(tok)
    if k == "pct":
        return Fraction(tok.rstrip("%")) / 100
    if k == "dec":
        return Fraction(tok.strip("()"))
    return int(tok)


def scalars(value):
    """{key: scalar} of a parameter value: a per-filing-status table, or {None: scalar}."""
    if isinstance(value, dict) and not ("num" in value and "den" in value):
        return dict(value)
    return {None: value}


def kind_of(ptype, scalar):
    """How a scalar of this type is printed: 'money', 'rate', 'count' or None (not a printed figure)."""
    if isinstance(scalar, bool) or scalar is None:
        return None
    if "Dollars" in ptype and isinstance(scalar, int):
        return "money" if scalar != 0 else None
    if ptype == "Rate" and isinstance(scalar, dict):
        return "rate" if scalar.get("num") else None
    if ptype == "Count" and isinstance(scalar, int):
        return "count" if scalar > 0 else None
    return None


def matches_scalar(kind, scalar, tok):
    """Whether a printed figure prints the scalar."""
    fk = figure_kind(tok)
    if fk == "ref":
        return False
    v = figure_value(tok)
    if kind == "money":
        return fk == "money" and abs(v) == abs(scalar)
    if kind == "rate":
        r = Fraction(scalar["num"], scalar["den"])
        if fk in ("pct", "dec"):
            return v == r
        return fk == "bare" and r.numerator == 1 and v == r.denominator
    if kind == "count":
        return fk == "bare" and v == scalar
    return False


def to_scalar(kind, old, tok):
    """The to-year scalar a printed figure gives, in the representation of the from-year's."""
    v = figure_value(tok)
    if kind == "money":
        return -abs(v) if old < 0 else abs(v)
    if kind == "count":
        return v
    r = Fraction(1, v) if figure_kind(tok) == "bare" else v
    if r == Fraction(old["num"], old["den"]):
        return dict(old)
    if figure_kind(tok) == "pct":
        digits = tok.rstrip("%")
        places = len(digits.partition(".")[2])
        return {"num": int(digits.replace(".", "")), "den": 100 * 10 ** places}
    if figure_kind(tok) == "bare":
        return {"num": 1, "den": v}
    s = tok.strip("()")
    places = len(s.partition(".")[2])
    return {"num": int(s.replace(".", "").lstrip("0") or "0"), "den": 10 ** places}


# ---------- patterns ----------

LINE_REF = re.compile(r"\b(lines?|columns?|boxe?s?|parts?|steps?|sections?|§)\s+([0-9][0-9a-z.()]*)", re.I)


class Pattern:
    """Printed text as a regular expression: each figure a slot, each year moved by `shift`,
    punctuation between words optional, an omission (`...`) a short gap.
    With `flex`, a line, column, box, part, step or section number and a bare item number
    may be any such number (a renumbered form); without it they are read as printed."""

    def __init__(self, text, shift, slots_of, flex=False):
        self.text, self.flex = text, flex
        pieces = [p for p in (C.norm(x).strip(" ,;:") for x in re.split(r"\.\s?\.\s?\.|…", text)) if p]
        self.tokens = []    # printed figures and bare numbers, in order
        out = []
        for n, piece in enumerate(pieces):
            if n:
                out.append(r".{0,%d}?" % GAP)
            out.append(self._piece(piece, shift))
        self.regex = re.compile("".join(out))
        self.slots = slots_of(self.tokens)
        self.words = len(re.findall(r"[a-z]{2,}", " ".join(pieces)))

    @staticmethod
    def _literal(text):
        return re.sub(r"[,;:]", lambda m: m.group(0) + "?", re.escape(text))

    def _piece(self, piece, shift):
        spans = []
        for m in LINE_REF.finditer(piece):
            spans.append((m.start(2), m.end(2), "ref"))
        for kind, rx in (("fig", FIGURE), ("year", YEAR_RE), ("bare", BARE)):
            for m in rx.finditer(piece):
                if not any(s <= m.start() < e for s, e, _ in spans):
                    spans.append((m.start(), m.end(), kind))
        out, pos = [], 0
        for s, e, k in sorted(spans):
            out.append(self._literal(piece[pos:s]))
            tok = piece[s:e]
            if k == "ref":
                out.append(r"[0-9][0-9a-z.()]*" if self.flex else re.escape(tok))
            elif k == "year":
                # moved with the tax year: a document printed for several years (a statute)
                # must be read at the to-year's sentence
                out.append(str(int(tok) + shift))
            else:
                self.tokens.append(tok)
                i = len(self.tokens) - 1
                out.append(f"(?P<b{i}>\\d{{1,3}}[a-z]?)" if k == "bare" else f"(?P<b{i}>{FIGURE.pattern})")
            pos = e
        out.append(self._literal(piece[pos:]))
        return "".join(out)

    def read(self, text, starts):
        """[(page, {slot: printed figure}, start, end)] for every match in a layer's text. A bare
        number that is a value slot (a count, 1/N) must be a number; any other must be as printed,
        unless `flex`."""
        found = []
        for m in self.regex.finditer(text):
            ok = True
            for i, tok in enumerate(self.tokens):
                got = m.group(f"b{i}")
                if figure_kind(tok) in ("bare", "ref"):
                    ok = ok and (got.isdigit() if i in self.slots else (self.flex or got == tok))
                else:
                    ok = ok and figure_kind(got) == figure_kind(tok)
            if ok:
                found.append((page_of(starts, m.start()), {i: m.group(f"b{i}") for i in self.slots},
                              m.start(), m.end()))
        return found


def page_of(starts, offset):
    return sum(1 for s in starts if s <= offset)


def joined(layers):
    """Each text layer as one string with the start offset of each page."""
    out = []
    for layer in layers or []:
        starts, pos = [], 0
        for p in layer:
            starts.append(pos)
            pos += len(p) + 1
        out.append((" ".join(layer), starts))
    return out


# ---------- the citation's sentences ----------

def quotes_of(cite):
    """[(doc, pages or None, quote)] of a citation: the locator's quotes per segment, then `quote`."""
    doc, locator = cite.get("doc"), cite.get("locator") or ""
    out = []
    for seg_doc, pages, _anchor, quotes in YD.all_segments(doc, locator):
        out += [(seg_doc, pages, q) for q in quotes]
    if cite.get("quote"):
        out.append((doc, None, cite["quote"]))
    return out


def segments_of(cite):
    doc, locator = cite.get("doc"), cite.get("locator") or ""
    return [(d, pages) for d, pages, _a, _q in YD.all_segments(doc, locator)] or [(doc, None)]


def value_slots(entry):
    """A function of a pattern's figures giving {slot index: [keys]}: the figures that print
    the value's scalars."""
    ptype, sc = entry["type"], scalars(entry["value"])

    def slots(tokens):
        out = {}
        for key, s in sc.items():
            k = kind_of(ptype, s)
            for i, tok in enumerate(tokens):
                if k and matches_scalar(k, s, tok):
                    out.setdefault(i, []).append(key)
        return out
    return slots


def printable(entry):
    return all(kind_of(entry["type"], s) for s in scalars(entry["value"]).values())


def on(pages, page):
    """Whether a page is one of the cited pages (or the page a cited text runs on to)."""
    return pages is None or page in pages or (page - 1) in pages


WIDTHS = (3, 6, 10, 16)  # words of printed context around an occurrence, narrowest first
MIN_WORDS = 3            # words a pattern must print besides its figures


def window(text, start, end, k):
    """The printed text from k words before [start, end) to k words after."""
    a = start
    for _ in range(k):
        a = text.rfind(" ", 0, a - 1) if a > 1 else -1
        if a < 0:
            break
    b = end
    for n in range(k + 10):
        # past k words, only to close a parenthesis the window opened
        if n >= k and text.count("(", max(a, 0), b) <= text.count(")", max(a, 0), b):
            break
        b = text.find(" ", b + 1)
        if b < 0:
            break
    return text[max(a, 0):len(text) if b < 0 else b].strip()


class Reader:
    """One parameter's places, read in the from-year text."""

    def __init__(self, entry, A):
        self.entry, self.A = entry, A
        self.sc = scalars(entry["value"])
        self.slots_of = value_slots(entry)

    def scalar(self, key, tok):
        return to_scalar(kind_of(self.entry["type"], self.sc[key]), self.sc[key], tok)

    def gives_value(self, pat, got):
        return all(self.scalar(key, tok) == self.sc[key] for i, tok in got.items() for key in pat.slots[i])

    def reads_back(self, text, layers):
        """Whether the text, its line and item numbers free, reads the from-year value, and only
        it, wherever it is printed in the from-year document."""
        pat = Pattern(text, 0, self.slots_of, flex=True)
        if not pat.slots or pat.words < MIN_WORDS:
            return False
        reads = [got for layer_text, starts in layers for _p, got, _s, _e in pat.read(layer_text, starts)]
        return bool(reads) and all(self.gives_value(pat, got) for got in reads)

    def occurrences(self, layers, pages, quote):
        """(layer text, start, end) of each place on the cited pages (or anywhere, with no pages)
        where the quote is printed with the from-year value (its line numbers as printed: the
        citation was written for this edition), or with no quote each figure that prints it."""
        out = []
        for layer_text, starts in layers:
            if quote is not None:
                pat = Pattern(quote, 0, self.slots_of)
                spans = [(s, e) for _p, got, s, e in pat.read(layer_text, starts) if self.gives_value(pat, got)]
            else:
                spans = [(m.start(), m.end()) for m in FIGURE.finditer(layer_text) if self.slots_of([m.group(0)])]
            out += [(layer_text, s, e) for s, e in spans if on(pages, page_of(starts, s))]
        return out

    def sentences(self, doc, pages, quote):
        """The texts to read in the to-year edition for one place of the citation: the quote itself
        if it reads the value back alone; else, per occurrence on the cited pages, the narrowest
        printed window that does, with the next wider window to confirm it; else the quote (or
        the narrowest window), to be read in order. None when the place is not printed."""
        layers = joined(self.A.pages(doc))
        if quote is not None and self.reads_back(quote, layers):
            return [quote]
        occ = self.occurrences(layers, pages, quote)
        if not occ:
            return None
        found = []
        for text, s, e in occ:
            for n, k in enumerate(WIDTHS):
                w = window(text, s, e, k)
                if self.reads_back(w, layers):
                    # the next wider window confirms the reading: printed text that changed just
                    # past the narrow window (a new clause) declines it
                    wide = window(text, s, e, WIDTHS[n + 1] if n + 1 < len(WIDTHS) else 2 * k)
                    found.append(w)
                    if wide != w and self.reads_back(wide, layers):
                        found.append(wide)
                    break
            else:
                w = quote if quote is not None else window(text, s, e, WIDTHS[0])
                if Pattern(w, 0, self.slots_of).words < MIN_WORDS:
                    return None
                found.append(w)
        return list(dict.fromkeys(found))


def _values(reader, pat, got):
    """{key: {scalar as json}} of one match; more than one scalar for a key when a percentage
    and its decimal disagree."""
    vals = {}
    for i, tok in got.items():
        for key in pat.slots[i]:
            vals.setdefault(key, set()).add(json.dumps(reader.scalar(key, tok), sort_keys=True))
    return vals


def _read_all(reader, pat, layers, pick=None):
    """('read' | 'not printed' | 'ambiguous' | 'disagrees', {key: scalar}, [(page, printed)]) of
    the matches of a pattern (those `pick` names per layer, if given)."""
    figs, hits = {}, []
    for n, (layer_text, starts) in enumerate(layers):
        for j, (page, got, start, end) in enumerate(pat.read(layer_text, starts)):
            if pick is not None and j not in pick.get(n, ()):
                continue
            vals = _values(reader, pat, got)
            if any(len(v) > 1 for v in vals.values()):
                return "disagrees", None, []
            for key, v in vals.items():
                figs.setdefault(key, set()).update(v)
            hits.append((page, layer_text[start:end]))
    if not hits:
        return "not printed", None, []
    if any(len(v) > 1 for v in figs.values()):
        return "ambiguous", None, hits
    return "read", {k: json.loads(next(iter(v))) for k, v in figs.items()}, hits


def read_to(reader, text, A_layers, B, d, shift, order_only=False):
    """(status, {key: scalar}, [(page, printed)], how) of a text read in the to-year document,
    its years moved and its line and item numbers free (a form may be renumbered; a number is
    never evidence of the place):

    - "printed once": every match gives one value;
    - "in order": the matches give different values, and the text is printed the same number of
      times in each text layer of both editions; the value is read from the to-year matches at
      the positions of the from-year matches that print the from-year value.
    The status is the reason it is not read otherwise: not printed, printed with different
    figures in several places, or a percentage that disagrees with its decimal."""
    B_layers = joined(B.pages(d))
    flex_b = Pattern(text, shift, reader.slots_of, flex=True)
    st, figs, hits = _read_all(reader, flex_b, B_layers)
    if st != "ambiguous" and not (order_only and st == "read"):
        return st, figs, hits, "printed once"
    flex_a = Pattern(text, 0, reader.slots_of, flex=True)
    pick = {}
    for n, (layer_text, starts) in enumerate(A_layers):
        a = flex_a.read(layer_text, starts)
        if not a:
            continue
        if n >= len(B_layers) or len(flex_b.read(*B_layers[n])) != len(a):
            return "ambiguous", None, hits, "in order"
        pick[n] = {j for j, (_p, got, _s, _e) in enumerate(a) if reader.gives_value(flex_a, got)}
    if not any(pick.values()):
        return "ambiguous", None, hits, "in order"
    st, figs, hits = _read_all(reader, flex_b, B_layers, pick)
    return st, figs, hits, "in order"


REASONS = {"no edition": "no {to} edition of {d} archived",
           "not printed": "not printed in the {to} edition of {d}",
           "ambiguous": "printed in the {to} edition of {d} with different figures in more than one place",
           "disagrees": "a percentage and its decimal disagree in the {to} edition of {d}"}


def propose_one(entry, A, B, shift, docs_to, to_year):
    """The record of one parameter: status, value and evidence, or the reason it is not found."""
    rec = {"type": entry["type"], "from_value": entry["value"]}
    if not printable(entry):
        rec.update(status="not found", reason="not a printed figure (a flag, an enumeration value or a zero)")
        return rec
    reader = Reader(entry, A)
    sources = [("quote", doc, pages, q) for doc, pages, q in quotes_of(entry["cite"])
               if Pattern(q, 0, reader.slots_of).slots]
    covered = {k for _h, _d, _p, q in sources for ks in Pattern(q, 0, reader.slots_of).slots.values() for k in ks}
    if not covered >= set(reader.sc) and all(kind_of(entry["type"], s) in ("money", "rate") for s in reader.sc.values()):
        # amounts no quote prints: each place on the cited pages that prints them
        sources += [("page", doc, pages, None) for doc, pages in segments_of(entry["cite"])]
    if not sources:
        rec.update(status="not found", reason="the citation quotes no printed figure of the value "
                                              "(a count or a fraction stated in words, a table cell)")
        return rec
    # A place the to-year edition does not print as it was (reworded, gone, or printed with
    # different figures in several places) declines the parameter. A place that cannot be
    # read at all (no to-year edition, no from-year text naming the value alone) is noted.
    got, evidence, reasons, notes = {}, [], [], []
    for how, doc, pages, q in sources:
        if doc not in A.docs or not A.pages(doc):
            notes.append(f"{doc} has no text in the from-year archive")
            continue
        texts = reader.sentences(doc, pages, q)
        if not texts:
            what = f"“{q[:80]}”" if q else f"{doc} p. {C._pages_text(pages) if pages else 'any'}"
            notes.append(f"no printed text at {what} reads the from-year value alone")
            continue
        d = docs_to(doc)
        if d not in B.docs or not B.pages(d):
            notes.append(REASONS["no edition"].format(to=to_year, d=d))
            continue
        A_layers = joined(A.pages(doc))
        reads = [(text,) + read_to(reader, text, A_layers, B, d, shift) for text in texts]
        if q is not None and q not in texts and any(r[1] == "not printed" for r in reads):
            # the words around the quote changed: the quote itself, read in order
            alone = read_to(reader, q, A_layers, B, d, shift, order_only=True)
            if alone[0] == "read":
                reads = [(q,) + alone]
        for text, st, figs, hits, matched in reads:
            if st != "read":
                reasons.append(f"“{text[:90]}” is " + REASONS[st].format(to=to_year, d=d))
                continue
            for k, v in figs.items():
                if isinstance(v, dict):
                    v = {"num": v["num"], "den": v["den"]}
                got.setdefault(k, {})[json.dumps(v, sort_keys=True)] = v
            evidence.append({"how": how, "matched": matched, "doc": d, "pages": sorted({p for p, _ in hits}),
                             "from_text": text, "read": sorted({h for _, h in hits})[:2]})
    if any(len(v) > 1 for v in got.values()):
        rec.update(status="not found", reason="the places the citation names give different values: "
                   + "; ".join(f"{k}: {sorted(v)}" for k, v in got.items() if len(v) > 1))
        return rec
    if set(got) != set(reader.sc) or reasons:
        rec.update(status="not found", reason="; ".join(dict.fromkeys(reasons + notes))
                   or "the value's figures are not all printed")
        return rec
    new = {k: next(iter(v.values())) for k, v in got.items()}
    value = new[None] if list(new) == [None] else {k: new[k] for k in entry["value"]}
    rec.update(status="unchanged" if value == entry["value"] else "changed", value=value, evidence=evidence)
    if notes:
        rec["notes"] = list(dict.fromkeys(notes))
    return rec


# ---------- values derived by a rule ----------

def moved_with_year(entry, shift, read):
    """The record of a Count declared `moves_with_year: N`: the from-year value plus N a year.
    `read` is the record of the ordinary reading of its citation, which must not contradict it."""
    n = entry["moves_with_year"]
    if not (isinstance(n, int) and isinstance(entry["value"], int) and entry["type"] == "Count"):
        return {"type": entry["type"], "from_value": entry["value"], "status": "not found",
                "reason": "moves_with_year is declared on a value that is not a Count"}
    value = entry["value"] + n * shift
    rec = {"type": entry["type"], "from_value": entry["value"],
           "status": "unchanged" if value == entry["value"] else "changed", "value": value,
           "derived": f"moves_with_year: {n} (the from-year value plus {n} a tax year)"}
    if read.get("status") in ("changed", "unchanged"):
        if read["value"] != value:
            return {"type": entry["type"], "from_value": entry["value"], "status": "not found",
                    "reason": f"the citation reads {read['value']} in the to-year edition, the year moved gives {value}"}
        rec["evidence"] = read["evidence"]
    return rec


TCW = re.compile(r"tcw\.(single|mfj|mfs|hoh)\.b(\d+)\.(upper|rate|subtract)$")


def tcw_rows(rows, boundary):
    """The rows of a rate schedule a Tax Computation Worksheet section has: those over the boundary."""
    return [r for r in rows if r["upper"] is None or r["upper"] > boundary]


def tcw_cell(row, field):
    if field == "upper":
        return row["upper"]
    if field == "rate":
        return {"num": row["rate"]["num"], "den": row["rate"]["den"]}
    sub = Fraction(row["rate"]["num"], row["rate"]["den"]) * row["over"] - row["base"]
    return int(sub) if sub.denominator == 1 else None


def tcw_records(values, schedules, from_year, to_year):
    """{pid: record} of every tcw.* parameter of the from-year file, derived from the to-year schedule.
    `schedules` is (from-year table, to-year table, to-year document id, draft) as written by
    extract_printed_tables.rate_schedule."""
    pids = [p for p in values if TCW.match(p)]
    if not pids:
        return {}
    (sa, sb, doc, draft), out = schedules, {}
    boundary = (values.get("ordinary.table_boundary") or {}).get("value")
    for pid in pids:
        status, k, field = TCW.match(pid).groups()
        entry = values[pid]
        rec = {"type": entry["type"], "from_value": entry["value"]}
        out[pid] = rec
        if not isinstance(boundary, int):
            rec.update(status="not found", reason="ordinary.table_boundary has no from-year amount")
            continue
        ra, rb = tcw_rows(sa["schedules"][status], boundary), tcw_rows(sb["schedules"][status], boundary)
        mine = sorted(int(TCW.match(p).group(2)) for p in pids if p.startswith(f"tcw.{status}."))
        # The rule on the from-year: worksheet rows, numbered from the lowest (b1, or b0 for a row added before
        # it), are the schedule's rows over the boundary in order.
        first = mine[0]
        bad = [p for p in pids if p.startswith(f"tcw.{status}.")
               and (int(TCW.match(p).group(2)) - first >= len(ra)
                    or tcw_cell(ra[int(TCW.match(p).group(2)) - first], TCW.match(p).group(3)) != values[p]["value"])]
        if bad or max(mine) - first + 1 != len(ra):
            rec.update(status="not found", reason=f"the {from_year} worksheet rows for {status} do not follow the rule "
                       f"(the {from_year} schedule's rows over ${boundary // 100:,}): " + ", ".join(bad or ["the row count"]))
            continue
        rate = ra[int(k) - first]["rate"]
        row = next((r for r in rb if Fraction(r["rate"]["num"], r["rate"]["den"]) == Fraction(rate["num"], rate["den"])), None)
        if row is None:
            rec.update(status="not found", reason=f"the {to_year} schedule for {status} has no row at "
                       f"{rate['num']}/{rate['den']} over ${boundary // 100:,}")
            continue
        value = tcw_cell(row, field)
        if value is None:
            rec.update(status="not found", reason=f"the {to_year} subtraction amount is not a whole number of cents")
            continue
        lo = "the boundary" if row["over"] <= boundary else f"${row['over'] / 100:,.2f}"
        rec.update(status="unchanged" if value == entry["value"] else "changed", value=value,
                   derived=f"the {to_year} rate table row at the worksheet row's rate (upper limit; rate; rate x lower limit "
                           "less base)",
                   evidence=[{"how": "derived", "doc": doc, "draft": draft, "table": f"rate_schedule {status}",
                              "row": {"over": row["over"], "upper": row["upper"], "base": row["base"], "rate": row["rate"]},
                              "read": f"over {lo}" + (f" but not over ${row['upper'] / 100:,.2f}" if row["upper"] else "")
                                      + f": ${row['base'] / 100:,.2f} plus {row['rate']['num']}%"}])
        if len(rb) != len(ra):
            extra = [r for r in rb if not any(r["rate"] == x["rate"] for x in ra)]
            rec["notes"] = [f"the {to_year} {status} schedule has {len(rb)} rows over ${boundary // 100:,}, the {from_year} "
                            f"{len(ra)}: the worksheet section needs a row the {from_year} form lacks ("
                            + "; ".join(f"{r['rate']['num']}% to ${r['upper'] / 100:,.0f}" for r in extra) + ")",
                            f"the boundary is the {from_year} value of ordinary.table_boundary"]
    return out


def rate_schedules(from_year, to_year):
    """(from-year table, to-year table, to-year document, draft) of the rate schedules, or None when
    either year's revenue procedure is not archived."""
    import extract_printed_tables as E
    try:
        tables = []
        for y in (from_year, to_year):
            arch = E.Archive(y)
            tables.append((E.rate_schedule(arch)[0], arch))
    except (E.Missing, ValueError):
        return None
    (sa, _), (sb, arch_b) = tables
    doc = sb["cite"]["doc"]
    return sa, sb, doc, bool(arch_b.docs.get(doc, {}).get("draft"))


# ---------- the run ----------

def doc_map(from_year, to_year):
    nxt = YD.counterparts(from_year, to_year)
    rename = nxt if from_year < to_year else {v: k for k, v in nxt.items()}
    return lambda d: rename.get(d, d)


def propose(from_year, to_year, params_file=None, archives=None, schedules=None):
    """{pid: record}. `schedules` (tests) stands in for the two years' rate schedules (rate_schedules)."""
    params_file = params_file or ROOT / "params" / f"{from_year}.yaml"
    values = yaml.safe_load(Path(params_file).read_text(encoding="utf-8"))["params"]["values"]
    A, B = archives or (C.Archive(str(from_year)), C.Archive(str(to_year)))
    shift = int(to_year) - int(from_year)
    docs_to = doc_map(int(from_year), int(to_year))
    if any(TCW.match(p) for p in values):
        schedules = schedules or rate_schedules(int(from_year), int(to_year))
    derived = tcw_records(values, schedules, from_year, to_year) if schedules else {}
    out = {}
    for pid, entry in values.items():
        if pid in derived:
            out[pid] = rec = derived[pid]
            if rec.get("evidence") and rec["evidence"][0]["draft"]:
                rec["draft"] = True
            continue
        if entry.get("value") is None or not entry.get("cite"):
            out[pid] = {"type": entry.get("type"), "from_value": entry.get("value"),
                        "status": "not found", "reason": "no from-year value or citation"}
            continue
        rec = propose_one(entry, A, B, shift, docs_to, to_year)
        if "moves_with_year" in entry:
            rec = moved_with_year(entry, shift, rec)
        for ev in rec.get("evidence", []):
            ev["draft"] = bool(B.docs.get(ev["doc"], {}).get("draft"))
        if rec.get("evidence") and any(ev["draft"] for ev in rec["evidence"]):
            rec["draft"] = True
        out[pid] = rec
    return out


def compare(proposal, truth_file):
    truth = yaml.safe_load(Path(truth_file).read_text(encoding="utf-8"))["params"]["values"]
    rows = collections.Counter()
    wrong, missed = [], []
    for pid, rec in proposal.items():
        t = truth.get(pid)
        if t is None or t.get("value") is None:
            rows["truth absent or null"] += 1
            if rec["status"] in ("changed", "unchanged"):
                rows["  proposed where the truth has no value"] += 1
            continue
        if rec["status"] not in ("changed", "unchanged"):
            rows["declined"] += 1
            missed.append(pid)
        elif rec["value"] == t["value"]:
            rows["equal"] += 1
        else:
            rows["different"] += 1
            wrong.append((pid, rec["value"], t["value"]))
    return rows, wrong, missed


def summary(proposal):
    c = collections.Counter(r["status"] for r in proposal.values())
    drafts = sum(1 for r in proposal.values() if r.get("draft"))
    reasons = collections.Counter(_reason_class(r["reason"]) for r in proposal.values() if r["status"] == "not found")
    return c, drafts, reasons


def _reason_class(reason):
    for key, label in (("not a printed figure", "not a printed figure (a flag, an enumeration value or a zero)"),
                       ("give different values", "the places the citation names give different values"),
                       ("not printed in the", "the text read is not printed in the to-year edition (reworded or gone)"),
                       ("different figures in more than one", "printed with different figures in several places"),
                       ("disagree", "a percentage and its decimal disagree"),
                       ("quotes no printed figure", "the citation quotes no printed figure of the value"),
                       ("reads the from-year value alone", "no printed text at the cited place names the value alone"),
                       ("edition of", "no to-year edition archived")):
        if key in reason:
            return label
    return reason


def write(from_year, to_year, proposal, compare_out=None):
    out_dir = ROOT / "reports" / str(to_year)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / f"params_proposal_from_{from_year}"
    header = (f"# Proposed {to_year} parameter values, read from the archived {to_year} documents at the places the\n"
              f"# {from_year} citations name. Generated by tools/propose_params.py --from {from_year} --to {to_year};\n"
              f"# a proposal, not read by the build. Values from IRS drafts are marked draft: true.\n")
    stem.with_suffix(".yaml").write_text(header + yaml.safe_dump({"proposal": proposal}, sort_keys=False,
                                                                  allow_unicode=True, width=120), encoding="utf-8")
    c, drafts, reasons = summary(proposal)
    lines = [f"# Parameters proposed for {to_year} from the {from_year} citations", "",
             f"Generated by `tools/propose_params.py --from {from_year} --to {to_year}`. Records with evidence are in "
             f"`params_proposal_from_{from_year}.yaml`.", "",
             f"- {len(proposal)} parameters: {c['unchanged']} found and unchanged, {c['changed']} found and changed, "
             f"{c['not found']} not found",
             f"- {drafts} of the found values are read from an IRS draft (a proposal to re-verify against the final)",
             f"- {sum(1 for r in proposal.values() if r.get('derived'))} of the found values are derived by a rule "
             "(`derived`: a year of birth moved with the year, a Tax Computation Worksheet row from the rate tables)", "",
             "## Not found, by reason", ""]
    lines += [f"- {n} {r}" for r, n in reasons.most_common()]
    if compare_out:
        rows, wrong, _missed = compare_out
        lines += ["", "## Compared with the reference file", ""] + [f"- {k}: {v}" for k, v in rows.items()]
        lines += [f"- DIFFERENT `{p}`: proposed {json.dumps(a)}, reference {json.dumps(b)}" for p, a, b in wrong]
    lines += ["", "## Changed", ""]
    lines += [f"- `{p}`: {json.dumps(r['from_value'])} -> {json.dumps(r['value'])}"
              + (" (draft)" if r.get("draft") else "") + (" (derived)" if r.get("derived") else "")
              for p, r in proposal.items() if r["status"] == "changed"]
    noted = [(p, n) for p, r in proposal.items() if r.get("derived") for n in r.get("notes", [])[:1]]
    if noted:
        lines += ["", "## Derived values with a note", ""] + [f"- `{p}`: {n}" for p, n in noted]
    lines += ["", "## Not found", ""]
    lines += [f"- `{p}`: {r['reason']}" for p, r in proposal.items() if r["status"] == "not found"]
    stem.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return stem


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--from", dest="from_year", type=int)
    ap.add_argument("--to", dest="to_year", type=int)
    ap.add_argument("--params", help="the from-year parameter file (default params/<from>.yaml)")
    ap.add_argument("--compare", help="a parameter file to score the proposal against")
    ap.add_argument("--write", action="store_true", help="write reports/<to>/params_proposal_from_<from>.{yaml,md}")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not (a.from_year and a.to_year):
        ap.error("--from and --to are required")
    proposal = propose(a.from_year, a.to_year, a.params)
    c, drafts, reasons = summary(proposal)
    print(f"{len(proposal)} parameters: {c['unchanged']} unchanged, {c['changed']} changed, {c['not found']} not found; "
          f"{drafts} read from drafts; {sum(1 for r in proposal.values() if r.get('derived'))} derived")
    for r, n in reasons.most_common():
        print(f"  not found: {n} {r}")
    cmp = None
    if a.compare:
        cmp = compare(proposal, a.compare)
        rows, wrong, _ = cmp
        print("compared with", a.compare, dict(rows))
        for p, x, y in wrong:
            print(f"  DIFFERENT {p}: proposed {json.dumps(x)}, reference {json.dumps(y)}")
    if a.write:
        print("wrote", write(a.from_year, a.to_year, proposal, cmp).relative_to(ROOT))
    return 0


SELF_TEST_FROM = {
    "tst": ["Line 3 Limitation Chart. Enter $4,300 on the line below for the month. "
            "Family coverage: enter $8,550 on the line below for the month.",
            "9 Enter $150,000 ($300,000 if married filing jointly) 10 Subtract line 9 from line 8. "
            "3 Multiply line 2 by 7.5% (0.075) 4 Subtract line 3 from line 1. "
            "Multiply line 6 by 40% (0.40) and enter the result.",
            "7 Enter the smaller of the amount on line 6 or $25,000 8 Enter the amount from line 3. "
            "15 Enter the smaller of the amount on line 14c or $12,500 16 Add lines. "
            "The credit is limited to $500 for each other dependent.",
            "Under age 19 at the end of 2025 and younger than you. "
            "is at or below $197,300 ($394,600 if married filing jointly), and you are not a patron."],
    "law": ["in the case of any taxable year beginning in calendar year 2025, $40,000; "
            "in the case of any taxable year beginning in calendar year 2026, $40,400; and"],
    "gone": ["The maximum deduction is $2,500 for the year."],
    "table": [" ".join(f"amount for the row ${n * 100:,}" for n in range(1, 13))],
}
SELF_TEST_TO = {
    "tst": ["Line 3 Limitation Chart. Enter $4,400 on the line below for the month. "
            "Family coverage: enter $8,750 on the line below for the month.",
            "9 Enter $160,000 ($320,000 if married filing jointly) 10 Subtract line 9 from line 8. "
            "3 Multiply line 2 by 8% (0.075) 4 Subtract line 3 from line 1. "
            "Multiply line 6 by 10% (0.10) and enter the result.",
            "8 Enter the smaller of the amount on line 7 or $25,000 9 Enter the amount from line 3. "
            "20 Enter the smaller of the amount on line 19 or $12,500 21 Add lines. "
            "The credit is limited to $500 for each other dependent who is a citizen. "
            "The credit is limited to $600 for each other dependent.",
            "Under age 17 at the end of 2026 and younger than you. "
            "is at or below $201,750 ($201,775 if married filing separately; $403,500 if married filing jointly), "
            "and you are not a patron."],
    "law": ["in the case of any taxable year beginning in calendar year 2025, $40,000; "
            "in the case of any taxable year beginning in calendar year 2026, $40,400; and"],
    "table": [" ".join(f"amount for the row ${n * 110:,}" for n in range(1, 13))],
}


def _plant(root, docs):
    root.mkdir(parents=True)
    entries = []
    for doc, pages in docs.items():
        (root / f"{doc}.txt").write_text("\f".join(pages), encoding="utf-8")
        entries.append({"id": doc, "file": f"{doc}.pdf", "text_file": f"{doc}.txt"})
    (root / "manifest.json").write_text(json.dumps({"documents": entries}), encoding="utf-8")


def self_test():
    """Plant two editions of three documents and a parameter file, propose, and compare each
    record with its expected status and value."""
    st = lambda single, mfj: {"single": single, "mfj": mfj, "mfs": single, "hoh": single, "qss": single}
    cite = lambda doc, loc: {"doc": doc, "locator": loc}
    params = {
        "chart.self": ("NonNegDollars", 430000, cite("tst", 'p. 1, Line 3 Limitation Chart, "Enter $4,300 on the line below for the month"'),
                       ("changed", 440000)),
        "chart.family": ("NonNegDollars", 855000, cite("tst", 'p. 1, Line 3 Limitation Chart, "enter $8,550 on the line below for the month"'),
                         ("changed", 875000)),
        "base": ("NonNegDollars", st(15000000, 30000000), cite("tst", 'p. 2, line 9, "Enter $150,000 ($300,000 if married filing jointly)"'),
                 ("changed", st(16000000, 32000000))),
        "rate.disagrees": ("Rate", {"num": 75, "den": 1000}, cite("tst", 'p. 2, line 3, "Multiply line 2 by 7.5% (0.075)"'),
                           ("not found", None)),
        "rate.changed": ("Rate", {"num": 40, "den": 100}, cite("tst", 'p. 2, "Multiply line 6 by 40% (0.40)"'),
                         ("changed", {"num": 10, "den": 100})),
        "renumbered": ("NonNegDollars", 2500000, cite("tst", 'p. 3, line 7, "Enter the smaller of the amount on line 6 or $25,000"'),
                       ("unchanged", 2500000)),
        "row": ("NonNegDollars", 20000, cite("table", 'p. 1, "amount for the row $200"'), ("changed", 22000)),
        "ambiguous": ("NonNegDollars", 50000, cite("tst", 'p. 3, "The credit is limited to $500 for each other dependent"'),
                      ("not found", None)),
        "count": ("Count", 19, cite("tst", 'p. 4, "Under age 19 at the end of 2025 and younger than you"'), ("changed", 17)),
        "clause": ("NonNegDollars", st(19730000, 39460000), cite("tst", "p. 4, the threshold"), ("not found", None)),
        "statute": ("NonNegDollars", 4000000, cite("law", 'p. 1, "in the case of any taxable year beginning in calendar year 2025, $40,000"'),
                    ("changed", 4040000)),
        "no.edition": ("NonNegDollars", 250000, cite("gone", 'p. 1, "The maximum deduction is $2,500 for the year"'), ("not found", None)),
        "flag": ("Bool", True, cite("tst", "p. 1, Line 3 Limitation Chart"), ("not found", None)),
        # moves_with_year: no to-year edition to read, so the year moved alone; a reading that contradicts it declines
        "born.moved": ("Count", 2007, cite("gone", 'p. 1, "The maximum deduction is $2,500 for the year"'), ("changed", 2008)),
        "born.contradicted": ("Count", 19, cite("tst", 'p. 4, "Under age 19 at the end of 2025 and younger than you"'),
                              ("not found", None)),
        # Tax Computation Worksheet rows from the rate schedules (planted below)
        "ordinary.table_boundary": ("Dollars", 10000000, cite("gone", "p. 1"), ("not found", None)),
        "tcw.single.b1.upper": ("Dollars", 20000000, cite("gone", "p. 1"), ("changed", 21000000)),
        "tcw.single.b1.rate": ("Rate", {"num": 20, "den": 100}, cite("gone", "p. 1"), ("unchanged", {"num": 20, "den": 100})),
        "tcw.single.b1.subtract": ("Dollars", 500000, cite("gone", "p. 1"), ("changed", 1050000)),
        "tcw.single.b2.rate": ("Rate", {"num": 30, "den": 100}, cite("gone", "p. 1"), ("unchanged", {"num": 30, "den": 100})),
        "tcw.single.b2.subtract": ("Dollars", 2500000, cite("gone", "p. 1"), ("changed", 3150000)),
        "tcw.mfj.b1.upper": ("Dollars", 20000000, cite("gone", "p. 1"), ("not found", None)),
        "tcw.mfj.b1.rate": ("Rate", {"num": 20, "den": 100}, cite("gone", "p. 1"), ("not found", None)),
        "tcw.mfj.b1.subtract": ("Dollars", 500001, cite("gone", "p. 1"), ("not found", None)),
        "tcw.mfj.b2.rate": ("Rate", {"num": 30, "den": 100}, cite("gone", "p. 1"), ("not found", None)),
        "tcw.mfj.b2.subtract": ("Dollars", 2500000, cite("gone", "p. 1"), ("not found", None)),
        # rows numbered from b0 (a row added before row 1)
        "tcw.hoh.b0.rate": ("Rate", {"num": 10, "den": 100}, cite("gone", "p. 1"), ("unchanged", {"num": 10, "den": 100})),
        "tcw.hoh.b0.subtract": ("Dollars", 0, cite("gone", "p. 1"), ("unchanged", 0)),
        "tcw.hoh.b1.rate": ("Rate", {"num": 20, "den": 100}, cite("gone", "p. 1"), ("unchanged", {"num": 20, "den": 100})),
        "tcw.hoh.b2.rate": ("Rate", {"num": 30, "den": 100}, cite("gone", "p. 1"), ("unchanged", {"num": 30, "den": 100})),
    }
    moves = {"born.moved", "born.contradicted"}
    row = lambda upper, base, rate, over: {"upper": upper, "base": base, "rate": {"num": rate, "den": 100}, "over": over}
    old = [row(5000000, 0, 10, 0), row(20000000, 500000, 20, 5000000), row(None, 3500000, 30, 20000000)]
    new = [row(10500000, 0, 10, 0), row(21000000, 1050000, 20, 10500000), row(None, 3150000, 30, 21000000)]
    schedules = ({"schedules": {"single": old, "mfj": old, "hoh": new}}, {"schedules": {"single": new, "mfj": new, "hoh": new}},
                 "rp-tst", False)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        _plant(tmp / "from", SELF_TEST_FROM)
        _plant(tmp / "to", SELF_TEST_TO)
        pfile = tmp / "params.yaml"
        pfile.write_text(yaml.safe_dump({"params": {"tax_year": 2025, "values": {
            pid: {"type": t, "value": v, "cite": c, **({"moves_with_year": 1} if pid in moves else {})}
            for pid, (t, v, c, _e) in params.items()}}}), encoding="utf-8")
        archives = (C.Archive("2025", sources=tmp / "from"), C.Archive("2026", sources=tmp / "to"))
        proposal = propose(2025, 2026, pfile, archives, schedules)
    bad = []
    for pid, (_t, _v, _c, (status, value)) in params.items():
        rec = proposal[pid]
        if rec["status"] != status or (value is not None and rec.get("value") != value):
            bad.append(f"{pid}: expected {status} {json.dumps(value)}, got {rec['status']} "
                       f"{json.dumps(rec.get('value'))} {rec.get('reason', '')}")
    if proposal["row"].get("evidence", [{}])[0].get("matched") != "in order":
        bad.append("row: expected the reading in order")
    if not proposal["born.moved"].get("derived") or not proposal["tcw.single.b1.upper"].get("derived"):
        bad.append("born.moved, tcw.single.b1.upper: expected marked derived")
    if "10% to $105,000" not in " ".join(proposal["tcw.single.b2.rate"].get("notes", [])):
        bad.append("tcw.single.b2.rate: expected the note of the to-year row over the boundary that the from-year lacks")
    if "follow the rule" not in proposal["tcw.mfj.b2.rate"].get("reason", ""):
        bad.append("tcw.mfj.b2.rate: expected declined, the from-year values not following the rule")
    print(f"propose_params self-test: {len(params) - len(bad)} of {len(params)} planted parameters as expected")
    for b in bad:
        print("  FAIL", b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
