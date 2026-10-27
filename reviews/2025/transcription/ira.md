# Transcription agreement — ira

Second transcription of `IRA Deduction Worksheet — Schedule 1, Line 20` by an isolated model (spec 6.5), compared line by line with `forms/2025/ira.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 53efe5dc0d1cf071417b3ec0216910fbdbe21e411edd3bdf2fce715f0e47a71e |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 21cc1ded866b0c1802ceff858c5b2fbf500a07985f24842b2b093dbcf45b2dd8 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 73d69e1a339b596759a13fbe27014c5001245845d806c3c823008847d474da26 |
| printed lines compared | 29 |
| agree / disagree / missing | 6 / 23 / 0 |
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
{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}
```

Ruling: representation; i1040gi p. 96: "You are also covered by a plan if you were self-employed and had a SEP, SIMPLE, or qualified retirement plan." Both lines count a person as covered on a work plan or a self-employed SEP or SIMPLE. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1476 of 1640 comparisons agree; 140 value, 17 candidate-unknown, 7 project-unknown. All 140 value and 7 project-unknown records supply person.plan sep or simple for a person with no Schedule C (classm.f8889.2.deepseek, classm.f5695.1, classm.ira.1; classm.f8880.3 also withholds ira_work_plan): person.plan (the self-employed person’s own SEP or SIMPLE) is read by the project only with that person’s Schedule C (person.ira_se_plan, amb.2025.ira_covered); without a Schedule C the interview never asks it and the answer is necessarily none, since other self-employment (Schedules E and F, partnerships) is refused by scope.schedule1, so the interview cannot produce these records. The 17 candidate-unknown records are returns without a Schedule C (stage16.ira.i6, stage16.ira.i7, stage16.ira.i9) where person.plan is not asked. Project stands.

### ira.cov_gate — Social security benefits, traditional IRA contributions for 2025, and you or your spouse c
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "ssb.line1"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_trad", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "ssb.line1"}], "test": "lt"}], "test": "all"}
```

Second transcription's note: Inferred from the line 6a/6b exception: with traditional IRA contributions and plan coverage, use Pub. 590-A to figure both taxable benefits and the IRA deduction.

Ruling: representation; i1040gi p. 31, Lines 6a and 6b, Exception: "You made contributions to a traditional IRA for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment. Instead, use the worksheets in Pub. 590-A". Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1617 of 1640 comparisons agree; 23 candidate-unknown. 22 of the 23 candidate-unknown records answer No to person.sav_trad and supply no amount (classm.dcprov.1, classm.retirement.4, stage10.ss.top): person.ira_trad is the amount question the interview asks only after Yes on person.sav_trad; the candidate reads it without that question, so on a return answered No the amount is not supplied, although it is necessarily zero; with that zero the candidate's conjunction is false like the project's, whatever the coverage answer. The 23rd (stage16.ira.i10) is person.plan on a return without a Schedule C (person.plan (the self-employed person’s own SEP or SIMPLE) is read by the project only with that person’s Schedule C (person.ira_se_plan, amb.2025.ira_covered); without a Schedule C the interview never asks it and the answer is necessarily none, since other self-employment (Schedules E and F, partnerships) is refused by scope.schedule1). The gate agrees on every reachable return; project stands.

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

Ruling: model error; i1040gi p. 98, Caution: "If married filing jointly and line 10 is less than $14,000 ($15,000 if one spouse is age 50 or older at the end of 2025; $16,000 if both spouses are age 50 or older at the end of 2025), stop here and use the worksheet in Pub. 590-A to figure your IRA deduction." The caution sits in the worksheet, which applies only to traditional contributions (i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction."). The candidate drops the contribution condition. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1472 of 1640 comparisons agree; 148 candidate-unknown, 10 candidate-refuses, 10 value. All 10 value records are joint returns with no traditional contributions and line 10 under the caution amount, where the candidate's gate is true and its lines 12a, 12b and 20 refuse a return the source gives a zero deduction; classm.sli.4, classm.ssb.4, classm.f1040.3 and generated 208 and 383 are refused by nothing else. The 148 candidate-unknown records are joint returns without contributions on which the candidate's line 10 needs ira.special or ira.se_capital (its line 8 and 9 screens), answers the source needs only when there are contributions. The 10 candidate-refuses records (generated 113, 121, 169) are returns refused by other cited gates (scope). Project stands.

### ira.both_kinds — A joint return on which you or your spouse made contributions to both a traditional IRA an
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.sav_roth", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_trad", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.sav_roth", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second transcription's note: Open: whether the rule means one spouse contributing to both kinds, or the couple together. The broader reading was chosen: any traditional contribution and any Roth contribution on the joint return.

Ruling: representation; i1040gi p. 95, Line 20, item 2: "If you are filing a joint return and you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, don’t use the IRA Deduction Worksheet in these instructions." Both lines take the broad reading the register records (amb.2025.ira_both_kinds). Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1617 of 1640 comparisons agree; 23 candidate-unknown. All 23 candidate-unknown records are joint returns whose persons answered No to person.sav_trad (tcw.mfj.b1, classm.f8880.2, classm.w2.1): person.ira_trad is the amount question the interview asks only after Yes on person.sav_trad; the candidate reads it without that question, so on a return answered No the amount is not supplied, although it is necessarily zero. Project stands.

### ira.over_comp — Traditional and Roth IRA contributions for 2025 more than the compensation on line 10
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"line": "10"}, {"of": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.sav_roth", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"line": "11b"}], "test": "lt"}], "test": "all"}, {"args": [{"of": [{"line": "10"}, {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}], "op": "smaller_of"}, {"line": "11a"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: Item 10 of the line 20 instructions sends filers to Pub. 590-A when the deduction plus nondeductible contributions is less than total traditional contributions. That is read as contributions above the contribution limit: the smaller of $7,000/$8,000 or compensation. For joint returns, low combined compensation is already refused by kbh_short. Roth contributions counting toward the same limit are left to the person-level excess screen.

Ruling: scope; p590a p. 35, Excess Contributions: "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of: • $7,000 ($8,000 if you are age 50 or older), or • Your taxable compensation for the year." The project refuses when traditional plus Roth contributions exceed line 10 and leaves the per-person dollar limit to person.ira_over_limit; the candidate compares each column's traditional contributions with the smaller of the limit and line 10 (the spouse's with the limit only) and leaves Roth contributions to the person.ira_excess screen. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 599 of 1640 comparisons agree; 987 candidate-unknown, 52 candidate-refuses, 2 value. The 2 value records move a refusal between cited gates on returns refused anyway: stage16.refuse.ira.kbh_short (project true, candidate false; refused by ira.kbh_short) and stage16.refuse.person.ira_over_limit (project false, candidate true; refused by person.ira_over_limit). Where the two can differ on a reachable return (Roth contributions taking the total above compensation), the project refuses with this cited screen an excess contribution the tool does not prepare (Form 5329), an acceptable scope refusal. The 52 candidate-refuses records are returns refused by other gates; of the 987 candidate-unknown records 948 answer No to person.sav_trad (person.ira_trad is the amount question the interview asks only after Yes on person.sav_trad; the candidate reads it without that question, so on a return answered No the amount is not supplied, although it is necessarily zero) 38 are no-contribution partial records on which a zero line 11 cannot exceed any cap, and ss.person.separation lacks a role. Project stands.

### ira.special_gate — Traditional IRA contributions with an IRA deduction special case (screen)
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}
```

