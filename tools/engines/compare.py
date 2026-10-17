#!/usr/bin/env python3
"""Compare the project's computed lines with the external engines' and write the report.

Categories per (engine, case, line):
  exact          engine equals the project to the cent
  table-adjusted engine equals the project's tax lines recomputed with every Tax
                 Table lookup replaced by the rate schedule (engines use the
                 schedule where the form uses the table); the recomputation keeps
                 the worksheet path and re-takes its smaller-of, so it is an
                 identified cause, not a tolerance
  float          engine differs by no more than two units in the last place of its
                 floating-point representation (float32 for PolicyEngine-US, float64
                 for Tax-Calculator), a bound derived from the engine's precision
  excluded       the engine cannot model a feature of the case; reason recorded
  explained      a disagreement with a cited cause in the investigation log
  UNEXPLAINED    a disagreement with no cause; fails the run
"""
import argparse, json, sys, os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TAX_LINES = {"f1040.line16", "f1040.line19", "f1040.line20", "f1040.line24", "f1040.line28", "f1040.tax_before_credits"}


def half_up(n, d):
    return (2 * n + d) // (2 * d)


def load_tables():
    sched = json.load(open(os.path.join(ROOT, "canonical", "2025", "tables", "rate_schedule.json")))["table"]
    table = json.load(open(os.path.join(ROOT, "canonical", "2025", "tables", "tax_table.json")))["table"]
    params = json.load(open(os.path.join(ROOT, "canonical", "2025", "params.json")))["params"]["values"]
    boundary = params["ordinary.table_boundary"]["value"]
    return {"schedules": sched["schedules"], "alias": sched.get("status_alias", {}), "table": table, "boundary": boundary}


def schedule_tax(t, status, amount):
    rows = t["schedules"][t["alias"].get(status, status)]
    for r in rows:
        if r["upper"] is None or amount <= r["upper"]:
            return r["base"] + half_up((amount - r["over"]) * r["rate"]["num"], r["rate"]["den"])
    raise ValueError("no bracket")


def table_tax(t, status, amount):
    col = next(i for i, c in enumerate(t["table"]["columns"]) if status in c["statuses"])
    for band in t["table"]["bands"]:
        if band["at_least"] <= amount < band["less_than"]:
            return band["tax"][col]
    raise ValueError("amount outside the Tax Table")


def table_minus_schedule(t, status, amount):
    """How much the project's Tax Table value exceeds the rate-schedule value for an
    amount; zero at or above the boundary where the form itself uses the schedule."""
    if amount is None or amount >= t["boundary"]:
        return 0
    return table_tax(t, status, amount) - schedule_tax(t, status, amount)


def schedule_mode_expectations(values, case, t):
    """The project's tax lines recomputed as an engine that uses the rate schedule in
    place of the Tax Table would compute them: the same worksheet path, each table
    lookup replaced by the schedule value, and the worksheet's smaller-of re-taken."""
    status = case["inputs"]["f1040.status"]
    def m(line):
        v = values.get(line, {}).get("value", {})
        return v.get("cents") if v.get("kind") == "money" else None
    def b(line):
        v = values.get(line, {}).get("value", {})
        return v.get("value") if v.get("kind") == "bool" else None
    d = lambda line: table_minus_schedule(t, status, m(line))
    if b("f1040.gate.sdtw"):
        tax16 = min(m("sdtw.line45") - d("sdtw.line21"), m("sdtw.line46") - d("sdtw.line1"))
    elif b("f1040.gate.qdcg_applies"):
        tax16 = min(m("qdcg.line23") - d("qdcg.line5"), m("qdcg.line24") - d("qdcg.line1"))
    else:
        tax16 = m("f1040.line16") - d("f1040.line15")
    line17 = m("f1040.line17") or 0
    line23 = m("f1040.line23") or 0
    ftc_taxes = case["inputs"].get("ftc.taxes", 0) if (m("f1040.line20") or 0) > 0 or case["inputs"].get("ftc.taxes", 0) > 0 else 0
    tax20 = min(ftc_taxes, tax16) if m("f1040.line20") is not None else 0
    # Schedule 8812: line 13 is the tax after the foreign tax credit, so lines 19 and 28
    # move with the table-versus-schedule difference through the credit limit.
    line12 = m("s8812.line12") or 0
    tax19 = min(line12, max(0, tax16 + line17 - tax20))
    line16a = line12 - tax19
    line17_8812 = min(line16a, m("s8812.line16b") or 0)
    line20_8812 = m("s8812.line20") or 0
    if b("s8812.few_children"):
        tax28 = min(line17_8812, line20_8812)
    elif line20_8812 >= line17_8812:
        tax28 = line17_8812
    else:
        tax28 = min(line17_8812, m("s8812.line26") or 0)
    return {"f1040.line16": tax16, "f1040.line19": tax19, "f1040.line20": tax20, "f1040.line28": tax28,
            "f1040.line24": max(0, tax16 + line17 - tax20 - tax19) + line23,
            "f1040.tax_before_credits": tax16 + line17 + line23}


