# Adjudication — ssb

Method: `README.md` in this directory. Triage record: `../triage/ssb.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 168 partial records).
DeepSeek family only. Full ruling text is in the log and its sidecar.

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| deepseek | ssb.has_benefits | representation | 1,751/1,751 agree | i1040gi p. 31, Lines 6a and 6b | Both test the box 5 total; line 1 copies ssb.benefits. |
| deepseek | 6 | ambiguity | 1,738/1,751 agree; 11 candidate-unknown, 1 candidate-refuses, 1 project-refuses | i1040gi p. 32, line 6; p. 31, Exception | Reads Schedule 1 line 20 literally, the text at issue of amb.2025.ira_ssb_copy; the witnesses show the line 20 to line 9 cycle the register resolves. |
| deepseek | 8 | representation | 1,751/1,751 agree | i1040gi p. 32, line 8 | Same status amounts; guards grouped differently. |
| deepseek | 10 | representation | 1,751/1,751 agree | i1040gi p. 32, line 10 | Same status amounts; guards grouped differently. |
| deepseek | 16 | scope | 1,722/1,751 agree; 23 project-unknown, 5 project-refuses, 1 candidate-refuses | i1040gi p. 32, line 8; p. 31, Line 6c | Same computation; the project's lump-sum refusal sits on line 2, the candidate's on line 18, so line 6b refuses on both. |
| deepseek | 18 | model error | 529/1,751 agree; 986 candidate-unknown, 232 candidate-refuses, 4 project-refuses | i1040gi p. 31, Line 6c, "If any of your benefits are taxable" | No zero-benefit guard and an unconditional lump-sum refusal, so it asks the lump-sum election on every return. |

Findings: none. Project lines unchanged.
