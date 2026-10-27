# Transcription agreement — s1a

Second transcription of `Schedule 1-A (Form 1040) — Additional Deductions` by an isolated model (spec 6.5), compared line by line with `forms/2025/s1a.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 2a067a6000c35550296eb9883b7fc3d22c1148aaa4a4b3082544022d6756dd00 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 3130b38ffe7c156858201da9c15524f13e1a15ad51e23cdf9c8c251d0c85ae2d |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d9d296549ec3233df658d3b4b072e05ab7e3e0325875ce858fc9709791e0cdfc |
| printed lines compared | 43 |
| agree / disagree / missing | 8 / 35 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104, 105, 106, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104, 106, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- s1a.s1a.h_tip_employers: reference 'tip_employers' does not resolve
- s1a.s1a.h_tip_reported: reference 'tip_reported' does not resolve
- s1a.s1a.h_tip_total: reference 'tip_total' does not resolve
- s1a.s1a.h_ot_total: reference 'ot_total' does not resolve
- s1a.s1a.h_car_total: reference 'col_iii' does not resolve

## Lines

### 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

### 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

### 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

### 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

### 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

### 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

### 3 — Add lines 1 and 2e
Status: **AGREE**

### 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, bo
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 1, "type": "Count"}], "test": "le"}, "then": {"collection": "person", "field": "person.tip_reported", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"collection": "person", "field": "tip_employers", "op": "sum_over", "where": null}, {"const": 1, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"collection": "person", "field": "tip_reported", "op": "sum_over", "where": null}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "tip_employers", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "s1a.h_tip_employers", "message": "s1a.s1a.h_tip_employers: reference 'tip_employers' does not resolve"}, {"line": "s1a.h_tip_reported", "message": "s1a.s1a.h_tip_reported: reference 'tip_reported' does not resolve"}]}
```

Second transcription's note: Uses the person collection's reported-tip aggregate; Form 4137 tips are outside the closed input interface.

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 4a's dependency closure carries that error: its expression reads s1a.h_tip_employers and s1a.h_tip_reported. This ruling adjudicates the declaration, not the tax reading (i1040gi p. 101, Part II caution; p. 104, Line 4a). Triage cannot execute a reply with any validation error, so no comparison was run.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Second transcription's note: Form 4137 unreported tips are outside the closed input interface; entered as zero.

