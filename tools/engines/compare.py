#!/usr/bin/env python3
"""Compare the project's computed lines with the external engines' and write the report.

Categories per (engine, case, line):
  exact          engine equals the project to the cent
  table-adjusted engine equals the project's tax lines recomputed with every Tax
                 Table lookup replaced by the rate schedule (engines use the
                 schedule where the form uses the table); the recomputation keeps
                 the worksheet path and re-takes its smaller-of, so it is an
                 identified cause, not a tolerance
  table-midpoint for an engine whose record declares "tax_table": "midpoint-unrounded"
                 (UsTaxes), the engine equals the project's lines recomputed by its
                 methods: each Tax Table lookup replaced by the schedule at the band
                 midpoint without rounding (midpoint_tax), Form 8960 line 17 rounded to
                 whole dollars (niit_whole_dollar), and the lines that follow re-taken
  float         engine differs by no more than two units in the last place of its
                 floating-point representation (float32 for PolicyEngine-US, float64
                 for Tax-Calculator), a bound derived from the engine's precision
  unrounded      for an engine of precision "decimal2" (OpenTaxSolver: doubles, nothing
                 rounded, each program's lines printed to the cent), the engine equals
                 the project's own derivation of the line re-evaluated in exact
                 arithmetic without the project's cent rounding of products and ratios
                 (amb.<year>.multiplication_subcent), each value that passes between the
                 engine's programs taken at its printed cent, and the result printed to
                 the cent (UnroundedModel); an identified cause, not a tolerance
  excluded       the engine cannot model a feature of the case; reason recorded. The
                 features are the generator's, those derived here from the project's own
                 values, and those the engine's adapter reports about its own run
                 (engines.json `features`)
  explained      a disagreement with a cited cause in the investigation log, matched by
                 case id or by a feature (generator, derived or engine-reported)
  UNEXPLAINED    a disagreement with no cause; fails the run

Beside the Markdown report, a JSON summary of the same run (same path, .json)
gives, per engine and per mapped line, the counts the evidence report reads:
  project_line      the project line the mapped id names, in the form's line-id
                    form (an instance key such as person[taxpayer].se_line12 is
                    reduced to person.se_line12, as the evidence report keys its
                    lines), or null for a virtual sum of lines (f1040.tax_before_credits)
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
import argparse, glob, json, math, re, sys, os
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


def table_minus_schedule(t, status, amount, engine_tax=None):
    """How much the project's Tax Table value exceeds the engine's value for an amount (the
    rate-schedule value, or `engine_tax(t, status, amount)` for an engine with another table
    method); zero at or above the boundary where the form itself uses the schedule."""
    if amount is None or amount >= t["boundary"]:
        return 0
    return table_tax(t, status, amount) - (engine_tax or schedule_tax)(t, status, amount)


def midpoint_tax(t, status, amount):
    """The Tax Table emulated as UsTaxes does (irsForms/TaxTable.ts `computeTax`): the rate schedule
    applied at the midpoint of the table band holding the whole-dollar part of the amount ($5 bands
    from $5 to $25, $25 bands to $3,000, $50 bands to $100,000; nothing under $5), without the
    table's rounding to whole dollars. Every midpoint is a multiple of $2.50 and the schedule's
    rates are whole percents, so the value is a whole number of cents."""
    dollars = amount // 100
    if dollars < 5:
        return 0
    band = 5 if dollars < 25 else 25 if dollars < 3000 else 50
    return schedule_tax(t, status, (dollars - dollars % band) * 100 + band * 50)


def niit_whole_dollar(line16):
    """Form 8960 line 17 as UsTaxes figures it (irsForms/F8960.ts line 126, `Math.round(l16 * 0.038)`):
    3.8% of line 16 rounded to whole dollars, half up, in cents."""
    return (line16 * 38 + 50_000) // 100_000 * 100


def schedule_mode_expectations(values, case, t, engine_tax=None, niit=None):
    """The project's tax lines recomputed as an engine that uses the rate schedule in
    place of the Tax Table would compute them: the same worksheet path, each table
    lookup replaced by the schedule value, and the worksheet's smaller-of re-taken.
    With `engine_tax`, each lookup is replaced by that function's value instead (an engine
    with another table method), and with `niit` Form 8960 line 17 is recomputed from line
    16 by that function; the dict then also carries the lines that follow (Form 1040 lines
    18 and 21 to 37, Schedule 3 line 8, Schedule 8812 lines 14 to 27, the worksheet's tax
    lines and Schedule 2 line 21)."""
    status = case["inputs"]["f1040.status"]
    def m(line):
        v = values.get(line, {}).get("value", {})
        return v.get("cents") if v.get("kind") == "money" else None
    def b(line):
        v = values.get(line, {}).get("value", {})
        return v.get("value") if v.get("kind") == "bool" else None
    d = lambda line: table_minus_schedule(t, status, m(line), engine_tax)
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
    niit17 = niit(m("f8960.line16")) if niit and m("f8960.line16") is not None else (m("f8960.line17") or 0)
    line23 = (m("f1040.line23") or 0) - (m("f8960.line17") or 0) + niit17
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
    line22 = max(0, tax18 - tax20 - cdcc - savers - eehic - tax19 - rce)
    out = {"f1040.line16": tax16, "f1040.line19": tax19, "f1040.line20": tax20, "f1040.line28": tax28,
           "f1040.line24": line22 + line23,
           "f1040.tax_before_credits": tax18 + line23,
           "f2441.line11": cdcc, "s3.line2": cdcc, "f8880.line12": savers,
           "f5695.line15": rce, "s3.line5a": rce, "f5695.line32": eehic, "s3.line5b": eehic}
    if engine_tax is None and niit is None:
        return out
    line33 = (m("f1040.line33") or 0) - (m("f1040.line28") or 0) + tax28
    out.update({"f1040.line18": tax18, "f1040.line21": tax19 + tax20 + cdcc + savers + eehic + rce, "f1040.line22": line22,
                "f1040.line23": line23, "s2.line21": (m("s2.line21") or 0) - (m("f8960.line17") or 0) + niit17,
                "f8960.line17": niit17, "f8960.tax": niit17, "s3.line8": tax20 + cdcc + savers + eehic + rce,
                "f1040.line32": (m("f1040.line32") or 0) - (m("f1040.line28") or 0) + tax28, "f1040.line33": line33,
                "f1040.line34": max(0, line33 - (line22 + line23)), "f1040.line37": max(0, line22 + line23 - line33),
                "s8812.line14": tax19, "s8812.line16a": line16a, "s8812.line17": line17_8812, "s8812.line27": tax28})
    if m("qdcg.line22") is not None:
        q22, q23, q24 = m("qdcg.line22") - d("qdcg.line5"), m("qdcg.line23") - d("qdcg.line5"), m("qdcg.line24") - d("qdcg.line1")
        out.update({"qdcg.line22": q22, "qdcg.line23": q23, "qdcg.line24": q24, "qdcg.line25": min(q23, q24)})
    return out


def midpoint_mode_expectations(values, case, t):
    """The project's tax lines recomputed by the methods of an engine whose record declares
    "tax_table": "midpoint-unrounded" (UsTaxes): every Tax Table lookup replaced by the schedule at
    the band midpoint without rounding (midpoint_tax) and Form 8960 line 17 rounded to whole dollars
    (niit_whole_dollar), along the project's own worksheet path."""
    return schedule_mode_expectations(values, case, t, engine_tax=midpoint_tax, niit=niit_whole_dollar)


