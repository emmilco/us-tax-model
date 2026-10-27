# Adjudication — sd

Method: `README.md` in this directory.

Round 2 (fresh replies of 2026-10-26 after BUG-0149): triage `../triage/sd.json` (executable-triage-v2; 1,094
fixtures, 500 generated returns, seed 20261026, 120 partial records; 1,714 comparisons) and `../triage/sd.deepseek.json`
(state "invalid": the refusal declarations of `sd.line18` and `sd.line19` name the collection field `sales.special`,
rejected as `sd.sd.__type_gate_6` and `__type_gate_7`; nothing executed). Only lines 18, 19 and 20 of the DeepSeek reply
carry that failure; the rest are ruled by reading. Full ruling text:
`.transcription/proposed/round2/transcription.sd[.deepseek].json`. Render sd had no open rulings.

## Round 2

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
