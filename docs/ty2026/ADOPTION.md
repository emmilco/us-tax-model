# Tax year 2026 adoption plan (for the owner's machine)

Written 2026-11-04 on branch `ty2026/prep` (`docs/ty2026/2026-11-04_ty2026_cloud_brief.md`, steps 1 to 6). The
adoption itself (TASKS.md T-011) runs when the IRS publishes the final 2026 documents, expected December 2026 to
January 2027. Nothing is adopted: `years.json` lists 2025 alone (`adopted` and `ny_adopted`). The preparation is
kept outside the build: the definition changes as operations in `changes/2026/` (checked against the 2025 forms on
every check-all run), and the parameters and tables staged in `research/ty2026/`. The tables below were brought up
to date on 2026-11-15, after the 2026 preparation lanes (`docs/provisional/lanes/ty26-*.md`; plan `ty26-plan.md`).

## What is ready

| Step | Output | State |
|---|---|---|
| 1 | `sources/2026/` (122 documents, 69 IRS drafts), `tools/sources/2026.json`, `reports/2026/archive_refresh_2026-11-04.md`, the refresh of 2026-11-14 (`archive_refresh_2026-11-14.md`: three finals, two reposted drafts, five new drafts), the 22 documents added on 2026-11-15 for the coverage expansion, and the refresh of 2026-11-22 (ten finals, posted 2026-11-17 to 2026-11-20: f8889, f8880, f8863, f5329, i1040sb, f7206, p915, f8919, f1045 and i1045; two new drafts, p969 and i6251; Notice 2026-5; the catalog rows name the drafts they supersede), and the refresh of 2026-11-24 (`docs/ty2026/2026-11-24_refresh_and_rehearsal.md`: no new final, no reposted draft, no gating document; the Form 6251 draft of 2026-05-28 added) | archive verified (`python3 tools/fetch_sources.py --year 2026`) |
| 2 | `reports/2026/year_diff_from_2025.{md,html}`; `reports/2026/worklist_split.md` and `research/ty2026/worklist.json` (`research/ty2026/split_worklist.py`) | 2,236 worklist items: 426 of kind (a), 1,810 of kind (b) as the script splits them; counting the 16 items of C-PEOP-23 and C-PEOP-24 as kind (b) (owner decision 2026-11-04), 410 of kind (a) and 1,826 of kind (b) |
| 3 | `research/ty2026/changes.md` (136 entries, with C-LAW-01 and C-LAW-02, the statute read, and C-SCHED-40, the final car loan regulations) and `changes.verification.md` (2 high, 11 medium, 7 low; all applied) | 836 quotes checked by `research/ty2026/check_quotes.py`, 0 not printed (2026-11-24, against the refreshed archive; C-LAW-02 rewritten with its operations) |
| 4 | `research/ty2026/params-2026.proposed.yaml` (`build_params.py`, `check_params.py`), merged with the mechanical proposal `reports/2026/params_proposal_from_2025.{md,yaml}` (`tools/propose_params.py`); the staged tables `research/ty2026/tables-2026/` (`dc_rate`, `ltc_limit`, `savers_rate`, `rate_schedule`) | 349 values (2026-11-24, with the parameters added to 2025 since): 168 from final sources, 82 from drafts, 16 derived (the `age.*` years of birth, `moves_with_year`), 83 with no 2026 source (`amt.rate_25`, now line 37 only, filled on 2026-11-24 from the Form 6251 draft, p. 3, 25%; the phase-out reads `amt.phaseout_rate`, BUG-1031; `sa.gift_total_limit_rate` and `sa.gift_property_limit_rate` wait for the 2026 Pub. 526); 13 of them new in 2026 (every parameter the operations read that 2025 lacks); filled on 2026-11-23 from final sources the audit of 2026-11-22 named: `sdtw.ordinary_ceiling`, `sli.divisor_*` (from rp-25-32), `clcw.prior_limit*` (the Schedule D draft, line 21), and six re-cited from draft to final (`qbi.threshold`, `sa.salt_threshold`, `ira.limit_50`, `f5329.cap_abuse`, `f5329.simple_rate`, `ctc.age_limit`); `refund.std_*` and `refund.box_*` stay unsourced until the 2026 Form 1040 instructions (their inferred values are in their notes); `savers_rate` and `ltc_limit` re-extracted from the final Forms 8880 and 7206 (values unchanged); 15 retired (`sc.mileage_rate`, `sc.bonus_rate_40`, `ptc.repay_*`, ten `f5695.*`) |
| 5 | `changes/2026/` (166 entries, 1,405 operations, carrying out 92 of the change map's entries; `changes/2026/README.md`), from the proposals of `research/ty2026/forms-proposed/` (Form 1040, Schedule A, Form W-2, new Schedule 3-A, the Schedule C vehicle lines) and the change map; `research/ty2026/fixtures-proposed/2026-predicted.json` (22 cases) | `python3 tools/year_changes.py --check`: all apply to the 2025 forms; 130 of the 166 entries rest on drafts (2026-11-24, after lane ty26b's additions; no entry has had all its documents turn final since 2026-11-22; on 2026-11-22: eight entries flipped to `verified: final` after their evidence and locators were checked against the finals: C-PEOP-02, C-SCHED-16, C-CRED-16 (three files), C-PEOP-17, C-PEOP-19, C-PEOP-21) |

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
3. **Verify every draft-sourced item against the final** (the list below): the change map entries, the 82 draft
   parameters, the operations (an entry is marked `verified: final` once checked; `year_changes.py --check` notes
   each entry whose documents are all final) and the draft-sourced fixture cases. Run
   `python3 research/ty2026/check_quotes.py` and `python3 research/ty2026/check_params.py` after refetching: a quote
   that is no longer printed on its page is the first sign a draft changed. Then fill the 82 parameters with no
   source from the final instructions (`build_params.py`, the `V` table). `python3 tools/propose_params.py --from 2025
   --to 2026 --write --compare research/ty2026/params-2026.proposed.yaml` reads every 2025 parameter at its cited
   place in the 2026 archive and lists, beside the hand-made proposal, what it found, what changed and what it
   could not place (`reports/2026/params_proposal_from_2025.md`); rerun it after the finals are archived.
