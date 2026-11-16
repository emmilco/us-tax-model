# sche adjudication

Adjudication of the review logs of sche (new form of the coverage expansion, lane x1-sche).

## Goal-1 round (2026-11-15)

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), worktree x1-sche (uncommitted). Whole-form reviews of a new form; rulings /tmp/xrev-new/sche.tr.json, applied with rule.py; full text in the log and sidecar.

Evidence: .transcription/triage/2025/sche.json (2,029 inputs per line); i1040se p. 3; forms/2025/sche.yaml.

| family | kind | line | class | reason |
| --- | --- | --- | --- | --- |
| claude | transcription | sche.loss_prelimit | representation | equivalent on executable triage (2,029 of 2,029 inputs agree): the reply sums line 21 losses over all rentals without the project's home-rented-under-15-days exclusion, which never changes the value (such a home has no reported... |
| claude | transcription | 23a | representation | equivalent on executable triage (2,029 of 2,029); the reply omits the project's exclusion of a home rented fewer than 15 days, whose line 3 is not reported. |
| claude | transcription | 23d | representation | equivalent on executable triage (2,029 of 2,029); as 23a. |
| claude | transcription | 24 | representation | equivalent on executable triage (2,029 of 2,029): positive line 21 amounts of rentals and royalties, as the project's sum of rental.net_income and royalty.income. |
| claude | transcription | 23c | representation | differs only as candidate-unknown (1 completed, 3 incomplete inputs) where the reply reads rental.active (or another entry answer) on a home rented fewer than 15 days, which the project leaves out of every Schedule E and Form 8... |
| claude | transcription | 23e | representation | as 23c (where the reply reads rental.active (or another entry answer) on a home rented fewer than 15 days, which the project leaves out of every Schedule E and Form 8582 total and so never asks (i1040se p. 3: a dwelling unit us... |
| claude | transcription | 25 | representation | as 23c (where the reply reads rental.active (or another entry answer) on a home rented fewer than 15 days, which the project leaves out of every Schedule E and Form 8582 total and so never asks (i1040se p. 3: a dwelling unit us... |
| claude | transcription | sche.any | model error | on classm.sche.2 (a home rented 10 days with 200 personal days) the reply says Schedule E is filed (it counts the entry, as its note says), but i1040se p. 3 says such a unit's rent is not reported, and the project, which counts... |

Counts: representation 7, model error 1. Findings: none.

## Goal-1 round (2026-11-15), render

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), worktree x1-sche (uncommitted). Whole-form reviews of a new form; rulings /tmp/xrev-new/sche.render.json, applied with rule.py; full text in the log and sidecar. Evidence: the log's reasons, rendered/2025/sche.md, the cited source, the form YAML.

| family | kind | line | class | reason |
| --- | --- | --- | --- | --- |
| claude | render | 41 | scope | sche's note: 'line 41 is line 26 (Parts II to IV are refused)': partnership, S corporation, estate and trust income is refused by scope.k1 (through scope.schedule1) and farm income by scope.farm, so lines 32, 37, 39 and 40 are ... |

Counts: scope 1. Findings: none.

## Goal-1 round (2026-11-15), class M

Claude class M (claude-opus-5-5): agree 18, disagree 0; cost $0.17. No open line; nothing to rule.
