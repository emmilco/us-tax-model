# Adjudication — clcw26

Method: `README.md` in this directory. New in Stage 20 (the carryover to 2026, the i1040sd p. 10 worksheet applied to
this return under amb.2025.clcw_to_2026); no earlier rounds.

## Stage 20, round 1 (superseded subject)

Fresh reviews of 2026-10-27. The Claude transcription agrees on all 13 lines (`../triage/clcw26.json`: "no candidate
lines"). The deepseek transcription is valid and triaged (`../triage/clcw26.deepseek.json`, executable-triage-v2: 1,159
fixtures, 500 generated returns seed 20261026, 1,659 comparisons per line); its 7 open lines are ruled. Class M logs had
no open line. Full ruling text: `.transcription/proposed/stage20/{transcription,render}.clcw26[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| deepseek | transcription | 1, 2, 5, 6, 9, 10 | model error | 392–532 agree; 15–106 value each; 1–10 candidate-shows-skipped; e.g. line 2 classm.clcw26.2.deepseek $3,000 vs $0 | i1040sd p. 14, Line 21; amb.2025.clcw_to_2026 | Reads the 2024 figures (clcw.prior_*), so it recomputes the carryover into 2025. |
| deepseek | transcription | 3 | model error | 405 agree; 44 value (classm.clcw26.4.deepseek: $149,038 vs $0) | i1040sd p. 10, line 3; p550 p. 102 | Same, and it subtracts line 2 where "combine" adds it. |
| claude | render | 1 | interface gap | UNCLEAR, line 15 = 11b − 14 not shown | Form 1040 (2025) p. 2, line 15 (not given) | The English is right; the defining page was not given. |
| deepseek | render | 1 | interface gap | UNCLEAR, same | as Claude | As Claude. |
| deepseek | render | 6 | model error | MISMATCH | i1040sd p. 10, line 6 | Reversed the subtraction: line 15 less zero, floored, is the gain. |
| deepseek | render | 10 | model error | MISMATCH | i1040sd p. 10, line 10 | Same for line 7. |

Read against i1040sd pp. 10 and 14 and p550 pp. 102–103. The 13 lines, their hiding and the decedent notice (p550 p.
103) agree with the worksheet as applied to 2025. Line 1 is held before the zero floor, as p. 14 and p550 p. 102
require.

Findings: one, in `.transcription/proposed/stage20/clcw26.findings.md`. F1 (low): `clcw26.show` tests only "a loss on
line 16" of p. 14's sentence and drops "and either: That loss is more than the loss on line 21; or ... line 15, would be
less than zero". So the worksheet shows lines 1–7 with amounts when there is no carryover to 2026 (a fully deducted
$1,000 loss). No carryover amount is wrong.

## Stage 20, round 2

Fresh reviews of 2026-10-27, after BUG-0187: `clcw26.show` now tests the whole i1040sd p. 14 sentence (line 16 a loss,
and line 16 below line 21 or line 11b below line 14). The first-round logs are archived in
`.transcription/archive/stage20-clcw-before-findings-fixes-2026-10-27/`. Open lines: Claude render line 1, deepseek
transcription line 3, and the 13 lines of deepseek class M case classm.clcw26.3. Triage `../triage/clcw26.deepseek.json`
(executable-triage-v2: 1,168 fixtures, 500 generated returns seed 20261026, 1,668 comparisons). Full ruling text:
`.transcription/proposed/stage20/{render.clcw26,transcription.clcw26.deepseek,classm.clcw26.deepseek}.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | interface gap | UNCLEAR, line 15 = 11b − 14 not shown | Form 1040 (2025) p. 2, line 15 (not given) | As round 1. |
| deepseek | transcription | 3 | model error | 308 agree, no value; 127 candidate-shows-skipped (82 completed; classm.f4952.1.deepseek $89,629.10 on a hidden line), 1,010 candidate-unknown, 203 candidate-refuses, 20 project-refuses | i1040sd p. 10, line 3; p. 14, Line 21 | The value is algebraically the project's; the reply shows the line where p. 14 says there is no carryover, and needs clcw.spouse_screen through its line 1. |
| deepseek | classm | classm.clcw26.3, lines 1–13 | model error (dropped) | MISSING: reply names lines "line N (type)", unparsed; line 16 a $51,731 gain | i1040sd p. 14, Line 21 | Format failure. The worksheet is not reached, so blank is right; the reply's $29,527 on lines 1 and 3 is on unreached lines. |

Fix checked: the BUG-0187 condition matches p. 14 word for word. Re-evaluating round 1's $1,000 fully deducted loss now
hides the worksheet. Observation (tooling, not ruled): cases classm.clcw26.1 and .3 have `clcw26.show` false, yet the class
M prompt asks for all 13 lines. Case 1's AGREE values on lines 1–5 ($89,629.10 and so on) assert internal values of hidden
lines.

Findings: none new; round-1 F1 is fixed.
