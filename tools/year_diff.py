#!/usr/bin/env python3
"""The year-diff (design Stage 6): which of one year's definitions rest on IRS text
that is different in another year.

    year_diff.py --from 2025 --to 2026              the report, reports/2026/year_diff_from_2025.{md,html}
    year_diff.py --from 2025 --to 2026 --adopt      first copy the 2025 definitions to 2026 (see adopt)

The citations of the data year (--data, by default --from: the year whose
definitions exist) are read against both years' archived text. Each archived PDF
is split into sentences of its reading-order text, and each archived web page into
sentences of its derived text (one page, so its citations, which name no page, read
it whole), and the two years' sentences
are aligned (difflib), the other year's text read with its years moved to the
data year's (a sentence naming its own tax year is not a change): each sentence of
the data year is unchanged, changed (with
its counterpart; "numbers only" when only figures differ) or has no counterpart.
For each citation segment:

  - a quote, or the citation's heading, printed in one year's edition and not the
    other's is a strong finding (either way round: after --adopt the citations
    were written for the other year's text);
  - changed sentences near the citation (from its heading's sentence on the cited
    pages, or the cited pages when the heading is not found) are a finding, listed
    old beside new;
  - a document with no edition in one of the years is reported as such (a document
    whose id changes from year to year names its successor with "next" in the
    earlier year's catalog, tools/sources/<year>.json).

Findings are grouped by what carries the citation: form line, refusal, collection,
parameter, table, ambiguity register entry, interview question. A parameter whose
value is printed in a changed sentence near its citation, and not in that sentence's
counterpart, is flagged as a probable value change (an amount under $1,000 is looked
for with its dollar sign only). Tables are reported by their pages; their cells need
re-extraction.
Nothing is changed: the report points, a person decides.

--adopt lists every line of the copied definitions that names a year outside a citation
(a locator or quote, its continuation lines included), on the worklist, each year classed
(literal_scan, LITERAL_CLASSES): the from-year, an id that bears a year (person.born_before_2001,
amb.2025.x), a year of birth beside a year-moving age parameter, a year next to the from-year,
a document number, or another year; with the line's moving years moved, as a candidate. It
lists, too, the year-shared code and tool data that name an id the operations remove
(tools/year_shared_refs.py). It copies
the from-year's definitions (forms, tables, parameters, register,
interview, the citation rulings, marked "carried" for review, the rulings and baselines
of the source-coverage checks, the twin declarations, and the input and adapter contract banks) to the to-year
with tax_year and the year in file names and in
"(<year>)" form citations replaced, relocates their page numbers against the
to-year's archive (tools/citations.py --relocate --from <from-year>, which lists
the segments left for review in reports/<to-year>/relocation_from_<from-year>.md),
applies the year-change operations of changes/<to-year>/ to the copy
(tools/year_changes.py: their values are written for the to-year's text, so they
replace relocated values and are not relocated), and then reports with the
to-year as the data year. It refuses to overwrite an existing year, and refuses to
adopt when an operation does not apply to the from-year's definitions or reads a
line it awaits that no operation has added. An enum declared `extends_with_year: true`
in the parameters (placed_year) gains the value y<to-year>, and the recovery_year table
is re-derived for the to-year (each row to-year less the year placed in service, plus 1,
after checking that every from-year row follows that rule) with a row for y<to-year>.
"""

import argparse
import collections
import difflib
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import citations as C  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny, docs/ny/DECISIONS.md C1, C8)
from jurisdiction import ypath  # noqa: E402

WINDOW = 8  # sentences from the heading's sentence that a citation is read to rest on
PRINTED = {}  # (doc, shift, page, compared sentence) -> the sentence as printed


# ---------- documents ----------

def year_shifted(text, shift):
    """The text with each year from 1900 to 2099 moved by `shift`: the other year's
    "at the end of 2024" or "born before January 2, 1960" reads as the data year's, so
    a sentence that differs only by the dates that move with the tax year is equal."""
    if not shift:
        return text
    return re.sub(r"(?<![\d,.$])((?:19|20)\d\d)(?!\d|,\d)", lambda m: str(int(m.group(1)) + shift), text)


def sentences(arch, doc, shift=0):
    """[(page, normalized sentence)] of a PDF's reading-order text (a web page's text: page 1), its years moved by
    `shift` (the text as printed is kept in .printed[(page, sentence)])."""
    out = []
    d = arch.docs[doc]
    pages = arch.read(doc, "cols_file" if "cols_file" in d else "text_file").split("\f")
    for n, page in enumerate(pages, 1):
        for s in C.split_sentences(C.norm(page), ends=".!?:;"):
            printed = s.strip()
            s = year_shifted(printed, shift)
            if len(s) > 2:
                out.append((n, s))
                PRINTED[(doc, shift, n, s)] = printed
    return out


def shape(s):
    """A sentence with its figures (amounts, years, percentages) replaced."""
    return re.sub(r"\$?\d[\d,]*(\.\d+)?%?", "#", s)


