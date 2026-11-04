#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Unit tests for the matching and tolerance logic of tools/engines/compare.py, on synthetic
tables and derivations: no engine, no canonical data.

    python3 tools/engines/test_compare.py      (in check-all)
"""
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare as C  # noqa: E402

# A two-bracket schedule (10% to $1,000, then 20%) and a Tax Table of $50 bands to $2,000.
SCHED = {"schedules": {"single": [{"over": 0, "upper": 100_000, "base": 0, "rate": {"num": 10, "den": 100}},
                                  {"over": 100_000, "upper": None, "base": 10_000, "rate": {"num": 20, "den": 100}}]},
         "alias": {"hoh": "single"}, "boundary": 200_000,
         "table": {"columns": [{"statuses": ["single", "hoh"]}],
                   "bands": [{"at_least": a, "less_than": a + 5_000, "tax": [C.half_up((a + 2_500) * 10, 100)]}
                             for a in range(0, 200_000, 5_000)]}}


def money(c):
    return {"kind": "money", "cents": c}


def der(op, value, operands=(), notes=(), guards=()):
    return {"op": op, "value": value, "operands": [{"ref": r, "value": v} for r, v in operands],
            "notes": list(notes), "guardsNotTaken": list(guards)}


class Arithmetic(unittest.TestCase):
    def test_half_up(self):
        self.assertEqual([C.half_up(n, 2) for n in (1, 3, 5)], [1, 2, 3])
        self.assertEqual(C.half_up(149, 100), 1)
        self.assertEqual(C.half_up(150, 100), 2)

    def test_schedule_and_table(self):
        self.assertEqual(C.schedule_tax(SCHED, "single", 50_000), 5_000)
        self.assertEqual(C.schedule_tax(SCHED, "hoh", 150_000), 20_000)  # an aliased status
        self.assertEqual(C.table_tax(SCHED, "single", 52_499), C.half_up(52_500 * 10, 100))
        with self.assertRaises(ValueError):
            C.table_tax(SCHED, "single", 200_000)

    def test_table_minus_schedule_stops_at_the_boundary(self):
        self.assertEqual(C.table_minus_schedule(SCHED, "single", 50_000), 250)  # the band midpoint is $25 above
        self.assertEqual(C.table_minus_schedule(SCHED, "single", 200_000), 0)
        self.assertEqual(C.table_minus_schedule(SCHED, "single", None), 0)

    def test_midpoint_tax_bands(self):
        self.assertEqual(C.midpoint_tax(SCHED, "single", 499), 0)                       # under $5
        self.assertEqual(C.midpoint_tax(SCHED, "single", 2_000), C.schedule_tax(SCHED, "single", 2_250))   # $5 bands
        self.assertEqual(C.midpoint_tax(SCHED, "single", 2_999_99), C.schedule_tax(SCHED, "single", 298_750))  # $25 bands
        self.assertEqual(C.midpoint_tax(SCHED, "single", 3_000_00), C.schedule_tax(SCHED, "single", 302_500))  # $50 bands

    def test_niit_whole_dollar(self):
        self.assertEqual(C.niit_whole_dollar(1_315_700), 50_000)  # $499.966 -> $500
        self.assertEqual(C.niit_whole_dollar(1_302_600), 49_500)  # $494.988 -> $495


class Tolerances(unittest.TestCase):
    def test_float_bound(self):
        self.assertEqual(C.float_bound_cents("float64", 0), 1)
        self.assertEqual(C.float_bound_cents("float64", 10_000_000_00), 1)
        # float32 at $100,000: an ulp of 2^16 / 2^23 dollars, two of them about 1.6 cents
        self.assertEqual(C.float_bound_cents("float32", 10_000_000), 2)
        self.assertEqual(C.float_bound_cents("float32", 10_000_000, components=3), 5)
        self.assertGreater(C.float_bound_cents("float32", 10_000_000_00), C.float_bound_cents("float32", 10_000_000))

    def test_prints(self):
        self.assertEqual(C.prints(Fraction(1049, 10)), {105})
        self.assertEqual(C.prints(Fraction(1041, 10)), {104})
        self.assertEqual(C.prints(Fraction(209, 2)), {104, 105})                   # an exact half cent
        self.assertEqual(C.prints(Fraction(209, 2) + Fraction(1, 2000)), {104, 105})  # within the slack
        self.assertEqual(C.prints(Fraction(209, 2) + Fraction(1, 500)), {105})

    def category(self, ev, pv, line="x.line1", bound=0, unrounded=False, uses_table=False, predicted=None,
                 midpoint=None, ptc=None, schedule_mode=None, eic=None):
        return C.identified_category(line, ev, pv, bound, unrounded, uses_table, predicted or (lambda: None),
                                     midpoint or {}, ptc or {}, schedule_mode or {}, eic or (lambda: None))

    def test_identified_categories(self):
        self.assertEqual(self.category(100, 100), "exact")
        self.assertEqual(self.category(101, 100, bound=1), "float")
        self.assertIsNone(self.category(102, 100, bound=1))
        self.assertEqual(self.category(101, 100, unrounded=True, predicted=lambda: {101}), "unrounded")
        # an engine of exact cents is never read with a float bound
        self.assertIsNone(self.category(101, 100, bound=1, unrounded=True, predicted=lambda: {100}))
        self.assertEqual(self.category(150, 100, midpoint={"x.line1": 151}, bound=1), "table-midpoint")
        self.assertEqual(self.category(150, 100, ptc={"x.line1": Fraction(301, 2)}, bound=1), "contribution-unrounded")
        tax = "f1040.line16"
        self.assertEqual(self.category(150, 100, line=tax, schedule_mode={tax: 150}), "table-adjusted")
        self.assertIsNone(self.category(150, 100, line=tax, uses_table=True, schedule_mode={tax: 150}))
        self.assertEqual(self.category(199, 100, line="f1040.line27a", eic=lambda: 100), "table-adjusted")  # within $1
        self.assertIsNone(self.category(201, 100, line="f1040.line27a", eic=lambda: 100))

    def test_a_reading_equal_to_the_project_explains_nothing(self):
        # A recomputation that gives the project's own value cannot account for the engine's.
        self.assertIsNone(self.category(150, 100, midpoint={"x.line1": 100}))
        self.assertIsNone(self.category(150, 100, line="f1040.line16", schedule_mode={"f1040.line16": 100}))

    def test_lazy_readings(self):
        def boom():
            raise AssertionError("computed although not reached")
        self.assertEqual(self.category(100, 100, unrounded=True, predicted=boom, eic=boom), "exact")


class Matching(unittest.TestCase):
    LIMITS = [{"feature": "hsa", "lines": ["f8889.line13"], "reason": "no HSA"},
              {"feature": "amt", "lines": ["f1040.line16", "f8889.line13"], "reason": "no AMT"}]
    INV = [{"engine": "A", "line": "f1040.line16", "case": "c1", "cause": "by case"},
           {"engine": "A", "line": "f1040.line16", "feature": "amt", "cause": "by feature"},
           {"engine": "B", "line": "f1040.line16", "case": "c2", "cause": "other engine"}]

    def test_limitation(self):
        self.assertEqual(C.limitation_reason(self.LIMITS, {"amt", "hsa"}, "f8889.line13"), "no HSA")
        self.assertEqual(C.limitation_reason(self.LIMITS, {"amt"}, "f8889.line13"), "no AMT")
        self.assertIsNone(C.limitation_reason(self.LIMITS, {"hsa"}, "f1040.line16"))

    def test_cause(self):
        self.assertEqual(C.find_cause(self.INV, "A", "f1040.line16", "c1", set())["cause"], "by case")
        self.assertEqual(C.find_cause(self.INV, "A", "f1040.line16", "c9", {"amt"})["cause"], "by feature")
        self.assertIsNone(C.find_cause(self.INV, "A", "f1040.line16", "c2", set()))   # another engine's case
        self.assertIsNone(C.find_cause(self.INV, "A", "f1040.line19", "c1", {"amt"}))  # another line

    def test_line_ids(self):
        self.assertEqual(C.template_id("person[taxpayer].sc[biz].line31"), "sc.line31")
        self.assertEqual(C.template_id("person[taxpayer].se_line12"), "person.se_line12")
        self.assertEqual(C.resolve_line("f8959.tax"), "f8959.line18")
        self.assertIsNone(C.resolve_line("f1040.tax_before_credits"))

    def test_project_line(self):
        values = {"f1040.line18": {"value": money(500)}, "f1040.line23": {"value": money(25)},
                  "f8960.line17": {"value": money(7)}, "x.flag": {"value": {"kind": "bool", "value": True}}}
        self.assertEqual(C.project_line(values, "f1040.tax_before_credits"), (525, None))
        self.assertEqual(C.project_line(values, "f8960.tax"), (7, None))
        self.assertEqual(C.project_line(values, "x.flag"), (None, "bool"))
        self.assertEqual(C.project_line(values, "x.none"), (None, "missing"))


class Unrounded(unittest.TestCase):
    """The model of an engine that keeps fractions of a cent."""
    LINES = {
        "f.rate": {"id": "f.rate", "expr": {"op": "input"}},
        "f.a": {"id": "f.a", "expr": {"op": "input"}},
        "f.prod": {"id": "f.prod", "expr": {"op": "multiply_rate"}},
        "f.small": {"id": "f.small", "expr": {"op": "input"}},
        "f.pick": {"id": "f.pick", "expr": {"op": "choose", "alternatives": [
            {"guard": {"op": "test", "gt": ["f.a", {"const": 0}]}, "then": "f.small"},
            {"guard": {"op": "test", "eq": ["f.a", "f.a"]}, "then": "f.prod"}]}},
        "f.band": {"id": "f.band", "expr": {"op": "rate_lookup", "table": "bands"}},
        "f.round": {"id": "f.round", "expr": {"op": "round", "unit": 100, "rule": "half_up"}},
    }
    TABLES = {"bands": {"id": "bands", "kind": "rate_bands", "rate_bands": [
        {"over": None, "not_over": 1000, "rates": [{"num": 1, "den": 10}]},
        {"over": 1000, "not_over": None, "rates": [{"num": 2, "den": 10}]}]}}

    def model(self, values, supplied=None, engine=None):
        return C.UnroundedModel(values, {}, supplied or {}, engine or {}, self.LINES, self.TABLES)

    def base(self, a=1001, rate=(1, 3)):
        prod = Fraction(a) * Fraction(*rate)
        V = {"f.a": der("input", money(a)), "f.rate": der("input", {"kind": "rate", "num": rate[0], "den": rate[1]}),
             "f.prod": der("multiply_rate", money(int(prod + Fraction(1, 2))), [("f.a", money(a)), ("f.rate", {"kind": "rate", "num": rate[0], "den": rate[1]})]),
             "f.small": der("input", money(5))}
        return V, prod

    def test_product_kept_exact(self):
        V, prod = self.base()
        m = self.model(V)
        self.assertEqual(m.value("f.prod"), prod)          # 1001/3 cents, the project prints 334
        self.assertEqual(m.predicted("f.prod"), {334})

    def test_supplied_amount_only_where_it_is_the_project_value(self):
        V, _ = self.base()
        self.assertEqual(self.model(V, supplied={"f.prod": 334}).value("f.prod"), 334)
        self.assertIsNone(self.model(V, supplied={"f.prod": 333}).value("f.prod"))

    def test_choose_follows_the_guard_taken(self):
        V, prod = self.base(a=0)
        alts = self.LINES["f.pick"]["expr"]["alternatives"]
        guards = [{"guard": json.dumps(alts[0]["guard"]), "value": {"kind": "bool", "value": False}}]
        V["f.pick"] = der("choose", money(0), [("f.a", money(0)), ("0", money(0)), ("f.a", money(0)), ("f.a", money(0)), ("f.prod", money(0))],
                          notes=["taken: (prose the model must not need)"], guards=guards)
        self.assertEqual(C.UnroundedModel.taken_guard(V["f.pick"], alts), 1)
        self.assertEqual(self.model(V).value("f.pick"), prod)
        # no guard held, one undecided, or guards that are not the line's own: not modelled
        self.assertIsNone(C.UnroundedModel.taken_guard({**V["f.pick"], "guardsNotTaken": guards * 2}, alts))
        self.assertIsNone(C.UnroundedModel.taken_guard({**V["f.pick"], "value": {"kind": "unknown"}}, alts))
        other = [{"guard": json.dumps({"op": "test", "lt": ["f.a", {"const": 0}]}), "value": {"kind": "bool", "value": False}}]
        self.assertIsNone(C.UnroundedModel.taken_guard({**V["f.pick"], "guardsNotTaken": other}, alts))

    def band(self, key, project_key=None):
        V = {"f.a": der("input", money(key))}
        pk = key if project_key is None else project_key
        rate = {"kind": "rate", "num": 1, "den": 10} if pk <= 1000 else {"kind": "rate", "num": 2, "den": 10}
        V["f.band"] = der("rate_lookup", rate, [("f.a", money(pk))], notes=["(prose the model must not need)"])
        return V

    def test_rate_band_from_the_table(self):
        self.assertEqual(C.UnroundedModel(self.band(1000), {}, {}, {}, self.LINES, self.TABLES).taken_band(
            self.LINES["f.band"]["expr"], self.band(1000)["f.band"]["operands"])["not_over"], 1000)
        self.assertEqual(self.model(self.band(1000)).value("f.band"), Fraction(1, 10))
        self.assertEqual(self.model(self.band(1001)).value("f.band"), Fraction(2, 10))

    def test_rate_band_edge_within_slack_is_not_modelled(self):
        # The exact key moved (supplied as an amount the engine's previous program printed) to the edge.
        V = self.band(1000)
        V["f.a"] = der("multiply_rate", money(1000), [("f.small", money(5)), ("f.rate", {"kind": "rate", "num": 200, "den": 1})])
        V["f.small"] = der("input", money(5))
        V["f.rate"] = der("input", {"kind": "rate", "num": 200, "den": 1})
        self.assertEqual(self.model(V).value("f.band"), Fraction(1, 10))  # exact 1000, not moved: the project's band
        V["f.rate"] = der("input", {"kind": "rate", "num": 2000001, "den": 10000})
        self.assertIsNone(self.model(V).value("f.band"))  # 1000.0005: moved within the slack of the edge

    def test_round_edge(self):
        V = {"f.a": der("input", money(150)), "f.round": der("round", money(200), [("f.a", money(150))])}
        self.assertEqual(self.model(V).value("f.round"), 200)


if __name__ == "__main__":
    unittest.main(verbosity=1)