def float_bound_cents(precision, engine_cents, components=1):
    """Cents of difference attributable to a floating-point engine's arithmetic: two units in
    the last place of the engine value in dollars (float32 or float64) per summed engine
    variable, never less than one cent."""
    dollars = abs(engine_cents) / 100.0
    if dollars == 0:
        return 1
    mantissa_bits = 23 if precision == "float32" else 52
    ulp = 2.0 ** (math.floor(math.log2(dollars)) - mantissa_bits)
    return max(1, math.ceil(2 * ulp * 100 * components))


# ---------------------------------------------------------------------------------------------
# The `unrounded` reading: an engine that holds fractions of a cent (OpenTaxSolver) modelled exactly

# How far the double an engine holds can be from the exact value. For amounts under 2^30 cents
# (about $10.7 million; larger lines are not modelled) a double's unit in the last place is
# under 2.4e-7 cent; a line's
# chain of at most a few hundred operations, each rounding to half a unit, and the decimal
# inputs and rates, each read to half a unit, stay under 1e-4 cent. Only an exact value nearer
# than this to a half cent can print either way, and only a comparison or a table edge nearer
# than this can go either way in the engine.
DOUBLE_SLACK = Fraction(1, 1000)
MODELLED_LIMIT = 2 ** 30
# Lines the project reports as one value that the engine prints as the parts the adapter adds.
VIRTUAL_PARTS = {"f8959.tax": ["f8959.line18"], "f8960.tax": ["f8960.line17"],
                 "f1040.tax_before_credits": ["f1040.line18", "f1040.line23"]}