class Alignment:
    """The data-year document's sentences, each marked against the other year's."""

    def __init__(self, a, b):
        self.a, self.b = a, b
        self.status = ["new"] * len(a)       # equal | numbers | changed | new
        self.partner = [None] * len(a)
        sm = difflib.SequenceMatcher(None, [s for _, s in a], [s for _, s in b], autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                for k in range(i2 - i1):
                    self.status[i1 + k] = "equal"
                    self.partner[i1 + k] = j1 + k
            elif tag == "replace":
                used = set()
                for i in range(i1, i2):
                    best, ratio = None, 0.5
                    for j in range(j1, j2):
                        if j in used:
                            continue
                        r = difflib.SequenceMatcher(None, a[i][1], b[j][1], autojunk=False).ratio()
                        if r > ratio:
                            best, ratio = j, r
                    if best is not None:
                        used.add(best)
                        self.partner[i] = best
                        self.status[i] = "numbers" if shape(a[i][1]) == shape(b[best][1]) else "changed"
        self.text_a = " ".join(s for _, s in a)
        self.text_b = " ".join(s for _, s in b)

    def changed(self, idx):
        return self.status[idx] != "equal"


# ---------- what carries each citation ----------

def carriers(year):
    """(kind, id, file, doc, locator) for every citation in the year's definitions."""
    y = str(year)
    out = []
    def add(kind, ident, path, cite):
        if isinstance(cite, dict) and isinstance(cite.get("locator"), str) and cite.get("doc"):
            out.append((kind, ident, C.rel(path), cite["doc"], cite["locator"]))
    for path in sorted((ypath("forms", y)).glob("*.yaml")):
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        doc = raw.get("form") or raw.get("def")
        if doc.get("collection"):
            add("collection", doc["id"], path, doc["collection"].get("cite"))
        for line in doc.get("lines", []):
            add("line", line["id"], path, line.get("cite"))
            for r in line.get("refuses", []) or []:
                add("refusal", line["id"], path, r.get("cite"))
    for path in sorted((ypath("tables", y)).glob("*.yaml")):
        t = yaml.safe_load(path.read_text(encoding="utf-8"))["table"]
        add("table", t["id"], path, t.get("cite"))
    p = jurisdiction.params_file(y)
    if p.exists():
        params = yaml.safe_load(p.read_text(encoding="utf-8"))["params"]
        for name, v in params.get("values", {}).items():
            add("parameter", name, p, v.get("cite"))
        for name, v in params.get("enums", {}).items():
            add("enum", name, p, v.get("cite"))
    p = jurisdiction.register_file(y)
    if p.exists():
        for e in yaml.safe_load(p.read_text(encoding="utf-8"))["register"]["entries"]:
            add("ambiguity", e["id"], p, e.get("cite"))
    p = jurisdiction.interview_dir(y) / "questions.yaml"
    if p.exists():
        for q in yaml.safe_load(p.read_text(encoding="utf-8"))["bank"]["questions"]:
            add("question", q["input"], p, q.get("cite"))
    return out


def param_values(year):
    """Dollar-amount parameters' values (rates and counts are not looked for in the text)."""
    p = jurisdiction.params_file(year)
    if not p.exists():
        return {}
    values = yaml.safe_load(p.read_text(encoding="utf-8"))["params"].get("values", {})
    return {k: v.get("value") for k, v in values.items() if "Dollars" in str(v.get("type", ""))}


def money_texts(value):
    """How a cents amount, or each amount of a per-filing-status table, may be printed:
    "15,750" (with the cents when not whole); amounts under a dollar are not looked for."""
    if isinstance(value, dict):
        return sorted({t for v in value.values() for t in money_texts(v)})
    if not isinstance(value, int) or isinstance(value, bool) or value < 100:
        return []
    return [f"{value // 100:,}" if value % 100 == 0 else f"{value / 100:,.2f}"]


def printed(amount, sentence):
    """Whether an amount ("22,937") is printed in a sentence as itself or with zero cents. An
    amount under $1,000 ("5", "400") must carry its dollar sign: as a bare number it is as
    likely a line, page or count."""
    dollar = r"\$\s?" if float(amount.replace(",", "")) < 1000 else ""
    return re.search(rf"(?<![\d,.]){dollar}{re.escape(amount)}(?:\.00)?(?![\d]|[.,]\d)", sentence) is not None


def all_segments(doc, locator):
    """(doc, pages, anchor, quotes) for every segment of a locator; a segment that names
    no pages ("section 3.06(1)", "Schedule SE (2025), line 7") has pages None: the
    whole document."""
    out = [(d, pages, anchor, quotes) for d, pages, anchor, quotes, _ in C.segments(doc, locator)]
    for plain, quotes in C.split_top(locator):
        if C.SEGMENT_RE.match(plain.strip()):
            continue
        out.append((doc, None, C.anchor_of(plain), quotes))
    return out


def counterparts(from_year, to_year):
    """data-year doc id -> other-year doc id, by "next" in the earlier year's catalog."""
    early, late = sorted((from_year, to_year))
    nxt = {}
    cat = jurisdiction.catalog(early)
    if cat.exists():
        for item in json.loads(cat.read_text()):
            if item.get("next"):
                nxt[item["id"]] = item["next"]
    return nxt


# ---------- the diff ----------

def run(from_year, to_year, data_year, archives=None, only=None, definitions=None):
    """The findings; `archives` replaces the archived years ({year: Archive}), `only`
    keeps the citations of one document and `definitions` reads another year's
    definitions as the data year's (all for the self-test)."""
    other_year = to_year if data_year == from_year else from_year
    arch = archives or {y: C.Archive(y) for y in (from_year, to_year)}
    A, B = arch[data_year], arch[other_year]
    nxt = counterparts(from_year, to_year)
    rename = nxt if data_year < other_year else {v: k for k, v in nxt.items()}
    alignments, doc_state = {}, {}

    def alignment(doc):
        if doc in alignments:
            return alignments[doc]
        other = rename.get(doc, doc)
        if doc not in A.docs and other in B.docs:
            alignments[doc] = None
            doc_state[doc] = f"no {data_year} edition archived"
        elif doc not in A.docs or not A.docs[doc]["file"].endswith((".pdf", ".html")):
            alignments[doc] = None
            doc_state[doc] = "not compared (no PDF or web page text)"
        elif other not in B.docs:
            alignments[doc] = None
            doc_state[doc] = f"no {other_year} edition archived"
        else:
            al = Alignment(sentences(A, doc), sentences(B, other, data_year - other_year))
            al.printed_b = lambda j, other=other: PRINTED[(other, data_year - other_year) + al.b[j]]
            alignments[doc] = al
            n = collections.Counter(al.status)
            doc_state[doc] = (f"{n['equal']} sentences unchanged, {n['numbers']} with figures changed, "
                              f"{n['changed']} reworded, {n['new']} without a counterpart"
                              + (f" (compared with {other})" if other != doc else ""))
        return alignments[doc]

    values = param_values(definitions or data_year)
    items = collections.OrderedDict()
    for kind, ident, path, doc, locator in carriers(definitions or data_year):
        for seg_doc, pages, anchor, quotes in all_segments(doc, locator):
            if only and seg_doc != only:
                continue
            al = alignment(seg_doc)
            shown = pages
            if al is not None and pages is None:
                pages = sorted({p for p, _ in al.a})
            key = (kind, ident)
            entry = items.setdefault(key, {"kind": kind, "id": ident, "file": path, "findings": []})
            if al is None:
                if doc_state[seg_doc].startswith("no "):
                    entry["findings"].append({"strength": "document", "doc": seg_doc, "pages": shown,
                                              "what": f"{seg_doc} has {doc_state[seg_doc]}"})
                continue
            # A quote or heading printed in one year's edition and not the other's: written for
            # the data year and gone from the other, or (after --adopt) written for the other
            # year and not printed in the data year.
            for q in quotes:
                parts = C.parts_of(q)
                if not parts:
                    continue
                # The quote as written and with its years moved to the data year's (after
                # --adopt a quote such as "at the end of 2025" was written for the other year).
                variants = (parts, [year_shifted(p, data_year - other_year) for p in parts])
                here, there = (any(all(p in t for p in v) for v in variants) for t in (al.text_a, al.text_b))
                if here != there:
                    entry["findings"].append({"strength": "quote", "doc": seg_doc, "pages": shown,
                                              "what": f"quote printed in {data_year if here else other_year} only: \u201c{q}\u201d",
                                              "pairs": near_pairs(al, pages, parts[0], 3)})
            keys = C.anchor_keys(anchor)
            here, there = (any(all(p in t for p in k) for k in keys) for t in (al.text_a, al.text_b))
            if here != there:
                entry["findings"].append({"strength": "heading", "doc": seg_doc, "pages": shown,
                                          "what": f"the heading \u201c{anchor}\u201d is printed in the {data_year if here else other_year} edition only"})
            window = citation_window(al, pages, anchor)
            changed = [i for i in window if al.changed(i)]
            if changed:
                figures_only = all(al.status[i] == "numbers" for i in changed)
                entry["findings"].append({"strength": "figures" if figures_only else "text", "doc": seg_doc, "pages": pages,
                                          "what": f"{len(changed)} of {len(window)} sentences near the citation "
                                                  + ("have different figures" if figures_only else "differ"),
                                          "pairs": [pair(al, i) for i in changed[:6]]})
            if kind == "parameter":
                cited = [i for i, (p, _) in enumerate(al.a) if p in pages]
                for text in money_texts(values.get(ident)):
                    # printed in a sentence that differs, and not printed in its counterpart: a
                    # sentence reworded around an unchanged amount is not a value change
                    hits = [i for i in cited if printed(text, al.a[i][1]) and al.changed(i)
                            and not (al.partner[i] is not None and printed(text, al.b[al.partner[i]][1]))]
                    if hits:
                        entry["findings"].append({"strength": "value", "doc": seg_doc, "pages": shown,
                                                  "what": f"the value {text} is printed in a sentence that differs in {other_year}",
                                                  "pairs": [pair(al, i) for i in hits[:3]]})
                        continue
                    # After --adopt the value is the other year's: printed on the other year's
                    # pages that hold the cited sentences' counterparts, and nowhere on this
                    # year's cited pages.
                    other_pages = {al.b[al.partner[i]][0] for i in cited if al.partner[i] is not None}
                    there = [j for j, (p, s) in enumerate(al.b) if p in other_pages and printed(text, s)]
                    if there and not any(printed(text, al.a[i][1]) for i in cited):
                        entry["findings"].append({"strength": "value", "doc": seg_doc, "pages": shown,
                                                  "what": f"the value {text} is printed in {other_year} and not on the cited {data_year} pages",
                                                  "pairs": [{"page": min(pages), "this": "(the value is not printed on the cited pages)",
                                                             "other": al.printed_b(j), "other_page": al.b[j][0]} for j in there[:3]]})
    flagged = [e for e in items.values() if e["findings"]]
    return {"from": from_year, "to": to_year, "data": data_year, "other": other_year,
            "docs": doc_state, "items": list(items.values()), "flagged": flagged}


def citation_window(al, pages, anchor):
    """Sentence indexes a citation rests on: from its heading's sentence on the cited
    pages (or a heading in force before them), WINDOW sentences on; else the cited pages."""
    on_pages = [i for i, (p, _) in enumerate(al.a) if p in pages]
    keys = C.anchor_keys(anchor)
    reach = range(max(1, min(pages) - C.IN_FORCE), max(pages) + 1)
    for k in keys:
        starts = [i for i, (p, s) in enumerate(al.a) if p in reach and all(part in s for part in k)]
        if starts:
            start = next((i for i in starts if al.a[i][0] in pages), starts[-1])
            return list(range(start, min(len(al.a), start + WINDOW)))
    return on_pages


def where(f):
    return f"{f['doc']}, " + ("whole document" if f["pages"] is None else f"p. {C._pages_text(f['pages'])}")


def pair(al, i):
    j = al.partner[i]
    return {"page": al.a[i][0], "this": al.a[i][1], "other": al.printed_b(j) if j is not None else None,
            "other_page": al.b[j][0] if j is not None else None}


def near_pairs(al, pages, first_part, n):
    hits = [i for i, (p, s) in enumerate(al.a) if p in pages and first_part[:40] in s]
    return [pair(al, i) for i in hits[:n]]


# ---------- report ----------

STRENGTH = {"document": "no edition in one year", "heading": "heading printed in one year only", "quote": "quote printed in one year only",
            "value": "probable value change", "text": "text near the citation differs", "figures": "figures near the citation differ"}
ORDER = ["document", "heading", "quote", "value", "text", "figures"]
REVIEW = {"document", "heading", "quote", "value"}  # the worklist; the rest is shown below it


def top_strength(e):
    return min(ORDER.index(f["strength"]) for f in e["findings"])


def on_worklist(e):
    return any(f["strength"] in REVIEW for f in e["findings"])


def write_report(r):
    out_dir = ypath("reports", str(r["to"]))
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / f"year_diff_from_{r['from']}"
    by_strength = collections.Counter(top_strength(e) for e in r["flagged"])
    kinds = collections.Counter(e["kind"] for e in r["flagged"] if on_worklist(e))
    work = sorted((e for e in r["flagged"] if on_worklist(e)), key=lambda e: (top_strength(e), e["kind"], e["id"]))
    rest = sorted((e for e in r["flagged"] if not on_worklist(e)), key=lambda e: (top_strength(e), e["kind"], e["id"]))
    lines = [f"# Year diff, {r['from']} to {r['to']}", "",
             f"Generated by `tools/year_diff.py`: the {r['data']} definitions' citations read against the {r['from']} and "
             f"{r['to']} archived text. Of {len(r['items'])} citing items, {len(work)} are on the worklist (a document, heading "
             f"or quote in one year only, or a probable value change) and {len(rest)} more have only nearby text or figures "
             "that differ.", "", "| Strongest finding | Items |", "| --- | --- |"]
    lines += [f"| {STRENGTH[ORDER[k]]} | {v} |" for k, v in sorted(by_strength.items())]
    lines += ["", "| Kind (worklist) | Items |", "| --- | --- |"] + [f"| {k} | {v} |" for k, v in kinds.most_common()]
    lines += ["", "## Documents", ""] + [f"- `{d}`: {s}" for d, s in sorted(r["docs"].items())] + ["", "## Worklist", ""]
    literals_file = ypath("reports", str(r["to"])) / f"year_literals_from_{r['from']}.json"
    if r["data"] == r["to"] and literals_file.exists():
        literals = json.loads(literals_file.read_text())
        lines += [f"### Definitions that name a year outside citations ({len(literals)})", ""]
        for c, what in LITERAL_CLASSES.items():  # a line is listed under the first class it holds
            recs = [x for x in literals if next(iter(x["classes"]), None) == c]
            if not recs:
                continue
            lines += [f"#### {c} ({len(recs)}): {what}", ""]
            for x in recs:
                also = ", ".join(f"{k} {', '.join(map(str, v))}" for k, v in x["classes"].items())
                lines.append(f"- `{x['file']}:{x['line']}` ({also}"
                             + (f"; beside {', '.join(x['age_params'])}" if x.get("age_params") else "") + f"): {x['text'][:160]}")
                if x.get("moved"):
                    lines.append(f"  - moved: {x['moved'][:160]}")
            lines.append("")
    for e in work:
        lines.append(f"### {e['kind']} `{e['id']}` ({e['file']})")
        lines.append("")
        for f in sorted(e["findings"], key=lambda f: ORDER.index(f["strength"])):
            lines.append(f"- **{STRENGTH[f['strength']]}** ({where(f)}): {f['what']}")
            for p in f.get("pairs", [])[:3]:
                lines.append(f"  - {r['data']} p. {p['page']}: {p['this'][:300]}")
                lines.append(f"    {r['other']}" + (f" p. {p['other_page']}: {p['other'][:300]}" if p["other"] else ": (no counterpart)"))
        lines.append("")
    lines += ["## Below the worklist", "", "Nearby text or figures differ; the sentences are in the HTML report.", ""]
    lines += [f"- {e['kind']} `{e['id']}`: {STRENGTH[ORDER[top_strength(e)]]}" for e in rest]
    stem.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    write_html(r, stem.with_suffix(".html"), by_strength, kinds)
    print(f"year diff {r['from']} to {r['to']} (citations of {r['data']}): {len(work)} of {len(r['items'])} items on the "
          f"worklist, {len(rest)} with nearby differences only; " + ", ".join(f"{STRENGTH[ORDER[k]]} {v}" for k, v in sorted(by_strength.items())))
    print(f"report: {stem.relative_to(ROOT)}.md and .html")


def write_html(r, path, by_strength, kinds):
    e = html.escape
    sections = []
    for it in sorted(r["flagged"], key=lambda x: (not on_worklist(x), top_strength(x), x["kind"], x["id"])):
        top = min(ORDER.index(f["strength"]) for f in it["findings"])
        rows = []
        for f in sorted(it["findings"], key=lambda f: ORDER.index(f["strength"])):
            pairs = "".join(
                f"<tr><td>{r['data']} p.&nbsp;{p['page']}</td><td>{e(p['this'][:400])}</td>"
                f"<td>{(str(r['other']) + ' p.&nbsp;' + str(p['other_page'])) if p['other'] else ''}</td>"
                f"<td>{e(p['other'][:400]) if p['other'] else '<i>no counterpart</i>'}</td></tr>" for p in f.get("pairs", [])[:3])
            rows.append(f"<p><b>{e(STRENGTH[f['strength']])}</b> · {e(where(f))}: {e(f['what'])}</p>"
                        + (f"<table>{pairs}</table>" if pairs else ""))
        sections.append(f"<details class=s{top}><summary><span class=kind>{e(it['kind'])}</span> <code>{e(it['id'])}</code> "
                        f"<span class=meta>{e(STRENGTH[ORDER[top]])}</span></summary>{''.join(rows)}</details>")
    summary = "".join(f"<li>{e(STRENGTH[ORDER[k]])}: {v}</li>" for k, v in sorted(by_strength.items()))
    page = f"""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>Year diff {r['from']} to {r['to']}</title>
<style>
:root {{ color-scheme: light dark; --ink:#1d1d1f; --muted:#6e6e73; --line:#d2d2d7; --bg:#fff; }}
@media (prefers-color-scheme: dark) {{ :root {{ --ink:#f5f5f7; --muted:#a1a1a6; --line:#3a3a3c; --bg:#1c1c1e; }} }}
body {{ font: 15px/1.5 -apple-system, system-ui, sans-serif; color: var(--ink); background: var(--bg); max-width: 64rem; margin: 2rem auto; padding: 0 1rem; }}
details {{ border-top: 1px solid var(--line); padding: .4rem 0; }}
summary {{ cursor: pointer; }}
.kind {{ font-size: .75rem; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }}
.meta {{ color: var(--muted); font-size: .85rem; }}
table {{ border-collapse: collapse; font-size: .85rem; margin: .3rem 0 .8rem; }}
td {{ border-top: 1px solid var(--line); padding: .3rem .5rem; vertical-align: top; }}
td:nth-child(1), td:nth-child(3) {{ white-space: nowrap; color: var(--muted); }}
</style>
<h1>Year diff, {r['from']} to {r['to']}</h1>
<p class=meta>Generated by <code>tools/year_diff.py</code>: the {r['data']} definitions' citations read against both years' archived text.
{len(r['flagged'])} of {len(r['items'])} citing items have a finding, strongest first. Each item opens to show its findings,
the {r['data']} sentence beside its {r['other']} counterpart.</p>
<ul>{summary}</ul>
{''.join(sections)}
</html>"""
    path.write_text(page, encoding="utf-8")


# ---------- adoption ----------

YEAR_ID = re.compile(r"[A-Za-z_]\.?(?:19|20)\d\d(?!\d)")  # a year inside an id or constant: is2025, born_before_2001, y2019, amb.2025.x


# A year as text: not part of a longer number, an amount ($2,024) or a decimal; "2024-40" (a Rev. Proc. or Notice
# number) is matched and classed as a fixed reference.
YEAR_TEXT = re.compile(r"(?<![\d$,])(?<!\d\.)(?<![A-Za-z_])((?:19|20)\d\d)(?!\d|[,.]\d)(-\d{1,3}(?!\d))?")
BIRTH = re.compile(r"\b(?:born|birth|birthday|births)\b", re.I)
KEY_LINE = re.compile(r"^(\s*)(?:- )?([\w.$\[\]]+):(?:\s|$)")
CITATION_KEYS = {"locator", "quote"}
# The classes of a year literal, in report order, with what each usually asks of the adoption lane.
LITERAL_CLASSES = {
    "from_year": "names the from-year: moves when it means the tax year",
    "year_id": "an id or constant bearing a year: kept (ids are stable) or renamed by an operation",
    "birth_cutoff": "a year of birth beside a year-moving age parameter: moves with the year, as the parameter does",
    "adjacent_year": "a year next to the from-year (prior returns, carryovers, testing periods, the next year): "
                     "moves when it is relative to the tax year, stays when it is a statutory date",
    "fixed_reference": "a document number (Rev. Proc. 2024-40, Notice 2025-69): stays",
    "other_year": "another year (a statutory or historical date): usually stays",
}


def birth_cutoffs(params_file):
    """The year-of-birth parameters that move with the year: {name: (value, step)}. A parameter declares
    `moves_with_year: N`; an `age.*` Count is taken to move by 1 where nothing is declared."""
    data = yaml.safe_load(Path(params_file).read_text(encoding="utf-8")) if Path(params_file).exists() else {}
    out = {}
    for name, e in (((data or {}).get("params") or {}).get("values") or {}).items():
        if not isinstance(e, dict) or not isinstance(e.get("value"), int):
            continue
        step = e.get("moves_with_year", 1 if name.startswith("age.") and e.get("type") == "Count" else None)
        if isinstance(step, int) and step:
            out[name] = (e["value"], step)
    return out


def literal_scan(text, from_year, cutoffs=None, shift=1):
    """Every line of one copied definitions file that names a year outside a citation, classed. A citation is a
    `locator:` or `quote:` scalar with its continuation lines (relocation moves those). A year of birth is recognised
    by a word of birth on its line or the line before it, within the same scalar. Returns [(line number, line, {class:
    [years]}, [age parameters a year of birth sits beside], the line with each year of a moving class shifted by
    `shift`)]: the from-year, the adjacent years and the years of birth move; ids, document numbers and other years
    are kept. The moved line is a candidate for a person to accept, not an edit."""
    f = int(from_year)
    cutoffs = cutoffs or {}
    lines = text.split("\n")
    scalars = []  # [first line index, last line index, key, the key's column, whether the key line holds a value]
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.lstrip()
        if scalars and scalars[-1][4] and indent > scalars[-1][3] and not stripped.startswith("#"):
            scalars[-1][1] = i  # a continuation line of a scalar (plain, quoted or block)
            continue
        m = KEY_LINE.match(line)
        if m:
            column = indent + (2 if stripped.startswith("- ") else 0)
            scalars.append([i, i, m.group(2), column, bool(line[m.end():].strip())])
        elif stripped.startswith("#"):
            scalars.append([i, i, "#", indent, False])
        else:  # a list item's scalar, or a stray line
            scalars.append([i, i, "-", indent + (2 if stripped.startswith("- ") else 0) - 1, True])
    out = []
    for first, last, key, _, _ in scalars:
        if key.split(".")[-1] in CITATION_KEYS:
            continue
        for i in range(first, last + 1):
            line = lines[i]
            born = bool(BIRTH.search(" ".join(lines[max(first, i - 1):i + 1])))  # this line and the one before
            classes, near, moved, at = {}, [], [], 0
            ids = [m.span() for m in YEAR_ID.finditer(line)]
            if ids:
                classes["year_id"] = sorted({int(m.group(0)[-4:]) for m in YEAR_ID.finditer(line)})
            for m in YEAR_TEXT.finditer(line):
                if any(a <= m.start(1) < b for a, b in ids):
                    continue  # the year of an id (amb.2025.x) is the id's
                y = int(m.group(1))
                # a cut-off year is printed as itself (born before January 2, 1961) or the year before (born after
                # December 31, 1960); the bounds that sit at the tax year (age.birth_year_latest) are not cut-offs
                beside = [n for n, (v, _) in sorted(cutoffs.items()) if y in (v, v - 1) and f - v >= 10]
                if m.group(2):
                    c = "fixed_reference"
                elif y == f:
                    c = "from_year"
                elif beside and (born or (key == "value" and any(cutoffs[n][0] == y for n in beside))):
                    c = "birth_cutoff"  # (a parameter's own value: propose_params.py moves it)
                    near += [n for n in beside if n not in near]
                elif f - 3 <= y <= f + 2:
                    c = "adjacent_year"
                else:
                    c = "other_year"
                classes.setdefault(c, [])
                if y not in classes[c]:
                    classes[c].append(y)
                if c in ("from_year", "birth_cutoff", "adjacent_year"):
                    moved += [line[at:m.start(1)], str(y + shift)]
                    at = m.end(1)
            if classes:
                out.append((i + 1, line, classes, near, "".join(moved) + line[at:]))
    return out


def year_literal_report(files, from_year, to_year, params_file):
    """The year-literal list of an adoption: one record per line of the from-year definitions that names a year
    outside a citation, reported at its line of the copy (the copy keeps the lines). `files` is [(from-year file,
    its copy)]. A line the copy already carries with every moving year moved (tax_year, by the copy's conversion) is
    not listed."""
    cutoffs = birth_cutoffs(params_file)
    shift = int(to_year) - int(from_year)
    out = []
    for src, dst in files:
        copied = dst.read_text(encoding="utf-8").split("\n") if dst.exists() else []
        for n, line, classes, near, moved in literal_scan(src.read_text(encoding="utf-8"), from_year, cutoffs, shift):
            now = copied[n - 1] if n <= len(copied) else line
            if now != line and now == moved:
                continue
            rec = {"file": str(dst.relative_to(ROOT)) if dst.is_relative_to(ROOT) else str(dst), "line": n, "text": now.strip(),
                   "classes": {c: classes[c] for c in LITERAL_CLASSES if c in classes}}
            if near:
                rec["age_params"] = near
            if moved.strip() != now.strip():
                rec["moved"] = moved.strip()
            out.append(rec)
    return out


RECOVERY_TABLE = "recovery_year"


def extend_year_enums(text, f, t):
    """A parameters file's text with every enum declared `extends_with_year: true` given the value y<t> after y<f>
    (its values a flow list), and the names extended. An enum already holding y<t> is left; one lacking y<f> is an
    error: the year values must run to the from-year."""
    enums = ((yaml.safe_load(text) or {}).get("params") or {}).get("enums") or {}
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if re.match(r"^\s+enums:\s*$", l)), None)
    done = []
    for name, e in enums.items():
        if not (isinstance(e, dict) and e.get("extends_with_year") is True) or f"y{t}" in e.get("values", []):
            continue
        if f"y{f}" not in e.get("values", []):
            raise ValueError(f"enum {name} extends with the year but does not list y{f}")
        i = next(i for i in range(start + 1, len(lines)) if re.match(rf"^\s+{re.escape(name)}:\s*$", lines[i]))
        j = next(j for j in range(i + 1, len(lines)) if re.match(r"^\s+values:", lines[j]))
        m = re.match(r"^(\s+values:\s*\[.*?)\s*\]\s*$", lines[j])
        if not m:
            raise ValueError(f"enum {name}: its values are not a one-line [list]")
        lines[j] = f"{m.group(1)}, y{t}]"
        done.append(name)
    out = "\n".join(lines)
    for name in done:  # the edit is the declared one: the values gain y<t> and nothing else changes
        before, after = enums[name]["values"], yaml.safe_load(out)["params"]["enums"][name]["values"]
        assert after == before + [f"y{t}"], (name, after)
    return out, done


