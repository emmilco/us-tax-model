# Transcription agreement — ira

Second transcription of `IRA Deduction Worksheet — Schedule 1, Line 20` by an isolated model (spec 6.5), compared line by line with `forms/2025/ira.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 53efe5dc0d1cf071417b3ec0216910fbdbe21e411edd3bdf2fce715f0e47a71e |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 579a196b9778f3baa5bc58f6bbede861cc899fdd80ea9762a29017b7d72dd960 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 73d69e1a339b596759a13fbe27014c5001245845d806c3c823008847d474da26 |
| printed lines compared | 29 |
| agree / disagree / missing | 7 / 22 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 95, 96, 97, 98 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31, 95, 96, 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p590a | 2025 | 6, 7, 16, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 6, 7, 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| i8606 | 2025 | 5 | cited pages | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 5 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| f8606 | 2025 | 1, 2 | whole document | 1e2747fd38afcfefc11564f9673556808470614c153f2d34458afe98a560cb2c | - | 47a023b69eb81610f8bf73059c609131854d900f1694660f8496a7791f974233 |

## Lines

### ira.joint — Married filing jointly
Status: **AGREE**

### ira.joint_type — Married filing jointly or qualifying surviving spouse
Status: **AGREE**

### ira.anyone_covered — You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "any"}
```

Ruling: representation; i1040gi p. 96: "You are also covered by a plan if you were self-employed and had a SEP, SIMPLE, or qualified retirement plan." The candidate reads person.ira_cov per column, as the project does. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1640 of 1640 comparisons agree; no differences. Observed equivalence on this sample, not proof. Project stands.

### ira.cov_gate — Social security benefits, traditional IRA contributions for 2025, and you or your spouse c
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "ssb.line1"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "any"}
```

Ruling: model error; i1040gi p. 31, Lines 6a and 6b, Exception: "You made contributions to a traditional IRA for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment. Instead, use the worksheets in Pub. 590-A". The candidate's gate copies ira.anyone_covered and drops both the social security benefits and the traditional contributions the exception names. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 645 of 1640 comparisons agree; 925 candidate-unknown, 70 value. The 70 value records are returns with a covered person but no social security benefits or no traditional contributions (stage16.ira.i1, stage16.ira.i2, audit.ira.covered_age50_joint_phaseout: project false, candidate true); bound in place of the project's gate, it also changes when the Social Security worksheet's IRA copy (person.ira_ssb_figured) refuses. The 925 candidate-unknown records are no-contribution returns where the candidate needs coverage the source does not. Project stands.

### ira.kbh_short — Married filing jointly with traditional IRA contributions and line 10 less than the amount
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"line": "10"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "ira.kbh_none"}}, {"guard": {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}}, {"const": 2, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "ira.kbh_one"}}, {"guard": {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}}], "test": "le"}, "then": {"param": "ira.kbh_both"}}], "op": "choose"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"line": "10"}, {"alternatives": [{"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}}], "test": "eq"}, "then": {"param": "ira.kbh_none"}}, {"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}}], "test": "eq"}, "then": {"param": "ira.kbh_one"}}, {"guard": {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}}], "test": "le"}, "then": {"param": "ira.kbh_both"}}], "op": "choose"}], "test": "lt"}], "test": "all"}
```

Ruling: model error; i1040gi p. 98, Caution: "If married filing jointly and line 10 is less than $14,000 ($15,000 if one spouse is age 50 or older at the end of 2025; $16,000 if both spouses are age 50 or older at the end of 2025), stop here and use the worksheet in Pub. 590-A to figure your IRA deduction." The caution is part of a worksheet used only with traditional contributions (i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction."); the candidate drops that condition. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1473 of 1640 comparisons agree; 148 candidate-unknown, 10 value, 9 candidate-refuses. The 10 value records are joint returns without contributions and line 10 under the caution amount, where the candidate refuses lines 12a, 12b and 20; classm.sli.4 and classm.ssb.4 are refused by nothing else. The 148 candidate-unknown records are no-contribution joint returns where its line 10 needs ira.special (its line 8 refusal) or ira.se_capital; the 9 candidate-refuses records (generated 113, 121, 169) are returns refused by other cited gates (scope). Project stands.

### ira.both_kinds — A joint return on which you or your spouse made contributions to both a traditional IRA an
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.sav_roth", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": 0}, {"ref": "person.ira_trad"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "person.sav_roth"}], "test": "lt"}], "test": "all"}}], "test": "lt"}
```

Ruling: model error; i1040gi p. 95, Line 20, item 2: "If you are filing a joint return and you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, don’t use the IRA Deduction Worksheet in these instructions." The candidate counts a person with both kinds on any return and omits the joint-return condition. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1439 of 1640 comparisons agree; 200 candidate-unknown, 1 value. The value record stage16.mut.ira_trad_and_roth is a single return with traditional and Roth contributions: the candidate's gate is true and its lines 12a, 12b and 20 refuse, where the project figures a $3,000 deduction and the item does not apply. (Its per-person count is also the narrow reading amb.2025.ira_both_kinds rejects, not observed on this sample.) The 200 candidate-unknown records answer No to person.sav_trad and supply no amount, which is necessarily zero (representation). Project stands.

### ira.over_comp — Traditional and Roth IRA contributions for 2025 more than the compensation on line 10
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"line": "10"}, {"of": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.sav_roth", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"line": "10"}, {"line": "11a"}], "test": "lt"}, {"args": [{"line": "10"}, {"line": "11b"}], "test": "lt"}], "test": "any"}
```

