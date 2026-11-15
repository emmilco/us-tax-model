# Landing the interview redraft on main: check-all to green (unpaid part)

Agent: claude-opus-5-5, judgment class, year 2025, jurisdiction us. Worktree `.claude/worktrees/landing`, branch
`landing/interview-redraft`, HEAD `5d5fb97c` with the redraft laid over as uncommitted changes. No commit is made
here; no paid review or model call is made.

## 1. Classification of the first run's failures

Source: `/tmp/claude-landing-checkall-1.log` (full tier, this worktree's tree). The run stopped after wave 1:
`self_tests adapter_contracts check_logs citations gate_frequencies instruction_cites screen_currency
false_no_currency question_currency consumers limits completeness year_ids`.

Categories: (a) a tool or test left stale by the redraft; (b) a ratchet that asks to be emptied; (c) a finding that
needs a fix in the forms or a ruling; (d) review currency only a paid review restores; (e) "due at the next release"
notices, which do not fail a commit.

| Step | Category | Count | What |
|---|---|---|---|
| self_tests / review_tools | (a) | 6 tests | 3 `HsaPartialInputs` errors (the partial-input checker throws), `InternalAdapterContracts` (state fail), 2 `PartialInputContracts` (state fail) |
| self_tests / interview_length_self_test | (a) | 1 | `umbrella-what-if.ts`: `s1.nqdc_pension is already gated by s1.nqdc_pension_if_w2` |
| self_tests / interview_coverage_self_test | (a) | 1 | the planted row's message changed: the walk now reaches `person.blind` from a row answer, so the "no answer of the row leads to it" case is not produced |
| self_tests / twins_self_test | (a) | 1 | no twin pair without declared differences is an asked input with bank entries and defaults |
| adapter_contracts | (a) | 1 adapter (several outputs) | `no input supplied for div.other_boxes` |
| gate_frequencies | (a)/(b) | 1 | `reports/2025/gate_frequencies.md` stale (and, per the redraft's notes, `interview/2025/gate_frequencies.yaml` names lines now derived and lacks the new parents) |
| screen_currency | (b) | 1 | orphan `gate:div.has_capital_gain` in `screen_review.json` |
| false_no_currency | (b) | 1 | orphan `gate:div.has_capital_gain` in `false_no/div.json` |
| question_currency | (b) | 31 | orphan question reviews (asset.screen, f1095a.uniform, f5695.part1_any/part2_any, household.married/unmarried, ira.special, 12 of person, retirement.code_screen, s1.line8g/h/i/j/r, s179.line10, sa.line8a, scope.other_line16, scveh.screen/smr_ok, tipjob.amount/qualified) |
| consumers | (b) | 97 | baseline entries that no longer fail |
| limits | (b) | 1 | `limit:p575:p35:1499b8a9` no longer fails |
| consumers | (c) | 62 | new input-page pairs: an input read by a new gate line that cites a page the input's own citation does not |
| citations | (c) | 1 + 82 | 1 anchor finding (`f8959` p. 1 "wage statements of U.S. territories"); 82 computed-line locator segments to rewrite (div 3, f5695 1, f8959 1, person 1, qbi 3, s1 4, s2 7, sa 21, sc 13, scope 27, …) |
| instruction_cites | (c) | 2 | `f1040.line25d` and `f8995.line3` name no page of their instructions |
| completeness | (c) | 2 | rulings `unruled:s1a#1.1`, `#1.2` name a "covered" line that no longer exists |
| check_logs | (d) | 96 logs | transcription 36 (line-scoped), render 33 (32 line-scoped, f5695 whole), class M 27 |
| year_ids | left alone | 21 | the pending rename (piece 3) |
| screen / false-no / question / completeness currency | (e) | 157 + 119 + 743 questions + 62; NY 2 + 1 + 19 + 4 | due at the next release; listed, not failed |

Not failing but noted: `check_logs` lists human readings pending (no H credit) for f1040, person, sa; human
readings are optional under the validation policy.

## 2. Progress

### Fixes, (a): tools and tests left stale

- `tools/transcription/adapter_contracts/2025/div.json`: base input `div.other_boxes: true` (the new plain parent of
  the less common 1099-DIV boxes; the contract's facts state those boxes, so the truthful parent answer is yes).
  `adapter_contracts.py`: 21 + 19 cases pass.
- `tools/transcription/input_contracts/2025/dependent.json`: the redraft's seven new dependent parents added to the
  base facts with the answers that open the detailed questions the bank already states (the same answers
  `fixtures/2025/defaults.json` gives, for the same reason): `citizen_ssn` false, `ever_married` true,
  `lived_all_year` false, `own_money` true, `parents_apart` true, `self_support_view` and `supported_view` "unsure".
  No expected value changed.
- `tools/transcription/input_contracts/2025/f8889.json`: H16 and H17 stated `household.married` (no longer an
  input); restated as `household.married_dec31: true` (status mfj, so `marriage_possible` reads the status and
  `household.married` is `married_dec31`). No expected value changed. **Piece (1) adds age questions to f8889: this
  bank may need its new inputs stated afterwards.**
- `engine/src/umbrella-what-if.ts`: `s1.nqdc_pension` dropped from the two Schedule 1 umbrellas' covers (the redraft
  gates it under `scope.has_w2`; the what-if only gates ungated inputs). `engine/src/interview-length.ts` self-test:
  the planted prize is `s1.winnings_any: true, s1.prizes: 100000` (was `s1.line8i`, now computed).
- `engine/src/interview-coverage.ts` self-test: the planted "question no answer of the row opened" was the
  background question after `sa.dependent`, which the redraft now opens from `sa.dependent` itself
  (`person.blind`). The test now takes the first background question after the row's answer whose walk, with its
  background answer removed, stops there with an opener that is not the row's. Same assertion, same message.
- `tools/check_twins.py` self-test: every asked twin pair now has declared differences (`interview.seq`,
  `interview.prompt`, the per-person frame). The asked pair is chosen among pairs with no declared difference in
  the fields the drift is planted in. Same planted cases.
- `reports/2025/gate_frequencies.md` regenerated (`gate_frequencies.py`); `--check` passes.
- Self-tests run after the fixes: `test_review_tools.py HsaPartialInputs PartialInputContracts
  InternalAdapterContracts` OK (28); `interview-length --self-test` passed; `interview-coverage --self-test` passed;
  `check_twins.py --self-test` passed and the check 0 problems.

### Fixes, (b): ratchets emptied (exactly what the checks named)

Removed records are kept in `landing_work/` for the review round and for re-ruling.

- 31 orphan question reviews removed from `reviews/2025/questions/*.json`; 1 orphan screen review
  (`gate:div.has_capital_gain`) from `screens/screen_review.json`; 1 orphan false-no review from `false_no/div.json`.
  Saved: `landing_work/removed_orphan_records.json`. Their verdicts were MATCH 11, NARROW 15, WIDE 3, UNCLEAR 2.
  **The questions that replace them are unreviewed and belong to the review round** (inferred from the ids and the
  forms, not traced one by one): `person.age65`, `born_after_1960`, `born_before_2001`, `died_before_65`,
  `edu_born_2002/2007`, `ira_age50`, `sav_born`, `under16` → `person.birth_year`, `born_jan1`, `died_at_64`,
  `age50_at_year_end`, `under16_at_year_end` (and piece 1's age questions); `person.ira_excess`, `sav_excess` →
  `person.ira_owner`, `x_ira_prior_excess`, `x_edu_*`, `x_archer_excess`, `x_hsa_prior_excess`; `household.married`,
  `unmarried` → `ever_married`, `married_dec31`, `considered_unmarried`; `s1.line8g/h/i/j/r` → `s1.alaska_any`,
  `alaska_dividend`, `jury_any`, `jury_pay`, `winnings_any`, `prizes`, `hobby_any`, `hobby_income`,
  `scholarship_any`, `scholarship_taxable`; `f5695.part1_any/part2_any` → `f5695.any` and the 18 item questions;
  `asset.screen` → the 17 new asset questions; `scveh.screen`, `smr_ok` → the new scveh questions; `tipjob.amount`,
  `qualified` → `tipjob.listed`, `tips`, `charged`, `other_work`, `unlawful`; `retirement.code_screen` → the new
  retirement questions; `ira.special` → `ira.care_payments`, `deferred_comp`, `fellowship`; `f1095a.uniform` →
  `f1095a.same_months`, `b_*`; `s179.line10` → `s179.carryover`, `prior_form`; `sa.line8a` →
  `sa.mortgage_interest` and the home questions; `scope.other_line16` → the scope screens; `div.has_capital_gain`
  (gate) → `div.other_boxes`.
- `reviews/2025/consumers.json`: 97 entries that no longer fail (49 baseline, 48 rulings). `reviews/2025/limits.json`:
  1 ruling (`limit:p575:p35:1499b8a9`). Saved: `landing_work/removed_stale_baseline_and_rulings.json`.
- Checks after: screens 0 new, false-no 0 new, questions 0 new; consumers 0 stale; limits 0 new 0 stale.

### Fixes, (c): findings fixed or ruled

- `forms/2025/f1040.yaml` `f1040.line25d`: locator gains `; i1040gi p. 39, Line 25` (the section the check names).
- `forms/2025/f8995.yaml` `f8995.line3`: locator gains `; i8995 p. 4, Line 3, "Include here the qualified portion
  of trade or business (loss)"`.
- `forms/2025/f8959.yaml` `f8959.territory_w2` and `f8959.unsupported`: cite `i8959` `p. 1, Forms W-2 of U.S.
  territories, "However, for Form 499R-2/W-2PR, Medicare"` (the anchor "wage statements of U.S. territories" was on
  no page of f8959; the rule is on i8959 p. 1).
- `reviews/2025/completeness/rulings.json` `unruled:s1a#1.1` and `#1.2` (class covered): `line` named
  `tipjob.qualified`, which the redraft took apart. Restated: #1.1 → `tipjob.mixed` (a Yes to `tipjob.charged` or
  `tipjob.unlawful` refuses through it), #1.2 → `tipjob.listed` (No makes the employer's qualified tips zero;
  `tipjob.other_work` Yes refuses through `tipjob.mixed`); evidence quotes the new questions. Class unchanged.
- Locator rewrites (82 segments): delegated to one Opus agent (judgment, source reading), editing only `cite:`
  blocks; four lines left for piece (1): `person.age65`, `scope.under24_if_not_joint`,
  `scope.unearned_2700_if_under24`, `scope.f8615_if_unearned_2700`.

### AI isolation classification of the review tools (AISP Part III)

Transcription, render, class M, screen, false-no, question and completeness reviews: fixed-prompt (`claude -p`
with `--tools ""`, `--setting-sources ""`; the reply is parsed as data and compared, no write path or command derives
from it) · curated input (archived IRS sources and this repository) · unattended batch · non-secret data · no
credential in the call's context for the Claude family → low risk, main account. Confirmed from the code that
`--dry-run` returns before `review_response` in `transcribe.py`, `render_compare.py`, `classm.py` (whose dry run
still runs `main.js build`), `screen_review.py`, `false_no_review.py`, `question_review.py`,
`completeness_review.py`, and that `rerun_all.py --dry-run` only runs the tools' dry runs.

### Waves 2 and 3

`tools/check_all_steps.sh` stops after a failed wave, so its wave 2 and 3 steps were run one after another by their
own commands (`/tmp/landing-scripts/waves23.sh`, logs in `/tmp/landing-wave23/`) on the build of this tree. Results
below as they come.

### Locator rewrites (agent result, verified)

The Opus agent rewrote the `cite:` blocks (doc and locator only) of 76 lines (77 segments) in `forms/2025/` div,
f5695, qbi, s1, s2, sa, sc, scope, sd. I reran `tools/citations.py --strict`: 0 findings, 0 unused rulings, 4
locator segments to rewrite (the four lines left for piece 1: `person.age65`, `scope.under24_if_not_joint`,
`scope.unearned_2700_if_under24`, `scope.f8615_if_unearned_2700`). The citations step stays red on those four
until piece 1 lands. The agent's table is in this session's record. Pages it called judgment calls:
`sa.home_other_if_not_owner` (cites the definition of a home), `scope.nonresident_if_noncitizen` (quote with no
heading anchor), `scope.other_line16` (includes the CFC/section 962 bullet). Helper scripts are in `/tmp/citefix/`.
**Consumer rulings (62 new) must be redone after these citations**: a reading line's cited pages define the pairs.

### Wave 2 at this point

conjecture, test_fixtures, ny_test_fixtures, interview_rules, person_wording pass; refusal_reach failed on one stale
exception, which I removed (`tools/refusal_reach_exceptions.json`, saved in `landing_work/`) and the step then passed
on my rerun. interview_coverage was still running; the remaining steps had not started.

## 3. Second session (2026-11-14): after the redraft's last pieces, the rename and the six tool lanes

Agent: claude-opus-5-5, judgment class, year 2025, jurisdiction us. Same worktree, now at `83c7d1c0` with the tree
of `refs/scratch/draft-land2` (`fc6cdaf6`) laid over. No commit, no paid review call, no model call from code. Scripts
and logs of this session: `/tmp/landing2/` (`wave1.sh` runs the wave 1 steps one after another by their own
commands; `build.sh`; `iter.sh` and `unk3.py` for the engine-differential cases).

### Form fixes made before the review round (they change what a reviewer reads)

- `forms/2025/f8959.yaml` `f8959.unsupported`: the label listed seven situations its expression no longer tests. It
  now says what the line tests (a territory wage statement, true when `f8959.territory_w2` is Yes). Where each listed
  situation is refused now, read in the forms and the coverage rows: church employee income at `scope.schedule1`
  (`scope.church_exempt_wages` beneath `scope.religious_work`; row `scope.yaml` church wages); other self-employment
  income outside Schedule SE at `scope.schedule1` (`scope.clergy`, `scope.farm`, `scope.k1`) and `person.se_screened`;
  RRTA at `person.medicare5`/`medicare6` (`person.rrta`; row `jobs.railroad`); Form 4137 and Form 8919 at
  `scope.other_income` (`scope.pay_no_w2`, whose help names unreported tips, box 8 and pay from a firm that treated
  the filer as a contractor; rows `scope.pay_no_w2`); box 8 and box 12 codes B and N at `s2.other` (`s2.w2_marks`; row
  `other.w2_uncollected_tax`). No scope hole. **Not changed:** the seven `refuses` entries of f8959 lines whose
  `remedy` still says "does not prepare RRTA, Form 4137 or Form 8919"; they fire only on a territory statement, so the
  remedy names the wrong forms. Left for the coordinator (it is form text a render review reads).
- Locators of the age lines: `person.age65` (i1040gi p. 33, line 12d); `scope.under24`, `scope.under24_if_not_joint`,
  `scope.unearned_2700_if_under24`, `scope.f8615_if_unearned_2700` (i8615 p. 1, Who Must File, one condition each).
  Five lines, not four: `scope.under24` also failed. `params/2025.yaml` `age.cut_73`: page 8 to 9 (its quote and anchor
  are on p. 9).
- `forms/ny/2025/ny_it201.yaml`: three locators of the New York lane that `citations --strict --jurisdiction ny`
  failed: `ask.abroad` and `ask.installment` (p. 5 to p. 6), `ask.spouse_itemizes` (the quote lost the circled
  status digit the archive drops). Cite text only; decided here because the step blocks the commit and a later fix
  would stale the review.

### Stale tools and tests (the rename, the merged pieces)

- `tools/transcription/input_contracts/2025/f8889.json`: three cases stated `f8889[hsa].age55: false`, no longer an
  input (derived from the birth year); restated as `person[...].birth_year: 1980` (under 55). No expected value changed.
- `tools/transcription/test_ny_review.py`: two assertions listed the New York screens and the federal lines the IT-201
  encoding reads; restated to what the New York lane built (`docs/provisional/lanes/ny.md`: `414h`, `529_*`,
  `abode_part_year`, `city_credits`, `out_of_state_bond_interest`, `real_property_credit`, `special_accrual` are now
  refusing screens; `gov_pension` and `pension_exclusion` are not; new federal reads such as `person.birth_year`,
  `scope.has_w2`, `s1.has_sc`).
- `tools/siblings.py`: the bug inventory is append-only, so entries written before the rename name old ids
  (BUG-0303, 0315, 0348, 0370, 0398, 0400, 0408, 0485), and review logs keep the old document name `clcw26`. The check
  now reads both through `tools/year_free_names.json` (`renamed()`); its self-test passes.
- `tools/transcription/test_classm_jobs.mjs:72`: the Form 1095-A route is read from the entry's computed
  `f1095a.uniform` in the job's project values (the input became derived).
- `engine/src/umbrella-what-if.ts`: dropped the candidates the redraft built (`sb.foreign_any`, `sb.foreign_wide_any`,
  `f1040.other_payments_any`, `f1040.withholding_other_any`, `sd.carryovers_any`, `s1.adjustments_any`) and the three
  covers of `s2.other_taxes_any` the redraft gates or derives; `RECOMMENDED` is now `s1.line8_any` alone. The earlier
  "throws" was the first of these; the run is slow (over 10 minutes; see the end of this section for its result).
- Engine differential. Cause of `KeyError: 'values'`: every generated case failed evaluation with
  `sd.other_forms: input is not declared` (the redraft made it derived), so no case had values. `generate_cases.py`
  now ends each case with `redraft_answers`, which turns the generator's working answers into the redraft's questions,
  as `engine/src/generate.ts` does (every draw unchanged): birth years from the ages (an HSA filer whose age-55 answer
  was drawn and who is younger is 56, the age the UsTaxes adapter already gave such a filer); the screens taken apart
  answered No item by item; Form 5695's parent and kinds from the costs; the 1095-A month and column B questions; the
  new parents of amounts the generator states (`ssb.any`, `f1040.withheld_other_any`, `f1040.estimated_any`,
  `sli.any`, `s1.uc_any`, `div.other_boxes`, Form 2441's questions, a Schedule C's `goods`, `employees`,
  `travel_meals`); `s3.foreign_any` Yes where foreign tax was drawn on a return with no dividends or interest. The
  adapters read the age facts instead of the removed inputs (`ots_adapter.py`, `ustaxes_adapter.py`), and
  `compare.py` reads the Form 5695 parts from the facts (`energy_part1`, `energy_part2`, also in its not-computed
  allowances). Check used while iterating: every compared line of every case evaluated with no unknown input. First
  full run: 319 unexplained (boxes 2b/2d hidden behind `div.other_boxes`, foreign tax with no dividends hidden behind
  `ftc.asked`); after those two fixes: **1700 cases, 568,880 comparisons, 0 unexplained, 34 explained**. The engines
  reran (new cases, new parameters): records stored under new keys.
- `tools/coverage/tree.json`: the five new refusal gates placed (household and deductions); `docs/COVERAGE.md` and the
  README table regenerated (234 gates).
- `interview/2025/gate_frequencies.yaml`: refs to inputs that became derived restated one to one (`person.birth_year`,
  `f5695.any`, `s179.prior_form`, `f8959.territory_w2`, `s2.amt_owed`); the aggregate screens (`scope.*`, `s2.other`,
  `sa.unsupported`, `qbi.unsupported`, `person.x_other`) keep their derived ids as the name of the situation. The file's
  rules require no entry per new parent; none added. Report regenerated.
- Year operations (`changes/2026/`): the three predicted failures mended as the design prescribes, each recorded in
  its entry's note and in `changes/2026/README.md`: `f1040.line33` reads `f1040.line26_if_estimated`; the
  `sa.unsupported` entry is re-based on the redraft's computed line (label; the premiums of line 8d, which the redraft
  no longer asks, become a new question `sa.mortgage_insurance` beneath the mortgage interest answer, with its gate
  line and bank entry, `like: sa.mortgage_other_use`, seq 29; the disaster-loss rule re-based on the help of
  `sd.casualty`, which now asks personal casualty losses). No operation named a renamed id. 90 operations apply.