def enum_typed_ids(nodes, names):
    """Each id in `nodes` (parsed definitions, walked whole) whose type is Enum(<name>) for a name in `names`,
    with that name."""
    out, stack = {}, list(nodes)
    while stack:
        n = stack.pop()
        if isinstance(n, dict):
            m = re.fullmatch(r"Enum\((\w+)\)", str(n.get("type", "")))
            if m and m.group(1) in names and isinstance(n.get("id"), str):
                out[n["id"]] = m.group(1)
            stack.extend(n.values())
        elif isinstance(n, list):
            stack.extend(n)
    return out


def extend_year_labels(bank_text, typed, before, f, t):
    """The question bank's text with y<t>: '<t>' labelled first (the labels run newest first) in the value_labels
    of every question whose input is typed by an enum adoption extended with the year (`typed`: input id -> enum,
    from enum_typed_ids; `before`: enum -> its from-year values), and the inputs labelled. Each such question's
    labels must be exactly the enum's from-year values, y<f> first, each year member (yNNNN) labelled with its own
    year: otherwise the rule does not apply and it is an error. A member that is not a year (realty_year's
    before1987) keeps whatever label it has."""
    bank = ((yaml.safe_load(bank_text) or {}).get("bank") or {}).get("questions") or []
    lines = bank_text.split("\n")
    done = []
    for q in bank:
        name = typed.get(q.get("input"))
        if name is None or not q.get("value_labels"):
            continue
        labels = q["value_labels"]
        if sorted(labels) != sorted(before[name]) or any(labels[k] != k[1:] for k in labels if re.fullmatch(r"y\d{4}", k)) or next(iter(labels)) != f"y{f}":
            raise ValueError(f"question {q['input']}: its value_labels are not the {name} years each labelled by its "
                             f"year, newest (y{f}) first; label y{t} by hand")
        i = next(i for i, l in enumerate(lines) if re.match(rf"^\s*- input: {re.escape(q['input'])}\s*$", l))
        j = next(j for j in range(i + 1, len(lines)) if re.match(r"^\s+value_labels:\s*$", lines[j]))
        m = re.match(rf"^(\s+)y{f}: '{f}'\s*$", lines[j + 1])
        if not m:
            raise ValueError(f"question {q['input']}: value_labels does not open with y{f}: '{f}' on its own line")
        lines.insert(j + 1, f"{m.group(1)}y{t}: '{t}'")
        done.append(q["input"])
    out = "\n".join(lines)
    after = {q.get("input"): q.get("value_labels") for q in ((yaml.safe_load(out) or {}).get("bank") or {}).get("questions") or []}
    for inp in done:  # the edit is the declared one: the labels gain y<t> first and nothing else changes
        assert list(after[inp]) == [f"y{t}"] + list(next(q for q in bank if q.get("input") == inp)["value_labels"]), inp
    return out, done


