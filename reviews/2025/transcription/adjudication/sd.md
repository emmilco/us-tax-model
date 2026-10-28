# Adjudication — sd

Method: `README.md` in this directory.

Stage 20 (fresh replies of 2026-10-27 after the capital loss carryover): triage `../triage/sd.json` and
`../triage/sd.deepseek.json` (executable-triage-v2, both evaluated; 1,159 fixtures, 500 generated returns, seed 20261026,
120 partial records; 1,779 comparisons). The reviewers had f1040sd pp. 1–2, i1040sd pp. 10, 11, 12, 15 and i1040gi
pp. 31, 38 (not i1040sd p. 2). Full ruling text: `.transcription/proposed/stage20/transcription.sd[.deepseek].json`
and `render.sd.deepseek.json`. Render sd (Claude) had no open sections.

## Stage 20

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | 6, 14 | representation | 1,695 and 1,699 of 1,779 agree; 26 and 22 value (all sign flips: classm.sd.2 −$16,565/$16,565, −$17,835/$17,835), 20 project-refuses, 38 project-unknown | f1040sd p. 1, lines 6, 14 ("( )"), 7, 15 | Same worksheet amount held positive and subtracted. The project holds it negative under the owner's sign decision (T-004), and lines 7 and 15 agree. |
| claude | transcription | 7, 15 | scope | 1,739 (all 1,704 in-scope agree) and 1,704 of 1,779; only project-refuses (40, 74) and 1 unknown | f1040sd p. 1, lines 7, 15 | Subtracting a positive carryover equals adding a negative one; the differences are cited gates. |
| claude | transcription | sd.filed | model error | 1,694/1,779; 1 value (stage20.line21_at_both_bounds, completed: project false, candidate true), 40 project-refuses, 44 project-unknown | i1040sd p. 10, "Otherwise, you don’t have any carryovers"; i1040gi p. 31, Exception 1, "You have no capital losses" | A Yes to the gate with worksheet lines 8 and 13 at $0 leaves no capital loss, so Schedule D is not required; the candidate requires it. |
| claude | transcription | 20 | interface gap | 1,721/1,779; 4 value (classm.sd.2, stage20.blind.r7, generated 235), 53 project-refuses, 1 project-unknown | f1040sd p. 2, line 20; i1040sd p. 11, 28% worksheet line 5 | The candidate's positive line 14 enters the project's g28.line5, which expects a negative loss. The interface lists g28.line5 and u1250.line16 only as Dollars, so the candidate could not see that they read line 14 negative. |
| claude | transcription | sd.investment_election | scope | 1,642/1,779; 58 project-refuses, 24 candidate-refuses (all on refused returns), 55 project-unknown | i1040sd p. 15, applicability and line 3 | Both give line 4g; the differences are cited gates and Schedule B gates. |
| claude | transcription | sd.to1040 | scope | 1,704/1,779; 74 project-refuses, 1 project-unknown | f1040sd p. 2, line 16 | Same values; only cited gates differ. |
| claude | transcription | 1a–10, columns (d)(e)(g)(h) (32 lines) | scope | 1,679 or 1,667 (1a(g), 8a(g): 1,628) of 1,779; 60–72 project-refuses, 40–79 project-unknown, no value | f1040sd p. 1, lines 1a–10 | Digital boxes G–L are refused by `sales.one` (T-003). Column (h) is computed as (d) − (e) + (g). The constant 0 in column (g) of lines 1a and 8a matches, because `sales.bad_aggregate` refuses aggregate entries with adjustments. |
| deepseek | transcription | 6, 14 | model error | 662/1,779; 1,081 candidate-unknown (gate-No returns, 413 completed, e.g. classm.f2441.1.deepseek), no value, 20 project-refuses, 16 project-unknown | i1040sd p. 10, "Otherwise, you don’t have any carryovers" | Drops the `sd.carryover` choice, so it needs the 2024 figures and the spouse screen on returns the interview never asks them for. |
| deepseek | transcription | sd.filed | model error | 822/1,779; 882 candidate-unknown, no value | i1040gi p. 31, Exception 1; i1040sd p. 10 | Tests worksheet lines 8 and 13 without the gate (same defect). |
| deepseek | transcription | sd.line19 | model error | 689/1,779; 9 value (line 17 No, box 2b: generated 162 $6,330.85 against $0), 1,022 candidate-unknown | f1040sd p. 2, line 17, "No. Skip lines 18 through 21" | Shows the section 1250 worksheet result on a skipped line. |
| deepseek | transcription | sd.line18 | interface gap | 1,519/1,779; 55 value (all box 2d with line 17 Yes: classm.f8889.1.deepseek $823, classm.sdtw.5 $3,800), 84 project-refuses, 121 project-unknown | i1040sd p. 11, Line 18; p. 2 (not given) | Candidate is 0; the box 2d trigger is on a page the reviewer lacked (as in round 2). |
| deepseek | transcription | 20 | interface gap | 758/1,779; 20 value (box 2d, line 17 Yes: classm.g28.2, generated 0, 78, 90, 100), 945 candidate-unknown, 4 candidate-refuses, 51 project-refuses | f1040sd p. 2, lines 17, 20 | Follows from the constant line 18. The unknowns are inherited from lines 6 and 14; the refusals are evaluation order on refused returns. |
| deepseek | transcription | sd.to1040, sd.net_gain, 21 | representation | 663/1,779 each; 1,022 candidate-unknown (inherited from lines 6 and 14), no value | f1040sd p. 2, lines 16, 21; i1040gi p. 38, line 3 | Algebraically equal: a zero branch, the min/max identity, 0 − 0. |
| deepseek | transcription | 4, 5, 11, 12 | representation | 1,779/1,779 agree | f1040sd p. 1 | 0 − 0 against 0. |
| deepseek | transcription | 1a–10, columns (d)(e)(g)(h) (32 lines) | scope | 1,667/1,779 each; 72 project-refuses, 40 project-unknown, no value | f1040sd p. 1, lines 1a–10 | Adds the digital boxes G–L, which `sales.one` refuses (T-003). |
| deepseek | render | 20 | representation | MISMATCH ("should be skipped" when line 17 is No) | f1040sd p. 2, line 17; sd.yaml note; README skipped-line rule | Boolean flow predicate shown on a skipped line, under the documented exemption; no amount reads it on that path. |

