# Lane land3-adj7: render adjudication (landing, 2026-11-14)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Scope: the open rulings of the Claude render logs
(`.transcription/logs/2025/render/<form>.md`) of clcw_next_year, div, f1095a, f2441, f8889, f8962, f8995, ftc, g28,
household, ira, refund, s1a, scveh, u1250: 17 lines, all ruled with `tools/transcription/rule.py --kind render`.
No paid review, no model call, no change to forms, questions, fixtures, params or tools. There are no render
adjudication summaries under `reviews/2025/render/`, so each form's round is a "Landing round (2026-11-14), render"
section in `reviews/2025/transcription/adjudication/<form>.md` (f8995.md is new).

## Counts by form

| form | rulings |
| --- | --- |
| clcw_next_year | interface gap 1 |
| div | ambiguity 1 |
| f1095a | finding 1 (medium) |
| f2441 | scope 1 |
| f8889 | ambiguity 1 |
| f8962 | scope 2 |
| f8995 | scope 1 |
| ftc | scope 1 |
| g28 | scope 1 |
| household | scope 2 |
| ira | interface gap 1 |
| refund | ambiguity and scope 1 |
| s1a | scope 1 |
| scveh | scope 1 |
| u1250 | scope 1 |

Totals: scope 11, ambiguity 2, ambiguity and scope 1, interface gap 2, finding 1.

## Findings

- **BUG-0634 (medium), f1095a line b_wrong.** The gate tests only blank or zero column B
  (f1095a.b_blank) and an unreported change (f1095a.b_changed). It leaves out i8962 p. 14 situation 1 ("If no APTC
  was paid ... column B ... may be wrong") and "if you have reason to believe the Marketplace reported the wrong
  applicable SLCSP premium". So when Part III is the same every month, the form is taken as uniform without asking
  f1095a.b_fixed_same, and f1095a.mo_b takes the corrected premium as one amount that is the same every month. A
  correct premium that differs by month cannot be entered, and line 10 comes out Yes where the instructions say No.
  Proposed fix: add the input f1095a.b_doubt, "Were no advance payments of the premium tax credit made for this
  policy (column C blank or zero every month), or do you have another reason to believe column B shows the wrong
  amount?", as a third limb of f1095a.b_wrong's `any`. Relabel b_wrong "Column B of this Form 1095-A may need
  correcting (blank or zero in a covered month, an unreported change, no advance payments, or another reason to
  believe it wrong)". Place the question after f1095a.b_changed under the interview construction protocol. Pending
  file: `bug_pending/land3-adj7-01.md`.

## Notes

- The refusals that earlier rounds cited were checked against the redraft. Where they moved, the rulings name the
  current gates: Schedule K-1 is now refused through scope.k1 in scope.schedule1 rather than sd.other_forms; Form
  2439 through sd.f2439 in sd.other_forms; the refund exceptions through refund.not_prior_year; the Form 1099-R lump
  sum through retirement.lump_sum_if_born_before_averaging_date in retirement.special.
- ira (screen): the 2-year repayment window in Pub. 590-A p. 9 means every 2025 repayer served after the start of
  2022, so the armed-forces gate loses nothing.
- No line is left open. check_logs shows no "open ruling(s) in the render log" for these forms. Other messages for
  them belong to other lanes: an open transcription ruling on scveh, and stale class M logs.
