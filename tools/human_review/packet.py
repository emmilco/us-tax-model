#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""One HTML packet per reading-list item for a person to read the project's lines against
the archived IRS pages (integrity plan items 1.0 and 1.1): the cited pages as images on the
left; on the right, for each line, its printed number, IRS label, rendered English, YAML
expression and citation, with an empty verdict box. Verdicts are saved by serve.py.

Writes the git-ignored .human-review/<item>.html (and index.html); page images are shared
under .human-review/pages/ and rendered once with pdftoppm, as page_review.py renders them.

    packet.py --item N        one packet (1..13)
    packet.py --all           every item and the index
    packet.py --list          the items, their line and page counts, and nothing written
"""
import argparse
import html
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402

HERE = Path(__file__).resolve().parent
ARCHIVE = ROOT / "sources" / Y
OUT = ROOT / ".human-review"
PAGES = OUT / "pages"
VERDICTS = ("MATCH", "MISMATCH", "UNCLEAR")

STYLE = """
body{margin:0;font:15px/1.45 -apple-system,Helvetica,Arial,sans-serif;color:#222}
header{display:flex;flex-wrap:wrap;gap:1em;align-items:center;padding:.6em 1em;border-bottom:1px solid #ddd;background:#fafafa;position:sticky;top:0;z-index:2}
header a{color:#1a4f8b;text-decoration:none}
header input{font:inherit;padding:.25em .5em}
header button{font:inherit;padding:.3em .9em}
#status{color:#555}
main{display:grid;grid-template-columns:1fr 1fr;height:calc(100vh - 3.4em)}
.pane{overflow:auto;padding:1em;border-right:1px solid #ddd}
.pane img{width:100%;height:auto;border:1px solid #ccc}
.page h3{margin:1em 0 .3em;font-size:1em;color:#444}
.line{border:1px solid #ddd;border-radius:.4em;padding:.7em .9em;margin-bottom:1em;background:#fff}
.line h3{margin:0 0 .4em;font-size:1.05em}
.line h3 code{font-weight:normal;color:#666;font-size:.9em}
.line .k{color:#666;font-size:.85em;text-transform:uppercase;letter-spacing:.03em;margin-top:.5em}
.line pre{white-space:pre-wrap;font:13px/1.45 Menlo,Consolas,monospace;margin:.2em 0;background:#f6f6f6;padding:.4em .6em;border-radius:.3em}
.line a.pg{color:#1a4f8b;text-decoration:none}
.verdict{display:flex;gap:.6em;align-items:flex-start;margin-top:.6em}
.verdict select{font:inherit;padding:.25em}
.verdict textarea{font:inherit;flex:1;min-height:3.2em;padding:.3em .5em}
.line.done{border-color:#9c9}
@media (max-width:900px){main{grid-template-columns:1fr;height:auto}.pane{border-right:0}}
"""

SCRIPT = """
const ITEM=%(item)d, KEY='human-review-'+ITEM, FORM=document.getElementById('packet');
const lines=[...document.querySelectorAll('.line')];
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
  mark();})();
"""


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


_forms = {}


def form_lines(fid):
    """The YAML lines of a form or def, by id."""
    if fid not in _forms:
        raw = yaml.safe_load((ROOT / "forms" / Y / f"{fid}.yaml").read_text(encoding="utf-8"))
        doc = raw.get("form") or raw.get("def")
        _forms[fid] = (doc, {l["id"]: l for l in doc["lines"]})
    return _forms[fid]


_rendered = {}


def rendered_sections(fid):
    """Each `## <printed> — `<id>`` section of rendered/<year>/<fid>.md: its bullets by key."""
    if fid not in _rendered:
        text = (ROOT / "rendered" / Y / f"{fid}.md").read_text(encoding="utf-8")
        out = {}
        for m in re.finditer(r"^## (.*?) — `([^`]+)`\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S):
            bullets = {}
            for b in re.finditer(r"^- (?:\*\*([^*]+)\*\*|([A-Za-z ]+):) ?(.*)$", m.group(3), flags=re.M):
                bullets[(b.group(1) or b.group(2)).strip().rstrip(":")] = b.group(3).strip()
            out[m.group(2)] = {"printed": m.group(1), "bullets": bullets}
        _rendered[fid] = out
    return _rendered[fid]


def cite_pages(cite):
    """The document and first page a rendered citation names, or (None, None)."""
    m = re.match(r"\[([a-z0-9-]+)\] (.*)", cite or "")
    if not m:
        return None, None
    p = re.search(r"\bpp?\. ?(\d+)", m.group(2))
    return m.group(1), (int(p.group(1)) if p else None)


def table_band(ref):
    fid, _, rest = ref.partition(".")
    at_least = int(rest.split("_")[1])
    t = yaml.safe_load((ROOT / "tables" / Y / f"{fid}.yaml").read_text(encoding="utf-8"))["table"]
    band = next(b for b in t["bands"] if b["at_least"] == at_least)
    cols = [c["key"] for c in t["columns"]]
    tax = dict(zip(cols, band["tax"]))
    secs = rendered_sections(fid)
    row = f"| ${at_least:,} | ${band['less_than']:,} | " + " | ".join(f"${v:,}" for v in band["tax"]) + " |"
    cite = ""
    m = re.search(r"^- Cite: (.*)$", (ROOT / "rendered" / Y / f"{fid}.md").read_text(encoding="utf-8"), flags=re.M)
    if m:
        cite = m.group(1)
    return {"ref": ref, "form": fid, "id": rest, "printed": "Tax Table", "kind": "table cell",
            "label": f"At least ${at_least:,} but less than ${band['less_than']:,}: the tax by filing status column",
            "english": "; ".join(f"{k} ${v:,}" for k, v in tax.items()) + f" (rendered/{Y}/{fid}.md row: {row})",
            "expr": yaml.safe_dump(band, sort_keys=False).strip(), "cite": cite, "type": t.get("kind"), "secs": secs}


def resolve(ref):
    """One reading-list reference to what the packet shows and the log records."""
    fid, _, rest = ref.partition(".")
    if fid == "tax_table":
        d = table_band(ref)
        d.pop("secs")
        return d
    doc, lines = form_lines(fid)
    lid = ref if ref in lines else rest
    if lid not in lines:
        sys.exit(f"{ref}: no such line in forms/{Y}/{fid}.yaml")
    line = lines[lid]
    sec = rendered_sections(fid).get(lid)
    if sec is None:
        sys.exit(f"{ref}: no section `{lid}` in rendered/{Y}/{fid}.md")
    b = sec["bullets"]
    label = b.get("IRS") or b.get("Authored helper label") or str(line.get("label", ""))
    english = next((v for k, v in b.items() if k.startswith("Encoded")), "")
    etype = next((k[len("Encoded ("):-1] for k in b if k.startswith("Encoded (")), str(line.get("type", "")))
    return {"ref": ref, "form": fid, "id": lid, "printed": str(line.get("printed", sec["printed"])),
            "kind": doc.get("kind"), "label": label, "english": english, "type": etype,
            "expr": yaml.safe_dump(line.get("expr"), sort_keys=False, allow_unicode=True, width=100).strip(),
            "cite": b.get("Cite", ""), "note": b.get("Note", "")}


def item_lines(it):
    return [resolve(r) for r in it["lines"]]


def page_png(doc, page, dpi, force=False):
    """Render one archived page to .human-review/pages/<doc>-p<NNN>.png (kept between runs)."""
    PAGES.mkdir(parents=True, exist_ok=True)
    stem = PAGES / f"{doc}-p{page:03d}"
    png = stem.with_suffix(".png")
    if force or not png.exists():
        pdf = ARCHIVE / manifest()[doc]["file"]
        subprocess.run(["pdftoppm", "-r", str(dpi), "-f", str(page), "-l", str(page), "-png", "-singlefile",
                        str(pdf), str(stem)], check=True)
    return png


def build(it, dpi, force=False):
    OUT.mkdir(parents=True, exist_ok=True)
    docs = manifest()
    pages_in = {(p["doc"], n) for p in it["pages"] for n in p["pages"]}
    first_page = {p["doc"]: p["pages"][0] for p in it["pages"]}
    left = []
    for p in it["pages"]:
        d = docs[p["doc"]]
        for n in p["pages"]:
            png = page_png(p["doc"], n, dpi, force)
            left.append(f'<div class="page" id="page-{p["doc"]}-{n}"><h3>{p["doc"]} p. {n} '
                        f'<span style="font-weight:normal;color:#777">({html.escape(d.get("revision") or "")})</span></h3>'
                        f'<img src="pages/{png.name}" alt="{p["doc"]} page {n}" loading="lazy"></div>')
    right = []
    lines = item_lines(it)
    for l in lines:
        doc, page = cite_pages(l["cite"])
        link = ""
        if doc and (doc, page) in pages_in:
            link = f' <a class="pg" href="#page-{doc}-{page}">show {doc} p. {page}</a>'
        elif doc in first_page:
            link = f' <a class="pg" href="#page-{doc}-{first_page[doc]}">show {doc} (first packet page)</a>'
        options = '<option value="">— no verdict yet —</option>' + "".join(f'<option value="{v}">{v}</option>' for v in VERDICTS)
        right.append(f"""<div class="line" data-ref="{html.escape(l["ref"])}" id="line-{html.escape(l["ref"])}">
<h3>{html.escape(l["printed"])} — <code>{html.escape(l["ref"])}</code></h3>
<div class="k">IRS label</div><div>{html.escape(l["label"])}</div>
<div class="k">Rendered English ({html.escape(l.get("type") or "")})</div><div>{html.escape(l["english"])}</div>
<div class="k">YAML expression</div><pre>{html.escape(l["expr"])}</pre>
<div class="k">Citation</div><div>{html.escape(l["cite"])}{link}</div>
{('<div class="k">Note</div><div>' + html.escape(l["note"]) + '</div>') if l.get("note") else ''}
<div class="verdict"><select aria-label="verdict for {html.escape(l["ref"])}">{options}</select>
<textarea placeholder="your reason, in your own words"></textarea></div></div>""")
    page = f"""<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Reading {it["id"]}: {html.escape(it["title"])}</title><style>{STYLE}</style>
<form id="packet" onsubmit="return false">
<header><a href="index.html">all items</a><strong>Item {it["id"]}</strong><span>{html.escape(it["title"])}</span>
<label>reader <input id="reader" placeholder="your name" required></label>
<label>date <input id="date" type="date" value="{__import__("datetime").date.today().isoformat()}"></label>
<button id="save" type="button">Save verdicts</button><span id="count"></span><span id="status"></span></header>
<main><div class="pane">{''.join(left)}</div><div class="pane">{''.join(right)}</div></main></form>
<script>{SCRIPT % {"item": it["id"]}}</script>"""
    (OUT / f"{it['id']}.html").write_text(page, encoding="utf-8")
    return len(lines), len(pages_in)


def index(rows):
    OUT.mkdir(parents=True, exist_ok=True)
    body = "".join(f'<tr><td><a href="{i}.html">{i}</a></td><td>{html.escape(t)}</td><td>{n}</td><td>{p}</td></tr>' for i, t, n, p in rows)
    (OUT / "index.html").write_text(f"""<!doctype html><meta charset="utf-8"><title>Human reading packets</title><style>{STYLE}
table{{border-collapse:collapse;margin:1em}} td,th{{padding:.3em .8em;border-bottom:1px solid #eee;text-align:left}}</style>
<header><strong>Human reading packets</strong><span>the reading list of the integrity plan, one packet per item</span></header>
<table><tr><th>item</th><th>title</th><th>lines</th><th>pages</th></tr>{body}</table>""", encoding="utf-8")


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
            print(f"{it['id']:>2}  {len(it['lines']):>3} lines  {sum(len(p['pages']) for p in it['pages']):>3} pages  {it['title']}")
        return
    if a.item:
        items = [item(a.item)]
    elif not a.all:
        ap.error("--item N, --all or --list")
    rows = []
    for it in items:
        n, p = build(it, a.dpi, a.force)
        rows.append((it["id"], it["title"], n, p))
        print(f"item {it['id']}: {n} lines, {p} pages -> {OUT / (str(it['id']) + '.html')}")
    if a.all:
        index(rows)
        print(f"open {OUT / 'index.html'}")


if __name__ == "__main__":
    main()
