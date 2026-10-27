# Adjudication — carloan

Method: `README.md` in this directory. Triage records: `../triage/carloan.json`,
`../triage/carloan.deepseek.json` (executable-triage-v1; 1,083 fixtures, 500 generated returns,
seed 20261026, 77 partial records). Full ruling text is in each log and its sidecar.

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | 22(iii) | representation | 111/141 agree; 28 candidate-unknown, 2 value | i1040gi p. 110, line 22 column (ii) | Column (ii) can be nonzero only with a Schedule C inside scope (Schedules E and F refused by `scope.schedule1`); every difference is a return without one. |
| deepseek | 22(iii) | model error | 102/141 agree; 32 candidate-unknown, 4 project-unknown, 3 value | fr-2025-24154 p. 21, proposed § 1.163-16(d)(2)(iii)(A) | Prorates every loan, mixed or not, so it requires the amount financed on loans the text needs no allocation for. |

Findings: none. Project lines unchanged.