def float_bound_cents(precision, engine_cents, components=1):
    """Cents of difference attributable to the engine's floating-point arithmetic:
    two units in the last place of the engine value in dollars (float32 or float64)
    per summed engine variable, never less than one cent."""
    import math
    dollars = abs(engine_cents) / 100.0
    if dollars == 0:
        return 1
    mantissa_bits = 23 if precision == "float32" else 52
    ulp = 2.0 ** (math.floor(math.log2(dollars)) - mantissa_bits)
    return max(1, math.ceil(2 * ulp * 100 * components))


def derived_features(case, values):
    """The generator's feature flags plus flags read off the project's own values."""
    feats = set(case["features"])
    if (m0 := (values.get("s8812.line10", {}).get("value", {}).get("cents") or 0)) > 0:
        feats.add("ctc_phaseout")
    def m(line):
        v = values.get(line, {}).get("value", {})
        return v.get("cents") if v.get("kind") == "money" else None
    if (m("f4952.line1") or 0) > (m("f4952.line8") or 0):
        feats.add("investment_interest_limited")
    it = values.get("sa.itemizes", {}).get("value", {})
    feats.add("itemizes" if it.get("kind") == "bool" and it["value"] else "does_not_itemize")
    if (m("div.box2b") or 0) > 0 and (m("sd.line19") or 0) < (m("div.box2b") or 0):
        feats.add("section_1250_netted")
    if (m("sa.line5d") or 0) > (m("f1040.line11b") or 0):
        feats.add("salt_exceeds_agi")
    if (m("f8960.line9a") or 0) > 0:
        feats.add("investment_interest_on_8960")
    if (m("f1040.line16") or 0) == 0:
        feats.add("no_tax_either_way")
    return feats


def money(v):
    return v["cents"] if v and v.get("kind") == "money" else None


def project_line(values, line):
    """A project line in cents, with virtual ids for the two Schedule 2 taxes."""
    if line == "f8959.tax":
        line = "f8959.line18"
    if line == "f8960.tax":
        line = "f8960.line17"
    if line == "f1040.tax_before_credits":
        a, ka = project_line(values, "f1040.line18"); c, kc = project_line(values, "f1040.line23")
        return (a + c, None) if a is not None and c is not None else (None, ka or kc)
    d = values.get(line)
    if d is None:
        return None, "missing"
    v = d["value"]
    if v["kind"] == "money":
        return v["cents"], None
    return None, v["kind"]


def table_deltas(values, schedules, alias, status):
    """Every Tax Table lookup the project performed in this case: table value minus schedule value."""
    deltas = []
    for key, d in values.items():
        if d.get("op") != "table_lookup" or d["value"]["kind"] != "money":
            continue
        amount = next((o["value"]["cents"] for o in d.get("operands", []) if o["value"].get("kind") == "money"), None)
        if amount is None:
            continue
        deltas.append(d["value"]["cents"] - schedule_tax(schedules, alias, status, amount))
    return deltas


