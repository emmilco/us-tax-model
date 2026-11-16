# rprop adjudication

A building or improvement depreciated for a rental (Form 4562 line 19i/19j columns), new in coverage wave X1 (lane x1-sche).

## Goal-1 round (2026-11-15)

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), worktree x1-sche. First whole-form Claude transcription review (cost $0.92): agree 2, disagree 1. Triage `.transcription/triage/2025/rprop.json` (20 compared). Rulings `/tmp/xrev-new/rprop.tr.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | (g) | scope | 18/20; 2 project-refuses | i4562 p. 9, Lines 19a-19j; p946 pp. 73-74 | The reply also depreciates personal property, which the project refuses (rprop.personal); buildings agree. |

Counts: scope 1. Findings: none.

## Goal-1 round (2026-11-15), render

First whole-form Claude render review (cost $0.13): match 3, mismatch 2. Rulings `/tmp/xrev-new/rprop.render.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | (a) | finding (medium) | rprop.screen list; scout R10 | i4562 p. 9, 15-year property | Qualified improvement property neither refused nor given 15 years (BUG-0919). |
| claude | render | (c) | finding (medium) | rprop.basis source; $rental prompt invites a room | i1040se p. 6, Renting out part of your home; i4562 Column (c) | Basis not limited to the rented part; allocable credits not subtracted (BUG-0920). |

Counts: finding 2. Findings: BUG-0919, BUG-0920 (medium).

## Goal-1 round (2026-11-15), class M

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us). Not run: classm.py found no jobs. `classm-jobs --docs rprop,rf4562 --include-fixtures`: "rf4562: 0 case(s) cover 0/2 branches on the interview's route (... 2 not reachable on the route by a computed case, 2 with every answer)"; "rprop: 0 case(s) cover 0/10 branches (... 10 with every answer)": no corpus case computes the document without a refusal. No cost.