Ruling: scope; p590a p. 35, Excess Contributions: "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of: • $7,000 ($8,000 if you are age 50 or older), or • Your taxable compensation for the year." The project refuses when traditional plus Roth contributions exceed line 10 (with person.ira_over_limit for the dollar limit); the candidate compares each column's traditional contributions with line 10 alone. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 611 of 1640 comparisons agree; 987 candidate-unknown, 41 candidate-refuses, 1 value. The single value record, stage16.refuse.ira.kbh_short (project true, candidate false), is refused by ira.kbh_short anyway; where the lines can differ on a reachable return (Roth contributions taking the total above compensation), the project refuses with this cited screen an excess the tool does not prepare. The 41 candidate-refuses records are returns refused by other gates; the 987 candidate-unknown records answer No to person.sav_trad (amount necessarily zero) or are no-contribution partial records on which a zero line 11 cannot exceed line 10. Project stands.

### ira.special_gate — Traditional IRA contributions with an IRA deduction special case (screen)
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"line": "(screen)"}
```

Ruling: model error; i1040gi p. 95, Line 20: "Use the IRA Deduction Worksheet to figure the amount, if any, of your IRA deduction. But read the following list before you fill in the worksheet." The candidate's gate is ira.special itself, with no contribution condition (i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction."), and its line 8 refuses on it. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 674 of 1640 comparisons agree; 966 candidate-unknown. All 966 candidate-unknown records have no traditional contributions (classm.f2441.1.deepseek, classm.asset.2, partial classm.s3.2 without ira.special), where the project does not ask the screen; the candidate requires an answer the source does not need and would refuse such a return. Project stands.

### ira.combat_gate — Traditional IRA contributions with nontaxable combat pay
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"ref": "s8812.combat_pay"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": false}, {"const": true}], "test": "eq"}
```

Ruling: model error; i1040gi p. 98, line 8: "Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q or reported on Form 1040, line 1i." The candidate's gate is the constant false, so its line 8 leaves out nontaxable combat pay, which the source puts on line 8. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1621 of 1640 comparisons agree; 18 project-unknown, 1 value. The value record stage16.refuse.ira.combat_pay (combat pay with traditional contributions) is refused by the project and computed by the candidate ($5,000 on line 20) without the combat pay. The 18 project-unknown records omit person.sav_trad (stage16.hsa.partial.H01, classm.f8889.3), which the interview asks; the project needs to know of contributions before it can rule combat pay out. Project stands.

### ira.excl_gate — Traditional IRA contributions, someone covered by a retirement plan, and Form 2555 or 4563
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"ref": "sa.excluded_income"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": false}, {"const": true}], "test": "eq"}
```

Ruling: model error; i1040gi p. 96: "If you were covered by a retirement plan and you file Form 2555 or 8815, or you exclude employer-provided adoption benefits, see Pub. 590-A to figure the amount, if any, of your IRA deduction." The candidate's gate is the constant false, so it figures the deduction with the worksheet where the source sends a covered filer with Form 2555 to Pub. 590-A. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1622 of 1640 comparisons agree; 17 project-unknown, 1 value. The value record stage16.refuse.ira.excluded_income is refused by the project and computed by the candidate ($2,800 on line 20). The 17 project-unknown records omit person.sav_trad, which the interview asks. Project stands.

### ira.line20 — The total of lines 12a and 12b for Schedule 1, line 20
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_deduction", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"line": "12a"}, {"line": "12b"}], "op": "sum"}
```

Second transcription's note: If the filer elects to deduct a smaller amount and treat the rest as a nondeductible contribution, the smaller amount is not determined here; line 20 refuses via ira.deduct_less.

Ruling: model error; i1040gi p. 97, line 6: "Is the amount on line 5 less than the amount on line 2?" with the No answer "None of your IRA contributions are deductible.". Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 576 of 1640 comparisons agree; 1006 candidate-unknown, 51 candidate-refuses, 6 project-refuses, 1 value. The value record stage16.ira.i2 (single, covered, line 5 $90,000, line 2 $89,000, so line 6a is No): the project deducts $0; the candidate's line 7a takes the $200 floor on a zero line 6a and deducts $200. Of the 51 candidate-refuses records, stage16.mut.ira_trad_and_roth (single; its ira.both_kinds) and 5 no-contribution joint returns (its ira.kbh_short) are reachable returns the source computes; the rest are refused by other gates (scope). The 6 project-refuses records are cited scope screens (person.ira_excess_gate, person.ira_over_limit, ira.over_comp, ira.excl_gate, ira.combat_gate, person.ira_dist_gate), the last three of which the candidate ignores (ruled on those gates). The 1,006 candidate-unknown records mostly need ira.deduct_less on returns with no deduction, where the answer is necessarily No (representation). Project stands.

