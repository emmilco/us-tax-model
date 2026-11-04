# New York work log

One entry per session on branch `ny/2025-foundation` (brief: `docs/ny/2026-11-04_ny_cloud_brief.md`), newest first.

---

## 2026-11-04 — Phases 1 and 2 (cloud session)

Session: https://claude.ai/code/session_01STA2Jxb5LuWnA1Q6LPZzfH

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

**Next:** the owner answers `docs/ny/DECISIONS.md`; then Phase 3 (a new section of the brief): the archive layout and
tool coverage (C1, C8), the New York forms, parameters and tables (tax tables extracted from the web page), interview
questions and fixtures (the two official tax-table examples first).

**Cost:** this session's cost was not shown in the session. One verification subagent was run (252,405 subagent tokens, 53 tool uses, about 8 minutes; logged in
`research/costs/agent_runs.jsonl`, dollar cost not reported); no paid review calls (`.transcription/costs.jsonl` unchanged).
