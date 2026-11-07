#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""How often each candidate gate situation applies: the share of all individual returns answering yes.

The data is interview/gate_frequencies-<year>.yaml: one entry per situation with its share, a range,
a source and a note. The formal gates design's "Rare-situation pages" rule reads it: gates answered
yes by fewer filers than the recorded `cut` (its share and source) go on themed grids at the end. Each
situation below the cut names a `theme` from `themes`, and no theme holds more than `max_rows` of them.

A source is one of three kinds:

- `soi`: IRS Statistics of Income cells (`sources/<year>/soi-*.xls`), each with its file, table, column,
  column header, optional row label (default the "All returns" row) and the number of returns read
  there, combined by `single`, `sum` or `max`. The share is that count over the total returns.
- `microdata`: a PolicyEngine-US predicate over filing units, weighted by the coverage estimate's
  weights raked to the IRS counts (`estimate.py`), with the share it gave.
- `judgment`: a recorded reasoning, with any IRS cells that bound it (`bounds`).

    gate_frequencies.py             write reports/<year>/gate_frequencies.md
    gate_frequencies.py --check     fail if an entry lacks a share in [0, 1] inside its range or a source,
                                    an IRS share does not follow from its recorded counts, the cut lacks a
                                    share or source, a situation below it lacks a known theme, a theme holds
                                    more than max_rows situations, or the report is stale
    gate_frequencies.py --recompute (engines interpreter) re-read every IRS cell and microdata predicate
                                    and fail on any recorded value that differs
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402

DATA = ROOT / "interview" / f"gate_frequencies-{Y}.yaml"
REPORT = ROOT / "reports" / Y / "gate_frequencies.md"
ARCHIVE = ROOT / "sources" / Y
KINDS = ("soi", "microdata", "judgment")
COMBINE = ("single", "sum", "max")
CELL_KEYS = {"file", "table", "column", "header", "returns", "row", "note"}


def load(path=DATA):
    import yaml

    class Loader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        keys = [loader.construct_object(k, deep=deep) for k, _ in node.value]
        dup = sorted({k for k in keys if keys.count(k) > 1})
        if dup:
            raise SystemExit(f"{path.relative_to(ROOT)}: duplicate keys {dup}")
        return loader.construct_mapping(node, deep=deep)

    Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    return yaml.load(path.read_text(), Loader=Loader)


def combined(cells, how):
    values = [c["returns"] for c in cells]
    return values[0] if how == "single" else sum(values) if how == "sum" else max(values)