### 1a — Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Ruling: representation; i1040gi p. 97, line 1: "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?" and "If married filing jointly, was your spouse covered by a retirement plan?"; i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction." The candidate reads person.ira_cov without the contribution condition the project's shown line carries; the deduction reads person.ira_cov on both sides. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 668 of 1640 comparisons agree; 924 candidate-unknown, 48 value. All 48 value records have no traditional contributions (classm.f8880.1, stage14.sep.basic, classm.f5695.5); all 924 candidate-unknown records are no-contribution returns where coverage is not asked. On a return with no traditional IRA contributions the worksheet is not used and no amount reads the line. Project stands.

### 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Ruling: representation; i1040gi p. 97, line 1: "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?" and "If married filing jointly, was your spouse covered by a retirement plan?"; i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction." Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1496 of 1640 comparisons agree; 134 candidate-unknown, 10 value. All 10 value records are joint returns without traditional contributions (classm.ira.2, classm.se.2); the 134 candidate-unknown records are no-contribution returns where spouse coverage is not asked (two of them rosters the interview cannot produce: stage13.refuse.single_with_spouse, ss.person.separation). On a return with no traditional IRA contributions the worksheet is not used and no amount reads the line. Project stands.

### 2a — Enter the amount shown below that applies to you (your IRA)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"line": "1a"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second transcription's note: For married filing separately living apart, the supplied ira.line2 parameter gives the married-filing-separately amount; no separate input for the line 20 checkbox is supplied.

Ruling: model error; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." Under the skipped-line rule (README), a nonzero amount on a line the source says to skip, on a reachable return, is a defect of the side producing it even when no later amount changes; the project shows zero. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 18 of 1640 comparisons agree; 1475 value, 133 candidate-unknown, 14 project-unknown. 180 value records are reachable returns (refused nowhere else) on which no one is covered, so line 2a is skipped, and the candidate enters an amount: stage16.ira.i6 (single, contributions) $0 against $89,000; stage16.mut.ira_kbh_none_edge (joint) $0 against $246,000. No deduction changes, since its line 7 takes the applicable amount when no one is covered. The 133 candidate-unknown records are no-contribution joint returns where coverage is not asked (representation); the 14 project-unknown records omit person.sav_trad, which the interview asks. The candidate's $10,000 for every separate return ignores the lived-apart amount, but married filing separately is refused for the whole return by s3.mfs (scope.ready). Project stands.

### 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"line": "1b"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"line": "1b"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second transcription's note: For married filing separately living apart, the supplied ira.line2 parameter gives the married-filing-separately amount; no separate input for the line 20 checkbox is supplied.

Ruling: model error; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." Under the skipped-line rule (README), a nonzero amount on a line the source says to skip, on a reachable return, is a defect of the side producing it even when no later amount changes; the project shows zero. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 9 of 1640 comparisons agree; 1485 value, 132 candidate-unknown, 14 project-unknown. 180 value records are reachable returns (refused nowhere else) on which no one is covered, so line 2b is skipped, and the candidate enters an amount: stage16.mut.ira_kbh_none_edge (joint) $0 against $246,000; classm.f5695.1 (no spouse’s column) $0 against $89,000. No deduction changes, since its line 7 takes the applicable amount when no one is covered. Off a joint return there is no spouse's column (i1040gi p. 95, Line 20, item 6: "You must file a joint return to deduct contributions to your spouse’s IRA."). The 132 candidate-unknown records are no-contribution joint returns where coverage is not asked (representation); the 14 project-unknown records omit person.sav_trad. Project stands.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

### 4 — Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25
Status: **AGREE**

### 5 — Subtract line 4 from line 3. If married filing jointly, enter the result in both columns
Status: **AGREE**

### 6a — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line6", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "2a"}, "op": "subtract_floor0", "take": {"line": "5"}}
```

Ruling: model error; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." Under the skipped-line rule (README), a nonzero amount on a line the source says to skip, on a reachable return, is a defect of the side producing it even when no later amount changes; the project shows zero. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 500 of 1640 comparisons agree; 628 value, 372 candidate-refuses, 140 candidate-unknown. 99 value records are reachable returns (refused nowhere else) on which no one is covered, so line 6a is skipped, and the candidate enters an amount: stage16.ira.i6 $0 against $84,000; classm.f5695.1 $0 against $56,064. No deduction changes, since its line 7 takes the applicable amount when no one is covered. The 372 candidate-refuses records come from figuring line 5 on every return, and every one of them is a return the project refuses on scope.ready, Form 1040 line 24 or Schedule 1 line 20 for another cited gate (scope); the 140 candidate-unknown records are no-contribution returns needing coverage or line 5 inputs (representation). Project stands.

### 6b — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line6", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "2b"}, "op": "subtract_floor0", "take": {"line": "5"}}
```