Ruling: scope; i1040gi p. 104, Line 4b: "Enter the qualified tips included on Form 4137, line 1, row A, column (c)."; p. 101: "If you received cash and charge tips of $20 or more in a calendar month and didn’t report all of those tips to your employer, you must file Form 4137." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate enters $0 with no refusal. The project's line 4b is $0 too, except on Form 4137 returns, which it refuses at its cited gate s2.other (stage12.refuse.form4137_one_employer and stage12.refuse.form4137_two_employers, refused); those returns are refused at s2.other in any case, so the candidate's $0 reaches no computed return. The only difference is the project's scope refusal.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 1, "type": "Count"}], "test": "le"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"collection": "person", "field": "tip_employers", "op": "sum_over", "where": null}, {"const": 1, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "tip_employers", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "tip_total", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "s1a.h_tip_employers", "message": "s1a.s1a.h_tip_employers: reference 'tip_employers' does not resolve"}, {"line": "s1a.h_tip_reported", "message": "s1a.s1a.h_tip_reported: reference 'tip_reported' does not resolve"}, {"line": "s1a.h_tip_total", "message": "s1a.s1a.h_tip_total: reference 'tip_total' does not resolve"}]}
```

Second transcription's note: Multiple-employer worksheet is represented by the person collection's total-tip aggregate.

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 4c's dependency closure carries that error: its expression reads s1a.h_tip_employers, s1a.h_tip_total and s1a.h_line4c_single, which reads line 4a. This ruling adjudicates the declaration, not the tax reading (i1040gi p. 104, Line 4c and the Qualified Tips From More Than One Employer Worksheet). Triage cannot execute a reply with any validation error, so no comparison was run.

### 5 — Qualified tips received in the course of a trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Second transcription's note: Trade-or-business qualified tips are outside the closed input interface; entered as zero.

Ruling: model error; i1040gi p. 104, Line 5: "Include the qualified tips you and/or your spouse received in the course of a trade or business, but only to the extent the trade or business in which you received the qualified tips has net income." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate enters $0 with no screen, its note saying trade-or-business tips are "outside the closed input interface"; the prompt's published interface includes the per-business screen sc.tips_ot and the gate s1.sc_1a. A filer who received qualified tips in a Schedule C business is given $0 on line 5, and the candidate's line 13 carries no refusal either, so the deduction the source allows is dropped. Example (evaluated read-only with engine/dist/main.js eval): stage14.refuse.sch1a_tips_business_only with s1a.tips true and one $5,000 employee tip job added: project line 5 refusal at s1.sc_1a (and Form 1040 line 37 refused with the shared BUG-0154 text); candidate $0.00 by its expression.

### 6 — Add lines 4c and 5
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}, "invalid_model_types": [{"line": "s1a.h_tip_employers", "message": "s1a.s1a.h_tip_employers: reference 'tip_employers' does not resolve"}, {"line": "s1a.h_tip_reported", "message": "s1a.s1a.h_tip_reported: reference 'tip_reported' does not resolve"}, {"line": "s1a.h_tip_total", "message": "s1a.s1a.h_tip_total: reference 'tip_total' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 6's dependency closure carries that error: it adds line 4c (s1a.h_tip_employers, s1a.h_tip_total) and line 5. This ruling adjudicates the declaration, not the tax reading (Schedule 1-A line 6). Triage cannot execute a reply with any validation error, so no comparison was run.

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "s1a.h_tip_employers", "message": "s1a.s1a.h_tip_employers: reference 'tip_employers' does not resolve"}, {"line": "s1a.h_tip_reported", "message": "s1a.s1a.h_tip_reported: reference 'tip_reported' does not resolve"}, {"line": "s1a.h_tip_total", "message": "s1a.s1a.h_tip_total: reference 'tip_total' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 7's dependency closure carries that error: it reads line 6, which reads line 4c. This ruling adjudicates the declaration, not the tax reading (Schedule 1-A line 7). Triage cannot execute a reply with any validation error, so no comparison was run.

### 8 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 8 copies line 3 with no test of whether Part II is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part2 false). It is the same expression as the Claude reply's line 8, which triage executed: classm.f2441.1.deepseek, s1a.tips false, completed: project $0.00 / $50,000.00; 509 completed returns differ (triage/s1a.json).

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.base_other"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 9 enters $150,000 or $300,000 with no test of whether Part II is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part2 false). It is the same expression as the Claude reply's line 9, which triage executed: classm.f2441.1.deepseek: project $0.00 / $150,000.00; 510 completed returns differ (triage/s1a.json).

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "8"}, "op": "subtract", "take": {"line": "9"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "8"}, "op": "subtract", "take": {"line": "9"}}
```

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 10 subtracts line 9 from line 8 with no test of whether Part II is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part2 false). It is the same expression as the Claude reply's line 10, which triage executed: classm.f2441.1.deepseek: project $0.00 / -$100,000.00; 508 completed returns differ (triage/s1a.json).

### 12 — Multiply line 11 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "8"}, "op": "subtract_floor0", "take": {"line": "9"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "10"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "10"}], "test": "lt"}, "then": {"amount": {"of": {"from": {"line": "10"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}], "op": "choose"}
```

Second transcription's note: Line 11 is floor(line 10 / $1,000); line 12 is line 11 times $100, implemented as floor-to-$1,000 of positive excess times 1/10.

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 12 figures the $100-per-$1,000 reduction (zero when line 10 is zero or less) with no test of whether Part II is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part2 false). It is an expression equivalent to the Claude reply's line 12, which triage executed: classm.f5695.7: project $0.00 / $9,400.00; 61 completed returns differ (triage/s1a.json).

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "8"}, {"line": "9"}], "test": "le"}, "then": {"line": "7"}}, {"guard": {"args": [{"line": "9"}, {"line": "8"}], "test": "lt"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}, "invalid_model_types": [{"line": "s1a.h_tip_employers", "message": "s1a.s1a.h_tip_employers: reference 'tip_employers' does not resolve"}, {"line": "s1a.h_tip_reported", "message": "s1a.s1a.h_tip_reported: reference 'tip_reported' does not resolve"}, {"line": "s1a.h_tip_total", "message": "s1a.s1a.h_tip_total: reference 'tip_total' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 13's dependency closure carries that error: it subtracts line 12 from line 7, which reads line 6 and line 4c. This ruling adjudicates the declaration, not the tax reading (i1040gi p. 101, Part II; p. 104, Line 5). Read against the source, the line would also lack any refusal for qualified tips received in a trade or business (see line 5) and any married filing separately bar ("If you are married, you must file a joint return with your spouse to claim this deduction", p. 101). Triage cannot execute a reply with any validation error, so no comparison was run.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"collection": "person", "field": "person.ot_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"collection": "person", "field": "ot_total", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "s1a.h_ot_total", "message": "s1a.s1a.h_ot_total: reference 'ot_total' does not resolve"}]}
```

