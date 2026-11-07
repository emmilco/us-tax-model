#!/usr/bin/env python3
"""Offline tests of the review tools' New York mode (`--jurisdiction ny`) and of their federal default.

The jurisdiction is read from the command line when tools/jurisdiction.py is imported, so the New York
cases run each tool, or a short script importing it, in a child process. No model is called: the prompts
are built as --dry-run builds them. Needs the canonical build and the New York rendering
(`node engine/dist/main.js build`, `render --ny`), as check-all runs them first.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import jurisdiction  # noqa: E402
import pending  # noqa: E402
import transcribe as T  # noqa: E402

NY_DOCS = ("ny_city_rs", "ny_it2", "ny_it201", "ny_rs", "ny_tcw", "ny_tcw_first")


def run_ny(code, env=None):
    """Run `code` in a child Python with --jurisdiction ny on its command line; returns its stdout as JSON."""
    prelude = f"import sys; sys.path[:0] = [{str(HERE)!r}, {str(HERE.parent)!r}]\n"
    r = subprocess.run([sys.executable, "-c", prelude + code, "--jurisdiction", "ny"], cwd=ROOT,
                       capture_output=True, text=True, env={**os.environ, **(env or {})})
    if r.returncode != 0:
        raise AssertionError(r.stderr[-2000:])
    return json.loads(r.stdout)


class FederalDefault(unittest.TestCase):
    """Without the flag every path, list and wording is the federal one."""

    def test_paths_and_wording(self):
        self.assertFalse(jurisdiction.NY)
        self.assertEqual(T.SOURCES, str(ROOT / "sources" / T.Y))
        self.assertEqual(T.FORMS, str(ROOT / "forms" / T.Y))
        self.assertEqual(T.LOGS, str(ROOT / "reviews" / T.Y / "transcription"))
        self.assertEqual(jurisdiction.preface("x"), "x")
        self.assertEqual(jurisdiction.system("y"), "y")
        self.assertEqual(T.TRANSCRIBE_SYSTEM[:30], "You transcribe IRS worksheets ")

    def test_documents_are_the_federal_ones(self):
        names = [f for f, _ in T.form_files()]
        self.assertEqual(names, sorted(os.listdir(T.FORMS)))
        self.assertFalse(any(n.startswith("ny_") for n in names))
        fed = json.load(open(ROOT / "sources" / T.Y / "manifest.json"))["documents"]
        self.assertEqual(T.manifest(), {d["id"]: d for d in fed})
        self.assertFalse(any(k.startswith("ny.") for k in (T.year_params()["params"])["values"]))

    def test_no_pending_federal_review(self):
        self.assertEqual(pending.load(), {})
        self.assertFalse(os.path.exists(pending.PATH))

    def test_federal_render_has_no_new_york_document(self):
        rendered = ROOT / "rendered" / T.Y
        self.assertFalse([p.name for p in rendered.glob("ny_*")])
        self.assertNotIn("`ny.", (rendered / "params.md").read_text())
        self.assertNotIn("amb.ny.", (rendered / "ambiguities.md").read_text())


class NewYorkMode(unittest.TestCase):

    def test_paths(self):
        got = run_ny("import json, transcribe as T, render_compare as R, classm as M, completeness_review as C, "
                     "screen_review as S, rulings\n"
                     "print(json.dumps([T.SOURCES, T.FORMS, T.LOGS, R.RENDERED, R.LOGS, M.LOGS, M.fixture_path(), C.OUT, S.OUT, "
                     "S.RAW, rulings.REVIEWS]))")
        y = T.Y
        want = [ROOT / "sources/ny" / y, ROOT / "forms/ny" / y, ROOT / "reviews/ny" / y / "transcription",
                ROOT / "rendered/ny" / y, ROOT / "reviews/ny" / y / "render", ROOT / "reviews/ny" / y / "classm",
                ROOT / "fixtures/ny" / y / "classm.json", ROOT / "reviews/ny" / y / "completeness",
                ROOT / "reviews/ny" / y / "screens", ROOT / ".transcription/ny/screens", ROOT / "reviews/ny" / y]
        self.assertEqual(got, [str(p) for p in want])

    def test_documents_read_across_both_trees(self):
        got = run_ny("import json, transcribe as T\n"
                     "m = T.manifest(); names = [f for f, _ in T.form_files()]\n"
                     "print(json.dumps({'ny_doc': 'ny_it201i' in m, 'fed_doc': 'f1040' in m, 'ny_form': 'ny_it201.yaml' in names,"
                     " 'fed_form': 'f1040.yaml' in names, 'f1040': T.load_form('f1040')['id'], 'it201': T.load_form('ny_it201')['id'],"
                     " 'ny_dir': T.source_dir('ny_it201i'), 'fed_dir': T.source_dir('f1040'),"
                     " 'ny_param': any(k.startswith('ny.') for k in T.year_params()['params']['values'])}))")
        self.assertEqual(got, {"ny_doc": True, "fed_doc": True, "ny_form": True, "fed_form": True, "f1040": "f1040",
                               "it201": "ny_it201", "ny_dir": str(ROOT / "sources/ny" / T.Y),
                               "fed_dir": str(ROOT / "sources" / T.Y), "ny_param": True})

    def test_transcription_prompts_carry_new_york_pages_and_federal_interfaces(self):
        """Each New York document's request opens with the jurisdiction note, cites only New York pages, lists only
        New York parameters, and carries every interface its review requires except the federal lines its encoding
        reads that the New York text does not name (by form and line or by printed label): those are reported as
        missing, review evidence, not supplied from the encoding."""
        got = run_ny("import json, transcribe as T, input_context\n"
                     "out = {}\n"
                     f"for fid in {list(NY_DOCS)!r}:\n"
                     "    doc = T.load_form(fid); mani = T.manifest()\n"
                     "    excerpt, used = T.excerpt_for(doc, mani)\n"
                     "    selected = T.catalog_selection(doc, excerpt, used, mani)\n"
                     "    values = T.year_params()['params']['values']\n"
                     "    params = {k: v['value'] for k, v in values.items() if k.startswith('ny.')}\n"
                     "    prompt = T.build_prompt(doc, excerpt, params, T.catalog_lines(fid, selected), {k: v['type'] for k, v in values.items()},"
                     " T.collection_notes(fid, selected))\n"
                     "    check = input_context.assess(doc, [], T.model_type_context(), prompt)\n"
                     "    fed = sorted({r['doc'] for r in check['required'] if not r['doc'].startswith('ny_')})\n"
                     "    out[fid] = {'note': prompt.startswith(T.jurisdiction.NY_NOTE), 'docs': sorted({u['doc'] for u in used}),"
                     " 'state': check['state'], 'missing': check['missing'], 'federal': fed,"
                     " 'note_after': T.NY_CATALOG_NOTE in prompt}\n"
                     "print(json.dumps(out))")
        for fid, r in got.items():
            self.assertTrue(r["note"] and r["note_after"], fid)
            self.assertTrue(r["docs"] and all(d.startswith("ny_") for d in r["docs"]), (fid, r["docs"]))
            if fid != "ny_it201":
                self.assertEqual((r["state"], r["missing"]), ("pass", []), fid)
        self.assertIn("f1040", got["ny_it201"]["federal"])
        self.assertIn("s1", got["ny_it201"]["federal"])
        # Federal helper lines the encoding reads, which no source text can name: review evidence.
        self.assertEqual(got["ny_it201"]["missing"], ["dependent:dependent.claimed", "dependent:dependent.one",
                                                      "dependent:dependent.under_ctc_age", "eic:eic.limit",
                                                      "f2441:f2441.benefits", "f2441:f2441.care", "person:person.one",
                                                      "person:person.sc_count", "person:person.sc_total"])

    def test_render_prompt_reads_the_new_york_rendering(self):
        got = run_ny("import json, render_compare as R\n"
                     "doc = R.load_form('ny_it201')\n"
                     "excerpt, used = R.excerpt_for(R.source_context(doc), R.manifest())\n"
                     "prompt = R.build_prompt(doc, excerpt)\n"
                     "print(json.dumps({'note': prompt.startswith(R.jurisdiction.NY_NOTE), 'path': R.rendered_path('ny_it201'),"
                     " 'fed_path': R.rendered_path('f1040'), 'docs': sorted({u['doc'] for u in used}),"
                     " 'federal_named': 'f1040 line 1z' in prompt}))")
        self.assertTrue(got["note"])
        self.assertEqual(got["path"], str(ROOT / "rendered/ny" / T.Y / "ny_it201.md"))
        self.assertEqual(got["fed_path"], str(ROOT / "rendered" / T.Y / "f1040.md"))
        self.assertIn("ny_it201i", got["docs"])
        self.assertTrue(got["federal_named"])

    def test_completeness_and_screens_cover_new_york_documents_only(self):
        got = run_ny("import json, completeness_review as C, screen_review as S\n"
                     "forms = C.load_forms(); every = C.context_forms()\n"
                     "lines = S.load_lines()\n"
                     "print(json.dumps({'forms': sorted(f['id'] for f in forms), 'context_federal': any(f['id'] == 'f1040' for f in every),"
                     " 'form_docs': [C.is_form_doc(d) for d in ('ny_it201', 'ny_it2', 'ny_it201i', 'ny_it201i-html', 'ny_it270i')],"
                     " 'screens': sorted(S.screens(lines))}))")
        self.assertEqual(got["forms"], sorted(NY_DOCS))
        self.assertTrue(got["context_federal"])
        self.assertEqual(got["form_docs"], [True, True, False, False, False])
        # The New York screens are the Yes/No questions whose Yes refuses; each is a gated input (asked only when a
        # computed amount makes it matter), and a gated screen is still a screen.
        self.assertEqual(got["screens"], ["ny_it201.ask.dependent_care", "ny_it201.ask.gov_pension", "ny_it201.ask.mctmt",
                                          "ny_it201.ask.pension_exclusion", "ny_it201.ask.refund_529",
                                          "ny_it201.ask.us_obligation_interest"])


class WebEditionSections(unittest.TestCase):
    """The IT-201-I web edition, archived as one page, is given by the sections its locators name
    (html_sections.py), with the headings above them; a locator naming no heading gives the whole page."""

    @classmethod
    def setUpClass(cls):
        import html_sections as H
        cls.H = H
        cls.src = ROOT / "sources/ny" / T.Y
        cls.entry = {d["id"]: d for d in json.load(open(cls.src / "manifest.json"))["documents"]}["ny_it201i-html"]
        cls.text = (cls.src / cls.entry["text_file"]).read_text(encoding="utf-8")
        cls.secs = H.load(cls.src, cls.entry, cls.text)

    def cut(self, *locators):
        return self.H.cut(self.src, self.entry, self.text, set(locators))

    def test_headings_rederive_the_archived_text(self):
        self.assertIsNotNone(self.secs)
        self.assertIsNone(self.H.outline("<html><h2>A</h2><p>b</p></html>", "A\nc\n"))
        self.assertEqual(self.H.outline("<html><h2>A</h2><p>b</p><h3>C</h3><p>d</p></html>", "A\nb\nC\nd\n"),
                         [(2, "A", 0), (3, "C", 2)])

    def test_a_worksheet_and_its_filing_status(self):
        text, titles, _ = self.cut('Tax computation worksheet 1, "8. Multiply line 5 by line 7"')
        self.assertEqual(titles, ["Tax computation worksheet 1"])     # not worksheets 10 to 16
        self.assertIn("then you must calculate your tax using this worksheet", text)
        self.assertNotIn("Tax computation worksheet 2", text)
        self.assertIn("Married filing jointly and qualifying surviving spouse", text)   # the heading above it
        self.assertIn("Find your New York State tax by using the correct tax computation worksheet", text)

    def test_a_quote_outside_the_section_widens_it(self):
        _, titles, _ = self.cut('New York State household credit table 2, "Note 3", '
                                '"For each individual over 7, add the amount in this column to the column 7 amount."')
        self.assertEqual(titles, ["Line 40: New York State household credit"])

    def test_segments_are_cut_one_by_one(self):
        self.assertEqual(self.H.segments('A, "x; y"; B, "z"'), ['A, "x; y"', 'B, "z"'])
        _, titles, _ = self.cut('Tax computation worksheet 1, "3. Multiply line 2 by 5.5% (0.055)"; '
                                'Tax computation worksheet 7, "3. Multiply line 2 by 6% (0.06)"')
        self.assertEqual(titles, ["Tax computation worksheet 1", "Tax computation worksheet 7"])

    def test_no_heading_gives_the_whole_page(self):
        self.assertIsNone(self.cut('p. 12, "New York State tax"'))
        self.assertIsNone(self.cut('Tax computation worksheet 1, "a phrase printed nowhere"'))

    def test_every_new_york_locator_is_cut_and_keeps_its_quotes(self):
        """Every locator of the New York documents and parameters names a heading, and its sections carry every
        phrase it quotes: nothing a citation points at is left out."""
        import re
        import yaml
        locs = set()
        def walk(x):
            if isinstance(x, dict):
                if x.get("doc") == "ny_it201i-html":
                    locs.add(x["locator"])
                for v in x.values():
                    walk(v)
            elif isinstance(x, list):
                for v in x:
                    walk(v)
        for path in [*(ROOT / "forms/ny" / T.Y).glob("*.yaml"), ROOT / "params/ny" / f"{T.Y}.yaml"]:
            walk(yaml.safe_load(path.read_text(encoding="utf-8")))
        self.assertGreater(len(locs), 100)
        for loc in sorted(locs):
            got = self.cut(loc)
            self.assertIsNotNone(got, loc)
            flat = " ".join(got[0].replace("|", " ").split())
            for q in re.findall(r'"([^"]+)"', loc):
                self.assertIn(" ".join(q.split()), flat, loc)

    def test_new_york_requests_use_the_sections(self):
        got = run_ny("import json, transcribe as T\n"
                     "mani = T.manifest(); out = {}\n"
                     f"for fid in {list(NY_DOCS)!r}:\n"
                     "    excerpt, used = T.excerpt_for(T.load_form(fid), mani)\n"
                     "    out[fid] = [[u['doc'], u['how'][:15], len(excerpt)] for u in used if u['doc'] == 'ny_it201i-html']\n"
                     "print(json.dumps(out))")
        whole = len(self.text)
        for fid, rows in got.items():
            for doc, how, size in rows:
                self.assertEqual(how, "cited sections:", fid)
        for fid in ("ny_rs", "ny_city_rs", "ny_tcw", "ny_tcw_first"):
            self.assertTrue(got[fid] and got[fid][0][2] < whole / 5, (fid, got[fid]))


class NewYorkFederalCatalog(unittest.TestCase):
    """A New York catalog stays source-selected: of the federal return it lists the lines the New York text names,
    by form and line or by printed label (whole where a line of the document cites the federal form's pages);
    nothing is taken from the encoding."""

    def test_federal_catalog(self):
        got = run_ny("import json, transcribe as T\n"
                     "mani = T.manifest(); out = {}; every = T.load_all_lines()\n"
                     f"for fid in {list(NY_DOCS)!r}:\n"
                     "    doc = T.load_form(fid)\n"
                     "    excerpt, used = T.excerpt_for(doc, mani)\n"
                     "    sel = T.catalog_selection(doc, excerpt, used, mani)\n"
                     "    lines = T.catalog_lines(fid, sel)\n"
                     "    coll = T.collection_notes(fid, sel)\n"
                     "    out[fid] = {'fed': {d: r for d, r in sel.items() if not d.startswith('ny_')},"
                     " 'listed': sorted([k for k in lines if not every[k][0].startswith('ny_')]"
                     " + [i for i in every if not every[i][0].startswith('ny_') and f'{i} (form ' in coll]),"
                     " 'notes': T.ny_catalog_notes(doc)}\n"
                     "doc = T.load_form('ny_it2'); doc = {**doc, 'lines': [{**doc['lines'][0], 'cite': {'doc': 'f1040', 'locator': 'p. 1'}}] + doc['lines'][1:]}\n"
                     "ex, used = T.excerpt_for(doc, mani)\n"
                     "out['stated'] = T.catalog_selection(doc, ex, used, mani).get('f1040')\n"
                     "print(json.dumps(out))")
        it201, stated = got.pop("ny_it201"), got.pop("stated")
        self.assertTrue(all(r.startswith(T.NAMED_LINES) for r in it201["fed"].values()))
        # The federal lines the New York text names (by form and line: 1z, 2a, 2b, 3b, 7a, and the Schedule 1 and Schedule C
        # lines the cited IT-216-I page names; the rest by label).
        self.assertEqual(it201["listed"], sorted([
            "f1040.line11a", "f1040.line15", "f1040.line1z", "f1040.line27a", "f1040.line2a", "f1040.line2b",
            "f1040.line3b", "f1040.line4b", "f1040.line5b", "f1040.line6b", "f1040.line7a", "f1040.status",
            "person.sep_s3", "s1.line1", "s1.line15", "s1.line26", "s1.line2a", "s1.line3", "s1.line7", "s1.line9", "s2.line4",
            "sc.f7206_line3", "sc.line3"]))
        for fid, r in got.items():
            self.assertTrue(r["notes"].strip().startswith("In this New York request"), fid)
            if fid != "ny_it2":
                self.assertEqual((r["fed"], r["listed"]), ({}, []), fid)
        self.assertNotIn("Federal lines this New York document reads", it201["notes"])
        self.assertIsNotNone(stated)                        # a federal document a line cites: listed whole
        self.assertFalse(stated.startswith(T.NAMED_LINES))

    def test_label_matching_rule(self):
        got = run_ny("import json, transcribe as T\n"
                     "mani = T.manifest()\n"
                     "f = lambda t: sorted(i for v in T.federal_labelled(t, mani).values() for i in v)\n"
                     "print(json.dumps({\n"
                     " 'federal': f('Enter your federal adjusted gross income here.'),\n"
                     " 'new_york': f('Enter your federal return amounts. Your New York adjusted gross income is line 33.'),\n"
                     " 'no_passage': f('Your adjusted gross income from line 33.'),\n"
                     " 'form_only': f('Do not send federal Form W-2. Total payments: add lines 63 to 75.'),\n"
                     " 'longer': f('From your federal return: taxable amount of IRA distributions.'),\n"
                     " 'acronym': f('Did you claim the federal earned income credit?'),\n"
                     " 'phrases': sorted(T.label_phrases('IRA distributions, taxable amount', T.label_norm('4a IRA distributions b Taxable amount'))),\n"
                     "}))")
        self.assertEqual(got["federal"], ["f1040.line11a"])
        self.assertEqual(got["new_york"], [])          # qualified as New York's
        self.assertEqual(got["no_passage"], [])        # no federal form named or implied before it
        self.assertEqual(got["form_only"], [])         # "federal Form W-2" names W-2, not the return
        self.assertEqual(got["longer"], ["f1040.line4b"])   # not 4a, whose phrase lies inside it
        self.assertEqual(got["acronym"], ["f1040.line27a"])
        self.assertEqual(got["phrases"], [" ira distributions taxable amount ", " taxable amount of ira distributions "])

    def test_federal_requests_carry_no_new_york_note(self):
        self.assertEqual(T.ny_catalog_notes(T.load_form("f1040")), "")


class PendingReviews(unittest.TestCase):
    """A New York document whose first review is pending is reported, not failed; once its review exists,
    the listing itself fails until it is removed."""

    def check_logs(self, listing):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, "pending.json")
            path.write_text(json.dumps(listing))
            reviews = Path(tmp, "reviews")  # an empty New York review tree, whatever reviews the repository holds
            for kind in ("transcription", "render", "classm"):
                (reviews / kind).mkdir(parents=True)
            return subprocess.run([sys.executable, str(HERE / "check_logs.py"), "--jurisdiction", "ny"], cwd=ROOT,
                                  capture_output=True, text=True,
                                  env={**os.environ, "REVIEW_PENDING_FILE": str(path), "NY_REVIEWS_ROOT": str(reviews)})

    def test_pending_reported_missing_failed(self):
        everything = {k: list(NY_DOCS) for k in ("transcription", "render", "classm")}
        ok = self.check_logs(everything)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertIn("ny_it201: pending, no review yet", ok.stdout)
        short = {**everything, "render": [d for d in NY_DOCS if d != "ny_it2"]}
        bad = self.check_logs(short)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("render logs [claude]: 0/6 forms logged; missing: ny_it2", bad.stdout)

    def test_reviewed_but_still_listed_fails(self):
        got = run_ny("import json, tempfile, pathlib, check_completeness as K\n"
                     "tmp = pathlib.Path(tempfile.mkdtemp())\n"
                     "(tmp / 'completeness.json').write_text(json.dumps([{'form': 'ny_it2', 'prompt_sha': 'x', 'claims': []}]))\n"
                     "(tmp / 'pending.json').write_text(json.dumps({'completeness': ['ny_it2']}))\n"
                     "K.RECORD = tmp / 'completeness.json'; K.RULINGS = tmp / 'rulings.json'; K.REPORT = tmp / 'report.md'\n"
                     "K.pending.PATH = str(tmp / 'pending.json')\n"
                     "import contextlib, io\n"
                     "buf = io.StringIO()\n"
                     "with contextlib.redirect_stdout(buf):\n"
                     "    status = K.check()\n"
                     "print(json.dumps({'status': status, 'out': buf.getvalue()}))")
        self.assertEqual(got["status"], 1)
        self.assertIn("ny_it2: reviewed but still listed as pending", got["out"])

    def test_unknown_kind_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, "pending.json")
            path.write_text(json.dumps({"transcriptions": []}))
            with self.assertRaises(SystemExit):
                pending.load(str(path))


if __name__ == "__main__":
    unittest.main(verbosity=2)
