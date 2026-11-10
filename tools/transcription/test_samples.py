#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Tests of sampled standing reviews: samples.py, the completeness check's due/release split and ruling carry,
and the completeness tool's guard. Run by check_completeness.py --self-test."""
import os
import sys
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import samples  # noqa: E402
import spend  # noqa: E402
import check_completeness as CC  # noqa: E402
import completeness_review as CR  # noqa: E402

S = "subj1"


def rec(n, subject=S, grandfathered=False, bad=0):
    r = {"form": "f", "subject_sha": subject,
         "samples": [{"claims": []} for _ in range(n)] + [{"claims": [], "parse_error": True} for _ in range(bad)]}
    if grandfathered:
        r["grandfathered"] = True
    return r


class SampleTests(unittest.TestCase):
    def setUp(self):
        self.n = mock.patch.object(samples, "SAMPLES_PER_MILESTONE", 2)
        self.n.start()

    def tearDown(self):
        self.n.stop()

    def test_wanted(self):
        self.assertEqual(samples.wanted(None, S), (2, False))
        self.assertEqual(samples.wanted(rec(1), S), (1, False))
        self.assertEqual(samples.wanted(rec(2), S), (0, False))
        self.assertEqual(samples.wanted(rec(2), S, asked=1), (1, True))
        self.assertEqual(samples.wanted(rec(1, bad=1), S), (1, False), "an unparsed sample does not count")
        self.assertEqual(samples.wanted(rec(2), "changed"), (2, False), "a changed subject starts over")
        self.assertEqual(samples.wanted(rec(1, grandfathered=True), S), (0, False))
        self.assertEqual(samples.wanted(rec(1, grandfathered=True), S, asked=1), (1, True))
        self.assertEqual(samples.wanted(rec(1, grandfathered=True), "changed"), (2, False))

    def test_satisfied(self):
        self.assertFalse(samples.satisfied(rec(1)))
        self.assertTrue(samples.satisfied(rec(2)))
        self.assertTrue(samples.satisfied(rec(1, grandfathered=True)))

    def test_carry_matches_item_and_normalised_quote_on_same_form(self):
        ck = samples.carry_key
        found = [{"kind": "unruled", "line": "f#1.1", "form": "f", "carry": ck("f.a", "You must file.")},
                 {"kind": "unruled", "line": "f#2.3", "form": "f", "carry": ck("f.a", "you  MUST file")},
                 {"kind": "unruled", "line": "f#2.4", "form": "f", "carry": ck("f.b", "You must file.")},
                 {"kind": "unruled", "line": "g#1.1", "form": "g", "carry": ck("f.a", "You must file.")}]
        ruling = {"class": "covered", "evidence": "e", "line": "f.a", "subject_sha": S}
        got = CC.carried(found, {"unruled:f#1.1": ruling})
        self.assertEqual(set(got), {"unruled:f#2.3"})
        self.assertEqual(got["unruled:f#2.3"]["carried_from"], "unruled:f#1.1")

    def _findings(self, records, release):
        forms = [{"id": "f", "lines": []}]
        with mock.patch.object(CC, "prompt_for", lambda f, mani: ("prompt", [], S)):
            return CC.findings(forms, {}, records, release)

    def test_changed_subject_is_due_not_failed(self):
        found, _, due, _ = self._findings({"f": rec(2, subject="old")}, release=False)
        self.assertEqual(found, [])
        self.assertEqual([d[0] for d in due], ["f"])

    def test_release_fails_on_due_and_short(self):
        found, _, _, _ = self._findings({"f": rec(2, subject="old")}, release=True)
        self.assertEqual([f["kind"] for f in found], ["due"])
        found, _, _, _ = self._findings({"f": rec(1)}, release=True)
        self.assertEqual([f["kind"] for f in found], ["short"])
        found, _, _, _ = self._findings({"f": rec(1, grandfathered=True)}, release=True)
        self.assertEqual(found, [])

    def test_claims_keyed_by_sample(self):
        r = rec(0)
        r["samples"] = [{"claims": [{"item": "a", "quote": "q"}]}, {"claims": [{"item": "a", "quote": "q"}, {"item": "b"}]}]
        found, _, _, _ = self._findings({"f": r}, release=False)
        self.assertEqual([f["line"] for f in found], ["f#1.1", "f#2.1", "f#2.2"])

    def test_plan_refuses_beyond_milestone_without_force(self):
        form = {"id": "f"}
        with mock.patch.object(CR, "prompt_for", lambda f, mani, forms=None: ("x" * 1000, [], S)), \
             mock.patch.object(CR, "context_forms", lambda: []):
            price = {("completeness_review.py", "claude"): 0.001}
            p = CR.plan([form], {}, {"f": rec(2)}, 1, None, price, "claude-opus-5-5")[0]
            self.assertEqual(p["jobs"], [])
            self.assertIn("refused", p["note"])
            p = CR.plan([form], {}, {"f": rec(2)}, 1, "calibration", price, "claude-opus-5-5")[0]
            self.assertEqual([j["k"] for j in p["jobs"]], [3])
            self.assertAlmostEqual(p["jobs"][0]["usd"], 1.0)
            p = CR.plan([form], {}, {"f": rec(1, subject="old")}, None, None, price, "claude-opus-5-5")[0]
            self.assertEqual([j["k"] for j in p["jobs"]], [1, 2], "a changed subject starts at sample 1")

    def test_gate_refuses_above_owner_gate(self):
        jobs = [{"kind": "completeness", "form": "f", "run": True, "usd": 2.0}] * 2
        self.assertIn("exceeds", spend.gate(jobs, None))
        self.assertIsNone(spend.gate(jobs, 4.0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