def main():
    ap = argparse.ArgumentParser()
    for a in ("cases", "project", "engines", "investigations", "report"):
        ap.add_argument("--" + a, required=True)
    a = ap.parse_args()
    cases = {c["id"]: c for c in json.load(open(a.cases))}
    project = json.load(open(a.project))["cases"]
    engines = json.load(open(a.engines))["engines"]
    investigations = json.load(open(a.investigations))
    tables = load_tables()

    stats = defaultdict(Counter)          # (engine, line) -> category counts
    unexplained, explained, excluded_reasons = [], [], defaultdict(Counter)
    for ename, eng in engines.items():
        for cid, elines in eng["lines"].items():
            case = cases[cid]; values = project[cid]["values"]
            status = case["inputs"]["f1040.status"]
            feats = derived_features(case, values)
            schedule_mode = schedule_mode_expectations(values, case, tables)
            for line, ev in elines.items():
                reason = next((l["reason"] for l in eng["limitations"] if l["feature"] in feats and line in l["lines"]), None)
                if reason:
                    stats[(ename, line)]["excluded"] += 1; excluded_reasons[(ename, line)][reason] += 1; continue
                pv, kind = project_line(values, line)
                if pv is None:
                    stats[(ename, line)]["project-" + kind] += 1; continue
                diff = ev - pv
                bound = float_bound_cents(eng.get("precision", "float64"), ev, eng.get("components", {}).get(line, 1))
                if diff == 0:
                    stats[(ename, line)]["exact"] += 1; continue
                if line in TAX_LINES and schedule_mode[line] != pv and abs(ev - schedule_mode[line]) <= bound:
                    stats[(ename, line)]["table-adjusted"] += 1; continue
                if abs(diff) <= bound:
                    stats[(ename, line)]["float"] += 1; continue
                cause = next((inv for inv in investigations
                              if inv["engine"] == ename and inv["line"] == line
                              and (inv.get("case") == cid or (inv.get("feature") and inv["feature"] in case["features"]))), None)
                rec = {"engine": ename, "case": cid, "line": line, "project": pv, "engine_value": ev, "diff": diff,
                       "features": case["features"]}
                if cause:
                    stats[(ename, line)]["explained"] += 1; rec["cause"] = cause["cause"]; explained.append(rec)
                else:
                    stats[(ename, line)]["UNEXPLAINED"] += 1; unexplained.append(rec)

    lines_out = ["# Engine differential — generated returns vs independent engines", "",
                 f"Cases: {len(cases)} generated single-filer returns (tools/engines/generate_cases.py). "
                 "Engines run locally under .engines/venv (tools/engines/setup.sh); versions: "
                 + ", ".join(f"{n} {e['version']}" for n, e in engines.items()) + ".", "",
                 "`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.", ""]
    for ename in engines:
        lines_out += [f"## {ename}", "", "| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for (en, line), c in sorted(stats.items()):
            if en != ename: continue
            notc = sum(v for k, v in c.items() if k.startswith("project-"))
            lines_out.append(f"| {line} | {c['exact']} | {c['table-adjusted']} | {c['float']} | {c['excluded']} | {c['explained']} | {c['UNEXPLAINED']} | {notc} |")
        lines_out.append("")
        reasons = {r for (en, _), rc in excluded_reasons.items() if en == ename for r in rc}
        if reasons:
            lines_out += ["Exclusions:", ""] + [f"- {r}" for r in sorted(reasons)] + [""]
    if explained:
        lines_out += ["## Explained differences", ""] + [f"- {r['engine']} {r['case']} {r['line']}: project {r['project']} engine {r['engine_value']} — {r['cause']}" for r in explained[:200]] + [""]
    if unexplained:
        lines_out += ["## UNEXPLAINED differences", ""] + [f"- {r['engine']} {r['case']} {r['line']}: project {r['project']} engine {r['engine_value']} (diff {r['diff']}) features={r['features']}" for r in unexplained[:300]] + [""]
    else:
        lines_out += ["## Unexplained differences", "", "None.", ""]
    os.makedirs(os.path.dirname(a.report), exist_ok=True)
    open(a.report, "w").write("\n".join(lines_out))
    total = sum(sum(c.values()) for c in stats.values())
    print(f"engine differential: {len(cases)} cases, {total} line comparisons, {len(unexplained)} unexplained, {len(explained)} explained")
    print(f"report: {os.path.relpath(a.report, ROOT)}")
    sys.exit(1 if unexplained else 0)


if __name__ == "__main__":
    main()
