# Tax year 2026: the year changes as operations

The operations that take the 2025 definitions to 2026, one file per form they act on, applied by
`tools/year_changes.py` (format and checks: `tools/README.md`, "Year changes as operations"; design:
`docs/2026-11-14_year_change_operations.md`). check-all applies them to `forms/2025`, `interview/2025`,
`ambiguities/2025.yaml` and the archived pages of `sources/2026` on every run (130 entries, 1,256 operations); `tools/year_diff.py --from 2025 --to 2026 --adopt` applies them to the
adopted copy. Nothing here is read by the build.

| File | Entries | Operations | Change-map entries |
|---|---:|---:|---|
| `asset.yaml` | 2 | 12 | C-BUS-11, C-BUS-12 |
| `carloan.s1a.yaml` | 2 | 6 | C-SCHED-01, C-SCHED-06 |
| `carloan.sc.yaml` | 1 | 1 | C-BUS-02 |
| `carloan.wording.yaml` | 1 | 1 | C-SCHED-07 |
| `dcprov.yaml` | 1 | 12 | C-CRED-12 |
| `dependent.dc.yaml` | 1 | 1 | C-PEOP-18 |
| `dependent.edu.yaml` | 3 | 36 | C-CRED-18+C-PEOP-16, C-CRED-20, C-PEOP-17 |
| `f1040.page1.yaml` | 1 | 5 | C-PRI-06 |
| `f1040.yaml` | 8 | 32 | C-PRI-01, C-PRI-02, C-PRI-18, C-PRI-08, C-PRI-04, C-PRI-03, C-PRI-07, C-PRI-05 |
| `f1095a.wording.yaml` | 1 | 8 | C-PEOP-02 |
| `f2441.wording.yaml` | 2 | 5 | C-CRED-13, C-CRED-14 |
| `f2441.yaml` | 3 | 40 | C-CRED-10, C-CRED-11, C-CRED-12 |
| `f4562.yaml` | 1 | 5 | C-BUS-11 |
| `f5329.yaml` | 3 | 15 | C-SCHED-11, C-PEOP-03, C-PEOP-04, C-PEOP-05 |
| `f5695.interview.yaml` | 1 | 28 | C-CRED-01 |
| `f5695.yaml` | 8 | 335 | C-CRED-01, C-CRED-02, C-CRED-03, C-CRED-04, C-CRED-05, C-CRED-06, C-CRED-07, C-CRED-08 |
| `f8863.wording.yaml` | 1 | 8 | C-CRED-17 |
| `f8863.yaml` | 1 | 7 | C-CRED-18 |
| `f8880.yaml` | 1 | 20 | C-CRED-16 |
| `f8889.wording.yaml` | 1 | 2 | C-PRI-21 |
| `f8889.yaml` | 3 | 40 | C-PRI-20, C-PRI-22, C-PRI-23 |
| `f8959.yaml` | 2 | 23 | C-SCHED-13, C-SCHED-15 |
| `f8960.wording.yaml` | 1 | 6 | C-SCHED-29 |
| `f8960.yaml` | 2 | 8 | C-SCHED-27, C-SCHED-28 |
| `f8962.yaml` | 3 | 17 | C-PEOP-12, C-PEOP-14, C-PEOP-27 |
| `f8995.yaml` | 1 | 12 | C-SCHED-31 |
| `f8995a.yaml` | 1 | 4 | C-SCHED-32 |
| `household.wording.yaml` | 1 | 5 | C-PEOP-01 |
| `ira.yaml` | 1 | 5 | C-PEOP-08 |
| `otjob.yaml` | 1 | 5 | C-SCHED-05 |
| `person.ambiguity.yaml` | 3 | 7 | C-CRED-18+C-PEOP-16, C-CRED-20, C-CRED-16 |
| `person.edu.yaml` | 3 | 39 | C-CRED-18+C-PEOP-16, C-CRED-20, C-PEOP-17 |
| `person.page1.yaml` | 1 | 2 | C-PRI-06 |
| `person.retirement.yaml` | 6 | 24 | C-SCHED-11, C-PEOP-03, C-PEOP-04, C-PEOP-05, C-PEOP-06, C-PEOP-08, C-PEOP-11 |
| `person.s1a.yaml` | 2 | 7 | C-SCHED-03, C-SCHED-05 |
| `person.sav.yaml` | 2 | 27 | C-CRED-16, C-PEOP-21 |
| `person.wording.yaml` | 4 | 11 | C-PEOP-01, C-PEOP-10, C-PEOP-19, C-PEOP-20 |
| `qbi.yaml` | 3 | 12 | C-SCHED-31, C-SCHED-32, C-SCHED-33 |
| `retirement.wording.yaml` | 1 | 2 | C-PEOP-07 |
| `retirement.yaml` | 4 | 24 | C-PEOP-04, C-PEOP-11, C-PEOP-05, C-PEOP-07 |
| `s1a.yaml` | 6 | 188 | C-SCHED-01, C-SCHED-02, C-SCHED-03, C-SCHED-04, C-SCHED-05, C-SCHED-08 |
| `s2.yaml` | 4 | 37 | C-SCHED-10, C-SCHED-11, C-PEOP-03, C-SCHED-13, C-PEOP-12 |
| `s3.yaml` | 2 | 12 | C-SCHED-12, C-SCHED-39 |
| `s3a.yaml` | 1 | 2 | C-PRI-05 |
| `s8812.yaml` | 7 | 20 | C-SCHED-16, C-SCHED-17, C-SCHED-18, C-SCHED-19, C-SCHED-20, C-SCHED-23, C-CRED-05, C-SCHED-26 |
| `sa.yaml` | 6 | 34 | C-PRI-14, C-PRI-16, C-PRI-17, C-PRI-15, C-PRI-18 |
| `sc.wording.yaml` | 3 | 10 | C-BUS-03, C-BUS-05, C-BUS-08 |
| `sc.yaml` | 4 | 28 | C-BUS-02, C-BUS-04, C-BUS-06, C-BUS-11 |
| `scope.credits.yaml` | 1 | 1 | C-SCHED-39 |
| `scope.wording.yaml` | 1 | 2 | C-PEOP-20 |
| `scveh.wording.yaml` | 1 | 8 | C-BUS-03 |
| `scveh.yaml` | 3 | 29 | C-BUS-01, C-BUS-02, C-BUS-12 |
| `tcw.yaml` | 1 | 3 | BUG-0647 |
| `tipjob.yaml` | 1 | 19 | C-SCHED-03 |
| `w2.yaml` | 1 | 4 | C-PRI-24 |