def load_lines():
    """Every canonical line by id (definition lines as <def>.<line>) and every table by id."""
    lines, tables = {}, {}
    for path in glob.glob(os.path.join(ROOT, "canonical", Y, "*.json")):
        doc = json.load(open(path))
        if isinstance(doc, dict) and isinstance(doc.get("form"), dict):
            for l in doc["form"]["lines"]:
                lines[l["id"]] = l
        if isinstance(doc, dict) and isinstance(doc.get("def"), dict):
            for l in doc["def"]["lines"]:
                lines[f"{doc['def']['id']}.{l['id']}"] = l
    for path in glob.glob(os.path.join(ROOT, "canonical", Y, "tables", "*.json")):
        t = json.load(open(path))["table"]
        tables[t["id"]] = t
    return lines, tables


def prints(x):
    """The cents a double near exact value x (cents) prints as with "%.2f": the nearer cent,
    or both neighbours when x is within the engine's slack of a half cent."""
    lo = math.floor(x)
    if abs(x - lo - Fraction(1, 2)) < DOUBLE_SLACK:
        return {lo, lo + 1}
    return {lo if x - lo < Fraction(1, 2) else lo + 1}


class UnroundedModel:
    """The project's derivation of one case re-evaluated as an engine that does not round
    computes it.

    Each derivation records its atom and its operands in evaluation order; this walks the
    same graph in exact rational arithmetic: a product or a prorated amount keeps its fraction
    (the project rounds it half-up to the cent), every other atom does what the project's does.
    A value that crosses from one of the engine's programs to another (`programs` in the
    adapter's `unrounded` declaration) is taken at the cent it prints; at an exact tie the
    engine's own printed line, where it shows one, says which cent it was. A line the adapter
    supplies as an amount (`supplied`) is that amount, and is modelled only where it equals the
    project's value, so a difference of substance is never absorbed. Where the exact values
    send a choice, a test or a table lookup another way than the project's, the model follows
    only when every alternative is a line the project evaluated and all agree; otherwise the
    line is not modelled (None) and its difference must be explained like any other."""

    def __init__(self, values, spec, supplied, engine_values, lines, tables):
        self.V, self.lines, self.tables = values, lines, tables
        self.supplied, self.ev = supplied, engine_values
        self.programs = [(re.compile(p), name) for p, name in spec.get("programs", [])]
        self.engine_line = spec.get("engine_line", {})
        self.first_pass = spec.get("first_pass", {})
        self.memo, self.program_memo = {}, {}

    # -- the engine's structure
    def program(self, key):
        if key not in self.program_memo:
            self.program_memo[key] = next((name for p, name in self.programs if p.search(key)), "Form 1040")
        return self.program_memo[key]

    def printed(self, key):
        """The cent the engine prints for a line and the next program reads, or None."""
        x = self.value(key)
        if not isinstance(x, Fraction):
            return None
        s = prints(x)
        if len(s) == 1:
            return Fraction(s.pop())
        at = key
        for _ in range(20):        # follow copies to the engine line that shows the value
            e = self.ev.get(self.engine_line.get(at, at))
            if e is not None:
                return Fraction(e) if e in s else None
            d = self.V.get(at)
            if d is None or d["op"] != "copy" or not d["operands"]:
                return None
            at = d["operands"][-1]["ref"]
        return None

    def predicted(self, line):
        """The set of cents the engine can print for a compared line, or None if not modelled."""
        parts = VIRTUAL_PARTS.get(line, [line])
        sets = []
        for p in parts:
            x = self.value(p)
            if not isinstance(x, Fraction) or abs(x) >= MODELLED_LIMIT:
                return None
            sets.append(prints(x))
        out = {0}
        for s in sets:
            out = {a + b for a in out for b in s}
        return out

    # -- reading derivations
    @staticmethod
    def plain(v):
        k = v.get("kind")
        if k == "money":
            return Fraction(v["cents"])
        if k == "rate":
            return Fraction(v["num"], v["den"])
        if k in ("bool", "enum", "count"):
            return v["value"]
        return None

    @staticmethod
    def is_constant(ref):
        return ref.startswith("#") or ref in ("true", "false") or ref.startswith('"') or re.fullmatch(r"-?\d+(\.\d+)?", ref) is not None

    def line_of(self, key):
        """The canonical line a derivation key evaluates, and the key of its frame."""
        if "|inst:" in key:
            cut = key.rfind("}.")
            frame = key[:cut + 1]
            seg = frame[frame.rfind("|inst:") + 6:]
            return self.lines.get(f"{seg[:seg.find('#')]}.{key[cut + 2:]}"), frame
        if "]" in key:
            cut = key.rfind("]")
            frame = key[:cut + 1]
            seg = frame[frame.rfind(".") + 1:]
            return self.lines.get(f"{seg[:seg.find('[')]}.{key[cut + 2:]}"), frame
        return self.lines.get(key), None

    @staticmethod
    def canonical(frame, line_id, raw):
        if frame is None:
            return raw
        if "|inst:" in frame:
            return f"{frame}.{raw}"
        doc = line_id.split(".")[0]
        return f"{frame}.{raw[len(doc) + 1:]}" if raw.startswith(doc + ".") else raw

    @staticmethod
    def instance_key(frame, sub):
        bind = json.dumps(sub["bind"], separators=(",", ":"), ensure_ascii=False)
        local = sub["line"][len(sub["def"]) + 1:] if sub["line"].startswith(sub["def"] + ".") else sub["line"]
        return f"{frame or 'root'}|inst:{sub['def']}#{bind}.{local}"

    def operand(self, o, consumer):
        r = o["ref"]
        if r in self.V:
            if o["value"].get("kind") == "money" and self.program(r) != self.program(consumer):
                return self.printed(r)
            return self.value(r)
        if self.is_constant(r):
            return self.plain(o["value"])
        return None

    def test(self, t, it, consumer):
        """Consume the operands the project's evaluator pushed for test t, in its order; return
        the project's outcome and the model's (None when the model cannot say)."""
        if "all" in t or "any" in t:
            is_all = "all" in t
            for sub in t["all" if is_all else "any"]:
                p, x = self.test(sub, it, consumer)
                if p != is_all:
                    return (not is_all), ((not is_all) if x == p else None)
                if x != p:
                    return is_all, None
            return is_all, is_all
        if "not" in t:
            p, x = self.test(t["not"], it, consumer)
            return (not p), (None if x is None else not x)
        key = next(k for k in ("eq", "ne", "lt", "le", "gt", "ge") if k in t)
        a, b = next(it), next(it)
        pa, pb = self.plain(a["value"]), self.plain(b["value"])
        xa, xb = self.operand(a, consumer), self.operand(b, consumer)
        rel = {"eq": lambda u, w: u == w, "ne": lambda u, w: u != w, "lt": lambda u, w: u < w,
               "le": lambda u, w: u <= w, "gt": lambda u, w: u > w, "ge": lambda u, w: u >= w}[key]
        p = rel(pa, pb)
        if xa is None or xb is None:
            return p, None
        if isinstance(xa, Fraction) and isinstance(xb, Fraction) and (xa, xb) != (pa, pb) and abs(xa - xb) < DOUBLE_SLACK:
            return p, None
        return p, rel(xa, xb)

    def value(self, key):
        if key not in self.memo:
            self.memo[key] = None          # a cycle is not modelled
            self.memo[key] = self._value(key)
        return self.memo[key]

    def _value(self, k):
        d = self.V[k]
        op, val, ops = d["op"], d["value"], list(d["operands"])
        if k in self.supplied:
            return Fraction(val["cents"]) if val.get("kind") == "money" and val["cents"] == self.supplied[k] else None
        if op in ("input", "param"):
            return self.plain(val)
        if op == "gate":
            return None
        line, frame = self.line_of(k)
        if op == "bound":
            if not ops:
                return self.plain(val)
            r = ops[0]["ref"]
            if r not in self.V and not self.is_constant(r):
                caller = k[:k.rfind("|inst:")]
                for cand in (f"{caller}.{r}", f"{caller}.{r.split('.', 1)[-1]}"):
                    if cand in self.V:
                        return self.value(cand)
                return None
            return self.operand(ops[0], k)
        if line is None:
            return None
        expr = line["expr"]
        gates = len(line.get("refuses") or [])
        if any(self.operand(g, k) is not False for g in ops[:gates]):
            return None
        it = iter(ops[gates:])
        if op == "test":
            return self.test(expr, it, k)[1]
        if op == "choose":
            taken = next((json.loads(n[len("taken: "):]) for n in d["notes"] if n.startswith("taken: ")), None)
            alts = expr["alternatives"]
            gi = next((i for i, a in enumerate(alts) if a["guard"] == taken), None)
            if gi is None:
                return None
            for alt in alts[:gi + 1]:
                p, x = self.test(alt["guard"], it, k)
                if x != p:
                    refs = [self.canonical(frame, line["id"], a["then"]) if isinstance(a["then"], str) else None for a in alts]
                    if all(r in self.V for r in refs):
                        vals = {self.value(r) for r in refs}
                        if len(vals) == 1 and None not in vals:
                            return vals.pop()
                    return None
            then = alts[gi]["then"]
            if isinstance(then, str):
                return self.operand(next(it), k)
            inner = self.instance_key(frame, then)
            return self.value(inner) if inner in self.V else None
        if op == "copy(instance)":
            inner = self.instance_key(frame, expr["from"])
            return self.value(inner) if inner in self.V else None
        if op == "sum_over":
            where, total = expr.get("where"), Fraction(0)
            while True:
                try:
                    if where:
                        p, x = self.test(where, it, k)
                        if x != p:
                            return None
                        if not p:
                            continue
                    o = next(it)
                except StopIteration:
                    break
                x = self.operand(o, k)
                if x is None:
                    return None
                total += x
            return total if val.get("kind") in ("money", "count") else None
        xs = []
        for o in it:
            x = self.operand(o, k)
            if x is None:
                return None
            xs.append((o["ref"], o["value"].get("kind"), x))
        money = [x for _, kind, x in xs if kind == "money"]
        # Where the exact operand is the project's own, a band or step edge is the project's
        # decision; where it moved, an edge within the engine's slack is not modelled.
        moved = bool(money) and money[0] != self.plain(next(o["value"] for o in ops[gates:] if o["value"].get("kind") == "money"))
        slack = DOUBLE_SLACK if moved else 0
        if k in self.first_pass:
            between = self.value(self.first_pass[k])
            if not isinstance(between, Fraction):
                return None
            if between != 0:
                # The adapter read the other operand from the first Form 1040 pass, before the
                # named deduction: not below the final pass's value, so only the smaller-of's
                # other operand, at or under the final value, is the same either way.
                return money[0] if op == "smaller_of" and money[0] <= money[1] else None
        if op == "copy":
            return xs[-1][2] if xs else None
        if op == "sum":
            return sum(money, Fraction(0))
        if op in ("subtract", "subtract_floor0"):
            r = money[0] - money[1]
            return max(Fraction(0), r) if op == "subtract_floor0" else r
        if op == "smaller_of":
            return min(money)
        if op == "larger_of":
            return max(money)
        if op == "multiply_count":
            return next(x for _, kind, x in xs if kind == "count") * money[0]
        if op == "multiply_rate":
            return next(x for _, kind, x in xs if kind == "rate") * money[0]
        if op == "prorate":
            # The ratio unrounded (OpenTaxSolver divides; the project rounds it to the places the
            # instruction names), not above one, times the amount, unrounded.
            def named(field):
                r = expr[field]
                return next(x for ref, _, x in xs if ref == r or ref.endswith("." + r.split(".", 1)[-1]))
            amount, part, whole = named("amount"), named("part"), named("whole")
            if whole <= 0:
                return None
            return amount * min(Fraction(1), max(Fraction(0), part / whole))
        if op == "round":
            u, x = expr["unit"], money[0]
            cell = {"up": lambda v: math.ceil(v / u), "down": lambda v: math.floor(v / u),
                    "half_up": lambda v: math.floor(v / u + Fraction(1, 2))}.get(expr["rule"])
            if cell is None or cell(x - slack) != cell(x + slack):
                return None
            return Fraction(cell(x) * u)
        if op == "keyed_lookup":
            return self.plain(val)
        if op == "rate_lookup":
            x = money[0]
            m = re.match(r"band over (\S+) but not over (\S+)", d["notes"][0])
            lo = None if m.group(1) == "-" else int(m.group(1))
            hi = None if m.group(2) == "-" else int(m.group(2))
            if (lo is None or x - slack > lo) and (hi is None or x + slack <= hi):
                return self.plain(val)
            return None
        if op == "table_lookup":
            x = money[0]
            status = next(x for _, kind, x in xs if kind == "enum")
            t = self.tables.get(expr["table"])
            if t is None:
                return None
            col = next((i for i, c in enumerate(t["columns"]) if status in c["statuses"]), None)
            band = next((b for b in t["bands"] if b["at_least"] <= x < b["less_than"]), None)
            if col is None or band is None or x - slack < band["at_least"] or x + slack >= band["less_than"]:
                return None
            return Fraction(band["tax"][col])
        return None


