# New York work log

One entry per session on branch `ny/2025-foundation` (brief: `docs/ny/2026-11-04_ny_cloud_brief.md`), newest first.

---

## 2026-11-04 — Phase 3, steps 1 to 8 (cloud session, continued)

**Repository hygiene first.** The repository is public: the owner's own checklist answers, recorded earlier in
`docs/ny/DECISIONS.md` and this log, were removed from the files (commit 0301f3c). They remain in the branch's
history (commits 4b4b161, df4895c, 640f150); removing them from history needs a rewrite and force push, which is the
owner's decision.

**Done and verified** (commits "NY Phase 3.1" to "NY Phase 3.4", each with the federal canonical output
byte-identical to the starting point):
1. The jurisdiction layout in the build (New York documents in the one canonical build, written to files of their
   own) and in the Python tools (`tools/jurisdiction.py`, `--jurisdiction ny`).
2. Parameters (`params/ny/2025.yaml`) and tables: the State and City Tax Tables extracted from the web page and
   checked against the rate schedules (all 7,812 cells explained), the household credit tables.
3. Form IT-201 (`forms/ny/2025/`), with the refusal screens of the decisions; the ambiguity register.
4. The New York interview (`interview/ny/`), asked after the federal questions.

**Done but committed only as work in progress** (the session ran out of budget before the step commits):
5. Fixtures: 135 cases (`fixtures/ny/2025/it201.json`), every value predicted by `tools/ny_predict.py` from the
   archived sources before the encoding ran; the two official tax-table examples as class A. 135/135 pass
   (`test-fixtures --ny`) on the final forms, and every New York branch was taken on the run before the review fixes
   (`coverage --ny` was not rerun after them). The build with the review fixes passed, and the federal canonical
   output stayed byte-identical. **Not finished:** the build that walks the New York interview over the final
   fixtures was stopped unfinished; the previous walk failed only because the joint-return paths need more than 200
   questions, now raised to 600 for New York.
6. PolicyEngine-US differential: 442 line comparisons, every difference with a stated cause, two of them the open
   item on recapture worksheet selection (`reports/ny/2025/engine_differential.md`). **Not done:** the Lean change is
   written but untested (no toolchain here); OpenTaxSolver needs a manual download; mutation (`mutate --ny`, code
   written) was not run.
7. Three independent in-session reviews; every medium-or-higher finding ruled and each defect fixed with a fixture
   (`research/audits/ny/2025-phase3-review.md`).
8. `PROJECT_INDEX.md` and `docs/ny/INTEGRATION.md` written. **Not done:** the values sheet (`render`, and the CLI
   values sheet for one synthetic case).

**Next session:** rerun `node engine/dist/main.js build` (the New York interview walk), `coverage --ny` and
`mutate --ny`; render the values sheet; then make the step commits 3.5 to 3.8 and push. Then Phase 4 on the owner's
machine (`docs/ny/INTEGRATION.md`).

**Cost:** this session's cost was not shown. Subagents: one Phase 2 verification and three Phase 3 reviews (logged in
`research/costs/agent_runs.jsonl`). No paid review call.

---

## 2026-11-04 — Phases 1 and 2 (cloud session)

**Environment.** The environment allowed `tax.ny.gov`, which redirects every document to `www.tax.ny.gov`; the owner
approved adding `www.tax.ny.gov` to the environment's allowed hosts at the start of the session.

**Phase 1, the source archive** (commit "NY Phase 1: tax-year 2025 source archive"):
- `tools/fetch_sources.py --jurisdiction ny`: catalog `tools/sources-ny-<year>.json`, archive `sources/ny/<year>/`,
  host `www.tax.ny.gov` only, under `/pdf/`, `/forms/` or `/pit/file/tax-tables/`, no query string; same layout,
  hashes and derived text as the federal archive; the self-test covers both jurisdictions' address rules. The federal
  archive still verifies (158 documents).
- `tools/check_extraction.py --jurisdiction ny` (report `reports/ny/2025/extraction.md`).
- Archived the final 2025 editions: IT-201, IT-201-I and its web edition, the State and City tax tables (web only),
  IT-201-ATT, IT-2, IT-270-I. Editions and dates in `sources/ny/2025/README.md` and the manifest.
- Extraction: 0 failing checks; six IT-201-I pages excepted against the web edition with reasons (a sample-check
  image, a running heading). PDFKit (macOS) and the OCR audit were not run here.
- Findings: the PDF text layers carry the filing-status digits ① to ⑤ as private-use characters; the tables of 11
  IT-201-I pages are unreliable in reading order and must be read from the web edition; the corrections page lists no
  year after 2023; the web edition is dated July 27, 2026 and has the same set of numbers as the PDF.

**Phase 2, the premise map and decisions** (commits "NY Phase 2: draft premise map ..." and "NY Phase 2: premise map,
verification and decision batch"):
- `research/premises/ny-it201-nyc-resident.md`: every IT-201 line in order, the tax computation (tax tables, rate
  schedules, the 16 recapture worksheets, the City tax), the household and school tax credits, refusal screens, the
  owner checklist, open items. Its quotes were checked by a script against the archive.
- `research/premises/ny-it201-nyc-resident.verification.md`: an independent subagent's verification: 14 errors (1
  medium: line 20's bond-purchase rule; 13 low: three wrong pages, a section cross-reference, unmarked inferences,
  incomplete screen wording), 8 omissions (1 medium: the line 77 to 80 arithmetic), no number in any table wrong, all
  27 federal ids present, every IT-201 line 1 to 84 and item A to H present in order. Its findings that bear on the
  owner's questions are folded into DECISIONS.md.
- `docs/ny/DECISIONS.md`: the owner's questions (profile checklist A1 to A13, scope choices B1 to B11, design C1 to
  C8) and the points settled by the source (Part D).

**Not done, by the brief:** no New York form, parameter, table, interview or fixture was authored (Phase 3 waits for the
decisions). No paid model call was made; the review tools under `tools/transcription/` were not run. `check-all` was
not run (commits use `--no-verify`, approved for this branch); `tools/citations.py --strict` reported 0 findings
before each commit (it does not read the New York archive yet: C1, C8).

**After Phase 2, same session:** the owner answered the checklist (Part A; the answers are not recorded, the
repository being public) and accepted every suggestion in Parts B and C (recorded at the end of
`docs/ny/DECISIONS.md`); spec 2.3 now records the branch's exception (C7).

**Next:** Phase 3 (a new section of the brief): the archive layout and
tool coverage (C1, C8), the New York forms, parameters and tables (tax tables extracted from the web page), interview
questions and fixtures (the two official tax-table examples first).

**Cost:** this session's cost was not shown in the session. One verification subagent was run (252,405 subagent tokens, 53 tool uses, about 8 minutes; logged in
`research/costs/agent_runs.jsonl`, dollar cost not reported); no paid review calls (`.transcription/costs.jsonl` unchanged).
