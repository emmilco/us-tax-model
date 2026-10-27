#!/usr/bin/env python3
"""The year-diff (design Stage 6): which of one year's definitions rest on IRS text
that is different in another year.

    year_diff.py --from 2025 --to 2026              the report, reports/2026/year_diff_from_2025.{md,html}
    year_diff.py --from 2025 --to 2026 --adopt      first copy the 2025 definitions to 2026 (see adopt)

The citations of the data year (--data, by default --from: the year whose
definitions exist) are read against both years' archived text. Each archived PDF
is split into sentences of its reading-order text, and the two years' sentences
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
    earlier year's catalog, tools/sources-<year>.json).

Findings are grouped by what carries the citation: form line, refusal, collection,
parameter, table, ambiguity register entry, interview question. A parameter whose
value is printed in a changed sentence near its citation is flagged as a probable
value change. Tables are reported by their pages; their cells need re-extraction.
Nothing is changed: the report points, a person decides.

--adopt lists every line of the copied definitions that still names the from-year
outside a citation (a year constant such as "y2025") on the worklist, and copies
the from-year's definitions (forms, tables, parameters, register,
interview, and the citation rulings, marked "carried" for review) to the to-year
with tax_year and the year in file names and in
"(<year>)" form citations replaced, relocates their page numbers against the
to-year's archive (tools/citations.py --relocate), and then reports with the
to-year as the data year. It refuses to overwrite an existing year.
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
    """[(page, normalized sentence)] of a PDF's reading-order text, its years moved by
    `shift` (the text as printed is kept in .printed[(page, sentence)])."""
    out = []
    d = arch.docs[doc]
    pages = arch.read(doc, "cols_file" if "cols_file" in d else "text_file").split("\f")
    for n, page in enumerate(pages, 1):
        for s in re.split(r"(?<=[.!?:;])\s+(?=\S)", C.norm(page)):
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
    for path in sorted((ROOT / "forms" / y).glob("*.yaml")):
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        doc = raw.get("form") or raw.get("def")
        if doc.get("collection"):
            add("collection", doc["id"], path, doc["collection"].get("cite"))
        for line in doc.get("lines", []):
            add("line", line["id"], path, line.get("cite"))
            for r in line.get("refuses", []) or []:
                add("refusal", line["id"], path, r.get("cite"))
    for path in sorted((ROOT / "tables" / y).glob("*.yaml")):
        t = yaml.safe_load(path.read_text(encoding="utf-8"))["table"]
        add("table", t["id"], path, t.get("cite"))
    p = ROOT / "params" / f"{y}.yaml"
    if p.exists():
        params = yaml.safe_load(p.read_text(encoding="utf-8"))["params"]
        for name, v in params.get("values", {}).items():
            add("parameter", name, p, v.get("cite"))
        for name, v in params.get("enums", {}).items():
            add("enum", name, p, v.get("cite"))
    p = ROOT / "ambiguities" / f"{y}.yaml"
    if p.exists():
        for e in yaml.safe_load(p.read_text(encoding="utf-8"))["register"]["entries"]:
            add("ambiguity", e["id"], p, e.get("cite"))
    p = ROOT / "interview" / f"questions-{y}.yaml"
    if p.exists():
        for q in yaml.safe_load(p.read_text(encoding="utf-8"))["bank"]["questions"]:
            add("question", q["input"], p, q.get("cite"))
    return out


def param_values(year):
    """Dollar-amount parameters' values (rates and counts are not looked for in the text)."""
    p = ROOT / "params" / f"{year}.yaml"
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
    """Whether an amount ("22,937") is printed in a sentence as itself or with zero cents."""
    return re.search(rf"(?<![\d,.]){re.escape(amount)}(?:\.00)?(?![\d]|[.,]\d)", sentence) is not None


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
    cat = ROOT / "tools" / f"sources-{early}.json"
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
        elif doc not in A.docs or not A.docs[doc]["file"].endswith(".pdf"):
            alignments[doc] = None
            doc_state[doc] = "not compared (no PDF text)"
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
                    hits = [i for i in cited if printed(text, al.a[i][1]) and al.changed(i)]
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
    out_dir = ROOT / "reports" / str(r["to"])
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
    literals_file = ROOT / "reports" / str(r["to"]) / f"year_literals_from_{r['from']}.json"
    if r["data"] == r["to"] and literals_file.exists():
        literals = json.loads(literals_file.read_text())
        lines += [f"### Definitions that still name {r['from']} ({len(literals)})", ""]
        lines += [f"- `{p}:{n}`: {text[:160]}" for p, n, text in literals] + [""]
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

