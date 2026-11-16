# Lane xadj-b: round-2 adjudication of f1040, s1, s1a, oi8z, sli, sa

Model: claude-opus-5-5 · Class: judgment · Year: 2025 · Jurisdiction: us · Worktree: `.claude/worktrees/xint`
(coverage-expansion merge, uncommitted). Fork of lane xadj. No form edits, no paid review run by this lane, no commit.
Rulings files: `/tmp/xadj/b/<form>.<kind>.json`, applied with `tools/transcription/rule.py`. Summaries appended to
`reviews/2025/transcription/adjudication/<form>.md` (sections "Goal-1 coverage-expansion round (2026-11-15)" and
", render"; `oi8z.md` is new).

## Findings (pending bugs, `bug_pending/xadj-b-NN.md`)

| id | severity | where | proposed change |
| --- | --- | --- | --- |
| BUG-0766 | medium | f1040.line1a; s1.inmate_wages / s1.inmate_amount | x2-s1o computes Schedule 1 line 8u, so inmate pay shown in W-2 box 1 is no longer kept off line 1a (i1040gi p. 23, "Do not report these wages on line 1a"): double count with 8u, or EIC earned income that p596 excludes. Either refuse "inmate pay on a W-2" at f1040.line1a, or ask that W-2 part and subtract it from line 1a while s1.inmate_amount includes it. |
| BUG-0767 | medium | sa.dep_earned_sum; amb.2025.sa_dep_earned | Standard Deduction Worksheet for Dependents earned income omits Schedule 1 line 8u (i1040gi p. 35 footnote names 1z, 3, 6, 8r, 8t, 8u, minus 15); the ambiguity's premise that 8u is refused upstream no longer holds. Add `s1.line8u` to `sa.dep_earned_sum`'s sum, fix its label and the ambiguity's chosen text, add a dependent fixture with 8u. |
| BUG-0768 | low | sa.line6; sa.foreign_tax_deduct_if_tax; ftc.taxes | Foreign taxes not allowed as a credit but deductible (p514 p. 3, e.g. dividend withholding failing the holding period) are neither computed nor refused. Proposed: a question beneath ftc.asked feeding sa.unsupported (refusal), or compute line 6. |

## Counts by form and kind

- f1040 transcription (d366a5e05a41): ambiguity 1 (6d), representation 3 (7a, 12b, 16). Render (5579a86673ec):
  finding 1 medium (1a), scope 2 (1h, 1z). Class M: agree 462, disagree 0.
- s1 transcription (4e8342b3a4f8): representation 6, ambiguity 1 (20 box). Render (0ce8f77a53a4): scope 4 (8e, 8a, 9, 10).
  Class M held by the coordinator until b1w1.
- s1a transcription (f93799ca7307): scope 1 (4b). Render: representation 1 (36b). Class M: run failed (see below).
- oi8z transcription: no open line after carry. Render: scope 1 (8z amount). Class M: agree 18, disagree 0.
- sli transcription (6e21762b3daa): model error 1 (sli.deduction: the reply omits the not-claimed-as-a-dependent
  condition), representation 1 (line 1). Render: no disagreement.
- sa transcription (8d1c7332dffb): representation 8, finding 1 medium (dep line 2). Render (93a84847a227): ambiguity 1,
  scope 3, finding 2 (dep line 2 medium; line 6 low).

## Not done / open

- Class M f1040 (whole): agree 462, disagree 0; nothing to rule (summary section added).
- Class M pending at hand-back (21:4x), not ruled: sa, sli (released late), s1 (released after b1w1, 21:23), s1a (its
  first run died in the pre-build, SIGTERM, before any model call; requeued by the lead). Rule each when
  `/tmp/xadj/classm-<form>.txt` ends with `classm rc=`.
- check_logs could not be run at the end: it refuses on a stale build (forms/2025/s2.yaml edited 21:06:57, after the
  build); building is outside this lane. Checked directly instead: no `Ruling: open` in any transcription, render or
  class M log of the six forms, and rule.py reported 0 open after each application.