Ruling: model error; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." Under the skipped-line rule (README), a nonzero amount on a line the source says to skip, on a reachable return, is a defect of the side producing it even when no later amount changes; the project shows zero. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 493 of 1640 comparisons agree; 635 value, 373 candidate-refuses, 139 candidate-unknown. 99 value records are reachable returns (refused nowhere else) on which no one is covered, so line 6b is skipped, and the candidate enters an amount: stage16.ira.i7 (joint) $0 against $146,000; classm.f5695.1 (no spouse’s column) $0 against $56,064. No deduction changes, since its line 7 takes the applicable amount when no one is covered. The 373 candidate-refuses records come from figuring line 5 on every return, and every one of them is a return the project refuses on scope.ready, Form 1040 line 24 or Schedule 1 line 20 for another cited gate (scope); the 139 candidate-unknown records are no-contribution returns needing coverage or line 5 inputs (representation). Project stands.

### 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.ira_line7", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"line": "1a"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "any"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 97, line 6: "Is the amount on line 5 less than the amount on line 2?" with the No answer "None of your IRA contributions are deductible."; i1040gi p. 97, line 6: "If married filing jointly or qualifying surviving spouse, and the result is $20,000 or more ($10,000 or more in the column for the IRA of a person who wasn’t covered by a retirement plan), enter the applicable amount below on line 7 for that column and go to line 8." The candidate multiplies whenever someone is covered: it gives the $200 floor when line 6a is zero and a percentage when line 6a is at or above the threshold. Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 48 of 1640 comparisons agree; 947 candidate-unknown, 620 value, 25 candidate-refuses. stage16.ira.i2 (single, line 5 not less than line 2): $0 against $200, which reaches line 12a and Schedule 1 line 20; stage16.mut.ira_joint_full_edge (joint, line 6a over $20,000): $7,000 against $7,010. The other 618 value records are no-contribution returns (zero against the applicable amount, no deduction either way); the 947 candidate-unknown records are no-contribution returns needing coverage or age; the 25 candidate-refuses records are returns refused for other gates. Project stands.

### 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.ira_line7", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"line": "1a"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "any"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 97, line 6: "If married filing jointly or qualifying surviving spouse, and the result is $20,000 or more ($10,000 or more in the column for the IRA of a person who wasn’t covered by a retirement plan), enter the applicable amount below on line 7 for that column and go to line 8." Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 27 of 1640 comparisons agree; 925 candidate-unknown, 651 value, 37 candidate-refuses. stage16.ira.i1 (joint, spouse not covered, line 6b at least $10,000): the project enters the applicable $7,000 and the candidate $83,650 (70% of line 6b); stage16.mut.ira_joint_full_edge: $7,000 against $84,010. The candidate also figures line 7b on returns that are not joint (stage16.ira.i3: $0 against $2,800), which have no spouse's column (i1040gi p. 95, Line 20, item 6: "You must file a joint return to deduct contributions to your spouse’s IRA."); line 11b is zero there. The 925 candidate-unknown records are no-contribution returns needing coverage or age; the 37 candidate-refuses records are returns refused for other gates. Line 12b is capped by line 11b, so on the sample no deduction differs, but the printed line is wrong. Project stands.

### 8 — Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "person", "field": "person.box1", "op": "sum_over", "where": null}, {"ref": "s1.line2a"}], "op": "sum"}
```

Second:

```json
{"of": [{"ref": "f1040.line1a"}, {"ref": "s1.line2a"}], "op": "sum"}
```

Second transcription's note: Nontaxable combat pay is not represented in the supplied input interface; line 8 includes wages and alimony only.

Ruling: model error; i1040gi p. 98, line 8: "Wages, salaries, tips, etc. Generally, this is the amount reported in box 1 of Form W-2." The candidate's wages equal the project's on every record where both compute; the difference is its refusal on ira.special with no contribution condition (i1040gi p. 95, Line 20: "Use the IRA Deduction Worksheet to figure the amount, if any, of your IRA deduction. But read the following list before you fill in the worksheet."). Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 688 of 1640 comparisons agree; 949 candidate-unknown, 2 project-refuses, 1 candidate-refuses. All 949 candidate-unknown records need ira.special on returns with no traditional contributions (classm.f2441.1.deepseek, classm.qdcg.2). The candidate-refuses record (stage16.refuse.ira.special) is refused by the project too; the 2 project-refuses records are the cited Schedule 1 line 2a alimony screens (scope). Project's wages stand.

### 9 — Enter the earned income you (and your spouse if filing jointly) received as a self-employe
Status: **AGREE**

### 10 — Add lines 8 and 9
Status: **AGREE**

### 11a — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"collection": "person", "field": "person.ira_trad", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}
```

Ruling: representation; i1040gi p. 98, line 11: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025 to your IRA on line 11a and to your spouse’s IRA on line 11b." Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 693 of 1640 comparisons agree; 947 candidate-unknown. All 947 candidate-unknown records answer No to person.sav_trad and supply no amount: person.ira_trad is the amount question the interview asks only after Yes on person.sav_trad; the candidate reads it without that question, so on a return answered No the amount is not supplied, although it is necessarily zero. Project stands.