def derived_features(case, values):
    """The generator's feature flags plus flags read off the project's own values."""
    feats = set(case["features"])
    if (m0 := (values.get("s8812.line10", {}).get("value", {}).get("cents") or 0)) > 0:
        feats.add("ctc_phaseout")
    def m(line):
        v = values.get(line, {}).get("value", {})
        return v.get("cents") if v.get("kind") == "money" else None
    if (m("f4952.line3") or 0) > (m("f4952.line8") or 0):
        feats.add("investment_interest_limited")
    it = values.get("sa.itemizes", {}).get("value", {})
    feats.add("itemizes" if it.get("kind") == "bool" and it["value"] else "does_not_itemize")
    if (m("div.box2b") or 0) > 0 and (m("sd.line19") or 0) < (m("div.box2b") or 0):
        feats.add("section_1250_netted")
    # A negative AGI would otherwise fire this for every return with no state and local tax at all.
    if (m("sa.line5d") or 0) > 0 and (m("sa.line5d") or 0) > (m("f1040.line11b") or 0):
        feats.add("salt_exceeds_agi")
    if (m("f1040.line27a") or 0) > 0:
        feats.add("eic")
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
    if (m("f1040.line11b") or 0) - (m("f1040.line12e") or 0) - (m("f1040.line13b") or 0) < 0:
        feats.add("taxable_before_qbi_negative")
    # A tax-line amount sitting exactly on a Tax Table band boundary ($5 bands under $25, $25 under $3,000, $50 under $100,000).
    for amount_line in ("f1040.line15", "qdcg.line1", "qdcg.line5", "sdtw.line1", "sdtw.line21"):
        amt = m(amount_line) or 0
        band = 500 if amt < 2500 else 2500 if amt < 300000 else 5000
        if 0 < amt < 10_000_000 and amt % band == 0:
            feats.add("tax_table_band_edge")
    # Taxable income before the QBI deduction above the Form 8995 threshold: Form 8995-A, which the project refuses.
    use_a = values.get("qbi.use_8995a", {}).get("value", {})
    if use_a.get("kind") == "bool" and use_a["value"]:
        feats.add("qbi_above_threshold")
    # Schedule D Tax Worksheet line 4 carries Form 4952 line 4e although no Form 4952 is filed (no investment interest).
    if (m("f4952.line1") or 0) == 0 and (m("sdtw.line4") or 0) > 0:
        feats.add("sdtw_line4_without_4952")
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
    # Schedule 8812 line 20 (15% of earned income over $2,500) below line 17: the form's line 20 question decides line 27.
    if m("s8812.line20") is not None and m("s8812.line17") is not None and m("s8812.line20") < m("s8812.line17"):
        feats.add("s8812_line20_below_line17")
    # Additional Medicare Tax owed or withheld: Schedule 8812 line 21 comes from the Additional Medicare Tax and RRTA Tax Worksheet.
    if (m("f8959.line18") or 0) > 0 or (m("f8959.line24") or 0) > 0:
        feats.add("additional_medicare_tax")
    # Social security benefits with Schedule 1 additional income (unemployment compensation): Social Security Benefits Worksheet line 6.
    if (m("ssb.line1") or 0) > 0 and (m("s1.line10") or 0) != 0:
        feats.add("ssb_with_schedule1_income")
    # An itemizer with a state and local tax deduction: Form 8960 line 9b may allocate part of it to investment income.
    if feats & {"itemizes"} and (m("sa.line5e") or 0) > 0:
        feats.add("itemized_state_tax")
        # ... and modified AGI over the net investment income tax threshold (Form 8960 line 15), so line 9b reaches the tax.
        if (m("f8960.line15") or 0) > 0:
            feats.add("itemized_state_tax_niit")
    # A car loan interest deduction remains after the phase-out (Schedule 1-A line 30).
    if (m("s1a.line30") or 0) > 0:
        feats.add("car_loan_deduction")
    # The foreign tax credit is less than the foreign tax paid: the tax on line 16 limited it.
    if case["inputs"].get("ftc.taxes", 0) > (m("ftc.credit") or 0):
        feats.add("foreign_tax_limited")
    return feats


