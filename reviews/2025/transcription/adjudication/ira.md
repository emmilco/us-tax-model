# Adjudication — ira

Method: `README.md` in this directory. Triage records: `../triage/ira.json`, `../triage/ira.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 57 partial records). Every
differing record, not only the recorded witnesses, was classified by rerunning the same evaluator without
the witness cap. Full ruling text is in each log and its sidecar.

Recurring facts. The project asks `person.sav_trad` (Yes/No) before the amount `person.ira_trad`; both
candidates read the amount directly, so after No it is unsupplied though necessarily zero. `person.plan`
is asked only with a Schedule C (amb.2025.ira_covered). The worksheet applies only with traditional
contributions (i1040gi p. 95), so lines shown on a return without them reach no amount. "Refused
elsewhere" means the project refuses scope.ready, Form 1040 line 24 or Schedule 1 line 20 for another
cited gate. Skipped-line rule (README): a nonzero amount on a skipped line of a reachable return is a
defect of the side producing it; the project shows zero on every skipped line.

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | ira.anyone_covered | representation | 1476/1640 agree; 140 value, 17 candidate-unknown, 7 project-unknown | i1040gi p. 96, self-employed SEP/SIMPLE coverage | Every difference is `person.plan` supplied or needed for a person with no Schedule C, which the interview never asks. |
| claude | ira.cov_gate | representation | 1617/1640; 23 candidate-unknown | i1040gi p. 31, Lines 6a and 6b, Exception | Unknowns come from the unasked `ira_trad` amount (zero) or `person.plan` without a Schedule C. |
| claude | ira.kbh_short | model error | 1472/1640; 148 candidate-unknown, 10 value, 10 candidate-refuses | i1040gi p. 98, Caution; p. 95 | Drops the traditional-contribution condition and refuses joint low-income returns with no contributions (classm.sli.4, classm.ssb.4). |
| claude | ira.both_kinds | representation | 1617/1640; 23 candidate-unknown | i1040gi p. 95, item 2 | Same broad reading (amb.2025.ira_both_kinds); unknowns are the unasked zero amount. |
| claude | ira.over_comp | scope | 599/1640; 987 candidate-unknown, 52 candidate-refuses, 2 value | p590a p. 35, Excess Contributions | Both value records are refused elsewhere; where they could differ the project refuses an excess contribution with a cited screen. |
| claude | ira.special_gate | model error | 674/1640; 966 candidate-unknown | i1040gi p. 95, "read the following list before you fill in the worksheet" | Asks the special-case screen and would refuse on it without any traditional contribution. |
| claude | ira.combat_gate | model error | 1599/1640; 21 candidate-unknown, 20 value | i1040gi p. 98, line 8, nontaxable combat pay | Refuses combat-pay returns with no IRA contribution (stage8.refuse.s8812.combat_pay). |
| claude | ira.excl_gate | model error | 1596/1640; 36 candidate-unknown, 8 value | i1040gi p. 96, Form 2555 or 8815 | Omits the contribution condition; needs coverage on returns without contributions. |
| claude | ira.line20 | model error | 520/1640; 1016 candidate-unknown, 102 candidate-refuses, 2 project-refuses | i1040gi p. 98, line 12 | No value differs; inherits the kbh_short refusal on 5 reachable no-contribution returns; other kinds representation or scope. |
| claude | 1a | representation | 530/1640; 938 candidate-unknown, 172 value | i1040gi p. 97, line 1; p. 95 | All differences on returns without contributions or with `person.plan` and no Schedule C. |
| claude | 1b | representation | 1466/1640; 136 candidate-unknown, 38 value | i1040gi p. 97, line 1 | As 1a, spouse column. |
| claude | 2a | model error | 18/1640; 1419 value, 184 candidate-unknown, 14 project-unknown, 5 candidate-refuses | i1040gi p. 97, "skip lines 2 through 6" | Skipped-line rule: candidate enters line 2 on 176 reachable returns where no one is covered (stage16.ira.i6: $89,000, project $0); MFS refusals fall under s3.mfs. |
| claude | 2b | model error | 7/1640; 1483 value, 136 candidate-unknown, 14 project-unknown | i1040gi p. 97; p. 95 item 6 | Skipped-line rule: 176 reachable returns with an amount on a skipped line (classm.f5695.2: $246,000, project $0). |
| claude | 6a | model error | 469/1640; 610 value, 373 candidate-refuses, 188 candidate-unknown | i1040gi p. 97, "skip lines 2 through 6" | Skipped-line rule: 94 reachable returns (stage16.ira.i6: $84,000, project $0); refusals are on returns refused elsewhere. |
| claude | 6b | model error | 493/1640; 626 value, 373 candidate-refuses, 148 candidate-unknown | i1040gi p. 97; p. 95 item 6 | Skipped-line rule: 92 reachable returns (classm.f5695.3: $72,349, project $0). |
| claude | 7a | representation | 93/1640; 943 candidate-unknown, 517 value, 87 candidate-refuses | i1040gi p. 97; p. 95 | All value records have no contributions; on contributing returns rates, thresholds and the $200 floor agree. |
| claude | 7b | representation | 1397/1640; 136 candidate-unknown, 69 value, 24 candidate-refuses, 14 project-unknown | i1040gi p. 97; p. 95 item 6 | As 7a. |
| claude | 8 | model error | 677/1640; 949 candidate-unknown, 12 candidate-refuses, 2 project-refuses | i1040gi p. 98, line 8; p. 95 list | Wages agree; the line's special-case and combat refusals lack the contribution condition. |
| claude | 9 | ambiguity | 671/1640; 921 candidate-unknown, 46 project-refuses, 2 value | p590a p. 7, Self-employment loss | Per-spouse floor (amb.2025.ira_se_floor) against combined floor (generated 293: $157,316.78 / $109,209.37); unconditional ira.se_capital screen partly model error. |
| claude | 11a | representation | 693/1640; 947 candidate-unknown | i1040gi p. 98, line 11 | Unasked zero amount. |
| claude | 11b | representation | 1505/1640; 134 candidate-unknown, 1 project-unknown | i1040gi p. 98, line 11 | Unasked zero amount; one roster the interview cannot produce. |
| claude | 12a | model error | 538/1640; 996 candidate-unknown, 104 candidate-refuses, 2 project-refuses | i1040gi p. 98, line 12 | No value differs; inherits kbh_short refusal on 6 reachable returns. |
| claude | 12b | model error | 556/1640; 1006 candidate-unknown, 78 candidate-refuses | i1040gi p. 98, line 12 | As 12a. |
| deepseek | ira.anyone_covered | representation | 1640/1640 agree | i1040gi p. 96 | Observed equivalence on the sample. |
| deepseek | ira.cov_gate | model error | 645/1640; 925 candidate-unknown, 70 value | i1040gi p. 31, Exception | Copies anyone_covered, dropping benefits and contributions (stage16.ira.i1). |
| deepseek | ira.kbh_short | model error | 1473/1640; 148 candidate-unknown, 10 value, 9 candidate-refuses | i1040gi p. 98, Caution | Drops the contribution condition, as in the Claude log. |
| deepseek | ira.both_kinds | model error | 1439/1640; 200 candidate-unknown, 1 value | i1040gi p. 95, item 2 | No joint-return condition: refuses a single filer with both kinds (stage16.mut.ira_trad_and_roth, project $3,000). |
| deepseek | ira.over_comp | scope | 611/1640; 987 candidate-unknown, 41 candidate-refuses, 1 value | p590a p. 35 | Only value record refused elsewhere; project's stricter screen is cited. |
| deepseek | ira.special_gate | model error | 674/1640; 966 candidate-unknown | i1040gi p. 95, list | As in the Claude log. |
| deepseek | ira.combat_gate | model error | 1621/1640; 18 project-unknown, 1 value | i1040gi p. 98, line 8 | Constant false: leaves nontaxable combat pay off line 8 (stage16.refuse.ira.combat_pay computed $5,000). |
| deepseek | ira.excl_gate | model error | 1622/1640; 17 project-unknown, 1 value | i1040gi p. 96 | Constant false: computes the covered Form 2555 case the source sends to Pub. 590-A. |
| deepseek | ira.line20 | model error | 576/1640; 1006 candidate-unknown, 51 candidate-refuses, 6 project-refuses, 1 value | i1040gi p. 97, line 6 | stage16.ira.i2: $200 deducted where line 5 is not less than line 2 (project $0). |
| deepseek | 1a | representation | 668/1640; 924 candidate-unknown, 48 value | i1040gi p. 97, line 1 | All on returns without contributions. |
| deepseek | 1b | representation | 1496/1640; 134 candidate-unknown, 10 value | i1040gi p. 97, line 1 | As 1a. |
| deepseek | 2a | model error | 18/1640; 1475 value, 133 candidate-unknown, 14 project-unknown | i1040gi p. 97 | Skipped-line rule: 180 reachable returns (stage16.ira.i6: $89,000, project $0); MFS refused by s3.mfs. |
| deepseek | 2b | model error | 9/1640; 1485 value, 132 candidate-unknown, 14 project-unknown | i1040gi p. 97; p. 95 item 6 | Skipped-line rule: 180 reachable returns (stage16.mut.ira_kbh_none_edge: $246,000, project $0). |
| deepseek | 6a | model error | 500/1640; 628 value, 372 candidate-refuses, 140 candidate-unknown | i1040gi p. 97 | Skipped-line rule: 99 reachable returns (stage16.ira.i6: $84,000, project $0); refusals on returns refused elsewhere. |
| deepseek | 6b | model error | 493/1640; 635 value, 373 candidate-refuses, 139 candidate-unknown | i1040gi p. 97; p. 95 item 6 | Skipped-line rule: 99 reachable returns (stage16.ira.i7: $146,000, project $0). |
| deepseek | 7a | model error | 48/1640; 947 candidate-unknown, 620 value, 25 candidate-refuses | i1040gi p. 97, line 6 | $200 floor on a zero line 6a (stage16.ira.i2) and a percentage above the threshold ($7,010 / $7,000). |
| deepseek | 7b | model error | 27/1640; 925 candidate-unknown, 651 value, 37 candidate-refuses | i1040gi p. 97, line 6 threshold | stage16.ira.i1: $83,650 where the applicable $7,000 applies. |
| deepseek | 8 | model error | 688/1640; 949 candidate-unknown, 2 project-refuses, 1 candidate-refuses | i1040gi p. 98, line 8; p. 95 list | Wages agree; refuses on ira.special with no contribution condition. |
| deepseek | 11a | representation | 693/1640; 947 candidate-unknown | i1040gi p. 98, line 11 | Unasked zero amount. |
| deepseek | 11b | representation | 1505/1640; 135 candidate-unknown | i1040gi p. 98, line 11 | Unasked zero amount. |
| deepseek | 12a | model error | 595/1640; 985 candidate-unknown, 53 candidate-refuses, 6 project-refuses, 1 value | i1040gi p. 98, line 12; p. 97 line 6 | stage16.ira.i2 $200 / $0; refuses reachable both_kinds and kbh_short returns. |
| deepseek | 12b | model error | 584/1640; 989 candidate-unknown, 67 candidate-refuses | i1040gi p. 98, line 12 | Refuses reachable both_kinds and kbh_short returns. |

Findings: none. Project lines unchanged.
