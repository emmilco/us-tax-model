# Tax year 2026 adoption plan (for the owner's machine)

Written 2026-11-04 on branch `ty2026/prep` (`docs/ty2026/2026-11-04_ty2026_cloud_brief.md`, steps 1 to 6). The
adoption itself (TASKS.md T-011) runs when the IRS publishes the final 2026 documents, expected December 2026 to
January 2027. Everything prepared here is a proposal: `main`, `years.json` (`[2025]`) and the 2025 encoding are
unchanged.

## What is ready

| Step | Output | State |
|---|---|---|
| 1 | `sources/2026/` (91 documents, 55 IRS drafts), `tools/sources/2026.json`, `reports/2026/archive_refresh_2026-11-04.md` | archive verified (`python3 tools/fetch_sources.py --year 2026`) |
| 2 | `reports/2026/year_diff_from_2025.{md,html}`; `reports/2026/worklist_split.md` and `research/ty2026/worklist.json` (`research/ty2026/split_worklist.py`) | 2,236 worklist items: 426 of kind (a), 1,810 of kind (b) as the script splits them; counting the 16 items of C-PEOP-23 and C-PEOP-24 as kind (b) (owner decision 2026-11-04), 410 of kind (a) and 1,826 of kind (b) |
| 3 | `research/ty2026/changes.md` (135 entries, with C-LAW-01 and C-LAW-02 and the statute read) and `changes.verification.md` (2 high, 11 medium, 7 low; all applied) | 808 quotes checked by `research/ty2026/check_quotes.py`, 0 not printed |
| 4 | `research/ty2026/params-2026.proposed.yaml` (`build_params.py`, `check_params.py`) | 2025 parameters: 92 values from final sources, 70 from drafts, 108 with no 2026 source, and `sc.mileage_rate` retired; 3 new 2026 parameters from final sources (`sc.mileage_rate_h1`, `sc.mileage_rate_h2`, `sa.gift_floor_rate`) |
| 5 | `research/ty2026/forms-proposed/` (Form 1040, Schedule A, Form W-2, new Schedule 3-A, the Schedule C vehicle lines; README) and `research/ty2026/fixtures-proposed/2026-predicted.json` (22 cases) | structural build test passed in a scratch copy (re-run 2026-11-04 after the owner's decisions); not wired in |

## Order of work when the final documents publish

1. **Refetch the finals.** For every row of `tools/sources/2026.json` with `"draft": true`, replace the URL with the
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
   that is no longer printed on its page is the first sign a draft changed. Then fill the 108 parameters with no
   source from the final instructions (`build_params.py`, the `V` table). `python3 tools/propose_params.py --from 2025
   --to 2026 --write --compare research/ty2026/params-2026.proposed.yaml` reads every 2025 parameter at its cited
   place in the 2026 archive and lists, beside the hand-made proposal, what it found, what changed and what it
   could not place (`reports/2026/params_proposal_from_2025.md`); rerun it after the finals are archived.
4. **Adopt the definitions**: `python3 tools/year_diff.py --from 2025 --to 2026 --adopt` (copies the 2025 definitions
   and rulings to 2026 and relocates pages); then apply the proposed parameters
   (`params-2026.proposed.yaml` → `params/2026.yaml`, in the `params/2025.yaml` format: drop `source`, `note`,
   `new_in_2026`, `unsourced` and `retired`, and remove the retired `sc.mileage_rate`) and the proposed definitions (`research/ty2026/forms-proposed/*.diff`, then the other sections of the
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
   prompt year-aware first (T-230). Which lines changed is decided by `tools/transcription/year_carry.py --year 2026
   --from <the 2025 tree> --write` (tools/transcription/README.md, "Carrying reviews across a tax year"): it carries
   the 2025 verdicts of unchanged lines into the 2026 indexes, and `--lines auto` then reviews the rest. Before that,
   check_logs must read a carried record's source snapshot rows against the 2025 manifest (not yet built). A rehearsal
   on this preparation copy is in `research/ty2026/review_carry_rehearsal.md`.
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
  draft and the statute; the W-2 codes on the final instructions; the mileage split on final guidance, with its
  layout from the draft Schedule C instructions).
- **Statute-sourced rules** (decisions 2 and 6): the 0.5% charitable floor (C-PRI-15; `sa.gift_floor`,
  `amb.2026.gift_floor_base`) against the 2026 Schedule A instructions' Charitable Contribution Limitation Worksheet;
  C-LAW-01 (hazardous duty areas) and C-LAW-02 (AMT) against the 2026 Form 1040 instructions; and every entry the statute
  read (`changes.md`, last section) points to.
- **Fixtures**: every case of `2026-predicted.json` labelled draft, and the four `ty2026.sa.gift_floor_*` cases
  against the Schedule A instructions.

## Documents still missing (on 2026-11-04)

The 2026 Instructions for Form 1040 (`i1040gi`: 937 kind (b) items and 60 parameters wait on it), Schedule A
(`i1040sca`), Schedule D (`i1040sd`), Form 8949, Form 8995-A, Form 4562, Form 8582, Schedule K-1 (Form 1065), Form
8962; Publications 334, 463, 501, 502, 504, 525, 526, 527, 550, 560, 561, 587, 590-A, 925, 946, 969, 970, 974; the HTML
editions of the instructions; final regulations on car loan interest (`fr-2025-24154` was proposed); 2026 guidance on
overtime methods (the 2025 `n-25-69`); the U.S. Code 2025 edition (not on GovInfo on 2026-11-04). Full list:
`reports/2026/archive_refresh_2026-11-04.md` section 7.

## Questions for the owner, and the owner's decisions (2026-11-04)

1. **Mileage rate in half cents** (C-BUS-01): the 2026 business rate is 72.5 cents before July 1 and 76 cents from July
   1. `sc.mileage_rate` is whole cents. Options: a rate type (cents per mile as a fraction), or refuse mixed-period
   mileage. Which?
   **Decision:** store the rate as an exact rate (the `Rate` type, num/den) and round at the line; do not refuse mileage
   spanning both periods. Done: `sc.mileage_rate_h1` (725/1000) and `sc.mileage_rate_h2` (76/100) replace
   `sc.mileage_rate`; `forms-proposed/scveh.yaml` asks each period's miles, rounds each product half-up to the cent and
   adds them (C-BUS-01; two predicted cases).
2. **Charitable gifts until the Schedule A instructions post** (C-PRI-15): the proposal refuses every itemizer with
   gifts to charity, because the 0.5% floor worksheet is not published. Acceptable as an interim, or should the floor
   be encoded from the statute (final) with an ambiguity entry?
   **Decision:** encode the 0.5% floor now from Public Law 119-21 (final) and recheck it when the Schedule A instructions
   post. Done: `forms-proposed/sa.yaml` line 13 is lines 11 and 12 less 0.5% of the contribution base (Form 1040 line 11b,
   not less than zero), with no refusal; new parameter `sa.gift_floor_rate`; ambiguity `amb.2026.gift_floor_base`; four
   cases predicted from the statute before any evaluation (C-PRI-15).
3. **Schedule 3-A** (C-PRI-05): encode it in full (two new questions, one of which, "qualified alien", needs the
   instructions), or refuse Schedule 3-A cases until its instructions post?
   **Decision:** refuse those returns until its instructions define "qualified alien". Done: `forms-proposed/s3a.yaml`
   refuses line 8 (so Form 1040 lines 32b to 37) whenever line 8 is reached, that is line 6 above zero and line 7 Yes;
   a return whose line 6 is zero, or that answers line 7 No, is still figured (C-PRI-05; cases updated).
4. **Kinds of the change map**: the PEOP section used "wording only (provisional)" for 33 items whose only source has
   no 2026 edition; keep that label, or fold them into kind (b)?
   **Decision:** count them as still waiting for a 2026 source (kind (b)). Done: C-PEOP-23 and C-PEOP-24 are kind (b).
   They hold 16 worklist items (the PEOP coverage table and `worklist.json`), not 33: the "33" in the PEOP section's
   introduction could not be reproduced and is corrected there. Counts above: 410 (a), 1,826 (b).
5. **Scope of new 2026 provisions**: Trump accounts (Form 1099-R box 7c, Form 5329 Parts X–XI, W-2 code TA), Form
   1062, the non-itemizer charitable deduction: refuse (as proposed) or plan coverage?
   **Decision:** keep Trump accounts, Form 1062 and the non-itemizer charitable deduction refused (as proposed).
6. **Public Law 119-21, the rest of it**: the verification found one 2026 rule (section 71304) that no 2026 IRS
   draft carried yet. Should the adoption include a full read of every section of Public Law 119-21 effective for 2026
   against the encoded forms (the tax provisions of its 332 archived pages, best read by one agent with the change map in hand)?
   **Decision:** a full read of the provisions effective for 2026 that touch the individual income tax as encoded. Done:
   `changes.md`, section "Public Law 119-21: the provisions in force for 2026": the heading, amended Code sections and effective date of
   every Title VII tax section, and the full text of the individual provisions (sections 70101 to 70120, 70424, 70425,
   70437 to 70506, and the parts of the others that name an encoded form); 61 provisions listed with quotes, each pointing to its entry; two new statute-sourced entries
   (C-LAW-01, section 70118, hazardous duty areas; C-LAW-02, section 70107, AMT), both not encoded and changing nothing
   computed; no further rule of the section 71304 kind (a computed change with no entry) was found.
7. **Agent use**: step 3 used five Opus agents (logged in `research/costs/agent_runs.jsonl`, token counts only; no
   dollar cost was shown in this environment). Is that the right trade for the adoption's own reviews?
   **Decision:** five Opus agents was fine. (The decisions above were applied in one session without agents.)