4. **Adopt the definitions**: `python3 tools/year_diff.py --from 2025 --to 2026 --adopt`. It copies the 2025
   definitions to 2026, relocates their pages, applies the operations of `changes/2026/` (refusing if one does not
   apply; `docs/2026-11-14_year_change_operations.md`), extends the year-valued enums (`placed_year`) and
   `recovery_year`, carries the review files adoption keeps (citation rulings, the source-coverage rulings and
   baselines, `input_quotes`, `twins.json`, the input and adapter contract banks), and lists the year literals of
   the copy and the year-shared references to removed ids (`reports/2026/year_literals_from_2025.json`,
   `shared_refs_from_2025.{json,md}`) for the adoption to judge (tools/README.md, "Year changes as operations").
   Then apply the proposed parameters (`params-2026.proposed.yaml` → `params/2026.yaml`, in the `params/2025.yaml`
   format: drop `source`, `note`, `new_in_2026`, `unsourced` and `retired`, and remove the retired parameters) and
   the staged tables. Work the citation check (`tools/citations.py --strict --year 2026`) and
   `reports/2026/relocation_from_2025.md` until `node engine/dist/main.js build --year 2026` passes.
5. **New inputs and their ripple.** Each new input's test-data default is in its `add_question` and is written to
   `fixtures/2026/defaults.json` by `fixtures_year.py`, and the contract banks are carried by `--adopt`; the rest of
   the ripple (`engine/src/generate.ts`, `tools/engines/generate_cases.py`, the contract banks' cases for the new
   inputs) has one owner per input (`handoffs/HANDOFF-HARDENING-1.md`).
6. **Fixtures**: `python3 tools/fixtures_year.py --from 2025 --to 2026` (spec 6.7); add the cases of
   `fixtures-proposed/2026-predicted.json` as full fixtures (every input answered), each re-checked against the final.
   The 2026 tables (Tax Table, EIC tables, Form 8962 tables, Pub. 946 tables, auto limits, `ltc_limit`,
   `simple_catchup`, `savers_rate`, `dc_rate`) need re-extraction from the finals.
   `python3 tools/extract_printed_tables.py --write --year 2026` writes `dc_rate`, `ltc_limit`, `savers_rate`,
   `rate_schedule` and the automobile limits from the archive (on the drafts it writes the first four, staged with
   `--out research/ty2026/tables-2026`; the automobile limits wait for the 2026 Pub. 946; the 2026
   `dc_rate` has a column for joint returns and one for the other statuses, which the Form 2441 operations read by
   filing status). `simple_catchup` is still written by hand (tools/README.md, "Printed tables"). Place the page
   layouts with `python3 tools/layouts.py --propose --from 2025 --to 2026` (on the drafts none of the six can be
   placed: they wait for i1040gi, i8962 and Pub. 946).