def problems(data):
    out = []
    total = (data.get("total_returns") or {}).get("returns")
    if not isinstance(total, (int, float)) or total <= 0:
        return ["total_returns.returns missing"]
    cut = data.get("cut") or {}
    if not isinstance(cut.get("share"), (int, float)) or not 0 < cut["share"] < 1:
        return [f"cut.share {cut.get('share')!r} not in (0, 1)"]
    if not isinstance(cut.get("source"), str) or not cut["source"].strip():
        out.append("cut: no source")
    themes, max_rows = data.get("themes") or {}, data.get("max_rows")
    if not isinstance(max_rows, int) or max_rows < 1:
        out.append(f"max_rows {max_rows!r} not a positive integer")
        max_rows = None
    rows = {}
    for sid, e in (data.get("situations") or {}).items():
        if not isinstance(e, dict) or not isinstance(e.get("share"), (int, float)):
            continue
        theme = e.get("theme")
        if e["share"] < cut["share"]:
            if theme not in themes:
                out.append(f"situation {sid}: below the cut but its theme {theme!r} is not one of the themes")
            else:
                rows.setdefault(theme, []).append(sid)
        elif theme is not None:
            out.append(f"situation {sid}: at or above the cut but has a theme")
    for theme, sids in rows.items():
        if max_rows and len(sids) > max_rows:
            out.append(f"theme {theme}: {len(sids)} situations, more than max_rows {max_rows}")

    def cell_errors(where, cells):
        errs = []
        if not isinstance(cells, list) or not cells:
            return [f"{where}: no cells"]
        for c in cells:
            if not isinstance(c, dict) or set(c) - CELL_KEYS or not {"file", "table", "column", "header", "returns"} <= set(c):
                errs.append(f"{where}: cell {c!r} needs file, table, column, header, returns (and optionally row, note)")
            elif not (ARCHIVE / f"{c['file']}.xls").exists():
                errs.append(f"{where}: {c['file']}.xls is not archived in sources/{Y}")
            elif not isinstance(c["returns"], (int, float)) or c["returns"] < 0:
                errs.append(f"{where}: cell returns {c['returns']!r}")
        return errs

    for sid, e in (data.get("situations") or {}).items():
        w = f"situation {sid}"
        if not isinstance(e, dict):
            out.append(f"{w}: not a mapping")
            continue
        for key in ("label", "refs", "share", "range", "source"):
            if key not in e:
                out.append(f"{w}: no {key}")
        share, rng, src = e.get("share"), e.get("range"), e.get("source") or {}
        if not isinstance(share, (int, float)) or not 0 <= share <= 1:
            out.append(f"{w}: share {share!r} not in [0, 1]")
            continue
        if not (isinstance(rng, list) and len(rng) == 2 and all(isinstance(x, (int, float)) for x in rng)
                and 0 <= rng[0] <= share <= rng[1] <= 1):
            out.append(f"{w}: range {rng!r} must be [low, high] in [0, 1] around the share {share}")
        if not isinstance(e.get("refs"), list) or not e.get("refs"):
            out.append(f"{w}: refs must name at least one candidate (survey, ladder or input)")
        kind = src.get("kind")
        if kind not in KINDS:
            out.append(f"{w}: source kind {kind!r} not one of {KINDS}")
            continue
        if kind == "soi":
            errs = cell_errors(w, src.get("cells"))
            out += errs
            if src.get("combine") not in COMBINE:
                out.append(f"{w}: combine {src.get('combine')!r} not one of {COMBINE}")
            elif not errs:
                expect = combined(src["cells"], src["combine"]) / total
                if abs(expect - share) > 5e-5:
                    out.append(f"{w}: share {share} but its cells give {expect:.5f}")
        elif kind == "microdata":
            if not isinstance(src.get("predicate"), dict) or not src.get("dataset"):
                out.append(f"{w}: microdata source needs dataset and predicate")
            if abs(src.get("microdata_share", -1) - share) > 5e-5:
                out.append(f"{w}: share {share} differs from microdata_share {src.get('microdata_share')!r}")
        else:
            if not isinstance(src.get("reasoning"), str) or len(src["reasoning"].split()) < 8:
                out.append(f"{w}: a judgment needs its reasoning")
        if "bounds" in src:
            out += cell_errors(f"{w} bounds", src["bounds"])
    return out


def pct(x):
    return f"{x * 100:.2f}%" if x < 0.1 else f"{x * 100:.1f}%"


def source_text(src):
    kind = src["kind"]
    if kind == "soi":
        cells = "; ".join(f"{c['file']} ({c['table']}) col. {c['column']} \"{c['header']}\""
                          + (f", row \"{c['row']}\"" if c.get("row") else "") for c in src["cells"])
        return f"IRS SOI, {src['combine']}: {cells}"
    if kind == "microdata":
        p = src["predicate"]
        return f"Microdata ({src['dataset']}, raked): " + "; ".join(f"{k} {', '.join(map(str, v))}" for k, v in p.items())
    bound = ""
    if src.get("bounds"):
        bound = " Bound: " + "; ".join(f"{c['file']} col. {c['column']} \"{c['header']}\" {c['returns']:,.0f}" for c in src["bounds"]) + "."
    return "Judgment." + bound


