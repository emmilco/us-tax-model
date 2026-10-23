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

Beside the Markdown report, a JSON summary of the same run (same path, .json)
gives, per engine and per mapped line, the counts the evidence report reads:
  project_line      the project line the mapped id names, or null for a virtual
                    sum of lines (f1040.tax_before_credits)
  compared          cases where both sides had a value and no limitation applied
  compared_nonzero  of those, cases where the project value was not zero
  excluded          cases set aside under an engine limitation
  excluded_nonzero  of those, cases where the project value was computed and not zero
  unexplained       compared cases whose difference has no cited cause
  not_computed      cases where the project had no money value for the line
  not_computed_allowed  of those, cases the allow-list covers (the form is not filed)
  not_computed_share    the rest as a share of the engine's cases; over
                    NOT_COMPUTED_FLOOR the run fails
together with the category counts above, the engine's version and its
pass-through declarations (run_engines.py). The summary's not_computed_floor
records the floor, the allow-list and any line over it.
"""
import argparse, json, sys, os
from fractions import Fraction
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
TAX_LINES = {"f1040.line16", "f1040.line19", "f1040.line20", "f1040.line24", "f1040.line28", "f1040.tax_before_credits",
             "f2441.line11", "s3.line2", "f8880.line12", "f5695.line15", "s3.line5a", "f5695.line32", "s3.line5b"}
# The run fails when, on a mapped line, the project left more than this share of the engine's cases
# without a value, unless the line is allow-listed below: the project value is unknown where the
# named input is false (the form is not filed), and the share is measured on the other returns.
NOT_COMPUTED_FLOOR = 0.05
NOT_COMPUTED_ALLOW = {
    "f2441.line9c": ("f2441.care", "Form 2441 is not filed without care expenses; Schedule 3 line 2 carries the zero and is compared on every return"),
    "f2441.line11": ("f2441.care", "Form 2441 is not filed without care expenses; Schedule 3 line 2 carries the zero and is compared on every return"),
    "f5695.line13": ("f5695.part1_any", "Form 5695 Part I is not filed without Part I costs; Schedule 3 line 5a carries the zero and is compared on every return"),
    "f5695.line15": ("f5695.part1_any", "Form 5695 Part I is not filed without Part I costs; Schedule 3 line 5a carries the zero and is compared on every return"),
    "f5695.line30": ("f5695.part2_any", "Form 5695 Part II is not filed without Part II costs; Schedule 3 line 5b carries the zero and is compared on every return"),
    "f5695.line32": ("f5695.part2_any", "Form 5695 Part II is not filed without Part II costs; Schedule 3 line 5b carries the zero and is compared on every return"),
}


def half_up(n, d):
    return (2 * n + d) // (2 * d)


def load_tables():
    sched = json.load(open(os.path.join(ROOT, "canonical", Y, "tables", "rate_schedule.json")))["table"]
    table = json.load(open(os.path.join(ROOT, "canonical", Y, "tables", "tax_table.json")))["table"]
    params = json.load(open(os.path.join(ROOT, "canonical", Y, "params.json")))["params"]["values"]
    boundary = params["ordinary.table_boundary"]["value"]
    return {"schedules": sched["schedules"], "alias": sched.get("status_alias", {}), "table": table, "boundary": boundary, "params": params}


def eic_formula(values, t):
    """Form 1040 line 27a recomputed along the project's own Worksheet A path with each EIC Table
    lookup replaced by the credit at the exact amount: the smaller of amount x (maximum / earned income
    amount) and the maximum, less (maximum / (completed - threshold phaseout)) x the excess over the
    threshold phaseout, not below zero. The rates are those the Rev. Proc. 2024-40 amounts imply. None
    when the project did not reach the worksheet."""
    def v(k):
        d = values.get(k, {}).get("value", {})
        return d.get("cents", d.get("value")) if d.get("kind") in ("money", "count", "bool", "enum") else None
    if v("eic.eligible") is not True:
        return 0 if v("eic.eligible") is False else None
    n, status, ei, agi = v("eic.ssn_count"), v("f1040.status"), v("eic.line1"), v("eic.line3")
    if None in (n, status, ei, agi):
        return None
    k, side = min(n, 3), "joint" if status == "mfj" else "other"
    P = lambda name: Fraction(t["params"][name]["value"])
    mx, eia = P(f"eic.maximum{k}"), P(f"eic.earned_amount{k}")
    thr, end = P(f"eic.ws_threshold{0 if k == 0 else 1}.{side}"), P(f"eic.limit{k}.{side}")
    def credit(x):
        c = min(Fraction(x) * mx / eia, mx) - mx / (end - thr) * max(Fraction(0), Fraction(x) - thr)
        return max(Fraction(0), c)
    line2 = credit(ei) if ei >= 100 else Fraction(0)
    if agi == ei or agi < thr:
        return round(line2)
    return round(min(credit(agi), line2))


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
    if m("f1040.line15") is None or m("f1040.line16") is None:
        # A return the project refuses or leaves incomplete has no schedule-mode expectations.
        return {line: None for line in TAX_LINES}
    if b("f1040.gate.sdtw"):
        tax16 = min(m("sdtw.line45") - d("sdtw.line21"), m("sdtw.line46") - d("sdtw.line1"))
    elif b("f1040.gate.qdcg_applies"):
        tax16 = min(m("qdcg.line23") - d("qdcg.line5"), m("qdcg.line24") - d("qdcg.line1"))
    else:
        tax16 = m("f1040.line16") - d("f1040.line15")
    line17 = m("f1040.line17") or 0
    line23 = m("f1040.line23") or 0
    tax18 = tax16 + line17
    ftc_taxes = case["inputs"].get("ftc.taxes", 0) if (m("f1040.line20") or 0) > 0 or case["inputs"].get("ftc.taxes", 0) > 0 else 0
    tax20 = min(ftc_taxes, tax16) if m("f1040.line20") is not None else 0
    # Schedule 3 lines 2, 4 and 5b: each credit is the smaller of its amount before the limit and the
    # tax left after the credits before it (Form 2441 line 10, Form 8880 line 11, Form 5695 line 31).
    remaining = max(0, tax18 - tax20)
    cdcc = min(m("f2441.line9c") or 0, remaining) if case["inputs"].get("f2441.care") else 0
    remaining = max(0, remaining - cdcc)
    savers = min(m("f8880.line10") or 0, remaining)
    remaining = max(0, remaining - savers)
    eehic = min(m("f5695.line30") or 0, remaining) if case["inputs"].get("f5695.part2_any") else 0
    # Schedule 8812: Credit Limit Worksheet A line 3 is the tax after those credits, so lines 19 and 28
    # move with the table-versus-schedule difference through the credit limit. With Worksheet B (Form
    # 5695 Part I and a qualifying child) the residential clean energy credit, limited after the Worksheet
    # B child tax credit, is taken first through Worksheet A line 4; otherwise it follows line 19.
    clw_a3 = tax18 - tax20 - cdcc - savers - eehic
    line12 = m("s8812.line12") or 0
    worksheet_b = bool(b("s8812.clwb_complete"))
    ctc_before_rce = (m("s8812.clwb_14") or 0) if worksheet_b else min(line12, clw_a3)
    rce = min(m("f5695.line13") or 0, max(0, clw_a3 - ctc_before_rce)) if case["inputs"].get("f5695.part1_any") else 0
    tax19 = min(line12, max(0, clw_a3 - (rce if worksheet_b else 0)))
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
            "f1040.line24": max(0, tax18 - tax20 - cdcc - savers - eehic - tax19 - rce) + line23,
            "f1040.tax_before_credits": tax18 + line23,
            "f2441.line11": cdcc, "s3.line2": cdcc, "f8880.line12": savers,
            "f5695.line15": rce, "s3.line5a": rce, "f5695.line32": eehic, "s3.line5b": eehic}


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
    if 0 < (m("sli.line8") or 0) < (m("sli.line1") or 0):
        feats.add("sli_phaseout")
    if (m("f1040.line16") or 0) == 0:
        feats.add("no_tax_either_way")
        if (m("f1040.line13b") or 0) > 0:
            feats.add("schedule1a_zero_tax")
    if (m("s3.line4") or 0) > 0:
        feats.add("savers_credit")
    if (m("f1040.line11b") or 0) < 0:
        feats.add("negative_agi")
    # Schedule 8812 Credit Limit Worksheet A: an engine that subtracts the Form 5695 Part I credit, or
    # omits the saver's credit, in line 2 changes line 14 only where the child tax credit does not fit
    # under its own limit.
    line12, clw_a3 = m("s8812.line12") or 0, m("s8812.clw_a3") or 0
    if (m("f5695.line13") or 0) > 0 and line12 > clw_a3 - (m("f5695.line13") or 0):
        feats.add("rce_displaces_ctc")
    if (m("s3.line4") or 0) > 0 and line12 > clw_a3:
        feats.add("savers_displaces_ctc")
    # The IRA deduction is below the contributions: the worksheet's phase-out or compensation limit applied.
    if (m("s1.line20") or 0) < (m("ira.line11a") or 0):
        feats.add("ira_phaseout")
    # A part's phase-out lines are figured from modified AGI whether or not the part is claimed;
    # the step matters only where the part has an amount to reduce.
    if any((m(cut) or 0) > 0 and (m(amount) or 0) > 0
           for cut, amount in (("s1a.line12", "s1a.line7"), ("s1a.line20", "s1a.line15"), ("s1a.line29", "s1a.line24"))):
        feats.add("schedule1a_stepped_phaseout")
    return feats


def money(v):
    return v["cents"] if v and v.get("kind") == "money" else None


VIRTUAL_LINES = {"f8959.tax": "f8959.line18", "f8960.tax": "f8960.line17", "f1040.tax_before_credits": None}


def resolve_line(line):
    """The project line a mapped id names; None for a virtual sum of several lines."""
    return VIRTUAL_LINES.get(line, line)


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
    summary = defaultdict(Counter)        # (engine, line) -> compared / nonzero counts for the JSON summary
    unexplained, explained, excluded_reasons = [], [], defaultdict(Counter)
    for ename, eng in engines.items():
        for cid, elines in eng["lines"].items():
            case = cases[cid]; values = project[cid]["values"]
            status = case["inputs"]["f1040.status"]
            feats = derived_features(case, values)
            schedule_mode = schedule_mode_expectations(values, case, tables)
            for line, ev in elines.items():
                pv, kind = project_line(values, line)
                reason = next((l["reason"] for l in eng["limitations"] if l["feature"] in feats and line in l["lines"]), None)
                if reason:
                    stats[(ename, line)]["excluded"] += 1; excluded_reasons[(ename, line)][reason] += 1
                    if pv is not None and pv != 0:
                        summary[(ename, line)]["excluded_nonzero"] += 1
                    continue
                if pv is None:
                    stats[(ename, line)]["project-" + kind] += 1
                    allow = NOT_COMPUTED_ALLOW.get(line)
                    if allow and not case["inputs"].get(allow[0]):
                        summary[(ename, line)]["not_computed_allowed"] += 1
                    continue
                summary[(ename, line)]["compared"] += 1
                if pv != 0:
                    summary[(ename, line)]["compared_nonzero"] += 1
                diff = ev - pv
                bound = float_bound_cents(eng.get("precision", "float64"), ev, eng.get("components", {}).get(line, 1))
                if diff == 0:
                    stats[(ename, line)]["exact"] += 1; continue
                if line in TAX_LINES and schedule_mode[line] != pv and abs(ev - schedule_mode[line]) <= bound:
                    stats[(ename, line)]["table-adjusted"] += 1; continue
                if line == "f1040.line27a" and (ef := eic_formula(values, tables)) is not None and abs(ev - ef) <= max(bound, 100):
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
                 f"Cases: {len(cases)} generated returns, single, head of household and married filing jointly (tools/engines/generate_cases.py). "
                 "Engines run locally under .engines/venv (tools/engines/setup.sh); versions: "
                 + ", ".join(f"{n} {e['version']}" for n, e in engines.items()) + ".", "",
                 f"`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/{Y}/differential/engine_investigations.json or the run fails.", ""]
    # The not-computed floor: the share of the engine's cases on which the project left the line without a
    # value, outside the allow-list's unfiled-form cases.
    shares, floor_failures = {}, []
    for (ename, line), c in stats.items():
        notc = sum(v for k, v in c.items() if k.startswith("project-"))
        outside = notc - summary[(ename, line)]["not_computed_allowed"]
        shares[(ename, line)] = outside / max(1, sum(c.values()))
        if shares[(ename, line)] > NOT_COMPUTED_FLOOR:
            floor_failures.append((ename, line, outside, sum(c.values())))
    lines_out += [f"Not-computed floor: the run fails when the project left more than {NOT_COMPUTED_FLOOR:.0%} of an engine's cases without a value on a mapped line "
                  "(a refusal, an unknown input, a non-money value), measured outside the allow-listed returns that do not file the form: "
                  + "; ".join(f"{line} unknown where `{inp}` is false ({reason})" for line, (inp, reason) in sorted(NOT_COMPUTED_ALLOW.items())) + ".", ""]
    for ename in engines:
        lines_out += [f"## {ename}", "", "| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |",
                      "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for (en, line), c in sorted(stats.items()):
            if en != ename: continue
            notc = sum(v for k, v in c.items() if k.startswith("project-"))
            outside = notc - summary[(ename, line)]["not_computed_allowed"]
            lines_out.append(f"| {line} | {c['exact']} | {c['table-adjusted']} | {c['float']} | {c['excluded']} | {c['explained']} | {c['UNEXPLAINED']} | {notc} | {outside} ({shares[(ename, line)]:.1%}) |")
        lines_out.append("")
        reasons = {r for (en, _), rc in excluded_reasons.items() if en == ename for r in rc}
        if reasons:
            lines_out += ["Exclusions:", ""] + [f"- {r}" for r in sorted(reasons)] + [""]
        unmapped = engines[ename].get("pass_through", {}).get("unmapped", {})
        if unmapped:
            lines_out += ["Project result lines not mapped:", ""] + [f"- {line}: {why}" for line, why in unmapped.items()] + [""]
    if floor_failures:
        lines_out += ["## NOT-COMPUTED FLOOR EXCEEDED", ""] + [f"- {en} {line}: {n} of {total} cases without a project value" for en, line, n, total in floor_failures] + [""]
    if explained:
        lines_out += ["## Explained differences", ""] + [f"- {r['engine']} {r['case']} {r['line']}: project {r['project']} engine {r['engine_value']} — {r['cause']}" for r in explained[:200]] + [""]
    if unexplained:
        lines_out += ["## UNEXPLAINED differences", ""] + [f"- {r['engine']} {r['case']} {r['line']}: project {r['project']} engine {r['engine_value']} (diff {r['diff']}) features={r['features']}" for r in unexplained[:300]] + [""]
    else:
        lines_out += ["## Unexplained differences", "", "None.", ""]
    os.makedirs(os.path.dirname(a.report), exist_ok=True)
    open(a.report, "w").write("\n".join(lines_out))
    summary_out = {"cases": len(cases), "engines": {}}
    for ename, eng in engines.items():
        per_line = {}
        for (en, line), c in sorted(stats.items()):
            if en != ename: continue
            sm = summary[(ename, line)]
            per_line[line] = {"project_line": resolve_line(line),
                              "compared": sm["compared"], "compared_nonzero": sm["compared_nonzero"],
                              "excluded": c["excluded"], "excluded_nonzero": sm["excluded_nonzero"],
                              "unexplained": c["UNEXPLAINED"], "exact": c["exact"], "table_adjusted": c["table-adjusted"],
                              "float": c["float"], "explained": c["explained"],
                              "not_computed": sum(v for k, v in c.items() if k.startswith("project-")),
                              "not_computed_allowed": sm["not_computed_allowed"],
                              "not_computed_share": round(shares[(ename, line)], 4)}
        summary_out["engines"][ename] = {"version": eng["version"], "pass_through": eng.get("pass_through", {"lines": [], "components": {}}),
                                         "lines": per_line}
    summary_out["not_computed_floor"] = {"share": NOT_COMPUTED_FLOOR, "allow": {l: {"input": i, "reason": r} for l, (i, r) in NOT_COMPUTED_ALLOW.items()},
                                         "exceeded": [{"engine": en, "line": line, "not_computed": n, "cases": total} for en, line, n, total in floor_failures]}
    summary_path = os.path.splitext(a.report)[0] + ".json"
    open(summary_path, "w").write(json.dumps(summary_out, indent=1) + "\n")
    total = sum(sum(c.values()) for c in stats.values())
    print(f"engine differential: {len(cases)} cases, {total} line comparisons, {len(unexplained)} unexplained, {len(explained)} explained, "
          f"{len(floor_failures)} lines over the not-computed floor")
    print(f"report: {os.path.relpath(a.report, ROOT)}; summary: {os.path.relpath(summary_path, ROOT)}")
    sys.exit(1 if unexplained or floor_failures else 0)


if __name__ == "__main__":
    main()