7. **Reviews of changed forms only** (CLAUDE.md, inference cost): transcription, render and class M for the forms whose
   content changed; completeness and screen reviews for those forms; adjudicate only those. Which lines changed is decided by `tools/transcription/year_carry.py --year 2026
   --from <the 2025 tree> --write` (tools/transcription/README.md, "Carrying reviews across a tax year"): it carries
   the 2025 verdicts of unchanged lines into the 2026 indexes, and `--lines auto` then reviews the rest. check_logs
   checks a carried record's source snapshot rows against the 2025 manifest and each carried line's year-carry key
   against its current one (T-340), and reads a carried log's source snapshot rows against the manifest of the year it
   was carried from as well as 2026's (`snapshot_problems`); `rerun_all.py` also plans, whole, the forms logged in 2025
   that the carry left with no 2026 log. A rehearsal on this preparation copy is in
   `research/ty2026/review_carry_rehearsal.md`; the whole adoption is rehearsed by `tools/year_rehearse.sh`
   (tools/README.md).
8. **`years.json`**: add 2026 to `adopted` only when every 2026 source is final and the 2026 build and fixtures pass;
   `ny_adopted` gains 2026 only with New York's own adoption (below).
9. **check-all** on the owner's machine (`tools/check_all.sh --year 2026`), then commit with the hook.

## New York

New York publishes its 2026 forms after the IRS; nothing for New York 2026 is archived or prepared. The New York
tools take `--year` and refuse a year with no New York data (`tools/README.md`, "New York years"). The order of work
the day New York publishes, after the federal adoption (New York reads federal lines), and what a rehearsal on the
2025 documents showed, are in `docs/ny/2026-11-14_ny_year_handling.md`, sections 3 and 6. Federal 2026 can be
adopted first: for a year `years.json` does not list in `ny_adopted`, check-all skips every New York step, naming it
and the reason, the build skips the conflict checks that name a New York gate, and its reader check counts as read
the federal lines the 2025 New York forms read (BUG-1409; tools/README.md, "New York years").

## Definition changes in the order to do them (from `changes.md`)

The order of 2026-11-04. The definition changes are now written as operations for 91 entries
(`changes/2026/README.md`, column "Written"). Of the rest, all but three change no definition (parameters, year
literals, page moves, no change, not encoded) or wait for a document. Three were classified as wording changes and
have no operation: C-PRI-11 (its lines cite only i1040gi; line 14 is a definition change left for a later lane),
C-PRI-29 (nothing stale; both `docs/provisional/lanes/ty26-w1.md`) and C-SCHED-36 (Form 4952, assigned to no
lane).

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

## Items that must be re-verified against the final documents (as of 2026-11-24)

No document has turned final since the refresh of 2026-11-22, so the list is that of 2026-11-22 with today's counts
(`docs/ty2026/2026-11-24_refresh_and_rehearsal.md`).

- **Change map**: every entry whose 2026 bullet is marked "(draft)" (most of the 135; the final-sourced entries are
  those resting on the final Schedule C, Schedule SE and its instructions, Form 4952, Form 1095-A, the 1099-R and W-2
  instructions, Schedule 8812, Forms 8606, 8863, 8880, 8889, 5329, 7206, 8919, 1045 and its instructions, Schedule B's
  instructions, Pub. 915, Rev. Procs. 2025-32, 2025-19, 2025-25 and 2026-15, Notices 2025-67, 2026-5 and 2026-10, IRB
  2026-29 and Public Law 119-21). The corrections in `changes.verification.md` apply first.