Second transcription's note: Uses the person collection's overtime aggregate; Form W-2 box 1 qualification is represented by the s1a.overtime gate.

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 14a's dependency closure carries that error: its expression reads s1a.h_ot_total. This ruling adjudicates the declaration, not the tax reading (i1040gi p. 106, Part III; p. 108, Line 14a). Triage cannot execute a reply with any validation error, so no comparison was run.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Second transcription's note: Nonemployee qualified overtime is outside the closed input interface; entered as zero.

Ruling: model error; i1040gi p. 108, Line 14b: "Enter on Line 14b only the qualified overtime compensation amount that is included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate enters $0 with no screen, its note saying nonemployee overtime is "outside the closed input interface"; the published interface includes sc.tips_ot and s1.sc_1a. Example: stage14.sch1a.refuse_overtime_1099 (s1a.overtime true, sc[gig].tips_ot true, Form 1099 overtime): project line 14b refusal at s1.sc_1a (evaluated read-only); candidate $0.00 by its expression, and its line 21 has no refusal, so the line 14b amount is dropped.

### 14c — Add lines 14a and 14b
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}, "invalid_model_types": [{"line": "s1a.h_ot_total", "message": "s1a.s1a.h_ot_total: reference 'ot_total' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 14c's dependency closure carries that error: it adds line 14a (s1a.h_ot_total) and line 14b. This ruling adjudicates the declaration, not the tax reading (Schedule 1-A line 14c). Triage cannot execute a reply with any validation error, so no comparison was run.

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.ot_max_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.ot_max_other"}}], "op": "choose"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "s1a.h_ot_total", "message": "s1a.s1a.h_ot_total: reference 'ot_total' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 15's dependency closure carries that error: it reads line 14c, which reads line 14a. This ruling adjudicates the declaration, not the tax reading (Schedule 1-A line 15). Triage cannot execute a reply with any validation error, so no comparison was run.

### 16 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 16 copies line 3 with no test of whether Part III is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part3 false). It is the same expression as the Claude reply's line 16, which triage executed: classm.f2441.1.deepseek, s1a.overtime false: project $0.00 / $50,000.00; 509 completed returns differ (triage/s1a.json).

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.base_other"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 17 enters $150,000 or $300,000 with no test of whether Part III is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part3 false). It is the same expression as the Claude reply's line 17, which triage executed: classm.f2441.1.deepseek: project $0.00 / $150,000.00; 510 completed returns differ (triage/s1a.json).

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "16"}, "op": "subtract", "take": {"line": "17"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "16"}, "op": "subtract", "take": {"line": "17"}}
```

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 18 subtracts line 17 from line 16 with no test of whether Part III is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part3 false). It is the same expression as the Claude reply's line 18, which triage executed: classm.f2441.1.deepseek: project $0.00 / -$100,000.00; 508 completed returns differ (triage/s1a.json).

### 20 — Multiply line 19 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "16"}, "op": "subtract_floor0", "take": {"line": "17"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "18"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "18"}], "test": "lt"}, "then": {"amount": {"of": {"from": {"line": "18"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}], "op": "choose"}
```

