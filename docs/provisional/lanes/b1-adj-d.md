# Lane b1-adj-d: adjudication of s2, s3, household, eic, f5695 (goal-1 B1, round 2)

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Worktree nx-b1 (uncommitted B1 merge).
Rulings files in `/tmp/b1-adj-d/`, applied with `tools/transcription/rule.py`; summaries appended to
`reviews/2025/transcription/adjudication/<form>.md` under "Goal-1 round (2026-11-15)".

## Rulings

| form | kind | lines | classes |
| --- | --- | --- | --- |
| s2 | transcription | s2.other, 2 | model error 1 (s2.other), scope 1 (2) |
| s3 | transcription | s3.adoption_if_any, s3.prior_amt_if_forms, s3.other_credit | interface gap 2, representation 1 |
| s3 | render | 7 | finding 1 (low) |
| household | transcription | household.marriage_possible, household.hoh_fails | representation 2 |
| eic | transcription | 16 lines | model error 14, representation 1 (eic.check_27c), scope 1 ((Step 5, 2)) |
| f5695 | transcription | 5b, 6a | representation 2 |

Notes:

- eic: the reply's eic.eligible refuses on household.eic_disallowed_claim, which reads household.eic_claimed and so
  eic.eligible: a cycle (825 completed returns unknown; eic.credit inherits it). The worksheet lines repeat the landing
  round's defect (shown_when splits Worksheet A from B by Schedule C but tests no Step 1-4 STOP).
- household: the triage record predates this reply (pass de16cc0a21be is not in it), so both lines were ruled by
  reading the reply against the YAML and the sources; triage was not rerun (outside this lane's files).
- s3.adoption_if_any and s3.prior_amt_if_forms: the prompt gives only the ids; the reply's own helpers
  (s3.h_adoption_now, s3.h_prior_amt_credit) equal the project's gates after BUG-0733, so interface gap.

## Findings

- **BUG-0761** (low; `bug_pending/b1-adj-d-01.md`), s3 render line 7: no refusal on `s3.line7` names Form
  8978 (line 6l); the return is refused at Form 1040 line 16 through `scope.other_line16`, so no value is wrong, but the
  line's note says every line 6 situation is refused there. Fix: add to `s3.line7` refuses `when:
  scope.f8978_if_business_before`, form "Form 8978 (partner's additional reporting year tax)", with a remedy and cite
  (i1040gi Line 16, "Tax from Form 8978, line 14"; f1040s3 line 6l). The landing round's render ruling filed this under
  BUG-0620 (6), which BUG-0733 closed without line 6l.

## Left open

- Class M: none ruled. The s2 and s3 class M logs had no open lines when read, and the coordinator held all class M
  rulings and carry runs while fixtures/2025/classm.json is restored (s2 and s3 class M due about 17:00).
