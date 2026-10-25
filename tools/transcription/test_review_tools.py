#!/usr/bin/env python3
"""Offline regression tests for independence, noise accounting and response provenance."""
import json
import io
import sys
import tempfile
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


class DefinitionInterfaces(unittest.TestCase):
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
