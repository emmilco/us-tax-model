# Adjudication — refund

Method: `README.md` in this directory. Triage record: `../triage/refund.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 295 partial records over
17 bases). DeepSeek family only. Full ruling text is in the log and its sidecar.

## Round 1 (superseded subject)

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| deepseek | refund.has | model error | 870/1,878 agree; 981 candidate-unknown, 17 project-unknown, 6 value, 4 candidate-refuses | i1040gi p. 88, Line 1, "If you received a refund, credit, or offset" | Redefines "a refund was received" as "line 9 is positive", so it asks the itemizing questions on returns with no refund. |
| deepseek | refund.taxable | model error | 1,841/1,878 agree; 34 project-unknown, 2 candidate-unknown, 1 project-refuses | f1099g p. 5, Box 8, "If taxable, report the amount in box 2 on Schedule C or F"; i1040gi p. 88, TIP | Skips the box 8 and other-year questions when 2024 deductions were not itemized, though neither depends on 2024 itemizing (amb.2025.refund_exceptions). |
| deepseek | 1 | representation | 1,791/1,878 agree; 51 candidate-unknown, 34 project-unknown, 2 candidate-refuses | i1040gi p. 90, worksheet line 1 | Same smaller-of on the worksheet path; the differences are partial records off that path or returns the project refuses on refund.taxable. |
| deepseek | 2 | representation | 1,826/1,878 agree; 34 project-unknown, 17 candidate-unknown, 1 project-refuses | i1040gi p. 90, worksheet line 2 | Same subtraction on the worksheet path; the project refusal is the cited impossible-entry screen on line 5e (i1040sca p. 7). |
| deepseek | 4 | representation | 1,844/1,878 agree; 17 candidate-unknown, 17 project-unknown | i1040gi p. 90, worksheet line 4 | Same entry where the worksheet is used; the differences are partial records off the worksheet path. |
| deepseek | 6 | model error | 1,826/1,878 agree; 35 candidate-unknown, 17 project-unknown | i1040gi p. 90, line 6 footnote; p. 33, "Don't check any boxes for your spouse if your filing status is head of household" | Asks the spouse boxes of single and head of household filers. |
| deepseek | 8 | model error | 1,809/1,878 agree; 52 candidate-unknown, 17 project-unknown | i1040gi p. 90, Note and line 8 | Own logic is equivalent; it inherits the line 6 spouse questions on a reachable single return (stage16.mut.refund_single_unasked). |
| deepseek | 9 | model error | 1,771/1,878 agree; 85 project-unknown, 19 candidate-unknown, 2 candidate-refuses, 1 project-refuses | i1040gi p. 90, line 3, "No. STOP None of your refund is taxable" | Ignores the line 3 STOP and needs the 2024 filing status after it (stage16.mut.refund_line3_stop). |

Findings: none. Project lines unchanged.

## Fix round 2 (superseded subject)

Fresh reviews of 2026-10-30 (claude-opus-5-5 and deepseek-flash, transcription and render) of the subject after BUG-0230
(`refund.not_2024` asks about any 2024 tax paid in 2025) and BUG-0251 (`refund.box8` asks about any business-only income
tax refund, with or without a Form 1099-G); no expression changed. Triage `../triage/refund[.deepseek].json`
(executable-triage-v2; 1,382 fixtures, 500 generated returns seed 20261026, 640 / 445 partial records from 40 bases, all
without a refund; 2,522 / 2,327 comparisons per line), every witness enumerated by an uncapped scratch rerun. No value
difference on a completed return reaches a printed amount (the 4 completed `refund.has` values leave Schedule 1 line 1 at
$0.00 on both sides). Class M log: no open section. Full ruling text:
`.transcription/proposed/fixr2/{transcription,render}.refund[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | refund.taxable | representation and scope | 1,242 agree; 1,239 project-unknown (524 completed), all with no refund; 40 candidate-unknown (refund.received); 1 project-refuses (line5e_bad) | i1040gi p. 88, TIP; f1099g p. 5, Box 8 | Same choice and same gates; s1.line1 never reads the line without a refund. |
| claude | transcription | 6 | representation | 2,482 agree; 40 project-unknown (refund.status withheld, no box checked) | i1040gi p. 90, line 6 and footnote; p. 33 | Spouse boxes now only for joint or separate, as the project; per-box sum equals count times rate. |
| claude | transcription | 8 | representation | 2,522 / 2,522 agree | i1040gi p. 90, Note and line 8 | Equivalent. |
| deepseek | transcription | refund.has | model error | 1,034 agree; 6 value (4 completed: stage16.refund.f1, f2, f4, f7, true vs false, Schedule 1 line 1 $0 both); 1,256 candidate-unknown | i1040gi p. 88, Line 1 | Redefines "a refund was received" as "line 9 is positive". |
| deepseek | transcription | refund.taxable | model error and scope | 2,270 agree; 56 candidate-unknown (2 fixtures need refund.mfs_spouse_itemized); 1 project-refuses | i1040gi p. 88, TIP; p. 90, line 3 | Box 8 and other-year now asked of every refund; inherits lines 8 and 9. |
| deepseek | transcription | 6 | model error and scope | 2,133 agree; 163 candidate-unknown (stage16.mut.refund_single_unasked); 4 candidate-refuses | i1040gi p. 90, line 6 footnote; p. 33 | Spouse boxes asked of single and head of household filers. |
| deepseek | transcription | 8 | model error and scope | 2,133 agree; 190 candidate-unknown (stage16.mut.refund_single_unasked, $1,400 project); 4 candidate-refuses | i1040gi p. 90, Note | Spouse-itemized question asked of every status. |
| deepseek | transcription | 9 | model error and scope | 2,160 agree; 83 candidate-unknown (refund_line3_stop, refund_single_unasked); 81 project-unknown (no refund); 2 candidate-refuses; 1 project-refuses | i1040gi p. 90, line 3 STOP | Ignores the line 3 STOP; inherits line 8. |
| claude | render | 1 | ambiguity and scope | - | i1040gi p. 90, line 1; p. 89, exceptions 1, 2, 5 | 5d cap is amb.2025.refund_cap_5d; exceptions refused by refund.not_2024 on refund.taxable and scope.schedule1. |
| claude | render | 6 | representation | - | i1040gi p. 90, line 6 | Rate is in refund.per_box's label; MFS footnote in the spouse questions. |
| deepseek | render | 1 | scope | - | i1040gi p. 89, exceptions 1, 2, 5 | As the Claude render ruling. |
| deepseek | render | 6 | representation | - | i1040gi p. 90, line 6 footnote | MFS conditions are in the spouse questions. |

Findings: none. Errors introduced by the fixes: none found; both rewordings are wider than before (safe direction).

## Fix round 5

The render logs (claude-opus-5-5 and deepseek-flash) were rerun on 2026-10-30 because the rendered English of `refund`
changed through a shared line. The refund form and its transcription were not changed or rerun, so fix round 2's
transcription rows stand. The open render lines are 1 and 6 in both families. Their restatements match fix round 2's
word for word, and the objections are the same. Fix round 2's rulings were rechecked against the current
`refund.not_2024`, `refund.received`, `scope.schedule1`, `refund.per_box` and spouse questions and the register. The
Claude line-6 reply also asks why the spouse boxes are zero for a qualifying surviving spouse; amb.2025.refund_boxes_2024
records that reading. Full ruling text: `.transcription/proposed/fixr5/render.refund[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | ambiguity and scope | render MISMATCH | i1040gi p. 90, line 1; p. 89, exceptions 1, 2, 5 | 5d cap is amb.2025.refund_cap_5d; exceptions refused by refund.not_2024 on refund.taxable and scope.schedule1. |
| claude | render | 6 | representation | render UNCLEAR | i1040gi p. 90, line 6; p. 33; amb.2025.refund_boxes_2024 | Rate in refund.per_box; MFS footnote in the spouse questions; no spouse boxes on a qss return. |
| deepseek | render | 1 | scope | render MISMATCH | i1040gi p. 89, exceptions 1, 2, 5 | As the Claude render ruling. |
| deepseek | render | 6 | representation | render MISMATCH | i1040gi p. 90, line 6 footnote | MFS conditions are in the spouse questions. |

Findings: none.
