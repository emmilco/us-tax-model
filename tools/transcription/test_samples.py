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

    def test_release_refuses_rulings_confirming_open_medium_or_high_bugs(self):
        import bug_status
        inventory = "".join(f"## {b} — t\n\n- **Symptom:** s\n{extra}\n" for b, extra in [
            ("BUG-0001", "- **Severity:** medium; wording.\n"), ("BUG-0002", "- **Severity:** low.\n"),
            ("BUG-0003", "- **Severity:** high.\n- **Fix:** done.\n"), ("BUG-0004", ""), ("BUG-0005", "- **Severity:** high.\n")])
        entries, _ = bug_status.derive(inventory, {}, "", "")
        rulings = {
            "unruled:a#1": {"class": "real gap", "bug": "BUG-0001"},                       # open medium: refused
            "unruled:b#1": {"class": "real gap", "bug": "BUG-0002"},                       # open low: accepted
            "unruled:c#1": {"class": "defect: x (BUG-0003)", "bugs": []},                 # fixed high: accepted
            "unruled:d#1": {"class": "no gate defect", "bugs": ["BUG-0004"]},              # open, no severity: refused
            "unruled:e#1": {"class": "no gate defect", "reason": "as BUG-0005 records",   # context only: accepted
                            "findings": [{"class": "covered", "evidence": "BUG-0005"}]},
            "unruled:f#1": {"class": "no gate defect", "findings": [{"class": "defect", "evidence": "see BUG-0005"}]},
        }
        self.assertEqual(samples.open_defects(rulings, entries),
                         [("unruled:a#1", "BUG-0001", "medium"), ("unruled:d#1", "BUG-0004", None), ("unruled:f#1", "BUG-0005", "high")])
        with mock.patch("builtins.print") as out:
            self.assertEqual(samples.release_open_bugs(rulings, allow=False, entries=entries), 1)
            self.assertEqual(samples.release_open_bugs(rulings, allow=True, entries=entries), 0)
        allowed = [c.args[0] for c in out.call_args_list if c.args[0].startswith("  allowed open bug: ")]
        self.assertEqual(len(allowed), 3)
        self.assertEqual(samples.release_open_bugs({k: rulings[k] for k in ("unruled:b#1", "unruled:c#1", "unruled:e#1")},
                                                   allow=False, entries=entries), 0)

    def test_a_class_ruling_no_defect_confirms_no_bug_it_names(self):
        """An id in a ruling's class is confirmed only when the class classes a defect or a real gap."""
        self.assertEqual(samples.confirmed_bugs({"class": "no gate defect; the finding is the prompt's text (BUG-0800)"}), set())
        self.assertEqual(samples.confirmed_bugs({"class": "no defect (as BUG-0123, already fixed)"}), set())
        self.assertEqual(samples.confirmed_bugs({"class": "covered by BUG-0124"}), set())
        self.assertEqual(samples.confirmed_bugs({"class": "defect: x (BUG-0125)"}), {"BUG-0125"})
        self.assertEqual(samples.confirmed_bugs({"class": "low defect: x (BUG-0126)"}), {"BUG-0126"})
        self.assertEqual(samples.confirmed_bugs({"class": "defect (medium) in part: BUG-0127"}), {"BUG-0127"})
        self.assertEqual(samples.confirmed_bugs({"class": "no gate defect", "findings": [
            {"class": "low defect", "evidence": "BUG-0128"}]}), {"BUG-0128"})

    def test_claims_keyed_by_sample(self):
        r = rec(0)
        r["samples"] = [{"claims": [{"item": "a", "quote": "q"}]}, {"claims": [{"item": "a", "quote": "q"}, {"item": "b"}]}]
        found, _, _, _ = self._findings({"f": r}, release=False)
        self.assertEqual([f["line"] for f in found], ["f#1.1", "f#2.1", "f#2.2"])

    def test_plan_refuses_beyond_milestone_without_force(self):
        form = {"id": "f"}
        with mock.patch.object(CR, "prompt_for", lambda f, mani, forms=None: ("x" * 1000, [], S)), \
             mock.patch.object(CR, "context_forms", lambda: []):
            price = {("completeness_review.py", "claude"): (0.0, 0.001)}
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