- Check-all wiring: `tick_groups` is a wave 2 step (`tools/check_all_steps.sh`); `tick_groups_self_test`,
  `interview_order_self_test`, `draft_walk_self_test` are rows of `tools/self_tests.py`; `tier_paths.py --self-test`
  passes. `tools/draft_check.sh` and `tools/draft/` (the clone's bar and merge scripts) are removed (copies in
  `landing_work/removed_tools/`); `PROJECT_INDEX.md` and `interview/README.md` now point at check-all.

### Ratchets emptied (exactly what the checks named; removed records in `landing_work/removed_after_rename.json`)

13 federal and 2 New York orphan question reviews (inputs renamed or removed whose records did not carry), 1 stale
false-no ruling, 8 stale consumers entries, 1 stale New York consumers ruling, 2 stale instruction-cites baseline
entries. `reviews/2025/completeness/rulings.json` `unruled:f4562#5.2`: its `line` renamed through the map
(`asset.bonus_2025` to `asset.bonus_this_year`), class and evidence unchanged. `reviews/2025/limits.json`: one new
ruling, `limit:i8582:p1:57da1db6` not applicable (Form 8582 is never figured: passive activities and rentals refuse).

### Carry across the rename

The map file `tools/year_free_names.json` is not in the form `rename_carry.py` reads (a dict of `{to, kind, ...}`
records, with the whole document `clcw26`), so the flat map it reads is derived in
`landing_work/rename_carry_map.json` (54 line ids and the 28 lines of `clcw26`: 82 ids; `rename.md` says 84, the
document has 28 lines). Run from `d6e7c1e6`, report first (`landing_work/rename_carry_dryrun.md`), then `--write`
(`landing_work/rename_carry_report.md`, 18 files written). Carried 41: transcription 19 lines, render 15 lines, class M
1 form (f8880), questions 2, screens 2, false-no 1, consumers 1. Not carried 173: transcription 87 and render 32 lines
"not current at the old names" (the redraft changed them), render 10 more whose cited text or table changed since
`d6e7c1e6` (8 on `i1040gi` Form 8862, 2 on the table `recovery_year`), class M 11 forms, questions 20, completeness 12,
screens 1 (no such unit now). The carry does not move a renamed document's logs: `clcw_next_year` has no transcription,
render or class M log, and the `clcw26` logs remain under the old name (check_logs lists `clcw_next_year` missing;
`audit_skipped.py`, step `classm_skipped`, fails loading `forms/2025/clcw26.yaml`). Left for the coordinator.