Second transcription's note: Line 19 is floor(line 18 / $1,000); line 20 is line 19 times $100, implemented as floor-to-$1,000 of positive excess times 1/10.

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 20 figures the $100-per-$1,000 reduction with no test of whether Part III is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part3 false). It is an expression equivalent to the Claude reply's line 20, which triage executed: classm.f5695.7: project $0.00 / $9,400.00; 63 completed returns differ (triage/s1a.json).

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "16"}, {"line": "17"}], "test": "le"}, "then": {"line": "15"}}, {"guard": {"args": [{"line": "17"}, {"line": "16"}], "test": "lt"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}, "invalid_model_types": [{"line": "s1a.h_ot_total", "message": "s1a.s1a.h_ot_total: reference 'ot_total' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 21's dependency closure carries that error: it subtracts line 20 from line 15, which reads line 14c and line 14a. This ruling adjudicates the declaration, not the tax reading (i1040gi p. 106, Part III; p. 108, Line 14b). Read against the source, the line would also lack the Form 1099 overtime refusal (see line 14b) and the married filing separately bar (p. 106). Triage cannot execute a reply with any validation error, so no comparison was run.

### 23 — Add lines 22a and 22b, column (iii)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"collection": "carloan", "field": "carloan.col_iii", "op": "sum_over", "where": null}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"collection": "carloan", "field": "col_iii", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "s1a.h_car_total", "message": "s1a.s1a.h_car_total: reference 'col_iii' does not resolve"}]}
```

Second transcription's note: Uses the carloan collection's column (iii) aggregate.

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 23's dependency closure carries that error: its expression reads s1a.h_car_total (col_iii). This ruling adjudicates the declaration, not the tax reading (i1040gi p. 109, Part IV; p. 110, Line 22). Triage cannot execute a reply with any validation error, so no comparison was run.

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"of": [{"line": "23"}, {"param": "s1a.car_max"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "23"}, {"param": "s1a.car_max"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "s1a.h_car_total", "message": "s1a.s1a.h_car_total: reference 'col_iii' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 24's dependency closure carries that error: it reads line 23, which reads s1a.h_car_total. This ruling adjudicates the declaration, not the tax reading (Schedule 1-A line 24). Triage cannot execute a reply with any validation error, so no comparison was run.

### 25 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"line": "3"}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 25 copies line 3 with no test of whether Part IV is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part4 false). It is the same expression as the Claude reply's line 25, which triage executed: classm.f2441.1.deepseek, s1a.carloan false: project $0.00 / $50,000.00; 509 completed returns differ (triage/s1a.json).

### 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.car_base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.car_base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.car_base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.car_base_other"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 26 enters $100,000 or $200,000 with no test of whether Part IV is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part4 false). It is the same expression as the Claude reply's line 26, which triage executed: classm.f2441.1.deepseek: project $0.00 / $100,000.00; 510 completed returns differ (triage/s1a.json).

### 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"from": {"line": "25"}, "op": "subtract", "take": {"line": "26"}}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "25"}, "op": "subtract", "take": {"line": "26"}}
```

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 27 subtracts line 26 from line 25 with no test of whether Part IV is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part4 false). It is the same expression as the Claude reply's line 27, which triage executed: classm.f2441.1.deepseek: project $0.00 / -$50,000.00; 508 completed returns differ (triage/s1a.json).

### 29 — Multiply line 28 by $200
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"amount": {"of": {"from": {"line": "25"}, "op": "subtract_floor0", "take": {"line": "26"}}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "27"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "27"}], "test": "lt"}, "then": {"amount": {"of": {"from": {"line": "27"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}}], "op": "choose"}
```

Second transcription's note: Line 28 is ceil(line 27 / $1,000); line 29 is line 28 times $200, implemented as ceil-to-$1,000 of positive excess times 1/5.

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 29 figures the $200-per-$1,000 reduction with no test of whether Part IV is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part4 false). It is an expression equivalent to the Claude reply's line 29, which triage executed: classm.f8889.1.deepseek: project $0.00 / $4,800.00; 107 completed returns differ (triage/s1a.json).

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "25"}, {"line": "26"}], "test": "le"}, "then": {"line": "24"}}, {"guard": {"args": [{"line": "26"}, {"line": "25"}], "test": "lt"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}, "invalid_model_types": [{"line": "s1a.h_car_total", "message": "s1a.s1a.h_car_total: reference 'col_iii' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 30's dependency closure carries that error: it subtracts line 29 from line 24, which reads line 23 and s1a.h_car_total. This ruling adjudicates the declaration, not the tax reading (i1040gi p. 110, Line 27). Triage cannot execute a reply with any validation error, so no comparison was run.

### 31 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 31 copies line 3 with no test of whether Part V is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false). It is the same expression as the Claude reply's line 31, which triage executed: classm.f2441.1.deepseek, filer not born before January 2, 1961: project $0.00 / $50,000.00; 499 completed returns differ (triage/s1a.json).

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.senior_base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.senior_base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.senior_base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.senior_base_other"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 32 enters $75,000 or $150,000 with no test of whether Part V is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false). It is the same expression as the Claude reply's line 32, which triage executed: classm.f2441.1.deepseek: project $0.00 / $75,000.00; 500 completed returns differ (triage/s1a.json).

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "31"}, "op": "subtract", "take": {"line": "32"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "31"}, "op": "subtract", "take": {"line": "32"}}
```

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 33 subtracts line 32 from line 31 with no test of whether Part V is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false). It is the same expression as the Claude reply's line 33, which triage executed: classm.f2441.1.deepseek: project $0.00 / -$25,000.00; 497 completed returns differ (triage/s1a.json).