def year_enum_rules(params_text, forms_dir, bank_text, f, t):
    """The year-valued enums extended (extend_year_enums) and the questions asking them labelled
    (extend_year_labels): (params text, enums extended, bank text, inputs labelled). Raises ValueError where a rule
    does not apply."""
    text, extended = extend_year_enums(params_text, f, t)
    if not extended or not bank_text:
        return text, extended, bank_text, []
    before = {n: yaml.safe_load(params_text)["params"]["enums"][n]["values"] for n in extended}
    typed = enum_typed_ids([yaml.safe_load(q.read_text(encoding="utf-8")) for q in sorted(Path(forms_dir).glob("*.yaml"))],
                           set(extended))
    btext, labelled = extend_year_labels(bank_text, typed, before, f, t)
    return text, extended, btext, labelled


def extend_recovery_year(text, f, t):
    """The recovery_year table's text re-derived for year t: each row's value is t less the year placed in service,
    plus 1 (year 1 is the year placed in service), a row for y<t> is added before the first, and the year in the
    title and the leading comment moves to t. Every from-year row is checked against the same rule first."""
    f, t = int(f), int(t)
    row = re.compile(r"^(\s*- \{ keys: \[y(\d{4})\], value: )(\d+)( \}\s*)$")
    lines = text.split("\n")
    first = None
    for i, l in enumerate(lines):
        m = row.match(l)
        if not m:
            if re.match(r"^\s*title:", l) or (first is None and l.startswith("#")):
                lines[i] = re.sub(rf"(?<!\d){f}(?!\d)", str(t), l)
            continue
        placed, value = int(m.group(2)), int(m.group(3))
        if value != f - placed + 1:
            raise ValueError(f"{RECOVERY_TABLE}: the row for y{placed} reads {value}, not {f} - {placed} + 1")
        if placed == t:
            raise ValueError(f"{RECOVERY_TABLE}: a row for y{t} exists")
        if first is None:
            first = (i, m.group(1)[:m.group(1).index("[") + 1])
        lines[i] = f"{m.group(1)}{t - placed + 1}{m.group(4)}"
    if first is None:
        raise ValueError(f"{RECOVERY_TABLE}: no row of the form '- {{ keys: [yNNNN], value: N }}'")
    lines.insert(first[0], f"{first[1]}y{t}], value: 1 }}")
    return "\n".join(lines)


