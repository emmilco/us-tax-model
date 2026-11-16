#!/usr/bin/env python3
"""Unit tests of tools/rename_ids.py: the three forms of an id, renamed and found; and apply and check on a small
tree of their own (fixtures with defaults, coverage rows, personas, rulings sidecars of two families, New York)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "transcription"))
import rename_ids as R  # noqa: E402

MAP = {"f8853c.pre1996": "f8853c.contract_before_ltc_date",
       "f8853c.pre1996_if_reimbursed": "f8853c.contract_before_ltc_date_if_reimbursed",
       "rec.not_2024": "rec.before_prior_year",
       "a.moved_2025": "b.moved_now"}
DOCS = {"clcw26": "clcw_next_year"}


class Forms(unittest.TestCase):
    def setUp(self):
        self.sub = R.substituter(MAP, DOCS)
        self.find = R.finder(MAP, DOCS)

    def test_whole(self):
        self.assertEqual(self.sub("f8853c.pre1996 and rec.not_2024."),
                         "f8853c.contract_before_ltc_date and rec.before_prior_year.")
        for other in ("f8853c.pre1996x", "x.f8853c.pre1996", "f8853c.pre1996.more", "classm.f8853c.pre1996"):
            self.assertEqual(self.sub(other), other, other)
            self.assertEqual(self.find(other), [], other)

    def test_collection_indexed(self):
        # the miss of 2026-11-16: a fixture key and a refusal's gate, written with a collection index
        self.assertEqual(self.sub('"f8853c[p0].pre1996": true, "gate": "f8853c[p0].pre1996_if_reimbursed"'),
                         '"f8853c[p0].contract_before_ltc_date": true, '
                         '"gate": "f8853c[p0].contract_before_ltc_date_if_reimbursed"')
        self.assertEqual(self.sub("f8853c[*].pre1996 f8853c[].pre1996"),
                         "f8853c[*].contract_before_ltc_date f8853c[].contract_before_ltc_date")

    def test_path_step(self):
        self.assertEqual(self.sub("person[taxpayer].f8853c[c1].pre1996: true"),
                         "person[taxpayer].f8853c[c1].contract_before_ltc_date: true")
        self.assertEqual(self.sub("x.f8853c[c1].pre1996"), "x.f8853c[c1].pre1996")  # a dotted id, not a path step
        self.assertEqual(self.sub("other[c1].pre1996"), "other[c1].pre1996")  # another document's local name

    def test_document(self):
        self.assertEqual(self.sub("$clcw26 clcw26.line1 $x@clcw26[a] person[t].clcw26[a].line1"),
                         "$clcw_next_year clcw_next_year.line1 $x@clcw_next_year[a] person[t].clcw_next_year[a].line1")
        for other in ("clcw26x", "xclcw26", "a.clcw26"):
            self.assertEqual(self.sub(other), other, other)

    def test_moved_document_is_found_not_rewritten(self):
        self.assertEqual(self.sub("a[k].moved_2025"), "a[k].moved_2025")
        self.assertEqual(self.find("a[k].moved_2025"), ["a.moved_2025"])
        self.assertEqual(self.sub("a.moved_2025"), "b.moved_now")

    def test_find_every_form(self):
        self.assertEqual(self.find("f8853c[p0].pre1996 rec.not_2024 person[t].f8853c[q].pre1996_if_reimbursed $clcw26"),
                         ["clcw26", "f8853c.pre1996", "f8853c.pre1996_if_reimbursed", "rec.not_2024"])
        text = "f8853c[p0].pre1996 rec.not_2024 person[t].f8853c[q].pre1996_if_reimbursed $clcw26 clcw26[x]"
        self.assertEqual(self.find(self.sub(text)), [])

    def test_witness(self):
        w = "partial:x2s1o.f8853c.adb-f8853c[p0].pre1996@f8853c[p0]"
        self.assertEqual(R._witness(w, self.sub),
                         "partial:x2s1o.f8853c.adb-f8853c[p0].contract_before_ltc_date@f8853c[p0]")
        # a case id is a label: kept, and not reported
        w = "fixture:classm.clcw26.2@clcw26"
        self.assertEqual(R._witness(w, self.sub), "fixture:classm.clcw26.2@clcw_next_year")
        self.assertEqual(R._witness("fixture:classm.clcw26.2@x", self.sub), "fixture:classm.clcw26.2@x")

    def test_load_map(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "m.json"
            p.write_text(json.dumps({"description": ["x"], "renames": {
                "clcw26": {"to": "clcw_next_year", "kind": "document"},
                "rec.not_2024": {"to": "rec.before_prior_year", "kind": "input"}}}))
            self.assertEqual(R.load_map(p), ({"rec.not_2024": "rec.before_prior_year"}, {"clcw26": "clcw_next_year"}))
            p.write_text(json.dumps({"rec.not_2024": "rec.before_prior_year"}))
            self.assertEqual(R.load_map(p), ({"rec.not_2024": "rec.before_prior_year"}, {}))
            p.write_text(json.dumps({"renames": [{"old": "rec.not_2024", "new": "rec.before_prior_year"}]}))
            self.assertEqual(R.load_map(p), ({"rec.not_2024": "rec.before_prior_year"}, {}))


FIXTURE = """{
  "cases": [
    {
      "id": "x2s1o.f8853c.pre1996",
      "description": "names f8853c.pre1996 in prose",
      "evidence_note": "the reviewer saw f8853c[p0].pre1996",
      "inputs": {
        "f8853c[p0].pre1996": true,
        "rec.not_2024": false
      },
      "expect": {"f8853c[p0].line25": {"kind": "refusal", "gate": "f8853c[p0].pre1996_if_reimbursed"}}
    }
  ]
}
"""
DEFAULTS = '{\n  "defaults": [\n    {"input": "f8853c[*].pre1996", "value": false}\n  ]\n}\n'
ROWS = "rows:\n  - id: ltc\n    answers:\n      person[taxpayer].f8853c[c].pre1996: true\n"
PERSONA = "answers:\n  f8853c[p0].pre1996: false\n  rec.not_2024: true\n"


def rulings(witness, text):
    return json.dumps({"kind": "transcription", "form": "f8853c", "rulings": [
        {"printed": "25", "ruling": text, "triage": {"verdict": "differs", "kinds": [], "witnesses": [witness],
                                                       "policy": "p"}}]}, indent=1, ensure_ascii=False) + "\n"


class Tree(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        r = self.root = Path(self.dir.name)
        files = {
            "fixtures/2025/f8853c.json": FIXTURE,
            "fixtures/2025/defaults.json": DEFAULTS,
            "fixtures/ny/2025/it201.json": '{"inputs": {"rec.not_2024": true}}\n',
            "interview/2025/coverage/ltc.yaml": ROWS,
            "interview/2025/personas/01_ltc.yaml": PERSONA,
            "reviews/2025/transcription/f8853c.rulings.json":
                rulings("partial:x2s1o.f8853c.adb-f8853c[p0].pre1996@f8853c[p0]", "the reply reads f8853c.pre1996"),
            "reviews/2025/transcription/f8853c.deepseek.rulings.json":
                rulings("partial:x2s1o.f8853c.adb-f8853c[p0].pre1996@f8853c[p0]", "historical"),
            "forms/2025/f8853c.yaml": "lines:\n  - id: f8853c.pre1996\n",
        }
        for rel, text in files.items():
            (r / rel).parent.mkdir(parents=True, exist_ok=True)
            (r / rel).write_text(text, encoding="utf-8")
        self.files = files

    def tearDown(self):
        self.dir.cleanup()

    def text(self, rel):
        return (self.root / rel).read_text(encoding="utf-8")

    def test_check_apply_check(self):
        found = R.check(MAP, DOCS, root=self.root, ny=False, year=2025)
        where = sorted({p.relative_to(self.root).as_posix() for p, _, _ in found})
        self.assertEqual(where, ["fixtures/2025/defaults.json", "fixtures/2025/f8853c.json",
                                 "interview/2025/coverage/ltc.yaml", "interview/2025/personas/01_ltc.yaml",
                                 "reviews/2025/transcription/f8853c.rulings.json"])
        changed = R.apply(MAP, DOCS, root=self.root, ny=False, year=2025)
        self.assertEqual(len(changed), 5)
        self.assertEqual(R.check(MAP, DOCS, root=self.root, ny=False, year=2025), [])
        fixture = self.text("fixtures/2025/f8853c.json")
        self.assertIn('"f8853c[p0].contract_before_ltc_date": true', fixture)
        self.assertIn('"gate": "f8853c[p0].contract_before_ltc_date_if_reimbursed"', fixture)
        self.assertIn('"rec.before_prior_year": false', fixture)
        for kept in ('"id": "x2s1o.f8853c.pre1996"', "names f8853c.pre1996 in prose", "saw f8853c[p0].pre1996"):
            self.assertIn(kept, fixture)
        self.assertIn("f8853c[*].contract_before_ltc_date", self.text("fixtures/2025/defaults.json"))
        self.assertIn("person[taxpayer].f8853c[c].contract_before_ltc_date: true", self.text("interview/2025/coverage/ltc.yaml"))
        side = json.loads(self.text("reviews/2025/transcription/f8853c.rulings.json"))["rulings"][0]
        self.assertEqual(side["triage"]["witnesses"], ["partial:x2s1o.f8853c.adb-f8853c[p0].contract_before_ltc_date@f8853c[p0]"])
        self.assertEqual(side["ruling"], "the reply reads f8853c.pre1996")
        for rel in ("reviews/2025/transcription/f8853c.deepseek.rulings.json", "forms/2025/f8853c.yaml",
                    "fixtures/ny/2025/it201.json"):
            self.assertEqual(self.text(rel), self.files[rel], rel)
        self.assertEqual(R.apply(MAP, DOCS, root=self.root, ny=False, year=2025), [])

    def test_new_york(self):
        found = R.check(MAP, DOCS, root=self.root, ny=True, year=2025)
        self.assertEqual([(p.name, ids) for p, _, ids in found], [("it201.json", ["rec.not_2024"])])
        R.apply(MAP, DOCS, root=self.root, ny=True, year=2025)
        self.assertEqual(R.check(MAP, DOCS, root=self.root, ny=True, year=2025), [])
        self.assertEqual(self.text("fixtures/2025/f8853c.json"), FIXTURE)

    def test_files_given(self):
        R.apply(MAP, DOCS, [str(self.root / "forms/2025/f8853c.yaml")], root=self.root, ny=False, year=2025)
        self.assertIn("f8853c.contract_before_ltc_date", self.text("forms/2025/f8853c.yaml"))

    def test_moved_document_reported(self):
        (self.root / "fixtures/2025/a.json").write_text('{"a[k].moved_2025": 1}\n', encoding="utf-8")
        R.apply(MAP, DOCS, root=self.root, ny=False, year=2025)
        found = R.check(MAP, DOCS, root=self.root, ny=False, year=2025)
        self.assertEqual([(p.name, ids) for p, _, ids in found], [("a.json", ["a.moved_2025"])])


def main():
    result = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]))
    ok = result.wasSuccessful()
    print(f"rename ids self-test: {'ok' if ok else 'FAILED'} ({result.testsRun} tests)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
