#!/usr/bin/env python3
"""Offline regression tests for independence, noise accounting and response provenance."""
import contextlib
import json
import io
import re
import sys
import tempfile
import subprocess
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_families as C
import transcribe as T
import render_compare as R
import classm as M
import yaml
import families
import rulings
import rule
import audit_skipped as skipped
import audit_transcription as transcription_audit
import input_contracts as contracts
import adapter_contracts as adapters
import carry
import migrate_line_subjects as ML
import input_context


def log(statuses, rulings=None):
    return {"lines": {str(i): {"status": s, "reason": "test reason", "ruling": (rulings or {}).get(i, "")}
                      for i, s in enumerate(statuses)}, "duplicates": []}


class RulingContext(unittest.TestCase):
    def test_changed_input_wording_reopens_identical_expression_disagreement(self):
        """The BUG-0121 failure: the formula key survives a changed input premise."""
        with tempfile.TemporaryDirectory() as temp, patch.object(rulings, "REVIEWS", temp), \
                patch.object(T, "LOGS", temp), patch.object(T.subjects, "current", return_value="a" * 64):
            Path(temp, "transcription").mkdir()
            args = ({"id": "x", "title": "Test form"}, "claude-opus-5-5")
            rows = [{"printed": "1", "label": "Expenses", "status": "DISAGREE",
                     "project": '{"input":"x.expenses"}', "second": '{"line":"2"}'}]
            def write(prompt):
                return T.write_log(*args, prompt, [], rows, [], "lines: []", {})
            write("Input: 2025 care paid in 2026")
            self.assertEqual(rule.apply("x", {"1": "representation; input covers the required expenses"}), ["1"])
            side = rulings.load("transcription", "x")
            self.assertTrue(next(iter(side.values()))["context"])
            write("Input: 2025 care paid in 2026")
            path = Path(rulings.log_path("transcription", "x"))
            self.assertNotIn("Ruling: open", path.read_text())
            write("Input: all 2025 incurred care, regardless of payment date")
            self.assertIn("Ruling: open", path.read_text())

    def test_legacy_rulings_are_preserved_but_not_automatically_reused(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(rulings, "REVIEWS", temp):
            Path(temp, "render").mkdir()
            key = ("1", "amount", "objection")
            rulings.save("render", "x", {key: {"ruling": "Ruling: scope; old rationale", "drop": False}})
            self.assertIn(key, rulings.load("render", "x"))
            self.assertEqual(rulings.kept("render", "x", context="new context"), {})

    def test_context_tracks_subject_sources_system_and_case_prompts(self):
        header = "| subject sha256 | " + "a" * 64 + " |\n| prompt sha256 | " + "b" * 64 + " |\n"
        header += "| system sha256 | " + "c" * 64 + " |\n| date | 2026-10-23 |\n"
        header += "| irs | 2025 | 1 | whole document | " + "d" * 64 + " | - | - |\n"
        context = rulings.review_context("render", header)
        self.assertEqual(context, rulings.review_context("render", header.replace("2026-10-23", "2026-10-24")))
        for token in ("a" * 64, "b" * 64, "c" * 64, "d" * 64):
            self.assertNotEqual(context, rulings.review_context("render", header.replace(token, "e" * 64)))
        case = "\n## Lines\n\n### case classm.x.1 — prompt sha256 " + "f" * 64 + "; branches: test\n"
        self.assertNotEqual(rulings.review_context("classm", header + case),
                            rulings.review_context("classm", header + case.replace("f" * 64, "e" * 64)))

    def test_context_survives_sidecar_roundtrip_for_dropped_classm_values(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(rulings, "REVIEWS", temp):
            Path(temp, "classm").mkdir()
            key = ("classm.x.1", "1", "$1", "$2")
            entry = {"ruling": "Ruling: model error; arithmetic", "drop": True, "context": "abc"}
            rulings.save("classm", "x", {key: entry})
            self.assertEqual(rulings.load("classm", "x")[key], entry)
            self.assertTrue(rulings.kept("classm", "x", context="abc")[key].endswith(" [dropped]"))
            self.assertEqual(rulings.kept("classm", "x", context="changed"), {})

    def test_render_writer_reuses_only_its_own_recorded_context(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(rulings, "REVIEWS", temp), \
                patch.object(R, "LOGS", temp), patch.object(R.subjects, "current", return_value="a" * 64):
            Path(temp, "render").mkdir()
            def write(prompt):
                return R.write_log({"id": "x", "title": "Test"}, "claude-opus-5-5", prompt, [],
                                   [{"key": "1", "label": "Test", "encoded": "source amount"}],
                                   {"1": {"status": "MISMATCH", "reason": "source objection"}}, "raw", {})
            write("original prompt")
            rule.apply("x", {"1": "scope; unsupported case"}, "render")
            path = Path(rulings.log_path("render", "x"))
            write("original prompt")
            self.assertNotIn("Ruling: open", path.read_text())
            write("changed prompt")
            self.assertIn("Ruling: open", path.read_text())

    def test_classm_writer_context_matches_its_case_headings(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(rulings, "REVIEWS", temp), \
                patch.object(M, "LOGS", temp), patch.object(M.subjects, "current", return_value="a" * 64), \
                patch.object(M, "fixture_path", return_value=str(Path(temp, "fixtures.json"))):
            Path(temp, "classm").mkdir()
            job = {"id": "classm.x.1", "branches": [], "inputs": {},
                   "fill": [{"id": "x.line1", "printed": "1", "label": "Test", "type": "Dollars"}],
                   "project": {"x.line1": {"kind": "money", "cents": 100}}}
            run = {"used": [], "verdicts": {"1": {"value": 2}}, "raw": "raw", "prompt_sha": "b" * 64}
            def write():
                return M.write_outputs({"id": "x", "title": "Test"}, "claude-opus-5-5", [job],
                                       {job["id"]: run}, {job["id"]: {"model_reported": ["claude-opus-5-5"]}})
            write()
            rule.apply("x", {"classm.x.1 — 1": "scope; synthetic test ruling"}, "classm")
            path = Path(rulings.log_path("classm", "x"))
            write()
            self.assertNotIn("Ruling: open", path.read_text())
            run["prompt_sha"] = "c" * 64
            write()
            self.assertIn("Ruling: open", path.read_text())


class OptionalStaleLogs(unittest.TestCase):
    """check_logs.py: a stale optional-family log fails only when it would earn second-family credit if it
    were current; one that would not is reported as stale-ineligible and passes."""

    def run_check(self, blockers, stale="subject changed since the review"):
        import check_logs
        with tempfile.TemporaryDirectory() as d:
            for stem in ("f1", families.stem("f1", "deepseek")):
                Path(d, stem + ".md").write_text("# log\n", encoding="utf-8")
            quality = {"quality": {"state": "pending", "blockers": blockers}}
            out = io.StringIO()
            with patch.object(check_logs.subjects, "log_state", return_value=stale), \
                 patch.object(check_logs.compare_families, "compare", return_value=quality), \
                 contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                failed = check_logs.check("render", d, "RENDER_LOGS_OPTIONAL", ["f1"], "deepseek", required=False)
        return failed, out.getvalue()

    def test_stale_ineligible_log_is_reported_not_failed(self):
        failed, out = self.run_check(["stale subject: deepseek", "model-error noise above 10%"])
        self.assertFalse(failed)
        self.assertIn("f1: stale-ineligible", out)
        self.assertIn("model-error noise above 10%", out)

    def test_stale_log_eligible_when_current_fails(self):
        failed, out = self.run_check(["stale subject: claude, deepseek", "stale source snapshot: i1040gi",
                                      "no verified current request context for deepseek: required input/interface hash differs"])
        self.assertTrue(failed)
        self.assertNotIn("stale-ineligible", out)

    def test_current_ineligible_log_still_passes(self):
        failed, out = self.run_check(["model-error noise above 10%"], stale=None)
        self.assertFalse(failed)
        self.assertNotIn("stale-ineligible", out)

    def test_required_family_stale_log_fails_whatever_its_eligibility(self):
        import check_logs
        with tempfile.TemporaryDirectory() as d:
            Path(d, "f1.md").write_text("# log\n", encoding="utf-8")
            with patch.object(check_logs.subjects, "log_state", return_value="subject changed"), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertTrue(check_logs.check("render", d, "RENDER_LOGS_OPTIONAL", ["f1"], families.DEFAULT, required=True))


class RenderedSubject(unittest.TestCase):
    def test_citation_text_never_reaches_the_rendered_subject(self):
        import subjects
        line = "- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)\n"
        moved = line.replace("boxes 1–16", "box 1a")
        plain = "- Cite: [f1040] Form 1040 (2025), line 9 (2025; sha256 0123abcd)\n"
        self.assertEqual(subjects.of_rendered("x\n" + line), subjects.of_rendered("x\n" + moved))
        self.assertEqual(subjects.of_rendered(plain), subjects.of_rendered(plain.replace("line 9", "line 10")))
        self.assertNotEqual(subjects.of_rendered("Adds lines 1 and 2\n" + line), subjects.of_rendered("Adds lines 1 and 3\n" + line))


class RenderContext(unittest.TestCase):
    def documents(self):
        def entry(lid, printed, encoded):
            return {"id": lid, "printed": printed, "label": lid, "type": "NonNegDollars",
                    "encoded": encoded, "refusals": []}
        return {
            "root": {"root.credit": entry("root.credit", "11", "Add person.credit over every confirmed person entry.")},
            "person": {
                "person.credit": entry("person.credit", "credit", "Choose — [line eligible = true → line excess] [line eligible = false → line zero]"),
                "person.eligible": entry("person.eligible", "eligible", "Test line wages is greater than 100."),
                "person.excess": entry("person.excess", "excess", "Subtract 10 from line withheld."),
                "person.wages": entry("person.wages", "wages", "Add w2.box3 over every confirmed w2 entry."),
                "person.withheld": entry("person.withheld", "withheld", "Add w2.box4 over every confirmed w2 entry."),
                "person.zero": entry("person.zero", "zero", "Zero."),
            },
            "w2": {"w2.box3": entry("w2.box3", "3", "Input from box 3."),
                   "w2.box4": entry("w2.box4", "4", "Input from box 4.")},
        }

    def test_foreign_printed_fields_follow_their_local_dependencies(self):
        docs = self.documents()
        with patch.object(R, "rendered", side_effect=lambda fid: docs[fid]), \
                patch.object(R, "form_ids", return_value=set(docs)), patch.object(R, "def_titles", return_value={}):
            gloss = R.glossary("root", list(docs["root"].values()))
        ids = [e["id"] for _, e in gloss]
        self.assertEqual(set(ids), set(docs["person"]) | set(docs["w2"]))
        self.assertEqual(len(ids), len(set(ids)))

    def test_local_references_do_not_capture_other_forms_or_marker_prefixes(self):
        docs = self.documents()
        docs["person"]["person.one"] = {**docs["w2"]["w2.box3"], "id": "person.one", "printed": "1"}
        with patch.object(R, "rendered", side_effect=lambda fid: docs[fid]), patch.object(R, "form_ids", return_value=set(docs)):
            self.assertEqual(R.local_printed_refs("Enter w2 line 1 and line 11.", "person"), [])
            self.assertEqual(R.local_printed_refs("Enter person line 1.", "person"), ["person.one"])

    def test_a_prior_year_input_reference_is_not_a_current_calculation_dependency(self):
        docs = self.documents()
        docs["root"]["root.credit"]["encoded"] = "Add person.carry over every confirmed person entry."
        docs["person"]["person.carry"] = {**docs["person"]["person.zero"], "id": "person.carry",
                                          "printed": "(helper)", "encoded": "Input — Last year's line credit."}
        with patch.object(R, "rendered", side_effect=lambda fid: docs[fid]), \
                patch.object(R, "form_ids", return_value=set(docs)), patch.object(R, "def_titles", return_value={}):
            gloss = R.glossary("root", list(docs["root"].values()))
        self.assertEqual([e["id"] for _, e in gloss], ["person.carry"])

    def test_glossary_source_citations_are_selected_without_exposing_yaml(self):
        docs = self.documents()
        sources = {fid: {"id": fid, "title": fid, "tax_year": 2025,
                         "lines": [{"id": e["id"], "printed": e["printed"],
                                    "cite": {"doc": "irs", "locator": "p. 1"},
                                    "expr": {"op": "copy", "from": "PRIVATE_YAML_OPERAND"}}
                                   for e in entries.values()]} for fid, entries in docs.items()}
        with patch.object(R, "rendered", side_effect=lambda fid: docs[fid]), \
                patch.object(R, "form_ids", return_value=set(docs)), patch.object(R, "def_titles", return_value={}), \
                patch.object(R, "load_form", side_effect=lambda fid: sources[fid]):
            context = R.source_context(sources["root"])
            prompt = R.build_prompt(sources["root"], "ARCHIVED IRS TEXT")
        self.assertEqual(len(context["lines"]), 9)
        self.assertIn("person line eligible", prompt)
        self.assertIn("person line excess", prompt)
        self.assertIn("person line withheld", prompt)
        self.assertNotIn("PRIVATE_YAML_OPERAND", prompt)

    def test_real_schedule3_context_contains_withholding_and_foreign_tax_sources(self):
        context = R.source_context(T.load_form("s3"))
        excerpt, used = T.excerpt_for(context, T.manifest())
        pages = {row["doc"]: set(row["pages"]) for row in used}
        self.assertIn(117, pages["i1040gi"])
        self.assertIn(1, pages["i1116"])
        self.assertIn("Figure this amount separately for you and your spouse", excerpt)
        prompt = R.build_prompt(T.load_form("s3"), excerpt)
        self.assertIn("person line eligible", prompt)
        self.assertIn("person line excess", prompt)


class NoiseRule(unittest.TestCase):
    def test_skipped_worked_values_cannot_dilute_noise_or_earn_credit(self):
        expected = log(["AGREE"] + ["SKIPPED"] * 9)
        second = log(["DISAGREE"] + ["SKIPPED"] * 9, {0: "model error; arithmetic"})
        result = C.quality("classm", expected, second)
        self.assertEqual(result["judged"], 1)
        self.assertTrue(result["above_limit"])
        self.assertEqual(C.quality("classm", log(["SKIPPED"]), log(["SKIPPED"]))["state"], "no lines")
        self.assertEqual(C.quality("classm", log(["AGREE"]), log(["SKIPPED"]))["missing"], ["0"])

    def test_skips_are_not_reported_as_disputes_or_independence_findings(self):
        a = log(["AGREE", "SKIPPED", "SKIPPED"])
        b = log(["SKIPPED", "SKIPPED", "AGREE"])
        for record, model in ((a, "claude-opus-5-5"), (b, "deepseek-flash")):
            record.update(model=model, reported=model, subject="same", policy="test", sources=[])
        with patch.object(C, "parse_log", side_effect=[a, b]), patch.object(C.subjects, "current", return_value="same"):
            result = C.compare("classm", "f2441", "deepseek")
        self.assertEqual(result["judged"], [])
        self.assertEqual(result["yield"], [])
        self.assertEqual(result["both_disputed"], [])

    def test_correct_systematic_objection_is_not_noise(self):
        expected = log(["MATCH"] * 10)
        second = log(["MISMATCH"] * 10, {i: "finding; source p. 1 says a different amount" for i in range(10)})
        result = C.quality("render", expected, second)
        self.assertEqual(result["state"], "pass")
        self.assertEqual(result["model_errors"], 0)

    def test_unprovided_interface_contract_stays_pending_without_counting_as_model_noise(self):
        result = C.quality('transcription', log(['AGREE']), log(['DISAGREE'], {0: 'interface gap; the IRS does not define this adapter'}))
        self.assertEqual(result['state'], 'pending')
        self.assertEqual(result['model_errors'], 0)
        self.assertEqual(result['categories']['0'], 'interface_gap')

    def test_one_in_ten_model_errors_passes_but_one_in_nine_does_not(self):
        for n, state in ((10, "pass"), (9, "pending")):
            with self.subTest(n=n):
                result = C.quality("render", log(["MATCH"] * n),
                                   log(["MISMATCH"] + ["MATCH"] * (n - 1), {0: "model error; source p. 1 supports the project"}))
                self.assertEqual(result["state"], state)

    def test_representation_scope_and_ambiguity_are_not_noise(self):
        for ruling in ("representation; distinct equivalent structure", "scope; the situation is refused",
                       "ambiguity; owner chose the documented reading", "equivalent; same value"):
            with self.subTest(ruling=ruling):
                self.assertEqual(C.quality("transcription", log(["AGREE"]), log(["DISAGREE"], {0: ruling}))["state"], "pass")

    def test_open_or_unclassified_rulings_do_not_earn_evidence(self):
        for ruling in ("", "open", "project retained because I say so"):
            self.assertEqual(C.quality("render", log(["MATCH"]), log(["UNCLEAR"], {0: ruling}))["state"], "pending")

    def test_missing_lines_cannot_improve_noise_eligibility(self):
        second = log(["MATCH"] * 9 + ["MISSING"])
        result = C.quality("render", log(["MATCH"] * 10), second)
        self.assertEqual(result["judged"], 9)
        self.assertEqual(result["state"], "pending")
        self.assertEqual(result["missing"], ["9"])

    def test_invalid_and_duplicate_verdicts_cannot_pass(self):
        invalid = C.quality("render", log(["MATCH"]), log(["FOO"]))
        duplicate = log(["MATCH"]); duplicate["duplicates"] = ["0"]
        self.assertEqual(invalid["state"], "pending")
        self.assertEqual(C.quality("render", log(["MATCH"]), duplicate)["state"], "pending")

    def test_extra_lines_cannot_dilute_model_errors(self):
        result = C.quality("render", log(["MATCH"]),
                           log(["MISMATCH"] + ["MATCH"] * 10, {0: "model error; unsupported claim"}))
        self.assertEqual(result["judged"], 1)
        self.assertEqual(result["model_errors"], 1)
        self.assertTrue(result["above_limit"])
        self.assertEqual(result["state"], "pending")
        self.assertEqual(len(result["unexpected"]), 10)

    def test_stale_subject_and_empty_review_cannot_pass(self):
        self.assertEqual(C.quality("render", log(["MATCH"]), log(["MATCH"]), ["deepseek"])["state"], "pending")
        self.assertEqual(C.quality("render", log([]), log([]))["state"], "no lines")

    def test_parser_preserves_ruling_and_detects_duplicates(self):
        text = "| model requested | deepseek-v4-pro |\n\n## Lines\n\n"
        text += "### 1 — a\nStatus: **MISMATCH**\n\nModel: different amount\n\nRuling: model error; p. 1 says 5\n\n"
        text += "### 1 — a\nStatus: **MATCH**\n\nModel: matches\n\n## Raw response\n"
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "log.md"; path.write_text(text)
            result = C.parse_log("render", path)
        self.assertEqual(result["duplicates"], ["1"])


class RawResponseValidation(unittest.TestCase):
    def test_render_duplicate_cannot_replace_an_objection_with_a_match(self):
        rows = [{"key": "1", "status": s, "reason": "source reason"} for s in ("MISMATCH", "MATCH")]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            R.extract(json.dumps({"lines": rows}))

    def test_render_invalid_status_and_empty_reason_fail(self):
        for status, reason in (("YES", "source reason"), ("MATCH", ""), ("MATCH", None)):
            with self.subTest(status=status, reason=reason):
                with self.assertRaises(ValueError):
                    R.extract(json.dumps({"lines": [{"key": "1", "status": status, "reason": reason}]}))

    def test_transcription_duplicate_cannot_replace_a_computation(self):
        row = {"id": "x.line1", "printed": "1", "expr": {"op": "param", "ref": "sales.zero"}}
        with self.assertRaisesRegex(ValueError, "duplicate"):
            T.extract_yaml(json.dumps({"lines": [row, row]}))

    def test_worked_value_duplicate_cannot_replace_an_answer(self):
        rows = [{"printed": key, "value": value} for key, value in (("line 1", 1), ("1", 2))]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            M.extract(json.dumps({"lines": rows}))

    def test_malformed_transcription_lines_fail(self):
        for rows in ({}, [None], [{"printed": "1"}]):
            with self.subTest(rows=rows):
                with self.assertRaises(ValueError):
                    T.extract_yaml(json.dumps({"lines": rows}))


class WorkedValueParsing(unittest.TestCase):
    def test_blank_is_distinct_from_numeric_zero_in_every_value_type(self):
        for typ in ("Dollars", "NonNegDollars", "Bool", "Count", "Rate", "Enum(status)"):
            for raw in ("", "blank", "skipped", "n/a", None):
                with self.subTest(typ=typ, raw=raw):
                    self.assertEqual(M.parse_value(raw, typ), {"kind": "blank"})

    def test_printed_zero_remains_a_numeric_assertion(self):
        self.assertEqual(M.parse_value("-0-", "Dollars"), {"kind": "money", "cents": 0})
        self.assertEqual(M.parse_value("0", "Count"), {"kind": "count", "value": 0})
        self.assertEqual(M.parse_value("no", "Bool"), {"kind": "bool", "value": False})
        self.assertEqual(M.parse_value("0%", "Rate"), {"kind": "rate", "num": 0, "den": 1})

    def test_invalid_bool_and_fractional_count_cannot_become_agreements(self):
        with self.assertRaises(ValueError):
            M.parse_value("unresolved", "Bool")
        with self.assertRaises(ValueError):
            M.parse_value("1.6", "Count")

    def test_skipped_zero_is_not_written_as_a_worked_value_fixture(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(rulings, "REVIEWS", temp), \
                patch.object(M, "LOGS", temp), patch.object(M.subjects, "current", return_value="a" * 64), \
                patch.object(M, "fixture_path", return_value=str(Path(temp, "fixtures.json"))):
            Path(temp, "classm").mkdir()
            job = {"id": "classm.x.1", "branches": [], "inputs": {},
                   "fill": [{"id": "x.line1", "printed": "1", "label": "Test", "type": "Dollars"}],
                   "project": {"x.line1": {"kind": "money", "cents": 0}}}
            run = {"used": [], "verdicts": {"1": {"value": "blank", "work": "Part skipped"}},
                   "raw": "raw", "prompt_sha": "b" * 64}
            path, counts = M.write_outputs({"id": "x", "title": "Test"}, "claude-opus-5-5", [job],
                                          {job["id"]: run}, {job["id"]: {"model_reported": ["claude-opus-5-5"]}})
            self.assertEqual(counts["SKIPPED"], 1)
            self.assertEqual(counts["AGREE"], 0)
            self.assertIn("Status: **SKIPPED**", Path(path).read_text())
            self.assertEqual(json.loads(Path(temp, "fixtures.json").read_text())["cases"][0]["expect"], {})


class ArchivedSkippedAudit(unittest.TestCase):
    def example(self, raw):
        text = ('# Test\n\n## Lines\n\n### classm.x.1 — 1 — Amount\nStatus: **AGREE**\n\nValue: $0.00\n'
                '\n## Raw responses\n\n### classm.x.1\n\n```yaml\nlines:\n'
                f'  - printed: "1"\n    value: {json.dumps(raw)}\n    work: "source answer"\n```\n')
        cases = {"classm.x.1": {"id": "classm.x.1", "evidence_note": "original",
                                "expect": {"x.line1": {"kind": "money", "cents": 0}}}}
        doc = {"lines": [{"id": "x.line1", "printed": "1"}]}
        return text, cases, doc

    def test_archived_blank_loses_assertion_without_altering_raw_response(self):
        text, cases, doc = self.example("blank")
        result, removed, changed = skipped.reclassify(text, cases, doc)
        self.assertEqual(removed, [("classm.x.1", "x.line1")])
        self.assertEqual(changed, 1)
        self.assertEqual(cases["classm.x.1"]["expect"], {})
        self.assertEqual(text.partition("## Raw responses")[2], result.partition("## Raw responses")[2])
        self.assertIn("Status: **SKIPPED**", result)
        self.assertEqual(skipped.reclassify(result, cases, doc)[1:], ([], 0))

    def test_explicit_numeric_zero_keeps_its_assertion(self):
        text, cases, doc = self.example("0.00")
        result, removed, changed = skipped.reclassify(text, cases, doc)
        self.assertEqual(result, text)
        self.assertEqual((removed, changed), ([], 0))
        self.assertIn("x.line1", cases["classm.x.1"]["expect"])

    def test_unknown_line_mapping_stops_the_audit(self):
        text, cases, doc = self.example("blank")
        doc["lines"][0]["printed"] = "2"
        with self.assertRaisesRegex(ValueError, "cannot map"):
            skipped.reclassify(text, cases, doc)


class DeepSeekTransport(unittest.TestCase):
    def test_unselected_model_is_rejected_before_network_or_keychain(self):
        with patch.object(families, "selected_model", return_value="deepseek-flash"), patch.object(T, "_deepseek_key", side_effect=AssertionError("must not read keychain")), patch.object(T, "_call_deepseek", side_effect=AssertionError("must not call model")):
            with self.assertRaisesRegex(ValueError, "selected model"):
                T.call_model("PUBLIC", "deepseek-v4-pro")

    def test_family_members_cannot_substitute_for_the_selected_model(self):
        with patch.object(families, "selected_model", return_value="deepseek-flash"):
            self.assertEqual(C.model_blockers("render", "deepseek", {"model": "deepseek-flash", "reported": "deepseek-flash"}), [])
            for requested, reported in (("deepseek-v4-pro", "deepseek-v4-pro"), ("deepseek-flash", "deepseek-v4-pro")):
                self.assertTrue(C.model_blockers("render", "deepseek", {"model": requested, "reported": reported}))

    def test_peer_reset_retries_the_same_request(self):
        response = {"model": "deepseek-v4-pro", "choices": [{"message": {"content": "lines: []"}}]}
        with patch.object(T, "_deepseek_key", return_value="TEST-ONLY"), patch("urllib.request.urlopen", side_effect=[ConnectionResetError(), io.BytesIO(json.dumps(response).encode())]) as send, patch("time.sleep") as sleep:
            result, meta = T._call_deepseek("PUBLIC", "deepseek-v4-pro", 1, "SYSTEM", max_output_tokens=131072)
        self.assertEqual(result, "lines: []")
        self.assertEqual(meta["attempts"], 2)
        self.assertEqual(sleep.call_count, 1)
        self.assertEqual(send.call_args_list[0].args[0].data, send.call_args_list[1].args[0].data)
        self.assertEqual(json.loads(send.call_args_list[0].args[0].data)["max_tokens"], 131072)

    def test_peer_reset_retry_count_is_bounded(self):
        with patch.object(T, "_deepseek_key", return_value="TEST-ONLY"), patch.object(T, "DEEPSEEK_RETRIES", 2), patch("urllib.request.urlopen", side_effect=ConnectionResetError()) as send, patch("time.sleep") as sleep:
            with self.assertRaisesRegex(RuntimeError, "connection failed"):
                T._call_deepseek("PUBLIC", "deepseek-v4-pro", 1, "SYSTEM")
        self.assertEqual(send.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    def test_options_cannot_be_silently_ignored_by_another_transport(self):
        for args in ({"reasoning_effort": "max"}, {"max_output_tokens": 131072}):
            with self.subTest(args=args), patch.object(T, "_call_claude", side_effect=AssertionError("no network")):
                with self.assertRaisesRegex(ValueError, "only by the DeepSeek"):
                    T.call_model("PUBLIC", "claude-test", **args)


class IndependentPrompt(unittest.TestCase):
    def test_prompt_schema_compiles_and_distinguishes_nested_tests_from_bare_bool_ids(self):
        samples = [
            {"op": "test", "all": [{"op": "test", "eq": ["example.flag", {"const": True}]}]},
            {"op": "test", "all": ["example.flag"]},
            {"op": "copy", "from": "example.amount"},
            {"op": "copy", "from": {"const": 0}},
            {"op": "bracket_schedule", "table": "rate_schedule", "key": "example.amount", "status": "example.status"},
        ]
        code = """import { readFileSync } from 'node:fs';
import { Ajv2020 } from 'ajv/dist/2020.js';
const {schema,samples}=JSON.parse(readFileSync(0,'utf8'));
const validate=new Ajv2020({strict:false}).compile(schema);
process.stdout.write(JSON.stringify(samples.map(sample=>validate(sample))));"""
        result = subprocess.run(["node", "--input-type=module", "-e", code],
                                input=json.dumps({"schema": T.expression_schema(), "samples": samples}),
                                text=True, capture_output=True, check=True, cwd=T.ROOT)
        self.assertEqual(json.loads(result.stdout), [True, False, True, False, False])

    def test_table_interfaces_preserve_key_order_without_cells_or_rules(self):
        table = {"id": "public_rates", "title": "Printed rate table", "kind": "keyed",
                 "keys": [{"name": "period", "type": "Enum(period)"}, {"name": "year", "type": "Count"}],
                 "cell": "Rate", "rows": [{"keys": ["first", 1], "value": "PRIVATE_CELL"}],
                 "note": "PRIVATE_RULE"}
        reserved = {"id": "rate_schedule", "title": "PRIVATE_RESERVED_TABLE", "kind": "bracket_schedule"}
        text = T.table_notes([table, reserved])
        self.assertIn("public_rates", text)
        self.assertIn("[period: Enum(period), year: Count]", text)
        self.assertIn("result Rate", text)
        self.assertNotIn("PRIVATE", text)

    def test_fast_project_parser_preserves_the_entire_form_catalog(self):
        paths = [*Path(T.FORMS).glob("*.yaml"), Path(T.ROOT) / "params" / f"{T.Y}.yaml"]
        for path in paths:
            with self.subTest(path=path.name):
                self.assertEqual(T.project_yaml(path), yaml.safe_load(path.read_text()))

    def test_computed_labels_and_expression_do_not_enter_prompt(self):
        inp = {"id": "fake.input", "printed": "1", "type": "NonNegDollars", "label": "INPUT_LABEL",
               "expr": {"op": "input", "source": "Box 1 of the supplied document"}}
        output = {"id": "fake.line2", "printed": "2", "type": "NonNegDollars", "label": "PRIVATE_COMPUTED_LABEL",
                  "expr": {"op": "copy", "from": "PRIVATE_OPERAND"}}
        helper = {"id": "fake.result", "printed": "(helper)", "type": "NonNegDollars", "label": "PRIVATE_HELPER_LABEL",
                  "expr": {"op": "copy", "from": "PRIVATE_OPERAND"}}
        form = {"id": "fake", "title": "Fake worksheet", "tax_year": 2025, "lines": [inp, output, helper]}
        with patch.object(T, "exported_lines", return_value=[helper]), patch.object(T, "collection_notes", return_value=""), patch.object(T, "screen_notes", return_value=""):
            prompt = T.build_prompt(form, "PUBLIC ARCHIVED TEXT", {}, {})
        for forbidden in ("PRIVATE_COMPUTED_LABEL", "PRIVATE_HELPER_LABEL", "PRIVATE_OPERAND"):
            self.assertNotIn(forbidden, prompt)
        self.assertIn("fake.result", prompt)
        self.assertIn("Box 1 of the supplied document", prompt)
        self.assertIn("PUBLIC ARCHIVED TEXT", prompt)

    def test_reference_catalog_omits_computed_label(self):
        line = {"id": "x.a", "printed": "2", "type": "Dollars", "label": "PRIVATE_CALCULATION",
                "expr": {"op": "sum", "of": ["PRIVATE_OPERAND"]}}
        text = T.reference_note({"id": "x"}, line)
        self.assertIn("printed '2'", text)
        self.assertNotIn("PRIVATE", text)


class PartialInputContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = contracts.load('dependent', T.Y)
        cls.project = T.load_form('dependent')['lines']

    def assess(self, lines, prompt=None):
        return contracts.assess('dependent', T.Y, lines, T.model_type_context(),
                                contracts.public_prompt(self.bank) if prompt is None else prompt)

    def test_authored_cases_include_decidable_and_genuinely_missing_timing(self):
        result = self.assess(self.project)
        self.assertEqual((result['state'], len(result['cases']), result['request_context']), ('pass', 10, 'included'))
        unknown = next(test for test in result['cases'] if test['id'] == 'P09')['outputs'][1]
        self.assertEqual(unknown['actual']['kind'], 'unknown')
        self.assertEqual(unknown['actual']['input'], 'dependent[sample].dc_over12_care')

    def test_negative_care_facts_do_not_inherit_qualified_expenses(self):
        for test in contracts.cases(self.bank):
            facts = test['inputs']
            age = facts['dependent[sample].age']
            incapable = facts['dependent[sample].dc_incapable']
            if not incapable and (age >= 14 or (age == 13 and facts.get('dependent[sample].dc_under13') is False)):
                with self.subTest(case=test['id']):
                    self.assertEqual(facts['dependent[sample].dc_paid'], 0)

    def test_type_valid_unconditional_timing_dependency_fails_partial_cases(self):
        changed = json.loads(json.dumps(self.project))
        next(line for line in changed if line['id'] == 'dependent.dc_qp')['expr'] = {'op': 'copy', 'from': 'dependent.dc_under13'}
        self.assertEqual(T.validate_model_types('dependent', changed), [])
        result = self.assess(changed)
        self.assertEqual(result['state'], 'fail')
        output = result['cases'][0]['outputs'][0]
        self.assertFalse(output['pass'])
        self.assertEqual(output['actual']['kind'], 'unknown')

    def test_false_default_cannot_pass_positive_or_undetermined_box_cases(self):
        changed = json.loads(json.dumps(self.project))
        next(line for line in changed if line['id'] == 'dependent.dc_line2c')['expr'] = {'op': 'test', 'ne': [{'const': True}, {'const': True}]}
        result = self.assess(changed)
        self.assertEqual(result['state'], 'fail')
        self.assertFalse(next(test for test in result['cases'] if test['id'] == 'P09')['pass'])

    def test_invalid_count_choose_is_never_evaluated(self):
        changed = json.loads(json.dumps(self.project))
        next(line for line in changed if line['id'] == 'dependent.dc_count')['expr'] = {'op': 'choose', 'alternatives': [{'guard': {'op': 'test', 'eq': [{'const': True}, {'const': True}]}, 'then': 'dependent.one'}]}
        result = self.assess(changed)
        self.assertEqual((result['state'], result['cases']), ('invalid', []))

    def test_nonboolean_refusal_gate_is_rejected_before_evaluation(self):
        changed = json.loads(json.dumps(self.project))
        next(line for line in changed if line['id'] == 'dependent.dc_qp')['refuses'] = ['dependent.age']
        result = self.assess(changed)
        self.assertEqual((result['state'], result['cases']), ('invalid', []))

    def test_public_projection_never_exposes_reference_answers_or_rationales(self):
        bank = json.loads(json.dumps(self.bank))
        bank['cases'][0]['expect']['dependent[sample].dc_qp']['value'] = 'PRIVATE_EXPECTED'
        bank['cases'][0]['basis'] = 'PRIVATE_RATIONALE'
        prompt = contracts.public_prompt(bank)
        self.assertNotIn('PRIVATE_', prompt)
        self.assertIn('dependent[sample].age', prompt)

    def test_diagnostic_without_fact_cases_in_original_request_cannot_claim_inclusion(self):
        result = self.assess(self.project, 'Earlier actual request')
        self.assertEqual((result['state'], result['request_context']), ('pass', 'absent'))

    def test_changed_host_case_bank_invalidates_ruling_context(self):
        header = '| comparison policy | checked-expression-types-v2 |\n'
        header += '| partial-input bank sha256 | ' + 'a' * 64 + ' |\n'
        self.assertNotEqual(rulings.review_context('transcription', header),
                            rulings.review_context('transcription', header.replace('a' * 64, 'b' * 64)))

    def test_required_bank_cannot_silently_disappear(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(contracts, 'DIRECTORY', Path(temp)):
            with self.assertRaises(FileNotFoundError):
                contracts.load('dependent', T.Y)

    def test_absent_stale_or_failing_partial_checks_block_either_family(self):
        parse = C.parse_log
        for field, value in [('partial_context', 'absent'), ('partial_bank', 'old'), ('partial_result', 'fail')]:
            def record(kind, path):
                result = parse(kind, path)
                result.update(partial_policy=contracts.POLICY, partial_bank=contracts.bank_sha(self.bank),
                              partial_context='included', partial_result='pass')
                if families.split_stem(Path(path).stem)[1] == 'claude':
                    result[field] = value
                return result
            with self.subTest(field=field), patch.object(C, 'parse_log', side_effect=record):
                result = C.compare('transcription', 'dependent', 'deepseek')['quality']
                self.assertTrue(any('source-based partial-input checks: claude' in blocker for blocker in result['blockers']))


class CompleteInputContext(unittest.TestCase):
    def test_foreign_refusal_and_visibility_dependencies_are_source_targets(self):
        gate={'id':'probe.gate','printed':'(gate)','type':'Bool','expr':{'op':'test','eq':['probe.answer',{'const':True}]}}
        doc={'id':'probe','lines':[gate]}
        other={'id':'other.value','expr':{'op':'param','ref':'zero'}}
        for use in [{'refuses':[{'when':'probe.gate'}]}, {'shown_when':'probe.gate'}]:
            with self.subTest(use=use), patch.object(T,'ALL_LINES',{'other.value':('other',{**other,**use})}), \
                    patch.object(T,'load_defs',return_value={}), patch.object(adapters,'excluded_ids',return_value=set()):
                self.assertEqual(T.exported_lines(doc),[gate])

    def test_question_words_cannot_create_a_false_foreign_dependency(self):
        gate={'id':'probe.gate','printed':'(gate)','type':'Bool','expr':{'op':'test','eq':['probe.answer',{'const':True}]}}
        other={'expr':{'op':'input','source':'A description mentions "probe.gate" but does not read it.'}}
        with patch.object(T,'ALL_LINES',{'other.answer':('other',other)}), \
                patch.object(T,'load_defs',return_value={}), patch.object(adapters,'excluded_ids',return_value=set()):
            self.assertEqual(T.exported_lines({'id':'probe','lines':[gate]}),[])

    def test_old_household_logs_do_not_cover_newly_discovered_hoh_target(self):
        targets=T.required_target_keys(T.load_form('household'))
        self.assertIn('household.hoh_fails',targets)
        parse=C.parse_log
        def old_inventory(kind,path):
            record=parse(kind,path)
            record['lines'].pop('household.hoh_fails',None)
            record['input_context_policy']='legacy-unrecorded'
            return record
        with patch.object(C,'parse_log',side_effect=old_inventory):
            quality=C.compare('transcription','household','deepseek')['quality']
        self.assertTrue(any('current source targets not judged' in b and 'household.hoh_fails' in b for b in quality['blockers']))

    def test_own_collection_catalog_does_not_offer_hidden_computed_helpers(self):
        own=T.collection_notes('carloan')
        others=T.collection_notes()
        self.assertNotIn('carloan.qpvli (',own)
        self.assertIn('carloan.interest (',own)
        self.assertIn('carloan.qpvli (',others)
        self.assertIn('person.income179 (',own)

    def test_saved_request_must_contain_late_meaning_before_completeness_passes(self):
        question = "Relationship. " + "Public context. " * 14 + "Grandnieces require the household test."
        lines = {"fake.relationship": ("fake", {"expr": {"op": "input", "source": question}})}
        with patch.object(T, "load_all_lines", return_value=lines):
            self.assertEqual(T.missing_input_context(question[:160]), ["fake.relationship"])
            self.assertEqual(T.missing_input_context(question.replace(" ", "\n")), [])

    def test_late_enum_semantics_survive_own_and_foreign_input_catalogs(self):
        question = "Relationship category. " + "Public interface description. " * 12 + "sibling_descendant excludes listed nieces and nephews."
        line = {"id": "fake.relationship", "printed": "1", "type": "Enum(relationship)",
                "expr": {"op": "input", "source": question}}
        form = {"id": "fake", "title": "Fake worksheet", "tax_year": 2025, "lines": [line]}
        with patch.object(T, "exported_lines", return_value=[]), patch.object(T, "collection_notes", return_value=""), patch.object(T, "screen_notes", return_value=""):
            prompt = T.build_prompt(form, "PUBLIC ARCHIVED TEXT", {}, {})
        self.assertIn(question, prompt)
        self.assertIn(question, T.reference_note(form, line))

    def test_late_scope_exception_survives_refusal_catalog(self):
        question = "Outside scope? " + "Public screening detail. " * 14 + "Except the specifically included timing case."
        gate = {"id": "fake.gate", "printed": "(screen)", "type": "Bool", "expr": {"op": "input", "source": question}}
        target = {"id": "fake.result", "expr": {"op": "copy", "from": "fake.amount"}, "refuses": [{"when": "fake.gate"}]}
        with patch.object(T, "load_all_lines", return_value={"fake.gate": ("fake", gate), "fake.result": ("fake", target)}):
            self.assertIn(question, T.screen_notes())


class LiteralUnits(unittest.TestCase):
    def test_count_threshold_cannot_agree_with_money_threshold(self):
        project = [
            {"id": "probe.months", "printed": "(helper)", "label": "Months", "type": "Count", "expr": {"op": "input", "source": "Months"}},
            {"id": "probe.result", "printed": "1", "label": "Threshold", "type": "Bool", "expr": {"op": "test", "gt": ["probe.months", {"const": 6, "type": "Count"}]}},
        ]
        second = json.loads(json.dumps(project))
        second[1]["expr"]["gt"][1].pop("type")
        with patch.object(T, "model_type_context", return_value=ModelExpressionTypes.context(project)):
            results, _ = T.compare("probe", project, second)
        self.assertEqual(results[0]["status"], "DISAGREE")

    def test_zero_and_one_parameters_keep_their_units(self):
        expander = T.Expander("probe", [], defs={}, params={"count.zero": 0, "count.one": 1, "money.zero": 0},
                              param_types={"count.zero": "Count", "count.one": "Count", "money.zero": "Dollars"})
        for value, name in [(0, "count.zero"), (1, "count.one")]:
            self.assertEqual(expander.param(name), {"const": value, "type": "Count"})
        self.assertEqual(expander.param("money.zero"), {"const": 0})

    def test_definition_and_foreign_helper_expansion_keep_parameter_units(self):
        line = {"id": "result", "printed": "1", "type": "Count", "expr": {"op": "param", "ref": "count.zero"}}
        defs = {"inner": {"id": "inner", "lines": [line]}}
        expander = T.Expander("probe", [], defs=defs, params={"count.zero": 0}, param_types={"count.zero": "Count"})
        self.assertEqual(expander.ref({"def": "inner", "line": "result", "bind": {}}, 0), {"const": 0, "type": "Count"})
        foreign = {**line, "id": "other.zero", "printed": "(helper)"}
        with patch.object(T, "ALL_LINES", {"other.zero": ("other", foreign)}):
            self.assertEqual(expander.ref("other.zero", 0), {"const": 0, "type": "Count"})

    def test_only_money_zero_is_elided_from_sum(self):
        expander = T.Expander("probe", [], defs={})
        money = {"op": "sum", "of": [{"const": 0}, {"const": 5}]}
        self.assertEqual(expander.expr(money), {"const": 5})
        for zero in ({"const": False}, {"const": 0, "type": "Count"}):
            self.assertFalse(T.money_zero(zero))
            self.assertEqual(expander.expr({"op": "sum", "of": [zero, {"const": 5}]})["op"], "sum")

    def test_money_one_does_not_become_boolean_true(self):
        condition = {"id": "probe.condition", "printed": "(helper)", "type": "Bool", "expr": {"op": "test", "eq": ["probe.flag", {"const": True}]}}
        expander = T.Expander("probe", [condition], defs={})
        boolean = expander.expr({"op": "test", "eq": ["probe.condition", {"const": True}]})
        money = expander.expr({"op": "test", "eq": ["probe.condition", {"const": 1}]})
        self.assertNotEqual(T.canonical(boolean), T.canonical(money))
        self.assertEqual(money["test"], "eq")

    def test_bare_number_is_not_a_valid_operand(self):
        expander = T.Expander("probe", [], defs={})
        self.assertIn("unknown", expander.ref(6, 0))
        self.assertEqual(expander.ref({"const": 6}, 0), {"const": 6})

    def test_comparison_policy_changes_ruling_context_without_changing_request(self):
        head = "| prompt sha256 | " + "a" * 64 + " |\n"
        typed = head + "| comparison policy | typed-literals-v1 |\n"
        self.assertNotEqual(rulings.review_context("transcription", head), rulings.review_context("transcription", typed))


class ConcurrentWorkedReceipts(unittest.TestCase):
    def test_concurrent_cases_keep_their_own_prompt_response_and_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp, 'jobs.json')
            jobs = [{'id': f'classm.fake.{i}', 'doc': 'fake', 'fill': [], 'given': [], 'own_inputs': []} for i in (1, 2)]
            path.write_text(json.dumps({'jobs': jobs}))
            barrier = threading.Barrier(2)
            def reply(prompt, model, base, *args):
                barrier.wait(timeout=5)
                return 'lines: []\n# ' + prompt, {'cost_usd': 0}
            with patch.object(M, 'JOBS', str(path)), patch.object(M, 'RAW', temp), \
                    patch.object(M.subprocess, 'run'), patch.object(M, 'load_form', return_value={'id': 'fake'}), \
                    patch.object(M, 'manifest', return_value={}), patch.object(M, 'excerpt_for', return_value=('SOURCE', [])), \
                    patch.object(M, 'build_prompt', side_effect=lambda form, excerpt, job: job['id']), \
                    patch.object(M, 'review_response', side_effect=reply), \
                    patch.object(M, 'write_outputs', return_value=('LOG', {'AGREE': 0, 'DISAGREE': 0, 'SKIPPED': 0, 'MISSING': 0})) as write, \
                    patch.object(sys, 'argv', ['classm.py', '--doc', 'fake', '--model', 'deepseek-flash', '--case-jobs', '2']):
                with self.assertRaises(SystemExit) as done:
                    M.main()
                self.assertEqual(done.exception.code, 0)
            runs = write.call_args.args[3]
            self.assertEqual(list(runs), [job['id'] for job in jobs])
            for job in jobs:
                self.assertEqual(runs[job['id']]['raw'], 'lines: []\n# ' + job['id'])
                self.assertEqual(runs[job['id']]['prompt_sha'], transcription_audit.sha(job['id']))


class HsaPartialInputs(unittest.TestCase):
    def assess(self, lines):
        bank = contracts.load('f8889', T.Y)
        return contracts.assess('f8889', T.Y, lines, T.model_type_context(), contracts.public_prompt(bank))

    def test_source_facts_cover_zero_positive_missing_and_contradictory_figures(self):
        result = self.assess(T.load_form('f8889')['lines'])
        self.assertEqual((result['state'], len(result['cases'])), ('pass', 17))

    def test_consistency_mode_changes_the_worked_review_subject(self):
        text = Path(T.FORMS, 'f8889.yaml').read_text()
        self.assertNotEqual(T.subjects.of_computation(text), T.subjects.of_computation(text.replace('      when_known: true\n', '')))

    def test_original_required_rollover_gate_fails_zero_distribution_case(self):
        changed = json.loads(json.dumps(T.load_form('f8889')['lines']))
        next(line for line in changed if line['id'] == 'f8889.line14b')['refuses'][0].pop('when_known')
        result = self.assess(changed)
        self.assertFalse(next(case for case in result['cases'] if case['id'] == 'H01')['pass'])

    def test_skipping_the_consistency_gate_cannot_pass_supplied_contradictions(self):
        changed = json.loads(json.dumps(T.load_form('f8889')['lines']))
        next(line for line in changed if line['id'] == 'f8889.line14b')['refuses'] = []
        result = self.assess(changed)
        self.assertFalse(next(case for case in result['cases'] if case['id'] == 'H03')['pass'])
        self.assertFalse(next(case for case in result['cases'] if case['id'] == 'H09')['pass'])


class ModelExpressionTypes(unittest.TestCase):
    def test_validation_follows_count_proration_table_and_collection_operands(self):
        expressions = [
            {"op": "round", "of": "probe.bad", "unit": 100, "rule": "up"},
            {"op": "multiply_count", "amount": "probe.amount", "count": "probe.bad"},
            {"op": "prorate", "amount": "probe.amount", "part": "probe.bad", "whole": {"const": 12, "type": "Count"}},
            {"op": "prorate", "amount": "probe.amount", "part": "probe.months", "whole": "probe.bad"},
            {"op": "keyed_lookup", "table": "probe.table", "keys": ["probe.bad"]},
            {"op": "sum_over", "collection": "probe.entries", "field": "probe.bad"},
        ]
        errors = [{"line": "probe.bad", "message": "invalid helper type"}]
        for expression in expressions:
            with self.subTest(expression=expression):
                rows = {"probe.result": {"expr": expression}, "probe.bad": {"expr": {"op": "param", "ref": "not.a.line"}}}
                checked = T.checked_second('{}', errors, "probe.result", rows)
                self.assertIn("invalid_model_types", checked)
                self.assertNotIn("not.a.line", T.validation_dependencies("probe.result", rows))

    @staticmethod
    def context(lines):
        return {"forms": [{"id": "probe", "kind": "form", "lines": lines}], "defs": [],
                "params": {"enums": {}, "values": {}}, "tables": [], "register": {"entries": []}}

    def lines(self):
        return [
            {"id": "probe.months", "printed": "(helper)", "label": "Months", "type": "Count", "expr": {"op": "input", "source": "Months"}},
            {"id": "probe.result", "printed": "1", "label": "Threshold", "type": "Bool", "expr": {"op": "test", "gt": ["probe.months", {"const": 6, "type": "Count"}]}},
        ]

    def test_build_checker_accepts_typed_candidate_with_published_inputs_omitted(self):
        project = self.lines()
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            self.assertEqual(T.validate_model_types("probe", project[1:]), [])

    def test_published_input_does_not_import_hidden_authored_gate(self):
        project = self.lines()
        project[0]['refuses'] = [{'when':'probe.authored_gate'}]
        project.append({'id':'probe.authored_gate','printed':'(gate)','type':'Bool',
                        'expr':{'op':'test','gt':['probe.months',{'const':12,'type':'Count'}]}})
        with patch.object(T,'model_type_context',return_value=self.context(project)):
            self.assertEqual(T.validate_model_types('probe',[project[1]]),[])

    def test_refusals_explicitly_returned_on_input_are_still_checked(self):
        project=self.lines()
        second=json.loads(json.dumps(project))
        second[0]['refuses']=[{'when':'probe.months'}]
        with patch.object(T,'model_type_context',return_value=self.context(project)):
            self.assertTrue(T.validate_model_types('probe',second))
        second[0]['refuses']=[{'when':'probe.result','when_known':True}]
        with patch.object(T,'model_type_context',return_value=self.context(project)):
            self.assertEqual(T.validate_model_types('probe',second),[])

    def test_nonboolean_or_malformed_refusal_is_rejected_without_execution(self):
        project = self.lines()
        for refusal in ['probe.months', {'when': 'probe.result', 'when_known': 'true'}, {'when': 'probe.result', 'invented': True}]:
            candidate = [{**project[1], 'refuses': [refusal]}]
            with self.subTest(refusal=refusal), patch.object(T, 'model_type_context', return_value=self.context(project)):
                self.assertTrue(T.validate_model_types('probe', candidate))

    def test_same_expression_with_wrong_declared_type_cannot_agree(self):
        project = self.lines()
        second = json.loads(json.dumps(project[1:]))
        second[0]["type"] = "Dollars"
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            result, _ = T.compare("probe", project, second)
        self.assertEqual(result[0]["status"], "DISAGREE")
        self.assertIn("invalid_model_types", result[0]["second"])

    def test_type_error_in_printed_dependency_blocks_its_caller(self):
        project = self.lines()
        project[1]["expr"] = {"op": "copy", "from": "probe.helper"}
        project.append({"id": "probe.helper", "printed": "2", "label": "Helper", "type": "Bool",
                        "expr": {"op": "test", "gt": ["probe.months", {"const": 6, "type": "Count"}]}})
        second = json.loads(json.dumps(project[1:]))
        second[1]["expr"] = {"op": "copy", "from": "probe.months"}
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            result, _ = T.compare("probe", project, second)
        self.assertEqual(result[0]["status"], "DISAGREE")
        self.assertIn("probe.helper", result[0]["second"])

    def test_closed_inputs_cannot_be_added_or_retyped(self):
        project = self.lines()
        changed = json.loads(json.dumps(project))
        changed[0]["type"] = "Dollars"
        added = {"id": "probe.extra", "type": "Count", "expr": {"op": "input", "source": "Invented"}}
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            errors = T.validate_model_types("probe", changed + [added])
        self.assertTrue(any("published input" in e["message"] for e in errors))
        self.assertTrue(any("outside the closed interface" in e["message"] for e in errors))

    def test_omitted_helpers_are_not_borrowed_from_project_computations(self):
        project = self.lines()
        project[1]["expr"] = {"op": "copy", "from": "probe.helper"}
        project.append({"id": "probe.helper", "printed": "(helper)", "label": "Helper", "type": "Bool",
                        "expr": {"op": "test", "gt": ["probe.months", {"const": 6, "type": "Count"}]}})
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            errors = T.validate_model_types("probe", [project[1]])
        self.assertTrue(any("does not resolve" in e["message"] for e in errors))

    def test_malformed_expression_becomes_diagnostic_without_execution(self):
        project = self.lines()
        changed = {**project[1], "expr": {"op": "sum"}}
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            errors = T.validate_model_types("probe", [changed])
        self.assertTrue(any("malformed expression" in e["message"] for e in errors))

    def test_unused_invalid_helper_still_prevents_form_type_pass(self):
        project = self.lines()
        extra = {"id": "probe.unused", "printed": "(helper)", "label": "Unused", "type": "Bool",
                 "expr": {"op": "copy", "from": "probe.months"}}
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            result, _ = T.compare("probe", project, project[1:] + [extra])
        self.assertEqual(result[0]["status"], "AGREE")
        self.assertTrue(result.validation_errors)
        with tempfile.TemporaryDirectory() as temp, patch.object(T, "LOGS", temp), \
                patch.object(rulings, "REVIEWS", temp), patch.object(T.subjects, "current", return_value="a" * 64):
            Path(temp, "transcription").mkdir()
            path, _ = T.write_log({"id": "probe", "title": "Probe"}, "deepseek-flash", "request", [], result, [], "lines: []", {})
            text = Path(path).read_text()
        self.assertIn("| model type validation | fail |", text)

    def test_extra_comparison_cannot_hide_behind_a_valid_comparison(self):
        project = self.lines()
        changed = json.loads(json.dumps(project[1:]))
        changed[0]["expr"]["eq"] = ["probe.months", {"const": 1, "type": "Count"}]
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            errors = T.validate_model_types("probe", changed)
        self.assertTrue(any("project schema" in e["message"] for e in errors))

    def test_unknown_literal_annotation_cannot_be_silently_ignored(self):
        project = self.lines()
        changed = json.loads(json.dumps(project[1:]))
        changed[0]["expr"]["gt"][1]["ignored_unit"] = "money"
        with patch.object(T, "model_type_context", return_value=self.context(project)):
            errors = T.validate_model_types("probe", changed)
        self.assertTrue(any("project schema" in e["message"] for e in errors))


class InternalAdapterContracts(unittest.TestCase):
    def test_election_adapter_copies_full_amount_and_preserves_scope_and_limit_gates(self):
        context = T.model_type_context()
        original = json.loads(json.dumps(context))
        result = adapters.assess("f4952", T.Y, context)
        self.assertEqual(result["state"], "pass")
        self.assertEqual(len(result["cases"]), 19)
        self.assertTrue(all(len(test["outputs"]) == 2 for test in result["cases"]))
        self.assertFalse(result["evidence_credit"])
        self.assertEqual(context, original)
        self.assertEqual(result['boundary_inputs'], ['sb.line2','sb.line6','sd.line16','sd.net_gain'])

    def test_election_gain_portion_substitution_and_gate_removal_are_caught(self):
        for change in ['gain-portion','remove-limit']:
            context=json.loads(json.dumps(T.model_type_context()))
            target=next(l for d in context['forms'] if d['id']=='f4952' for l in d['lines'] if l['id']=='f4952.election')
            if change=='gain-portion':
                target['expr']={'op':'copy','from':'f4952.line4e'}
            else:
                target=next(l for d in context['forms'] if d['id']=='f4952' for l in d['lines']
                            if any(r.get('when')=='f4952.bad_election' for r in l.get('refuses',[])))
                target['refuses']=[r for r in target['refuses'] if r['when']!='f4952.bad_election']
            with self.subTest(change=change):
                self.assertEqual(adapters.assess('f4952',T.Y,context)['state'],'fail')

    def test_engineering_boundaries_cannot_replace_reviewed_form_arithmetic(self):
        bank=json.loads(json.dumps(adapters.load('f4952',T.Y)))
        bank['boundary_inputs']=['f4952.line4e']
        with patch.object(adapters,'load',return_value=bank):
            with self.assertRaisesRegex(ValueError,'foreign return subtotal'):
                adapters.assess('f4952',T.Y,T.model_type_context())

    def test_election_adapter_is_excluded_but_printed_tax_results_remain_blind_targets(self):
        doc=T.load_form('f4952')
        self.assertNotIn('f4952.election',{line['id'] for line in T.exported_lines(doc)})
        prompt=T.build_prompt(doc,'ARCHIVED SOURCE',{}, {})
        self.assertIn('id f4952.line4h;',prompt)
        self.assertNotIn('id f4952.election (',prompt)

    def test_authored_adapter_and_all_consumer_copies_pass(self):
        result = adapters.assess("div", T.Y, T.model_type_context())
        self.assertEqual(result["state"], "pass")
        self.assertEqual(len(result["cases"]), 21)
        self.assertFalse(result["evidence_credit"])
        self.assertTrue(all(len(test["outputs"]) == 15 for test in result["cases"]))

    def test_refusal_removal_is_caught_by_engineering_cases(self):
        context = json.loads(json.dumps(T.model_type_context()))
        screen = next(line for doc in context["forms"] if doc["id"] == "div" for line in doc["lines"] if line["id"] == "div.screen")
        screen["refuses"] = []
        result = adapters.assess("div", T.Y, context)
        self.assertEqual(result["state"], "fail")
        self.assertFalse(next(test for test in result["cases"] if test["id"] == "section1202")["pass"])
        self.assertFalse(next(test for test in result["cases"] if test["id"] == "missing-section1202-answer")["pass"])

    def test_changed_adapter_amount_is_caught(self):
        context = json.loads(json.dumps(T.model_type_context()))
        screen = next(line for doc in context["forms"] if doc["id"] == "div" for line in doc["lines"] if line["id"] == "div.screen")
        screen["expr"] = {"op": "copy", "from": "div.box2b"}
        result = adapters.assess("div", T.Y, context)
        self.assertEqual(result["state"], "fail")
        self.assertFalse(next(test for test in result["cases"] if test["id"] == "accepted-positive-components")["pass"])

    def test_changed_consumer_wiring_cannot_silently_drop_coverage(self):
        context = json.loads(json.dumps(T.model_type_context()))
        line = next(line for doc in context["forms"] if doc["id"] == "g28" for line in doc["lines"] if line["id"] == "g28.line1")
        line["expr"] = {"op": "param", "ref": "sales.zero"}
        with self.assertRaisesRegex(ValueError, "consumer inventory"):
            adapters.assess("div", T.Y, context)

    def test_required_registry_cannot_disappear(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(adapters, "DIRECTORY", Path(temp)):
            with self.assertRaises(FileNotFoundError):
                adapters.load("div", T.Y)

    def test_empty_reference_answer_cannot_make_all_outputs_pass(self):
        bank = json.loads(json.dumps(adapters.load("div", T.Y)))
        bank["cases"][0]["expect"] = {}
        with tempfile.TemporaryDirectory() as temp, patch.object(adapters, "DIRECTORY", Path(temp)):
            folder = Path(temp, str(T.Y))
            folder.mkdir()
            (folder / "div.json").write_text(json.dumps(bank))
            with self.assertRaisesRegex(ValueError, "reference answer"):
                adapters.load("div", T.Y)

    def test_blind_target_list_contains_no_internal_adapter(self):
        self.assertEqual(T.exported_lines(T.load_form("div")), [])
        with patch.object(T, "review_response", side_effect=AssertionError("empty source review must make no request")), \
                patch.object(sys, "argv", ["transcribe.py", "--form", "div"]):
            with patch("sys.stdout", new_callable=io.StringIO) as out:
                T.main()
        self.assertIn("no model call or review assertion", out.getvalue())

    def test_historical_adapter_agreement_cannot_earn_source_credit(self):
        record = {"lines": {"div.screen": {"status": "AGREE"}}}
        projected = adapters.source_record("div", T.Y, record)
        self.assertFalse(projected["lines"])
        self.assertIn("div.screen", record["lines"])
        quality = C.quality("transcription", projected, projected)
        self.assertEqual(quality["state"], "no lines")
        result = C.compare("transcription", "div", "deepseek")
        self.assertEqual(result["judged"], [])
        self.assertEqual(result["excluded_adapters"], ["div.screen"])
        self.assertTrue(any("no tax-evidence credit" in text for text in result["quality"]["blockers"]))

    def test_adapter_behavior_and_reference_answers_stay_host_only(self):
        bank = json.loads(json.dumps(adapters.load("div", T.Y)))
        bank["adapters"]["div.screen"]["behavior"] = "PRIVATE_ADAPTER_BEHAVIOR_CANARY"
        bank["cases"][0]["expect"] = {"kind": "PRIVATE_ADAPTER_ANSWER_CANARY"}
        with patch.object(adapters, "load", return_value=bank):
            prompt = T.build_prompt(T.load_form("div"), "ARCHIVED SOURCE", {}, {})
        self.assertNotIn("PRIVATE_ADAPTER_", prompt)
        self.assertNotIn("id div.screen", prompt)


class SavedTranscriptionAudit(unittest.TestCase):
    def artifacts(self):
        prompt, response, subject = "Original source-only request", "lines: []\n", "a" * 64
        meta = {"prompt_sha256": transcription_audit.sha(prompt), "system_sha256": "b" * 64,
                "prompt_policy": "source-only-computation-v2", "model_requested": "deepseek-flash"}
        fields = {"subject sha256": subject, "prompt sha256": meta["prompt_sha256"],
                  "system sha256": meta["system_sha256"], "prompt policy": meta["prompt_policy"],
                  "model requested": meta["model_requested"]}
        log_text = "\n".join(f"| {k} | {v} |" for k, v in fields.items())
        log_text += "\n## Lines\n\n## Raw second transcription\n\n```yaml\n" + response + "\n```\n"
        return log_text, prompt, response, meta, subject

    def test_saved_request_identity_is_checked_without_upgrading_legacy_receipts(self):
        args = self.artifacts()
        receipt = transcription_audit.verify_saved(*args)
        self.assertEqual(receipt["request_provenance"], "bound")
        self.assertEqual(receipt["original_comparison_policy"], "legacy-unversioned")
        legacy = (*args[:3], {}, args[4])
        self.assertEqual(transcription_audit.verify_saved(*legacy)["request_provenance"], "legacy-limited")

    def test_changed_subject_prompt_reply_or_request_metadata_is_rejected(self):
        args = list(self.artifacts())
        for index, replacement in [(1, "different prompt"), (2, "lines: [different]\n"),
                                   (4, "c" * 64), (3, {**args[3], "model_requested": "deepseek-v4-pro"})]:
            changed = list(args)
            changed[index] = replacement
            with self.assertRaises(ValueError):
                transcription_audit.verify_saved(*changed)

    def test_truncated_saved_response_cannot_be_audited_as_complete(self):
        args = list(self.artifacts())
        args[3] = {**args[3], "finish_reason": "length"}
        with self.assertRaisesRegex(ValueError, "output budget"):
            transcription_audit.verify_saved(*args)

    def test_current_log_writer_strips_only_response_edge_whitespace(self):
        args = list(self.artifacts())
        args[0] = args[0].replace("```yaml\n" + args[2] + "\n```", "```yaml\n" + args[2].strip() + "\n```")
        receipt = transcription_audit.verify_saved(*args)
        self.assertEqual(receipt["response_sha256"], transcription_audit.sha(args[2]))

    def test_original_validation_policies_stay_historical(self):
        args = list(self.artifacts())
        args[0] = ("| type validation policy | project-expression-types-v1 |\n"
                   "| input context policy | complete-input-context-v1 |\n" + args[0])
        receipt = transcription_audit.verify_saved(*args)
        self.assertEqual(receipt["original_type_policy"], "project-expression-types-v1")
        self.assertEqual(receipt["original_input_context_policy"], "complete-input-context-v1")

    def test_verified_replay_archives_originals_without_editing_raw_artifacts(self):
        log_text,prompt,response,meta,subject=self.artifacts()
        with tempfile.TemporaryDirectory() as temp, patch.object(T,'RAW',str(Path(temp,'raw'))):
            raw=Path(T.RAW);raw.mkdir()
            path=Path(temp,'probe.md');path.write_text(log_text)
            for suffix,value in [('.prompt.txt',prompt),('.response.txt',response),('.meta.json',json.dumps(meta))]:
                (raw/('probe'+suffix)).write_text(value)
            before={p.name:p.read_bytes() for p in raw.iterdir()}
            receipt=transcription_audit.prepare_replay(path,prompt,response,meta,subject)
            folder=raw/'archive/verified-replays/probe'/receipt['parent_sha256']
            self.assertEqual((folder/'probe.md').read_text(),log_text)
            self.assertEqual(path.read_text(),log_text)
            derived=('| review provenance | verified saved-response replay; no model call |\n'
                     '| parent review log sha256 | '+receipt['parent_sha256']+' |\n'+log_text)
            transcription_audit.verify_replay_archive(path,derived,prompt,response,meta,subject)
            archived_response=folder/'probe.response.txt'
            archived_response.write_text('corrupted parent')
            with self.assertRaisesRegex(ValueError,'archive hash mismatch'):
                transcription_audit.verify_replay_archive(path,derived,prompt,response,meta,subject)
            archived_response.write_text(response)
            for name,data in before.items():
                self.assertEqual((raw/name).read_bytes(),data)
            (raw/'probe.response.txt').write_text('different')
            with self.assertRaisesRegex(ValueError,'artifacts changed'):
                transcription_audit.prepare_replay(path,prompt,response,meta,subject)

    def test_unbound_legacy_receipt_cannot_be_replayed_into_new_headers(self):
        log_text,prompt,response,_,subject=self.artifacts()
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp,'probe.md');path.write_text(log_text)
            with self.assertRaisesRegex(ValueError,'unbound or legacy-limited'):
                transcription_audit.prepare_replay(path,prompt,response,{},subject,Path(temp,'archive'))
            self.assertFalse(Path(temp,'archive').exists())


class CurrentRequestContext(unittest.TestCase):
    def checked_record(self, kind, path):
        result = self.parse(kind, path)
        result.update(input_context_policy=T.INPUT_CONTEXT_POLICY, complete_inputs="pass",
                      input_context_sha256="a" * 64, type_policy=T.TYPE_VALIDATION_POLICY, model_types="pass")
        return result

    def setUp(self):
        self.parse = C.parse_log
        self.replay = {"request_provenance":"bound", "type_errors":[],
                       "input_context":{"state":"pass", "required_sha256":"a" * 64}}

    def quality(self, replay=None, error=None):
        with patch.object(C, "parse_log", side_effect=self.checked_record), \
                patch.object(transcription_audit, "audit", return_value=replay or self.replay, side_effect=error):
            return C.compare("transcription", "dcprov", "deepseek")["quality"]

    def test_live_bound_request_check_passes_without_a_global_hold(self):
        quality=self.quality()
        self.assertFalse(any("verified current request context" in b for b in quality['blockers']))
        self.assertFalse(any("BUG-0129" in b for b in quality['blockers']))

    def test_stale_interface_hash_or_wording_cannot_pass_on_recorded_header(self):
        for context in [{"state":"pass", "required_sha256":"b" * 64},
                        {"state":"fail", "required_sha256":"a" * 64}]:
            with self.subTest(context=context):
                quality=self.quality({**self.replay,"input_context":context})
                self.assertTrue(any("verified current request context" in b for b in quality['blockers']))

    def test_changed_receipts_unbound_metadata_and_new_type_errors_fail_closed(self):
        for changes in [{"request_provenance":"legacy-limited"}, {"type_errors":[{"message":"bad gate"}]}]:
            with self.subTest(changes=changes):
                quality=self.quality({**self.replay,**changes})
                self.assertTrue(any("verified current request context" in b for b in quality['blockers']))
        quality=self.quality(error=ValueError("saved prompt differs from original receipt"))
        self.assertTrue(any("saved prompt differs" in b for b in quality['blockers']))

    def test_interface_fingerprint_is_bound_into_ruling_context(self):
        header='| required input context sha256 | '+ 'a' * 64 +' |\n| comparison policy | checked-expression-types-v2 |\n'
        self.assertNotEqual(rulings.review_context('transcription',header),
                            rulings.review_context('transcription',header.replace('a' * 64,'b' * 64)))


class DefinitionInterfaces(unittest.TestCase):
    def test_legacy_comparison_blocks_transcription_but_not_render(self):
        # Both dcprov reviews agree; a log compared before unit preservation must still not qualify.
        parse = C.parse_log
        def legacy(kind, path):
            result = parse(kind, path)
            result["comparison_policy"] = "legacy-unversioned"
            return result
        with patch.object(C, "parse_log", side_effect=legacy):
            transcription = C.compare("transcription", "dcprov", "deepseek")["quality"]
        self.assertEqual(transcription["state"], "pending")
        self.assertFalse(any("BUG-0129" in b for b in transcription["blockers"]))
        self.assertTrue(any("unit-preserving comparison" in b for b in transcription["blockers"]))
        rendering = C.compare("render", "dcprov", "deepseek")["quality"]
        self.assertEqual(rendering["state"], "pass")
        self.assertFalse(any("BUG-0129" in b for b in rendering["blockers"]))

    def test_either_family_without_passing_types_blocks_transcription(self):
        parse = C.parse_log
        for family in ("claude", "deepseek"):
            def checked(kind, path):
                result = parse(kind, path)
                result.update(comparison_policy=T.COMPARISON_POLICY, type_policy=T.TYPE_VALIDATION_POLICY,
                              model_types="fail" if families.split_stem(Path(path).stem)[1] == family else "pass")
                return result
            with self.subTest(family=family), patch.object(C, "parse_log", side_effect=checked):
                quality = C.compare("transcription", "dcprov", "deepseek")["quality"]
                self.assertTrue(any("expression type validation: " + family in b for b in quality["blockers"]))

    def test_legacy_prompt_cannot_qualify_merely_by_rechecking_expression_types(self):
        parse = C.parse_log
        def incomplete(kind, path):
            result = parse(kind, path)
            result.update(comparison_policy=T.COMPARISON_POLICY, type_policy=T.TYPE_VALIDATION_POLICY,
                          model_types="pass", input_context_policy="unrecorded", complete_inputs="unrecorded")
            return result
        with patch.object(C, "parse_log", side_effect=incomplete):
            quality = C.compare("transcription", "dcprov", "deepseek")["quality"]
        self.assertTrue(any("complete input context" in b for b in quality["blockers"]))

    def test_namespace_change_preserves_computation(self):
        project = [{"id": "line2"}, {"id": "line13"}]
        second = [{"id": "se.line13", "printed": "13", "expr": {"op": "multiply_rate", "amount": "se.line2", "rate": {"param": "se.half"}}}]
        normalized = T.normalize_definition_ids("se", project, second)
        self.assertEqual(normalized[0]["id"], "line13")
        self.assertEqual(normalized[0]["expr"], {"op": "multiply_rate", "amount": "line2", "rate": {"param": "se.half"}})
        self.assertEqual(second[0]["id"], "se.line13")

    def test_unknown_helpers_are_not_renamed(self):
        second = [{"id": "se.own_helper", "expr": {"op": "copy", "from": "se.own_input"}}]
        self.assertEqual(T.normalize_definition_ids("se", [{"id": "line13"}], second), second)

    def test_conflicting_namespace_aliases_are_rejected(self):
        second = [{"id": i, "expr": {"op": "copy", "from": "line2"}} for i in ("line13", "se.line13")]
        with self.assertRaisesRegex(ValueError, "conflicting ids"):
            T.normalize_definition_ids("se", [{"id": "line13"}], second)

    def test_required_families_can_differ_by_review_kind(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "families.json"
            path.write_text(json.dumps({"required": ["claude", "deepseek"], "optional": [],
                                       "by_kind": {"classm": {"required": ["claude"], "optional": ["deepseek"]}}}))
            with patch.object(families, "LIST", str(path)):
                self.assertEqual(families.load("render")["required"], ["claude", "deepseek"])
                self.assertEqual(families.load("classm")["required"], ["claude"])


def node_module(script):
    """Run an ES module snippet from this directory and return its JSON output."""
    out = subprocess.run(["node", "--input-type=module", "-e", script], cwd=str(Path(__file__).resolve().parent),
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


class ClassMReplyHandles(unittest.TestCase):
    """T-070 (1), T-081 (1), T-076 (1): answers keyed in a form the prompt did not give."""

    def write(self, fill, verdicts, existing=()):
        with tempfile.TemporaryDirectory() as temp, patch.object(rulings, "REVIEWS", temp), \
                patch.object(M, "LOGS", temp), patch.object(M.subjects, "current", return_value="a" * 64), \
                patch.object(M, "fixture_path", return_value=str(Path(temp, "fixtures.json"))):
            Path(temp, "classm").mkdir()
            if existing:
                Path(temp, "fixtures.json").write_text(json.dumps({"tax_year": 2025, "cases": list(existing)}))
            job = {"id": "classm.x.1", "branches": [], "inputs": {"x.a": 1}, "fill": fill,
                   "project": {l["id"]: {"kind": "money", "cents": 500} for l in fill}}
            run = {"used": [], "verdicts": verdicts, "raw": "raw", "prompt_sha": "b" * 64}
            err = io.StringIO()
            with patch.object(sys, "stderr", err):
                _, counts = M.write_outputs({"id": "x", "title": "Test"}, "claude-opus-5-5", [job],
                                            {job["id"]: run}, {job["id"]: {"model_reported": ["claude-opus-5-5"]}})
            return counts, err.getvalue()

    def test_unparenthesised_worksheet_marker_is_an_answer(self):
        fill = [{"id": "x.s5_1", "printed": "(Step 5, 1)", "label": "Step 5", "type": "Dollars"},
                {"id": "x.clw1", "printed": "(CLW 1)", "label": "CLW", "type": "Dollars"}]
        verdicts = M.extract('lines:\n  - printed: "Step 5, 1"\n    value: "5.00"\n  - printed: "line CLW 1"\n    value: "5.00"\n')
        counts, _ = self.write(fill, verdicts)
        self.assertEqual((counts["AGREE"], counts["MISSING"]), (2, 0))

    def test_echoed_value_type_is_an_answer_but_another_parenthesis_is_not(self):
        fill = [{"id": "x.line1", "printed": "1", "label": "One", "type": "NonNegDollars"},
                {"id": "x.line2", "printed": "2", "label": "Two", "type": "Dollars"}]
        verdicts = M.extract('lines:\n  - printed: "line 1 (NonNegDollars)"\n    value: "5.00"\n'
                             '  - printed: "line 2 (NonNegDollars)"\n    value: "5.00"\n')
        counts, _ = self.write(fill, verdicts)
        self.assertEqual((counts["AGREE"], counts["MISSING"]), (1, 1))

    def test_prompt_does_not_parenthesise_the_value_type_after_the_line_number(self):
        job = {"given": [], "own_inputs": [], "collections": {}, "status": "single",
               "fill": [{"id": "x.line1", "printed": "1", "label": "Enter the gain", "type": "NonNegDollars"}]}
        prompt = M.build_prompt({"id": "x", "title": "T", "tax_year": 2025}, "", job)
        self.assertNotIn("line 1 (NonNegDollars)", prompt)
        self.assertIn("- line 1: Enter the gain [value type: NonNegDollars]", prompt)

    def test_replaced_cases_are_named_for_the_mutation_step(self):
        fill = [{"id": "x.line1", "printed": "1", "label": "One", "type": "Dollars"}]
        old = [{"id": "classm.x.1", "inputs": {"x.a": 1}, "expect": {}}, {"id": "classm.x.2", "inputs": {"x.a": 9}, "expect": {}}]
        _, err = self.write(fill, {"1": {"value": "5.00", "work": ""}}, old)
        self.assertIn("1 earlier class M case(s) replaced (classm.x.2)", err)


class TranscriptionVisibility(unittest.TestCase):
    """T-076 (2): equal amounts do not agree when only the project hides the line."""

    def test_candidate_without_shown_when_differs_on_hidden_lines(self):
        import copy
        doc = T.load_form("g28")
        second = copy.deepcopy(doc["lines"])
        hidden = {T.marker_keys(doc["lines"])[l["id"]] for l in doc["lines"] if l.get("shown_when")}
        self.assertTrue(hidden)
        results, _ = T.compare("g28", doc["lines"], second)
        self.assertTrue(all(r["status"] == "AGREE" for r in results))
        for line in second:
            line.pop("shown_when", None)
        results, _ = T.compare("g28", doc["lines"], second)
        for r in results:
            if r["printed"] in hidden:
                self.assertEqual(r["status"], "DISAGREE", r["printed"])
                self.assertIn('"shown_when"', r["project"])


class TriageWitnesses(unittest.TestCase):
    """T-070 (2), T-070 (3), T-083."""

    def test_refused_or_unknown_visibility_is_not_a_shown_amount(self):
        out = node_module("import { displayed } from './triage_rules.mjs';"
                          "const v = { kind: 'money', cents: 500 };"
                          "console.log(JSON.stringify([displayed(v, { kind: 'refusal', reason: 'r' }), displayed(v, { kind: 'unknown' }),"
                          "displayed(v, { kind: 'bool', value: false }), displayed(v, { kind: 'bool', value: true })]))")
        self.assertEqual(out, [{"kind": "refusal"}, {"kind": "unknown"}, {"kind": "hidden"}, {"kind": "money", "cents": 500}])

    def test_completed_witnesses_are_sampled_apart_from_refused_ones(self):
        out = node_module("import { recordWitness } from './triage_rules.mjs';"
                          "const s = { witnesses: [], completed_witnesses: [] };"
                          "for (let i = 0; i < 10; i++) recordWitness(s, 'value', 'refused', () => ({ kind: 'value', i }), 6);"
                          "for (let i = 10; i < 26; i++) recordWitness(s, 'value', 'completed', () => ({ kind: 'value', i, project_return: 'completed' }), 6);"
                          "recordWitness(s, 'project-unknown', 'completed', () => ({ kind: 'project-unknown', i: 30 }), 6);"
                          "console.log(JSON.stringify([s.witnesses.length, s.completed_witnesses.map(w => w.i)]))")
        self.assertEqual(out, [7, [10, 11, 12, 13, 14, 15, 30]])

    def record(self, temp, line):
        import triage
        stem = families.stem("x", "deepseek")
        Path(temp, stem + ".json").write_text(json.dumps({"state": "invalid", "errors": ["bad ref"], "lines": [line]}))
        return triage

    def test_explain_reports_a_line_without_witnesses(self):
        with tempfile.TemporaryDirectory() as temp:
            triage = self.record(temp, {"handle": "3", "triage": "candidate invalid"})
            with patch.object(triage, "OUT", temp), self.assertRaisesRegex(SystemExit, "no witnesses .*candidate invalid"):
                triage.explain("x", "deepseek", "3", 0, 6)

    def test_explain_reaches_completed_witnesses(self):
        with tempfile.TemporaryDirectory() as temp:
            w = {"kind": "value", "source": {"kind": "fixture", "id": "f"}, "instance": "x", "project_return": "completed"}
            triage = self.record(temp, {"handle": "3", "triage": "differs", "project": "x.line3", "candidate": "x.line3",
                                        "witnesses": [], "completed_witnesses": [w]})
            seen = {}
            def run(cmd, input, **kw):
                seen["payload"] = json.loads(input)
                return subprocess.CompletedProcess(cmd, 0, stdout="{}", stderr="")
            with patch.object(triage, "OUT", temp), patch.object(triage.subprocess, "run", side_effect=run), \
                    patch("builtins.open", side_effect=lambda p, *a, **k: io.StringIO("lines: []") if str(p).endswith(".response.txt") else io.open(p, *a, **k)), \
                    patch.object(triage.T, "load_form", return_value={"lines": []}), patch.object(triage.T, "load_defs", return_value={}), \
                    patch.object(triage.T, "model_type_context", return_value={}), patch.object(sys, "stdout", io.StringIO()):
                triage.explain("x", "deepseek", "3", 0, 6, completed=True)
            self.assertEqual(seen["payload"]["explain"]["source"], w["source"])


class ClassMProvenance(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.jobs = Path(self.temp.name) / "jobs.json"
        self.job = {"id": "classm.fake.1", "doc": "fake", "fill": [], "given": [], "own_inputs": [1]}
        self.jobs.write_text(json.dumps({"jobs": [self.job]}))
        self.base = str(Path(self.temp.name) / "classm.fake.1.deepseek")
        with patch.object(T, "call_model", return_value=("lines: []", {"model_reported": ["deepseek-v4-pro"]})):
            T.review_response("AMOUNT 1", "deepseek-v4-pro", self.base, M.PROMPT_POLICY, system=M.SYSTEM)

    def run_main(self, extra):
        with patch.object(M, "JOBS", str(self.jobs)), patch.object(M, "RAW", self.temp.name), patch.object(M.subprocess, "run") as build, patch.object(M, "load_form", return_value={"id": "fake"}), patch.object(M, "manifest", return_value={}), patch.object(M, "excerpt_for", return_value=("SOURCE", [])), patch.object(M, "build_prompt", side_effect=lambda f, e, j: f"AMOUNT {j['own_inputs'][0]}"), patch.object(M, "write_outputs", return_value=("LOG", {"AGREE": 0, "DISAGREE": 0, "SKIPPED": 0, "MISSING": 0})) as write, patch.object(sys, "argv", ["classm.py", "--doc", "fake", "--model", "deepseek-v4-pro", *extra]), patch.object(T, "call_model", side_effect=AssertionError("must stay offline")):
            try:
                M.main()
            finally:
                self.assertEqual(build.call_count, 2, "reuse must also rebuild current jobs")
                self.written = write.call_count

    def test_current_jobs_can_reuse_matching_request(self):
        with self.assertRaises(SystemExit) as result:
            self.run_main(["--from-response"])
        self.assertEqual(result.exception.code, 0)
        self.assertEqual(self.written, 1)

    def test_changed_job_amount_cannot_relabel_saved_work_or_write_fixtures(self):
        self.job["own_inputs"] = [2]
        self.jobs.write_text(json.dumps({"jobs": [self.job]}))
        with self.assertRaisesRegex(ValueError, "fresh review"):
            self.run_main(["--from-response"])
        self.assertEqual(self.written, 0)

    def test_dry_run_preserves_actual_request_and_response(self):
        saved = {s: Path(self.base + s).read_bytes() for s in (".prompt.txt", ".response.txt", ".meta.json")}
        self.run_main(["--dry-run"])
        self.assertEqual(self.written, 0)
        self.assertTrue(Path(self.base + ".preview.prompt.txt").exists())
        self.assertEqual(saved, {s: Path(self.base + s).read_bytes() for s in saved})


class ResponseProvenance(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = str(Path(self.temp.name) / "qdcg.deepseek")
        self.model = "deepseek-v4-pro"

    def initial(self):
        with patch.object(T, "call_model", return_value=("RESPONSE", {"model_reported": [self.model]})) as call:
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, system="SYSTEM")
        self.assertEqual(call.call_count, 1)

    def test_exact_saved_request_can_be_reused_without_network(self):
        self.initial()
        with patch.object(T, "call_model", side_effect=AssertionError("must not call a model")):
            text, meta = T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM")
        self.assertEqual(text, "RESPONSE")
        self.assertEqual(meta["model_requested"], self.model)

    def test_changed_prompt_model_system_or_policy_requires_fresh_review(self):
        self.initial()
        for prompt, model, policy, system in (("OTHER", self.model, T.PROMPT_POLICY, "SYSTEM"),
                                               ("PROMPT", "deepseek-other", T.PROMPT_POLICY, "SYSTEM"),
                                               ("PROMPT", self.model, "other-policy", "SYSTEM"),
                                               ("PROMPT", self.model, T.PROMPT_POLICY, "OTHER")):
            with self.subTest(prompt=prompt, model=model, policy=policy, system=system):
                with self.assertRaisesRegex(ValueError, "fresh review"):
                    T.review_response(prompt, model, self.base, policy, True, system)

    def test_legacy_response_cannot_acquire_new_provenance(self):
        self.initial()
        Path(self.base + ".meta.json").write_text(json.dumps({"model_reported": [self.model]}))
        with self.assertRaisesRegex(ValueError, "fresh review"):
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM")

    def test_reasoning_effort_is_bound_in_both_directions(self):
        self.initial()
        with self.assertRaisesRegex(ValueError, "fresh review"):
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM", "max")
        with patch.object(T, "call_model", return_value=("STRONGER RESPONSE", {"model_reported": [self.model]})):
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, False, "SYSTEM", "max")
        with self.assertRaisesRegex(ValueError, "fresh review"):
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM")

    def test_output_budget_is_bound_in_both_directions(self):
        self.initial()
        with self.assertRaisesRegex(ValueError, "fresh review"):
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM", max_output_tokens=131072)
        with patch.object(T, "call_model", return_value=("LARGER RESPONSE", {"model_reported": [self.model]})) as call:
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, False, "SYSTEM", max_output_tokens=131072)
        self.assertEqual(call.call_args.kwargs["timeout"], 1800)
        with self.assertRaisesRegex(ValueError, "fresh review"):
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM")

    def test_original_fixed_budget_receipt_cannot_be_relabelled(self):
        self.initial()
        path = Path(self.base + ".meta.json")
        meta = json.loads(path.read_text()); meta.pop("request_max_tokens"); path.write_text(json.dumps(meta))
        original = path.read_bytes()
        text, reused = T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM")
        self.assertEqual(text, "RESPONSE")
        self.assertNotIn("request_max_tokens", reused)
        self.assertEqual(path.read_bytes(), original)
        with self.assertRaisesRegex(ValueError, "fresh review"):
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM", max_output_tokens=131072)

    def test_truncated_response_is_preserved_but_never_accepted(self):
        with patch.object(T, "call_model", return_value=("lines: []", {"finish_reason": "length", "model_reported": [self.model]})):
            with self.assertRaisesRegex(ValueError, "exhausted"):
                T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, system="SYSTEM")
        self.assertEqual(Path(self.base + ".response.txt").read_text(), "lines: []")
        with self.assertRaisesRegex(ValueError, "exhausted"):
            T.review_response("PROMPT", self.model, self.base, T.PROMPT_POLICY, True, "SYSTEM")

    def test_dry_run_does_not_overwrite_live_request(self):
        self.initial()
        before = {suffix: Path(self.base + suffix).read_bytes() for suffix in (".prompt.txt", ".response.txt", ".meta.json")}
        with patch.object(T, "RAW", self.temp.name), patch.object(sys, "argv", ["transcribe.py", "--form", "qdcg", "--model", self.model, "--dry-run"]), patch.object(T, "call_model", side_effect=AssertionError("dry run must be offline")):
            T.main()
        self.assertTrue(Path(self.base + ".preview.prompt.txt").exists())
        self.assertEqual(before, {suffix: Path(self.base + suffix).read_bytes() for suffix in before})


class CostLedger(unittest.TestCase):
    META = {"model_reported": ["deepseek-flash"], "usage": {"prompt_tokens": 1000, "completion_tokens": 100,
            "prompt_cache_hit_tokens": 200, "prompt_cache_miss_tokens": 800}, "cost_usd": None, "transport": "deepseek"}

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.ledger = Path(self.temp.name, T.LEDGER_NAME)

    def tearDown(self):
        self.temp.cleanup()

    def rows(self):
        return [json.loads(line) for line in self.ledger.read_text().splitlines()]

    def test_success_and_failure_each_append_one_line_without_touching_meta(self):
        meta = json.loads(json.dumps(self.META))
        with patch.object(T, "RAW", self.temp.name), patch.object(families, "selected_model", return_value="deepseek-flash"), \
                patch.object(T, "_call_deepseek", return_value=("lines: []", meta)):
            text, got = T.call_model("PUBLIC", "deepseek-flash", kind="render", subject="f8962")
        self.assertEqual((text, got), ("lines: []", self.META))
        with patch.object(T, "RAW", self.temp.name), patch.object(families, "selected_model", return_value="deepseek-flash"), \
                patch.object(T, "_call_deepseek", side_effect=RuntimeError("deepseek HTTP 500")):
            with self.assertRaisesRegex(RuntimeError, "HTTP 500"):
                T.call_model("PUBLIC", "deepseek-flash", kind="render", subject="f8962")
        ok, failed = self.rows()
        self.assertEqual((ok["kind"], ok["subject"], ok["model_requested"], ok["transport"], ok["prompt_chars"], ok["outcome"]),
                         ("render", "f8962", "deepseek-flash", "deepseek", 6, "ok"))
        self.assertEqual(ok["usage"], self.META["usage"])
        self.assertIsNone(ok["cost_usd"])
        self.assertIsInstance(ok["estimated_cost_usd"], float)
        self.assertTrue(failed["outcome"].startswith("error: RuntimeError"))

    def test_rejected_options_make_no_ledger_line(self):
        with patch.object(T, "RAW", self.temp.name), patch.object(T, "_call_claude", side_effect=AssertionError("no network")):
            with self.assertRaises(ValueError):
                T.call_model("PUBLIC", "claude-test", reasoning_effort="max")
        self.assertFalse(self.ledger.exists())

    def test_receipt_is_unchanged_by_the_ledger(self):
        base = str(Path(self.temp.name, "x"))
        with patch.object(T, "RAW", self.temp.name), patch.object(families, "selected_model", return_value="deepseek-flash"), \
                patch.object(T, "_call_deepseek", return_value=("lines: []", json.loads(json.dumps(self.META)))):
            T.review_response("PROMPT", "deepseek-flash", base, T.PROMPT_POLICY, system="SYSTEM", kind="transcription", subject="x")
        saved = json.loads(Path(base + ".meta.json").read_text())
        self.assertEqual(set(saved) - set(self.META), {"prompt_sha256", "system_sha256", "prompt_policy", "model_requested",
                                                       "reasoning_effort", "request_max_tokens"})
        self.assertEqual(self.rows()[0]["subject"], "x")

    def test_deepseek_estimate_follows_peak_hours(self):
        import datetime
        prices = {"models": {"m": {"basis": "deepseek", "source": "S", "off_peak_factor": 0.5, "peak_hours_utc": [[1, 4]],
                                   "per_million_usd": {"input_cache_hit": 1.0, "input_cache_miss": 2.0, "output": 4.0}}}}
        usage = {"prompt_cache_hit_tokens": 1_000_000, "prompt_cache_miss_tokens": 1_000_000, "completion_tokens": 1_000_000}
        monday_peak = datetime.datetime(2026, 11, 2, 2, tzinfo=datetime.timezone.utc)
        saturday = datetime.datetime(2026, 11, 7, 2, tzinfo=datetime.timezone.utc)
        self.assertEqual(T.estimate_cost("m", usage, None, monday_peak, prices)[0], 7.0)
        self.assertEqual(T.estimate_cost("m", usage, None, saturday, prices)[0], 3.5)
        self.assertEqual(T.estimate_cost("unpriced", usage, None, saturday, prices), (None, "no price entry"))

    def test_price_table_cites_every_filled_price(self):
        for model, entry in T.load_prices()["models"].items():
            with self.subTest(model=model):
                self.assertTrue(entry.get("source", "").startswith("https://"))

    def test_concurrent_writers_keep_whole_lines(self):
        import multiprocessing
        ctx = multiprocessing.get_context("fork")
        procs = [ctx.Process(target=_ledger_writer, args=(self.temp.name, n)) for n in range(4)]
        for p in procs:
            p.start()
        for p in procs:
            p.join()
        rows = self.rows()
        self.assertEqual(len(rows), 4 * 50)
        self.assertEqual({r["subject"] for r in rows}, {f"w{n}" for n in range(4)})


def _ledger_writer(raw, n):
    import datetime
    T.RAW = raw
    for _ in range(50):
        T.record_cost(datetime.datetime.now(datetime.timezone.utc), 0.1, "claude-x", "claude-print", "P" * 5000, "S",
                      {"usage": {}, "cost_usd": 0.01}, "ok", "transcription", f"w{n}")


class SourceCatalog(unittest.TestCase):
    def test_selection_ignores_the_reviewed_forms_encoding(self):
        mani = T.manifest()
        form = T.load_form("f8960")
        excerpt, used = T.excerpt_for(form, mani)
        before = T.catalog_selection(form, excerpt, used, mani)
        altered = json.loads(json.dumps(form))
        for line in altered["lines"]:
            line["expr"] = {"op": "copy", "from": "mq.total"}
            line["refuses"] = ["sc.unsupported"]
            line["shown_when"] = "ftc.credit"
        self.assertEqual(T.catalog_selection(altered, excerpt, used, mani), before)

    def test_named_line_of_a_worksheet_title_and_of_an_enter_on_sentence(self):
        mani = T.manifest()
        self.assertIn(("1040", "27a"), T.source_profile(T.load_form("eic"), mani)["fed"])
        self.assertIn(("1040", "2b"), T.source_profile(T.load_form("sb"), mani)["fed"])
        self.assertIn(("1040", "2b"), T.named_lines("Include • Form 1040 or 1040-SR, line 2b.", mani))
        self.assertIn(("1040s1", "17"), T.named_lines("enter it on line 17 of Schedule 1", mani))

    def test_screening_list_carries_each_gates_interface(self):
        lines = T.load_all_lines()
        gate = next(r["when"] for _, l in lines.values() for r in (l.get("refuses") or [])
                    if lines.get(r["when"], (0, {"expr": {}}))[1]["expr"].get("op") == "input")
        doc_id, line = lines[gate]
        self.assertIn(T.reference_note({"id": doc_id}, line), T.screen_notes())

    def test_shown_when_is_requested_where_the_source_conditions_a_line(self):
        with patch.object(T, "exported_lines", return_value=[]), patch.object(T, "collection_notes", return_value=""), \
                patch.object(T, "screen_notes", return_value=""):
            prompt = T.build_prompt(T.load_form("div"), "ARCHIVED SOURCE", {}, {})
        self.assertIn(T.SHOWN_WHEN_NOTE, prompt)
        self.assertIn("shown_when: <Bool line id of this document>", prompt)


class _Files(carry.Snapshot):
    """A snapshot held in memory: {relative path: text}."""

    def __init__(self, files):
        super().__init__("memory")
        self.files = files

    def read(self, rel):
        return self.files.get(rel)

    def forms(self):
        return sorted(p.split("/")[-1][:-5] for p in self.files if p.startswith("forms/") and p.endswith(".yaml"))

    def tables(self):
        return {}


def _form(fid, lines):
    return yaml.safe_dump({"form": {"id": fid, "title": fid, "lines": lines}})


class CarryOver(unittest.TestCase):
    """carry.py rules a repeat disagreement from an earlier ruling only when it and the line are unchanged."""
    LINES = [{"id": "x.a", "printed": "1", "type": "Dollars", "expr": {"op": "input"}, "cite": {"doc": "d", "locator": "p. 1"}},
             {"id": "x.b", "printed": "2", "type": "Dollars", "expr": {"op": "copy", "from": "x.a"}},
             {"id": "x.c", "printed": "3", "type": "Dollars", "expr": {"op": "copy", "from": "y.z"}}]
    OTHER = [{"id": "y.z", "printed": "1", "type": "Dollars", "expr": {"op": "input"}}]

    def files(self, lines=None, other=None):
        return {f"forms/{rulings.Y}/x.yaml": _form("x", lines or self.LINES),
                f"forms/{rulings.Y}/y.yaml": _form("y", other or self.OTHER), f"params/{rulings.Y}.yaml": "params: {}\n"}

    def write(self, rows, prompt="P"):
        args = ({"id": "x", "title": "Test form"}, "claude-opus-5-5")
        return T.write_log(*args, prompt, [], rows, [], "lines: []", {})

    def rows(self, second='{"op":"copy","from":"x.other"}'):
        return [{"printed": "2", "label": "B", "status": "DISAGREE", "project": '{"from":"x.a","op":"copy"}', "second": second},
                {"printed": "3", "label": "C", "status": "DISAGREE", "project": '{"from":"y.z","op":"copy"}', "second": '{"const":0}'}]

    def run_carry(self, temp, source_text, current, source=None, dry_run=False):
        with patch.object(carry, "source_log", return_value=(source_text, "old.md", source or _Files(self.files()))), \
                patch.object(carry.subjects, "of_text", return_value="a" * 64):
            return carry.carry("transcription", "x", origin="old.md", dry_run=dry_run, current=current)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.patches = [patch.object(rulings, "REVIEWS", self.temp.name), patch.object(T, "LOGS", self.temp.name),
                        patch.object(T.subjects, "current", return_value="a" * 64)]
        for p in self.patches:
            p.start()
        Path(self.temp.name, "transcription").mkdir()
        self.write(self.rows())
        rule.apply("x", {"2": "model error; the reply copies an unrelated line",
                         "3": {"ruling": "finding; line 3 reads the wrong input", "severity": "medium"}})
        self.source = Path(rulings.log_path("transcription", "x")).read_text()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.temp.cleanup()

    def test_repeat_disagreement_carries_with_its_source_and_class(self):
        self.write(self.rows(), prompt="a changed prompt")  # new review context: both open again
        text = Path(rulings.log_path("transcription", "x")).read_text()
        self.assertEqual(text.count("Ruling: open"), 2)
        ruled, stats, left = self.run_carry(self.temp.name, self.source, _Files(self.files()))
        self.assertEqual(list(ruled), ["2"])
        self.assertEqual(stats["carried"], 1)
        self.assertEqual(left, [("3", "earlier ruling not carried: finding or defect")])
        text = Path(rulings.log_path("transcription", "x")).read_text()
        line = next(l for l in text.splitlines() if l.startswith("Ruling: model error"))
        self.assertTrue(line.endswith("(carried over from old.md, review of " + carry.recorded(self.source, "date") + ")"))
        self.assertEqual(C.ruling_category(line[len("Ruling: "):]), "model_error")
        self.assertEqual(text.count("Ruling: open"), 1)  # the finding is re-judged
        side = rulings.load("transcription", "x")
        self.assertEqual({v["context"] for v in side.values() if v["ruling"] == line}, {rulings.review_context("transcription", text)})
        self.assertEqual(rulings.check(), 0)

    def test_dry_run_writes_nothing(self):
        self.write(self.rows(), prompt="a changed prompt")
        before = Path(rulings.log_path("transcription", "x")).read_text()
        ruled, _, _ = self.run_carry(self.temp.name, self.source, _Files(self.files()), dry_run=True)
        self.assertEqual(list(ruled), ["2"])
        self.assertEqual(Path(rulings.log_path("transcription", "x")).read_text(), before)

    def test_a_different_model_tree_does_not_carry(self):
        self.write(self.rows(second='{"op":"copy","from":"x.something_else"}'), prompt="a changed prompt")
        ruled, _, left = self.run_carry(self.temp.name, self.source, _Files(self.files()))
        self.assertEqual(ruled, {})
        self.assertIn(("2", "no earlier ruling on the same disagreement"), left)

    def test_a_changed_line_or_a_line_it_reads_does_not_carry(self):
        self.write(self.rows(), prompt="a changed prompt")
        changed = [dict(l) for l in self.LINES]
        changed[0] = {**changed[0], "type": "NonNegDollars"}  # x.a, read by line 2
        ruled, _, left = self.run_carry(self.temp.name, self.source, _Files(self.files(lines=changed)))
        self.assertEqual(ruled, {})
        self.assertIn(("2", "the project line or what it reads changed"), left)

    def test_a_citation_or_an_unread_line_does_not_block(self):
        self.write(self.rows(), prompt="a changed prompt")
        changed = [dict(l) for l in self.LINES]
        changed[0] = {**changed[0], "cite": {"doc": "d", "locator": "p. 2"}}
        changed[2] = {**changed[2], "type": "NonNegDollars"}  # x.c, not read by line 2
        ruled, _, _ = self.run_carry(self.temp.name, self.source, _Files(self.files(lines=changed)))
        self.assertEqual(list(ruled), ["2"])

    def test_closure_follows_other_documents(self):
        old, new = _Files(self.files()), _Files(self.files(other=[{**self.OTHER[0], "type": "NonNegDollars"}]))
        self.assertNotEqual(carry.line_subject("transcription", old, "x", "3"), carry.line_subject("transcription", new, "x", "3"))
        self.assertEqual(carry.line_subject("transcription", old, "x", "2"), carry.line_subject("transcription", new, "x", "2"))

    def test_a_stale_log_carries_nothing(self):
        self.write(self.rows(), prompt="a changed prompt")
        with patch.object(carry.subjects, "of_text", return_value="b" * 64):
            ruled, _, left = carry.plan("transcription", "x", origin="old.md", current=_Files(self.files()))
        self.assertEqual(ruled, {})
        self.assertEqual({w for _, w in left}, {"the log is stale; rerun first"})

    def test_validation_failure_is_ruled_mechanically_and_shown_when_is_not(self):
        invalid = T.canonical({"invalid_model_types": [{"line": "x.h", "message": "x.x.h: whole operand\nis not money"},
                                                       {"line": None, "message": "model contains a non-finite numeric value"}],
                               "expression": {"op": "copy", "from": "x.h"}})
        rows = [{"printed": "2", "label": "B", "status": "DISAGREE", "project": '{"from":"x.a","op":"copy"}', "second": invalid},
                {"printed": "3", "label": "C", "status": "DISAGREE", "project": '{"shown_when":{"line":"x.a"},"value":{"const":0}}',
                 "second": '{"shown_when":null,"value":{"const":0}}'}]
        self.write(rows, prompt="a changed prompt")
        with patch.object(carry, "source_log", return_value=(None, "no source log", None)), \
                patch.object(carry.subjects, "of_text", return_value="a" * 64):
            ruled, stats, left = carry.carry("transcription", "x", current=_Files(self.files()))
        self.assertEqual((list(ruled), stats["mechanical"], stats["carried"]), (["2"], 1, 0))
        self.assertEqual(left, [("3", "no source log")])  # a missing shown_when is a source reading
        text = Path(rulings.log_path("transcription", "x")).read_text()
        line = next(l for l in text.splitlines() if l.startswith(carry.MECHANICAL))
        self.assertIn('x.h: "x.x.h: whole operand is not money"', line)
        self.assertIn('the reply: "model contains a non-finite numeric value"', line)
        self.assertEqual(C.ruling_category(line[len("Ruling: "):]), "model_error")
        entry = next(v for v in rulings.load("transcription", "x").values() if v["ruling"] == line)
        self.assertEqual(entry["run"], T.response_sha256("lines: []"))
        self.assertRegex(entry["date"], r"^\d{4}-\d{2}-\d{2}$")
        # Not mechanical: a valid reply, a MISSING line, another kind.
        valid = {"status": "DISAGREE", "key": ("2", "{}", '{"op":"copy","from":"x.a"}')}
        self.assertIsNone(carry.mechanical("transcription", valid))
        self.assertIsNone(carry.mechanical("transcription", {"status": "MISSING", "key": ("2", "{}", "None")}))
        self.assertIsNone(carry.mechanical("render", {"status": "MISMATCH", "key": ("2", "x", invalid)}))
        self.assertEqual(rulings.check(), 0)

    def test_rulings_are_stamped_and_a_finding_needs_a_severity(self):
        side = rulings.load("transcription", "x")
        finding = next(v for v in side.values() if v["ruling"].startswith("Ruling: finding"))
        self.assertEqual((finding["severity"], finding["run"]), ("medium", T.response_sha256("lines: []")))
        self.write(self.rows(), prompt="a changed prompt")
        with self.assertRaisesRegex(SystemExit, "needs a severity"):
            rule.apply("x", {"3": "finding; again"})
        with self.assertRaisesRegex(SystemExit, "severity"):
            rule.apply("x", {"3": {"ruling": "defect in the line", "severity": "grave"}})
        self.assertEqual(rule.apply("x", {"3": "scope; no severity needed"}), ["3"])
        # Stamps survive a load/save round trip and malformed stamps fail the check.
        before = rulings.load("transcription", "x")
        self.assertTrue(all("date" in v for v in before.values()))
        rulings.save("transcription", "x", before)
        self.assertEqual(rulings.load("transcription", "x"), before)
        path = Path(rulings.sidecar_path("transcription", "x"))
        data = json.loads(path.read_text())
        data["rulings"][0]["run"] = "not-a-hash"
        path.write_text(json.dumps(data))
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(rulings.check(), 1)

    def test_a_section_names_the_reply_it_records(self):
        text = Path(rulings.log_path("transcription", "x")).read_text()
        self.assertEqual(rulings.section_reply("transcription", text, "2 — B", "Status: **DISAGREE**\n"), "lines: []")
        fenced = "```yaml\nlines:\n  - id: a\n```"
        classm_log = ("x\n## Lines\n\n### case c.1 — prompt sha256 " + "0" * 64 + "; branches: b\n\n## Raw responses\n\n"
                      "### c.1\n\n```yaml\n" + fenced + "\n```\n\n### c.2\n\n```yaml\nlines: []\n```\n")
        self.assertEqual(rulings.section_reply("classm", classm_log, "c.1 — 2 — L", ""), fenced)
        self.assertEqual(rulings.section_reply("classm", classm_log, "c.2 — 2 — L", ""), "lines: []")
        self.assertIsNone(rulings.section_reply("classm", classm_log, "c.3 — 2 — L", ""))

    def test_ledger_names_the_reply_a_ruling_stamps(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(T, "RAW", temp), \
                patch.object(families, "selected_model", return_value="deepseek-flash"), \
                patch.object(T, "_call_deepseek", return_value=("\nlines: []\n", {"usage": {}, "cost_usd": None})):
            T.call_model("PUBLIC", "deepseek-flash", kind="transcription", subject="x")
            row = json.loads(Path(temp, T.LEDGER_NAME).read_text())
        self.assertEqual(row["response_sha256"], T.response_sha256("lines: []"))
        self.assertEqual(row["prompt_sha256"], T.hashlib.sha256(b"PUBLIC").hexdigest())

    def test_classes_that_are_re_judged(self):
        self.assertEqual(carry.excluded("Ruling: finding; wrong line"), "finding or defect")
        self.assertEqual(carry.excluded("Ruling: defect in the encoding"), "finding or defect")
        self.assertEqual(carry.excluded("Ruling: project corrected after BUG-0001"), "finding or defect")
        self.assertEqual(carry.excluded("Ruling: interface gap; no contract yet"), "unsettled class (interface gap)")
        self.assertEqual(carry.excluded("Ruling: the model may be right"), "unsettled class (unclassified)")
        self.assertEqual(carry.excluded("Ruling: open"), "open")
        for settled in ("model error; x", "scope; x", "representation; x", "ambiguity (amb.x); x", "model error; x [dropped]"):
            self.assertIsNone(carry.excluded("Ruling: " + settled), settled)

    def test_carried_text_is_marked_once_and_keeps_the_drop(self):
        once = carry.carried_text("Ruling: model error; x [dropped]", "a/b.md", "2026-11-01")
        self.assertEqual(once, "Ruling: model error; x (carried over from a/b.md, review of 2026-11-01)")
        self.assertEqual(carry.carried_text(once, "c.md", "2026-11-03"), once)
        self.assertEqual(rulings.split_ruling(once + " [dropped]"), (once, True))

    def test_handles_name_lines(self):
        snap = _Files({f"forms/{rulings.Y}/x.yaml": _form("x", self.LINES + [
            {"id": "x.d", "printed": "4", "type": "Dollars", "expr": {"op": "input"}},
            {"id": "x.e", "printed": "4", "type": "Dollars", "expr": {"op": "input"}}])})
        self.assertEqual(carry.find_line(snap, "x", "1")["id"], "x.a")
        self.assertEqual(carry.find_line(snap, "x", "x.b")["id"], "x.b")
        self.assertEqual(carry.find_line(snap, "x", "b")["id"], "x.b")
        self.assertIsNone(carry.find_line(snap, "x", "4"))  # shared printed number
        self.assertEqual(carry.find_line(snap, "x", "4 (x.e)")["id"], "x.e")
        self.assertEqual(carry.find_line(snap, "x", "person[taxpayer].x[e1].c")["id"], "x.c")

    def test_content_keys(self):
        t = {"key": ("2", '{"b": 1, "a": 2}', '{"x": 1}'), "status": "DISAGREE", "case": None}
        u = {"key": ("2", '{"a":2,"b":1}', '{"x":1}'), "status": "DISAGREE", "case": None}
        self.assertEqual(carry.content("transcription", t), carry.content("transcription", u))
        r1 = {"key": ("2", "Enter line 1.", "objection one"), "status": "MISMATCH"}
        r2 = {"key": ("2", "Enter line 1.", "objection two"), "status": "MISMATCH"}
        r3 = {"key": ("2", "Enter line 1.", "objection two"), "status": "UNCLEAR"}
        self.assertEqual(carry.content("render", r1), carry.content("render", r2))
        self.assertNotEqual(carry.content("render", r2), carry.content("render", r3))
        m1 = {"key": ("classm.x.1", "2", "$1.00", "$2.00"), "status": "DISAGREE"}
        m2 = {"key": ("classm.x.1", "2", "$1.00", "$3.00"), "status": "DISAGREE"}
        self.assertNotEqual(carry.content("classm", m1), carry.content("classm", m2))

class CompletenessPages(unittest.TestCase):
    """The pages a completeness review is given."""

    def test_instructions_printed_on_the_form_are_used_only_when_no_other_document_is_cited(self):
        import completeness_review as CR
        line = lambda doc, loc: {"cite": {"doc": doc, "locator": loc}, "refuses": []}
        on_form = {"lines": [line("f4952", "p. 3, Line 1"), line("f4952", "p. 4")]}
        self.assertEqual(CR.cited_pages(on_form), {"f4952": {3, 4}})
        mixed = {"lines": [line("f4952", "p. 3"), line("i8960", "p. 9")]}
        self.assertEqual(CR.cited_pages(mixed), {"i8960": {9}})


class LocatorPages(unittest.TestCase):
    """transcribe.py reads page lists with tools/citations.py's grammar."""
    def test_pages_joined_by_and_are_all_read(self):
        self.assertEqual(T.locator_pages("pp. 17 and 19, Steps 1 and 4"), {17, 19})
        self.assertEqual(T.locator_pages("p. 12, Column (g); p946 pp. 71–73 and 77–79, Table A-2"), {12, 71, 72, 73, 77, 78, 79})

    def test_a_hyphenated_document_id_names_its_own_pages(self):
        mani = {"i5695": {}, "fs-2025-01": {}}
        more, rest = T.secondary_pages('p. 1, Costs; fs-2025-01 p. 5, Energy Efficient', mani, "i5695")
        self.assertEqual(more, {"fs-2025-01": {5}})
        self.assertEqual(T.locator_pages(rest), {1})


def synthetic_reply(lines):
    return "lines:\n" + yaml.safe_dump([{k: l[k] for k in ("id", "printed", "type", "expr") if k in l}
                                        for l in lines], sort_keys=False)


class LineScopedReviews(unittest.TestCase):
    """A line-scoped review reviews only some lines and merges into the existing log; no model call."""
    FORM = "f8960"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        for kind in ("transcription", "render"):
            Path(self.temp.name, kind).mkdir()
        for target, value in ((rulings, "REVIEWS"), (T, "LOGS"), (R, "LOGS"), (T, "RAW")):
            p = patch.object(target, value, self.temp.name if value != "LOGS" else str(Path(self.temp.name, "transcription" if target is T else "render")))
            p.start(); self.addCleanup(p.stop)
        self.doc = T.load_form(self.FORM)
        self.computed = [l for l in self.doc["lines"] if l["expr"].get("op") != "input"]

    def base_log(self, change=None):
        """A whole review of the form from a synthetic reply equal to the project's lines except `change`."""
        reply = [dict(l, **(change or {}).get(l["id"], {})) for l in self.computed]
        raw = synthetic_reply(reply)
        results, extra = T.compare(self.FORM, self.doc["lines"], T.extract_yaml(raw)["lines"])
        T.write_log(self.doc, "claude-opus-5-5", "BASE PROMPT", [], results, extra, raw, {"prompt_policy": T.PROMPT_POLICY})
        return Path(rulings.log_path("transcription", self.FORM)).read_text()

    def scoped(self, names, reply_lines, recorded=None, receipts=False):
        """Run transcribe.py's --lines path with a synthetic saved reply; with `receipts`, the reply's
        receipt is saved where the pass records it, as review_response saves it."""
        args = type("A", (), {"form": self.FORM, "model": "claude-opus-5-5", "lines": names, "dry_run": False,
                              "from_response": False, "reasoning_effort": None, "max_output_tokens": None})()
        params_doc = T.project_yaml(Path(T.ROOT) / "params" / f"{T.Y}.yaml")
        values = (params_doc.get("params") or params_doc)["values"]
        reply = (synthetic_reply(reply_lines), {"prompt_policy": T.LINE_PROMPT_POLICY, "model_reported": ["claude-opus-5-5"]})

        def respond(prompt, model, base, policy, *rest, **kw):
            meta = {**reply[1], **self.bound_meta(prompt, policy, model)}
            for suffix, value in ((".prompt.txt", prompt), (".response.txt", reply[0]), (".meta.json", json.dumps(meta))):
                Path(base + suffix).write_text(value)
            return reply[0], meta
        with contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(T, "review_response", **({"side_effect": respond} if receipts else {"return_value": reply})))
            stack.enter_context(patch.object(T, "call_model", side_effect=AssertionError("offline")))
            if recorded is not None:
                stack.enter_context(patch.object(T, "recorded_line_subjects", return_value=(recorded, "test")))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            try:
                T.scoped_main(args, self.doc, T.manifest(), {k: v["value"] for k, v in values.items()}, values)
            except SystemExit:
                pass
        return Path(rulings.log_path("transcription", self.FORM)).read_text()

    def sections(self, text):
        return dict((part.partition("\n")[0].split(" — ")[0], part)
                    for part in text.partition("\n## Lines\n")[2].split("\n## ")[0].split("\n### ")[1:])

    def test_reach_stops_at_printed_lines_and_records_their_type(self):
        members, boundary = T.subjects.reach(self.doc, "f8960.line8")
        self.assertIn("f8960.line1", boundary)
        self.assertNotIn("f8960.line1", members)
        text = Path(T.FORMS, self.FORM + ".yaml").read_text()
        keys = T.line_keys(self.doc)
        base, _ = T.subjects.line_subjects_of("transcription", self.FORM, text, keys)
        moved = text.replace("from: f1040.line2b", "from: f1040.line2a", 1)
        other, _ = T.subjects.line_subjects_of("transcription", self.FORM, moved, keys)
        self.assertEqual([k for k in base if base[k] != other[k]], ["1"])
        retyped = text.replace("      printed: \"1\"\n      type: Dollars", "      printed: \"1\"\n      type: NonNegDollars", 1)
        self.assertNotEqual(retyped, text)
        third, _ = T.subjects.line_subjects_of("transcription", self.FORM, retyped, keys)
        self.assertEqual(sorted(k for k in base if base[k] != third[k]), ["1", "8"])

    def test_scoped_prompt_lists_only_scoped_lines_and_no_project_computation(self):
        scope, reach = T.scoped_lines(self.doc, ["f8960.line1"])
        self.assertEqual(scope, {"f8960.line1", "f8960.line8"})
        with patch.object(T, "collection_notes", return_value=""), patch.object(T, "screen_notes", return_value=""):
            full = T.build_prompt(self.doc, "SOURCE", {}, {})
            again = T.build_prompt(self.doc, "SOURCE", {}, {}, scope=None)
            part = T.build_prompt(self.doc, "SOURCE", {}, {}, scope=scope)
        self.assertEqual(full, again)
        self.assertIn("printed '1' (id f8960.line1", part)
        self.assertIn(T.SCOPE_NOTE, part)
        listed = part.partition(T.SCOPE_NOTE)[2].partition("\n\n")[0]
        self.assertIn("printed '17' (id f8960.line17", listed)
        self.assertNotIn("f8960.line1;", listed)
        for line in self.computed:   # no project expression or computed label enters the request
            if line["id"] not in scope and line["printed"] in T.HELPER_PRINTED:
                self.assertNotIn(line["id"], part)
        self.assertNotIn("f1040.line2b", part.replace("SOURCE", ""))

    def test_partial_review_merges_and_keeps_rulings_of_both_reviews(self):
        old = self.base_log({"f8960.line2": {"expr": {"op": "copy", "from": "f1040.line3a"}}})
        self.assertEqual(rule.apply(self.FORM, {"2": "representation; base-review ruling"}), ["2"])
        old = Path(rulings.log_path("transcription", self.FORM)).read_text()
        self.assertIn(T.subjects.LINE_SUBJECTS, old)
        self.assertIsNone(T.subjects.log_state("transcription", self.FORM, T.Y, old))
        rows, rest = T.subjects.recorded(old)
        stale = dict(rows, **{"1": "0" * 64})   # as if line 1 changed since the base review
        reply = [l for l in self.computed if l["id"] in ("f8960.line8",)] + \
                [{"id": "f8960.line1", "printed": "1", "type": "Dollars", "expr": {"op": "copy", "from": "f1040.line2a"}}]
        new = self.scoped("auto", reply, recorded=(stale, rest))
        before, after = self.sections(old), self.sections(new)
        self.assertEqual(set(before), set(after))
        for key in before:
            if key == "1":
                self.assertIn("Status: **DISAGREE**", after[key])
                self.assertRegex(after[key], r"Ruling: open\nReviewed in: pass [0-9a-f]{12}\n")
            else:
                self.assertEqual(before[key], after[key], key)
        self.assertIn("Ruling: representation; base-review ruling", after["2"])
        self.assertEqual(new.partition("\n## Lines\n")[0].count("| line-scoped reviews | 1 "), 1)
        self.assertIn("| agree / disagree / missing | 23 / 2 / 0 |", new)
        self.assertEqual(len(rulings.pass_blocks(new)), 1)
        self.assertIsNone(T.subjects.log_state("transcription", self.FORM, T.Y, new))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(rulings.check(), 0)
        # A ruling on the pass's section is bound to the pass's own context.
        self.assertEqual(rule.apply(self.FORM, {"1": "model error; line 1 is line 2b"}), ["1"])
        new = Path(rulings.log_path("transcription", self.FORM)).read_text()
        contexts = {k[0]: v["context"] for k, v in rulings.load("transcription", self.FORM).items()}
        base_context = rulings.review_context("transcription", new)
        self.assertEqual(contexts["2"], base_context)
        self.assertEqual(contexts["1"], rulings.review_context("transcription", next(iter(rulings.pass_blocks(new).values()))))
        self.assertNotEqual(contexts["1"], base_context)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(rulings.check(), 0)
        # The same request and disagreement again reuses that ruling; the replaced pass is not duplicated.
        again = self.scoped("auto", reply, recorded=(stale, rest))
        self.assertNotIn("Ruling: open", again)
        self.assertEqual(len(rulings.pass_blocks(again)), 1)
        # A wider pass (line 1 named explicitly brings line 8, its reader) replaces the narrower one.
        wider = self.scoped("f8960.line1", reply)
        blocks = rulings.pass_blocks(wider)
        self.assertEqual(len(blocks), 1)
        self.assertIn("| review scope | lines 1, 8 |", next(iter(blocks.values())))
        self.assertIn("Ruling: open", self.sections(wider)["1"])   # a new request: the earlier ruling is not reused
        # Every line of an earlier pass reviewed again by the whole review: no pass remains.
        self.base_log()
        self.assertEqual(rulings.pass_blocks(Path(rulings.log_path("transcription", self.FORM)).read_text()), {})

    @staticmethod
    def bound_meta(prompt, policy, model="claude-opus-5-5"):
        return {"prompt_sha256": transcription_audit.sha(prompt), "system_sha256": transcription_audit.sha(T.TRANSCRIBE_SYSTEM),
                "prompt_policy": policy, "model_requested": model}

    def test_audit_verifies_each_line_scoped_pass(self):
        reply = [dict(l) for l in self.computed]
        raw = synthetic_reply(reply)
        meta = self.bound_meta("BASE PROMPT", T.PROMPT_POLICY)
        results, extra = T.compare(self.FORM, self.doc["lines"], T.extract_yaml(raw)["lines"])
        T.write_log(self.doc, "claude-opus-5-5", "BASE PROMPT", [], results, extra, raw, meta)
        for suffix, value in ((".prompt.txt", "BASE PROMPT"), (".response.txt", raw), (".meta.json", json.dumps(meta))):
            Path(T.RAW, self.FORM + suffix).write_text(value)
        path = Path(rulings.log_path("transcription", self.FORM))
        old = path.read_text()
        rows, rest = T.subjects.recorded(old)
        line1 = [{"id": "f8960.line1", "printed": "1", "type": "Dollars", "expr": {"op": "copy", "from": "f1040.line2a"}}]
        new = self.scoped("auto", [l for l in self.computed if l["id"] == "f8960.line8"] + line1,
                          recorded=(dict(rows, **{"1": "0" * 64}), rest), receipts=True)
        (pid, block), = rulings.pass_blocks(new).items()
        with patch.object(T.subjects, "log_state", return_value=None):
            result = transcription_audit.audit(path)
        self.assertEqual(result["request_provenance"], "bound")
        (p,) = result["passes"]
        self.assertEqual((p["pass"], p["request_provenance"], p["type_errors"], p["changes"]), (pid, "bound", [], []))
        self.assertEqual(p["scope"], ["1"])
        self.assertEqual(p["input_context"]["required_sha256"], C.parse_log_text("transcription", new)["passes"][pid]["input_context_sha256"])
        # The pass is held to its own receipt.
        receipt = Path(T.ROOT, transcription_audit.fields_of(block)["receipt"] + ".response.txt")
        receipt.write_text(receipt.read_text() + "\n  - id: extra\n")
        with patch.object(T.subjects, "log_state", return_value=None), self.assertRaisesRegex(ValueError, "embedded in the pass"):
            transcription_audit.audit(path)
        # A stale line fails the merged log before any reply is compared.
        with patch.object(T.subjects, "log_state", return_value="the transcription log is stale for lines 1"), \
                self.assertRaisesRegex(ValueError, "stale"):
            transcription_audit.audit(path)

    @contextlib.contextmanager
    def reworded(self, line_id, question):
        """The year's documents with one other document's input question reworded."""
        index = T.subjects._all_lines(T.Y)
        fid, line = index[line_id]
        changed = {**line, "expr": {**line["expr"], "source": question}}
        with patch.dict(T.subjects._ALL, {T.Y: {**index, line_id: (fid, changed)}}):
            yield

    def test_a_reworded_foreign_question_stales_exactly_its_readers(self):
        before = T.subjects.current_foreign("sa", T.Y)
        with self.reworded("person.blind", "Were you blind? (reworded)"):
            after = T.subjects.current_foreign("sa", T.Y)
        self.assertEqual(sorted(k for k in before if before[k] != after[k]), ["sa.deduction", "sa.itemizes"])
        # A log of the reader records the rows; the rewording stales those lines, and --lines auto takes them.
        old = self.base_log()
        rows = T.subjects.recorded_foreign(old)
        self.assertEqual(set(rows), {k for k, _ in T.line_keys(self.doc)})
        self.assertIsNone(T.subjects.log_state("transcription", self.FORM, T.Y, old))
        read = sorted({s for l in self.doc["lines"] for s in T.subjects._strings({k: v for k, v in l.items() if k != "id"})
                       if s in T.subjects._all_lines(T.Y) and not s.startswith(self.FORM + ".")
                       and (T.subjects._all_lines(T.Y)[s][1].get("expr") or {}).get("op") == "input"})
        target = read[0]
        with self.reworded(target, "A reworded question"):
            moved = T.subjects.foreign_stale(self.FORM, T.Y, old)
            self.assertTrue(moved)
            self.assertIn("foreign interfaces", T.subjects.log_state("transcription", self.FORM, T.Y, old))
            with contextlib.redirect_stdout(io.StringIO()):
                keys, *_ = T.plan_scope("transcription", self.FORM, old, ["auto"])
            self.assertEqual(sorted(keys), sorted(moved))
            # A line-scoped review of those lines rewrites their rows and keeps the others.
            by_id = dict(T.line_keys(self.doc))
            new = self.scoped("auto", [l for l in self.computed if l["id"] in T.members_of(self.doc, {by_id[k] for k in moved})])
            self.assertIsNone(T.subjects.log_state("transcription", self.FORM, T.Y, new))
            after = T.subjects.recorded_foreign(new)
        self.assertEqual({k for k in rows if rows[k] != after[k]}, set(moved))
        # Back to the original wording, the rewritten rows are stale and the others are not.
        self.assertEqual(sorted(T.subjects.foreign_stale(self.FORM, T.Y, new)), sorted(moved))
        # A log written before the table existed is not checked (the check is prospective).
        legacy = re.sub(r"\n## Foreign interfaces\n.*?(?=\n## )", "", old, flags=re.S)
        self.assertIsNone(T.subjects.recorded_foreign(legacy))
        with self.reworded(target, "A reworded question"):
            self.assertIsNone(T.subjects.log_state("transcription", self.FORM, T.Y, legacy))

    def test_a_pass_record_is_held_to_the_header_conditions(self):
        good = {"model": "deepseek-flash", "reported": "deepseek-flash", "policy": T.LINE_PROMPT_POLICY,
                "comparison_policy": T.COMPARISON_POLICY, "type_policy": T.TYPE_VALIDATION_POLICY, "model_types": "pass",
                "input_context_policy": T.INPUT_CONTEXT_POLICY, "complete_inputs": "pass", "input_context_sha256": "a" * 64}
        with patch.object(families, "selected_model", return_value="deepseek-flash"):
            self.assertEqual(C.pass_blockers("transcription", "deepseek", good), [])
            for change, blocker in [({"policy": "source-only-computation-v1+lines-v1"}, "prompt-independence"),
                                    ({"model_types": "fail"}, "type validation"), ({"complete_inputs": "fail"}, "input context"),
                                    ({"comparison_policy": "legacy"}, "unit-preserving"),
                                    ({"reported": "claude-opus-5-5"}, "named second family")]:
                with self.subTest(change=change):
                    self.assertTrue(any(blocker in b for b in C.pass_blockers("transcription", "deepseek", {**good, **change})))
            self.assertEqual(C.pass_blockers("render", "deepseek", {**good, "policy": "anything"}), [])

    def test_per_line_staleness_names_exactly_the_lines_not_yet_reviewed(self):
        old = self.base_log()
        self.assertIsNone(T.subjects.log_state("transcription", self.FORM, T.Y, old))
        tampered = re.sub(r"^\| 16 \| [0-9a-f]{64} \|$", "| 16 | " + "0" * 64 + " |", old, flags=re.M)
        state = T.subjects.log_state("transcription", self.FORM, T.Y, tampered.replace(
            re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", old, re.M).group(1), "1" * 64))
        self.assertIn("lines changed or not yet reviewed: 16;", state)
        self.assertIn("--lines auto", state)
        rest = re.sub(r"^\| \(rest of the document\) \| [0-9a-f]{64} \|$", "| (rest of the document) | " + "0" * 64 + " |", old, flags=re.M)
        self.assertIn("outside every compared line", T.subjects.log_state("transcription", self.FORM, T.Y, rest.replace(
            re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", old, re.M).group(1), "1" * 64)))

    def test_a_scope_missing_a_changed_line_is_refused(self):
        old = self.base_log()
        rows, rest = T.subjects.recorded(old)
        with self.assertRaises(SystemExit) as raised, contextlib.redirect_stdout(io.StringIO()):
            with patch.object(T, "recorded_line_subjects", return_value=((dict(rows, **{"16": "0" * 64}), rest), "test")):
                T.plan_scope("transcription", self.FORM, old, ["f8960.line1"])
        self.assertIn("16", str(raised.exception))

    def test_legacy_log_with_every_line_current_records_its_table_without_a_call(self):
        old = self.base_log()
        cur = T.subjects.recorded(old)
        subject = re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", old, re.M).group(1)
        # Reviewed whole before tables existed, of a version that differs from the current one only
        # outside every line subject (e.g. a reworded refusal no compared line reaches).
        legacy = (old.partition("\n" + T.subjects.LINE_SUBJECTS + "\n")[0] + "\n## Raw second transcription\n"
                  + old.partition("\n## Raw second transcription\n")[2]).replace(subject, "1" * 64)
        Path(rulings.log_path("transcription", self.FORM)).write_text(legacy)
        self.assertIn("earlier form", T.subjects.log_state("transcription", self.FORM, T.Y, legacy))
        new = self.scoped("auto", [], recorded=cur)
        self.assertEqual(T.subjects.recorded(new), cur)
        self.assertIsNone(T.subjects.log_state("transcription", self.FORM, T.Y, new))
        self.assertEqual(self.sections(new), self.sections(legacy))
        # A second run finds the table and leaves the log as it is.
        self.assertEqual(self.scoped("auto", []), new)

    def test_legacy_log_finds_the_reviewed_version(self):
        old = self.base_log()
        legacy = old.partition("\n" + T.subjects.LINE_SUBJECTS + "\n")[0] + "\n## Raw second transcription\n" + old.partition("\n## Raw second transcription\n")[2]
        (rec, where) = T.recorded_line_subjects("transcription", self.FORM, legacy)
        self.assertEqual(where, "working tree")
        self.assertEqual(rec, T.subjects.recorded(old))

    def test_render_partial_review_merges(self):
        judged = R.judged_lines(self.doc)
        verdicts = {e["key"]: {"status": "MATCH", "reason": "says what the text says"} for e in judged}
        verdicts["2"] = {"status": "MISMATCH", "reason": "base objection"}
        R.write_log(self.doc, "claude-opus-5-5", "BASE", [], judged, verdicts, "raw", {})
        self.assertEqual(rule.apply(self.FORM, {"2": "representation; base"}, "render"), ["2"])
        old = Path(rulings.log_path("render", self.FORM)).read_text()
        scope = R.render_scope(self.doc, ["f8960.line1"])
        keys = [e["key"] for e in R.judged_lines(self.doc, scope)]
        self.assertIn("1", keys)
        reply = "lines:\n" + "".join(f'  - key: "{k}"\n    status: {"UNCLEAR" if k == "1" else "MATCH"}\n    reason: "pass reason"\n' for k in keys)
        args = type("A", (), {"form": self.FORM, "model": "claude-opus-5-5", "lines": "f8960.line1", "dry_run": False,
                              "from_response": False, "reasoning_effort": None, "max_output_tokens": None})()
        with patch.object(R, "review_response", return_value=(reply, {"prompt_policy": R.LINE_PROMPT_POLICY})), \
                contextlib.redirect_stdout(io.StringIO()):
            try:
                R.scoped_main(args, self.doc)
            except SystemExit:
                pass
        new = Path(rulings.log_path("render", self.FORM)).read_text()
        before, after = self.sections(old), self.sections(new)
        self.assertEqual(set(before), set(after))
        for key in before:
            if key in keys:
                self.assertRegex(after[key], r"Reviewed in: pass [0-9a-f]{12}\n")
            else:
                self.assertEqual(before[key], after[key], key)
        self.assertIn("Status: **UNCLEAR**", after["1"])
        self.assertIsNone(T.subjects.log_state("render", self.FORM, T.Y, new))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(rulings.check(), 0)


class ScopedCatalog(unittest.TestCase):
    """A line-scoped request's catalog is narrowed by the scoped lines' citations; no model call."""

    def scoped(self, fid, names):
        mani = T.manifest()
        doc = T.load_form(fid)
        scope, reach = T.scoped_lines(doc, names)
        scoped_doc = {**doc, "lines": [l for l in doc["lines"] if l["id"] in reach]}
        excerpt, used = T.excerpt_for(scoped_doc, mani)
        return doc, scope, reach, excerpt, used, mani, scoped_doc

    def test_named_forms_are_narrowed_and_required_interfaces_stay(self):
        for fid, names in (("sales", ["sales.e", "sales.g"]), ("sli", ["1"])):
            doc, scope, reach, excerpt, used, mani, scoped_doc = self.scoped(fid, names)
            before = T.catalog_selection(doc, excerpt, used, mani, whole_text=False)
            after = T.catalog_selection(doc, excerpt, used, mani, whole_text=False, cited=scoped_doc)
            for d, why in before.items():
                if why != "named form":
                    self.assertEqual(after[d], why, d)        # the other source rules are unchanged
                elif d in after and after[d] != why:
                    listed = T.listed_lines(fid, d, after)
                    self.assertTrue(after[d].startswith(T.NAMED_FORM_INPUTS), d)
                    self.assertFalse(T.load_form(d).get("collection"), d)
                    self.assertTrue({l["id"] for l in T.load_form(d)["lines"] if l["expr"].get("op") == "input"} <= listed)
                elif d not in after:   # a collection, or a form with no input the excerpt names no line of
                    other = T.load_form(d)
                    self.assertTrue(other.get("collection") or not any(l["expr"].get("op") == "input" for l in other["lines"]), d)
            self.assertNotIn(fid, after)
            prompt = T.build_prompt(doc, excerpt, {}, T.catalog_lines(fid, after), None, T.collection_notes(fid, after), scope=scope)
            assessed = {**doc, "lines": [l for l in doc["lines"] if l["id"] in reach or l["expr"].get("op") == "input"]}
            self.assertEqual(input_context.assess(assessed, [], T.model_type_context(), prompt)["missing"], [], fid)
            if fid == "sales":
                self.assertNotIn("person", after)
                self.assertIn("f1040.status", T.listed_lines(fid, "f1040", after))
                self.assertIn("sales.e", prompt)                  # the reviewed collection's fields are all listed
                whole = T.build_prompt(doc, excerpt, {}, T.catalog_lines(fid, before), None, T.collection_notes(fid, before), scope=scope)
                self.assertLess(len(prompt), 0.75 * len(whole))

    def test_a_whole_review_catalog_is_unchanged(self):
        doc = T.load_form("sales")
        mani = T.manifest()
        excerpt, used = T.excerpt_for(doc, mani)
        whole = T.catalog_selection(doc, excerpt, used, mani)
        self.assertFalse(any(why.startswith((T.NAMED_LINES, T.NAMED_FORM_INPUTS)) for why in whole.values()))
        self.assertIn("named form", whole.values())


class WordingBlindSubjects(unittest.TestCase):
    """A transcription log's line subjects leave out wording (label, help, note), and the no-call
    migration rewrites a table to them without turning a stale log current."""
    FORM = "f8960"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        Path(self.temp.name, "transcription").mkdir()
        self.yaml = Path(self.temp.name, self.FORM + ".yaml")
        self.orig = Path(T.FORMS, self.FORM + ".yaml").read_text()
        self.yaml.write_text(self.orig)
        real = T.subjects.path
        for target, value, new in ((rulings, "REVIEWS", self.temp.name), (T, "LOGS", str(Path(self.temp.name, "transcription"))),
                                   (T, "RAW", self.temp.name),
                                   (T.subjects, "path", lambda kind, fid, year: str(self.yaml) if kind == "transcription" and fid == self.FORM
                                    else real(kind, fid, year))):
            p = patch.object(target, value, new)
            p.start(); self.addCleanup(p.stop)
        self.doc = T.load_form(self.FORM)
        self.keys = T.line_keys(self.doc)

    def edited(self, change):
        """The YAML of the form with `change(document)` applied; written as the working tree."""
        raw = yaml.safe_load(self.orig)
        change(raw["form"])
        text = yaml.safe_dump(raw, sort_keys=False, allow_unicode=True)
        self.yaml.write_text(text)
        return text

    def line(self, doc, line_id):
        return next(l for l in doc["lines"] if l["id"] == line_id)

    def base_log(self):
        """A whole review written while the working tree is the original YAML (synthetic agreeing reply)."""
        self.yaml.write_text(self.orig)
        computed = [l for l in self.doc["lines"] if l["expr"].get("op") != "input"]
        raw = synthetic_reply(computed)
        results, extra = T.compare(self.FORM, self.doc["lines"], T.extract_yaml(raw)["lines"])
        T.write_log(self.doc, "claude-opus-5-5", "BASE PROMPT", [], results, extra, raw, {"prompt_policy": T.PROMPT_POLICY})
        return Path(rulings.log_path("transcription", self.FORM)).read_text()

    def citation_only_log(self):
        """The same review with the line subjects the table recorded before wording was left out."""
        with ML.citation_only_subjects():
            return self.base_log()

    def state(self, text):
        return T.subjects.log_state("transcription", self.FORM, T.Y, text)

    def wording(self, doc):
        doc["note"] = "Reworded document note."
        self.line(doc, "f8960.line8")["label"] = "Reworded label of line 8"
        self.line(doc, "f8960.prior_2i")["label"] = "Reworded label of an input"
        self.line(doc, "f8960.line17")["note"] = "A new note on line 17."

    def test_a_wording_edit_does_not_stale_a_log(self):
        log = self.base_log()
        self.assertIsNone(self.state(log))
        text = self.edited(self.wording)
        self.assertNotEqual(T.subjects.of_form(text), T.subjects.of_form(self.orig))   # the whole subject moved
        self.assertIsNone(self.state(log))

    def test_an_input_question_or_title_edit_stales(self):
        log = self.base_log()
        self.edited(lambda d: self.line(d, "f8960.prior_2i")["expr"].update(source="A reworded question?"))
        state = self.state(log)
        self.assertIn("lines changed or not yet reviewed:", state)
        stale = state.partition("lines changed or not yet reviewed: ")[2].partition(";")[0].split(", ")
        readers = sorted(k for k, i in self.keys if "f8960.prior_2i" in T.subjects.closure(self.doc, i))
        self.assertEqual(sorted(stale), readers)
        self.assertTrue(readers)
        self.edited(lambda d: d.update(title="Another title"))     # the request carries the title
        self.assertIn("outside every compared line", self.state(log))

    def test_migration_rewrites_a_citation_only_table_and_is_idempotent(self):
        old = self.citation_only_log()
        self.assertIsNone(self.state(old))
        self.assertIsNone(ML.state_before(self.FORM, old))
        self.edited(self.wording)
        self.assertIsNotNone(self.state(old))   # unmigrated, a wording edit stales it
        self.yaml.write_text(self.orig)
        versions = ML.Versions(self.FORM, T.Y, texts=[("working tree", self.orig)])
        new, how, before, after = ML.migrate_one(self.FORM, old, T.Y, versions, self.keys)
        self.assertIn("rows rewritten from the working tree", how)
        self.assertEqual((before, after), (None, None))
        self.assertEqual(T.subjects.recorded(new), T.subjects.current_line_subjects("transcription", self.FORM, T.Y))
        self.assertEqual(new.replace(T.subjects.LINE_SUBJECTS, "").count("\n"), old.replace(T.subjects.LINE_SUBJECTS, "").count("\n"))
        outside = lambda t: t.partition("\n" + T.subjects.LINE_SUBJECTS + "\n")[0] + t.partition("\n" + T.subjects.FOREIGN + "\n")[2]
        self.assertEqual(outside(new), outside(old))                   # nothing else in the log changes
        again, how, _, _ = ML.migrate_one(self.FORM, new, T.Y, versions, self.keys)
        self.assertEqual(again, new)
        self.assertEqual(how, "already wording-blind")
        # Migrated, the log stays current through a wording edit.
        self.edited(self.wording)
        self.assertIsNone(self.state(new))

    def test_a_genuinely_stale_log_stays_stale(self):
        old = self.citation_only_log()
        changed = self.edited(lambda d: (self.wording(d), self.line(d, "f8960.line1")["expr"].update({"from": "f1040.line2a"})))
        versions = lambda: ML.Versions(self.FORM, T.Y, texts=[("working tree", changed), ("revision 0123456789ab", self.orig)])
        self.assertIsNotNone(ML.state_before(self.FORM, old))
        new, how, before, after = ML.migrate_one(self.FORM, old, T.Y, versions(), self.keys)
        self.assertIn("revision 0123456789ab", how)
        self.assertEqual(after, "the transcription log is stale for lines changed or not yet reviewed: 1; "
                                f"rerun them: transcribe.py --form {self.FORM} --lines auto")
        self.assertEqual(ML.migrate_one(self.FORM, new, T.Y, versions(), self.keys)[0], new)
        # A log reviewed whole with no table: the table of its reviewed version is recorded, still stale for line 1.
        legacy = (old.partition("\n" + T.subjects.LINE_SUBJECTS + "\n")[0] + "\n## Raw second transcription\n"
                  + old.partition("\n## Raw second transcription\n")[2])
        self.assertIn("reviewed an earlier form", ML.state_before(self.FORM, legacy))
        new, how, _, after = ML.migrate_one(self.FORM, legacy, T.Y, versions(), self.keys)
        self.assertEqual(how, "table recorded from the revision 0123456789ab")
        self.assertIn("lines changed or not yet reviewed: 1;", after)
        self.assertIsNone(T.subjects.recorded_foreign(new))

    def test_a_stale_log_the_migration_would_make_current_is_left_as_it_is(self):
        old = self.base_log()
        legacy = (old.partition("\n" + T.subjects.LINE_SUBJECTS + "\n")[0] + "\n## Raw second transcription\n"
                  + old.partition("\n## Raw second transcription\n")[2])
        changed = self.edited(self.wording)
        versions = ML.Versions(self.FORM, T.Y, texts=[("working tree", changed), ("revision 0123456789ab", self.orig)])
        new, how, before, after = ML.migrate_one(self.FORM, legacy, T.Y, versions, self.keys)
        self.assertEqual(new, legacy)
        self.assertIn("would turn stale -> current, left as it is", how)
        self.assertIsNotNone(before)
        self.assertEqual(after, before)


import gates as G  # noqa: E402
import screen_review as SR  # noqa: E402
import check_screens as CS  # noqa: E402
import false_no_review as FN  # noqa: E402
import check_false_no as CFN  # noqa: E402


def _gate_lines(condition_prompt="Did you or your spouse receive any dividends?"):
    """A synthetic document `div` with one existence gate `div.any` over two gated inputs, and a computed condition
    `div.has_1a` gating a third; `lines` as screen_review.load_lines gives them."""
    cite = {"doc": "i1099div", "locator": "p. 1, Box 1a"}
    eq = lambda ref, v: {"op": "test", "eq": [ref, {"const": v}]}
    def gate(gid, cond, inp, guard=None):
        g = guard or (lambda v: eq(cond, v))
        return {"id": gid, "printed": gid[-2:], "label": gid, "type": "NonNegDollars", "cite": cite,
                "expr": {"op": "choose", "alternatives": [{"guard": g(True), "then": inp}, {"guard": g(False), "then": "div.zero"}]}}
    def inp(iid, gid, q):
        return {"id": iid, "printed": "1", "label": iid, "type": "NonNegDollars", "cite": cite, "gated_by": gid,
                "expr": {"op": "input", "source": q}}
    ls = [
        {"id": "div.any", "printed": "(gate)", "label": "Any dividends", "type": "Bool", "cite": cite, "expr": {"op": "input", "source": condition_prompt}},
        gate("div.box1a", "div.any", "div.box1a_amount"), inp("div.box1a_amount", "div.box1a", "Ordinary dividends (box 1a)"),
        gate("div.box2a", "div.any", "div.box2a_amount"), inp("div.box2a_amount", "div.box2a", "Capital gain distributions (box 2a)"),
        {"id": "div.has_1a", "printed": "(helper)", "label": "Box 1a above zero", "type": "Bool", "cite": cite,
         "expr": {"op": "test", "gt": ["div.box1a", {"const": 0}]}},
        gate("div.box1b", "div.has_1a", "div.box1b_amount"), inp("div.box1b_amount", "div.box1b", "Qualified dividends (box 1b)"),
        {"id": "div.zero", "printed": "zero", "label": "zero", "type": "NonNegDollars", "cite": cite, "expr": {"op": "param", "ref": "div.zero"}},
    ]
    return {l["id"]: ("div", l) for l in ls}


ENGLISH = lambda doc, lid: f"English of {lid}"


class GateUnits(unittest.TestCase):
    def setUp(self):
        stack = contextlib.ExitStack()
        self.addCleanup(stack.close)
        stack.enter_context(patch.object(G, "_QUESTIONS", {}))

    def test_gate_lines_group_by_their_condition(self):
        units = G.units(_gate_lines())
        self.assertEqual(sorted(units), ["gate:div.any", "gate:div.has_1a"])
        self.assertEqual([g["id"] for _, g, _ in units["gate:div.any"]["gates"]], ["div.box1a", "div.box2a"])
        self.assertEqual([i["id"] for _, _, i in units["gate:div.any"]["gates"]], ["div.box1a_amount", "div.box2a_amount"])
        self.assertEqual(units["gate:div.has_1a"]["condition"], "div.has_1a")
        self.assertEqual(G.unit_form(units["gate:div.any"], _gate_lines()), "div")

    def test_the_subject_follows_wording_and_gated_lines_not_the_prompt(self):
        lines = _gate_lines()
        unit = G.units(lines)["gate:div.any"]
        base = G.subject(unit, lines, ENGLISH)
        self.assertEqual(base, G.subject(unit, _gate_lines(), ENGLISH))
        reworded = _gate_lines("Did you receive any dividends?")
        self.assertNotEqual(base, G.subject(G.units(reworded)["gate:div.any"], reworded, ENGLISH))
        relabelled = _gate_lines()
        relabelled["div.box2a_amount"][1]["expr"]["source"] = "Capital gain distributions"
        self.assertNotEqual(base, G.subject(G.units(relabelled)["gate:div.any"], relabelled, ENGLISH))
        self.assertNotEqual(base, G.subject(unit, lines, lambda d, l: "other English"))
        recited = _gate_lines()
        recited["div.box1a"][1]["cite"] = {"doc": "i1099div", "locator": "p. 2, Box 1a"}
        self.assertNotEqual(base, G.subject(G.units(recited)["gate:div.any"], recited, ENGLISH))
        # The interview's own wording, where the bank gives one, is what the filer reads.
        with patch.object(G, "_QUESTIONS", {"div.any": {"prompt": "Any dividends or fund distributions?", "help": "Not sure is yes."}}):
            self.assertNotEqual(base, G.subject(unit, lines, ENGLISH))

    def test_a_marker_whose_gate_line_is_not_a_choose_makes_no_unit(self):
        lines = _gate_lines()
        lines["div.box2a"][1]["expr"] = {"op": "sum", "of": ["div.box2a_amount"]}
        self.assertEqual([g["id"] for _, g, _ in G.units(lines)["gate:div.any"]["gates"]], ["div.box1a"])


class GateReviewRuns(unittest.TestCase):
    """The screen review of a gate and the false-no review, run offline: the model call is a stub, the archived pages
    a placeholder, and every file goes to a temporary directory."""
    REPLY_COVERS = "verdict: COVERS\nfindings: []\n"
    REPLY_FALSE_NO = ("verdict: FALSE_NO\nfindings:\n  - kind: FALSE_NO\n    pattern: '1'\n    who: a filer paid in 2025 on a 2021 sale\n"
                      "    why_no: in 2025\n    line: div.box1a\n    irs_text: x\n    severity: high\n    fix: any year\n")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        stack = contextlib.ExitStack()
        self.addCleanup(stack.close)
        stack.enter_context(patch.object(G, "_QUESTIONS", {}))
        for mod in (SR, FN):
            stack.enter_context(patch.object(mod, "RAW", self.temp.name))
            stack.enter_context(patch.object(mod, "excerpt_for", return_value=("ARCHIVED PAGES", [{"doc": "i1099div", "pages": [1]}])))
        stack.enter_context(patch.object(SR, "encoded_english", ENGLISH))
        stack.enter_context(patch.object(FN, "encoded_english", ENGLISH))
        stack.enter_context(patch.object(CS, "encoded_english", ENGLISH))
        stack.enter_context(patch.object(CFN, "encoded_english", ENGLISH))
        self.out = Path(self.temp.name) / "false_no"
        stack.enter_context(patch.object(FN, "OUT", str(self.out)))
        self.lines = _gate_lines()
        self.unit = G.units(self.lines)["gate:div.any"]

    def test_the_screen_review_covers_choose_guard_gates(self):
        units = SR.units(self.lines)
        self.assertEqual(units["gate:div.any"][0], "gate")
        prompt, used = SR.prompt_for("gate:div.any", self.unit, self.lines, {})
        for text in ("Did you or your spouse receive any dividends?", "div.box1a", "div.box2a_amount", "Capital gain distributions (box 2a)",
                     "English of div.box1a", "ARCHIVED PAGES", "NARROW", "SOURCE", "spouse"):
            self.assertIn(text, prompt)
        with patch.object(SR, "call_model", side_effect=AssertionError("a dry run makes no call")):
            dry = SR.run_one("gate:div.any", self.unit, self.lines, {}, "claude-opus-5-5", True, False)
        self.assertEqual(dry["lines"], 2)
        with patch.object(SR, "call_model", return_value=(self.REPLY_COVERS, {"model_reported": ["claude-opus-5-5"], "cost_usd": 0.2})) as call:
            r = SR.run_one("gate:div.any", self.unit, self.lines, {}, "claude-opus-5-5", False, False)
        self.assertEqual(call.call_args.kwargs["kind"], "screen")
        self.assertEqual(call.call_args.kwargs["subject"], "gate:div.any")
        self.assertEqual((r["kind"], r["verdict"], r["condition"]), ("gate", "COVERS", "div.any"))
        self.assertEqual(r["subject_sha"], G.subject(self.unit, self.lines, ENGLISH))
        self.assertTrue((Path(self.temp.name) / "gate_div.any.prompt.txt").exists())

    def test_screen_currency_of_gates(self):
        sha = G.subject(self.unit, self.lines, ENGLISH)
        kinds = lambda reviewed, rulings={}: {f["line"]: f["kind"] for f in CS.gate_findings(self.lines, reviewed, rulings)}
        self.assertEqual(kinds({})["gate:div.any"], "stale")
        current = {"gate:div.any": {"subject_sha": sha, "prompt_sha": "p1", "verdict": "COVERS"},
                   "gate:div.has_1a": {"subject_sha": G.subject(G.units(self.lines)["gate:div.has_1a"], self.lines, ENGLISH), "prompt_sha": "p", "verdict": "COVERS"}}
        self.assertEqual(kinds(current), {})
        changed = _gate_lines("Did you receive dividends?")
        self.assertEqual({f["line"]: f["kind"] for f in CS.gate_findings(changed, current, {})}, {"gate:div.any": "stale"})
        narrow = dict(current, **{"gate:div.any": dict(current["gate:div.any"], verdict="NARROW", findings=[{"kind": "NARROW"}])})
        self.assertEqual(kinds(narrow), {"gate:div.any": "unruled"})
        self.assertEqual(kinds(narrow, {"unruled:gate:div.any": {"prompt_sha": "p0"}}), {"gate:div.any": "rerun"})
        self.assertEqual(kinds(dict(current, **{"gate:gone": {}})), {"gate:gone": "orphan"})

    def test_the_false_no_review_logs_per_form_with_its_kind_in_the_cost_ledger(self):
        prompt, _ = FN.prompt_for(self.unit, self.lines, {})
        for text in ("Did you or your spouse receive any dividends?", "adversarial", "A narrow time frame", "A missing spouse",
                     "A document for a fact", "L-1", "L-43" if "L-43" in FN.PATTERNS else "L-40", "severity", "ARCHIVED PAGES"):
            self.assertIn(text, prompt)
        with patch.object(FN, "call_model", side_effect=AssertionError("a dry run makes no call")):
            self.assertEqual(FN.run_one("gate:div.any", self.unit, self.lines, {}, "claude-opus-5-5", True, False)["lines"], 2)
        with patch.object(FN, "call_model", return_value=(self.REPLY_FALSE_NO, {"model_reported": ["claude-opus-5-5"], "cost_usd": 0.25})) as call:
            r = FN.run_one("gate:div.any", self.unit, self.lines, {}, "claude-opus-5-5", False, False)
        self.assertEqual((call.call_args.kwargs["kind"], call.call_args.kwargs["subject"]), ("false_no", "gate:div.any"))
        self.assertEqual(T.TOOL_KINDS["false_no_review.py"], "false_no")
        self.assertEqual((r["verdict"], r["form"], r["findings"][0]["severity"]), ("FALSE_NO", "div", "high"))
        FN.write_results([r])
        log = json.loads((self.out / "div.json").read_text())
        self.assertEqual(list(log["reviews"]), ["gate:div.any"])
        # A rerun of another gate merges into the same form's log.
        r2 = dict(r, gate="gate:div.has_1a", verdict="SOUND", findings=[])
        FN.write_results([r2])
        self.assertEqual(sorted(json.loads((self.out / "div.json").read_text())["reviews"]), ["gate:div.any", "gate:div.has_1a"])
        # --from-response parses the saved reply without a call.
        with patch.object(FN, "call_model", side_effect=AssertionError("offline")):
            again = FN.run_one("gate:div.any", self.unit, self.lines, {}, "claude-opus-5-5", False, True)
        self.assertEqual(again["verdict"], "FALSE_NO")

    def test_false_no_currency_and_rulings(self):
        with patch.object(FN, "call_model", return_value=(self.REPLY_FALSE_NO, {"model_reported": ["claude-opus-5-5"]})):
            r = FN.run_one("gate:div.any", self.unit, self.lines, {}, "claude-opus-5-5", False, False)
        with patch.object(FN, "call_model", return_value=("verdict: SOUND\nfindings: []\n", {"model_reported": ["claude-opus-5-5"]})):
            r2 = FN.run_one("gate:div.has_1a", G.units(self.lines)["gate:div.has_1a"], self.lines, {}, "claude-opus-5-5", False, False)
        reviewed = {"gate:div.any": ("div", r), "gate:div.has_1a": ("div", r2)}
        kinds = lambda lines, reviewed, rulings={}: {f["line"]: f["kind"] for f in CFN.findings(lines, reviewed, rulings)}
        self.assertEqual(kinds(self.lines, {}), {"gate:div.any": "stale", "gate:div.has_1a": "stale"})
        self.assertEqual(kinds(self.lines, reviewed), {"gate:div.any": "unruled"})
        self.assertEqual(kinds(self.lines, reviewed, {"unruled:gate:div.any": {"prompt_sha": "older"}}), {"gate:div.any": "rerun"})
        self.assertEqual(kinds(_gate_lines("Did you get dividends?"), reviewed), {"gate:div.any": "stale"})
        self.assertEqual(kinds(self.lines, dict(reviewed, **{"gate:gone": ("div", {})})), {"gate:div.any": "unruled", "gate:gone": "orphan"})
        # Accepted by a ruling naming the review's prompt hash (tools/baseline_check.py), and the report written.
        rulings_path, report = Path(self.temp.name) / "rulings.json", Path(self.temp.name) / "report.md"
        rulings_path.write_text(json.dumps({"rulings": {"unruled:gate:div.any": {"prompt_sha": r["prompt_sha"], "reason": "L-1 designed out"}}}))
        found = CFN.findings(self.lines, reviewed, json.loads(rulings_path.read_text())["rulings"])
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(CFN.baseline_check.run("false_no", [], found, rulings_path, report, "t", "l"), 0)
            self.assertEqual(CFN.baseline_check.run("false_no", [], found, Path(self.temp.name) / "none.json", report, "t", "l"), 1)


def _screen_lines(gated):
    """Document `div` with a refusal screen `div.pr` (a Bool input) and the line `div.line` that refuses on it; with
    `gated`, the screen's input is gated on `div.any` by the gate line `div.pr_if_any`, which the refusal names."""
    cite = {"doc": "i1099div", "locator": "p. 1"}
    eq = lambda ref, v: {"op": "test", "eq": [ref, {"const": v}]}
    refusal = {"when": "div.pr_if_any" if gated else "div.pr", "form": "Form X", "remedy": "file it", "cite": cite}
    ls = [
        {"id": "div.any", "printed": "(gate)", "label": "Any", "type": "Bool", "cite": cite, "expr": {"op": "input", "source": "Any dividends?"}},
        {"id": "div.pr", "printed": "(screen)", "label": "Screen", "type": "Bool", "cite": cite, "expr": {"op": "input", "source": "Outside scope?"}},
        {"id": "div.line", "printed": "1", "label": "Line", "type": "NonNegDollars", "cite": cite, "refuses": [refusal],
         "expr": {"op": "const", "value": 0}},
        {"id": "div.false", "printed": "f", "label": "false", "type": "Bool", "cite": cite, "expr": {"op": "param", "ref": "div.false"}},
    ]
    if gated:
        ls[1]["gated_by"] = "div.pr_if_any"
        ls.append({"id": "div.pr_if_any", "printed": "g", "label": "gate", "type": "Bool", "cite": cite,
                   "expr": {"op": "choose", "alternatives": [{"guard": eq("div.any", True), "then": "div.pr"},
                                                             {"guard": eq("div.any", False), "then": "div.false"}]}})
    return {l["id"]: ("div", l) for l in ls}


class GatedScreens(unittest.TestCase):
    """A refusal screen whose input is gated stays a screen: its refusals name the gate line, not the input."""

    def setUp(self):
        stack = contextlib.ExitStack()
        self.addCleanup(stack.close)
        stack.enter_context(patch.object(G, "_QUESTIONS", {}))
        stack.enter_context(patch.object(SR, "encoded_english", ENGLISH))
        stack.enter_context(patch.object(SR, "excerpt_for", return_value=("ARCHIVED PAGES", [])))

    def test_a_gated_screen_is_still_a_screen(self):
        for gated in (False, True):
            found = SR.screens(_screen_lines(gated))
            self.assertEqual(list(found), ["div.pr"])
            self.assertEqual([l["id"] for _, l, _ in found["div.pr"]], ["div.line"])

    def test_a_refusal_on_a_gate_of_a_non_bool_input_is_not_a_screen(self):
        lines = _screen_lines(True)
        lines["div.pr"][1]["type"] = "NonNegDollars"
        self.assertEqual(SR.screens(lines), {})

    def test_the_prompt_shows_the_gate_and_the_subject_ignores_it(self):
        plain, gated = _screen_lines(False), _screen_lines(True)
        p_plain, _ = SR.prompt_for("div.pr", SR.screens(plain)["div.pr"], plain, {})
        p_gated, _ = SR.prompt_for("div.pr", SR.screens(gated)["div.pr"], gated, {})
        self.assertNotIn("Gate condition", p_plain)
        self.assertIn("Gate condition: The filer is asked (input `div.any`", p_gated)
        self.assertIn("Any dividends?", p_gated)
        self.assertIn("Outside scope?", p_gated)
        self.assertEqual(SR.screen_subject("div.pr", SR.screens(plain)["div.pr"], plain, {}),
                         SR.screen_subject("div.pr", SR.screens(gated)["div.pr"], gated, {}))
        self.assertEqual(SR.screen_subject("div.pr", SR.screens(plain)["div.pr"], plain, {}),
                         __import__("hashlib").sha256(p_plain.encode()).hexdigest())

    def test_a_review_recorded_before_the_gate_stays_current_and_a_reworded_screen_does_not(self):
        plain, gated = _screen_lines(False), _screen_lines(True)
        old = SR.screen_subject("div.pr", SR.screens(plain)["div.pr"], plain, {})
        for lines, record in ((gated, {"prompt_sha": old, "verdict": "COVERS"}),
                              (plain, {"prompt_sha": old, "verdict": "COVERS"})):
            with patch.object(CS, "load_lines", return_value=lines), patch.object(CS, "manifest", return_value={}), \
                    patch.object(CS, "screens", SR.screens), patch.object(CS, "RECORD", Path(tempfile.mkdtemp()) / "r.json"), \
                    patch.object(CS, "RULINGS", Path("/nonexistent")), patch.object(CS.pending, "listed", return_value=set()):
                CS.RECORD.write_text(json.dumps([{"screen": "div.pr", **record}]))
                self.assertEqual([f for f in CS.findings() if f["line"] == "div.pr"], [])
        reworded = _screen_lines(True)
        reworded["div.pr"][1]["expr"]["source"] = "Outside scope or abroad?"
        with patch.object(CS, "load_lines", return_value=reworded), patch.object(CS, "manifest", return_value={}), \
                patch.object(CS, "RECORD", Path(tempfile.mkdtemp()) / "r.json"), patch.object(CS, "RULINGS", Path("/nonexistent")), \
                patch.object(CS.pending, "listed", return_value=set()):
            CS.RECORD.write_text(json.dumps([{"screen": "div.pr", "prompt_sha": old, "verdict": "COVERS"}]))
            self.assertEqual([f["kind"] for f in CS.findings() if f["line"] == "div.pr"], ["stale"])


class StructuredTextOneLineTests(unittest.TestCase):
    """Where a question or label shares a line with what follows it, structured text keeps its items and nesting."""
    STRUCTURED = "Does any of these apply?\n\nIncluding:\n- a\n  - c\n  - d\n- b\n\nIf none, answer no."

    def test_inline_keeps_item_boundaries_and_nesting(self):
        import structured_text as S
        self.assertEqual(S.inline(self.STRUCTURED),
                         "Does any of these apply? \u2014 Including: (1) a [nested: c; d]; (2) b \u2014 If none, answer no.")

    def test_inline_leaves_plain_text_unchanged(self):
        import structured_text as S
        self.assertEqual(S.inline("Plain  question, one line."), "Plain  question, one line.")

    def test_reference_note_and_classm_names_use_it(self):
        line = {"id": "x.q", "printed": "(gate)", "type": "Bool", "expr": {"op": "input", "source": self.STRUCTURED}}
        self.assertIn("input Does any of these apply? \u2014 Including: (1) a [nested: c; d]; (2) b", T.reference_note({"id": "x"}, line))
        given = {"doc": "other", "printed": "(helper)", "label": self.STRUCTURED}
        with patch.object(M, "title_of", return_value="Other"):
            self.assertIn("Including: (1) a [nested: c; d]; (2) b", M.given_name(given, "x"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
