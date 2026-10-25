#!/usr/bin/env python3
"""Offline regression tests for independence, noise accounting and response provenance."""
import json
import io
import sys
import tempfile
import subprocess
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
        gate = {"id": "fake.gate", "expr": {"op": "input", "source": question}}
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
            path, _ = T.write_log({"id": "probe", "title": "Probe"}, "deepseek-flash", "request", [], result, [], "raw", {})
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


class DefinitionInterfaces(unittest.TestCase):
    def test_transcription_unit_audit_hold_does_not_block_render_qualification(self):
        # Both dcprov reviews agree; a known comparer defect must still prevent promotion.
        parse = C.parse_log
        def legacy(kind, path):
            result = parse(kind, path)
            result["comparison_policy"] = "legacy-unversioned"
            return result
        with patch.object(C, "parse_log", side_effect=legacy):
            transcription = C.compare("transcription", "dcprov", "deepseek")["quality"]
        self.assertEqual(transcription["state"], "pending")
        self.assertTrue(any("BUG-0129" in b for b in transcription["blockers"]))
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
