# Adjudication — sa

Method: `README.md` in this directory. Triage records: `../triage/sa.json`,
`../triage/sa.deepseek.json` (executable-triage-v1; 1,083 fixtures, 500 generated returns,
seed 20261026, 537 partial records). Full ruling text is in each log and its sidecar (proposed in
`.transcription/proposed/sa.json` and `sa.deepseek.json`).

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
