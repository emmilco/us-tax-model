# Tax year 2026 adoption plan (for the owner's machine)

Written 2026-11-04 on branch `ty2026/prep` (`docs/ty2026/2026-11-04_ty2026_cloud_brief.md`, steps 1 to 6). The
adoption itself (TASKS.md T-011) runs when the IRS publishes the final 2026 documents, expected December 2026 to
January 2027. Everything prepared here is a proposal: `main`, `years.json` (`[2025]`) and the 2025 encoding are
unchanged.

## What is ready

| Step | Output | State |
|---|---|---|
| 1 | `sources/2026/` (91 documents, 55 IRS drafts), `tools/sources-2026.json`, `reports/2026/archive_refresh_2026-11-04.md` | archive verified (`python3 tools/fetch_sources.py --year 2026`) |
| 2 | `reports/2026/year_diff_from_2025.{md,html}`; `reports/2026/worklist_split.md` and `research/ty2026/worklist.json` (`research/ty2026/split_worklist.py`) | 2,236 worklist items: 426 of kind (a), 1,810 of kind (b) |
| 3 | `research/ty2026/changes.md` (133 entries) and `changes.verification.md` (2 high, 11 medium, 7 low; all applied) | 674 quotes checked by `research/ty2026/check_quotes.py` |
| 4 | `research/ty2026/params-2026.proposed.yaml` (`build_params.py`, `check_params.py`) | 92 values from final sources, 70 from drafts, 109 with no 2026 source |
| 5 | `research/ty2026/forms-proposed/` (Form 1040, Schedule A, Form W-2, new Schedule 3-A; README) and `research/ty2026/fixtures-proposed/2026-predicted.json` (16 cases) | structural build test passed in a scratch copy; not wired in |

## Order of work when the final documents publish

1. **Refetch the finals.** For every row of `tools/sources-2026.json` with `"draft": true`, replace the URL with the
   final (`irs.gov/pub/irs-pdf/<name>.pdf`), drop the draft fields, delete the draft's manifest entry and files, and
   run `python3 tools/fetch_sources.py --year 2026 --fetch` and `--derive`. Add the documents still missing
   (below). Recheck the 13 continuous-use revisions (`archive_refresh_2026-11-04.md` section 5) for a newer revision.
   Archive Notice 2026-5 (HSA eligibility, cited by i8889) and the final Schedule 3-A and Form 1062 instructions if
   posted. `fetch_sources.py --year 2026` must report no drafts before step 9.
2. **Rerun the year diff** against the finals: `python3 tools/year_diff.py --from 2025 --to 2026`, then
   `python3 research/ty2026/split_worklist.py`. Kind (b) items whose document has now posted become kind (a); read
   each one the way `changes.md` was written.
3. **Verify every draft-sourced item against the final** (the list below): the change map entries, the 70 draft
   parameters, the proposed definitions and the draft-sourced fixture cases. Run
   `python3 research/ty2026/check_quotes.py` and `python3 research/ty2026/check_params.py` after refetching: a quote
   that is no longer printed on its page is the first sign a draft changed. Then fill the 109 parameters with no
   source from the final instructions (`build_params.py`, the `V` table).
4. **Adopt the definitions**: `python3 tools/year_diff.py --from 2025 --to 2026 --adopt` (copies the 2025 definitions
   and rulings to 2026 and relocates pages); then apply the proposed parameters
   (`params-2026.proposed.yaml` → `params/2026.yaml`, in the `params/2025.yaml` format: drop `source`, `note`,
   `unsourced`) and the proposed definitions (`research/ty2026/forms-proposed/*.diff`, then the other sections of the
   change map in the order of the next section). Work the citation check (`tools/citations.py --strict --year 2026`)
   and `reports/2026/relocation_from_2025.md` until `node engine/dist/main.js build --year 2026` passes.
5. **New inputs and their ripple** (fixtures, interview bank and profiles, `engine/src/generate.ts`,
   `tools/engines/generate_cases.py`, `tools/transcription/input_contracts/`), one owner per input
   (`handoffs/HANDOFF-HARDENING-1.md`).
6. **Fixtures**: `python3 tools/fixtures_year.py --from 2025 --to 2026` (spec 6.7); add the cases of
   `fixtures-proposed/2026-predicted.json` as full fixtures (every input answered), each re-checked against the final.
   The 2026 tables (Tax Table, EIC tables, Form 8962 tables, Pub. 946 tables, auto limits, `ltc_limit`,
   `simple_catchup`, `savers_rate`, `dc_rate`) need re-extraction from the finals.
7. **Reviews of changed forms only** (CLAUDE.md, inference cost): transcription, render and class M for the forms whose
   content changed; completeness and screen reviews for those forms; adjudicate only those. Make the completeness
   prompt year-aware first (T-230).
8. **`years.json`**: add 2026 only when every 2026 source is final and the 2026 build and fixtures pass.
9. **check-all** on the owner's machine (`tools/check_all.sh --year 2026`), then commit with the hook.

## Definition changes in the order to do them (from `changes.md`)

