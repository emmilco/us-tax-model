# Lane b1-adj-a: adjudication, B1 round 2

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Forms: s1, sa, sales, sd, sb, f4952.
Worktree `.claude/worktrees/nx-b1`. Rulings files `/tmp/b1-adj-a/<form>.json` (transcription) and
`/tmp/b1-adj-a/render/<form>.json` (render), applied with `tools/transcription/rule.py`. Summaries appended to
`reviews/2025/transcription/adjudication/<form>.md` ("Goal-1 round (2026-11-15)"). Deepseek logs dormant, not ruled.

## Rulings

| form | kind | lines | classes |
| --- | --- | --- | --- |
| s1 | transcription | 8c | representation 1 |
| s1 | render | 8r | finding 1 (medium) |
| sa | transcription | sa.itemizes, sa.deduction, 8a, 16 | representation 4 |
| sa | render | 8a, 6, 15, 16 | scope 4 (refusal located elsewhere) |
| sales | transcription | (g) | model error 1 |
| sales | render | (g) | scope 1 |
| sd | transcription | 1a–10 columns (d)(e)(g)(h) (32), sd.f2439_if_dividends, sd.filed | scope 32, representation 1, model error 1 |
| sd | render | 5, 12 | scope 2 |
| sb | transcription | 6 | representation 1 |
| sb | render | 8 | finding 1 (low) |
| f4952 | transcription | f4952.required, 2, 8 | model error 1, representation 2 |
| f4952 | render | none open | - |

Class M (sd, sb): not ruled. The coordinator held all class M rule.py and carry.py runs (fixtures/2025/classm.json
being restored); no class M log of these forms had an open line when checked.

## Findings

- **BUG-0758** (medium; `bug_pending/b1-adj-a-01.md`). s1 line 8r: `s1.scholarship_taxable` asks for
  pay for "teaching, research or other services required as a condition for receiving the grant", but p525 p. 35,
  Exceptions, excludes that pay under the National Health Service Corps Scholarship Program, the Armed Forces Health
  Professions Scholarship and Financial Assistance Program and work-college work-learning-service programs. Fix:
  forms/2025/s1.yaml `s1.scholarship_taxable` source, after "required as a condition for receiving the grant", add
  " (but not service pay under the National Health Service Corps Scholarship Program, the Armed Forces Health
  Professions Scholarship and Financial Assistance Program, or a work college’s comprehensive student
  work-learning-service program)"; cite p525 p. 35, Exceptions; interview/2025/questions.yaml help adds "Leave out
  service pay under the National Health Service Corps or Armed Forces Health Professions scholarship programs or a
  work college’s work-learning program." Wording only. This disagrees with BUG-0716's reasoning that those
  obligations are not "teaching or research": the wording also says "other services".
- **BUG-0759** (low; `bug_pending/b1-adj-a-02.md`). sb line 8: the label and source add indirect
  receipt, free or below-market use of trust property, and foreign foundations or waqfs counting as trusts. No
  archived page supports these clauses (they follow the Form 3520 rules). Fix: archive the 2025 i3520 and cite its
  passages in `sb.line8`, or drop any clause it does not support. Each clause only widens a Yes that refuses, so no
  value changes.

## Notes

- sd transcription: the 32 column lines are the landing round's scope pattern (digital boxes G–L, refused by
  sales.one, T-003). The new `sd.qof` screen shows up only as more project-unknown/refuses. No value differs.
- sd.filed and f4952.required are value-differing model errors with the same witnesses as earlier rounds
  (carryover with no carryover amount; the line 4g election left out).
- Verification: `tools/transcription/check_logs.py`, filtered to these forms. Result in the report.