### 34 — Multiply line 33 by 6% (0.06)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"line": "32"}}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "33"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "33"}], "test": "lt"}, "then": {"amount": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 34 figures 6% of line 33 (zero when line 33 is zero or less) with no test of whether Part V is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false). It is an expression equivalent to the Claude reply's line 34, which triage executed: classm.f8889.1.deepseek: project $0.00 / $4,435.68; 159 completed returns differ (triage/s1a.json).

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"line": "31"}, {"line": "32"}], "test": "le"}, "then": {"param": "s1a.senior_amount"}}, {"guard": {"args": [{"line": "32"}, {"line": "31"}], "test": "lt"}, "then": {"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}
```

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate's line 35 subtracts line 34 from $6,000 with no test of whether Part V is filled out, so it shows a nonzero amount on returns where the Part is not filled out. Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false). It is the same expression as the Claude reply's line 35, which triage executed: classm.f2441.1.deepseek: project $0.00 / $6,000.00; 443 completed returns differ (triage/s1a.json).

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"line": "35"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"line": "35"}
```

Second transcription's note: Assumes the taxpayer has a valid SSN and was born before January 2, 1961; the closed input interface does not supply these qualification facts.

Ruling: model error; Schedule 1-A line 36a: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35"; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate copies line 35 with no age, SSN, filing-status or death test, its note saying the interface "does not supply these qualification facts"; the prompt's published interface includes person.age65, person.work_ssn and person.died_before_65. Every filer is given the senior deduction. Example: classm.f2441.1.deepseek (head of household, person.age65 false, completed): project line 36a $0.00 (evaluated read-only); candidate line 35 is $6,000 there (line 33 is $50,000 less $75,000, below zero; the Claude reply's identical line 35 evaluates to $6,000.00, triage/s1a.json), so the candidate's line 36a is $6,000.00 and Form 1040 line 13b would be $6,000 too high.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"line": "35"}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Second transcription's note: Spouse qualification facts are not supplied by the closed input interface; entered as zero.

Ruling: model error; Schedule 1-A line 36b: "If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35". Ruled by reading the expression against the source: the expression has no validation error in its own closure, but triage cannot execute a reply with any validation error (triage/s1a.deepseek.json, state invalid). The candidate enters $0 on every return, its note saying spouse facts are not supplied; the published interface includes person.role, person.age65 and person.work_ssn. Example: stage13.senior_spouse_only (married filing jointly, spouse born before January 2, 1961, with a valid SSN): project line 36b $6,000.00 (fixture expectation); candidate $0.00 by its expression, so the spouse's deduction is lost.

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "13"}, {"line": "21"}, {"line": "30"}, {"line": "37"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "13"}, {"line": "21"}, {"line": "30"}, {"line": "37"}], "op": "sum"}, "invalid_model_types": [{"line": "s1a.h_tip_employers", "message": "s1a.s1a.h_tip_employers: reference 'tip_employers' does not resolve"}, {"line": "s1a.h_tip_reported", "message": "s1a.s1a.h_tip_reported: reference 'tip_reported' does not resolve"}, {"line": "s1a.h_tip_total", "message": "s1a.s1a.h_tip_total: reference 'tip_total' does not resolve"}, {"line": "s1a.h_ot_total", "message": "s1a.s1a.h_ot_total: reference 'ot_total' does not resolve"}, {"line": "s1a.h_car_total", "message": "s1a.s1a.h_car_total: reference 'col_iii' does not resolve"}]}
```

Ruling: model error; on the validation failure. The reply fails reference validation (triage/s1a.deepseek.json, state invalid; the log's "Host-side model expression type checks"): s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total use the bare fields tip_employers, tip_reported, tip_total, ot_total and col_iii, which do not resolve; the published interface in the prompt names them person.tip_employers, person.tip_reported, person.tip_total, person.ot_total and carloan.col_iii. Line 38's dependency closure carries that error: it adds lines 13, 21 and 30, whose closures read s1a.h_tip_employers, s1a.h_tip_reported, s1a.h_tip_total, s1a.h_ot_total and s1a.h_car_total. This ruling adjudicates the declaration, not the tax reading (Schedule 1-A line 38). Triage cannot execute a reply with any validation error, so no comparison was run.

## Raw second transcription

```yaml
lines:
  - id: s1a.line1
    printed: "1"
    label: "Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
  - id: s1a.line2a
    printed: "2a"
    label: "Enter any income from Puerto Rico that you excluded"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Puerto Rico excluded income is outside the closed input interface; entered as zero."
  - id: s1a.line2b
    printed: "2b"
    label: "Enter the amount from Form 2555, line 45"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Form 2555 exclusion is outside the closed input interface; entered as zero."
  - id: s1a.line2c
    printed: "2c"
    label: "Enter the amount from Form 2555, line 50"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Form 2555 exclusion is outside the closed input interface; entered as zero."
  - id: s1a.line2d
    printed: "2d"
    label: "Enter the amount from Form 4563, line 15"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Form 4563 exclusion is outside the closed input interface; entered as zero."
  - id: s1a.line2e
    printed: "2e"
    label: "Add lines 2a, 2b, 2c, and 2d"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line2a, s1a.line2b, s1a.line2c, s1a.line2d]}
  - id: s1a.line3
    printed: "3"
    label: "Add lines 1 and 2e"
    type: Dollars
    expr: {op: sum, of: [s1a.line1, s1a.line2e]}
  - id: s1a.line4a
    printed: "4a"
    label: "Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            not:
              op: test
              eq: [s1a.tips, {const: true}]
          then: s1a.h_zero_money
        - guard:
            op: test
            all:
              - op: test
                eq: [s1a.tips, {const: true}]
              - op: test
                gt: [s1a.h_tip_employers, {const: 1, type: Count}]
          then: s1a.h_zero_money
        - guard:
            op: test
            all:
              - op: test
                eq: [s1a.tips, {const: true}]
              - op: test
                le: [s1a.h_tip_employers, {const: 1, type: Count}]
          then: s1a.h_tip_reported
    note: "Uses the person collection's reported-tip aggregate; Form 4137 tips are outside the closed input interface."
  - id: s1a.line4b
    printed: "4b"
    label: "Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Form 4137 unreported tips are outside the closed input interface; entered as zero."
  - id: s1a.line4c
    printed: "4c"
    label: "If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c. If you received tips as an employee in more than one occupation, see the instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            not:
              op: test
              eq: [s1a.tips, {const: true}]
          then: s1a.h_zero_money
        - guard:
            op: test
            all:
              - op: test
                eq: [s1a.tips, {const: true}]
              - op: test
                gt: [s1a.h_tip_employers, {const: 1, type: Count}]
          then: s1a.h_tip_total
        - guard:
            op: test
            all:
              - op: test
                eq: [s1a.tips, {const: true}]
              - op: test
                le: [s1a.h_tip_employers, {const: 1, type: Count}]
          then: s1a.h_line4c_single
    note: "Multiple-employer worksheet is represented by the person collection's total-tip aggregate."
  - id: s1a.line5
    printed: "5"
    label: "Qualified tips received in the course of a trade or business. Qualified tip amount included in Form 1099-NEC, box 1; Form 1099-MISC, box 3; or Form 1099-K, box 1a. Do not enter more than the net profit from the trade or business. If you received qualified tips in the course of more than one trade or business or in more than one occupation, see instructions"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Trade-or-business qualified tips are outside the closed input interface; entered as zero."
  - id: s1a.line6
    printed: "6"
    label: "Add lines 4c and 5"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line4c, s1a.line5]}
  - id: s1a.line7
    printed: "7"
    label: "Enter the smaller of the amount on line 6 or $25,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [s1a.line6, s1a.h_tips_max]}
  - id: s1a.line8
    printed: "8"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}
  - id: s1a.line9
    printed: "9"
    label: "Enter $150,000 ($300,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_other
  - id: s1a.line10
    printed: "10"
    label: "Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13"
    type: Dollars
    expr: {op: subtract, from: s1a.line8, take: s1a.line9}
  - id: s1a.line12
    printed: "12"
    label: "Multiply line 11 by $100"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line10, {const: 0}]}
          then: s1a.h_zero_money
        - guard: {op: test, gt: [s1a.line10, {const: 0}]}
          then: s1a.h_tips_12_product
    note: "Line 11 is floor(line 10 / $1,000); line 12 is line 11 times $100, implemented as floor-to-$1,000 of positive excess times 1/10."
  - id: s1a.line13
    printed: "13"
    label: "Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line7, take: s1a.line12}
  - id: s1a.line14a
    printed: "14a"
    label: "Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            not:
              op: test
              eq: [s1a.overtime, {const: true}]
          then: s1a.h_zero_money
        - guard:
            op: test
            eq: [s1a.overtime, {const: true}]
          then: s1a.h_ot_total
    note: "Uses the person collection's overtime aggregate; Form W-2 box 1 qualification is represented by the s1a.overtime gate."
  - id: s1a.line14b
    printed: "14b"
    label: "Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3 (see instructions)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Nonemployee qualified overtime is outside the closed input interface; entered as zero."
  - id: s1a.line14c
    printed: "14c"
    label: "Add lines 14a and 14b"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line14a, s1a.line14b]}
  - id: s1a.line15
    printed: "15"
    label: "Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [s1a.line14c, s1a.h_ot_limit]}
  - id: s1a.line16
    printed: "16"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}
  - id: s1a.line17
    printed: "17"
    label: "Enter $150,000 ($300,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_other
  - id: s1a.line18
    printed: "18"
    label: "Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21"
    type: Dollars
    expr: {op: subtract, from: s1a.line16, take: s1a.line17}
  - id: s1a.line20
    printed: "20"
    label: "Multiply line 19 by $100"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line18, {const: 0}]}
          then: s1a.h_zero_money
        - guard: {op: test, gt: [s1a.line18, {const: 0}]}
          then: s1a.h_ot_20_product
    note: "Line 19 is floor(line 18 / $1,000); line 20 is line 19 times $100, implemented as floor-to-$1,000 of positive excess times 1/10."
  - id: s1a.line21
    printed: "21"
    label: "Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line15, take: s1a.line20}
  - id: s1a.line23
    printed: "23"
    label: "Add lines 22a and 22b, column (iii)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            not:
              op: test
              eq: [s1a.carloan, {const: true}]
          then: s1a.h_zero_money
        - guard:
            op: test
            eq: [s1a.carloan, {const: true}]
          then: s1a.h_car_total
    note: "Uses the carloan collection's column (iii) aggregate."
  - id: s1a.line24
    printed: "24"
    label: "Enter the smaller of the amount on line 23 or $10,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [s1a.line23, s1a.h_car_max]}
  - id: s1a.line25
    printed: "25"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}
  - id: s1a.line26
    printed: "26"
    label: "Enter $100,000 ($200,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_car_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_car_base_other
  - id: s1a.line27
    printed: "27"
    label: "Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30"
    type: Dollars
    expr: {op: subtract, from: s1a.line25, take: s1a.line26}
  - id: s1a.line29
    printed: "29"
    label: "Multiply line 28 by $200"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line27, {const: 0}]}
          then: s1a.h_zero_money
        - guard: {op: test, gt: [s1a.line27, {const: 0}]}
          then: s1a.h_car_29_product
    note: "Line 28 is ceil(line 27 / $1,000); line 29 is line 28 times $200, implemented as ceil-to-$1,000 of positive excess times 1/5."
  - id: s1a.line30
    printed: "30"
    label: "Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line24, take: s1a.line29}
  - id: s1a.line31
    printed: "31"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}
  - id: s1a.line32
    printed: "32"
    label: "Enter $75,000 ($150,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_senior_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_senior_base_other
  - id: s1a.line33
    printed: "33"
    label: "Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35"
    type: Dollars
    expr: {op: subtract, from: s1a.line31, take: s1a.line32}
  - id: s1a.line34
    printed: "34"
    label: "Multiply line 33 by 6% (0.06)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line33, {const: 0}]}
          then: s1a.h_zero_money
        - guard: {op: test, gt: [s1a.line33, {const: 0}]}
          then: s1a.h_line34_product
  - id: s1a.line35
    printed: "35"
    label: "Subtract line 34 from $6,000. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.h_senior_amount, take: s1a.line34}
  - id: s1a.line36a
    printed: "36a"
    label: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr: {op: copy, from: s1a.line35}
    note: "Assumes the taxpayer has a valid SSN and was born before January 2, 1961; the closed input interface does not supply these qualification facts."
  - id: s1a.line36b
    printed: "36b"
    label: "If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Spouse qualification facts are not supplied by the closed input interface; entered as zero."
  - id: s1a.line37
    printed: "37"
    label: "Enhanced deduction for seniors. Add lines 36a and 36b"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line36a, s1a.line36b]}
  - id: s1a.line38
    printed: "38"
    label: "Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form 1040-NR, line 13c"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line13, s1a.line21, s1a.line30, s1a.line37]}

  - id: s1a.h_zero_money
    printed: "(helper)"
    label: "Zero money helper"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: s1a.h_base_other
    printed: "(helper)"
    label: "Part II/III MAGI base for other filing statuses"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_other}
  - id: s1a.h_base_joint
    printed: "(helper)"
    label: "Part II/III MAGI base for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_joint}
  - id: s1a.h_tip_employers
    printed: "(helper)"
    label: "Total tip employers"
    type: Count
    expr: {op: sum_over, collection: person, field: tip_employers}
  - id: s1a.h_tip_reported
    printed: "(helper)"
    label: "Reported qualified tips"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: tip_reported}
  - id: s1a.h_tip_total
    printed: "(helper)"
    label: "Total qualified tips"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: tip_total}
  - id: s1a.h_line4c_single
    printed: "(helper)"
    label: "Line 4c single-employer amount"
    type: NonNegDollars
    expr: {op: larger_of, of: [s1a.line4a, s1a.line4b]}
  - id: s1a.h_tips_excess_pos
    printed: "(helper)"
    label: "Positive tips phase-out excess"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line10, take: {const: 0}}
  - id: s1a.h_tips_floor
    printed: "(helper)"
    label: "Tips excess rounded down to the next $1,000"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_tips_excess_pos, unit: 100000, rule: down}
  - id: s1a.h_tips_12_product
    printed: "(helper)"
    label: "Line 12 reduction amount"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_tips_floor, rate: {param: s1a.hundred_per_thousand}}
  - id: s1a.h_tips_max
    printed: "(helper)"
    label: "Maximum qualified tips deduction"
    type: NonNegDollars
    expr: {op: param, ref: s1a.tips_max}
  - id: s1a.h_ot_total
    printed: "(helper)"
    label: "Total qualified overtime compensation"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: ot_total}
  - id: s1a.h_ot_max_other
    printed: "(helper)"
    label: "Maximum qualified overtime deduction for other filing statuses"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_other}
  - id: s1a.h_ot_max_joint
    printed: "(helper)"
    label: "Maximum qualified overtime deduction for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_joint}
  - id: s1a.h_ot_limit
    printed: "(helper)"
    label: "Qualified overtime maximum for the filing status"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_ot_max_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_ot_max_other
  - id: s1a.h_ot_excess_pos
    printed: "(helper)"
    label: "Positive overtime phase-out excess"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line18, take: {const: 0}}
  - id: s1a.h_ot_floor
    printed: "(helper)"
    label: "Overtime excess rounded down to the next $1,000"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_ot_excess_pos, unit: 100000, rule: down}
  - id: s1a.h_ot_20_product
    printed: "(helper)"
    label: "Line 20 reduction amount"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_ot_floor, rate: {param: s1a.hundred_per_thousand}}
  - id: s1a.h_car_total
    printed: "(helper)"
    label: "Total Schedule 1-A car loan interest"
    type: NonNegDollars
    expr: {op: sum_over, collection: carloan, field: col_iii}
  - id: s1a.h_car_max
    printed: "(helper)"
    label: "Maximum car loan interest deduction"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_max}
  - id: s1a.h_car_base_other
    printed: "(helper)"
    label: "Car loan MAGI base for other filing statuses"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_other}
  - id: s1a.h_car_base_joint
    printed: "(helper)"
    label: "Car loan MAGI base for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_joint}
  - id: s1a.h_car_excess_pos
    printed: "(helper)"
    label: "Positive car loan phase-out excess"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line27, take: {const: 0}}
  - id: s1a.h_car_ceil
    printed: "(helper)"
    label: "Car loan excess rounded up to the next $1,000"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_car_excess_pos, unit: 100000, rule: up}
  - id: s1a.h_car_29_product
    printed: "(helper)"
    label: "Line 29 reduction amount"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_car_ceil, rate: {param: s1a.two_hundred_per_thousand}}
  - id: s1a.h_senior_base_other
    printed: "(helper)"
    label: "Senior deduction MAGI base for other filing statuses"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_other}
  - id: s1a.h_senior_base_joint
    printed: "(helper)"
    label: "Senior deduction MAGI base for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_joint}
  - id: s1a.h_line33_pos
    printed: "(helper)"
    label: "Positive senior phase-out excess"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line33, take: {const: 0}}
  - id: s1a.h_line34_product
    printed: "(helper)"
    label: "Line 34 senior phase-out amount"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_line33_pos, rate: {param: s1a.senior_rate}}
  - id: s1a.h_senior_amount
    printed: "(helper)"
    label: "Maximum enhanced deduction for seniors per person"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_amount}
```
