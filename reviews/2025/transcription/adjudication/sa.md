# Adjudication — sa

Method: `README.md` in this directory. Triage records: `../triage/sa.json`,
`../triage/sa.deepseek.json` (executable-triage-v1; 1,083 fixtures, 500 generated returns,
seed 20261026, 537 partial records). Full ruling text is in each log and its sidecar (proposed in
`.transcription/proposed/sa.json` and `sa.deepseek.json`).

## Backlog round (2026-11-03)

Fresh reviews of 2026-11-03 (claude-opus-5-5 and deepseek-flash, and gpt-6-astra for the transcription) after the backlog packages; the change record of this form's package is `research/audits/ptc-sa/PROPOSED_BUGS.md`. Triage: `../triage/<stem>.json`, executable-triage-v2 rerun 2026-11-03 for these stems (1,495 fixtures, 500 generated returns seed 20261026, 40 partial bases), with every completed-return witness enumerated by an uncapped scratch rerun where a ruling counts them. Full ruling text: `.transcription/proposed/bklg/{transcription,render}.sa[.<family>].json`. The sa changes are PENDING-2 and PENDING-4 (wording of `sa.line1`, `sa.line5a` to `sa.line5c`); no expression changed. Line 9 now reads `f4952.line8`, gated on `f4952.used` by PENDING-6 of credits-misc. Completed-return value differences: `sa.age65` (Claude 17, deepseek 16; the candidates' readings), and `sa.itemizes`/`sa.deduction` only on `classm.f5695.8.deepseek`, a single record answering the married-filing-separately question Yes. Class M: no open section.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | sa.age65 | model error | 2,427 of 2,521 agree; completed: 17 value | f1040s1a line 36a; i1040gi p. 33 | Reads any line 12d box for a question about you (17 completed value witnesses). |
| claude | transcription | sa.itemizes | model error | 1,392 of 2,521 agree; completed: 170 candidate-unknown, 3 candidate-refuses, 3 value | i1040gi pp. 14, 33; i1040sca p. 11 | Spouse-itemizes without MFS; gambling losses without winnings; value only on an unreachable single record. |
| claude | transcription | sa.deduction | model error | 1,388 of 2,521 agree; completed: 171 candidate-unknown, 3 candidate-refuses, 2 value | i1040gi p. 34 | Inherited from sa.itemizes and line 16. |
| claude | transcription | 16 | model error | 1,035 of 2,521 agree; completed: 144 candidate-unknown | i1040sca p. 11, Line 16 | Needs gambling losses without winnings. |
| claude | render | 1 | scope | MISMATCH | i1040sca p. 2, Line 1 | The claimable-filer person is unreachable: sa.dependent refuses. |
| claude | render | 9 | representation | UNCLEAR | f4952 p. 3, Who Must File | A filer under the exception still has line 1 above zero, so line 8 is computed. |
| deepseek | transcription | sa.age65 | model error | 2,475 of 2,520 agree; completed: 16 value | f1040s1a line 36a | Counts the spouse (16 completed value witnesses). |
| deepseek | transcription | sa.itemizes | model error | 1,374 of 2,520 agree; completed: 165 candidate-unknown, 13 candidate-refuses, 1 value | i1040gi p. 33, death of spouse; p. 14; i1040sca p. 11 | No died-before-65 rule; spouse-itemizes without MFS; gambling losses. |
| deepseek | transcription | sa.deduction | model error | 1,369 of 2,520 agree; completed: 165 candidate-unknown, 13 candidate-refuses, 1 value | i1040gi p. 34 | Inherited. |
| deepseek | transcription | 5e | scope | 2,463 of 2,520 agree; completed: none | i1040sca p. 7, worksheet line 10 | Same amount; its excluded-income refusal on refused returns. |
| deepseek | transcription | 16 | model error | 1,027 of 2,520 agree; completed: 143 candidate-unknown | i1040sca p. 11 | As Claude. |
| deepseek | transcription | 9 | interface gap | 2,304 of 2,520 agree; completed: 13 candidate-refuses, 13 candidate-unknown | f4952 p. 3; i1040sca p. 9 | Rebuilds line 8 from lines 3 and 6 (pre-PENDING-6 screens); pages lacked Form 4952 and i1040sca p. 9. |
| deepseek | render | 1 | scope | MISMATCH | i1040sca p. 2, Line 1 | As Claude. |
| deepseek | render | 2 | ambiguity | MISMATCH | Schedule A line 2 | amb.2025.sa_medical_negative_agi. |
| gpt | transcription | sa.itemizes | model error | 1,397 of 2,521 agree; completed: 155 candidate-unknown, 3 candidate-refuses | i1040sca p. 11 | Selection equal; gambling losses without winnings; sa.spouse_extra on single records. |
| gpt | transcription | sa.deduction | model error | 1,385 of 2,521 agree; completed: 155 candidate-unknown, 3 candidate-refuses | i1040gi p. 34 | Inherited. |
| gpt | transcription | 5e | scope | 2,162 of 2,521 agree; completed: none | i1040sca p. 7, worksheet line 10 | Same amount; refusals only. |
| gpt | transcription | 16 | model error | 1,029 of 2,521 agree; completed: 142 candidate-unknown | i1040sca p. 11 | As Claude. |