Ruling: model error; i1040gi p. 95, Line 20: "Use the IRA Deduction Worksheet to figure the amount, if any, of your IRA deduction. But read the following list before you fill in the worksheet." The special cases matter only to a worksheet that is filled in (i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction."); the candidate's gate omits the contribution condition and its line 8 refuses on it. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 674 of 1640 comparisons agree; 966 candidate-unknown. All 966 candidate-unknown records have no traditional contributions (classm.f2441.1.deepseek, classm.f8995a.2, partial classm.s3.2 without ira.special), where the project does not ask the screen. The answer is not determined there (deferred compensation income can exist without an IRA), so the candidate requires an answer the source does not need and would refuse such a return, which has no IRA deduction. Project stands.

### ira.combat_gate — Traditional IRA contributions with nontaxable combat pay
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"ref": "s8812.combat_pay"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": true}, {"ref": "s8812.combat_pay"}], "test": "eq"}
```

Ruling: model error; i1040gi p. 98, line 8: "Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q or reported on Form 1040, line 1i." Combat pay matters to line 8 only when the worksheet is used (i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction."); the candidate's gate omits the contribution condition and its line 8 refuses on it. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1599 of 1640 comparisons agree; 21 candidate-unknown, 20 value. All 20 value records have combat pay and no traditional contributions; the candidate refuses Schedule 1 line 20, and stage8.refuse.s8812.combat_pay, stage9.eic.refuse.combat_pay and stage9.s8812.not_taking_eic.combat_pay are refused by nothing else on scope.ready, Form 1040 line 24 or Schedule 1 line 20. The 21 candidate-unknown records (ss.multi, ss.base.below, ss.mfj) are returns without contributions on which the project never asks combat pay. Project stands.

### ira.excl_gate — Traditional IRA contributions, someone covered by a retirement plan, and Form 2555 or 4563
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"ref": "sa.excluded_income"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"ref": "sa.excluded_income"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Form 2555 is detected through sa.excluded_income. Form 8815 exclusions and excluded adoption benefits are already outside scope (sb.unsupported, scope.other_income).

Ruling: model error; i1040gi p. 96: "If you were covered by a retirement plan and you file Form 2555 or 8815, or you exclude employer-provided adoption benefits, see Pub. 590-A to figure the amount, if any, of your IRA deduction." The sentence concerns figuring an IRA deduction, which needs traditional contributions (i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction."); the candidate omits that condition. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1596 of 1640 comparisons agree; 36 candidate-unknown, 8 value. The 8 value records (classm.f8889.4, classm.retirement.3, generated 39) have excluded income and coverage but no contributions, and every one of them is a return the project refuses on scope.ready, Form 1040 line 24 or Schedule 1 line 20 for another cited gate. 35 of the 36 candidate-unknown records are no-contribution returns where the candidate needs the coverage answer (ss.multi, classm.carloan.2), which the source does not need there; ss.person.separation lacks a role. Project stands.

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

Second transcription's note: Choosing to deduct a smaller amount and treat the rest as nondeductible is not computed; that choice is refused.

Ruling: model error; i1040gi p. 98, line 12: "This is the most you can deduct. Add the amounts on lines 12a and 12b and enter the total on Schedule 1, line 20. Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606)." Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 520 of 1640 comparisons agree; 1016 candidate-unknown, 102 candidate-refuses, 2 project-refuses. The candidate refuses through its gates. Of the 102 candidate-refuses records, 5 are reachable joint returns with no traditional contributions refused by its ira.kbh_short (classm.sli.4, classm.ssb.4, classm.f1040.3, generated 208 and 383; ruled model error there), where the source gives zero; the other 97 are refused by other cited gates (scope). Of the 1,016 candidate-unknown records, 966 need ira.deduct_less on returns with no deduction, where the election to deduct less is necessarily No (representation); 10 need person.plan without a Schedule C and 2 the amount after No to person.sav_trad (both necessarily determined); 38 are no-contribution partial records needing ira.special or ira.se_capital (model error, as ruled on ira.special_gate and line 9). The 2 project-refuses records are cited scope screens: stage16.refuse.person.ira_excess (person.ira_excess_gate) and stage16.refuse.ira.dist (person.ira_dist_gate). No value differs. Project stands.

### 1a — Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": true}, {"ref": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"ref": "person.plan"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second transcription's note: Open: for married filing separately, a person who was not covered but whose spouse was is considered covered unless they lived apart all year. The closed interface has no input for a separate-return spouse's coverage, so this line reflects only the taxpayer's own coverage (work plan, SEP or SIMPLE). Married filing separately while living apart is refused at line 2a.

Ruling: representation; i1040gi p. 97, line 1: "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?" and "If married filing jointly, was your spouse covered by a retirement plan?"; i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction." The project shows line 1a Yes only when traditional contributions make the worksheet apply, and the deduction reads person.ira_cov, not this line. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 530 of 1640 comparisons agree; 938 candidate-unknown, 172 value. All 172 value records have no traditional contributions (project No, candidate Yes; classm.f5695.1, classm.ira.1, classm.f8880.1), many also with person.plan supplied without a Schedule C. Of the 938 candidate-unknown records, 920 are no-contribution returns where coverage is not asked, 17 are contributing returns needing person.plan without a Schedule C (person.plan (the self-employed person’s own SEP or SIMPLE) is read by the project only with that person’s Schedule C (person.ira_se_plan, amb.2025.ira_covered); without a Schedule C the interview never asks it and the answer is necessarily none, since other self-employment (Schedules E and F, partnerships) is refused by scope.schedule1), and ss.person.separation lacks a role. On contributing returns the answers agree; on a return with no traditional IRA contributions the worksheet is not used and no amount reads the line. Project stands.

### 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": true}, {"ref": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"ref": "person.plan"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}
```

Ruling: representation; i1040gi p. 97, line 1: "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?" and "If married filing jointly, was your spouse covered by a retirement plan?"; i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction." Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1466 of 1640 comparisons agree; 136 candidate-unknown, 38 value. All 38 value records are joint returns with no traditional contributions (classm.ira.2, classm.f5695.5, classm.f8960.2), several with person.plan supplied without a Schedule C. Of the 136 candidate-unknown records, 128 are no-contribution returns where spouse coverage is not asked and 8 need person.plan without a Schedule C (person.plan (the self-employed person’s own SEP or SIMPLE) is read by the project only with that person’s Schedule C (person.ira_se_plan, amb.2025.ira_covered); without a Schedule C the interview never asks it and the answer is necessarily none, since other self-employment (Schedules E and F, partnerships) is refused by scope.schedule1). On contributing returns the answers agree; on a return with no traditional IRA contributions the worksheet is not used and no amount reads the line. Project stands.

### 2a — Enter the amount shown below that applies to you (your IRA)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"line": "1a"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"line": "1a"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second transcription's note: Open: married filing separately while living apart all year uses $89,000. The only supplied line 2 parameter is keyed by filing status and gives $10,000 for mfs. No unkeyed $89,000 parameter exists, so this case is refused instead of computed.

Ruling: model error; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." Under the skipped-line rule (README), a nonzero amount on a line the source says to skip, on a reachable return, is a defect of the side producing it even when no later amount changes; the project shows zero. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 18 of 1640 comparisons agree; 1419 value, 184 candidate-unknown, 14 project-unknown, 5 candidate-refuses. 176 value records are reachable returns (refused nowhere else) on which no one is covered, so line 2a is skipped, and the candidate enters an amount: stage16.ira.i6 (single, contributions) $0 against $89,000; classm.f5695.2 (joint) $0 against $246,000. No deduction changes, since its line 7 takes the applicable amount when no one is covered. The other value records are returns without contributions or refused elsewhere. Of the 184 candidate-unknown records, 132 are no-contribution joint returns where coverage is not asked, 46 are separate returns needing ssb.lived_apart and 6 need person.plan without a Schedule C (representation); the 14 project-unknown records omit person.sav_trad, which the interview asks; the 5 candidate-refuses records are separate returns, which s3.mfs refuses (scope). Project stands.

### 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"line": "1b"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"line": "1b"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second transcription's note: The spouse column is used only on a joint return. Line 7b is zero otherwise.

Ruling: model error; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." Under the skipped-line rule (README), a nonzero amount on a line the source says to skip, on a reachable return, is a defect of the side producing it even when no later amount changes; the project shows zero. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 7 of 1640 comparisons agree; 1483 value, 136 candidate-unknown, 14 project-unknown. 176 value records are reachable returns (refused nowhere else) on which no one is covered, so line 2b is skipped, and the candidate enters an amount: classm.f5695.2 (joint) $0 against $246,000; classm.f5695.1 (head of household, no spouse’s column) $0 against $89,000. No deduction changes, since its line 7 takes the applicable amount when no one is covered. Off a joint return there is no spouse's column (i1040gi p. 95, Line 20, item 6: "You must file a joint return to deduct contributions to your spouse’s IRA."). The 136 candidate-unknown records are no-contribution joint returns where coverage is not asked or need person.plan without a Schedule C (representation); the 14 project-unknown records omit person.sav_trad. Project stands.

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

Second transcription's note: A zero here means line 5 is not less than line 2 (STOP). Line 7a is then zero.

Ruling: model error; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." Under the skipped-line rule (README), a nonzero amount on a line the source says to skip, on a reachable return, is a defect of the side producing it even when no later amount changes; the project shows zero. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 469 of 1640 comparisons agree; 610 value, 373 candidate-refuses, 188 candidate-unknown. 94 value records are reachable returns (refused nowhere else) on which no one is covered, so line 6a is skipped, and the candidate enters an amount: stage16.ira.i6 $0 against $84,000; classm.f5695.1 $0 against $56,064. No deduction changes, since its line 7 takes the applicable amount when no one is covered. The 373 candidate-refuses records come from figuring line 5 on every return, and every one of them is a return the project refuses on scope.ready, Form 1040 line 24 or Schedule 1 line 20 for another cited gate (scope); the 188 candidate-unknown records are no-contribution returns needing coverage or line 5 inputs, or person.plan without a Schedule C (representation). Project stands.

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

Ruling: model error; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." Under the skipped-line rule (README), a nonzero amount on a line the source says to skip, on a reachable return, is a defect of the side producing it even when no later amount changes; the project shows zero. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 493 of 1640 comparisons agree; 626 value, 373 candidate-refuses, 148 candidate-unknown. 92 value records are reachable returns (refused nowhere else) on which no one is covered, so line 6b is skipped, and the candidate enters an amount: classm.f5695.3 (joint) $0 against $72,349; classm.f5695.1 (no spouse’s column) $0 against $56,064. No deduction changes, since its line 7 takes the applicable amount when no one is covered. The 373 candidate-refuses records come from figuring line 5 on every return, and every one of them is a return the project refuses on scope.ready, Form 1040 line 24 or Schedule 1 line 20 for another cited gate (scope); the 148 candidate-unknown records are no-contribution returns needing coverage or line 5 inputs, or person.plan without a Schedule C (representation). Project stands.

### 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.ira_line7", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"line": "6a"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 0}, {"line": "6a"}], "test": "lt"}, {"args": [{"line": "6a"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"line": "1a"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"line": "1a"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"line": "6a"}], "test": "le"}, {"args": [{"const": 0}, {"line": "6a"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}
```

Ruling: representation; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8."; i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction." Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 93 of 1640 comparisons agree; 943 candidate-unknown, 517 value, 87 candidate-refuses. All 517 value records have no traditional contributions: the project shows zero and the candidate the applicable $7,000 or $8,000; line 12a is the smallest of line 7a, 10 and 11a, and 11a is zero, so no deduction differs. 926 of the 943 candidate-unknown records are no-contribution returns needing coverage or age; 17 contributing returns need person.plan without a Schedule C (person.plan (the self-employed person’s own SEP or SIMPLE) is read by the project only with that person’s Schedule C (person.ira_se_plan, amb.2025.ira_covered); without a Schedule C the interview never asks it and the answer is necessarily none, since other self-employment (Schedules E and F, partnerships) is refused by scope.schedule1). The 87 candidate-refuses records are returns the project refuses for other cited gates (scope). On contributing returns the two lines agree on every record, including the 35%/70% rates, the $10,000/$20,000 thresholds and the $200 floor. Project stands.

### 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.ira_line7", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "6b"}], "test": "lt"}, {"args": [{"line": "6b"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"line": "6b"}], "test": "le"}, {"args": [{"const": 0}, {"line": "6b"}], "test": "lt"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"line": "6b"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Only a joint return has a spouse's column (you must file jointly to deduct contributions to your spouse's IRA). Otherwise this line is zero.

Ruling: representation; i1040gi p. 97: "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8."; i1040gi p. 95, Line 20, item 6: "You must file a joint return to deduct contributions to your spouse’s IRA." Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1397 of 1640 comparisons agree; 136 candidate-unknown, 69 value, 24 candidate-refuses, 14 project-unknown. All 69 value records are no-contribution returns (project zero, candidate the applicable amount); line 11b is zero there. The 136 candidate-unknown records are no-contribution joint returns needing coverage or age, plus contributing returns needing person.plan without a Schedule C; the 14 project-unknown records omit person.sav_trad, which the interview asks; the 24 candidate-refuses records are returns refused for other cited gates (scope). On contributing returns the lines agree. Project stands.

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

Second transcription's note: Wages are taken as Form 1040 line 1a (the total of Form W-2 box 1). The closed interface has no combat-pay amount, so returns with nontaxable combat pay are refused.

Ruling: model error; i1040gi p. 98, line 8: "Wages, salaries, tips, etc. Generally, this is the amount reported in box 1 of Form W-2." The candidate's wages (Form 1040 line 1a) equal the project's Form W-2 box 1 total on every record where both compute; no value differs. The difference is the refusals attached to the candidate's line 8, ira.special_gate and ira.combat_gate without the contribution condition (i1040gi p. 95, Line 20: "Use the IRA Deduction Worksheet to figure the amount, if any, of your IRA deduction. But read the following list before you fill in the worksheet."). Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 677 of 1640 comparisons agree; 949 candidate-unknown, 12 candidate-refuses, 2 project-refuses. All 949 candidate-unknown records need ira.special on returns with no traditional contributions (classm.f2441.1.deepseek, classm.f8995a.2), an answer the source needs only for a worksheet that is used. The 12 candidate-refuses records are returns the project refuses for other gates (stage16.refuse.ira.special, stage16.refuse.ira.combat_pay); the 2 project-refuses records are the cited Schedule 1 line 2a alimony screens (stage16.refuse.s1.alimony_received, stage16.refuse.s1.alimony_paid), scope. Project's wages stand.

### 9 — Enter the earned income you (and your spouse if filing jointly) received as a self-employe
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_se", "op": "sum_over", "where": null}
```

Second:

```json
{"from": {"from": {"ref": "s1.line3"}, "op": "subtract", "take": {"ref": "s1.line15"}}, "op": "subtract_floor0", "take": {"ref": "s1.line16"}}
```

Second transcription's note: Open: Pub. 590-A says a self-employment loss is not subtracted from wages. Spouses' Schedule C results are combined here, as the worksheet line asks, and the floor of zero is applied to that total. Schedule 1 line 3 is used as the net earnings from the trade or business; partnerships and other self-employment income are out of scope.

Ruling: ambiguity; p590a p. 7: "Self-employment loss. If you have a net loss from self-employment, don’t subtract the loss from your salaries or wages when figuring your total compensation." The project floors each spouse's self-employment earned income at zero before adding (amb.2025.ira_se_floor, owner decision); the candidate floors the combined total, the other recorded reading. Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 671 of 1640 comparisons agree; 921 candidate-unknown, 46 project-refuses, 2 value. The 2 value records are joint returns where one spouse has a Schedule C loss (generated 293: $157,316.78 against $109,209.37; generated 491), both refused for other gates. Of the 921 candidate-unknown records, 792 are returns without a Schedule C where the candidate's unconditional ira.se_capital screen asks a question whose answer is necessarily No (representation), and 129 have a Schedule C but no traditional contributions, where the source needs no such answer (model error in the candidate's screen). The 46 project-refuses records are Schedule C returns refused by cited Schedule C and plan screens (person.sc[].screened, s179.multi, person.plan_screened), scope. Project stands.

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

Ruling: representation; i1040gi p. 98, line 11: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025 to your IRA on line 11a and to your spouse’s IRA on line 11b." Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 693 of 1640 comparisons agree; 947 candidate-unknown. All 947 candidate-unknown records answer No to person.sav_trad and supply no amount (classm.f2441.1.deepseek, classm.asset.2): person.ira_trad is the amount question the interview asks only after Yes on person.sav_trad; the candidate reads it without that question, so on a return answered No the amount is not supplied, although it is necessarily zero. Values agree wherever the amount is known. Project stands.

### 11b — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"collection": "person", "field": "person.ira_trad", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: You must file a joint return to deduct contributions to your spouse's IRA, so this line is zero otherwise.

Ruling: representation; i1040gi p. 98, line 11: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025 to your IRA on line 11a and to your spouse’s IRA on line 11b."; i1040gi p. 95, Line 20, item 6: "You must file a joint return to deduct contributions to your spouse’s IRA." Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 1505 of 1640 comparisons agree; 134 candidate-unknown, 1 project-unknown. All 134 candidate-unknown records are joint returns whose spouse answered No to person.sav_trad (classm.f2441.2, stage16.mut.ira_joint_full_edge): person.ira_trad is the amount question the interview asks only after Yes on person.sav_trad; the candidate reads it without that question, so on a return answered No the amount is not supplied, although it is necessarily zero. The 1 project-unknown record (ss.person.separation) has a person keyed 'second' without a role, which the interview's taxpayer/spouse roster never produces. Project stands.

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

Ruling: model error; i1040gi p. 98, line 12: "On line 12a, enter the smallest of line 7a, 10, or 11a. On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct." Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 538 of 1640 comparisons agree; 996 candidate-unknown, 104 candidate-refuses, 2 project-refuses. No value differs. Of the 104 candidate-refuses records, 6 are reachable joint returns with no traditional contributions refused by the candidate's ira.kbh_short (classm.sli.4, classm.ssb.4, classm.f1040.3, generated 208, 383), where the source gives zero (as ruled on ira.kbh_short); the rest are refused by other cited gates (scope). The 996 candidate-unknown records need the amount after No to person.sav_trad, person.plan without a Schedule C (both necessarily determined, representation) or ira.special and ira.se_capital on no-contribution returns (model error as ruled on ira.special_gate). The 2 project-refuses records are cited scope screens (stage16.refuse.person.ira_excess, stage16.refuse.ira.dist). Project stands.

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

Ruling: model error; i1040gi p. 98, line 12: "On line 12a, enter the smallest of line 7a, 10, or 11a. On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct."; i1040gi p. 95, Line 20, item 6: "You must file a joint return to deduct contributions to your spouse’s IRA." Triage executable-triage-v1 (triage/ira.json; 1,083 fixtures, 500 generated returns seed 20261026, 57 partial records): 556 of 1640 comparisons agree; 1006 candidate-unknown, 78 candidate-refuses. No value differs. Of the 78 candidate-refuses records, 6 are reachable joint returns without traditional contributions refused by the candidate's ira.kbh_short (classm.sli.4, classm.ssb.4, generated 208), where the source gives zero; the rest are refused by other cited gates (scope). The 1,006 candidate-unknown records need the amount after No to person.sav_trad (stage16.hsa.partial.H01, classm.f8889.3), person.plan without a Schedule C (representation) or ira.special and ira.se_capital on no-contribution returns (model error as ruled on ira.special_gate). Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ira.kbh_short | ira.combat_gate, ira.se_capital, ira.special_gate | ira.combat_gate, ira.se_capital, ira.special_gate |
| ira.over_comp | ira.combat_gate, ira.se_capital, ira.special_gate | ira.combat_gate, ira.se_capital, ira.special_gate |
| ira.line20 | ira.both_kinds, ira.combat_gate, ira.cov_gate, ira.deduct_less, ira.excl_gate, ira.h_mfs_apart, ira.kbh_short, ira.over_comp, ira.se_capital, ira.special_gate, scope.schedule1 | ira.deduct_less, ira.h_mfs_apart, ira.se_capital |
| 2a | ira.h_mfs_apart | ira.h_mfs_apart |
| 4 | scope.schedule1 | scope.schedule1 |
| 5 | scope.schedule1 | - |
| 6a | ira.h_mfs_apart, scope.schedule1 | ira.h_mfs_apart |
| 6b | scope.schedule1 | - |
| 7a | ira.h_mfs_apart, scope.schedule1 | ira.h_mfs_apart |
| 7b | scope.schedule1 | - |
| 8 | ira.combat_gate, ira.special_gate | ira.combat_gate, ira.special_gate |
| 9 | ira.se_capital | ira.se_capital |
| 10 | ira.combat_gate, ira.se_capital, ira.special_gate | ira.combat_gate, ira.se_capital, ira.special_gate |
| 12a | ira.both_kinds, ira.combat_gate, ira.cov_gate, ira.excl_gate, ira.h_mfs_apart, ira.kbh_short, ira.over_comp, ira.se_capital, ira.special_gate, scope.schedule1 | ira.h_mfs_apart, ira.se_capital |
| 12b | ira.both_kinds, ira.combat_gate, ira.cov_gate, ira.excl_gate, ira.kbh_short, ira.over_comp, ira.se_capital, ira.special_gate, scope.schedule1 | ira.se_capital |

## Raw second transcription

```yaml
```yaml
lines:
  - id: ira.joint
    printed: "(helper)"
    label: "Married filing jointly"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfj"}]}

  - id: ira.joint_type
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse (lines 6 and 7)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [f1040.status, {const: "qss"}]}

  - id: ira.h_tp_cov_n
    printed: "(helper)"
    label: "Number of taxpayer entries covered by a retirement plan at work or through self-employment (SEP or SIMPLE)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - op: test
            any:
              - {op: test, eq: [person.ira_work_plan, {const: true}]}
              - {op: test, ne: [person.plan, {const: "none"}]}

  - id: ira.h_sp_cov_n
    printed: "(helper)"
    label: "Number of spouse entries covered by a retirement plan at work or through self-employment (SEP or SIMPLE)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - op: test
            any:
              - {op: test, eq: [person.ira_work_plan, {const: true}]}
              - {op: test, ne: [person.plan, {const: "none"}]}

  - id: ira.line1a
    printed: "1a"
    label: "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?"
    type: Bool
    expr: {op: test, gt: [ira.h_tp_cov_n, {const: 0, type: Count}]}
    note: >-
      Open: for married filing separately, a person who was not covered but whose spouse was is considered
      covered unless they lived apart all year. The closed interface has no input for a separate-return
      spouse's coverage, so this line reflects only the taxpayer's own coverage (work plan, SEP or SIMPLE).
      Married filing separately while living apart is refused at line 2a.

  - id: ira.line1b
    printed: "1b"
    label: "If married filing jointly, was your spouse covered by a retirement plan?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint, {const: true}]}
        - {op: test, gt: [ira.h_sp_cov_n, {const: 0, type: Count}]}

  - id: ira.anyone_covered
    printed: "(helper)"
    label: "Yes on line 1a, or Yes on line 1b if married filing jointly (otherwise skip lines 2 through 6)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [ira.line1a, {const: true}]}
        - {op: test, eq: [ira.line1b, {const: true}]}

  - id: ira.h_mfs_apart
    printed: "(helper)"
    label: "Married filing separately and you lived apart from your spouse for all of 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "mfs"}]}
        - {op: test, eq: [ssb.lived_apart, {const: true}]}

  - id: ira.h_line2_status
    printed: "(helper)"
    label: "Line 2 amount by filing status ($89,000 single or head of household; $146,000 married filing jointly or qualifying surviving spouse; $10,000 married filing separately and lived with spouse)"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2}

  - id: ira.h_line2_nc
    printed: "(helper)"
    label: "Line 2 amount for the person who wasn't covered by a plan on a joint return ($246,000)"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2_not_covered}

  - id: ira.line2a
    printed: "2a"
    label: "Enter the amount shown below that applies to you (Your IRA)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.joint, {const: true}]}
              - {op: test, eq: [ira.line1a, {const: false}]}
          then: ira.h_line2_nc
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [ira.joint, {const: true}]}
                - {op: test, eq: [ira.line1a, {const: false}]}
          then: ira.h_line2_status
    refuses: [ira.h_mfs_apart]
    note: >-
      Open: married filing separately while living apart all year uses $89,000. The only supplied line 2
      parameter is keyed by filing status and gives $10,000 for mfs. No unkeyed $89,000 parameter exists,
      so this case is refused instead of computed.

  - id: ira.line2b
    printed: "2b"
    label: "Enter the amount shown below that applies to you (Spouse's IRA)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.joint, {const: true}]}
              - {op: test, eq: [ira.line1b, {const: false}]}
          then: ira.h_line2_nc
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [ira.joint, {const: true}]}
                - {op: test, eq: [ira.line1b, {const: false}]}
          then: ira.h_line2_status
    note: "The spouse column is used only on a joint return. Line 7b is zero otherwise."

  - id: ira.line3
    printed: "3"
    label: "Enter the amount from Form 1040 or 1040-SR, line 9"
    type: Dollars
    expr: {op: copy, from: f1040.line9}

  - id: ira.line4
    printed: "4"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"
    type: NonNegDollars
    expr:
      op: sum
      of: [s1.line11, s1.line13, s1.line15, s1.line16, s1.line17, s1.line18, s1.line19a, s1.line25]
    refuses: [scope.schedule1]
    note: >-
      Schedule 1 lines 12, 14 and 23 are not in the catalog. Adjustments on those lines are outside scope
      and refused by scope.schedule1, so they are taken as absent.

  - id: ira.line5
    printed: "5"
    label: "Subtract line 4 from line 3. If married filing jointly, enter the result in both columns"
    type: Dollars
    expr: {op: subtract, from: ira.line3, take: ira.line4}

  - id: ira.line6a
    printed: "6a"
    label: "Is the amount on line 5 less than the amount on line 2? No: STOP, none of your IRA contributions are deductible. Yes: subtract line 5 from line 2 (Your IRA)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ira.line2a, take: ira.line5}
    note: "A zero here means line 5 is not less than line 2 (STOP). Line 7a is then zero."

  - id: ira.line6b
    printed: "6b"
    label: "Is the amount on line 5 less than the amount on line 2? No: STOP. Yes: subtract line 5 from line 2 (Spouse's IRA)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ira.line2b, take: ira.line5}

  - id: ira.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: ira.h_lim
    printed: "(helper)"
    label: "$7,000 if under age 50 at the end of 2025"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit}

  - id: ira.h_lim50
    printed: "(helper)"
    label: "$8,000 if age 50 or older at the end of 2025"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit_50}

  - id: ira.h_tp50_n
    printed: "(helper)"
    label: "Number of taxpayer entries age 50 or older at the end of 2025"
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

  - id: ira.h_sp50_n
    printed: "(helper)"
    label: "Number of spouse entries age 50 or older at the end of 2025"
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

  - id: ira.h_tp50
    printed: "(helper)"
    label: "You were age 50 or older at the end of 2025"
    type: Bool
    expr: {op: test, gt: [ira.h_tp50_n, {const: 0, type: Count}]}

  - id: ira.h_sp50
    printed: "(helper)"
    label: "Your spouse was age 50 or older at the end of 2025"
    type: Bool
    expr: {op: test, gt: [ira.h_sp50_n, {const: 0, type: Count}]}

  - id: ira.h_limit_a
    printed: "(helper)"
    label: "Applicable amount for your IRA ($7,000, or $8,000 if age 50 or older)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.h_tp50, {const: true}]}
          then: ira.h_lim50
        - guard: {op: test, eq: [ira.h_tp50, {const: false}]}
          then: ira.h_lim

  - id: ira.h_limit_b
    printed: "(helper)"
    label: "Applicable amount for your spouse's IRA ($7,000, or $8,000 if age 50 or older)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.h_sp50, {const: true}]}
          then: ira.h_lim50
        - guard: {op: test, eq: [ira.h_sp50, {const: false}]}
          then: ira.h_lim

  - id: ira.h_wide_a
    printed: "(helper)"
    label: "Your column uses the joint/qualifying surviving spouse rules for a covered person ($20,000 threshold, 35%/40%)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint_type, {const: true}]}
        - {op: test, eq: [ira.line1a, {const: true}]}

  - id: ira.h_wide_b
    printed: "(helper)"
    label: "Spouse's column uses the joint rules for a covered person ($20,000 threshold, 35%/40%)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint, {const: true}]}
        - {op: test, eq: [ira.line1b, {const: true}]}

  - id: ira.h_full_narrow
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.full_narrow}

  - id: ira.h_full_joint
    printed: "(helper)"
    label: "$20,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.full_joint}

  - id: ira.h_full_a
    printed: "(helper)"
    label: "Line 6 threshold for full deduction, your column"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.h_wide_a, {const: true}]}
          then: ira.h_full_joint
        - guard: {op: test, eq: [ira.h_wide_a, {const: false}]}
          then: ira.h_full_narrow

  - id: ira.h_full_b
    printed: "(helper)"
    label: "Line 6 threshold for full deduction, spouse's column"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.h_wide_b, {const: true}]}
          then: ira.h_full_joint
        - guard: {op: test, eq: [ira.h_wide_b, {const: false}]}
          then: ira.h_full_narrow

  - id: ira.h_at_full_a
    printed: "(helper)"
    label: "Line 6a result is at or above the threshold"
    type: Bool
    expr: {op: test, ge: [ira.line6a, ira.h_full_a]}

  - id: ira.h_at_full_b
    printed: "(helper)"
    label: "Line 6b result is at or above the threshold"
    type: Bool
    expr: {op: test, ge: [ira.line6b, ira.h_full_b]}

  - id: ira.h_p70_a
    printed: "(helper)"
    label: "Line 6a times 70%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: {param: ira.rate_70}}

  - id: ira.h_p80_a
    printed: "(helper)"
    label: "Line 6a times 80%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: {param: ira.rate_80}}

  - id: ira.h_p35_a
    printed: "(helper)"
    label: "Line 6a times 35%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: {param: ira.rate_35}}

  - id: ira.h_p40_a
    printed: "(helper)"
    label: "Line 6a times 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: {param: ira.rate_40}}

  - id: ira.h_prod_a
    printed: "(helper)"
    label: "Multiply line 6a by the percentage that applies to you"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_wide_a, {const: true}]}
              - {op: test, eq: [ira.h_tp50, {const: true}]}
          then: ira.h_p40_a
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_wide_a, {const: true}]}
              - {op: test, eq: [ira.h_tp50, {const: false}]}
          then: ira.h_p35_a
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_wide_a, {const: false}]}
              - {op: test, eq: [ira.h_tp50, {const: true}]}
          then: ira.h_p80_a
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_wide_a, {const: false}]}
              - {op: test, eq: [ira.h_tp50, {const: false}]}
          then: ira.h_p70_a

  - id: ira.h_round_a
    printed: "(helper)"
    label: "If the result isn't a multiple of $10, increase it to the next multiple of $10"
    type: NonNegDollars
    expr: {op: round, of: ira.h_prod_a, unit: 1000, rule: up}

  - id: ira.h_min
    printed: "(helper)"
    label: "$200"
    type: NonNegDollars
    expr: {op: param, ref: ira.min}

  - id: ira.h_figured_a
    printed: "(helper)"
    label: "If the result is $200 or more, enter the result; if less than $200, enter $200 (your column)"
    type: NonNegDollars
    expr: {op: larger_of, of: [ira.h_round_a, ira.h_min]}

  - id: ira.line7a
    printed: "7a"
    label: "Line 7, Your IRA (applicable amount if not covered or at/above the threshold; otherwise line 6a times the percentage, rounded up to $10, at least $200)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.anyone_covered, {const: false}]}
          then: ira.h_limit_a
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.anyone_covered, {const: true}]}
              - {op: test, eq: [ira.line6a, {const: 0}]}
          then: ira.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.anyone_covered, {const: true}]}
              - {op: test, gt: [ira.line6a, {const: 0}]}
              - {op: test, eq: [ira.h_at_full_a, {const: true}]}
          then: ira.h_limit_a
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.anyone_covered, {const: true}]}
              - {op: test, gt: [ira.line6a, {const: 0}]}
              - {op: test, eq: [ira.h_at_full_a, {const: false}]}
          then: ira.h_figured_a

  - id: ira.h_p70_b
    printed: "(helper)"
    label: "Line 6b times 70%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: {param: ira.rate_70}}

  - id: ira.h_p80_b
    printed: "(helper)"
    label: "Line 6b times 80%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: {param: ira.rate_80}}

  - id: ira.h_p35_b
    printed: "(helper)"
    label: "Line 6b times 35%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: {param: ira.rate_35}}

  - id: ira.h_p40_b
    printed: "(helper)"
    label: "Line 6b times 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: {param: ira.rate_40}}

  - id: ira.h_prod_b
    printed: "(helper)"
    label: "Multiply line 6b by the percentage that applies"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_wide_b, {const: true}]}
              - {op: test, eq: [ira.h_sp50, {const: true}]}
          then: ira.h_p40_b
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_wide_b, {const: true}]}
              - {op: test, eq: [ira.h_sp50, {const: false}]}
          then: ira.h_p35_b
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_wide_b, {const: false}]}
              - {op: test, eq: [ira.h_sp50, {const: true}]}
          then: ira.h_p80_b
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.h_wide_b, {const: false}]}
              - {op: test, eq: [ira.h_sp50, {const: false}]}
          then: ira.h_p70_b

  - id: ira.h_round_b
    printed: "(helper)"
    label: "If the result isn't a multiple of $10, increase it to the next multiple of $10 (spouse's column)"
    type: NonNegDollars
    expr: {op: round, of: ira.h_prod_b, unit: 1000, rule: up}

  - id: ira.h_figured_b
    printed: "(helper)"
    label: "If the result is $200 or more, enter the result; if less than $200, enter $200 (spouse's column)"
    type: NonNegDollars
    expr: {op: larger_of, of: [ira.h_round_b, ira.h_min]}

  - id: ira.line7b
    printed: "7b"
    label: "Line 7, Spouse's IRA (if applicable)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.joint, {const: false}]}
          then: ira.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.joint, {const: true}]}
              - {op: test, eq: [ira.anyone_covered, {const: false}]}
          then: ira.h_limit_b
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.joint, {const: true}]}
              - {op: test, eq: [ira.anyone_covered, {const: true}]}
              - {op: test, eq: [ira.line6b, {const: 0}]}
          then: ira.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.joint, {const: true}]}
              - {op: test, eq: [ira.anyone_covered, {const: true}]}
              - {op: test, gt: [ira.line6b, {const: 0}]}
              - {op: test, eq: [ira.h_at_full_b, {const: true}]}
          then: ira.h_limit_b
        - guard:
            op: test
            all:
              - {op: test, eq: [ira.joint, {const: true}]}
              - {op: test, eq: [ira.anyone_covered, {const: true}]}
              - {op: test, gt: [ira.line6b, {const: 0}]}
              - {op: test, eq: [ira.h_at_full_b, {const: false}]}
          then: ira.h_figured_b
    note: "Only a joint return has a spouse's column (you must file jointly to deduct contributions to your spouse's IRA). Otherwise this line is zero."

  - id: ira.special_gate
    printed: "(gate)"
    label: "Nonqualified deferred compensation or nongovernmental 457 income, non-W-2 fellowship/stipend compensation, qualified reservist repayment, or difficulty of care payments (figure under Pub. 590-A)"
    type: Bool
    expr: {op: test, eq: [ira.special, {const: true}]}

  - id: ira.combat_gate
    printed: "(gate)"
    label: "Nontaxable combat pay is included in line 8 earned income; no amount is supplied"
    type: Bool
    expr: {op: test, eq: [s8812.combat_pay, {const: true}]}

  - id: ira.line8
    printed: "8"
    label: "Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.; alimony and separate maintenance payments reported on Schedule 1, line 2a; nontaxable combat pay"
    type: NonNegDollars
    expr: {op: sum, of: [f1040.line1a, s1.line2a]}
    refuses: [ira.special_gate, ira.combat_gate]
    note: >-
      Wages are taken as Form 1040 line 1a (the total of Form W-2 box 1). The closed interface has no
      combat-pay amount, so returns with nontaxable combat pay are refused.

  - id: ira.h_se
    printed: "(helper)"
    label: "Net earnings from self-employment (Schedule C) minus the Schedule 1, line 15 deduction"
    type: Dollars
    expr: {op: subtract, from: s1.line3, take: s1.line15}

  - id: ira.line9
    printed: "9"
    label: "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner, minus any deductions on Schedule 1, lines 15 and 16. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ira.h_se, take: s1.line16}
    refuses: [ira.se_capital]
    note: >-
      Open: Pub. 590-A says a self-employment loss is not subtracted from wages. Spouses' Schedule C results
      are combined here, as the worksheet line asks, and the floor of zero is applied to that total.
      Schedule 1 line 3 is used as the net earnings from the trade or business; partnerships and other
      self-employment income are out of scope.

  - id: ira.line10
    printed: "10"
    label: "Add lines 8 and 9"
    type: NonNegDollars
    expr: {op: sum, of: [ira.line8, ira.line9]}

  - id: ira.h_all50_n
    printed: "(helper)"
    label: "Number of spouses age 50 or older at the end of 2025"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.ira_age50, {const: true}]}

  - id: ira.h_kbh_none
    printed: "(helper)"
    label: "$14,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_none}

  - id: ira.h_kbh_one
    printed: "(helper)"
    label: "$15,000 if one spouse is age 50 or older"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_one}

  - id: ira.h_kbh_both
    printed: "(helper)"
    label: "$16,000 if both spouses are age 50 or older"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_both}

  - id: ira.h_kbh
    printed: "(helper)"
    label: "Joint-return compensation threshold for the caution under line 10"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.h_all50_n, {const: 0, type: Count}]}
          then: ira.h_kbh_none
        - guard: {op: test, eq: [ira.h_all50_n, {const: 1, type: Count}]}
          then: ira.h_kbh_one
        - guard: {op: test, ge: [ira.h_all50_n, {const: 2, type: Count}]}
          then: ira.h_kbh_both

  - id: ira.kbh_short
    printed: "(gate)"
    label: "If married filing jointly and line 10 is less than $14,000 ($15,000 if one spouse is age 50 or older; $16,000 if both), stop here and use the worksheet in Pub. 590-A"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint, {const: true}]}
        - {op: test, lt: [ira.line10, ira.h_kbh]}

  - id: ira.line11a
    printed: "11a"
    label: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your IRA"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_trad
      where: {op: test, eq: [person.role, {const: "taxpayer"}]}

  - id: ira.h_spouse_trad
    printed: "(helper)"
    label: "Traditional IRA contributions for 2025 to your spouse's IRA"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_trad
      where: {op: test, eq: [person.role, {const: "spouse"}]}

  - id: ira.line11b
    printed: "11b"
    label: "Enter traditional IRA contributions made for 2025 to your spouse's IRA"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.joint, {const: true}]}
          then: ira.h_spouse_trad
        - guard: {op: test, eq: [ira.joint, {const: false}]}
          then: ira.h_zero
    note: "You must file a joint return to deduct contributions to your spouse's IRA, so this line is zero otherwise."

  - id: ira.h_trad_total
    printed: "(helper)"
    label: "Total traditional IRA contributions for 2025 (you and your spouse)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.ira_trad}

  - id: ira.h_roth_total
    printed: "(helper)"
    label: "Total Roth IRA contributions for 2025 (you and your spouse)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.sav_roth}

  - id: ira.both_kinds
    printed: "(gate)"
    label: "Filing a joint return and you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025 (use Pub. 590-A)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint, {const: true}]}
        - {op: test, gt: [ira.h_trad_total, {const: 0}]}
        - {op: test, gt: [ira.h_roth_total, {const: 0}]}
    note: >-
      Open: whether the rule means one spouse contributing to both kinds, or the couple together. The broader
      reading was chosen: any traditional contribution and any Roth contribution on the joint return.

  - id: ira.h_cap_a
    printed: "(helper)"
    label: "Smaller of your applicable limit or line 10 compensation"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.h_limit_a, ira.line10]}

  - id: ira.over_comp
    printed: "(gate)"
    label: "Traditional IRA contributions exceed the amount that can be contributed (deduction plus nondeductible contributions would be less than total contributions; see Pub. 590-A)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [ira.line11a, ira.h_cap_a]}
        - op: test
          all:
            - {op: test, eq: [ira.joint, {const: true}]}
            - {op: test, gt: [ira.line11b, ira.h_limit_b]}
    note: >-
      Item 10 of the line 20 instructions sends filers to Pub. 590-A when the deduction plus nondeductible
      contributions is less than total traditional contributions. That is read as contributions above the
      contribution limit: the smaller of $7,000/$8,000 or compensation. For joint returns, low combined
      compensation is already refused by kbh_short. Roth contributions counting toward the same limit are
      left to the person-level excess screen.

  - id: ira.cov_gate
    printed: "(gate)"
    label: "You made traditional IRA contributions, you or your spouse were covered by a retirement plan, and you received social security benefits (use the worksheets in Pub. 590-A)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.anyone_covered, {const: true}]}
        - {op: test, gt: [ira.h_trad_total, {const: 0}]}
        - {op: test, eq: [ssb.has_benefits, {const: true}]}
    note: >-
      Inferred from the line 6a/6b exception: with traditional IRA contributions and plan coverage, use
      Pub. 590-A to figure both taxable benefits and the IRA deduction.

  - id: ira.excl_gate
    printed: "(gate)"
    label: "Covered by a retirement plan and you file Form 2555 or 8815, or exclude employer-provided adoption benefits (see Pub. 590-A)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.anyone_covered, {const: true}]}
        - {op: test, eq: [sa.excluded_income, {const: true}]}
    note: >-
      Form 2555 is detected through sa.excluded_income. Form 8815 exclusions and excluded adoption benefits
      are already outside scope (sb.unsupported, scope.other_income).

  - id: ira.h_12a
    printed: "(helper)"
    label: "Smaller of line 7a or line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.line7a, ira.line10]}

  - id: ira.line12a
    printed: "12a"
    label: "On line 12a, enter the smallest of line 7a, 10, or 11a. This is the most you can deduct"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.h_12a, ira.line11a]}
    refuses: [ira.kbh_short, ira.both_kinds, ira.over_comp, ira.cov_gate, ira.excl_gate]

  - id: ira.h_12b
    printed: "(helper)"
    label: "Smaller of line 7b or line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.line7b, ira.line10]}

  - id: ira.line12b
    printed: "12b"
    label: "On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.h_12b, ira.line11b]}
    refuses: [ira.kbh_short, ira.both_kinds, ira.over_comp, ira.cov_gate, ira.excl_gate]

  - id: ira.line20
    printed: "(helper)"
    label: "Add the amounts on lines 12a and 12b and enter the total on Schedule 1, line 20"
    type: NonNegDollars
    expr: {op: sum, of: [ira.line12a, ira.line12b]}
    refuses: [ira.deduct_less]
    note: "Choosing to deduct a smaller amount and treat the rest as nondeductible is not computed; that choice is refused."
```
```
