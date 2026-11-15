# Lane land3-fix: BUG-0634 (Form 1095-A column B correction gate)

Agent: claude-opus-5-5, judgment; tax year 2025, jurisdiction us. Worktree `.claude/worktrees/land3-fix` (detached
snapshot 98f5c29d). Not committed. No paid review call and no model call from code.

## Is the defect real

Yes. It was checked against the source and the form.

- i8962 (2025) p. 14, Line 10, Missing or incorrect SLCSP premium: "If either of these two situations applies to you,
  or if you have reason to believe the Marketplace reported the wrong applicable SLCSP premium, you must determine the
  correct applicable SLCSP premium for every month. If the correct applicable SLCSP premium is not the same for every
  month of 2025, check “No”". Situation 1: "No APTC was paid for your coverage ... column B ... may be wrong, left
  blank, or reported as -0-". p. 15 repeats "reason to believe" for the months affected. i8962 p. 16 (Column (b),
  "Need to determine applicable SLCSP premium") names "or if no APTC was paid" too.
- `forms/2025/f1095a.yaml` before the fix: `f1095a.b_wrong` = any(`b_blank`, `b_changed`). On the route where months
  are the same (`same_months` Yes), a form with neither was taken as uniform. `b_fixed_same` was never asked, and
  `mo_b` took one amount for every month. The fixture `stage18.blind.p17` (no advance payments, uniform form,
  line 10 Yes) went down exactly this path.
- On the route where months differ, the defect does not change values: each month's column B is entered and may be
  corrected. That route is left as it was.

## The change

Form (`forms/2025/f1095a.yaml`):

- New input `f1095a.b_doubt` (gate): "Do you have any other reason to think column B shows the wrong amount for some
  month?" Cited to i8962 p. 14 (reason to believe; situation 1) and p. 15.
- New helper `f1095a.no_aptc`: `f1095a.c_total` (line 33, column C) equals 0. This is derived, not asked: the filer of
  a form that is the same every month enters line 33C in any case.
- New helper `f1095a.b_check`: any(`f1095a.b_wrong`, `f1095a.b_doubt`, `f1095a.no_aptc`), in that order, so line 33C
  is read only when no box is ticked.
- `f1095a.b_wrong_asked`: on `same_months` Yes it reads `b_check`; on No it reads `b_wrong` as before. Its label was
  extended.
- `f1095a.b_wrong` is unchanged.

Question bank (`interview/2025/questions.yaml`, order 197):

- New tick group `f1095a_col_b`, heading "Is any of these true of column B or your plan in 2025?". Its boxes:
  - `b_blank` (seq 3), "Column B is blank or zero in a month with coverage"
  - `b_changed` (seq 4), "Address, household or other coverage changed without telling the Marketplace"
  - `b_doubt` (seq 5), "Another reason to think column B is wrong"
- The help sentence "Answer Yes also if the Marketplace has told you column B is wrong" moved from `b_changed` to
  `b_doubt`. The new help of `b_doubt`: "For example, the Marketplace has told you column B is wrong, or its tax tool
  (HealthCare.gov/Tax-Tool) gives a different amount for some month."
- `c_total` moves from seq 12 to seq 6, before `b_fixed_same` (seq 5 to 7), because the no-APTC limb reads it.
- The help of `b_fixed_same` adds: "Where no advance payments were made (column C zero), column B may be wrong even
  when filled in."

Why not the adjudicator's single question ("no advance payments ..., or another reason ..."):

- it asks two subjects in one question (N1);
- column C is already entered, and asking about it again breaks N8.

Cost:

- A typical filer with a form that is the same every month and advance payments sees one question more, `b_doubt`, but
  one step fewer on the page. Walk of `marketplace.same_all_year`: same_months, the screen (three boxes), c_total, mo_a,
  mo_b, which is 5 steps against 6 before.
- Who could wrongly answer No to `b_doubt`: a filer who suspects column B but takes the printed amount as
  authoritative. The help names the tax tool as the check.
- No filer is asked about column C twice.

Other files:

