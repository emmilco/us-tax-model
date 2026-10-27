# Adjudication — refund

Method: `README.md` in this directory. Triage record: `../triage/refund.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 295 partial records over
17 bases). DeepSeek family only. Full ruling text is in the log and its sidecar.

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