## Where they come from

The first entries express the proposals of `research/ty2026/forms-proposed/` (Form 1040, Schedule A, the Schedule C
vehicle lines, Form W-2 and the new Schedule 3-A), which stay there as the record of the preparation. The others were
written by the 2026 preparation lanes straight from the change map (`research/ty2026/changes.md`) against the 2025
forms as they stand, each with the entry's 2026 quotes as evidence (lane notes `docs/provisional/lanes/ty26-o*.md`
and `ty26-w1.md`, the wording-only entries); `tcw.yaml` carries a defect the parameter lane found rather than a
change-map entry (BUG-0647: the 2026 joint 12% bracket ends above the Tax Table's $100,000 boundary).

Each proposal was compared, line id by line id, with the 2025 file it was copied from (the blob its `.diff` names),
and every difference became an operation, grouped by the change-map entry it carries out. Every operation was then
applied to the 2025 forms as they stood, and those that no longer applied were mended (each entry concerned says so
in its `note`):

- `f1040.gate.nonitemizer_gifts` and `sa.gifts_total` read `sa.line11_if_gifts`, not `sa.line11`, and `sa.line14` is
  expected to read `sa.line11_if_gifts`: Schedule A line 11 has been gated since the proposal was written, and only
  its gate line may read a gated input.
- `sa.line8d` refuses on `sa.charity_limited_if_gifts`, as the other Schedule A lines held at zero now do.
- The questions the proposals left to adoption are written: `s3a.wants_benefit`, `w2.box12_tp`, `w2.box12_tt`,
  and `scveh.miles_business_h1` and `_h2`, which take the place of `scveh.miles_business` in the bank and the
  profiles. The Form 1062 election, first a question of its own (`f1040.form1062`), is asked by the Schedule 3
  questions `s3.farmland` and `s3.farmland_deferral` (C-PRI-04).
- The interview redraft: `f1040.line33` reads `f1040.line26_if_estimated` (line 26 is asked beneath
  `f1040.estimated_any`); the Schedule A screen `sa.unsupported` is a computed line over the questions it was taken
  apart into, so its label is re-based on it, mortgage insurance premiums (line 8d) are a new question
  `sa.mortgage_insurance` beneath the mortgage interest answer that makes it true, and the disaster rule for personal
  casualty losses is re-based on the help of `sd.casualty`.
- `s3a.line4` reads the 2026 Schedule 2 line 20, which the Schedule 2 renumbering (C-SCHED-10, `s2.yaml`) adds.

The operations read twelve parameters the 2025 file does not define (`niit.s68_threshold`, `qbi.min_active`,
`qbi.min_deduction`, `sa.gambling_rate`, `sa.gift_floor_rate`, `sa.limit_screen`, `sc.bonus_rate_phase_down`,
`sc.mileage_rate_h1`, `sc.mileage_rate_h2` and the new joint Tax Computation Worksheet row `tcw.mfj.b0.*`): the 2026
parameters must define them, and the staged `research/ty2026/params-2026.proposed.yaml` does. The ambiguity register
is changed by operations too: `amb.2026.gift_floor_base`, which `sa.gift_floor` and `sa.line13_ws` name, is added in
`sa.yaml` (C-PRI-15), and other entries are set or removed where their lines change (`f2441.yaml`, `f5695.yaml`,
`f8960.yaml`, `person.ambiguity.yaml`). Each new input's `add_question` carries its test-data `default` and `reason`,
which `tools/fixtures_year.py` writes to `fixtures/2026/defaults.json` at adoption. `f5695.interview.yaml` changes the
interview files beside the question bank's questions (the `full` profile's targets, the coverage rows, the gate
frequencies, the bank's tick-box groups and a persona) with the interview-file operations.

A form several lanes change may take split files, `<form>.<topic>.yaml`, each with `form: <form>`; they apply after
the form's own file (`tools/README.md`, "Year changes as operations").

## The 135 change-map entries by operation kind

Each entry of `research/ty2026/changes.md` by the operations it needs and what it needs outside them, read from the
entry's kind, touched ids and notes, before any operation was written. "Written" marks the 90 entries whose
operations are in this directory; the files, not this classification, say what the operations are (written against
the current forms, several entries classified "—" took citation or wording operations).

| Entry | Title | Operations | Outside the operations | Written |
|---|---|---|---|---|
| C-PRI-01 | Form 1040 line 12f: charitable contribution deduction for non-itemi... | add_line, set label, set expr | — | yes |
| C-PRI-02 | Form 1040 lines 13a and 13b exchange places; Schedule 1-A total mov... | set printed, set label, set cite | — | yes |
| C-PRI-03 | Form 1040 lines 24a, 24b and 24c: Form 1062 installment (new form) | add_line, set printed, set label, set expr | — | yes |
| C-PRI-04 | Form 1062: election to pay tax on a sale of qualified farmland prop... | add_line, add_question | — | yes |
| C-PRI-05 | Schedule 3-A and Form 1040 lines 32a to 32c: federal public benefit | add_line, set printed, set label, set expr, add_form, add_question | — | yes |
| C-PRI-06 | Form 1040 page 1: work-authorization question | add_line, add_question | — | yes |
| C-PRI-07 | Form 1040 line 28: the ACTC opt-out box is not printed | remove_line | — | yes |
| C-PRI-08 | Form 1040: labels reworded | set label | parameters/enums/tables | yes |
| C-PRI-09 | Form 1040: dates that move with the year | — | year literals |  |
| C-PRI-10 | Standard deduction, tax rate schedules and other Rev. Proc. amounts | — | parameters/enums/tables |  |
| C-PRI-11 | Schedule 1: sub-line numbers printed in full; line 14 reworded | set label | — |  |
| C-PRI-12 | Schedule 1: excess business loss threshold | — | parameters/enums/tables |  |
| C-PRI-13 | Schedule A line 5e: SALT limit and phase-down threshold | — | parameters/enums/tables |  |
| C-PRI-14 | Schedule A line 8d: mortgage insurance premiums return | add_line, set label, set expr, set cite | — | yes |
| C-PRI-15 | Schedule A lines 11 to 15: charitable contributions after the 0.5% ... | add_line, set printed, set label, set expr, set cite | parameters/enums/tables, ambiguity register | yes |
| C-PRI-16 | Schedule A line 16 (was 15): casualty losses include state-declared... | set printed, set label | — | yes |
| C-PRI-17 | Schedule A line 17 (was 16): other itemized deductions itemized by ... | add_line, set printed, set label, set expr, set cite | parameters/enums/tables | yes |
| C-PRI-18 | Schedule A line 18: total itemized deductions may be limited (2/37 ... | add_line, set printed, set label, set expr, set cite, set refuses | parameters/enums/tables | yes |
| C-PRI-19 | Schedule A: other lines reworded, quote unchanged | — | page moves |  |
| C-PRI-20 | Form 8889: 2026 HSA contribution limits | set cite | parameters/enums/tables | yes |
| C-PRI-21 | Form 8889: Schedule 2 line references renumbered | set label, set cite | — | yes |
| C-PRI-22 | HSA eligibility: bronze and catastrophic plans and direct primary care | set_question | — | yes |
| C-PRI-23 | HSA qualified medical expenses: definition rewritten | set cite, set_question | — | yes |
| C-PRI-24 | Form W-2 (final): new box 12 codes TP, TT and TA; box 14 split into... | add_line, add_question | — | yes |
| C-PRI-25 | Social security wage base: $184,500 | — | parameters/enums/tables |  |
| C-PRI-26 | Schedules B and D, Form 8949: no change beyond wording | — | no change |  |
| C-PRI-27 | Earned income credit amounts | — | parameters/enums/tables |  |
| C-PRI-28 | Enumerations whose citations moved | — | parameters/enums/tables |  |
| C-PRI-29 | Net investment income MAGI sentences: printed on the same page | set cite | — |  |
| C-SCHED-01 | Schedule 1-A renumbered; total moves to Form 1040 line 13a | set printed, set label, set cite | — | yes |
| C-SCHED-02 | Schedule 1-A dollar limits and rates unchanged (cited at new line n... | set cite | — | yes |
| C-SCHED-03 | Schedule 1-A Part II: employee tips entered per employer from W-2 b... | add_line, set expr, add_question | — | yes |
| C-SCHED-04 | Schedule 1-A Part II: trade-or-business tips entered per business w... | add_line, set expr, add_question | — | yes |
| C-SCHED-05 | Schedule 1-A Part III: overtime entered per employer from W-2 box 1... | add_line, set expr, add_question | parameters/enums/tables | yes |
| C-SCHED-06 | Schedule 1-A Part IV: Form 1098-VLI named; original-use and final-a... | add_line, add_question | — | yes |
| C-SCHED-07 | Schedule C interest on a Schedule 1-A vehicle loan: rule restated u... | set label, set cite | — | yes |
| C-SCHED-08 | Schedule 1-A Part V: birth-date cutoff moves to January 2, 1962 | — | year literals | yes |
| C-SCHED-09 | Schedule 1-A captions and Part III caution (wording) | — | no change |  |
| C-SCHED-10 | Schedule 2 laid out again: Part II split into Sections A–C; line 21... | add_line, remove_line, set printed, set label, set expr | — | yes |
| C-SCHED-11 | Form 5329 taxes split between Schedule 2 line 5 (early distribution... | set label, set expr | — | yes |
| C-SCHED-12 | Schedule 3: line 5a from Form 5695 line 3; line 5b "Reserved"; line... | remove_line, set label, set expr | — | yes |
| C-SCHED-13 | Form 8959 reordered: wages+RRTA total (line 12) to Schedule 2 line ... | set printed, set label, set expr | — | yes |
| C-SCHED-14 | Additional Medicare Tax thresholds unchanged | — | no change |  |
| C-SCHED-15 | Form 8959 instructions: dates and W-2 box 14a (wording) | set label | — | yes |
| C-SCHED-16 | Schedule 8812 line 1 reads Form 1040 line 11b | set label, set cite | — | yes |
| C-SCHED-17 | Schedule 8812 line 22 and Credit Limit Worksheet B line 8 read Sche... | set label, set cite | — | yes |
| C-SCHED-18 | Additional Medicare Tax and RRTA Tax Worksheet: Form 8959 line refe... | set label, set cite | — | yes |
| C-SCHED-19 | Schedule 8812 SSN and TIN requirements reworded | set cite | — | yes |
| C-SCHED-20 | Credit Limit Worksheet B: "Continued" heading reworded | set cite | — | yes |
| C-SCHED-21 | Schedule 8812 Part II-B routing sentence unchanged | — | no change |  |
| C-SCHED-22 | Additional Medicare Tax and RRTA Tax Worksheet: RRTA amounts from W... | — | no change |  |
| C-SCHED-23 | Credit Limit Worksheet A line 2 drops Schedule 3 line 5b; Worksheet... | set expr | — | yes |
| C-SCHED-24 | Schedule 8812 form cautions unchanged | — | no change |  |
| C-SCHED-25 | Schedule 8812 credit amounts unchanged | — | no change |  |
| C-SCHED-26 | ACTC refund limited to U.S. citizens, U.S. nationals and qualified ... | add_line, set refuses | — | yes |
| C-SCHED-27 | Form 8960: section 68 limitation worksheet for lines 9 and 10 | add_line, set expr | — | yes |
| C-SCHED-28 | Form 8960 line 7: Schedule 1 line 8j (rental at less than fair rent... | set expr | ambiguity register | yes |
| C-SCHED-29 | Form 8960 instructions: lines 1, 2, 5, 7 and 10 reworded (wording) | set cite | — | yes |
| C-SCHED-30 | QBI: Form 8995 threshold rises, with a separate married-filing-sepa... | — | parameters/enums/tables |  |
| C-SCHED-31 | Form 8995: new lines 15–17 (minimum deduction of $400) and 20 (ESBT... | add_line, set printed, set expr | — | yes |
| C-SCHED-32 | Form 8995-A Part IV: new lines 39–41 (minimum deduction) and 43 (ES... | add_line, set printed | — | yes |
| C-SCHED-33 | QBI: taxable income before the deduction uses Form 1040 lines 12e, ... | set expr | — | yes |
| C-SCHED-34 | Form 8995-A Part III: threshold and phase-in range (not encoded) | — | not encoded |  |
| C-SCHED-35 | QBI: qualified tips excluded from QBI (clarified) | — | not encoded |  |
| C-SCHED-36 | Form 4952 (final 2026): line 4g election text and other wording | set cite | year literals |  |
| C-SCHED-37 | Student loan repayment assistance text moved (p4681) | — | page moves |  |
| C-SCHED-38 | Form 1116 instructions: 2026 What's New and Reminders (election pat... | — | not encoded |  |
| C-SCHED-39 | Schedule 3: new line 13e (Form 1062 line 14) among other payments; ... | add_line, set expr | — | yes |
| C-CRED-01 | Form 5695 becomes a carryforward-only form | set_form | — | yes |
| C-CRED-02 | Part I current-year property costs (lines 1 to 11) removed | remove_line, remove_question | ambiguity register | yes |
| C-CRED-03 | Carryforward lines renumbered and rolled forward (2025 lines 12, 13... | set printed, set expr | — | yes |
| C-CRED-04 | Residential Clean Energy Credit Limit Worksheet now for line 2, wit... | set expr | — | yes |
| C-CRED-05 | Schedule 8812 Credit Limit Worksheets: "Form 5695, Part I" becomes ... | set label, set expr | ambiguity register | yes |
| C-CRED-06 | Part II, Section A (lines 17a to 20d, qualified energy efficiency i... | remove_line, remove_question | — | yes |
| C-CRED-07 | Part II, Section B (lines 21a to 29h, residential energy property e... | remove_line, remove_question | — | yes |
| C-CRED-08 | Part II totals, limit worksheet and statements (lines 30 to 32b) re... | remove_line, remove_question | — | yes |
| C-CRED-09 | Form 5695 year parameters: no 2026 value | — | parameters/enums/tables |  |
| C-CRED-10 | Child and dependent care credit percentage: 50% to 20%, with separa... | set expr | parameters/enums/tables | yes |
| C-CRED-11 | Dependent care exclusion limit $5,000 to $7,500 ($2,500 to $3,750 m... | — | parameters/enums/tables | yes |
| C-CRED-12 | Form 2441 Part I: columns (a) to (e) become lines 1a to 1e | set printed | — | yes |
| C-CRED-13 | Credit Limit Worksheet line 3: comma added | set cite | — | yes |
| C-CRED-14 | Qualifying person: disabled person's gross income test $5,200 to $5... | set label | parameters/enums/tables | yes |
| C-CRED-15 | Saver's credit AGI limits and line 9 bands re-indexed | — | parameters/enums/tables |  |
| C-CRED-16 | Form 8880 year roll (age cutoff, distribution testing period) and A... | — | year literals | yes |
| C-CRED-17 | Form 8863 lines 3 and 14 read Form 1040 line 11a instead of 11b | set label, set cite | — | yes |
| C-CRED-18 | Education credits: valid SSN required for the taxpayer and a depend... | add_line, set expr | — | yes |
| C-CRED-19 | Education credit MAGI limits and phaseout range unchanged | — | no change |  |
| C-CRED-20 | Form 1098-T request date moved for a weekend | — | year literals | yes |
| C-PEOP-01 | Form 1040 spouse name line: "If a joint return" | set cite | — | yes |
| C-PEOP-02 | Form 1095-A line 33: "Total" becomes "Add" | set cite | — | yes |
| C-PEOP-03 | Form 5329 taxes now go to Schedule 2 line 5 (early distributions) a... | set expr | — | yes |
| C-PEOP-04 | Form 1099-R box 7 becomes boxes 7a–7d (code in 7a, IRA/SEP/SIMPLE b... | add_line, set printed, add_question | parameters/enums/tables | yes |
| C-PEOP-05 | New early-distribution exception 24: qualified long-term care distr... | set expr | parameters/enums/tables | yes |
| C-PEOP-06 | Domestic abuse victim distribution cap $10,300 → $10,500 | — | parameters/enums/tables | yes |
| C-PEOP-07 | Birth-or-adoption and first-time-homebuyer sentences reworded | set cite | — | yes |
| C-PEOP-08 | IRA contribution limit $7,000/$8,000 → $7,500/$8,600; spousal compe... | — | parameters/enums/tables | yes |
| C-PEOP-09 | IRA deduction and Roth MAGI phase-outs for 2026 | — | parameters/enums/tables |  |
| C-PEOP-10 | Form 8606 line 2: "-0-" becomes "zero"; Total Basis Chart rows move... | set cite | year literals | yes |
| C-PEOP-11 | Trump accounts: a new kind of traditional IRA, excluded from Form 8... | add_line, set expr | parameters/enums/tables | yes |
| C-PEOP-12 | Repayment limitation on excess advance PTC eliminated; Form 8962 li... | remove_line, set expr | parameters/enums/tables | yes |
| C-PEOP-13 | Form 8962 lines 24 and 25 unchanged on the 2026 draft; the 2026 ins... | — | no change |  |
| C-PEOP-14 | Form 8962 line 6: household income above 400% of the poverty line e... | add_line, set expr | — | yes |
| C-PEOP-15 | 2026 applicable percentage table and the 2025 poverty guidelines | — | parameters/enums/tables |  |
| C-PEOP-16 | Education credits require a valid SSN (filer and dependent student)... | set expr | — | yes |
| C-PEOP-17 | Education items: the year changes and the line 24 question moves a ... | — | page moves, year literals | yes |
| C-PEOP-18 | Dependent care expenses: Form 2441 Part I columns become lines 1a–1... | — | page moves | yes |
| C-PEOP-19 | Form 8889 line 17b now routes to Schedule 2 line 13c | set label, set cite | — | yes |
| C-PEOP-20 | Elective deferral limit $23,500 → $24,500 (in the input question) | set label | parameters/enums/tables | yes |
| C-PEOP-21 | Form 8880: the ABLE and saver's-match notes move from "What's New" ... | — | page moves, year literals | yes |
| C-PEOP-22 | Pub. 575 / Pub. 590-B / i8889 sentences near pension, rollover and ... | — | page moves |  |
| C-PEOP-23 | Items waiting on the 2026 Instructions for Form 1040 (i1040gi not a... | — | waiting for a source |  |
| C-PEOP-24 | Items waiting on other unarchived 2026 editions (i4562, p970, p590a... | — | waiting for a source |  |
| C-PEOP-25 | Exclusions for qualified principal residence debt and student loan ... | — | not encoded |  |
| C-PEOP-26 | Below-100% lawfully present alien branch repealed (sec. 71302) | — | not encoded |  |
| C-PEOP-27 | No premium tax credit for a plan enrolled in during an income-based... | add_line, add_question | — | yes |
| C-BUS-01 | Business standard mileage rate: 72.5 cents to June 30, 76 cents fro... | add_line, remove_line, set label, set expr, set cite, add_question, remove_question | parameters/enums/tables | yes |
| C-BUS-02 | Schedule C line 16 split: new 16b "Vehicle loan", 16c "Other" | add_line, set label, set expr | — | yes |
| C-BUS-03 | Line 9 and line 20a vehicle text reworded ("business-use portion");... | set label, set cite | — | yes |
| C-BUS-04 | Business meals: new section 274(o) disallowance and a new list of f... | set expr | parameters/enums/tables | yes |
| C-BUS-05 | Line 24a incidental expenses: "telegrams" dropped | set label | — | yes |
| C-BUS-06 | Simplified method: storage space allowed only if the home is the so... | set label, set_question | — | yes |
| C-BUS-07 | Simplified Method Worksheet line 5: unchanged | — | no change |  |
| C-BUS-08 | The `sc.special` screen: items reworded, dropped or dated in 2026 | set label | — | yes |
| C-BUS-09 | Section 179 limits: $2,560,000, $4,090,000, SUV $32,000 | — | parameters/enums/tables |  |
| C-BUS-10 | Form 4562 Part I: note moved, years advanced | — | page moves, year literals |  |
| C-BUS-11 | Form 4562 Part II line 14 becomes 14a–14d; line 22 sum; Part VI mov... | add_line, set printed, set expr | — | yes |
| C-BUS-12 | Special depreciation allowance: 20% (not 40%) for property acquired... | — | parameters/enums/tables | yes |
| C-BUS-13 | Passenger automobile depreciation limits for vehicles placed in ser... | — | parameters/enums/tables |  |
| C-BUS-14 | Social security wage base $184,500 | — | parameters/enums/tables |  |
| C-BUS-15 | Schedule SE optional-method amounts and instructions rewording | — | not encoded |  |
| C-BUS-16 | Form 7206 line 2 long-term care premium limits | — | parameters/enums/tables |  |
| C-BUS-17 | Form 7206 and its instructions: years only; i1040gi cites unverifiable | — | year literals |  |
| C-BUS-18 | Schedule E, Form 8582, the K-1s and Form 6198: archived, not encoded | — | not encoded |  |
| C-LAW-01 | Hazardous duty areas: the Sinai Peninsula treatment made permanent;... | — | not encoded |  |
| C-LAW-02 | Alternative minimum tax: exemption amounts permanent, phase-out thr... | — | not encoded |  |
