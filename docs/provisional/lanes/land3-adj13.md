# Lane land3-adj13: class M adjudication (person, s179, sli, f1095a, f2441, f8889)

Agent: claude-opus-5-5, judgment; tax year 2025, jurisdiction us. Worktree `.claude/worktrees/landing`. Not committed. No
paid review and no model call from code. Only the Claude class M logs were ruled. The transcription and render logs were
not touched.

`carry.py --kind classm` ruled nothing on any of the six forms. All 23 open lines were ruled by hand and applied with
`rule.py --kind classm`. Each one drops the model value from `fixtures/2025/classm.json` because the project's value is
retained. Rulings files are in `/tmp/land3-adj13/<form>.json`. Each form's summary is under "Landing round (2026-11-14),
class M" in `reviews/2025/transcription/adjudication/<form>.md`.

## Counts

| form | model error | ambiguity | representation | finding |
| --- | --- | --- | --- | --- |
| person | 10 | | | |
| s179 | | 4 | | |
| sli | | | 3 | |
| f1095a | 2 | | | |
| f2441 | 1 | | | |
| f8889 | | 3 | | |

Findings: none. Pending bugs: none. Left open: none.

## Grounds

- **person, `wages`, 10 lines (cases 7 x2, 8, 9, 10, 12, 13, 15, 16, 22).** `person.wages` sums `w2.wages`, which is W-2
  box 3 plus box 7 (iw2w3 p. 18; amb.2025.ss_wages). The prompt gives that sum as $0.00 on each W-2, and the model summed
  box 1 instead. This is the same pattern as the earlier rulings on this line.
- **s179, line 1 of case 3 and line 5 of cases 1, 3 and 4.** The model used the optional Worksheet 1, which takes line 1
  as the smaller of the 2025 cost and $2,500,000. That is the reading amb.2025.s179_carryover_no_property did not choose
  (owner, T-043). On the separate return in case 4, line 5 is 50% of $2,500,000. Lines 9, 12 and 13 agree in every case.
- **sli, case 3, lines 1, 8 and 9.** The filer is claimed as a dependent. The model wrote that bar into worksheet line 1.
  The project figures the worksheet as printed and applies the bar in `sli.eligible`. Running the engine on the case gives
  `s1.line21` $0.00, so the deduction is the same as the model's. This follows the earlier ruling on classm.sli.2.
- **f1095a, case 3, `b_check` and `b_wrong_asked`.** The case has `same_months` yes and `b_fixed_same` no, so the monthly
  column B amounts ($400 then $300) are the corrected amounts. Line 33C is $0, and i8962 p. 14, situation 1 says that
  with no APTC, column B "may be wrong". So `b_check` is yes, and on this route `b_wrong_asked` reads it. The model ignored
  the filer's months answer. The fix to the column-B test made in this round (land3-fix) gives the right value here.
- **f2441, case 1, line 30.** The model added column (d) without leaving out the $1,000 of line 28 benefits. Under either
  reading of amb.2025.dc_line30 the result is $19,500 - $1,000 = $18,500. Line 31 agrees.
- **f8889, case 4, spouse lines 7, 8 and 12.** The spouse was born in 1950 and had 12 eligible months, 10 of them with
  family coverage. The owner's reading of amb.2025.hsa_line7_months counts every eligible month, so line 7 is $1,000. The
  model counted only the family months and got $833.33. Lines 8 and 12 follow from line 7.

## Observations (not findings)

- In every person class M case taken from a stage fixture, W-2 box 3 is zero while box 4 is 6.2% of box 1. The zero is a
  test-data default. As a result, only classm.person.14 exercises the excess social security credit.
- The f1095a class M prompt labels the monthly column B entries only "column B (monthly SLCSP premium)". It does not show
  the input's source text, which says the entry is the corrected amount when column B is wrong. That label invited the
  model's misreading.

## Verification

- After applying, `rule.py` reported "open rulings remaining: 0" for each form.
- `grep -c 'Ruling: open'` returns 0 on all six class M logs.
- The fixture's `evidence_note` records each dropped line.
- `tools/transcription/check_logs.py` did not run here. It refuses with "stale build: canonical/ is older than
  forms/2025/sa.yaml" because another lane edited sa.yaml at 21:55, after the 21:53 build. The brief says not to rebuild.
  The check should be rerun after the next build.