def money(v):
    return v["cents"] if v and v.get("kind") == "money" else None


VIRTUAL_LINES = {"f8959.tax": "f8959.line18", "f8960.tax": "f8960.line17", "f1040.tax_before_credits": None}


def template_id(key):
    """An instance key reduced to the form's line id, as the evidence report keys its lines:
    person[taxpayer].sc[biz].line31 -> sc.line31, person[taxpayer].se_line12 -> person.se_line12."""
    import re
    if "[" not in key:
        return key
    return re.sub(r"(?:[a-zA-Z0-9_]+\[[^\]]+\]\.)+", lambda m: m.group(0).split(".")[-2].split("[")[0] + ".", key)


def resolve_line(line):
    """The project line a mapped id names, in line-id form; None for a virtual sum of several lines."""
    line = VIRTUAL_LINES.get(line, line)
    return None if line is None else template_id(line)


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
    ap.add_argument("--dump", help="write every unexplained and explained record to this JSON file (the report lists the first 300)")
    a = ap.parse_args()
    cases = {c["id"]: c for c in json.load(open(a.cases))}
    project = json.load(open(a.project))["cases"]
    engines = json.load(open(a.engines))["engines"]
    investigations = json.load(open(a.investigations))
    tables = load_tables()
    canonical_lines, canonical_tables = load_lines()

    stats = defaultdict(Counter)          # (engine, line) -> category counts
    summary = defaultdict(Counter)        # (engine, line) -> compared / nonzero counts for the JSON summary
    unexplained, explained, excluded_reasons = [], [], defaultdict(Counter)
    for ename, eng in engines.items():
        for cid, elines in eng["lines"].items():
            case = cases[cid]; values = project[cid]["values"]
            status = case["inputs"]["f1040.status"]
            feats = derived_features(case, values) | set(eng.get("features", {}).get(cid, []))
            schedule_mode = schedule_mode_expectations(values, case, tables)
            # An engine that uses the Tax Table itself (OpenTaxSolver) has no table-adjusted reading.
            uses_table = bool(eng.get("tax_table"))
            # An engine that holds fractions of a cent is read through the model of its arithmetic,
            # built only when a difference needs it.
            unrounded = eng.get("precision") == "decimal2"
            model = None
            # An engine that emulates the Tax Table at the band midpoint without rounding (UsTaxes) is read against the
            # project's lines recomputed by that method.
            midpoint = midpoint_mode_expectations(values, case, tables) if eng.get("tax_table") == "midpoint-unrounded" else {}
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
                if diff == 0:
                    stats[(ename, line)]["exact"] += 1; continue
                if unrounded:
                    if model is None:
                        model = UnroundedModel(values, eng.get("unrounded", {}), eng.get("supplied", {}).get(cid, {}), elines,
                                               canonical_lines, canonical_tables)
                    if ev in (model.predicted(line) or ()):
                        stats[(ename, line)]["unrounded"] += 1; continue
                bound = 0 if unrounded else float_bound_cents(eng.get("precision", "float64"), ev, eng.get("components", {}).get(line, 1))
                if midpoint.get(line) is not None and midpoint[line] != pv and abs(ev - midpoint[line]) <= bound:
                    stats[(ename, line)]["table-midpoint"] += 1; continue
                if not uses_table and line in TAX_LINES and schedule_mode[line] != pv and abs(ev - schedule_mode[line]) <= bound:
                    stats[(ename, line)]["table-adjusted"] += 1; continue
                if not uses_table and line == "f1040.line27a" and (ef := eic_formula(values, tables)) is not None and abs(ev - ef) <= max(bound, 100):
                    stats[(ename, line)]["table-adjusted"] += 1; continue
                if not unrounded and abs(diff) <= bound:
                    stats[(ename, line)]["float"] += 1; continue
                cause = next((inv for inv in investigations
                              if inv["engine"] == ename and inv["line"] == line
                              and (inv.get("case") == cid or (inv.get("feature") and inv["feature"] in feats))), None)
                rec = {"engine": ename, "case": cid, "line": line, "project": pv, "engine_value": ev, "diff": diff,
                       "features": case["features"]}
                if cause:
                    stats[(ename, line)]["explained"] += 1; rec["cause"] = cause["cause"]; explained.append(rec)
                else:
                    stats[(ename, line)]["UNEXPLAINED"] += 1; unexplained.append(rec)

    lines_out = ["# Engine differential — generated returns vs independent engines", "",
                 f"Cases: {len(cases)} generated returns, single, head of household and married filing jointly (tools/engines/generate_cases.py). "
                 "Engines run locally under .engines/ (tools/engines/setup.sh); versions: "
                 + ", ".join(f"{n} {e['version']}" for n, e in engines.items()) + ".", "",
                 f"`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `unrounded` (OpenTaxSolver, which computes in doubles, rounds nothing and prints each program's lines to the cent) means the engine equals the project's own derivation of the line re-evaluated in exact arithmetic without the project's half-up cent rounding of products and ratios (amb.{Y}.multiplication_subcent), with each amount that passes between the engine's programs taken at the cent it prints and the result printed to the cent; where the exact value is within 1/1000 cent of a half cent either neighbouring cent is the print (an engine double stays within 1/10,000 cent of the exact value at these amounts). No difference is allowed beyond what that recomputation gives; a line the adapter supplies as an amount is recomputed only where the project's value is that amount, and a case whose exact values take another branch, test or table band than the project's is not recomputed. An identified cause, not a tolerance. OpenTaxSolver builds its tax from the Tax Table below $100,000 as the form does, so it has no `table-adjusted` reading. `table-midpoint` (UsTaxes, which emulates the Tax Table by applying the rate schedule at the midpoint of the band holding the whole-dollar amount, without the table's rounding to whole dollars, and rounds Form 8960 line 17 to whole dollars) means the engine equals the project's lines recomputed by those two methods along the project's own worksheet path: each Tax Table lookup replaced by the schedule at the band midpoint, Form 8960 line 17 by 3.8% of line 16 rounded half up to whole dollars, and the lines that follow (the worksheet's tax lines, Form 1040 lines 16 to 37, Schedule 8812 lines 14 to 27) re-taken; within the engine's `float` bound, it is an identified cause, not a tolerance. `excluded` lines carry the engine limitation stated below; the features that trigger them are the generator's, those read off the project's values, and those the engine's adapter reports about its own run. Every other difference must be explained in fixtures/{Y}/differential/engine_investigations.json or the run fails.", ""]
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
        lines_out += [f"## {ename}", "", "| line | exact | table-adjusted | table-midpoint | float | unrounded | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |",
                      "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for (en, line), c in sorted(stats.items()):
            if en != ename: continue
            notc = sum(v for k, v in c.items() if k.startswith("project-"))
            outside = notc - summary[(ename, line)]["not_computed_allowed"]
            lines_out.append(f"| {line} | {c['exact']} | {c['table-adjusted']} | {c['table-midpoint']} | {c['float']} | {c['unrounded']} | {c['excluded']} | {c['explained']} | {c['UNEXPLAINED']} | {notc} | {outside} ({shares[(ename, line)]:.1%}) |")
        lines_out.append("")
        reasons = {r for (en, _), rc in excluded_reasons.items() if en == ename for r in rc}
        if reasons:
            lines_out += ["Exclusions:", ""] + [f"- {r}" for r in sorted(reasons)] + [""]
        unmapped = engines[ename].get("pass_through", {}).get("unmapped", {})
        if unmapped:
            lines_out += ["Project result lines not mapped:", ""] + [f"- {line}: {why}" for line, why in unmapped.items()] + [""]
        rejected = engines[ename].get("rejected", [])
        if rejected:
            lines_out += [f"Cases the engine's programs rejected (no lines compared): {len(rejected)}: {', '.join(rejected[:20])}", ""]
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
                              "unexplained": c["UNEXPLAINED"], "exact": c["exact"], "table_adjusted": c["table-adjusted"], "table_midpoint": c["table-midpoint"],
                              "float": c["float"], "unrounded": c["unrounded"], "explained": c["explained"],
                              "not_computed": sum(v for k, v in c.items() if k.startswith("project-")),
                              "not_computed_allowed": sm["not_computed_allowed"],
                              "not_computed_share": round(shares[(ename, line)], 4)}
        summary_out["engines"][ename] = {"version": eng["version"], "pass_through": eng.get("pass_through", {"lines": [], "components": {}}),
                                         "limitations": eng.get("limitations", []), "rejected": eng.get("rejected", []), "lines": per_line}
    summary_out["not_computed_floor"] = {"share": NOT_COMPUTED_FLOOR, "allow": {l: {"input": i, "reason": r} for l, (i, r) in NOT_COMPUTED_ALLOW.items()},
                                         "exceeded": [{"engine": en, "line": line, "not_computed": n, "cases": total} for en, line, n, total in floor_failures]}
    if a.dump:
        open(a.dump, "w").write(json.dumps({"unexplained": unexplained, "explained": explained}, indent=1) + "\n")
    summary_path = os.path.splitext(a.report)[0] + ".json"
    open(summary_path, "w").write(json.dumps(summary_out, indent=1) + "\n")
    total = sum(sum(c.values()) for c in stats.values())
    print(f"engine differential: {len(cases)} cases, {total} line comparisons, {len(unexplained)} unexplained, {len(explained)} explained, "
          f"{len(floor_failures)} lines over the not-computed floor")
    print(f"report: {os.path.relpath(a.report, ROOT)}; summary: {os.path.relpath(summary_path, ROOT)}")
    sys.exit(1 if unexplained or floor_failures else 0)


if __name__ == "__main__":
    main()
