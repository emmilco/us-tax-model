# rec adjudication

Adjudication record of the reviews of rec (new form, coverage expansion lane x2-s1o).

## Goal-1 round (2026-11-15)

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), worktree x2-s1o (uncommitted). First whole-form Claude transcription review of the new form; open lines ruled on `.transcription/triage/2025/rec.json`, `--explain` witnesses, the reply, the archived sources and `forms/2025/rec.yaml`. Rulings `/tmp/xrev-new/rec.tr.json`, applied with rule.py; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | rec.path | model error | 2,244/2,444 agree; completed: 1 value (rec.not_itemized) | p525 pp. 26-27, Worksheets 2a and 2 | the reply's path is any recovery kind ticked, without the 2024 itemizing test. On fixture rec.not_itemized (a property tax refund, no itemized deductions for 2024) the project says false and the reply true (41 value diff |
| claude | transcription | rec.to_line1 | model error | 519/2,444; completed: 1,095 candidate-refuses | p525 pp. 26-27, Worksheets 2a and 2 | the reply refuses through its own gate rec.h_ti_conflict on 1,095 completed returns where the project computes (stage14.asset.hy_5yr: project $0, no recovery at all); its value branches follow the p525 p. 27 split ('If l |
| claude | transcription | rec.to_line8z | model error | 530/2,444; completed: 1,095 candidate-refuses | p525 pp. 26-27, Worksheets 2a and 2 | as rec.to_line1: the reply refuses through its own rec.h_ti_conflict on 1,095 completed returns where the project computes $0; no value differs where both compute. |
| claude | transcription | 2a:1 | representation | 2,439/2,444; completed: 2 value (off path) | p525 pp. 26-27, Worksheets 2a and 2 | the reply drops the refund gates (refund.itemized, refund.sales, refund.two_returns). Value differences (5; completed: stage16.refund.f1, project $0, reply $1,000) fall only on returns where Worksheet 2 is not used (rec. |
| claude | transcription | 2a:2 | representation | 2,363/2,444; completed: 1 value (off path), 19 unknown | p525 pp. 26-27, Worksheets 2a and 2 | the reply drops the parent gate (scope.recovery and refund.itemized). Its one completed value difference (rec.not_itemized, project $0, reply $300) is a non-itemizer for whom Worksheet 2 is not used (p525 p. 27, Recoveri |
| claude | transcription | 2a:6 | representation | 2,359/2,444; completed: 3 value (off path), 3 hides-shown | p525 pp. 26-27, Worksheets 2a and 2 | value differences only where line 1 differs off the Worksheet 2 path (as 2a:1); the reply also hides line 6 after the line 5 STOP ('No. [STOP] None of the refunds on line 1 or 2 are taxable', p525 p. 26), where the proje |
| claude | transcription | 2a:4 | representation | 2,408/2,444; unknowns only | p525 pp. 26-27, Worksheets 2a and 2 | the reply subtracts 2024 line 5e from line 5d where the project reads refund.line2 (the same 2024 figure); the reply reads the worksheet's inputs without their parent questions (scope.recovery, refund.itemized, the rec_k |
| claude | transcription | 2a:5 | representation | 2,430/2,444; project-unknown only | p525 pp. 26-27, Worksheets 2a and 2 | the reply adds a shown_when for the line 5 'Yes' branch; differences are project-unknown only on refused or incomplete returns, no value differs (p525 p. 26, line 5). |
| claude | transcription | 2a:7 | ambiguity | 2,428/2,444; completed: 6 value (classm.rec.3) | p525 pp. 26-27, Worksheets 2a and 2 | amb.2025.rec_ratio_places (p525 p. 26, line 7, 'divide line 1 by line 6. Then multiply by the amount on line 5', precision unstated): the project rounds the ratio to six places (classm.rec.3: $666.67), the reply to four  |
| claude | transcription | 2a:8 | ambiguity | 2,396/2,444; completed: 5 value (classm.rec.3) | p525 pp. 26-27, Worksheets 2a and 2 | amb.2025.rec_ratio_places, as 2a:7 (classm.rec.3: project $333.33, reply $333.30). |
| claude | transcription | 2 | representation | 2,312/2,444; unknowns only | p525 pp. 26-27, Worksheets 2a and 2 | the reply reads the worksheet's inputs without their parent questions (scope.recovery, refund.itemized, the rec_kinds ticks), so it is unknown where the interview never asks them; no value differs on any completed return |
| claude | transcription | 7 | representation | 2,444/2,444 | p525 pp. 26-27, Worksheets 2a and 2 | equivalent on executable triage (2,444/2,444 agree); the project's extra branch is married filing separately with a spouse who itemized, and MFS is refused for every return (scope, s3.mfs). |
| claude | transcription | 9 | representation | 2,430/2,444; project-unknown only | p525 pp. 26-27, Worksheets 2a and 2 | the reply hides the line when line 8 is zero or less (p525 p. 27, line 8, 'If the result is zero or less, stop here'); differences are project-unknown only on refused or incomplete returns, no value differs. |
| claude | transcription | 10 | representation | 2,383/2,444; 7 hides-shown on refused returns | p525 pp. 26-27, Worksheets 2a and 2 | the reply hides line 10 after the line 8 stop; its only shown/hidden differences are on refused returns (7), and no value differs on a completed return. |
| claude | transcription | 11 | model error | 2,378/2,444; completed: 16 candidate-refuses | p525 pp. 26-27, Worksheets 2a and 2 | the reply refuses through its own rec.h_ti_conflict on 16 completed returns where the project computes (classm.rec.1: project $925); its value expression equals the project's (p525 p. 27, line 11, 'If line 10 is a negati |
| claude | transcription | B | model error | 670/2,444; completed: 1,095 candidate-refuses | p525 pp. 26-27, Worksheets 2a and 2 | the reply refuses through its own rec.h_ti_conflict on 1,095 completed returns (stage14.asset.hy_5yr); its ratio rounded to four places instead of six is amb.2025.rec_ratio_places. |
| claude | transcription | C | model error | 667/2,444; completed: 1,095 candidate-refuses, 3 hides-shown | p525 pp. 26-27, Worksheets 2a and 2 | as B (the reply's rec.h_ti_conflict refusal on 1,095 completed returns); its shown_when also hides line C where line 1a is zero (classm.rec.4, project shows $50), where p525 p. 27 sends line 11 to line 8z without the A-C |

Counts: ambiguity 2, model error 6, representation 9. Findings: none.

## Goal-1 round (2026-11-15), render

Open lines of the Claude render log (rendered text fresh), ruled on the reply's reason, `rendered/2025/rec.md`, the cited source and the form YAML. Rulings `/tmp/xrev-new/rec.render.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 2a:1 | ambiguity | reply's reason | p525 pp. 26-27, Worksheets 2a and 2 | amb.2025.refund_two_returns (i1040gi p. 90 tests a refund against one 2024 return): on a joint 2025 return with refunds of both spouses' tax on separate 2024 returns the chosen reading takes none as taxable when neither return itemized state and local income t |
| claude | render | 2 | scope | reply's reason | p525 pp. 26-27, Worksheets 2a and 2 | a recovered general sales tax deduction (p525 footnote 2, 'If you deducted state and local general sales taxes and received a refund of those taxes, include the amount on line 2') is refused (rec.sales_tax_if_any, form note: 'of general sales tax ... refused') |
| claude | render | 5 | ambiguity | reply's reason | p525 pp. 26-27, Worksheets 2a and 2 | amb.2025.rec_line5 (p525 p. 27, line 5, 'Enter any amount previously refunded to you'): chosen reading zero for 2024 deductions recovered in 2025, since an amount refunded during 2024 reduced the 2024 deduction itself; recoveries for years before 2024 are refu |

Counts: ambiguity 2, scope 1. Findings: none.

## Goal-1 round (2026-11-15), class M

Whole-form Claude class M run: agree 101, disagree 0, skipped 9, missing 0; cost $0.54. Nothing to rule.