def render(data):
    total = data["total_returns"]["returns"]
    rows = sorted(data["situations"].items(), key=lambda kv: (-kv[1]["share"], kv[0]))
    cut = data["cut"]["share"]
    below = [(sid, e) for sid, e in rows if e["share"] < cut]
    out = [
        f"# How often each candidate gate applies ({Y})",
        "",
        f"Generated by `tools/coverage/gate_frequencies.py` from `interview/gate_frequencies-{Y}.yaml`; do not edit by hand.",
        "",
        f"Each share is of all {total:,.0f} individual returns the IRS counted for tax year {data['tax_year_counts']}",
        "(Statistics of Income, Publication 1304), the denominator of the coverage estimate. Sources are IRS cells",
        "where one counts the situation, PolicyEngine-US microdata raked to the IRS counts where only the microdata",
        "places it, and a recorded judgment otherwise. An IRS count is of returns *reporting* an amount; where more",
        "people would honestly answer the question yes than report the amount (a state refund that is not taxable,",
        "gambling winnings, tuition paid without a credit) the entry is a judgment bounded by the IRS count.",
        "",
    ]
    out += [
        f"**Cut:** {pct(cut)} of all returns ({data['cut']['source']}). {len(below)} of {len(rows)} situations fall below it",
        f"and go on the rare-situation grids, grouped by a proposed theme, at most {data['max_rows']} rows per grid.",
        "Situations whose range crosses the cut are marked ~: the estimate does not settle their side of it.",
        "",
        "## Proposed grids (situations below the cut)",
        "",
        "The themes are a proposal for the owner, recorded as `theme` in the data.",
        "",
    ]
    for theme, title in data["themes"].items():
        members = [(sid, e) for sid, e in below if e.get("theme") == theme]
        out.append(f"- **{title}** (`{theme}`, {len(members)} rows): "
                   + ", ".join(f"{e['label']} (`{sid}`, {pct(e['share'])})" for sid, e in members))
    out += ["", "## All situations by share", "",
            "| # | Situation | Share | Range | Kind | Grid | Candidate | Source |", "|---|---|---|---|---|---|---|---|"]
    marked = False
    for i, (sid, e) in enumerate(rows, 1):
        if not marked and e["share"] < cut:
            out.append(f"| | **— cut at {pct(cut)}: rare-situation grids below —** | | | | | | |")
            marked = True
        lo, hi = e["range"]
        flag = " ~" if lo < cut <= hi else ""
        out.append(f"| {i} | {e['label']} (`{sid}`){flag} | {pct(e['share'])} | {pct(lo)}–{pct(hi)} | {e['source']['kind']} | "
                   f"{e.get('theme', '')} | {', '.join(e['refs'])} | {source_text(e['source'])} |")
    out += ["", "## Estimates that straddle the cut", ""]
    out += [f"- `{sid}` ({pct(e['share'])}, {pct(e['range'][0])}–{pct(e['range'][1])}, {e['source']['kind']})"
            for sid, e in rows if e["range"][0] < cut <= e["range"][1]] or ["- None."]
    out += ["", "## Notes by situation", ""]
    for sid, e in rows:
        reason = e["source"].get("reasoning", "").strip()
        text = " ".join(x for x in (reason, e.get("note", "").strip()) if x)
        if text:
            out.append(f"- `{sid}`: {text}")
    return "\n".join(out) + "\n"