## Earlier rounds (superseded subject)

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | sa.age65 | model error | 2,070/2,120 agree; 50 value | f1040s1a lines 36a–36b; i1040gi p. 33, line 12d | Counts the spouse in a question about you, which would give the taxpayer the senior deduction on line 36a. |
| claude | sa.itemizes | model error | 1,270/2,120 agree; 790 candidate-unknown, 59 candidate-refuses, 1 project-refuses | i1040sca p. 11, gambling losses; Schedule A line 18 | Comparison matches, but its line 17 needs gambling losses with no winnings; refusals are MFS (refused by scope.ready) or gates the project hits on sa.deduction. |
| claude | sa.deduction | model error | 1,285/2,120 agree; 799 candidate-unknown, 35 candidate-refuses, 1 project-refuses | i1040gi p. 34, line 12e; i1040sca p. 11 | Same selection; line 12e unknown wherever its line 16 needs unneeded losses; no value differences. |
| claude | 5e | scope | 2,006/2,120 agree; 52 candidate-refuses, 53 candidate-unknown, 9 project-refuses | i1040sca p. 7, SALT worksheet lines 1–10 | Formula agrees on every return; differences are excluded-income and unsupported screens placed on 5d/5e instead of line 17. |
| claude | 16 | model error | 879/2,120 agree; 1,116 candidate-unknown, 91 project-refuses, 34 project-unknown | i1040sca p. 11; amb.2025.gambling_losses | Unguarded smaller_of needs gambling losses when there are no winnings and the line is zero; project's extra line-16 screens are also on line 17. |
| deepseek | sa.age65 | model error | 2,066/2,120 agree; 54 value | f1040s1a lines 36a–36b | Counts any person's age box for a question about you. |
| deepseek | sa.itemizes | model error | 1,178/2,120 agree; 13 value, 814 candidate-unknown, 43 candidate-refuses, 69 project-refuses, 3 project-unknown | i1040gi p. 33, line 12d; p501 p. 23 | Counts people not boxes, ignores died-before-65, and compares its own wrong line 17 (lines 9, 12, 16). |
| deepseek | sa.deduction | model error | 987/2,120 agree; 226 value, 823 candidate-unknown, 32 candidate-refuses, 52 project-refuses | i1040gi pp. 33–34, lines 12d–12e | Both amounts it chooses between are wrong as ruled at sa.itemizes. |
| deepseek | 5e | model error | 2,032/2,120 agree; 4 value (all MFS), 51 candidate-refuses, 24 candidate-unknown, 9 project-refuses | i1040sca p. 7, SALT worksheet line 1 | Halves $40,000 at line 1 and again at line 10 for MFS; MFS is refused by every interview, so no in-scope amount differs. |
| deepseek | 16 | model error | 879/2,120 agree; 1,116 candidate-unknown, 91 project-refuses, 34 project-unknown | i1040sca p. 11; amb.2025.gambling_losses | As in the Claude log. |
| deepseek | 9 | interface gap | 1,485/2,120 agree; 635 value | f4952 lines 7–8; i1040sca p. 9 | Copies Form 4952 line 7 (carryforward) instead of line 8; no Form 4952 page or line 9 instruction was given and the interface entries are unlabeled. |
| deepseek | 12 | model error | 1,367/2,120 agree; 401 value, 197 project-refuses, 155 project-unknown | i1040sca p. 10, line 12 | Enters zero claiming no gift input, though the gift collection is in its interface. |

Findings: none. Project lines unchanged.
