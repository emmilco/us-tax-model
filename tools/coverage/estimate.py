"""Estimate the share of all individual returns the tool can prepare (spec 2.4).

A return is covered only if no refused situation applies to it. The share of
returns each situation affects comes from the archived IRS Statistics of Income
tables (`categories.json`, `sources/2025/soi-*.xls`). The overlaps between
situations come from PolicyEngine-US household microdata, reweighted by raking
(iterative proportional fitting) so that every category with an IRS count
matches it. Categories the microdata cannot place are combined as independent
of everything else; the report also gives the range their overlap allows.

Runs under the engines interpreter (`.engines/venv`, `tools/engines/setup.sh`)
with the microdata at `.engines/data/populace_us_2024.h5` (`fetch_microdata.sh`); it skips visibly when
either is missing.

    .engines/venv/bin/python -I tools/coverage/estimate.py
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
CATALOG = Path(__file__).with_name("categories.json")
ARCHIVE = ROOT / "sources" / "2025"
DATASET = ROOT / ".engines" / "data" / "populace_us_2024.h5"
DATASET_SHA256 = "6496cc4393d4d3c6574f76eca231de5898c803b9067645591fd5c4d3e65aee84"
CACHE = ROOT / ".engines" / "work" / "coverage_flags.npz"
REPORT_MD = ROOT / "reports" / "2025" / "filer_coverage.md"
REPORT_JSON = ROOT / "reports" / "2025" / "filer_coverage.json"
YEAR = 2025


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def irs_cell(cell, tables):
    """Number of returns in the 'All returns, total' row, after checking the column header."""
    import pandas as pd
    source = cell["source"]
    if source not in tables:
        tables[source] = pd.read_excel(ARCHIVE / f"{source}.xls", header=None)
    sheet = tables[source]
    first = sheet.iloc[:, 0].fillna("").astype(str).str.strip()
    total_row = first[first.str.startswith("All returns")].index[0]
    header = " ".join(" ".join(str(x).split()) for x in sheet.iloc[2:total_row, :cell["column"] + 1].ffill(axis=1).iloc[:, cell["column"]] if str(x) != "nan")
    norm = lambda t: " ".join(t.replace("/", " ").lower().split())
    if norm(cell["header"]) not in norm(header) or "number of returns" not in norm(header):
        raise SystemExit(f"{source} column {cell['column']}: header {header!r} does not contain {cell['header']!r} and 'Number of returns'")
    return float(sheet.iloc[total_row, cell["column"]])


def irs_count(spec, tables):
    if spec["combine"] == "max_of_sums":
        return max(sum(irs_cell(c, tables) for c in part) for part in spec["cells"])
    values = [irs_cell(c, tables) for c in spec["cells"]]
    return sum(values) if spec["combine"] == "sum" else max(values)


def form_gates():
    """Every refusal gate in the forms: the `when` of each `refuses` entry."""
    import yaml
    gates = set()
    def walk(x):
        if isinstance(x, dict):
            gates.update(r["when"] for r in x.get("refuses") or [] if isinstance(r, dict) and "when" in r)
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for path in sorted((ROOT / "forms" / "2025").glob("*.yaml")):
        walk(yaml.safe_load(path.read_text()))
    return gates


def micro_flags(categories):
    """Per-filing-unit flags for every microdata predicate, cached by dataset and predicate."""
    import numpy as np
    predicates = {c["id"]: c["micro"] for c in categories if "micro" in c}
    key = hashlib.sha256(json.dumps([DATASET_SHA256, YEAR, predicates], sort_keys=True).encode()).hexdigest()
    if CACHE.exists():
        cached = np.load(CACHE, allow_pickle=False)
        if str(cached["key"]) == key:
            return cached["weight"], {k: cached["f_" + k] for k in predicates}
    from policyengine_us import Microsimulation
    sim = Microsimulation(dataset=str(DATASET))
    unit = lambda v: np.asarray(sim.calculate(v, YEAR, map_to="tax_unit"))
    filer = unit("tax_unit_is_filer") > 0
    weight = np.asarray(sim.calculate("tax_unit_weight", YEAR))[filer]
    status = np.asarray(sim.calculate("filing_status", YEAR)).astype(str)[filer]
    flags = {}
    for cid, p in predicates.items():
        if "filing_status" in p:
            flags[cid] = np.isin(status, p["filing_status"])
        elif "positive" in p:
            flags[cid] = np.any([unit(v)[filer] > 0 for v in p["positive"]], axis=0)
        else:
            flags[cid] = np.any([unit(v)[filer] != 0 for v in p["nonzero"]], axis=0)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    np.savez(CACHE, key=key, weight=weight, **{"f_" + k: v for k, v in flags.items()})
    return weight, flags


def rake(weight, flags, targets, total, iterations=5000, tolerance=1e-6):
    """Scale weights until the total and every flagged share match their targets."""
    import numpy as np
    w = weight * (total / weight.sum())
    for _ in range(iterations):
        worst = 0.0
        for cid, target in targets.items():
            f = flags[cid]
            have = w[f].sum()
            worst = max(worst, abs(have - target) / total)
            w[f] *= target / have
            w[~f] *= (total - target) / w[~f].sum()
        if worst < tolerance:
            return w, worst
    raise SystemExit(f"raking did not converge (largest share error {worst:.2e})")


def main():
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args()
    try:
        import numpy as np
        import pandas  # noqa: F401
    except ImportError:
        print("coverage estimate: SKIPPED - run under .engines/venv (tools/engines/setup.sh)")
        return
    if not DATASET.exists():
        print(f"coverage estimate: SKIPPED - microdata not present at {DATASET.relative_to(ROOT)}")
        return
    if sha256(DATASET) != DATASET_SHA256:
        raise SystemExit("microdata hash does not match the pinned build")
    catalog = json.loads(CATALOG.read_text())
    cats, groups = catalog["categories"], catalog["groups"]
    tables = {}
    total = irs_cell(catalog["irs_total"], tables)
    for c in cats:
        if "irs" in c:
            c["irs_count"] = irs_count(c["irs"], tables)
    weight, flags = micro_flags(cats)
    weight = weight.astype("float64")
    raw_total = weight.sum()
    targets = {c["id"]: c["irs_count"] for c in cats if "irs" in c and "micro" in c}
    w, err = rake(weight, flags, targets, total)

    refused = [c for c in cats if c.get("refused", True)]
    micro = [c for c in refused if "micro" in c]
    irs_only = [c for c in refused if "micro" not in c]

    def covered(exclude_groups=()):
        hit = np.zeros(len(w), dtype=bool)
        for c in micro:
            if c["group"] not in exclude_groups:
                hit |= flags[c["id"]]
        micro_share = w[~hit].sum() / total
        rest = [c["irs_count"] / total for c in irs_only if c["group"] not in exclude_groups]
        return micro_share, float(np.prod([1 - s for s in rest])), sum(rest)

    m, indep, s = covered()
    central, low, high = m * indep, max(0.0, m - s), m

    rows = []
    for c in refused:
        share_raw = None
        if "micro" in c:
            share_raw = weight[flags[c["id"]]].sum() / raw_total
        share = (w[flags[c["id"]]].sum() / total) if "micro" in c else c["irs_count"] / total
        rows.append({"id": c["id"], "group": c["group"], "label": c["label"], "gates": c.get("gates", []),
                     "irs_returns": c.get("irs_count"), "microdata_share_before_raking": share_raw,
                     "share": share, "basis": ("IRS count with qualifying surviving spouses (" + c["calibrated_by"] + "), overlap from microdata" if "calibrated_by" in c
                                               else "IRS count, overlap from microdata" if "irs" in c and "micro" in c
                                               else "IRS count only (independence assumed)" if "irs" in c
                                               else "microdata model only (no IRS count; new for 2025)")})

    order, done, steps = [], set(), []
    remaining = [g for g in groups if any(c["group"] == g for c in refused)]
    while remaining:
        best = max(remaining, key=lambda g: (lambda r: r[0] * r[1])(covered(tuple(done | {g}))))
        done.add(best); remaining.remove(best)
        r = covered(tuple(done))
        steps.append({"group": best, "label": groups[best], "coverage_after": r[0] * r[1]})
    model_only = [c for c in micro if "irs" not in c and "calibrated_by" not in c]
    sensitivity = {}
    for c in model_only:
        micro.remove(c)
        r = covered()
        sensitivity[c["id"]] = r[0] * r[1]
        micro.append(c)
    alone = {g: (lambda r: r[0] * r[1])(covered((g,))) - central for g in groups if any(c["group"] == g for c in refused)}

    all_gates = sorted({g for c in cats for g in c.get("gates", [])})
    gates = form_gates()
    unknown = sorted(set(all_gates) - gates)
    if unknown:
        raise SystemExit(f"categories.json names gates not in the forms: {unknown}")
    unmeasured = sorted(gates - set(all_gates))
    result = {"tax_year_counts": 2023, "simulated_year": YEAR, "irs_total_returns": total,
              "microdata_filing_units_unweighted_total": raw_total, "raking_max_share_error": err,
              "coverage": {"central": central, "low": low, "high": high,
                           "microdata_part": m, "irs_only_independent_factor": indep, "irs_only_share_sum": s},
              "categories": rows, "greedy_order": steps, "coverage_without_model_only_category": sensitivity, "gain_if_covered_alone": alone,
              "gates_mapped": all_gates, "gates_unmeasured": unmeasured}
    REPORT_JSON.write_text(json.dumps(result, indent=1) + "\n")
    REPORT_MD.write_text(render(result, groups))
    print(f"coverage estimate: {central*100:.1f}% of returns (range {low*100:.1f}% to {high*100:.1f}%); report {REPORT_MD.relative_to(ROOT)}")


def render(r, groups):
    pct = lambda x: f"{x*100:.1f}%"
    cov = r["coverage"]
    out = [
        "# Coverage of all individual returns (estimate)",
        "",
        "Generated by `tools/coverage/estimate.py`; do not edit by hand.",
        "",
        "A return counts as covered only if none of the refused situations below applies to it.",
        f"Shares are of the {r['irs_total_returns']:,.0f} individual returns the IRS counted for tax year 2023",
        "(Statistics of Income, Publication 1304, archived under `sources/2025/soi-*`). Overlaps between situations",
        f"come from PolicyEngine-US microdata simulated for {r['simulated_year']}, raked to every IRS count it can place.",
        "",
        f"**Estimated coverage: {pct(cov['central'])}** of returns. If the IRS-only categories overlapped the rest",
        f"completely the figure would be {pct(cov['high'])}; if they overlapped nothing, {pct(cov['low'])}.",
        "",
        "Limits of this estimate:",
        "",
        "- IRS counts are for 2023; the 2025 shares are assumed similar.",
        "- Where the IRS gives only parts of a situation with unknown overlap, the largest part is used, a lower bound.",
        f"- {len(r['gates_unmeasured'])} of the {len(r['gates_unmeasured']) + len(r['gates_mapped'])} refusal gates in the forms are not measured (no IRS count or",
        "  microdata variable), so the true coverage is lower by their share. Gates measured only in part (for example",
        "  `scope.credits`, `scope.other_line16`) also refuse situations not counted here. Unmeasured:",
        "  " + ", ".join(f"`{g}`" for g in r["gates_unmeasured"]) + ".",
        "",
        *(["Categories without an IRS count rest on the microdata model alone. Present coverage if each were set aside:", "",
           *[f"- {k}: {pct(v)}" for k, v in r["coverage_without_model_only_category"].items()], ""]
          if r["coverage_without_model_only_category"] else []),
        "## Coverage gained by each group, in the order that gains most",
        "",
        "Coverage here is of the measured situations only; 100% would still leave the unmeasured refusals above.",
        "",
        "| Step | Group | Coverage after | Gain if covered alone now |",
        "|---|---|---|---|",
    ]
    prev = cov["central"]
    for i, s in enumerate(r["greedy_order"], 1):
        out.append(f"| {i} | {s['label']} | {pct(s['coverage_after'])} (+{(s['coverage_after']-prev)*100:.1f}) | +{r['gain_if_covered_alone'][s['group']]*100:.1f} |")
        prev = s["coverage_after"]
    out += ["", "## Refused situations", "", "| Situation | Group | Share of returns | IRS returns (2023) | Microdata before raking | Basis |", "|---|---|---|---|---|---|"]
    for c in sorted(r["categories"], key=lambda c: -c["share"]):
        irs = f"{c['irs_returns']:,.0f}" if c["irs_returns"] else "—"
        raw = pct(c["microdata_share_before_raking"]) if c["microdata_share_before_raking"] is not None else "—"
        out.append(f"| {c['label']} | {groups[c['group']]} | {pct(c['share'])} | {irs} | {raw} | {c['basis']} |")
    out += ["", f"Raking converged with a largest share error of {r['raking_max_share_error']:.1e}.", ""]
    return "\n".join(out)


if __name__ == "__main__":
    sys.exit(main())