Priority forms first (proposals drafted in `forms-proposed/`): C-PRI-01 to -08 (Form 1040: line 12f, 13a/13b, 24a–24c
and Form 1062, 32a–32c and Schedule 3-A, the ACTC box), C-PRI-13 to -18 (Schedule A: SALT amounts, line 8d, the
charitable worksheet and the 0.5% floor, casualty losses, gambling at 90%, the 2/37 limitation), C-PRI-22 to -24
(HSA eligibility and qualified expenses help text; Form W-2 codes TP, TT, TA and box 14b). Then: Schedule 1-A
renumbering and per-employer tips and overtime (C-SCHED-01 to -05); Schedule 2 renumbering and the Form 5329, 8959 and
8960 destinations (C-SCHED-10, -11, -13, -18; C-PEOP-03); Forms 8995 and 8995-A, the $400 minimum and the taxable
income definition (C-SCHED-31 to -33); Form 8960's section 68 worksheet (C-SCHED-27, -28); Schedule 3 line 5b and the
Schedule 8812 Credit Limit Worksheets (C-SCHED-12, -23; C-CRED-04, -05); Form 5695 carryforward only (C-CRED-01 to
-09); Form 2441 rates, lines and the exclusion (C-CRED-10 to -12); the education credits' SSN rule and Form 8863 line
references (C-CRED-17, -18; C-PEOP-16); Form 8962 without the repayment limitation, with no credit above 400%, and without plans enrolled in during an
income-based special enrollment period (C-PEOP-12, -14, -15, -27); Schedule 3 line 13e (Form 1062; C-SCHED-39); Form 5329 exception 24 (C-PEOP-05; enum `early_exception` gains `e24`); Form 1099-R boxes 7a
to 7d and Trump accounts (C-PEOP-04, -11); the mileage rate split (C-BUS-01); Schedule C line 16 (C-BUS-02); meals
(C-BUS-04); the home office storage rule (C-BUS-06); Form 4562 line 14 and bonus rates (C-BUS-11, -12); the
remaining wording-only entries last.

## Items that must be re-verified against the final documents

- **Change map**: every entry whose 2026 bullet is marked "(draft)" (most of the 133; the final-sourced entries are
  those resting on the final Schedule C, Schedule SE and its instructions, Form 4952, Form 1095-A, the 1099-R and W-2
  instructions, Rev. Procs. 2025-32, 2025-19, 2025-25 and 2026-15, Notices 2025-67 and 2026-10, IRB 2026-29 and
  Public Law 119-21). The corrections in `changes.verification.md` apply first.
- **Parameters**: the 70 with `source: draft` in `params-2026.proposed.yaml` (from Schedules 1-A, 8812, A, D, Forms
  8863, 2441, 8959, 8995, 8880, 5329, 8962, 8889 and the instructions for 8889, 1040-SC, 8606, 2441, 8960, 1116, 1095-A,
  5329, and Pub. 590-B). Also the Tax Computation Worksheet rows taken from the rate tables (confirm against the
  worksheet), the EIC limits taken from Rev. Proc. 2025-32 (confirm against the Form 1040 instructions' EIC steps), and
  `qbi.threshold`, whose married-filing-separately amount ($201,775) is $25 above the single amount in the draft and
  in Rev. Proc. 2025-32 (C-SCHED-30; confirmed by the final Rev. Proc. p. 22, so not a draft error). The dependent
  care exclusion: the final W-2 instructions (p. 19) still print "$5,000 exclusion" against the Form 2441 draft's
  $7,500 (C-CRED-11).
- **Proposed definitions**: all of `forms-proposed/` (Form 1040 and Schedule 3-A rest on drafts; Schedule A on a
  draft and the statute; the W-2 codes on the final instructions).
- **Fixtures**: every case of `2026-predicted.json` labelled draft.

## Documents still missing (on 2026-11-04)

The 2026 Instructions for Form 1040 (`i1040gi`: 937 kind (b) items and 60 parameters wait on it), Schedule A
(`i1040sca`), Schedule D (`i1040sd`), Form 8949, Form 8995-A, Form 4562, Form 8582, Schedule K-1 (Form 1065), Form
8962; Publications 334, 463, 501, 502, 504, 525, 526, 527, 550, 560, 561, 587, 590-A, 925, 946, 969, 970, 974; the HTML
editions of the instructions; final regulations on car loan interest (`fr-2025-24154` was proposed); 2026 guidance on
overtime methods (the 2025 `n-25-69`); the U.S. Code 2025 edition (not on GovInfo on 2026-11-04). Full list:
`reports/2026/archive_refresh_2026-11-04.md` section 7.

## Questions for the owner

1. **Mileage rate in half cents** (C-BUS-01): the 2026 business rate is 72.5 cents before July 1 and 76 cents from July
   1. `sc.mileage_rate` is whole cents. Options: a rate type (cents per mile as a fraction), or refuse mixed-period
   mileage. Which?
2. **Charitable gifts until the Schedule A instructions post** (C-PRI-15): the proposal refuses every itemizer with
   gifts to charity, because the 0.5% floor worksheet is not published. Acceptable as an interim, or should the floor
   be encoded from the statute (final) with an ambiguity entry?
3. **Schedule 3-A** (C-PRI-05): encode it in full (two new questions, one of which, "qualified alien", needs the
   instructions), or refuse Schedule 3-A cases until its instructions post?
4. **Kinds of the change map**: the PEOP section used "wording only (provisional)" for 33 items whose only source has
   no 2026 edition; keep that label, or fold them into kind (b)?
5. **Scope of new 2026 provisions**: Trump accounts (Form 1099-R box 7c, Form 5329 Parts X–XI, W-2 code TA), Form
   1062, the non-itemizer charitable deduction: refuse (as proposed) or plan coverage?
6. **Public Law 119-21, the rest of it**: the verification found one 2026 rule (section 71304) that no 2026 IRS
   draft carried yet. Should the adoption include a full read of every section of Public Law 119-21 effective for 2026
   against the encoded forms (the tax provisions of its 332 archived pages, best read by one agent with the change map in hand)?
7. **Agent use**: step 3 used five Opus agents (logged in `research/costs/agent_runs.jsonl`, token counts only; no
   dollar cost was shown in this environment). Is that the right trade for the adoption's own reviews?
