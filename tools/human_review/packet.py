#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""One HTML packet per reading-list item for a person to judge the project's printed lines
against the archived IRS pages (integrity plan items 1.0 and 1.1).

Right pane, one card per printed line: the IRS label as printed, the citation's quotes, the
reading English (reading.py: what the encoding computes, in page terms, every helper it reads
folded in), the refusal gates, a worked example from the fixtures (examples.py), the YAML
expression under a collapsed toggle, and the verdict box. Left pane: the pages that line's own
citation and its folded helpers' citations name (pages.py), the cited words highlighted.
A listed helper is never judged on its own: it is folded into the printed line that reads it,
or, when no printed line on the list reads it, into the nearest printed line that does; a
listed helper no chosen printed line reads is shown at the end without a verdict box.
Verdicts are saved by serve.py.

Writes the git-ignored .human-review/<item>.html (and index.html); page images are shared
under .human-review/pages/, highlighted copies under .human-review/pages/hl/.

    packet.py --item N        one packet
    packet.py --all           every item and the index
    packet.py --list          the items, their line and page counts, and nothing written
"""
import argparse
import datetime
import html
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from taxyear import Y  # noqa: E402
import citations as C  # noqa: E402
import examples  # noqa: E402
import pages as P  # noqa: E402
import reading as R  # noqa: E402

ARCHIVE = ROOT / "sources" / Y
OUT = ROOT / ".human-review"
VERDICTS = ("MATCH", "MISMATCH", "UNCLEAR")

STYLE = """
body{margin:0;font:15px/1.5 -apple-system,Helvetica,Arial,sans-serif;color:#222}
header{display:flex;flex-wrap:wrap;gap:1em;align-items:center;padding:.6em 1em;border-bottom:1px solid #ddd;background:#fafafa;position:sticky;top:0;z-index:2}
header a{color:#1a4f8b;text-decoration:none}
header input{font:inherit;padding:.25em .5em}
header button{font:inherit;padding:.3em .9em}
#status{color:#555}
main{display:grid;grid-template-columns:1fr 1fr;height:calc(100vh - 3.4em)}
.pane{overflow:auto;padding:1em;border-right:1px solid #ddd}
.pane img{width:100%;height:auto;border:1px solid #ccc}
.pages{display:none}.pages.active{display:block}
.pages>p.which{margin:0 0 .6em;color:#444}
.page h3{margin:1em 0 .3em;font-size:1em;color:#444}
.page .cited{font-size:.9em;color:#555;margin:.2em 0}
.page .located{font-size:.9em;margin:.3em 0 0}
.page .located .no{color:#a33}
.line{border:1px solid #ddd;border-radius:.4em;padding:.7em .9em;margin-bottom:1em;background:#fff}
.line.active{border-color:#1a4f8b;box-shadow:0 0 0 2px #cfe0f5}
.line h3{margin:0 0 .4em;font-size:1.1em}
.line h3 code{font-weight:normal;color:#666;font-size:.85em}
.line .reached{font-size:.9em;color:#555;margin:0 0 .5em}
.line .k{color:#666;font-size:.8em;text-transform:uppercase;letter-spacing:.03em;margin-top:.7em}
.line pre{white-space:pre-wrap;font:13px/1.45 Menlo,Consolas,monospace;margin:.2em 0;background:#f6f6f6;padding:.4em .6em;border-radius:.3em}
.line blockquote{margin:.3em 0;padding:.3em .8em;border-left:3px solid #ffd54a;background:#fffbe6}
.line .flag{background:#fdecea;border-left:3px solid #d33;padding:.3em .8em;margin:.3em 0}
.reading ul{margin:.2em 0 .2em 1.2em;padding:0}
.reading li{margin:.25em 0}
.reading>p{margin:.2em 0}
.tag{font-weight:600}
a.pg{color:#1a4f8b;text-decoration:none;white-space:nowrap}
.verdict{display:flex;gap:.6em;align-items:flex-start;margin-top:.8em}
.verdict select{font:inherit;padding:.25em}
.verdict textarea{font:inherit;flex:1;min-height:3.2em;padding:.3em .5em}
.line.done{border-color:#9c9}
details summary{cursor:pointer;color:#1a4f8b}
.orphans{border-top:2px solid #ddd;margin-top:1.5em;padding-top:.6em}
.example{background:#f3f7fb;padding:.4em .8em;border-radius:.3em}
@media (max-width:900px){main{grid-template-columns:1fr;height:auto}.pane{border-right:0}}
"""

SCRIPT = """
const ITEM=%(item)d, KEY='human-review-'+ITEM, FORM=document.getElementById('packet');
const lines=[...document.querySelectorAll('.line')];
function activate(ref){for(const l of lines)l.classList.toggle('active',l.dataset.ref===ref);
  for(const g of document.querySelectorAll('.pages'))g.classList.toggle('active',g.dataset.ref===ref);}
for(const l of lines){l.addEventListener('focusin',()=>activate(l.dataset.ref));l.addEventListener('click',()=>activate(l.dataset.ref));}
document.querySelectorAll('a.pg').forEach(a=>a.addEventListener('click',e=>{activate(a.dataset.ref);
  const t=document.getElementById(a.getAttribute('href').slice(1));if(t){e.preventDefault();t.scrollIntoView({block:'start'});}}));
function state(){return {item:ITEM,reader:document.getElementById('reader').value.trim(),date:document.getElementById('date').value,
  lines:lines.map(l=>({ref:l.dataset.ref,verdict:l.querySelector('select').value,reason:l.querySelector('textarea').value}))};}
function apply(saved){for(const s of saved.lines||[]){const l=lines.find(x=>x.dataset.ref===s.ref);if(!l)continue;
  if(s.verdict)l.querySelector('select').value=s.verdict;if(s.reason)l.querySelector('textarea').value=s.reason;}
  if(saved.reader)document.getElementById('reader').value=saved.reader;mark();}
function mark(){for(const l of lines)l.classList.toggle('done',!!l.querySelector('select').value);
  const n=lines.filter(l=>l.querySelector('select').value).length;document.getElementById('count').textContent=n+' of '+lines.length+' lines judged';}
function draft(){localStorage.setItem(KEY,JSON.stringify(state()));mark();}
FORM.addEventListener('input',draft);FORM.addEventListener('change',draft);
const say=t=>document.getElementById('status').textContent=t;
async function save(){const s=state();if(!s.reader){say('type your name as the reader first');return;}
  try{const r=await fetch('/api/verdicts',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(s)});
    const j=await r.json();say(r.ok?('saved: '+j.written.join(', ')):('not saved: '+(j.error||r.status)));}
  catch(e){say('not saved: no server (run tools/human_review/serve.py and open this page through it)');}}
document.getElementById('save').addEventListener('click',save);
(async()=>{let d=localStorage.getItem(KEY);if(d)apply(JSON.parse(d));
  try{const r=await fetch('/api/verdicts?item='+ITEM);if(r.ok){const j=await r.json();if(j.lines&&j.lines.length)apply(j);say('loaded the saved log');}}catch(e){}
  mark();if(lines.length)activate(lines[0].dataset.ref);})();
"""

esc = html.escape


def reading_list():
    return json.loads((HERE / "reading_list.json").read_text(encoding="utf-8"))


def item(n):
    for it in reading_list()["items"]:
        if it["id"] == n:
            return it
    sys.exit(f"no reading-list item {n}")


def manifest():
    m = json.loads((ARCHIVE / "manifest.json").read_text(encoding="utf-8"))
    return {d["id"]: d for d in m["documents"]}


_canon = None


def canon():
    global _canon
    if _canon is None:
        _canon = R.Canon()
    return _canon


def form_title(fid):
    if fid == "tax_table":
        return f"{Y} Tax Table"
    return canon().docs[fid]["title"]


def cite_text(cite):
    return f"[{cite.get('doc', '')}] {cite.get('locator', '')}" if cite else ""


def table_band(ref):
    """One Tax Table cell, read as a printed record of its own."""
    fid, _, rest = ref.partition(".")
    at_least = int(rest.split("_")[1])
    t = yaml.safe_load((ROOT / "tables" / Y / f"{fid}.yaml").read_text(encoding="utf-8"))["table"]
    band = next(b for b in t["bands"] if b["at_least"] == at_least)
    cols = [c["key"] for c in t["columns"]]
    tax = dict(zip(cols, band["tax"]))
    cite = t.get("cite", {})
    text = "; ".join(f"{R.STATUS_WORDS.get(k, k)} {R.dollars(v * 100) if v < 100000 else v}" for k, v in tax.items())
    return {"ref": ref, "form": fid, "id": rest, "printed": "Tax Table", "reached": "listed",
            "label": f"At least ${at_least:,} but less than ${band['less_than']:,}: the tax by filing status column",
            "reading": R.Node("The tax in this row, by filing status column: " + text), "reading_text": text,
            "cite": cite, "cite_text": cite_text(cite), "helpers": [], "leaves": [], "refusals": [],
            "expr": yaml.safe_dump(band, sort_keys=False).strip(), "example": {"none": "a table cell has no fixture example"},
            "rd": None}


def record(lid, rd, reached):
    c = canon()
    l = c.lines[lid]
    fid = c.form_of[lid]
    return {"ref": lid, "form": fid, "id": lid, "printed": str(l.get("printed", "")), "reached": reached,
            "label": str(l.get("label", "")), "reading": rd.node, "reading_text": rd.node.flat(),
            "cite": l.get("cite", {}), "cite_text": cite_text(l.get("cite", {})),
            "helpers": list(rd.helpers), "leaves": list(rd.leaves), "refusals": R.refusals(c, rd),
            "expr": yaml.safe_dump(l.get("expr"), sort_keys=False, allow_unicode=True, width=100).strip(), "rd": rd}


def plan_item(it):
    """The printed records the packet judges for an item and the listed helpers none reads."""
    refs = [r for r in it["lines"] if not r.startswith("tax_table.")]
    tables = [r for r in it["lines"] if r.startswith("tax_table.")]
    docs = {p["doc"] for p in it.get("pages", [])}
    printed, orphans = R.plan(canon(), refs, docs)
    recs = [record(lid, rd, how) for lid, rd, how in printed] + [table_band(r) for r in tables]
    listed = {canon().resolve(r) for r in refs}
    for rec in recs:
        # the citations folded into the line: its helpers', and those of listed inputs and parameters it names
        rec["folded_cites"] = [h for h in rec["helpers"]] + [x for x in rec["leaves"] if x in listed]
    return recs, orphans


def example_names(rd):
    """The phrase the example uses for each line the reading names."""
    c = canon()
    names = dict(rd.tags)
    for h in rd.helpers:
        if h not in names:
            hint = rd.hint(h)
            names[h] = f"“{hint}” ({h})" if hint else h
    for x in rd.leaves:
        k = c.kind(x)
        if k == "printed":
            names[x] = c.line_name(x).split(" (“")[0]
        elif k == "input":
            names[x] = f"“{c.question(x, bare=True)}”"
        elif k == "param":
            names[x] = f"parameter {c.lines[x]['expr']['ref']}"
    return names


def node_html(node):
    out = f"<p>{esc(node.text)}</p>"
    if node.kids:
        out += "<ul>" + "".join(f"<li>{node_html(k)}</li>" for k in node.kids) + "</ul>"
    return re.sub(r"\(([a-zA-Z])\)", r'<span class="tag">(\1)</span>', out)


def segments_html(cite, located, flags, ref):
    """The citation, segment by segment: its quotes verbatim, where it was placed, or why not."""
    parts = []
    for plain, quotes in C.split_top(cite.get("locator", "")):
        shown = re.sub("\x00", lambda _, it=iter(quotes): f"“{next(it)}”", plain.strip())
        parts.append(f"<div>{esc(shown)}</div>")
        for q in quotes:
            parts.append(f"<blockquote>{esc(q)}</blockquote>")
    for seg, why in flags:
        parts.append(f'<div class="flag">a citation folded into this line does not locate a page: <em>{esc(seg)}</em> — {esc(why)} '
                     f'(on a computed line such a locator is listed under “Locators to rewrite” in reports/{Y}/citations.md)</div>')
    links = " ".join(f'<a class="pg" data-ref="{esc(ref)}" href="#page-{esc(ref)}-{d}-{p}">{d} p. {p}</a>' for d, p in located)
    if links:
        parts.append(f"<div>pages: {links}</div>")
    return "".join(parts)


def example_html(ex, printed):
    if "none" in ex:
        return f'<div class="example">No worked example: {esc(ex["none"])}.</div>'
    because = "; ".join(f"{esc(n)} = {esc(v)}" for n, v in ex["reads"])
    return (f'<div class="example">Example (fixture {esc(ex["case"])}): line {esc(printed)} = <strong>{esc(ex["value"])}</strong> '
            f'because {because}.</div>')


def build(it, dpi, force=False):
    OUT.mkdir(parents=True, exist_ok=True)
    c = canon()
    docs = manifest()
    arch = C.Archive()
    loc = P.Locator(arch, dpi, force)
    recs, orphans = plan_item(it)
    left, right = [], []
    for rec in recs:
        ref = rec["ref"]
        slug = re.sub(r"[^A-Za-z0-9]+", "_", ref)
        # pages: the line's own citation, then its folded helpers' citations
        cites = [(ref, rec["cite"])] + [(h, c.lines[h].get("cite", {})) for h in rec.get("folded_cites", [])]
        page_marks, flags, cited_by, fallback_for = {}, {}, {}, {}
        for who, cite in cites:
            if not cite.get("doc"):
                continue
            label = str(c.lines[who].get("label", "")) if who in c.lines else rec["label"]
            printed = str(c.lines[who].get("printed", "")) if who in c.lines else ""
            found, bad = loc.locate(cite["doc"], cite.get("locator", ""), label, printed)
            for d, p, marks in found:
                have = page_marks.setdefault((d, p), [])
                for m in marks:
                    if not any(m[0] == h[0] and m[1] == h[1] and m[2] == h[2] for h in have):
                        have.append(m)
                cited_by.setdefault((d, p), []).append(who)
            for seg, why in bad:
                flags.setdefault((seg, why), []).append(who)
                for p in loc.fallback(cite["doc"]):
                    page_marks.setdefault((cite["doc"], p), [])
                    fallback_for.setdefault((cite["doc"], p), []).append(who)
        flags = [(f"{seg} (cited by {', '.join(dict.fromkeys(whos))})", why) for (seg, why), whos in flags.items()]
        ordered = sorted(page_marks, key=lambda k: (k[0] != rec["cite"].get("doc"), k[0], k[1]))
        group = [f'<div class="pages" data-ref="{esc(ref)}"><p class="which">Pages for line {esc(rec["printed"])} '
                 f'(<code>{esc(ref)}</code>)</p>']
        for d, p in ordered:
            marks = page_marks[(d, p)]
            png = loc.image(d, p, marks, slug)
            rel = png.relative_to(OUT).as_posix()
            rev = docs.get(d, {}).get("revision") or ""
            who = ", ".join(dict.fromkeys(cited_by.get((d, p), [])))
            if (d, p) in fallback_for:
                who += ("; " if who else "") + "offered as a fallback for " + ", ".join(dict.fromkeys(fallback_for[(d, p)])) + \
                       ", whose citations locate no page"
            notes = []
            for kind, text, found, rects in marks:
                what = {"quote": "quote", "heading": "heading", "line": "printed line"}[kind]
                if found:
                    notes.append(f'<li>highlighted {what}: “{esc(text)}”</li>')
                else:
                    notes.append(f'<li class="no">not located on this page (not highlighted): {what} “{esc(text)}”</li>')
            if not marks:
                notes.append("<li>nothing to highlight: the citation names this page without a quote or heading found on it</li>")
            group.append(f'<div class="page" id="page-{esc(ref)}-{d}-{p}"><h3>{d} p. {p} '
                         f'<span style="font-weight:normal;color:#777">({esc(rev)})</span></h3>'
                         f'<p class="cited">cited by: {esc(who)}</p>'
                         f'<img src="{rel}" alt="{d} page {p}" loading="lazy"><ul class="located">{"".join(notes)}</ul></div>')
        group.append("</div>")
        left.append("".join(group))
        # the card
        ex = rec["example"] if "example" in rec else examples.example(c, rec["rd"], example_names(rec["rd"]))
        folded_cites = {}
        for h in rec.get("folded_cites", []):
            ct = c.lines[h].get("cite", {})
            if ct.get("doc"):
                folded_cites.setdefault((ct["doc"], ct.get("locator", "")), []).append(h)
        folded_html = ""
        for (d, locator), whos in folded_cites.items():
            if d == rec["cite"].get("doc") and locator == rec["cite"].get("locator"):
                continue
            folded_html += f"<li><em>{esc(', '.join(whos))}</em>: [{esc(d)}] " + segments_html({"locator": locator}, [], [], ref) + "</li>"
        refusals = "".join(f"<li>{node_html(n)}<div style='color:#555;font-size:.9em'>remedy: {esc(remedy.rstrip('.'))}. Cite: {esc(cite_text(cite))}</div></li>"
                           for _, n, remedy, cite in rec["refusals"])
        helpers = "".join(f"<li><code>{esc(h)}</code> — {esc(str(c.lines[h].get('label', '')))}</li>" for h in rec["helpers"])
        exprs = f"<div class='k'>{esc(ref)}</div><pre>{esc(rec['expr'])}</pre>" + "".join(
            f"<div class='k'>{esc(h)}</div><pre>{esc(yaml.safe_dump(c.lines[h].get('expr'), sort_keys=False, allow_unicode=True, width=100).strip())}</pre>"
            for h in rec["helpers"])
        options = '<option value="">— no verdict yet —</option>' + "".join(f'<option value="{v}">{v}</option>' for v in VERDICTS)
        reached = "" if rec["reached"] == "listed" else \
            f'<p class="reached">Not itself on the reading list: {esc(rec["reached"])}, which it reads and folds in. A verdict here judges the printed line with everything folded into it.</p>'
        right.append(f"""<div class="line" data-ref="{esc(ref)}" id="line-{esc(ref)}" tabindex="0">
<h3>Line {esc(rec["printed"])} of {esc(c.form_name(rec["form"]) if rec["form"] in c.docs else form_title(rec["form"]))} — <code>{esc(ref)}</code></h3>
{reached}
<div class="k">IRS label as printed</div><div>{esc(rec["label"])}</div>
<div class="k">Citation of this line</div>{segments_html(rec["cite"], ordered, flags, ref)}
{('<div class="k">Citations of the lines folded in</div><ul class="reading">' + folded_html + '</ul>') if folded_html else ''}
<div class="k">Reading: what the encoding computes</div><div class="reading"><p><strong>Line {esc(rec["printed"])} is:</strong></p>{node_html(rec["reading"])}</div>
{('<div class="k">Refused when</div><ul class="reading">' + refusals + '</ul>') if refusals else ''}
<div class="k">Worked example</div>{example_html(ex, rec["printed"])}
<details><summary>show expression</summary>{exprs}</details>
{('<details><summary>helpers folded into this line (' + str(len(rec["helpers"])) + ')</summary><ul>' + helpers + '</ul></details>') if helpers else ''}
<div class="verdict"><select aria-label="verdict for {esc(ref)}">{options}</select>
<textarea placeholder="your reason, in your own words"></textarea></div></div>""")
    if orphans:
        parts = []
        for h in orphans:
            rd = R.Reading(c, h)
            parts.append(f"<div class='line' style='border-style:dashed'><h3>{esc(str(c.lines[h].get('label', '')))} — <code>{esc(h)}</code></h3>"
                         f"<div class='k'>Reading</div><div class='reading'>{node_html(rd.node)}</div>"
                         f"<div class='k'>Citation</div><div>{esc(cite_text(c.lines[h].get('cite', {})))}</div></div>")
        right.append('<div class="orphans"><h2 style="font-size:1.05em">Helpers used only by other items</h2>'
                     '<p>Listed for this item, but no printed line judged here reads them; they carry no verdict box.</p>' + "".join(parts) + "</div>")
    page = f"""<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Reading {it["id"]}: {esc(it["title"])}</title><style>{STYLE}</style>
<form id="packet" onsubmit="return false">
<header><a href="index.html">all items</a><strong>Item {it["id"]}</strong><span>{esc(it["title"])}</span>
<label>reader <input id="reader" placeholder="your name" required></label>
<label>date <input id="date" type="date" value="{datetime.date.today().isoformat()}"></label>
<button id="save" type="button">Save verdicts</button><span id="count"></span><span id="status"></span></header>
<main><div class="pane">{''.join(left)}</div><div class="pane">{''.join(right)}</div></main></form>
<script>{SCRIPT % {"item": it["id"]}}</script>"""
    (OUT / f"{it['id']}.html").write_text(page, encoding="utf-8")
    return recs, orphans


def index(rows):
    OUT.mkdir(parents=True, exist_ok=True)
    body = "".join(f'<tr><td><a href="{i}.html">{i}</a></td><td>{esc(t)}</td><td>{n}</td><td>{p}</td></tr>' for i, t, n, p in rows)
    (OUT / "index.html").write_text(f"""<!doctype html><meta charset="utf-8"><title>Human reading packets</title><style>{STYLE}
table{{border-collapse:collapse;margin:1em}} td,th{{padding:.3em .8em;border-bottom:1px solid #eee;text-align:left}}</style>
<header><strong>Human reading packets</strong><span>the reading list of the integrity plan, one packet per item</span></header>
<table><tr><th>item</th><th>title</th><th>printed lines judged</th><th>helpers folded</th></tr>{body}</table>""", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--item", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--dpi", type=int, default=110)
    ap.add_argument("--force", action="store_true", help="re-render page images that already exist")
    a = ap.parse_args()
    items = reading_list()["items"]
    if a.list:
        for it in items:
            recs, orphans = plan_item(it)
            print(f"{it['id']:>2}  {len(it['lines']):>3} listed  {len(recs):>2} printed judged  "
                  f"{sum(len(r['helpers']) for r in recs):>3} helpers folded  {len(orphans)} unread  {it['title']}")
        return
    if a.item:
        items = [item(a.item)]
    elif not a.all:
        ap.error("--item N, --all or --list")
    rows = []
    for it in items:
        recs, orphans = build(it, a.dpi, a.force)
        folded = sum(len(r["helpers"]) for r in recs)
        rows.append((it["id"], it["title"], len(recs), folded))
        print(f"item {it['id']}: {len(recs)} printed lines judged ({', '.join(r['ref'] for r in recs)}), "
              f"{folded} helpers folded, {len(orphans)} listed helpers unread -> {OUT / (str(it['id']) + '.html')}")
    if a.all:
        index(rows)
        print(f"open {OUT / 'index.html'}")


if __name__ == "__main__":
    main()