def adopt(from_year, to_year):
    """Copy the from-year definitions to the to-year (refusing to overwrite), with the
    year replaced where it names the year, and relocate their pages."""
    f, t = str(from_year), str(to_year)
    pairs = [(ROOT / "forms" / f, ROOT / "forms" / t), (ROOT / "tables" / f, ROOT / "tables" / t),
             (ROOT / "params" / f"{f}.yaml", ROOT / "params" / f"{t}.yaml"),
             (ROOT / "ambiguities" / f"{f}.yaml", ROOT / "ambiguities" / f"{t}.yaml")]
    pairs += [(p, p.with_name(p.name.replace(f, t))) for p in sorted((ROOT / "interview").glob(f"*{f}.yaml"))]
    clash = [str(dst.relative_to(ROOT)) for _, dst in pairs if dst.exists()]
    if clash:
        sys.exit("adopt: refusing to overwrite " + ", ".join(clash))
    if not (ROOT / "sources" / t / "manifest.json").exists():
        sys.exit(f"adopt: archive the {t} sources first (tools/fetch_sources.py --year {t} --fetch)")

    def convert(text):
        text = re.sub(rf"(?m)^(\s*tax_year:\s*){f}\b", rf"\g<1>{t}", text)
        return re.sub(rf"\((?:Rev\. )?{f}\)", f"({t})", text)

    for src, dst in pairs:
        if src.is_dir():
            dst.mkdir(parents=True)
            for p in sorted(src.glob("*.yaml")):
                (dst / p.name).write_text(convert(p.read_text(encoding="utf-8")), encoding="utf-8")
        elif src.exists():
            dst.write_text(convert(src.read_text(encoding="utf-8")), encoding="utf-8")
    rulings = ROOT / "reviews" / f / "citations.json"
    if rulings.exists() and not (ROOT / "reviews" / t / "citations.json").exists():
        data = json.loads(rulings.read_text())
        for r in data.get("anchors", []) + data.get("quotes", []):
            r["status"] = f"carried from {f}"
        (ROOT / "reviews" / t).mkdir(parents=True, exist_ok=True)
        (ROOT / "reviews" / t / "citations.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    literals = []
    for _, dst in pairs:
        for p in (sorted(dst.glob("*.yaml")) if dst.is_dir() else [dst]):
            for n, line in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
                if re.search(rf"(?<!\d){f}(?!\d)", line) and not re.search(r"\b(locator|quote):", line):
                    literals.append((str(p.relative_to(ROOT)), n, line.strip()))
    (ROOT / "reports" / t).mkdir(parents=True, exist_ok=True)
    (ROOT / "reports" / t / f"year_literals_from_{f}.json").write_text(json.dumps(literals, indent=1) + "\n")
    print(f"adopt: {len(literals)} line(s) of the {t} definitions still name {f} outside citations "
          f"(reports/{t}/year_literals_from_{f}.json); each is on the worklist")
    print(f"adopt: copied the {f} definitions (and citation rulings, to be reviewed again) to {t}; "
          f"relocating page numbers against the {t} archive")
    subprocess.run([sys.executable, str(ROOT / "tools" / "citations.py"), "--relocate", "--year", t], check=True)


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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="from_year", type=int)
    ap.add_argument("--to", dest="to_year", type=int)
    ap.add_argument("--data", dest="data_year", type=int, help="whose definitions' citations to read (default --from; --to after --adopt)")
    ap.add_argument("--adopt", action="store_true")
    ap.add_argument("--self-test", action="store_true", help="the synthetic check run by check-all (uses --to's archive)")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test(a.to_year or int(C.Y)))
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