def definition_files(pairs):
    """The (source, copy) file pairs of the from-year definitions: a directory pair gives every .yaml file under it
    (subdirectories included, at the same relative path, as year_changes.year_tree reads them), a file pair itself."""
    files = []
    for src, dst in pairs:
        if src.is_dir():
            files += [(p, dst / p.relative_to(src)) for p in sorted(src.rglob("*.yaml"))]
        elif src.exists():
            files.append((src, dst))
    return files


def unplanned_definitions(files, tree, interview_src):
    """The files the year operations read in the from-year tree (year_changes.Tree) that `files` does not copy:
    adoption would then fail on them half done, so it refuses first."""
    planned = {p for p, _ in files}
    read = [d["path"] for d in tree.forms.values()] + [interview_src / rel for rel in tree.others]
    read += [tree.bank_path] if tree.bank_text else []
    return sorted(str(p) for p in read if Path(p) not in planned)


def copy_definitions(files, f, t):
    """Write each planned copy (definition_files) with the year replaced where it names the tax year."""
    def convert(text):
        text = re.sub(rf"(?m)^(\s*tax_year:\s*){f}\b", rf"\g<1>{t}", text)
        return re.sub(rf"\((?:Rev\. )?{f}\)", f"({t})", text)

    for p, q in files:
        q.parent.mkdir(parents=True, exist_ok=True)
        q.write_text(convert(p.read_text(encoding="utf-8")), encoding="utf-8")


def adopt(from_year, to_year):
    """Copy the from-year definitions to the to-year (refusing to overwrite), with the
    year replaced where it names the year, and relocate their pages."""
    f, t = str(from_year), str(to_year)
    pairs = [(ypath("forms", f), ypath("forms", t)), (ypath("tables", f), ypath("tables", t)),
             (jurisdiction.params_file(f), jurisdiction.params_file(t)),
             (jurisdiction.register_file(f), jurisdiction.register_file(t))]
    pairs += [(jurisdiction.interview_dir(f), jurisdiction.interview_dir(t))]
    clash = [str(dst.relative_to(ROOT)) for _, dst in pairs if dst.exists()]
    if clash:
        sys.exit("adopt: refusing to overwrite " + ", ".join(clash))
    if not (ypath("sources", t) / "manifest.json").exists():
        sys.exit(f"adopt: archive the {t} sources first (tools/fetch_sources.py --year {t} --fetch)")
    import year_changes
    if year_changes.check(f, adopting=True, static=True)[0]:
        sys.exit(f"adopt: the operations of {ypath('changes', t).relative_to(ROOT)} do not all apply to the {f} "
                 "definitions, or the tree they produce fails the engine's static checks (above); mend them first")

    files = definition_files(pairs)
    missed = unplanned_definitions(files, year_changes.year_tree(f), jurisdiction.interview_dir(f))
    if missed:
        sys.exit(f"adopt: the year operations read {len(missed)} file(s) the copy would leave out: " + ", ".join(missed[:5]))
    params_f, bank_f = jurisdiction.params_file(f), jurisdiction.interview_dir(f) / "questions.yaml"
    try:  # the rules by year, tried on the from-year texts so a refusal leaves nothing half written
        year_enum_rules(params_f.read_text(encoding="utf-8") if params_f.exists() else "params: {}", ypath("forms", f),
                        bank_f.read_text(encoding="utf-8") if bank_f.exists() else "", f, t)
    except ValueError as e:
        sys.exit(f"adopt: {e}")
    for src, dst in pairs:
        if src.is_dir():
            dst.mkdir(parents=True)
    copy_definitions(files, f, t)
    # Year-valued enums and the table derived from them move by rule, not by judgment.
    params_t = jurisdiction.params_file(t)
    if params_t.exists():
        bank_t = jurisdiction.interview_dir(t) / "questions.yaml"
        text, extended, btext, labelled = year_enum_rules(params_t.read_text(encoding="utf-8"), ypath("forms", t),
                                                          bank_t.read_text(encoding="utf-8") if bank_t.exists() else "", f, t)
        params_t.write_text(text, encoding="utf-8")
        if extended:
            print(f"adopt: enums extended by y{t}: {', '.join(extended)}")
        if labelled:
            bank_t.write_text(btext, encoding="utf-8")
            print(f"adopt: y{t} labelled in the value_labels of {', '.join(labelled)}")
    recovery = ypath("tables", t) / f"{RECOVERY_TABLE}.yaml"
    if recovery.exists():
        recovery.write_text(extend_recovery_year(recovery.read_text(encoding="utf-8"), f, t), encoding="utf-8")
        print(f"adopt: {RECOVERY_TABLE} re-derived for {t}, with a row for y{t}")
    carried = carry_reviews(f, t) + carry_contracts(f, t)
    literals = year_literal_report(files, f, t, jurisdiction.params_file(f))
    (ypath("reports", t)).mkdir(parents=True, exist_ok=True)
    (ypath("reports", t) / f"year_literals_from_{f}.json").write_text(json.dumps(literals, indent=1, ensure_ascii=False) + "\n")
    by_class = collections.Counter(c for rec in literals for c in rec["classes"])
    print(f"adopt: {len(literals)} line(s) of the {t} definitions name a year outside citations "
          f"({(ypath('reports', t) / f'year_literals_from_{f}.json').relative_to(ROOT)}; "
          + ", ".join(f"{c} {by_class[c]}" for c in LITERAL_CLASSES if by_class[c]) + "); each is on the worklist")
    print(f"adopt: copied the {f} definitions (and citation rulings, to be reviewed again) to {t}; "
          f"relocating page numbers against the {t} archive")
    for line in carried:
        print("adopt: " + line)
    subprocess.run([sys.executable, str(ROOT / "tools" / "citations.py"), "--relocate", "--from", f, "--year", t, *jurisdiction.J_ARGS], check=True)
    r = year_changes.write(t)
    print(f"adopt: applied the {len(r.ops)} operations of {ypath('changes', t).relative_to(ROOT)} to the {t} "
          f"definitions ({len(r.touched)} lines added or changed, {len(r.removed)} removed); their values are written "
          f"for {t}'s text and were not relocated")
    if r.new_params:
        print(f"adopt: the operations read parameters params/{t}.yaml does not define: {', '.join(sorted(r.new_params))}")
    import year_shared_refs  # code and tool data kept for every year that name what the operations remove
    refs = year_shared_refs.references(year_changes.year_tree(f), r)
    stem = year_shared_refs.write_report(refs, f, t, ypath("reports", t))
    print(f"adopt: {len(refs)} reference(s) in year-shared files name ids the {t} operations remove or gates they "
          f"retire ({stem.relative_to(ROOT)}.md); each shared file is to be made to serve both years")


COVERAGE = ("operands", "consumers", "limits", "instruction_cites", "signs")  # tools/baseline_check.py
KEYED_BY_YEAR = ("input_quotes",)  # tools/citations.py: a parameter's finding is keyed "<year>:<parameter>"
DECLARED = ("twins",)  # tools/check_twins.py: the year's twin blocks and their intended differences
CONTRACT_BANKS = ("input_contracts", "adapter_contracts")  # under tools/transcription/


