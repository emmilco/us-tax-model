#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""A local page-by-page review of the archived text: the rendered page on the left, the
project's reading of it on the right, for a person to judge an extraction against the
page itself (the court of last appeal for the conservation checks).

Writes .extraction-review/index.html plus one HTML file and one PNG per page for each
document; open index.html in a browser. Nothing here is committed; rerun to refresh.

    page_review.py [--docs id,id] [--dpi 110]
"""
import argparse
import html
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "sources" / "2025"
OUT = ROOT / ".extraction-review"

STYLE = """
body{margin:0;font:15px/1.45 -apple-system,Helvetica,Arial,sans-serif;color:#222}
header{display:flex;gap:1.2em;align-items:baseline;padding:.6em 1em;border-bottom:1px solid #ddd;background:#fafafa;position:sticky;top:0}
header a{color:#1a4f8b;text-decoration:none} header .kind{padding:.1em .5em;border-radius:.6em;background:#eef;font-size:.9em}
main{display:grid;grid-template-columns:1fr 1fr;height:calc(100vh - 3.2em)}
.pane{overflow:auto;padding:1em;border-right:1px solid #ddd} .pane img{width:100%;height:auto;border:1px solid #ccc}
pre{white-space:pre-wrap;font:14px/1.5 Menlo,Consolas,monospace;margin:0}
details{margin-top:1em} summary{cursor:pointer;color:#555}
"""


def pages_of(path):
    pages = path.read_text(encoding="utf-8", errors="replace").split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def build(entry, dpi):
    doc = entry["id"]
    d = OUT / doc
    d.mkdir(parents=True, exist_ok=True)
    layout = pages_of(ARCHIVE / entry["text_file"])
    cols = pages_of(ARCHIVE / entry["cols_file"])
    meta = json.loads((ARCHIVE / entry["pages_file"]).read_text(encoding="utf-8"))
    n = len(layout)
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", str(ARCHIVE / entry["file"]), str(d / "p")], check=True)
    pngs = sorted(d.glob("p-*.png"))
    for i in range(1, n + 1):
        kind, columns = meta["pages"][i - 1], meta["columns"][i - 1]
        reading = cols[i - 1] if kind == "prose" else layout[i - 1]
        other = layout[i - 1] if kind == "prose" else cols[i - 1]
        img = pngs[i - 1].name if i - 1 < len(pngs) else ""
        nav = f'<a href="p{i-1:03d}.html">previous</a>' if i > 1 else "<span>previous</span>"
        nav += f' · <a href="p{i+1:03d}.html">next</a>' if i < n else " · <span>next</span>"
        page = f"""<!doctype html><meta charset="utf-8"><title>{doc} p. {i}</title><style>{STYLE}</style>
<header><a href="../index.html">all documents</a><strong>{doc}</strong><span>page {i} of {n}</span>
<span class="kind">{kind}, {columns} column{'s' if columns != 1 else ''}</span><span>{nav}</span>
<span style="margin-left:auto;color:#666">the model reads the {'reading-order' if kind == 'prose' else 'layout'} text for this page</span></header>
<main><div class="pane"><img src="{img}" alt="page {i}"></div>
<div class="pane"><pre>{html.escape(reading)}</pre>
<details><summary>the other extraction ({'layout' if kind == 'prose' else 'reading order'})</summary><pre>{html.escape(other)}</pre></details></div></main>"""
        (d / f"p{i:03d}.html").write_text(page, encoding="utf-8")
    return n, meta


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docs")
    ap.add_argument("--dpi", type=int, default=110)
    a = ap.parse_args()
    docs = [d for d in json.loads((ARCHIVE / "manifest.json").read_text())["documents"] if d.get("format", "pdf") == "pdf" and "cols_file" in d]
    if a.docs:
        want = set(a.docs.split(",")); docs = [d for d in docs if d["id"] in want]
    rows = []
    for d in docs:
        n, meta = build(d, a.dpi)
        kinds = {k: meta["pages"].count(k) for k in ("prose", "mixed", "table", "single")}
        rows.append(f'<tr><td><a href="{d["id"]}/p001.html">{d["id"]}</a></td><td>{html.escape(d.get("revision") or "")}</td><td>{n}</td>'
                    f'<td>{kinds["prose"]}</td><td>{kinds["mixed"]}</td><td>{kinds["table"]}</td><td>{kinds["single"]}</td></tr>')
        print(f"{d['id']}: {n} pages", flush=True)
    index = f"""<!doctype html><meta charset="utf-8"><title>Extraction review</title><style>{STYLE}
table{{border-collapse:collapse;margin:1em}} td,th{{padding:.3em .8em;border-bottom:1px solid #eee;text-align:left}}</style>
<header><strong>Extraction review</strong><span>page image on the left, the text the project reads on the right</span></header>
<table><tr><th>document</th><th>revision</th><th>pages</th><th>prose</th><th>mixed</th><th>table</th><th>single</th></tr>{''.join(rows)}</table>"""
    (OUT / "index.html").write_text(index, encoding="utf-8")
    print(f"open {OUT / 'index.html'}")


if __name__ == "__main__":
    main()
