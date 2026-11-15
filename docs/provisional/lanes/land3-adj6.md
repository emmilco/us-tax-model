# Lane land3-adj6: adjudication of person, scveh and ira (landing round, 2026-11-14)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. The lane made no model calls and no paid reviews.

## What was ruled

These are the open disagreements in the Claude transcription logs (`.transcription/logs/2025/transcription/<form>.md`)
after the line-scoped reruns that followed the `(screen) (<id>)` keying fix (`land3-screen.md`):

- person, pass 1b9b7f0d8800: 29 open lines;
- scveh, pass b03568771f62: 23 open lines;
- ira, pass 12f36e046fb1: 5 open lines.

For person and ira the triage record was older than the log, so `triage.py` and then `carry.py` were run. Carry ruled
nothing. All 57 lines were ruled with `tools/transcription/rule.py`. The rulings files are
`/tmp/land3-adj6/{person,scveh,ira}.json`. Each form's summary has a "Landing round (2026-11-14)" section in
`reviews/2025/transcription/adjudication/<form>.md`. `check_logs.py` now reports no open transcription ruling for these
three forms.

## Counts

| form | ambiguity | representation | model error | finding | open |
| --- | --- | --- | --- | --- | --- |
| person | 0 | 19 | 10 | 0 | 0 |
| scveh | 15 | 2 | 4 | 2 | 0 |
| ira | 0 | 1 | 4 | 0 | 0 |

## Evidence

- The executable triage record of each pass (`.transcription/triage/2025/<form>.json`, executable-triage-v2; 1,986
  fixtures, 500 generated returns, seed 20261026).
- `triage.py --explain` derivations where a ruling cites one.
- A scratch rerun of the same evaluator with the witness cap lifted (`/tmp/land3-adj6/triage/`). It was used to check the
  "every value record" statements, and they all held. The records it checked:
  - person.sav_ineligible: 22/22 records have `sa.dependent` false and `person.sav_claimed` supplied as true.
  - person.sav_line2: 61/61 records have no Schedule C.
  - person.ira_line7: 49/49 records have no traditional contribution.
  - (screen) (scveh.smr_ok): 3,380/3,380 records have `smr_always` Yes and `smr_first` unasked.
  - (screen) (scveh.screen): 83/83 records have the project false and the reply true.
  - person.senior_work_ssn: 113/113 records are spouse rows.
  - person.age55_at_year_end_if_open_year: 616/616 records have the project false and the reply true.
- An engine evaluation of `stage14.veh.2025_179_over_line9`, used for the finding.
- The archived sources (`sources/2025/`).
- Triage applies the project's `shown_when` only, not the reply's. So the reply's own display conditions were ruled by
  reading its expressions. This matters for scveh lines 11, 15, 17 and 18, whose candidate-shows-skipped counts include
  records that the reply's own condition hides.

## Finding

**BUG-0633** (low), on scveh lines 15 and 18 (`bug_pending/land3-adj6-01.md`).

Pub. 946's Depreciation Worksheet for Passenger Automobiles says "If line 10 is equal to line 9, stop here" and "If line
16 is equal to line 11, stop here". The project shows worksheet lines 13 to 16, 18 and 19 for every owned vehicle on
actual expenses, so a passenger automobile that stops still shows nonzero amounts. The evaluated example is
`stage14.veh.2025_179_over_line9`: line 10 = line 9 = $12,200, yet the project shows line 13 $90,000, line 14 $12,200,
line 15 $77,800, line 18 $77,800 and line 19 $15,560. No later amount changes.

Fix (`forms/2025/scveh.yaml`):

- Add helper `scveh.part2_reached` = `is_actual_owned` and not (`on_auto_limits` and `line10 >= line9w`).
- Add helper `scveh.part3_reached` = `part2_reached` and not (`on_auto_limits` and `line16 >= line11`).
- Set `shown_when: scveh.part2_reached` on `bus_cost` (13), `line14`, `line15` and `line16`.
- Set `shown_when: scveh.part3_reached` on `line18` and `line19`.
- Leave the expressions unchanged. Line 15 still feeds the mid-quarter bases.
- Add regressions for both stop notes.

## Model errors (reply)

- **person.s16 and person.ira_se.** The reply keys the SIMPLE catch-up on `person.simple_age_at_year_end`, which only a
  person born in 1962 or 1966 answers. On `stage14.simple.nonelective_60` (born 1965) this gives $21,108.20 against
  $22,858.20, and line 9 $34,652.93 against $32,902.93.
- **person.age55_at_year_end_if_open_year.** The reply computes the whole age-55 test, but the gate holds only the answer
  of a person born in 1971. There are 65 completed value records.
- **person.senior_work_ssn.** The reply restricts the line to the taxpayer, so `s1a.senior_count` drops a qualifying
  spouse.
- **(screen) (person.sav_excess) and (screen) (person.ira_excess).** The reply redefines the screens: sav_excess as an IRA
  excess, and ira_excess as item 10 computed from the worksheet.
- **person lines 27 to 30.** The reply gives no American opportunity credit for a student whose ITIN was applied for by
  the due date, contrary to p970 p. 11 and owner decision T-113 (`f1.t113.person_aoc_itin_applied`: $0 against $4,000 on
  line 27).
- **ira.over_comp.** The reply transcribes the line 10 caution, which the project carries on `ira.kbh_short`, without the
  traditional-contribution condition.
- **ira.special_gate and ira.line20.** These have no contribution condition.
- **(screen) (ira.special).** The reply drops the reservist repayment and adds `ira.se_capital`.
- **scveh lines 7, 9 (line9w), 11 and 17.** The reply shows the passenger-automobile limit lines for vehicles that are
  not passenger automobiles.

## Ambiguity (scveh)

The reply rounds the business-use ratio to four places. The owner's ruling `amb.2025.vehicle_business_pct` sets six
places, so values differ by cents. The other kinds on these lines come from the reply's screen, ruled representation.

## Representation (highlights)

- **Birth-year derivation.** The reply reads `person.born_jan1` where the interview asks the at-year-end question of the
  cut year.
- **Unasked answers.** The reply reads several inputs without their parent questions:
  - `person.sav_claimed` without `sa.dependent`;
  - `person.plan` without a Schedule C;
  - `scveh.smr_first` when `smr_always` is Yes;
  - `scveh.bonus_same` with no allowance claimed.
- **Screen items refused elsewhere.** Some items of the scveh screen are refused at another line by the project.

## Corrections to ruling text already applied

`rule.py` rules only open sections, so these were not rewritten in the logs. The class of each line stands.

- **ira.over_comp.** The ruling quotes witness counts ("12 value records ... 6 candidate-refuses, 6 candidate-unknown, 6
  project-unknown"). The totals are 17 value, 13 candidate-refuses, 6 candidate-unknown, 9 project-unknown and 2
  project-refuses, with 7 value records on completed returns. In 16 of the 17 value records the reply refuses a joint
  return that has no traditional contribution. In the other one the project's excess-contribution screen fires and the
  reply's does not.
- **(screen) (ira.special).** The ruling says "all 28 differences are candidate-unknown". In fact 26 are candidate-unknown
  and 2 are value records:
  - `stage16.refuse.ira.se_capital`: project false, reply true;
  - `mutation.m1.ira.special_reservist`: project true, reply false.

  Both confirm the model error.

The adjudication summaries carry the triage totals.
