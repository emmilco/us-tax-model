# Lane land3-adj5: transcription adjudication, landing round (2026-11-14)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Adjudicated every open disagreement in the Claude
transcription logs of 22 forms: 69 lines in all. Four sub-lanes (opus forks) split the forms. Rulings were applied with
`tools/transcription/rule.py`; the rulings JSON is in `/tmp/land3-adj5/<form>.json`. Each form's adjudication summary
(`reviews/2025/transcription/adjudication/<form>.md`) has a `## Landing round (2026-11-14)` section with the per-line
table. `qbi.md` and `sli.md` are new.

Check: `check_logs.py` reports no "open ruling(s) in the transcription log" for any of the 22 forms, and no
`Ruling: open` remains in their logs. The same run still reports render, class M and stale-subject items on these
forms. Those were outside this lane and were left alone.

## Counts by form

| form | model error | representation | scope | finding |
|---|---|---|---|---|
| f2441 | 0 | 4 | 3 | 1 (low) |
| s8812 | 2 | 0 | 0 | 0 |
| f8863 | 1 | 0 | 0 | 0 |
| s2 | 1 | 0 | 0 | 0 |
| refund | 0 | 2 | 0 | 0 |
| f1040 | 0 | 1 | 0 | 0 |
| sa | 0 | 7 | 0 | 1 (low) |
| s1a | 0 | 4 | 0 | 0 |
| sales | 0 | 1 | 0 | 0 |
| f4952 | 1 | 3 | 0 | 0 |
| s1 | 0 | 4 | 0 | 0 |
| s3 | 0 | 7 | 0 | 0 |
| scope | 3 | 1 | 0 | 0 |
| household | 2 | 1 | 3 | 0 |
| qbi | 0 | 3 | 0 | 0 |
| sc | 2 | 1 | 0 | 0 |
| s179 | 0 | 2 | 0 | 0 |
| carloan | 1 | 0 | 0 | 0 |
| div | 0 | 2 | 0 | 0 |
| ftc | 1 | 1 | 0 | 0 |
| sli | 1 | 1 | 0 | 0 |
| ssb | 0 | 1 | 0 | 0 |
| **total** | **15** | **46** | **6** | **2** |

The representation count includes the lines ruled as plain equivalence (qbi carryforward, sc 40, s1 2a).

Household was ruled on the source and the YAML alone. `triage.py --form household` refuses because an earlier pass
names the renamed line `household.widowed_2025`, and the triage JSON on disk predates the redraft. Each household
ruling says so.

## Most common pattern

Most representation rulings follow one pattern. The reply reads an amount directly. The redraft reads the same amount
through its plain-language parent question, or puts the refusal on a different line. Triage then shows differences
only on refused or incomplete returns (project-unknown or project-refuses), with no value difference.

## Findings

- **BUG-0631 (low), f2441 line 18** (`bug_pending/land3-adj5-01.md`).
  - Problem: no printed Part III line (12 to 31) has a `shown_when`. On a return with care expenses and no dependent
    care benefits, lines 18 and 19 still show earned income. Form 2441 Part I says: "No. Complete only Part II
    below."
  - Fix: in `forms/2025/f2441.yaml`, add `shown_when: f2441.benefits` to `f2441.line12` through `f2441.line31`,
    leaving the expressions unchanged. Then check the readers of lines 26 and 31.
  - Not verified on a rendered values sheet. The claim rests on `engine/src/classm.ts`, which treats only a line
    whose `shown_when` is false as no form value. `f2441.yaml` has no `shown_when` at all.
- **BUG-0632 (low), sa line 5a** (`bug_pending/land3-adj5-02.md`).
  - Problem: `sa.line5a`'s label and source still describe the whole state and local income tax total. The redraft
    splits that total into W-2 withholding (`sa.line5a`) plus `sa.state_tax_other`. Read as written, the two
    double-count. The interview's return is right; only the declared text is wrong.
  - Fix: in `forms/2025/sa.yaml`:
    - Change the `sa.line5a` label and source to the W-2 boxes 17 and 19 withholding only.
    - Move the estimated-payment, prior-year, fund, tax-credit and territory paragraphs into the source of
      `sa.state_tax_other`.
    - Change the `sa.state_tax_any` wording to ask whether state or local income tax was taken out of pay.
    - Rerun the line 5a transcription review.

## Model errors and scope rulings that matter for later reviews

- **scope.schedule1, scope.other_income, scope.other_line16** (model error): the reply drops screened items that other
  forms rely on to refuse (for example the CFC question, which reaches a section 962 election).
- **s2.other** (model error): the reply drops household employment taxes and W-2 box 12 codes A, B, M and N, which the
  label names.
- **s8812 18a and (CLW B 3)** (model error): the reply refuses self-employment earnings, which the Earned Income
  Worksheet adds on lines 2a to 2e.
- **f8863 7** (model error): the reply's display condition leaves out the "claimed as a dependent" bar.
- **f4952.required** (model error): the reply applies the p. 3 Exception to a filer who elects on line 4g.
- **carloan 22(ii)** (model error): the reply does not prorate the interest.
- **ftc.credit** (model error): the reply drops Schedule 2 line 1z from the limit.
- **sli.deduction** (model error): the reply drops the "not claimed as a dependent" condition.
- **sc.line31_pre179 and sc 5** (model error): both readings are circular.
- **household.married and household.widowed_this_year** (model error): the reply mishandles a spouse who died in 2025.
- **f2441 5, 19 and 30** (scope): the reply computes cases the project refuses. These are the surviving spouse's
  choice under p503 p. 11, the separate-return line 19 rule (which `s3.mfs` refuses), and employer-furnished care.
- **household.roster_bad, hoh_fails and filing_status_conflict** (scope): the project carries extra refusals.

## Corrections recorded in summaries, not in the logs

- **Three citation slips in the applied sa ruling texts.** The rulings were applied with these errors; the corrections
  are in the sa summary:
  - The itemize quote actually reads "your federal income tax will be less".
  - i1040sca Line 5b is on p. 6, not p. 4.
  - The gambling-loss rule is on p. 11, not p. 12.
- **One misquote in a pending bug file, fixed by hand.** `bug_pending/land3-adj5-02.md` had a misquote in its Source
  field, corrected after `new_bug.py` created the file: "withheld from your salary".

## Open

None.