def carry_reviews(f, t):
    """Copy the from-year's review files that adoption keeps to the to-year, never over an existing file:
    the citation rulings, each marked "carried from <f>" to be reviewed again, and the rulings and baselines
    of the source-coverage checks (COVERAGE) and the twin declarations (DECLARED), byte for byte, and those of
    the input-quote check (KEYED_BY_YEAR), with the year in a parameter's key moved to the to-year. A coverage
    ruling is keyed by its finding and a baseline entry holds only while its finding's subject hashes as recorded
    (baseline_check.py), so a carried entry comes due where the to-year changed what it rests on; a declared
    twin difference the year's operations changed is reported by check_twins.py, to be restated. Returns a
    line per file copied."""
    f, t = str(f), str(t)
    out = []
    src, dst = ypath("reviews", f), ypath("reviews", t)
    for name in ("citations",) + COVERAGE + KEYED_BY_YEAR + DECLARED:
        if not (src / f"{name}.json").exists() or (dst / f"{name}.json").exists():
            continue
        dst.mkdir(parents=True, exist_ok=True)
        if name == "citations":
            data = json.loads((src / f"{name}.json").read_text(encoding="utf-8"))
            for r in data.get("anchors", []) + data.get("quotes", []):
                r["status"] = f"carried from {f}"
            (dst / f"{name}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
        elif name in KEYED_BY_YEAR:
            data = json.loads((src / f"{name}.json").read_text(encoding="utf-8"))
            moved = lambda k: re.sub(rf"^([\w-]+:){f}:", rf"\g<1>{t}:", k)
            for part in ("rulings", "baseline"):
                data[part] = {moved(k): v for k, v in (data.get(part) or {}).items()}
            (dst / f"{name}.json").write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
        else:
            shutil.copyfile(src / f"{name}.json", dst / f"{name}.json")
        out.append(f"carried {(dst / f'{name}.json').relative_to(ROOT)} from {f}")
    return out


def carry_contracts(f, t):
    """Copy the from-year's input and adapter contract banks (CONTRACT_BANKS) to the to-year, with their
    tax_year moved, never over an existing file. An input bank keeps its source snapshot (each cited
    document's text_sha256): a to-year edition whose text differs makes the bank's loader refuse it as stale,
    which asks for the cases to be reviewed against the new text. Returns a line per bank copied."""
    f, t = str(f), str(t)
    out = []
    for bank in CONTRACT_BANKS:
        top = ROOT / "tools" / "transcription" / bank / ("ny" if jurisdiction.NY else "")
        for p in sorted((top / f).glob("*.json")):
            q = top / t / p.name
            if q.exists():
                continue
            data = json.loads(p.read_text(encoding="utf-8"))
            if data.get("tax_year") != int(f):
                sys.exit(f"adopt: {p.relative_to(ROOT)} names tax_year {data.get('tax_year')}, not {f}")
            data["tax_year"] = int(t)
            q.parent.mkdir(parents=True, exist_ok=True)
            q.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            out.append(f"carried {q.relative_to(ROOT)} from {f}"
                       + (f" (its source snapshot is checked against the {t} archive)" if data.get("sources") else ""))
    return out


def carry_self_test():
    """carry_reviews and carry_contracts in a scratch tree: each file is copied, the citation rulings marked,
    a coverage file byte for byte, a bank's tax_year moved; nothing is copied over an existing file. Exits 1
    otherwise."""
    import tempfile
    global ROOT, ypath
    saved = ROOT, ypath
    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        ROOT = Path(tmp)
        ypath = lambda top, year, *rest: ROOT.joinpath(top, *(["ny"] if jurisdiction.NY else []), str(year), *rest)
        try:
            (ypath("reviews", 2025)).mkdir(parents=True)
            (ypath("reviews", 2025) / "citations.json").write_text(json.dumps({"anchors": [{"id": "a"}], "quotes": []}))
            coverage = '{\n  "rulings": {"operands:x": "why"},\n  "baseline": {"operands:y": "0123456789abcdef"}\n}\n'
            (ypath("reviews", 2025) / "operands.json").write_text(coverage)
            (ypath("reviews", 2025) / "twins.json").write_text('{"sides": ["person", "dependent"]}\n')
            (ypath("reviews", 2025) / "input_quotes.json").write_text(json.dumps(
                {"rulings": {}, "baseline": {"input-quote:2025:p.x d \u201cq\u201d": "h", "input-quote:t:t d \u201c2025\u201d": "g"}}))
            bank = ROOT / "tools" / "transcription" / "input_contracts" / ("ny" if jurisdiction.NY else "") / "2025"
            bank.mkdir(parents=True)
            (bank / "x.json").write_text(json.dumps({"form": "x", "tax_year": 2025, "sources": [{"doc": "d", "text_sha256": "s"}]}))
            lines = carry_reviews(2025, 2026) + carry_contracts(2025, 2026)
            cit = json.loads((ypath("reviews", 2026) / "citations.json").read_text())
            if cit["anchors"][0].get("status") != "carried from 2025":
                bad.append("citation ruling not marked carried")
            if (ypath("reviews", 2026) / "operands.json").read_text() != coverage:
                bad.append("coverage rulings and baseline not copied byte for byte")
            if not (ypath("reviews", 2026) / "twins.json").exists():
                bad.append("twin declarations not carried")
            quotes = json.loads((ypath("reviews", 2026) / "input_quotes.json").read_text())["baseline"]
            if quotes != {"input-quote:2026:p.x d \u201cq\u201d": "h", "input-quote:t:t d \u201c2025\u201d": "g"}:
                bad.append(f"input-quote baseline carried as {quotes}")
            moved = json.loads((bank.parent / "2026" / "x.json").read_text())
            if moved["tax_year"] != 2026 or moved["sources"] != [{"doc": "d", "text_sha256": "s"}]:
                bad.append(f"contract bank not carried with its year moved and its snapshot kept: {moved}")
            if len(lines) != 5:
                bad.append(f"{len(lines)} files reported carried, not 5")
            (ypath("reviews", 2026) / "operands.json").write_text("{}")
            if carry_reviews(2025, 2026) + carry_contracts(2025, 2026) or (ypath("reviews", 2026) / "operands.json").read_text() != "{}":
                bad.append("copied over an existing to-year file")
        finally:
            ROOT, ypath = saved
        # A carried baseline entry holds where adoptions only moved the year's marks, however many, and comes due on any
        # other change.
        import baseline_check as B
        line = lambda year, text: {"id": "x.l", "cite": {"tax_year": year, "locator": f"Form X ({year}), line 1"}, "text": text}
        finding = lambda year, text: {"kind": "k", "line": "x.l", "form": "x", "detail": "d", "subject": B.line_subject(line(year, text))}
        import contextlib, io
        outcomes = []
        for year, text in ((2026, "a"), (2026, "b"), (2027, "a"), (2027, "b"), (2025 + B.YEARS_BACK + 1, "a")):
            rulings = Path(tmp) / "baseline" / str(year) / "k.json"
            rulings.parent.mkdir(parents=True, exist_ok=True)
            rulings.write_text(json.dumps({"rulings": {}, "baseline": {"k:x.l": B.subject_hash(finding(2025, "a"), {})}}))
            with contextlib.redirect_stdout(io.StringIO()):
                outcomes.append(B.run("k", [], [finding(year, text)], rulings, Path(tmp) / "r.md", "t", "l"))
        if outcomes != [0, 1, 0, 1, 1]:
            bad.append(f"carried baseline entry: year marks moved one year, text changed, marks moved two years, two "
                       f"years and text changed, beyond YEARS_BACK: {outcomes} (want 0, 1, 0, 1, 1)")
    print("year-diff self-test: adoption carries review rulings, baselines, twin declarations and contract banks: "
          + ("as expected" if not bad else "WRONG: " + "; ".join(bad)))
    return 1 if bad else 0


# ---------- self-test ----------

SELF_TEST_DOC = "i8889"


def self_test(year):
    """Build an earlier year from this year's text of one document and diff against it:
    with only its years moved there must be no finding on the worklist; with a cited
    amount changed, a cited quote removed and a cited heading renamed, each must be
    found; nor may the IRS draft watermarks make a finding. Then the other way round,
    as after --adopt: this year's definitions read against a later year built the
    same way, where a changed amount and a removed quote that names the year must be
    found. Exits 1 otherwise."""
    import tempfile
    A = C.Archive(year)
    doc = SELF_TEST_DOC
    d = A.docs[doc]
    pages = [C.norm(p) for p in A.read(doc, "cols_file" if "cols_file" in d else "text_file").split("\f")]
    values = param_values(year)
    cited = [(kind, ident, seg) for kind, ident, _, cdoc, loc in carriers(year) for seg in all_segments(cdoc, loc) if seg[0] == doc and seg[1]]
    text = "\f".join(pages)
    value = next(((ident, t) for kind, ident, (_, pp, _, _) in cited if kind == "parameter"
                  for t in money_texts(values.get(ident)) if any(printed(t, pages[p - 1]) for p in pp)), None)
    quote = next(((kind, ident, C.parts_of(qs[0])[0]) for kind, ident, (_, _, _, qs) in cited if qs and C.parts_of(qs[0])
                  and C.parts_of(qs[0])[0] in text and len(C.parts_of(qs[0])[0]) > 30), None)
    heading = next(((kind, ident, k) for kind, ident, (_, _, anchor, qs) in cited if not qs
                    for k in C.anchor_keys(anchor)[:1] if len(" ".join(k)) > 12 and all(p in text for p in k)), None)
    if not (value and quote and heading):
        sys.exit(f"year-diff self-test: {doc} lacks a cited amount, quote or heading to plant")

    year_quote = next(((kind, ident, C.parts_of(qs[0])[0]) for kind, ident, (_, _, _, qs) in cited if qs and C.parts_of(qs[0])
                       and C.parts_of(qs[0])[0] in text and str(year) in C.parts_of(qs[0])[0]), None)

    def diff(edit, draft=False, adopted=False):
        with tempfile.TemporaryDirectory() as tmp:
            body = year_shifted("\f".join(edit(p) for p in pages), 1 if adopted else -1)
            if draft:  # the IRS draft watermarks, inside sentences, on every page
                body = "\f".join(p.replace(". ", ". DRAFT \u2014 DO NOT FILE ", 3) + " TREASURY/IRS AND OMB USE ONLY DRAFT"
                                 for p in body.split("\f"))
            (Path(tmp) / f"{doc}.cols.txt").write_text(body, encoding="utf-8")
            (Path(tmp) / "manifest.json").write_text(json.dumps({"documents": [{**d, "cols_file": f"{doc}.cols.txt", "draft": draft}]}))
            if adopted:
                r = run(year, year + 1, year + 1, archives={year: A, year + 1: C.Archive(sources=tmp)}, only=doc, definitions=year)
            else:
                r = run(year - 1, year, year, archives={year: A, year - 1: C.Archive(sources=tmp)}, only=doc)
        return {(e["kind"], e["id"]): {f["strength"] for f in e["findings"]} & REVIEW for e in r["items"]}

    status = 0
    baseline = {k: v for k, v in diff(lambda p: p).items() if v}
    if baseline:
        status = 1
        print(f"year-diff self-test: with only the years moved, {len(baseline)} item(s) were flagged: {sorted(baseline)[:5]}")
    bumped = f"{int(value[1].split('.')[0].replace(',', '')) + 1:,}"
    heading_text = " ".join(heading[2])
    planted = diff(lambda p: p.replace(value[1], bumped).replace(quote[2], "").replace(heading_text, "renamed heading"))
    expect = [(("parameter", value[0]), "value"), ((quote[0], quote[1]), "quote"), ((heading[0], heading[1]), "heading")]
    for key, strength in expect:
        ok = strength in planted.get(key, set())
        status = status or (0 if ok else 1)
        print(f"year-diff self-test: {strength} planted for {key[0]} {key[1]}: {'found' if ok else 'MISSED'}")
    if not baseline:
        print(f"year-diff self-test: {doc} with only its years moved: nothing on the worklist")
    # The sentence printing the cited amount reworded, the amount kept: not a value change.
    reworded = diff(lambda p: p.replace(value[1], value[1] + " (reworded)"))
    ok = "value" not in reworded.get(("parameter", value[0]), set())
    status = status or (0 if ok else 1)
    print(f"year-diff self-test: the sentence printing {value[0]}'s amount reworded, the amount kept: "
          + ("no value finding" if ok else "WRONG, a value finding"))
    # A small amount is looked for with its dollar sign, not as a bare number.
    small = [("5", "enter the amount from line 5", False), ("5", "multiply line 3 by $5", True),
             ("400", "see page 400 of pub. 17", False), ("400", "less than $400", True),
             ("15,750", "15,750", True)]
    bad = [(a, s) for a, s, want in small if printed(a, s) != want]
    status = status or (1 if bad else 0)
    print("year-diff self-test: small amounts read only with their dollar sign: "
          + ("as expected" if not bad else f"WRONG for {bad}"))
    # The classed year-literal list: every year outside a citation, years of birth beside the age parameters.
    status = self_test_literals() or status
    # Adoption extends the year-valued enums and re-derives recovery_year, by rule.
    status = status or self_test_year_rules()
    # An abbreviation's period does not end a sentence: the text is compared lower-cased.
    split = C.split_sentences(C.norm("See Pub. 946 and Rev. Proc. 2024-40; a U.S. person, Form No. 15. Is it? No. Stop."),
                              ends=".!?:;")
    want = ["see pub. 946 and rev. proc. 2024-40;", "a u.s. person, form no. 15.", "is it?", "no.", "stop."]
    status = status or (0 if split == want else 1)
    print("year-diff self-test: sentences split past abbreviations: " + ("as expected" if split == want else f"WRONG {split}"))
    watermarked = {k: v for k, v in diff(lambda p: p, draft=True).items() if v}
    if watermarked:
        status = 1
        print(f"year-diff self-test: as an IRS draft with watermarks, {len(watermarked)} item(s) were flagged: {sorted(watermarked)[:5]}")
    else:
        print(f"year-diff self-test: {doc} as an IRS draft with watermarks: nothing on the worklist")
    carried = {k: v for k, v in diff(lambda p: p, adopted=True).items() if v}
    if carried:
        status = 1
        print(f"year-diff self-test: as after --adopt, with only the years moved, {len(carried)} item(s) were flagged: {sorted(carried)[:5]}")
    if not year_quote:  # a carried year's quotes name the earlier year and are not printed in its text
        print(f"year-diff self-test: as after --adopt, no cited quote of {doc} names {year} and is printed; quote not planted")
    planted = diff(lambda p: p.replace(value[1], bumped).replace(year_quote[2] if year_quote else "\0", ""), adopted=True)
    expect = [(("parameter", value[0]), "value")] + ([((year_quote[0], year_quote[1]), "quote")] if year_quote else [])
    for key, strength in expect:
        ok = strength in planted.get(key, set())
        status = status or (0 if ok else 1)
        print(f"year-diff self-test: as after --adopt, {strength} planted for {key[0]} {key[1]}: {'found' if ok else 'MISSED'}")
    return status


def self_test_literals():
    """Plant each class of year literal in a copied form and its parameters, and check the classed list."""
    import tempfile
    params = ("params:\n  tax_year: 2025\n  values:\n    age.cut_65:\n      type: Count\n      value: 1961\n"
              "    age.cut_50:\n      type: Count\n      value: 1976\n      moves_with_year: 1\n"
              "    age.birth_year_latest:\n      type: Count\n      value: 2025\n"
              "    sa.rate:\n      type: Count\n      value: 1936\n")
    form = "\n".join([
        "form:",
        "  id: fx",
        "  tax_year: 2025",                                                         # 3 converted by the copy: not listed
        "  lines:",
        "  - id: fx.old",
        "    label: Born before January 2, 1961",                                   # 6 birth_cutoff (age.cut_65)
        "    cite:",
        "      doc: i1040gi",
        "      locator: 'p. 33, Line 12d, \"born before January 2, 1961, or were blind at the end",
        "        of 2025, check the box\"'",                                       # 10 a citation's continuation: not listed
        "  - id: fx.prior",
        "    label: Was more put into your HSA for 2024, or will be in 2026?",      # 12 adjacent_year 2024, 2026
        "  - id: fx.young",
        "    label: Number of people born after December 31, 1960, and before",
        "      January 2, 2001, on the return",                                      # 15 continuation, other_year (no param)
        "  - id: fx.lump",
        "    label: Born before January 2, 1936?",                                  # 17 other_year: a fixed birth date
        "  - id: fx.gift",
        "    help: For a gift after 1976, add the gift tax paid.",                  # 19 other_year: 1976 without a birth
        "  - id: fx.otjob",
        "    note: figured by the methods of Notice 2025-69 and amb.2025.otjob for $2,024.",  # 21 fixed_reference, year_id
        "  - id: fx.cutline",
        "    source: |-",
        "      Were you born in 1976?",                                              # 24 block scalar: birth_cutoff (cut_50)
        "      - The child was born in 2024 (a child born in 2025 counts).",         # 25 adjacent (2024 not a cut-off)
        "  - id: fx.died_2025",                                                     # 26 year_id
        ""])
    with tempfile.TemporaryDirectory() as tmp:
        src, dst, pf = Path(tmp) / "fx.yaml", Path(tmp) / "fx.2026.yaml", Path(tmp) / "params.yaml"
        src.write_text(form, encoding="utf-8")
        dst.write_text(form.replace("tax_year: 2025", "tax_year: 2026"), encoding="utf-8")
        pf.write_text(params, encoding="utf-8")
        recs = {x["line"]: x for x in year_literal_report([(src, dst)], 2025, 2026, pf)}
        own = {x["text"]: x["classes"] for x in year_literal_report([(pf, pf)], 2025, 2026, pf)}
    want = {6: ({"birth_cutoff": [1961]}, "label: Born before January 2, 1962"),
            12: ({"adjacent_year": [2024, 2026]}, "label: Was more put into your HSA for 2025, or will be in 2027?"),
            14: ({"birth_cutoff": [1960]}, "label: Number of people born after December 31, 1961, and before"),
            15: ({"other_year": [2001]}, None),
            17: ({"other_year": [1936]}, None),
            19: ({"other_year": [1976]}, None),
            21: ({"year_id": [2025], "fixed_reference": [2025]}, None),
            24: ({"birth_cutoff": [1976]}, "Were you born in 1977?"),
            25: ({"from_year": [2025], "adjacent_year": [2024]}, "- The child was born in 2025 (a child born in 2026 counts)."),
            26: ({"year_id": [2025]}, None)}
    got = {n: (x["classes"], x.get("moved")) for n, x in recs.items()}
    # the age parameters' own values are years of birth; another parameter's value that looks like a year is not
    ok = own.get("value: 1961") == {"birth_cutoff": [1961]} and own.get("value: 1936") == {"other_year": [1936]}
    ok = ok and got == want and recs[6].get("age_params") == ["age.cut_65"] and recs[24]["age_params"] == ["age.cut_50"]
    print("year-diff self-test: the classed year-literal list (a copied tax_year and a citation's continuation not "
          "listed; adjacent years, years of birth beside the age parameters, fixed birth dates, document numbers and "
          "ids classed; candidates moved; the age parameters' own values): " + ("as expected" if ok else f"WRONG {own}\n" + "\n".join(
              f"  line {n}: got {got.get(n)}, want {want.get(n)}" for n in sorted(set(got) | set(want)) if got.get(n) != want.get(n))))
    return 0 if ok else 1


def self_test_year_rules():
    import tempfile
    params = ("params:\n  tax_year: 2025\n  values: {}\n  enums:\n    placed_year:\n      values: [y2024, y2025]\n"
              "      extends_with_year: true\n      cite: {doc: p946, locator: p. 39}\n"
              "    quarter:\n      values: [q1, y2025]\n      cite: {doc: p946, locator: p. 41}\n")
    text, done = extend_year_enums(params, 2025, 2026)
    e = yaml.safe_load(text)["params"]["enums"]
    ok = done == ["placed_year"] and e["placed_year"]["values"] == ["y2024", "y2025", "y2026"] and e["quarter"]["values"] == ["q1", "y2025"]
    ok = ok and extend_year_enums(text, 2025, 2026)[1] == []  # already extended: left
    try:
        extend_year_enums(params.replace("[y2024, y2025]", "[y2023, y2024]"), 2025, 2026)
        ok = False
    except ValueError:
        pass
    table = ("# The 2025 year of recovery, each row 2025 less the year placed in service, plus 1.\ntable:\n  id: recovery_year\n"
             "  title: \"Year of recovery in 2025\"\n  cite:\n    locator: \"p. 39, sold March 2, 2025\"\n  rows:\n"
             "    - { keys: [y2025], value: 1 }\n    - { keys: [y2024], value: 2 }\n")
    out = extend_recovery_year(table, 2025, 2026)
    t = yaml.safe_load(out)["table"]
    ok = ok and [(r["keys"][0], r["value"]) for r in t["rows"]] == [("y2026", 1), ("y2025", 2), ("y2024", 3)]
    ok = ok and t["title"] == "Year of recovery in 2026" and "sold March 2, 2025" in out and out.startswith("# The 2026 year")
    try:
        extend_recovery_year(table.replace("[y2024], value: 2", "[y2024], value: 3"), 2025, 2026)
        ok = False
    except ValueError:
        pass
    print("year-diff self-test: adoption extends enums declared extends_with_year and re-derives recovery_year "
          "(a from-year row off the rule refused): " + ("as expected" if ok else f"WRONG\n{text}\n{out}"))
    status = 0 if ok else 1
    # The questions asking an extended enum gain the year's label, first; a question with other labels is refused.
    form = {"form": {"id": "x", "lines": [{"id": "x.placed", "type": "Enum(placed_year)"}, {"id": "x.q", "type": "Enum(quarter)"}]}}
    bank = ("bank:\n  questions:\n  - input: x.q\n    value_labels:\n      q1: 'Q1'\n      y2025: '2025'\n"
            "  - input: x.placed\n    order: 1\n    value_labels:\n      y2025: '2025'\n      y2024: '2024'\n  - input: x.other\n")
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "x.yaml").write_text(yaml.safe_dump(form))
        _, ext, btext, labelled = year_enum_rules(params, tmp, bank, 2025, 2026)
        qs = {q["input"]: q.get("value_labels") for q in yaml.safe_load(btext)["bank"]["questions"]}
        ok = labelled == ["x.placed"] and list(qs["x.placed"].items()) == [("y2026", "2026"), ("y2025", "2025"), ("y2024", "2024")]
        ok = ok and qs["x.q"] == {"q1": "Q1", "y2025": "2025"} and btext.replace("      y2026: '2026'\n", "", 1) == bank
        for wrong in (bank.replace("y2024: '2024'", "y2024: 'last year'"), bank.replace("      y2024: '2024'\n", "")):
            try:
                year_enum_rules(params, tmp, wrong, 2025, 2026)
                ok = False
            except ValueError:
                pass
        # an enum with a member that is not a year: the year members follow the rule, the other keeps its label
        nparams = params.replace("[y2024, y2025]", "[before2024, y2024, y2025]")
        nbank = bank.replace("      y2024: '2024'\n", "      y2024: '2024'\n      before2024: Before 2024\n")
        _, _, nbtext, nlabelled = year_enum_rules(nparams, tmp, nbank, 2025, 2026)
        nqs = {q["input"]: q.get("value_labels") for q in yaml.safe_load(nbtext)["bank"]["questions"]}
        ok = ok and nlabelled == ["x.placed"] and list(nqs["x.placed"]) == ["y2026", "y2025", "y2024", "before2024"]
        ok = ok and nqs["x.placed"]["before2024"] == "Before 2024"
        try:
            year_enum_rules(nparams, tmp, nbank.replace("y2024: '2024'", "y2024: 'last year'"), 2025, 2026)
            ok = False
        except ValueError:
            pass
    print("year-diff self-test: adoption labels the extended year in the value_labels of the questions asking that enum "
          "(other questions untouched; a non-year member keeps its label; labels off the rule refused): "
          + ("as expected" if ok else f"WRONG\n{btext}"))
    status = status or (0 if ok else 1)
    # Adoption copies every definition file the year operations read, subdirectories of interview/<year>/ included.
    import year_changes
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel, body in (("forms/2025/x.yaml", "form:\n  id: x\n  tax_year: 2025\n  lines: []\n"),
                          ("interview/2025/questions.yaml", "bank:\n  questions: []\n"),
                          ("interview/2025/full.yaml", "interview:\n  questions: []\n"),
                          ("interview/2025/coverage/c.yaml", "cover: (2025)\n"),
                          ("interview/2025/personas/p/q.yaml", "interview:\n  tax_year: 2025\n  questions: []\n")):
            (root / rel).parent.mkdir(parents=True, exist_ok=True)
            (root / rel).write_text(body)
        pairs = [(root / "forms/2025", root / "forms/2026"), (root / "interview/2025", root / "interview/2026")]
        files = definition_files(pairs)
        tree = year_changes.Tree(root / "forms/2025", root / "interview/2025", root / "params.yaml")
        missed = unplanned_definitions(files, tree, root / "interview/2025")
        shallow = [(p, q) for p, q in files if p.parent.name in ("2025",)]
        refused = unplanned_definitions(shallow, tree, root / "interview/2025")
        copy_definitions(files, 2025, 2026)
        got = sorted(str(p.relative_to(root)) for p in (root / "interview/2026").rglob("*.yaml"))
        ok = (not missed and len(refused) == 2 and got == ["interview/2026/coverage/c.yaml", "interview/2026/full.yaml",
              "interview/2026/personas/p/q.yaml", "interview/2026/questions.yaml"]
              and (root / "interview/2026/coverage/c.yaml").read_text() == "cover: (2026)\n"
              and "tax_year: 2026" in (root / "interview/2026/personas/p/q.yaml").read_text())
    print("year-diff self-test: adoption copies the interview subdirectories (a copy of the top level only refused "
          "before anything is written): " + ("as expected" if ok else f"WRONG: missed {missed}, refused {refused}, copied {got}"))
    return status or (0 if ok else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="from_year", type=int)
    ap.add_argument("--to", dest="to_year", type=int)
    ap.add_argument("--data", dest="data_year", type=int, help="whose definitions' citations to read (default --from; --to after --adopt)")
    ap.add_argument("--adopt", action="store_true")
    ap.add_argument("--self-test", action="store_true", help="the synthetic check run by check-all (uses --to's archive)")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(max(self_test(a.to_year or int(C.Y)), carry_self_test()))
    if a.from_year is None or a.to_year is None:
        ap.error("--from and --to are required")
    data = a.data_year or a.from_year
    if a.adopt:
        adopt(a.from_year, a.to_year)
        data = a.to_year
    if data not in (a.from_year, a.to_year):
        sys.exit("--data must be --from or --to")
    write_report(run(a.from_year, a.to_year, data))


if __name__ == "__main__":
    main()