### 11b — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"collection": "person", "field": "person.ira_trad", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Ruling: representation; i1040gi p. 98, line 11: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025 to your IRA on line 11a and to your spouse’s IRA on line 11b."; i1040gi p. 95, Line 20, item 6: "You must file a joint return to deduct contributions to your spouse’s IRA." Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1505 of 1640 comparisons agree; 135 candidate-unknown. All 135 candidate-unknown records are returns whose spouse answered No to person.sav_trad (classm.f2441.2, stage16.mut.ira_joint_full_edge), or the roster the interview cannot produce (stage13.refuse.single_with_spouse): person.ira_trad is the amount question the interview asks only after Yes on person.sav_trad; the candidate reads it without that question, so on a return answered No the amount is not supplied, although it is necessarily zero. Project stands.

### 12a — Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your IRA)
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_deduction", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"of": [{"line": "11a"}, {"of": [{"line": "10"}, {"line": "7a"}], "op": "smaller_of"}], "op": "smaller_of"}
```

Ruling: model error; i1040gi p. 98, line 12: "On line 12a, enter the smallest of line 7a, 10, or 11a. On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct."; i1040gi p. 97, line 6: "Is the amount on line 5 less than the amount on line 2?" with the No answer "None of your IRA contributions are deductible.". Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 595 of 1640 comparisons agree; 985 candidate-unknown, 53 candidate-refuses, 6 project-refuses, 1 value. The value record stage16.ira.i2: $0 against $200, the candidate's line 7a floor on a zero line 6a. Of the 53 candidate-refuses records, stage16.mut.ira_trad_and_roth (single; its ira.both_kinds) and 6 no-contribution joint returns (its ira.kbh_short) are reachable returns the source computes; the rest are refused for other gates (scope). The 6 project-refuses records are cited scope screens (person.ira_excess_gate, person.ira_over_limit, ira.over_comp, ira.excl_gate, ira.combat_gate, person.ira_dist_gate). The 985 candidate-unknown records need coverage, the amount after No to person.sav_trad or ira.special on no-contribution returns. Project stands.

### 12b — Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your spouse's
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_deduction", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"of": [{"line": "11b"}, {"of": [{"line": "10"}, {"line": "7b"}], "op": "smaller_of"}], "op": "smaller_of"}
```