- `fixtures/2025/defaults.json`: `f1095a.b_doubt` false ("Closed: the circumstance this question asks about does
  not apply unless the scenario says so.").
- `engine/src/generate.ts` and `tools/engines/generate_cases.py`: generated uniform forms state `b_doubt` false and
  `b_fixed_same` equal to the uniform draw, so a draw with zero column C keeps the annual route.
- `interview/2025/coverage/marketplace.yaml`:
  - set `column_b_right` adds `b_doubt` false;
  - new rows `marketplace.no_advance_payments` (line 33C zero asks `b_fixed_same`) and `marketplace.column_b_doubted`
    (`b_doubt` Yes asks `b_fixed_same`, line 33C not asked first).
- `bug_pending/land3-adj7-01.md`: the Fix, Fix lines, Siblings checked and Regression predictions fields.

Fixtures (no expected value edited):

- Answers restated where the new input is reached:
  - `b_doubt` false in 31 cases of the class M and mutation files, which take no defaults;
  - `b_fixed_same` true in six forms that are the same every month with line 33C zero, because their scenarios take
    column B as correct: `stage18.blind.p17`, `stage18.mut.below_100_no_advance`, `stage18.refuse.b_zero_uniform`,
    `classm.f8962.4`, and at first `classm.f8962.2.deepseek` and `classm.f5695.2.deepseek`.
- The two deepseek cases had no line 33C, which was never read before. It is now stated as the sum of the form's
  monthly column C (193,200 and 21,600 cents), and their added `b_fixed_same` was dropped because it is no longer
  reached.
- New case `stage18.reg.no_aptc_slcsp_by_month` in `fixtures/2025/f8962.json`, predicted by hand before evaluating:
  - facts: those of P17, no advance payments, the filer moved on July 1 and told the Marketplace, correct SLCSP $400
    for January to June and $300 for July to December;
  - predicted: line 10 No, line 8b $49, columns (e) $351 and $251, line 24 $3,612, line 25 0, line 26 $3,612,
    s3.line9 $3,612;
  - result: matched on all 20 values.

Year operations: `tools/year_changes.py --check` passes with no new entry (no 2026 operation touches these lines), so
no mapping was added.

## Verification (run in this worktree, after the last edit to forms, bank and fixtures)

| Command | Result |
|---|---|
| `npm run compile --silent && node engine/dist/main.js build && node engine/dist/main.js render` | build OK; 68 rendered files |
| `node engine/dist/main.js test-fixtures` | 1987/1987 (baseline 1986/1986, plus the new case) |
| `node engine/dist/main.js test-fixtures --ny` | 357/357 |
| `python3 tools/citations.py --strict` | 0 findings |
| `python3 tools/check_consumers.py` | 0 new |
| `python3 tools/transcription/check_questions.py` | 0 new |
| `python3 tools/transcription/check_screens.py` | 0 new |
| `python3 tools/transcription/check_false_no.py` | exit 1: 1 new, `gate:clcw_next_year.final_ask#1` (FALSE_NO verdict unruled). Not this change: no clcw_next_year file was touched. Inferred to predate it; not rerun on the untouched tree |
| `python3 tools/siblings.py --check` | this entry passes. Still failing: three other pending entries (land3-adj5-01, land3-adj5-02, land3-adj6-01: Fix with no Fix lines) |
| `python3 tools/check_bug_inventory.py` | exit 1, as at baseline (missing landing-09 to 13 pending files), plus one new line: `bug_pending/land3-adj7-01.md: a committed pending entry was changed or removed`. The brief asked for the entry's fields to be filled in, and the check treats committed pending entries as append-only (replaced only by `tools/new_bug.py --assign` at a merge). Needs the coordinator's decision |
| `node engine/dist/main.js interview-rules` | 0 problems (177 walks) |
| `node engine/dist/main.js tick-groups` | passed, 0 problems. The new group lies behind a Form 1095-A, which the background return does not have, so the tool reports it "not checked here". The screen was not seen in a browser |
| `node engine/dist/main.js interview-coverage --write` | 0 problems; 496 rows, the two new ones included |
| `python3 tools/year_changes.py --check` | all 90 operations apply |

## Review dry run

`python3 tools/transcription/rerun_all.py --dry-run --kinds transcription,render,classm --forms f1095a,f8962 --model claude-opus-5-5`:

- 4 jobs, total $3.56, which is above the $3.00 gate and needs `--approve-cost`:
  - classm f1095a (whole), $0.81
  - classm f8962 (whole), $2.13
  - render f1095a (line-scoped), $0.20
  - transcription f1095a (line-scoped), $0.41
- Render and transcription of f8962 are not rerun: their logs already answer the current subject.
- No job was run.

## Left open

- Residual, not fixed: the monthly column B questions (`f1095a.in_b_*`) and `f1095a.mo_b` give a move or an unreported
  change as the example of a wrong column B and do not say that, with no advance payments, column B may be wrong. On
  the route where months differ, a filer with no advance payments is not told to check column B.
- Reading kept: "no APTC was paid for your coverage" is read per policy (this form's line 33C). The per-return reading
  fires on a subset of the same forms. The per-policy reading only asks `b_fixed_same` more often, and a Yes leaves
  every value as it was, so no ambiguity entry was added.
- Reviews due: those in the dry run above, plus a question review of `b_doubt` and the changed help, and the screen
  and false-no reviews of the new gate `b_doubt` at the next sample.