- **Parameters**: the 82 with `source: draft` in `params-2026.proposed.yaml`, among them `amt.rate_25` (Form 6251
  line 37, from the Form 6251 draft since 2026-11-24). Also the Tax Computation Worksheet rows taken from the rate tables
  (confirm against the worksheet), the EIC limits taken from Rev. Proc. 2025-32 (confirm against the Form 1040
  instructions' EIC steps), and the 83 with no 2026 source (`check_params.py` lists them; most wait on i1040gi). The
  dependent care exclusion: the final W-2 instructions (p. 19) print "$5,000 exclusion" against the Form 2441 draft's
  $7,500 (C-CRED-11; recorded 2026-11-04, not re-read today).
- **Operations**: the 130 of the 166 entries of `changes/2026/` marked `verified: draft`. The drafts most often left
  alone in an entry: Schedule 1-A (12 entries), Form 1040 (11), the Schedule C instructions (10), the Form 8863
  instructions (9), Schedule A (7), the Form 5329 instructions (7). The entries the rehearsals of 2026-11-24 found
  wanting are written (lane ty26b): `person.edu_tin_missing` removed with its reader (BUG-1408); the two Roth IRA
  refusals of `person.x_tax` moved to `person.x_tax_excess` with the 2026 amounts (they carry the 2025 refusals of
  BUG-1154: a change to those refusals in 2025 is to be made in `changes/2026/person.retirement.yaml` too); the
  Schedule 2 AMT citations of Form 6251 itself requoted from the 2026 draft (`changes/2026/s2.f6251.yaml`, C-LAW-02;
  `f6251` draft, so they are rechecked at the final). `year_changes.py --check` now fails on a helper or gate line
  left with no reader by the operations, the build's reader check, so this class is caught before adoption.
  The rehearsal of the result (`docs/ty2026/2026-11-24_refresh_and_rehearsal.md`, section 6) adopts and builds 2026
  with no workaround but the unpublished sources stood in: 2,400 of 2,403 fixtures pass, review estimate $240.22
  for 215 jobs with class M priced.
- **Car loan interest**: the final regulations (T.D. 10054, `fr-2026-18219`) replace the proposed ones
  (`fr-2025-24154`) for 2026: every citation of the proposed regulations in `carloan`, the `carloan_kind` enum and the
  two register entries moves to the final (`changes/2026/carloan.regs.yaml`, C-SCHED-40, `verified: final`;
  `build_params.py`). The rules computed read the same. The final applies to taxable years beginning after
  December 31, 2024, so to 2025 too, and counts credit insurance products and GAP as qualifying, which
  `carloan.nonqualifying`'s question ("insurance") does not say: a 2025 defect (BUG-1441), whose fix
  the year carries. Line 28(1) for a loan taken over at a death is decided and registered for 2026
  (`amb.2026.carloan_heir_original_use`, BUG-0734), to recheck against the 2026 Form 1040 instructions.
- **Statute-sourced rules** (decisions 2 and 6): the 0.5% charitable floor (C-PRI-15; `sa.gift_floor`,
  `amb.2026.gift_floor_base`) against the 2026 Schedule A instructions' Charitable Contribution Limitation Worksheet;
  C-LAW-01 (hazardous duty areas) and C-LAW-02 (AMT) against the 2026 Form 1040 instructions; and every entry the statute
  read (`changes.md`, last section) points to.
- **Fixtures**: every case of `2026-predicted.json` labelled draft, and the four `ty2026.sa.gift_floor_*` cases
  against the Schedule A instructions.

## Documents still missing (as of 2026-11-24)

Checked 2026-11-24 at `irs.gov/pub/irs-pdf/` and `irs.gov/pub/irs-dft/` (and the draft listing for Forms 6251, 8829
and Pub. 926): no gating document has posted, as a final or as a 2026 draft. `i1040gi` (the Form 1040 instructions,
which most of the 83 unsourced parameters and C-PEOP-23 wait on), `i1040sca`, `i1040sd`, `i8949`, `i8995a`, `i4562`,
and Publications 463, 501, 526, 560, 946 and 970 each show only an edition dated December 2025 to March 2026. Also
still with no 2026 edition: the instructions for Schedule K-1 (Form 1065); Publications 334, 502, 504, 527, 550, 561,
587 and 974; the HTML editions of the instructions; the U.S. Code 2025 edition. No 2026 notice on overtime methods
(the counterpart of `n-25-69`) was found: for 2026 the IRS's August 2026 FAQs (Fact Sheet 2026-13, not archived)
describe reporting on Form W-2 box 12 code TT, which the 2026 operations already read. Still drafts in the archive: 69
(all the IRS drafts listed in `tools/sources/2026.json`); the final Schedule 3-A and the final Form 1062 instructions
have not posted. Posted but not archived (no 2026 definition cites them): the final 2026 Form 8829 (2026-11-20), and
drafts of Pub. 936 (posted 2026-10-07), Pub. 926 (2027 edition, 2026-10-16) and the Schedule H instructions
(2026-11-19), editions not read. A December 2026 revision of
Publication 529 was posted as a draft on 2026-11-05; the catalog keeps the continuous-use final (Rev. December 2020)
until the new revision is final. Earlier lists: `reports/2026/archive_refresh_2026-11-04.md` section 7 and
`archive_refresh_2026-11-14.md`.

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
   (C-LAW-01, section 70118, hazardous duty areas; C-LAW-02, section 70107, AMT), C-LAW-01 not encoded and changing
   nothing computed; C-LAW-02 changes the computed AMT screen (operations in `changes/2026/s2.yaml`, BUG-1031); no further rule of the section 71304 kind (a computed change with no entry) was found.
7. **Agent use**: step 3 used five Opus agents (logged in `research/costs/agent_runs.jsonl`, token counts only; no
   dollar cost was shown in this environment). Is that the right trade for the adoption's own reviews?
   **Decision:** five Opus agents was fine. (The decisions above were applied in one session without agents.)