### Consumer rulings

After the locator rewrites, the age-line locators and the rename, the federal consumers check had 296 new pairs (not
62: a reading line's cited pages define the pairs, and the rewritten locators cite more pages); New York 3. Prompts with
the page text: `tools/check_consumers.py --prompts`. The 296 were split by reader across four Opus agents (judgment;
read-only; each wrote proposed rulings to /tmp): A, the refusal aggregators of the scope screens, Schedule D's other
forms and Schedule 1 line 8 (108); B, `sa.unsupported`, `s2.other`, `s2.amt`, `ftc.asked` (51); C1 and C2, the gate
lines, where the pair is the parent question against the child's page (68 and 69). I checked every proposed ruling
mechanically (key is an open pair; verdict `same`; both phrases verbatim substrings of the question and of the page
text), and merged 271 into `reviews/2025/consumers.json`. I did not re-read each page: the rulings rest on the agents'
reading. 25 pairs are left unruled as findings (`landing_work/consumers/`, with each agent's reasoning); the check stays
red on exactly those 25. The 3 New York pairs are not ruled (see "Not done").

Recorded as pending defects (`bug_pending/landing-01` to `-13`; 01 and 02 confirmed by me against the bank, the rest
the agents' reading): mortgage limit question without the married-filing-separately limits; church employee income,
Form 8978 and reservist repayment questions without the spouse; a personal-casualty NOL gated behind
`scope.business_before`; the PFIC question defining a PFIC as a fund; `s3.adoption_any` missing employer-paid benefits;
ISO stock vesting in 2025 after an earlier exercise; `s2.amt_owed` asking only whether AMT is owed; Archer and Medicare
Advantage MSA distributions (line 8e) not asked; forks missing from the digital asset question; Medicaid waiver
payments for care outside the home; education credit recapture for the student's aid. Unsure, not recorded:
`scope.reforestation` (leased timber land), `dependent.eic_ssn@i1040gi:p18` (likely a citation, not the question),
`person.ira_owner@f5329:p1` (present tense), `scope.religious_work` (Christian Science practitioner),
`scope.passive@i8582:p1`, `scope.se_plan_other` (contributions made in 2026 for 2025),
`sa.personal_property_tax_any` (territory tax), `sd.sold_other` (single payment the next year).

### Check-all, step by step (RAN, on this tree after the last form edit; build and render fresh)

Run by their own commands, one after another (`/tmp/landing2/wave1.sh`, `/tmp/landing2/waves23.sh`), not by
`tools/check_all.sh`. Wave 1 (`/tmp/landing2/w1b/`): every step passes except
- `classm_skipped` (`audit_skipped.py` loads `forms/2025/clcw26.yaml`; the logs keep the old document name);
- `check_logs`, `ny_check_logs`: stale review logs (the review round) and `clcw_next_year` without logs;
- `consumers`: the 25 unruled pairs above (New York 0 after the 5 New York rulings).
Waves 2 and 3 (`/tmp/landing2/w23/`): pass lean_build, conjecture, test_fixtures, ny_test_fixtures, tick_groups,
person_wording, interview_length (309 returns, 0 problems, 79 min), interview_coverage, test_integration,
test_serve, classm_job_seeds, coverage, coverage_tree, properties, ny_properties, differential,
engine_differential (0 unexplained), compare, ny_compare, evidence, review_packets (rerun alone after a concurrent
class M dry run had removed `canonical/` mid-run). interview_rules: its only problem was the stale
`reports/2025/interview_pruning.md`, rewritten with `--write-pruning` (then 0 problems). Fail:
- `mutate`, `ny_mutate`: stale arguments (pins), as expected; the mutation lanes' work.
- `refusal_reach`: `t264.f4952.unsupported_with_interest` no longer refuses at an interview target: `f4952.required`
  still refuses, but the targets that read it are now unknown first on inputs the fixture leaves out
  (`person[taxpayer].birth_year` null, `f8959.territory_w2` absent). Not fixed: it needs a fixture input stated or an
  exception added, a coordinator decision.
`interview-length --what-if` was not rerun after trimming the candidates (it timed out at 10 minutes earlier).

### Review round plan (dry runs only; no paid call)

`rerun_all.py --kinds transcription,render,classm --model claude-opus-5-5 --dry-run` (saved:
`landing_work/rerun_us.txt`, `rerun_ny.txt`). Federal: 99 jobs, **$182.24** (class M 28 forms $91.73, of which
`person` $36.20, `s1` $7.26, `eic` $5.94, `dependent` $4.76; render 33 jobs $34.07, line-scoped but `f5695` whole;
transcription 38 jobs $56.45, line-scoped but `dependent` and `f8889` whole because they have partial-input cases);
77 jobs current. New York: 3 jobs for `ny_it201`, **$6.41**. `clcw_next_year`: 0 jobs, because it has no log (the
`clcw26` logs were not moved); the 3 `clcw26` jobs cannot be built. Sampled reviews due (each tool's `--dry-run`):
screens 185 ($40.85) + NY 32 ($4.49); false-no 142 ($41.04) + NY 23 ($5.09); questions 748 ($115.12) + NY 52
($4.97); completeness 62 ($16.18) + NY 4 ($0.94). Every run is above the $3.00 gate and needs `--approve-cost`.
Classification (AISP Part III), unchanged from section 2: fixed-prompt, curated input, unattended batch, non-secret,
low risk, main account.

### Not done, for the coordinator

1. Move the `clcw26` review logs to `clcw_next_year` (or teach `audit_skipped.py` and the plan the rename); until then
   `classm_skipped` fails and `clcw_next_year` has no reviews.
2. `refusal_reach` (above). 3. The 25 unruled consumer pairs (13 pending defects). 4. f8959 refusal remedies naming
   RRTA, Form 4137 and Form 8919. 5. Mutation pins (the mutation lanes). 6. The review round, after owner approval of
   its cost.