def recompute(data):
    """Re-read every IRS cell from the archived tables and every microdata predicate from the raked weights."""
    import numpy as np
    import pandas as pd
    sys.path.insert(0, str(Path(__file__).parent))
    import estimate

    tables, bad = {}, []

    def read(c):
        if c["file"] not in tables:
            tables[c["file"]] = pd.read_excel(ARCHIVE / f"{c['file']}.xls", header=None)
        s = tables[c["file"]]
        first = s.iloc[:, 0].fillna("").astype(str).str.strip()
        label = c.get("row", "All returns")
        hits = first[first.str.startswith(label)].index
        if not len(hits):
            raise SystemExit(f"{c['file']}: no row starting {label!r}")
        row = hits[0]
        header_end = first[first.str.startswith("All returns")].index[0]
        header = " ".join(" ".join(str(x).split()) for x in s.iloc[2:header_end, :c["column"] + 1].ffill(axis=1).iloc[:, c["column"]] if str(x) != "nan")
        norm = lambda t: " ".join(t.replace("/", " ").lower().split())
        if norm(c["header"]) not in norm(header):
            raise SystemExit(f"{c['file']} column {c['column']}: header {header!r} does not contain {c['header']!r}")
        return float(s.iloc[row, c["column"]])

    def check_cells(where, cells):
        for c in cells:
            got = read(c)
            if got != c["returns"]:
                bad.append(f"{where}: {c['file']} col {c['column']} reads {got:,.0f}, recorded {c['returns']:,.0f}")

    check_cells("total_returns", [data["total_returns"]])
    micro = {}
    for sid, e in data["situations"].items():
        src = e["source"]
        if src["kind"] == "soi":
            check_cells(sid, src["cells"])
        check_cells(f"{sid} bounds", src.get("bounds", []))
        if src["kind"] == "microdata" or "microdata_share" in src:
            micro[sid] = src
    if micro:
        from policyengine_us import Microsimulation
        catalog = __import__("json").loads(estimate.CATALOG.read_text())
        cats = catalog["categories"]
        total = estimate.irs_cell(catalog["irs_total"], {})
        for c in cats:
            if "irs" in c:
                c["irs_count"] = estimate.irs_count(c["irs"], {})
        weight, flags = estimate.micro_flags(cats)
        targets = {c["id"]: c["irs_count"] for c in cats if "irs" in c and "micro" in c}
        w, _ = estimate.rake(weight.astype("float64"), flags, targets, total)
        sim = Microsimulation(dataset=str(estimate.DATASET))
        unit = lambda v: np.asarray(sim.calculate(v, estimate.YEAR, map_to="tax_unit"))
        filer = unit("tax_unit_is_filer") > 0
        if filer.sum() != len(w):
            raise SystemExit("filer count differs from the coverage estimate's")
        for sid, src in micro.items():
            p = src["predicate"]
            parts = []
            for v in p.get("positive", []):
                parts.append(unit(v)[filer] > 0)
            for v in p.get("nonzero", []):
                parts.append(unit(v)[filer] != 0)
            if "state_fips" in p:
                parts.append(np.isin(unit("state_fips")[filer].astype(int), p["state_fips"]))
            flag = np.any(parts, axis=0)
            share = w[flag].sum() / total
            print(f"{sid}: microdata {share:.4f} (recorded {src.get('microdata_share')})")
            if abs(share - src.get("microdata_share", -1)) > 5e-5:
                bad.append(f"{sid}: microdata share {share:.4f}, recorded {src.get('microdata_share')}")
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--recompute", action="store_true")
    args = ap.parse_args()
    data = load()
    errs = problems(data)
    if errs and not args.recompute:
        print("gate frequencies: FAIL\n  " + "\n  ".join(errs))
        return 1
    if args.recompute:
        bad = recompute(data)
        if bad:
            print("gate frequencies: recorded values differ\n  " + "\n  ".join(bad))
            return 1
        print("gate frequencies: every IRS cell and microdata share matches")
        return 0
    text = render(data)
    if args.check:
        if not REPORT.exists() or REPORT.read_text() != text:
            print(f"gate frequencies: FAIL - {REPORT.relative_to(ROOT)} is stale (run tools/coverage/gate_frequencies.py)")
            return 1
        print(f"gate frequencies: {len(data['situations'])} situations, each with a share and a source; report current")
        return 0
    REPORT.write_text(text)
    print(f"gate frequencies: wrote {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