Stage 20 check. Lines 6 and 14 take worksheet lines 8 and 13 behind the gate, held negative. Their values were
checked by hand on classm.sd.2. The worksheet's applicability test needs no gate line: an independent brute force over
112,395 random 2024 loss returns found no case with lines 8 or 13 nonzero outside test (a) or (b). `sd.filed`'s new
line 6/14 test is right on the one triage difference. Removing the carryover refusals changed no line-1a–10 total.

Findings: F1, low, English only: the labels of lines 4, 5, 11 and 12 still say "source/carryover screening" after
the carryover refusal was removed (see `.transcription/proposed/stage20/sd.findings.md`; it also notes the
pre-existing `doc: f1040sd` on `sd.filed`'s i1040gi quotes). No tax amount differs. Suspected tooling limitation:
triage evaluates the candidate's sd lines inside the project's g28 and u1250, and the published interface does not
state their sign contract, so a sign choice that is legitimate within sd shows up as line 18/20 differences.

Round 2 (fresh replies of 2026-10-26 after BUG-0149): triage `../triage/sd.json` (executable-triage-v2; 1,094
fixtures, 500 generated returns, seed 20261026, 120 partial records; 1,714 comparisons) and `../triage/sd.deepseek.json`
(state "invalid": the refusal declarations of `sd.line18` and `sd.line19` name the collection field `sales.special`,
rejected as `sd.sd.__type_gate_6` and `__type_gate_7`; nothing executed). Only lines 18, 19 and 20 of the DeepSeek reply
carry that failure; the rest are ruled by reading. Full ruling text:
`.transcription/proposed/round2/transcription.sd[.deepseek].json`. Render sd had no open rulings.

## Round 2 (superseded subject)

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | sd.line18 | interface gap | 1,390/1,714 agree; 52 value (all line 17 Yes, box 2d: classm.f8889.1.deepseek $823, classm.tcw.1 $400), 115 project-refuses, 157 project-unknown | f1040sd p. 2, line 18; i1040sd p. 2, Capital Gain Distributions (not given) | Candidate is 0 always; the box 2d rule is on a page the reviewer lacked. No line 17 No difference remains, so the candidate agrees with the BUG-0149 fix. |
| claude | transcription | sd.line19 | scope | 1,528/1,714; 79 project-refuses, 107 project-unknown, no value | f1040sd p. 2, line 17; i1040sd pp. 11–12, Line 19 | Box 2b is the only in-scope trigger; the line 17 guard is the BUG-0149 fix. |
| claude | transcription | sd.investment_election | scope | 1,596/1,714; 67 project-refuses, 34 project-unknown, 17 candidate-refuses | i1040sd p. 15, worksheet applicability and line 3 | Both give line 4g; the differences are cited gates and Schedule B gates on refused returns. |
| claude | transcription | sd.filed | interface gap | 1,556/1,714; 45 value (no sales, line 18 or 19 positive), 52 project-refuses, 61 project-unknown | i1040gi p. 31, Line 7a, Exception 1 (not given) | Candidate omits boxes 2b and 2d; the filing rule is on a page the reviewer lacked. BUG-0149 changes no value. |
| claude | transcription | sd.to1040 | scope | 1,630/1,714; 83 project-refuses, 1 project-unknown | f1040sd p. 2, line 16 | Same values; only the cited gates behind lines 16 and 21 differ. |
| claude | transcription | 1a–10, columns (d)(e)(g)(h) (32 lines) | scope | each 1,552/1,714; 82 project-refuses, 80 project-unknown, no value | f1040sd p. 1, lines 1a–10; i1040sd p. 11, Example 2 | Added digital boxes G–L and the dropped route test on lines 2, 3, 9 and 10 reach only refused entries (T-003). Column (h) is computed as (d) − (e) + (g). |
| claude | transcription | 7, 15 | scope | 1,664/1,714 (50 refuses); 1,630/1,714 (83 refuses, 1 unknown) | f1040sd p. 1, lines 7 and 15 | The carryover sign does not matter because carryovers are refused (T-004). |
| claude | transcription | 20 | interface gap | 1,624/1,714; 22 value (project line 18 positive: classm.tcw.1), 63 project-refuses, 4 candidate-refuses, 1 project-unknown | f1040sd p. 2, line 20 | Follows from the zero line 18. The 963 line-17-No differences of round 1 are gone. |
| deepseek | transcription | sd.line18, sd.line19 | model error | not executed: `sd.sd.__type_gate_6`/`_7` fail | host type check | Ruled on the invalid refusal declaration (`sales.special`). The constant 0 is consistent with BUG-0149. |
| deepseek | transcription | 20 | model error | not executed | host type check (closure) | Reads lines 18 and 19, whose declarations fail. |
| deepseek | transcription | sd.filed | model error | not executed (ruled by reading) | i1040gi p. 38 (given); p. 31, Exception 1 | Makes every capital gain distribution require Schedule D, against the given p. 38 sentence. |
| deepseek | transcription | sd.to1040, sd.net_gain, 21 | representation | not executed (ruled by reading) | f1040sd p. 2, lines 16 and 21; i1040gi p. 38, line 3 | Algebraically equal: zero branch; min/max identity; negative loss limit. |
| deepseek | transcription | 4, 5, 6, 11, 12, 14 | representation | not executed (ruled by reading) | f1040sd p. 1 | 0 − 0 against 0, behind the same screens. |
| deepseek | transcription | 1a–10, columns (d)(e)(g)(h) (32 lines) | scope | not executed; the Claude filters with the same boxes agree in scope | f1040sd p. 1, lines 1a–10 | Digital boxes G–L are refused by `sales.one` (T-003). |

BUG-0149 check: neither fresh candidate gives a nonzero line 18 or 19 when line 17 is No. The fix follows f1040sd
p. 2, line 17 ("No. Skip lines 18 through 21"). No new error was found downstream (`sd.filed`, line 20,
`f1040.gate.sdtw`, Schedule D Tax Worksheet line 11).

Findings: none for sd in round 2. Two interface gaps come from review pages that were not given (i1040sd p. 2,
i1040gi p. 31). A fresh request with those pages would be needed to get a usable review of lines 18 and 20 and
`sd.filed`.

## Round 1 (superseded subject)

Triage records: `../triage/sd.json` (executable-triage-v1;
1,083 fixtures, 500 generated returns, seed 20261026, 120 partial records) and
`../triage/sd.deepseek.json` (state invalid: the refusal declarations of `sd.line18` and `sd.line19`
name the collection field `sales.special`, reported as `sd.sd.__type_gate_6` and `__type_gate_8`; no
open DeepSeek line reads either, so those lines are ruled by reading). Full ruling text is in
`.transcription/proposed/sd.json` and `sd.deepseek.json`.

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | sd.line18 | finding | 1,618/1,703 agree; 5 value, 79 project-refuses, 1 project-unknown | f1040sd p. 2, line 17; i1040sd p. 11, Line 18 | The project keeps the 28% worksheet result when line 17 is No; on the Form 4952 path it puts it on worksheet line 11 and opens lines 41–43 (tax unchanged). |
| claude | sd.line19 | finding | 1,613/1,703 agree; 10 value, 79 project-refuses, 1 project-unknown | f1040sd p. 2, line 17; i1040sd p. 11, Line 19 | Same for the section 1250 result; on the Form 4952 path worksheet line 11 shows $500 for a 0 and lines 35–40 are opened (tax unchanged). |
| claude | sd.investment_election | scope | 1,585/1,703 agree; 70 project-refuses, 31 project-unknown, 17 candidate-refuses | i1040sd p. 15, worksheet applicability and line 3 | Both yield line 4g; differences are the election's cited gates, screen answers, and the project's own Schedule B gates reached by the candidate. |
| claude | sd.filed | model error | 1,545/1,703 agree; 43 value, 56 project-refuses, 59 project-unknown | i1040gi p. 31, Line 7a, Exception 1 | The candidate leaves out boxes 2b/2d, which require Schedule D; all 43 value differences are such returns. |
| claude | sd.to1040 | scope | 1,616/1,703 agree; 86 project-refuses, 1 project-unknown | f1040sd p. 2, line 16 | The values are the same; only the cited gates behind lines 16 and 21 differ. |
| claude | 1a–10, columns (d)(e)(g)(h) (32 lines) | scope | each 1,540/1,703 agree; 83 project-refuses, 80 project-unknown | f1040sd p. 1, lines 1a–10; i1040sd p. 11, Example 2 | The extra digital and non-basis-reported aggregate boxes reach only entries that `sales.one` refuses; the unknowns are withheld screen answers. |
| claude | 7 | scope | 1,653/1,703 agree; 50 project-refuses | f1040sd p. 1, line 7 | The line 6 sign does not matter because carryovers are refused (T-004); the only differences are `sales.one` refusals. |
| claude | 15 | scope | 1,616/1,703 agree; 86 project-refuses, 1 project-unknown | f1040sd p. 1, line 15 | Same for line 14. |
| claude | 20 | representation | 588/1,703 agree; 963 value, 151 project-refuses, 1 project-unknown | f1040sd p. 2, lines 16–17; sd.yaml convention | When line 17 is No the project shows its Yes/No predicate on the skipped line 20, as the documented convention for Boolean flow predicates allows; no amount reads it; the refusals are cited gates. |
| deepseek | sd.investment_election | scope | not executable (reply invalid elsewhere) | i1040sd p. 15 | The expression is identical to the Claude candidate's and yields line 4g; the only differences are refusals. |
| deepseek | sd.filed | model error | not executable | i1040gi p. 31, Line 7a, Exception 1 | It tests sales only, so returns with box 2b/2d amounts are wrongly marked as not needing Schedule D. |
| deepseek | sd.to1040 | representation | not executable | f1040sd p. 2, line 16 | Its value equals the project's on every input. |
| deepseek | 1a–10, columns (d)(e)(g)(h) (32 lines) | scope | not executable | f1040sd p. 1, lines 1a–10 | It adds the printed digital boxes, which the project refuses through `sales.digital`; the result is the same within scope (T-003). |

Findings: sd.line18 and sd.line19 (worksheet results kept when line 17 is No), in the Claude log; see `.transcription/proposed/sd.findings.md`. No tax amount differs.