Ruling: model error; i1040gi p. 98, line 12: "On line 12a, enter the smallest of line 7a, 10, or 11a. On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct."; i1040gi p. 95, Line 20, item 6: "You must file a joint return to deduct contributions to your spouse’s IRA." Triage executable-triage-v1 (triage/ira.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 584 of 1640 comparisons agree; 989 candidate-unknown, 67 candidate-refuses. No value differs. Of the 67 candidate-refuses records, 6 no-contribution joint returns (its ira.kbh_short: classm.sli.4, classm.ssb.4) and stage16.mut.ira_trad_and_roth (its ira.both_kinds, on a single return) are reachable returns the source computes; the rest are refused for other gates (scope). The 989 candidate-unknown records need coverage, the amount after No to person.sav_trad or ira.special on no-contribution returns. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ira.kbh_short | ira.se_capital, ira.special | ira.se_capital, ira.special |
| ira.over_comp | ira.se_capital, ira.special | ira.se_capital, ira.special |
| ira.line20 | ira.both_kinds, ira.combat_gate, ira.deduct_less, ira.excl_gate, ira.kbh_short, ira.se_capital, ira.special, ira.special_gate, scope.schedule1 | ira.deduct_less, ira.se_capital, ira.special |
| 4 | scope.schedule1 | scope.schedule1 |
| 5 | scope.schedule1 | - |
| 6a | scope.schedule1 | - |
| 6b | scope.schedule1 | - |
| 7a | scope.schedule1 | - |
| 7b | scope.schedule1 | - |
| 8 | ira.special | ira.special |
| 9 | ira.se_capital | ira.se_capital |
| 10 | ira.se_capital, ira.special | ira.se_capital, ira.special |
| 12a | ira.both_kinds, ira.kbh_short, ira.se_capital, ira.special, scope.schedule1 | ira.se_capital, ira.special |
| 12b | ira.both_kinds, ira.kbh_short, ira.se_capital, ira.special, scope.schedule1 | ira.se_capital, ira.special |

## Raw second transcription

```yaml
lines:
  - id: ira.line1a
    printed: "1a"
    label: "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?"
    type: Bool
    expr:
      op: test
      gt:
        - ira.h_taxpayer_cov_count
        - {const: 0, type: Count}
  - id: ira.line1b
    printed: "1b"
    label: "If married filing jointly, was your spouse covered by a retirement plan?"
    type: Bool
    expr:
      op: test
      gt:
        - ira.h_spouse_cov_count
        - {const: 0, type: Count}
  - id: ira.line2a
    printed: "2a"
    label: "Enter the amount shown below that applies to you."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.joint, {const: true}]}
              - {op: test, eq: [ira.line1a, {const: false}]}
          then: ira.h_line2_not_covered
        - guard:
            op: test
            any:
              - {op: test, eq: [ira.joint, {const: false}]}
              - {op: test, eq: [ira.line1a, {const: true}]}
          then: ira.h_line2_status
    note: "For married filing separately living apart, the supplied ira.line2 parameter gives the married-filing-separately amount; no separate input for the line 20 checkbox is supplied."
  - id: ira.line2b
    printed: "2b"
    label: "Enter the amount shown below that applies to you."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.joint, {const: true}]}
              - {op: test, eq: [ira.line1b, {const: false}]}
          then: ira.h_line2_not_covered
        - guard:
            op: test
            any:
              - {op: test, eq: [ira.joint, {const: false}]}
              - {op: test, eq: [ira.line1b, {const: true}]}
          then: ira.h_line2_status
    note: "For married filing separately living apart, the supplied ira.line2 parameter gives the married-filing-separately amount; no separate input for the line 20 checkbox is supplied."
  - id: ira.line3
    printed: "3"
    label: "Enter the amount from Form 1040 or 1040-SR, line 9."
    type: Dollars
    expr:
      op: copy
      from: f1040.line9
  - id: ira.line4
    printed: "4"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25."
    type: NonNegDollars
    expr:
      op: sum
      of:
        - s1.line11
        - s1.line13
        - s1.line15
        - s1.line16
        - s1.line17
        - s1.line18
        - s1.line19a
        - s1.line25
    refuses: [scope.schedule1]
  - id: ira.line5
    printed: "5"
    label: "Subtract line 4 from line 3. If married filing jointly, enter the result in both columns."
    type: Dollars
    expr:
      op: subtract
      from: ira.line3
      take: ira.line4
  - id: ira.line6a
    printed: "6a"
    label: "If the amount on line 5 is less than the amount on line 2, subtract line 5 from line 2."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: ira.line2a
      take: ira.line5
  - id: ira.line6b
    printed: "6b"
    label: "If the amount on line 5 is less than the amount on line 2, subtract line 5 from line 2."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: ira.line2b
      take: ira.line5
  - id: ira.line7a
    printed: "7a"
    label: "Multiply line 6a by the applicable percentage; increase the result to the next multiple of $10; enter at least $200."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.cov_gate, {const: false}]}
          then: ira.h_full_a
        - guard: {op: test, eq: [ira.cov_gate, {const: true}]}
          then: ira.h_computed7a
  - id: ira.line7b
    printed: "7b"
    label: "Multiply line 6b by the applicable percentage; increase the result to the next multiple of $10; enter at least $200."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.cov_gate, {const: false}]}
          then: ira.h_full_b
        - guard: {op: test, eq: [ira.cov_gate, {const: true}]}
          then: ira.h_computed7b
  - id: ira.line8
    printed: "8"
    label: "Enter the total of your (and your spouse's if filing jointly) wages, salaries, tips, etc.; alimony and separate maintenance payments; and nontaxable combat pay."
    type: NonNegDollars
    expr:
      op: sum
      of:
        - f1040.line1a
        - s1.line2a
    refuses: [ira.special]
    note: "Nontaxable combat pay is not represented in the supplied input interface; line 8 includes wages and alimony only."
  - id: ira.line9
    printed: "9"
    label: "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner, minus Schedule 1 lines 15 and 16; if zero or less, enter -0-."
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_se
    refuses: [ira.se_capital]
  - id: ira.line10
    printed: "10"
    label: "Add lines 8 and 9."
    type: NonNegDollars
    expr:
      op: sum
      of:
        - ira.line8
        - ira.line9
  - id: ira.line11a
    printed: "11a"
    label: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your IRA."
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_trad
      where:
        op: test
        eq: [person.role, {const: "taxpayer"}]
  - id: ira.line11b
    printed: "11b"
    label: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your spouse's IRA."
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_trad
      where:
        op: test
        eq: [person.role, {const: "spouse"}]
  - id: ira.line12a
    printed: "12a"
    label: "Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct."
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ira.h_small_a1
        - ira.line11a
    refuses: [ira.kbh_short, ira.both_kinds]
  - id: ira.line12b
    printed: "12b"
    label: "Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct."
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ira.h_small_b1
        - ira.line11b
    refuses: [ira.kbh_short, ira.both_kinds]

  - id: ira.h_taxpayer_cov_count
    printed: "(helper)"
    label: "Taxpayer retirement plan coverage count"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.ira_cov, {const: true}]}
  - id: ira.h_spouse_cov_count
    printed: "(helper)"
    label: "Spouse retirement plan coverage count"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.ira_cov, {const: true}]}
  - id: ira.h_line2_status
    printed: "(helper)"
    label: "Applicable line 2 amount by filing status"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.line2
  - id: ira.h_line2_not_covered
    printed: "(helper)"
    label: "Line 2 amount for a person not covered by a plan"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.line2_not_covered
  - id: ira.h_min200
    printed: "(helper)"
    label: "Minimum line 7 amount"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.min
  - id: ira.h_limit
    printed: "(helper)"
    label: "IRA limit under age 50"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.limit
  - id: ira.h_limit_50
    printed: "(helper)"
    label: "IRA limit age 50 or older"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.limit_50
  - id: ira.h_taxpayer_age50_count
    printed: "(helper)"
    label: "Taxpayer age 50 or older count"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.ira_age50, {const: true}]}
  - id: ira.h_taxpayer_age50
    printed: "(helper)"
    label: "Taxpayer is age 50 or older"
    type: Bool
    expr:
      op: test
      gt:
        - ira.h_taxpayer_age50_count
        - {const: 0, type: Count}
  - id: ira.h_spouse_age50_count
    printed: "(helper)"
    label: "Spouse age 50 or older count"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.ira_age50, {const: true}]}
  - id: ira.h_spouse_age50
    printed: "(helper)"
    label: "Spouse is age 50 or older"
    type: Bool
    expr:
      op: test
      gt:
        - ira.h_spouse_age50_count
        - {const: 0, type: Count}
  - id: ira.h_use_joint_rate_a
    printed: "(helper)"
    label: "Use joint percentage for the taxpayer column"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint_type, {const: true}]}
        - {op: test, eq: [ira.line1a, {const: true}]}
  - id: ira.h_use_joint_rate_b
    printed: "(helper)"
    label: "Use joint percentage for the spouse column"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint_type, {const: true}]}
        - {op: test, eq: [ira.line1b, {const: true}]}
  - id: ira.h_p70a
    printed: "(helper)"
    label: "Line 6a times 70%"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ira.line6a
      rate: {param: ira.rate_70}
  - id: ira.h_p80a
    printed: "(helper)"
    label: "Line 6a times 80%"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ira.line6a
      rate: {param: ira.rate_80}
  - id: ira.h_p35a
    printed: "(helper)"
    label: "Line 6a times 35%"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ira.line6a
      rate: {param: ira.rate_35}
  - id: ira.h_p40a
    printed: "(helper)"
    label: "Line 6a times 40%"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ira.line6a
      rate: {param: ira.rate_40}
  - id: ira.h_p70b
    printed: "(helper)"
    label: "Line 6b times 70%"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ira.line6b
      rate: {param: ira.rate_70}
  - id: ira.h_p80b
    printed: "(helper)"
    label: "Line 6b times 80%"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ira.line6b
      rate: {param: ira.rate_80}
  - id: ira.h_p35b
    printed: "(helper)"
    label: "Line 6b times 35%"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ira.line6b
      rate: {param: ira.rate_35}
  - id: ira.h_p40b
    printed: "(helper)"
    label: "Line 6b times 40%"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ira.line6b
      rate: {param: ira.rate_40}
  - id: ira.h_raw7a
    printed: "(helper)"
    label: "Unrounded line 7a product"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_use_joint_rate_a, {const: true}]}
              - {op: test, eq: [ira.h_taxpayer_age50, {const: false}]}
          then: ira.h_p35a
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_use_joint_rate_a, {const: true}]}
              - {op: test, eq: [ira.h_taxpayer_age50, {const: true}]}
          then: ira.h_p40a
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_use_joint_rate_a, {const: false}]}
              - {op: test, eq: [ira.h_taxpayer_age50, {const: false}]}
          then: ira.h_p70a
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_use_joint_rate_a, {const: false}]}
              - {op: test, eq: [ira.h_taxpayer_age50, {const: true}]}
          then: ira.h_p80a
  - id: ira.h_raw7b
    printed: "(helper)"
    label: "Unrounded line 7b product"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_use_joint_rate_b, {const: true}]}
              - {op: test, eq: [ira.h_spouse_age50, {const: false}]}
          then: ira.h_p35b
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_use_joint_rate_b, {const: true}]}
              - {op: test, eq: [ira.h_spouse_age50, {const: true}]}
          then: ira.h_p40b
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_use_joint_rate_b, {const: false}]}
              - {op: test, eq: [ira.h_spouse_age50, {const: false}]}
          then: ira.h_p70b
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_use_joint_rate_b, {const: false}]}
              - {op: test, eq: [ira.h_spouse_age50, {const: true}]}
          then: ira.h_p80b
  - id: ira.h_round7a
    printed: "(helper)"
    label: "Line 7a product rounded up to the next $10"
    type: NonNegDollars
    expr:
      op: round
      of: ira.h_raw7a
      unit: 1000
      rule: up
  - id: ira.h_round7b
    printed: "(helper)"
    label: "Line 7b product rounded up to the next $10"
    type: NonNegDollars
    expr:
      op: round
      of: ira.h_raw7b
      unit: 1000
      rule: up
  - id: ira.h_computed7a
    printed: "(helper)"
    label: "Computed line 7a, at least $200"
    type: NonNegDollars
    expr:
      op: larger_of
      of:
        - ira.h_round7a
        - ira.h_min200
  - id: ira.h_computed7b
    printed: "(helper)"
    label: "Computed line 7b, at least $200"
    type: NonNegDollars
    expr:
      op: larger_of
      of:
        - ira.h_round7b
        - ira.h_min200
  - id: ira.h_full_a
    printed: "(helper)"
    label: "Full IRA limit for the taxpayer column"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.h_taxpayer_age50, {const: true}]}
          then: ira.h_limit_50
        - guard: {op: test, eq: [ira.h_taxpayer_age50, {const: false}]}
          then: ira.h_limit
  - id: ira.h_full_b
    printed: "(helper)"
    label: "Full IRA limit for the spouse column"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.h_spouse_age50, {const: true}]}
          then: ira.h_limit_50
        - guard: {op: test, eq: [ira.h_spouse_age50, {const: false}]}
          then: ira.h_limit
  - id: ira.h_small_a1
    printed: "(helper)"
    label: "Smaller of line 7a and line 10"
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ira.line7a
        - ira.line10
  - id: ira.h_small_b1
    printed: "(helper)"
    label: "Smaller of line 7b and line 10"
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ira.line7b
        - ira.line10
  - id: ira.h_both_kinds_count
    printed: "(helper)"
    label: "Number of persons with both traditional and Roth IRA contributions"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, gt: [person.ira_trad, {const: 0}]}
          - {op: test, gt: [person.sav_roth, {const: 0}]}
  - id: ira.both_kinds
    printed: "(helper)"
    label: "Both traditional and Roth IRA contributions were made"
    type: Bool
    expr:
      op: test
      gt:
        - ira.h_both_kinds_count
        - {const: 0, type: Count}
  - id: ira.h_age50_count
    printed: "(helper)"
    label: "Number of persons age 50 or older"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        eq: [person.ira_age50, {const: true}]
  - id: ira.h_kbh_none
    printed: "(helper)"
    label: "Kay Bailey Hutchison short compensation threshold, no spouse age 50 or older"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.kbh_none
  - id: ira.h_kbh_one
    printed: "(helper)"
    label: "Kay Bailey Hutchison short compensation threshold, one spouse age 50 or older"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.kbh_one
  - id: ira.h_kbh_both
    printed: "(helper)"
    label: "Kay Bailey Hutchison short compensation threshold, both spouses age 50 or older"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.kbh_both
  - id: ira.h_kbh_threshold
    printed: "(helper)"
    label: "Kay Bailey Hutchison short compensation threshold"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.h_age50_count, {const: 0, type: Count}]}
          then: ira.h_kbh_none
        - guard: {op: test, eq: [ira.h_age50_count, {const: 1, type: Count}]}
          then: ira.h_kbh_one
        - guard: {op: test, ge: [ira.h_age50_count, {const: 2, type: Count}]}
          then: ira.h_kbh_both
  - id: ira.joint
    printed: "(helper)"
    label: "Filing status is married filing jointly"
    type: Bool
    expr:
      op: test
      eq: [f1040.status, {const: "mfj"}]
  - id: ira.joint_type
    printed: "(helper)"
    label: "Filing status uses joint rates (married filing jointly or qualifying surviving spouse)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [f1040.status, {const: "qss"}]}
  - id: ira.anyone_covered
    printed: "(helper)"
    label: "Either spouse is covered by a retirement plan"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [ira.line1a, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [ira.joint, {const: true}]}
            - {op: test, eq: [ira.line1b, {const: true}]}
  - id: ira.cov_gate
    printed: "(helper)"
    label: "Coverage gate for lines 2 through 6"
    type: Bool
    expr:
      op: copy
      from: ira.anyone_covered
  - id: ira.special_gate
    printed: "(helper)"
    label: "Special IRA items from the screening input"
    type: Bool
    expr:
      op: copy
      from: ira.special
  - id: ira.combat_gate
    printed: "(helper)"
    label: "Nontaxable combat pay gate (not represented in supplied inputs)"
    type: Bool
    expr:
      op: test
      eq: [{const: false}, {const: true}]
  - id: ira.excl_gate
    printed: "(helper)"
    label: "Excluded income gate (not represented in supplied inputs)"
    type: Bool
    expr:
      op: test
      eq: [{const: false}, {const: true}]
  - id: ira.over_comp
    printed: "(helper)"
    label: "Traditional IRA contributions exceed earned income"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [ira.line11a, ira.line10]}
        - {op: test, gt: [ira.line11b, ira.line10]}
  - id: ira.kbh_short
    printed: "(helper)"
    label: "Married filing jointly with earned income below the Kay Bailey Hutchison threshold"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint, {const: true}]}
        - {op: test, lt: [ira.line10, ira.h_kbh_threshold]}
  - id: ira.line20
    printed: "(helper)"
    label: "Add lines 12a and 12b; enter the total on Schedule 1, line 20."
    type: NonNegDollars
    expr:
      op: sum
      of:
        - ira.line12a
        - ira.line12b
    refuses: [ira.deduct_less, ira.kbh_short, ira.both_kinds, ira.special_gate, ira.combat_gate, ira.excl_gate]
    note: "If the filer elects to deduct a smaller amount and treat the rest as a nondeductible contribution, the smaller amount is not determined here; line 20 refuses via ira.deduct_less."
```
