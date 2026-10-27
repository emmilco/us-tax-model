# Transcription agreement — s1a

Second transcription of `Schedule 1-A (Form 1040) — Additional Deductions` by an isolated model (spec 6.5), compared line by line with `forms/2025/s1a.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2a067a6000c35550296eb9883b7fc3d22c1148aaa4a4b3082544022d6756dd00 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a06d5399c6aea3a0e3abd04d0e257b0300df1428c1d01a472537ee7f8780bd0a |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d9d296549ec3233df658d3b4b072e05ab7e3e0325875ce858fc9709791e0cdfc |
| printed lines compared | 43 |
| agree / disagree / missing | 9 / 34 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104, 105, 106, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104, 106, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

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
{"alternatives": [{"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "eq"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: With one employer, the worksheet row's column (d) is the greater of column (b) and column (c). Form 4137 (column (c)) is refused, so column (d) equals the W-2 or Form 4070 amount the filer chose. That amount is used for line 4a. With more than one employer, -0- is entered, as the form says.

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)."; i1040gi p. 104, Line 4a: "If you received qualified tips as an employee with respect to employment with more than one employer, enter -0- on line 4a and see the instructions for line 4c." The candidate's line 4a reads the worksheet roster $tipjob (person.tip_employers, person.tip_total) on every return with no s1a.tips or Part gate, although s1a.tips is in its interface and it tests it on its deduction line. A filer who answers s1a.tips no is never asked for that roster, so the candidate's line 4a is unknown on completed returns where the source needs no answer, because the Part is not filled out at all: an answer required that the source does not need to determine the result. The two value differences are married filing separately returns (stage12.mfs.bar $0.00 / $8,000.00; generated 386), on which the candidate also omits "If you are married, you must file a joint return with your spouse to claim this deduction" (p. 101); both are refused at s3.mfs. Its s2.other refusals are Form 4137 returns the project refuses too. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 407 of 1,707 comparisons agree; differences: 1294 candidate-unknown, 3 candidate-refuses, 2 value, 1 project-unknown; by full-interview outcome of the return: completed: 425 candidate-unknown; incomplete: 208 candidate-unknown; refused: 661 candidate-unknown, 3 candidate-refuses, 2 value, 1 project-unknown; witnesses (project / candidate): value e.g. stage12.mfs.bar ($0.00 / $8,000.00; return refused), generated 386 ($0.00 / $8,265.95; return refused); candidate-refuses e.g. stage12.refuse.form4137_one_employer ($8,000.00 / refusal at s2.other; return refused), generated 95 ($13,926.81 / refusal at s2.other; return refused); candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $tipjob@person[taxpayer]; return completed), classm.f2441.3.deepseek ($0.00 / unknown $tipjob@person[taxpayer]; return completed); project-unknown e.g. classm.carloan.1 without s1a.tips (unknown s1a.tips / $0.00; return refused).

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

Second transcription's note: Form 4137 (unreported or allocated tips) is outside the tool's scope (screened by f8959.unsupported). Only the case where Form 4137 is not filed is encoded.

Ruling: scope; i1040gi p. 104, Line 4b: "Enter the qualified tips included on Form 4137, line 1, row A, column (c)."; p. 101: "If you received cash and charge tips of $20 or more in a calendar month and didn’t report all of those tips to your employer, you must file Form 4137." Both sides give $0 when Form 4137 is not filed, and no difference is on a completed return. The project refuses Form 4137 returns at its cited gate s2.other (stage12.refuse.form4137_one_employer, stage12.refuse.form4137_two_employers), where the candidate's $0 stands, but those returns are refused at s2.other in any case. The candidate refuses at its own screen f8959.unsupported, and is unknown where that answer is not supplied, only on returns the full interview refuses or leaves incomplete. The project-unknown records withhold s1a.tips, the Part II screen the source needs (p. 101). Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 1,399 of 1,707 comparisons agree; differences: 155 project-unknown, 130 candidate-unknown, 19 candidate-refuses, 4 project-refuses; by full-interview outcome of the return: incomplete: 96 candidate-unknown, 93 project-unknown; refused: 62 project-unknown, 34 candidate-unknown, 19 candidate-refuses, 4 project-refuses; witnesses (project / candidate): candidate-refuses e.g. classm.carloan.1 ($0.00 / refusal at f8959.unsupported; return refused), classm.carloan.2 ($0.00 / refusal at f8959.unsupported; return refused); project-refuses e.g. stage12.refuse.form4137_one_employer (refusal at s2.other / $0.00; return refused), stage12.refuse.form4137_two_employers (refusal at s2.other / $0.00; return refused); candidate-unknown e.g. table.band.first ($0.00 / unknown f8959.unsupported; return incomplete), table.band.mid ($0.00 / unknown f8959.unsupported; return incomplete); project-unknown e.g. classm.f4952.2 (unknown s1a.tips / $0.00; return incomplete), classm.f4952.1 (unknown s1a.tips / $0.00; return refused).

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 1, "type": "Count"}], "test": "le"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "eq"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "ne"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)."; i1040gi p. 104, Line 4c: "If you and/or your spouse received qualified tips as employees with respect to employment with more than one employer, complete the Qualified Tips From More Than One Employer Worksheet." The candidate's line 4c reads the worksheet roster $tipjob (person.tip_employers, person.tip_total) on every return with no s1a.tips or Part gate, although s1a.tips is in its interface and it tests it on its deduction line. A filer who answers s1a.tips no is never asked for that roster, so the candidate's line 4c is unknown on completed returns where the source needs no answer, because the Part is not filled out at all: an answer required that the source does not need to determine the result. The value differences are married filing separately returns (stage12.mfs.bar $0.00 / $8,000.00; generated 258 and 386), refused at s3.mfs; the tipjob.mixed refusals are on refused returns. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 403 of 1,707 comparisons agree; differences: 1294 candidate-unknown, 6 candidate-refuses, 3 value, 1 project-unknown; by full-interview outcome of the return: completed: 425 candidate-unknown; incomplete: 208 candidate-unknown; refused: 661 candidate-unknown, 6 candidate-refuses, 3 value, 1 project-unknown; witnesses (project / candidate): value e.g. stage12.mfs.bar ($0.00 / $8,000.00; return refused), generated 258 ($0.00 / $22,803.80; return refused); candidate-refuses e.g. classm.carloan.4 ($0.00 / refusal at person[taxpayer].tipjob[tip_1].mixed; return refused), generated 96 ($0.00 / refusal at person[taxpayer].tipjob[tip_1].mixed; return refused); candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $tipjob@person[taxpayer]; return completed), classm.f2441.3.deepseek ($0.00 / unknown $tipjob@person[taxpayer]; return completed); project-unknown e.g. classm.carloan.1 without s1a.tips (unknown s1a.tips / $22,539.00; return refused).

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

Second transcription's note: The tool does not compute qualified tips received in a trade or business, including the net income limitation and the Multiple Trades or Businesses Worksheet. It refuses when any Schedule C reports such tips. The sc.tips_ot screen also covers 1099 overtime, so the refusal reaches that case too.

Ruling: scope; i1040gi p. 104, Line 5: "Include the qualified tips you and/or your spouse received in the course of a trade or business, but only to the extent the trade or business in which you received the qualified tips has net income." and p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." The candidate gives $0 and refuses at s1a.h_sc_1a (person.sc_1a, the per-business screen sc.tips_ot) on every return. It refuses the three business-tips or Form 1099 overtime fixtures (stage14.refuse.sch1a_tips, stage14.refuse.sch1a_tips_business_only, stage14.sch1a.refuse_overtime_1099) where the project's line 5 is $0 because the Part II gate is false; the project refuses the same three returns at s1.sc_1a on lines 13 and 21 (BUG-0147, one shared text since BUG-0154), so both refuse them. The project's refusals at its cited screen scope.schedule1 (Schedule E or F trade or business), where the candidate gives $0, are on refused returns; the project-unknown records withhold s1a.tips, which the source needs (p. 101); the candidate-unknown record withholds sc.tips_ot on a refused return. No difference is on a completed return; the round-2 defect of this family (no screen) is not in this reply. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 1,523 of 1,707 comparisons agree; differences: 177 project-unknown, 3 candidate-refuses, 3 project-refuses, 1 candidate-unknown; by full-interview outcome of the return: incomplete: 109 project-unknown; refused: 68 project-unknown, 3 candidate-refuses, 3 project-refuses, 1 candidate-unknown; witnesses (project / candidate): candidate-refuses e.g. stage14.refuse.sch1a_tips ($0.00 / refusal at s1a.h_sc_1a; return refused), stage14.refuse.sch1a_tips_business_only ($0.00 / refusal at s1a.h_sc_1a; return refused); project-refuses e.g. classm.f8889.5.deepseek (refusal at scope.schedule1 / $0.00; return refused), classm.f8889.5 (refusal at scope.schedule1 / $0.00; return refused); candidate-unknown e.g. stage16.cleanup.f8959_line16_se_refused ($0.00 / unknown person[taxpayer].sc[b].tips_ot; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.tips / $0.00; return incomplete), classm.f4952.1 (unknown s1a.tips / $0.00; return refused).

### 6 — Add lines 4c and 5
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}
```

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." Inherited from line 4c: the candidate's line 6 reads its line 4c, which reads the $tipjob roster with no s1a.tips or Part II gate, so it is unknown on completed returns where the source needs no answer (e.g. classm.f2441.1.deepseek, s1a.tips false). Its other differences are line 5's refusal at s1a.h_sc_1a on returns the project refuses at s1.sc_1a, the project's scope.schedule1 refusal (stage12.refuse.tips_trade_or_business), and married filing separately values on returns refused at s3.mfs. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 402 of 1,707 comparisons agree; differences: 1291 candidate-unknown, 9 candidate-refuses, 3 value, 1 project-refuses, 1 project-unknown; by full-interview outcome of the return: completed: 425 candidate-unknown; incomplete: 208 candidate-unknown; refused: 658 candidate-unknown, 9 candidate-refuses, 3 value, 1 project-refuses, 1 project-unknown; witnesses (project / candidate): value e.g. stage12.mfs.bar ($0.00 / $8,000.00; return refused), generated 258 ($0.00 / $22,803.80; return refused); candidate-refuses e.g. classm.carloan.4 ($0.00 / refusal at person[taxpayer].tipjob[tip_1].mixed; return refused), stage14.refuse.sch1a_tips ($0.00 / refusal at s1a.h_sc_1a; return refused); project-refuses e.g. stage12.refuse.tips_trade_or_business (refusal at scope.schedule1 / $8,000.00; return refused); candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $tipjob@person[taxpayer]; return completed), classm.f2441.3.deepseek ($0.00 / unknown $tipjob@person[taxpayer]; return completed); project-unknown e.g. classm.carloan.1 without s1a.tips (unknown s1a.tips / $22,539.00; return refused).

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}
```

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." Inherited from line 4c: the candidate's line 7 reads its line 4c, which reads the $tipjob roster with no s1a.tips or Part II gate, so it is unknown on completed returns where the source needs no answer (e.g. classm.f2441.1.deepseek, s1a.tips false). Its other differences are line 5's refusal at s1a.h_sc_1a on returns the project refuses at s1.sc_1a, the project's scope.schedule1 refusal (stage12.refuse.tips_trade_or_business), and married filing separately values on returns refused at s3.mfs. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 402 of 1,707 comparisons agree; differences: 1291 candidate-unknown, 9 candidate-refuses, 3 value, 1 project-refuses, 1 project-unknown; by full-interview outcome of the return: completed: 425 candidate-unknown; incomplete: 208 candidate-unknown; refused: 658 candidate-unknown, 9 candidate-refuses, 3 value, 1 project-refuses, 1 project-unknown; witnesses (project / candidate): value e.g. stage12.mfs.bar ($0.00 / $8,000.00; return refused), generated 258 ($0.00 / $22,803.80; return refused); candidate-refuses e.g. classm.carloan.4 ($0.00 / refusal at person[taxpayer].tipjob[tip_1].mixed; return refused), stage14.refuse.sch1a_tips ($0.00 / refusal at s1a.h_sc_1a; return refused); project-refuses e.g. stage12.refuse.tips_trade_or_business (refusal at scope.schedule1 / $8,000.00; return refused); candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $tipjob@person[taxpayer]; return completed), classm.f2441.3.deepseek ($0.00 / unknown $tipjob@person[taxpayer]; return completed); project-unknown e.g. classm.carloan.1 without s1a.tips (unknown s1a.tips / $22,539.00; return refused).

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

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." The candidate's line 8 copies line 3 with no test of whether Part II is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek, s1a.tips false: project $0.00, candidate $50,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part2 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 88 of 1,707 comparisons agree; differences: 1094 value, 394 candidate-refuses, 129 project-unknown, 2 candidate-unknown; by full-interview outcome of the return: completed: 509 value; incomplete: 210 value, 93 project-unknown; refused: 394 candidate-refuses, 375 value, 36 project-unknown, 2 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $50,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $85,000.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused), ss.mfs ($0.00 / unknown sb.unsupported; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.tips / $498,523.00; return incomplete), classm.f4952.1 (unknown s1a.tips / $388,706.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

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

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." The candidate's line 9 enters $150,000 or $300,000 with no test of whether Part II is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate $150,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part2 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 41 of 1,707 comparisons agree; differences: 1472 value, 194 project-unknown; by full-interview outcome of the return: completed: 510 value; incomplete: 217 value, 120 project-unknown; refused: 745 value, 74 project-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $150,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $300,000.00; return completed); project-unknown e.g. classm.f8889.3.deepseek (unknown s1a.tips / $150,000.00; return incomplete), classm.f4952.2 (unknown s1a.tips / $150,000.00; return incomplete). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete.

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

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." The candidate's line 10 subtracts line 9 from line 8 with no test of whether Part II is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate -$100,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part2 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 78 of 1,707 comparisons agree; differences: 1104 value, 394 candidate-refuses, 129 project-unknown, 2 candidate-unknown; by full-interview outcome of the return: completed: 508 value; incomplete: 217 value, 93 project-unknown; refused: 394 candidate-refuses, 379 value, 36 project-unknown, 2 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $-100,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $-215,000.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused), ss.mfs ($0.00 / unknown sb.unsupported; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.tips / $348,523.00; return incomplete), classm.f4952.1 (unknown s1a.tips / $238,706.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

### 12 — Multiply line 11 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "8"}, "op": "subtract_floor0", "take": {"line": "9"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"from": {"line": "10"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Second transcription's note: When line 10 is zero or less, the IRS skips lines 11 and 12. This line is then zero, so line 13 equals line 7, as the instructions require.

Ruling: model error; i1040gi p. 101, Part II caution: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025. • You have a valid social security number (SSN)." The candidate's line 12 figures the $100-per-$1,000 reduction with no test of whether Part II is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f5695.7: project $0.00, candidate $9,400.00, on returns with modified AGI above the base and no qualified tips). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part2 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 921 of 1,707 comparisons agree; differences: 394 candidate-refuses, 261 value, 129 project-unknown, 2 candidate-unknown; by full-interview outcome of the return: completed: 61 value; incomplete: 93 project-unknown, 62 value; refused: 394 candidate-refuses, 138 value, 36 project-unknown, 2 candidate-unknown; witnesses (project / candidate): value e.g. classm.f5695.7 ($0.00 / $9,400.00; return completed), classm.f8995.2 ($0.00 / $1,800.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused), ss.mfs ($0.00 / unknown sb.unsupported; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.tips / $34,800.00; return incomplete), classm.f4952.1 (unknown s1a.tips / $23,800.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "8"}, {"line": "9"}], "test": "le"}, "then": {"line": "7"}}, {"guard": {"args": [{"line": "9"}, {"line": "8"}], "test": "lt"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The rule 'If married, you must file jointly to claim this deduction' is applied as zero for married filing separately. The valid-SSN rule is applied by counting only persons with an SSN valid for employment.

Ruling: model error; i1040gi p. 104, Line 5: "Include the qualified tips you and/or your spouse received in the course of a trade or business, but only to the extent the trade or business in which you received the qualified tips has net income." and p. 101: "Fill out Schedule 1-A, Part II, only if: • You (and/or your spouse if filing a joint return) received qualified tips in 2025." The candidate's line 13 is the Part II computation gated on s1a.tips and filing status, with no refusal for qualified tips received in a trade or business; its line 5 refusal (s1a.h_sc_1a) is reached only when s1a.tips, the employee-tips question, is true. On stage14.refuse.sch1a_tips_business_only and stage14.refuse.sch1a_tips (s1a.tips false, sc[b].tips_ot true: qualified tips received in the business or Form 1099 overtime) the candidate completes line 13 at $0.00, so business tips the source includes on line 5 and deducts on line 13 are dropped without a refusal; the project refuses at s1.sc_1a (BUG-0147). On stage14.sch1a.refuse_overtime_1099 (overtime only) the candidate's $0 is right for line 13 itself and the project's refusal of the return is its cited screen (scope). BUG-0154 checked: the refusal reported for Form 1040 line 37 on these returns is the one shared text, also when employee tips are claimed with the screen answered yes (evaluated on a variant of stage14.refuse.sch1a_tips_business_only with s1a.tips true and one $5,000 tip job). The candidate's refusals (generated 119, 203, 213) are upstream gates its line 3 chain reaches, on returns the project refuses; the project-unknown records withhold s1a.tips or sc.tips_ot. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 1,678 of 1,707 comparisons agree; differences: 23 project-unknown, 3 candidate-refuses, 3 project-refuses; by full-interview outcome of the return: refused: 23 project-unknown, 3 candidate-refuses, 3 project-refuses; witnesses (project / candidate): candidate-refuses e.g. generated 119 ($0.00 / refusal at person[taxpayer].f8889[hsa].unsupported; return refused), generated 203 ($0.00 / refusal at person[taxpayer].se_screened; return refused); project-refuses e.g. stage14.refuse.sch1a_tips (refusal at s1.sc_1a / $0.00; return refused), stage14.refuse.sch1a_tips_business_only (refusal at s1.sc_1a / $0.00; return refused); project-unknown e.g. classm.f4952.3 (unknown s1a.tips / $0.00; return refused), classm.g28.2 (unknown s1a.tips / $0.00; return refused).

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"collection": "person", "field": "person.ot_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"collection": "person", "field": "person.ot_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}
```

Second transcription's note: Assumes person.ot_total is the person's Qualified Overtime Compensation From More Than One Employer Worksheet total (column (b), otjob.col_b). The spouses' totals are added (worksheet line 2). Only persons with an SSN valid for employment are counted.

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." The candidate's line 14a reads the worksheet roster $otjob (person.ot_total) on every return with no s1a.overtime or Part gate, although s1a.overtime is in its interface and it tests it on its deduction line. A filer who answers s1a.overtime no is never asked for that roster, so the candidate's line 14a is unknown on completed returns where the source needs no answer, because the Part is not filled out at all: an answer required that the source does not need to determine the result. The value differences are married filing separately returns (stage12.mfs.bar $0.00 / $6,000.00; generated 96, 258, 386: s1a.overtime true, status mfs), on which the candidate omits "If you are married, you must file a joint return with your spouse to claim this deduction" (p. 106) on this line; all are refused at s3.mfs. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 406 of 1,707 comparisons agree; differences: 1294 candidate-unknown, 4 value, 2 project-unknown, 1 candidate-refuses; by full-interview outcome of the return: completed: 424 candidate-unknown; incomplete: 208 candidate-unknown; refused: 662 candidate-unknown, 4 value, 2 project-unknown, 1 candidate-refuses; witnesses (project / candidate): value e.g. stage12.mfs.bar ($0.00 / $6,000.00; return refused), generated 96 ($0.00 / $32,267.31; return refused); candidate-refuses e.g. generated 302 ($0.00 / refusal at person[taxpayer].otjob[ot_1].refused; return refused); candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $otjob@person[taxpayer]; return completed), classm.f2441.3.deepseek ($0.00 / unknown $otjob@person[taxpayer]; return completed); project-unknown e.g. classm.carloan.1 without s1a.overtime (unknown s1a.overtime / $0.00; return refused), classm.otjob.1 without s1a.overtime (unknown s1a.overtime / $11,471.00; return refused).

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

Second transcription's note: Overtime reported on Form 1099-NEC or 1099-MISC is screened with Schedule C (sc.tips_ot) and not computed. The tool refuses when it is claimed.

Ruling: scope; i1040gi p. 108, Line 14b: "Enter on Line 14b only the qualified overtime compensation amount that is included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3." and p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." The candidate gives $0 and refuses at s1a.h_sc_1a (the sc.tips_ot screen) on every return; it refuses stage14.refuse.sch1a_tips and stage14.refuse.sch1a_tips_business_only where the project's line 14b is $0 (Part III gate false), and the project refuses both returns at s1.sc_1a on lines 13 and 21. The project's refusals at its cited screen scope.schedule1 (stage12.refuse.overtime_nonemployee, generated 102), where the candidate gives $0, are on refused returns; the project-unknown records withhold s1a.overtime, which the source needs (p. 106). No difference is on a completed return. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 1,525 of 1,707 comparisons agree; differences: 177 project-unknown, 2 candidate-refuses, 2 project-refuses, 1 candidate-unknown; by full-interview outcome of the return: incomplete: 109 project-unknown; refused: 68 project-unknown, 2 candidate-refuses, 2 project-refuses, 1 candidate-unknown; witnesses (project / candidate): candidate-refuses e.g. stage14.refuse.sch1a_tips ($0.00 / refusal at s1a.h_sc_1a; return refused), stage14.refuse.sch1a_tips_business_only ($0.00 / refusal at s1a.h_sc_1a; return refused); project-refuses e.g. stage12.refuse.overtime_nonemployee (refusal at scope.schedule1 / $0.00; return refused), generated 102 (refusal at scope.schedule1 / $0.00; return refused); candidate-unknown e.g. stage16.cleanup.f8959_line16_se_refused ($0.00 / unknown person[taxpayer].sc[b].tips_ot; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.overtime / $0.00; return incomplete), classm.f4952.1 (unknown s1a.overtime / $0.00; return refused).

### 14c — Add lines 14a and 14b
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}
```

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." Inherited from line 14a: the candidate's line 14c reads line 14a, which reads the $otjob roster with no s1a.overtime or Part III gate, so it is unknown on completed returns where the source needs no answer (e.g. classm.f2441.1.deepseek, s1a.overtime false). Its other differences are line 14b's refusal at s1a.h_sc_1a on returns the project refuses at s1.sc_1a, the project's scope.schedule1 refusal (stage12.refuse.overtime_nonemployee), and married filing separately values on returns refused at s3.mfs. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 405 of 1,707 comparisons agree; differences: 1292 candidate-unknown, 4 value, 3 candidate-refuses, 2 project-unknown, 1 project-refuses; by full-interview outcome of the return: completed: 424 candidate-unknown; incomplete: 208 candidate-unknown; refused: 660 candidate-unknown, 4 value, 3 candidate-refuses, 2 project-unknown, 1 project-refuses; witnesses (project / candidate): value e.g. stage12.mfs.bar ($0.00 / $6,000.00; return refused), generated 96 ($0.00 / $32,267.31; return refused); candidate-refuses e.g. stage14.refuse.sch1a_tips ($0.00 / refusal at s1a.h_sc_1a; return refused), stage14.refuse.sch1a_tips_business_only ($0.00 / refusal at s1a.h_sc_1a; return refused); project-refuses e.g. stage12.refuse.overtime_nonemployee (refusal at scope.schedule1 / $3,000.00; return refused); candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $otjob@person[taxpayer]; return completed), classm.f2441.3.deepseek ($0.00 / unknown $otjob@person[taxpayer]; return completed); project-unknown e.g. classm.carloan.1 without s1a.overtime (unknown s1a.overtime / $0.00; return refused), classm.otjob.1 without s1a.overtime (unknown s1a.overtime / $11,471.00; return refused).

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.ot_max_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.ot_max_other"}}], "op": "choose"}], "op": "smaller_of"}
```

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." Inherited from line 14a: the candidate's line 15 reads line 14a, which reads the $otjob roster with no s1a.overtime or Part III gate, so it is unknown on completed returns where the source needs no answer (e.g. classm.f2441.1.deepseek, s1a.overtime false). Its other differences are line 14b's refusal at s1a.h_sc_1a on returns the project refuses at s1.sc_1a, the project's scope.schedule1 refusal (stage12.refuse.overtime_nonemployee), and married filing separately values on returns refused at s3.mfs. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 405 of 1,707 comparisons agree; differences: 1292 candidate-unknown, 4 value, 3 candidate-refuses, 2 project-unknown, 1 project-refuses; by full-interview outcome of the return: completed: 424 candidate-unknown; incomplete: 208 candidate-unknown; refused: 660 candidate-unknown, 4 value, 3 candidate-refuses, 2 project-unknown, 1 project-refuses; witnesses (project / candidate): value e.g. stage12.mfs.bar ($0.00 / $6,000.00; return refused), generated 96 ($0.00 / $12,500.00; return refused); candidate-refuses e.g. stage14.refuse.sch1a_tips ($0.00 / refusal at s1a.h_sc_1a; return refused), stage14.refuse.sch1a_tips_business_only ($0.00 / refusal at s1a.h_sc_1a; return refused); project-refuses e.g. stage12.refuse.overtime_nonemployee (refusal at scope.schedule1 / $3,000.00; return refused); candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $otjob@person[taxpayer]; return completed), classm.f2441.3.deepseek ($0.00 / unknown $otjob@person[taxpayer]; return completed); project-unknown e.g. classm.carloan.1 without s1a.overtime (unknown s1a.overtime / $0.00; return refused), classm.otjob.1 without s1a.overtime (unknown s1a.overtime / $11,471.00; return refused).

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

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." The candidate's line 16 copies line 3 with no test of whether Part III is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek, s1a.overtime false: project $0.00, candidate $50,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part3 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 94 of 1,707 comparisons agree; differences: 1091 value, 391 candidate-refuses, 129 project-unknown, 2 candidate-unknown; by full-interview outcome of the return: completed: 509 value; incomplete: 210 value, 93 project-unknown; refused: 391 candidate-refuses, 372 value, 36 project-unknown, 2 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $50,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $85,000.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused), ss.mfs ($0.00 / unknown sb.unsupported; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.overtime / $498,523.00; return incomplete), classm.f4952.1 (unknown s1a.overtime / $388,706.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

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

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." The candidate's line 17 enters $150,000 or $300,000 with no test of whether Part III is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate $150,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part3 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 47 of 1,707 comparisons agree; differences: 1466 value, 194 project-unknown; by full-interview outcome of the return: completed: 510 value; incomplete: 217 value, 120 project-unknown; refused: 739 value, 74 project-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $150,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $300,000.00; return completed); project-unknown e.g. classm.f8889.3.deepseek (unknown s1a.overtime / $150,000.00; return incomplete), classm.f4952.2 (unknown s1a.overtime / $150,000.00; return incomplete). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete.

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

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." The candidate's line 18 subtracts line 17 from line 16 with no test of whether Part III is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate -$100,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part3 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 84 of 1,707 comparisons agree; differences: 1101 value, 391 candidate-refuses, 129 project-unknown, 2 candidate-unknown; by full-interview outcome of the return: completed: 508 value; incomplete: 217 value, 93 project-unknown; refused: 391 candidate-refuses, 376 value, 36 project-unknown, 2 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $-100,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $-215,000.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused), ss.mfs ($0.00 / unknown sb.unsupported; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.overtime / $348,523.00; return incomplete), classm.f4952.1 (unknown s1a.overtime / $238,706.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

### 20 — Multiply line 19 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "16"}, "op": "subtract_floor0", "take": {"line": "17"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"from": {"line": "18"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Ruling: model error; i1040gi p. 106, Part III caution: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025; and • You have a valid social security number (SSN)." The candidate's line 20 figures the $100-per-$1,000 reduction with no test of whether Part III is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f5695.7: project $0.00, candidate $9,400.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part3 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 922 of 1,707 comparisons agree; differences: 391 candidate-refuses, 263 value, 129 project-unknown, 2 candidate-unknown; by full-interview outcome of the return: completed: 63 value; incomplete: 93 project-unknown, 62 value; refused: 391 candidate-refuses, 138 value, 36 project-unknown, 2 candidate-unknown; witnesses (project / candidate): value e.g. classm.f5695.7 ($0.00 / $9,400.00; return completed), classm.f8995.2 ($0.00 / $1,800.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused), ss.mfs ($0.00 / unknown sb.unsupported; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.overtime / $34,800.00; return incomplete), classm.f4952.1 (unknown s1a.overtime / $23,800.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "16"}, {"line": "17"}], "test": "le"}, "then": {"line": "15"}}, {"guard": {"args": [{"line": "17"}, {"line": "16"}], "test": "lt"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The rule 'If married, you must file jointly to claim this deduction' is applied as zero for married filing separately.

Ruling: model error; i1040gi p. 108, Line 14b: "Enter on Line 14b only the qualified overtime compensation amount that is included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3." and p. 106: "Fill out Schedule 1-A, Part III, only if: • You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025". The candidate's line 21 is gated on s1a.overtime, the employee-overtime question, and its line 14b refusal (s1a.h_sc_1a) is reached only when that answer is true. The per-business screen sc.tips_ot is one yes for qualified tips in the business or qualified overtime on Form 1099-NEC or 1099-MISC; on stage14.refuse.sch1a_tips_business_only and stage14.refuse.sch1a_tips (s1a.overtime false, sc[b].tips_ot true) the candidate completes line 21 at $0.00, so a filer whose yes is Form 1099 overtime loses the line 14b amount without a refusal, where the project refuses at s1.sc_1a. Where s1a.overtime is true (stage14.sch1a.refuse_overtime_1099) both refuse. The candidate's refusals are upstream gates (sb.fbar_required, se_screened, scope.other_income, sd.carryover) on returns the project refuses; the project-unknown records withhold s1a.overtime or sc.tips_ot. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 1,677 of 1,707 comparisons agree; differences: 23 project-unknown, 5 candidate-refuses, 2 project-refuses; by full-interview outcome of the return: refused: 23 project-unknown, 5 candidate-refuses, 2 project-refuses; witnesses (project / candidate): candidate-refuses e.g. generated 21 ($0.00 / refusal at sb.fbar_required; return refused), generated 203 ($0.00 / refusal at person[taxpayer].se_screened; return refused); project-refuses e.g. stage14.refuse.sch1a_tips (refusal at s1.sc_1a / $0.00; return refused), stage14.refuse.sch1a_tips_business_only (refusal at s1.sc_1a / $0.00; return refused); project-unknown e.g. classm.f4952.3 (unknown s1a.overtime / $0.00; return refused), classm.g28.2 (unknown s1a.overtime / $0.00; return refused).

### 23 — Add lines 22a and 22b, column (iii)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"collection": "carloan", "field": "carloan.col_iii", "op": "sum_over", "where": null}}], "op": "choose"}
```

Second:

```json
{"collection": "carloan", "field": "carloan.col_iii", "op": "sum_over", "where": null}
```

Second transcription's note: All loans entered are added, including any beyond two VINs that are reported on an attached statement as the instructions direct.

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." The candidate's line 23 reads the worksheet roster $carloan (carloan.col_iii) on every return with no s1a.carloan or Part gate, although s1a.carloan is in its interface and it tests it on its deduction line. A filer who answers s1a.carloan no is never asked for that roster, so the candidate's line 23 is unknown on completed returns where the source needs no answer, because the Part is not filled out at all: an answer required that the source does not need to determine the result. Its line 30 is gated on s1a.carloan, which is why line 30 agrees. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 261 of 1,707 comparisons agree; differences: 1443 candidate-unknown, 3 project-unknown; by full-interview outcome of the return: completed: 510 candidate-unknown; incomplete: 214 candidate-unknown; refused: 719 candidate-unknown, 3 project-unknown; witnesses (project / candidate): candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $carloan; return completed), classm.f2441.2.deepseek ($0.00 / unknown $carloan; return completed); project-unknown e.g. classm.carloan.1 without s1a.carloan (unknown s1a.carloan / $318.00; return refused), classm.dcprov.1 without s1a.carloan (unknown s1a.carloan / $0.00; return refused).

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"of": [{"line": "23"}, {"param": "s1a.car_max"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "23"}, {"param": "s1a.car_max"}], "op": "smaller_of"}
```

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." Inherited from line 23: the candidate's line 24 reads line 23, which reads the $carloan roster with no s1a.carloan gate, so it is unknown on completed returns where the source needs no answer (e.g. classm.f2441.1.deepseek, s1a.carloan false). Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 261 of 1,707 comparisons agree; differences: 1443 candidate-unknown, 3 project-unknown; by full-interview outcome of the return: completed: 510 candidate-unknown; incomplete: 214 candidate-unknown; refused: 719 candidate-unknown, 3 project-unknown; witnesses (project / candidate): candidate-unknown e.g. classm.f2441.1.deepseek ($0.00 / unknown $carloan; return completed), classm.f2441.2.deepseek ($0.00 / unknown $carloan; return completed); project-unknown e.g. classm.carloan.1 without s1a.carloan (unknown s1a.carloan / $318.00; return refused), classm.dcprov.1 without s1a.carloan (unknown s1a.carloan / $0.00; return refused).

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

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." The candidate's line 25 copies line 3 with no test of whether Part IV is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek, s1a.carloan false: project $0.00, candidate $50,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part4 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 92 of 1,707 comparisons agree; differences: 1071 value, 391 candidate-refuses, 152 project-unknown, 1 candidate-unknown; by full-interview outcome of the return: completed: 509 value; incomplete: 207 value, 96 project-unknown; refused: 391 candidate-refuses, 355 value, 56 project-unknown, 1 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $50,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $85,000.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.carloan / $498,523.00; return incomplete), classm.f4952.1 (unknown s1a.carloan / $388,706.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

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

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." The candidate's line 26 enters $100,000 or $200,000 with no test of whether Part IV is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate $100,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part4 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 44 of 1,707 comparisons agree; differences: 1443 value, 220 project-unknown; by full-interview outcome of the return: completed: 510 value; incomplete: 214 value, 123 project-unknown; refused: 719 value, 97 project-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $100,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $200,000.00; return completed); project-unknown e.g. classm.f8889.3.deepseek (unknown s1a.carloan / $100,000.00; return incomplete), classm.f4952.2 (unknown s1a.carloan / $100,000.00; return incomplete). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete.

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

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." The candidate's line 27 subtracts line 26 from line 25 with no test of whether Part IV is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate -$50,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part4 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 129 of 1,707 comparisons agree; differences: 1034 value, 391 candidate-refuses, 152 project-unknown, 1 candidate-unknown; by full-interview outcome of the return: completed: 508 value; incomplete: 183 value, 96 project-unknown; refused: 391 candidate-refuses, 343 value, 56 project-unknown, 1 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $-50,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $-115,000.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.carloan / $398,523.00; return incomplete), classm.f4952.1 (unknown s1a.carloan / $288,706.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

### 29 — Multiply line 28 by $200
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"amount": {"of": {"from": {"line": "25"}, "op": "subtract_floor0", "take": {"line": "26"}}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"from": {"line": "27"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}
```

Ruling: model error; i1040gi p. 109, Part IV: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025." The candidate's line 29 figures the $200-per-$1,000 reduction with no test of whether Part IV is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f8889.1.deepseek: project $0.00, candidate $4,800.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part4 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 809 of 1,707 comparisons agree; differences: 391 candidate-refuses, 354 value, 152 project-unknown, 1 candidate-unknown; by full-interview outcome of the return: completed: 107 value; incomplete: 96 project-unknown, 77 value; refused: 391 candidate-refuses, 170 value, 56 project-unknown, 1 candidate-unknown; witnesses (project / candidate): value e.g. classm.f8889.1.deepseek ($0.00 / $4,800.00; return completed), classm.f5695.2 ($0.00 / $12,600.00; return completed); candidate-refuses e.g. classm.w2.1.deepseek ($0.00 / refusal at f2441.line14_bad; return refused), classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused); candidate-unknown e.g. stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused); project-unknown e.g. classm.f4952.2 (unknown s1a.carloan / $79,800.00; return incomplete), classm.f4952.1 (unknown s1a.carloan / $57,800.00; return refused). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete. The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "25"}, {"line": "26"}], "test": "le"}, "then": {"line": "24"}}, {"guard": {"args": [{"line": "26"}, {"line": "25"}], "test": "lt"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}], "op": "choose"}
```

Second transcription's note: The supplied text states no married-filing-jointly or SSN requirement for Part IV, so none is applied. The only gate is the s1a.carloan question.

Ruling: representation; i1040gi p. 110, Line 27: "If the amount on line 27 is zero or less, the amount of your QPVLI reported on line 24 is not reduced. Skip lines 28 and 29 and enter the amount from Schedule 1-A, line 24, on Schedule 1-A, line 30." The candidate's line 30 is gated on s1a.carloan and subtracts a zero-floored, rounded-up line 29, which equals the project's line 27 skip. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 1,707 of 1,707 comparisons agree; no differences. Observed equivalence on that sample, not proof.

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

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." The candidate's line 31 copies line 3 with no test of whether Part V is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek, filer not born before January 2, 1961: project $0.00, candidate $50,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 115 of 1,707 comparisons agree; differences: 1198 value, 391 candidate-refuses, 3 candidate-unknown; by full-interview outcome of the return: completed: 499 value; incomplete: 298 value; refused: 401 value, 391 candidate-refuses, 3 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $50,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $85,000.00; return completed); candidate-refuses e.g. classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused), classm.f8889.5.deepseek ($0.00 / refusal at sd.carryover; return refused); candidate-unknown e.g. stage16.cleanup.refuse.rrta_medicare ($0.00 / unknown f2441.benefits; return refused), stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused). The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

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

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." The candidate's line 32 enters $75,000 or $150,000 with no test of whether Part V is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate $75,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 69 of 1,707 comparisons agree; differences: 1603 value, 35 project-unknown; by full-interview outcome of the return: completed: 500 value; incomplete: 305 value, 27 project-unknown; refused: 798 value, 8 project-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $75,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $150,000.00; return completed); project-unknown e.g. classm.f8889.3.deepseek (unknown person[sample].age65 / $75,000.00; return incomplete), classm.f8889.3 (unknown person[sample].age65 / $75,000.00; return incomplete). The project-unknown records withhold the Part screen the source needs to decide whether the Part is filled out, on returns the full interview refuses or leaves incomplete.

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

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." The candidate's line 33 subtracts line 32 from line 31 with no test of whether Part V is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate -$25,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 106 of 1,707 comparisons agree; differences: 1207 value, 391 candidate-refuses, 3 candidate-unknown; by full-interview outcome of the return: completed: 497 value; incomplete: 305 value; refused: 405 value, 391 candidate-refuses, 3 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $-25,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $-65,000.00; return completed); candidate-refuses e.g. classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused), classm.f8889.5.deepseek ($0.00 / refusal at sd.carryover; return refused); candidate-unknown e.g. stage16.cleanup.refuse.rrta_medicare ($0.00 / unknown f2441.benefits; return refused), stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused). The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

### 34 — Multiply line 33 by 6% (0.06)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"line": "32"}}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}
```

Second transcription's note: When line 33 is zero or less, this is zero, so line 35 is $6,000, as the form directs.

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." The candidate's line 34 figures 6% of line 33 with no test of whether Part V is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f8889.1.deepseek: project $0.00, candidate $4,435.68). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 775 of 1,707 comparisons agree; differences: 538 value, 391 candidate-refuses, 3 candidate-unknown; by full-interview outcome of the return: completed: 159 value; incomplete: 129 value; refused: 391 candidate-refuses, 250 value, 3 candidate-unknown; witnesses (project / candidate): value e.g. classm.f8889.1.deepseek ($0.00 / $4,435.68; return completed), classm.f5695.2 ($0.00 / $6,772.50; return completed); candidate-refuses e.g. classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused), classm.f8889.5.deepseek ($0.00 / refusal at sd.carryover; return refused); candidate-unknown e.g. stage16.cleanup.refuse.rrta_medicare ($0.00 / unknown f2441.benefits; return refused), stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused). The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

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

Ruling: model error; i1040gi p. 110, Part V caution: "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse if filing a joint return) were born before January 2, 1961. • You have a valid social security number (SSN)." The candidate's line 35 subtracts line 34 from $6,000 with no test of whether Part V is filled out, so it shows a nonzero amount on completed returns where the Part is not filled out (e.g. classm.f2441.1.deepseek: project $0.00, candidate $6,000.00). Under the adjudication README skip rule a line of a Part the instructions say not to fill out must not show an amount on a reachable return; the project enters zero there through its Part gate (s1a.part5 false), which changes no deduction but makes the candidate's shown amount a defect. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 371 of 1,707 comparisons agree; differences: 942 value, 391 candidate-refuses, 3 candidate-unknown; by full-interview outcome of the return: completed: 443 value; incomplete: 234 value; refused: 391 candidate-refuses, 265 value, 3 candidate-unknown; witnesses (project / candidate): value e.g. classm.f2441.1.deepseek ($0.00 / $6,000.00; return completed), classm.f2441.2.deepseek ($0.00 / $6,000.00; return completed); candidate-refuses e.g. classm.f8889.4.deepseek ($0.00 / refusal at sd.other_forms; return refused), classm.f8889.5.deepseek ($0.00 / refusal at sd.carryover; return refused); candidate-unknown e.g. stage16.cleanup.refuse.rrta_medicare ($0.00 / unknown f2441.benefits; return refused), stage16.cleanup.refuse.f2441_line24 ($0.00 / unknown person[spouse].sav_trad; return refused). The candidate refusals and unknowns are upstream gates or answers its ungated chain reaches through line 3, all on refused returns.

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"line": "35"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "35"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Applies the instructions' rules that a person who died in 2025 before reaching 65 doesn't qualify, and 'If married, you must file jointly' (zero for married filing separately).

Ruling: scope; i1040gi p. 110, Death of a taxpayer in 2025: "If a taxpayer was born before January 2, 1961, but died in 2025 before reaching age 65, then the taxpayer doesn’t qualify for the enhanced deduction for seniors." The candidate gives $0 for a taxpayer born before January 2, 1961, who died in 2025 before 65, which the text supports; the project refuses that return at its cited gate s1a.senior_decedent (stage12.refuse.senior_decedent, i1040gi p. 110). The project-unknown record withholds person.age65 on a married filing separately return refused at s3.mfs. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 1,705 of 1,707 comparisons agree; differences: 1 project-refuses, 1 project-unknown; by full-interview outcome of the return: refused: 1 project-refuses, 1 project-unknown; witnesses (project / candidate): project-refuses e.g. stage12.refuse.senior_decedent (refusal at s1a.senior_decedent / $0.00; return refused); project-unknown e.g. ss.mfs (unknown person[taxpayer].age65 / $0.00; return refused).

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"line": "35"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}], "test": "all"}, "then": {"line": "35"}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: scope; i1040gi p. 110, Death of a taxpayer in 2025: "If a taxpayer was born before January 2, 1961, but died in 2025 before reaching age 65, then the taxpayer doesn’t qualify for the enhanced deduction for seniors." As line 36a for the spouse: the candidate gives $0 and the project refuses at its cited gate s1a.spouse_senior_decedent (stage13.refuse.senior_spouse_decedent, generated 491). The project-unknown record lacks a roster role on an incomplete return. Triage executable-triage-v2 (triage/s1a.json; 1,099 fixtures, 500 generated returns seed 20261026, 108 partial records): 1,704 of 1,707 comparisons agree; differences: 2 project-refuses, 1 project-unknown; by full-interview outcome of the return: incomplete: 1 project-unknown; refused: 2 project-refuses; witnesses (project / candidate): project-refuses e.g. stage13.refuse.senior_spouse_decedent (refusal at s1a.spouse_senior_decedent / $0.00; return refused), generated 491 (refusal at s1a.spouse_senior_decedent / $0.00; return refused); project-unknown e.g. ss.person.separation (unknown person[second].role / $0.00; return incomplete).

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 2a | sa.excluded_income | - |
| 2b | sa.excluded_income | sa.excluded_income |
| 2c | sa.excluded_income | sa.excluded_income |
| 2d | sa.excluded_income | sa.excluded_income |
| 2e | sa.excluded_income | - |
| 3 | sa.excluded_income | - |
| 4b | f8959.unsupported | f8959.unsupported |
| 4c | f8959.unsupported | f8959.unsupported |
| 5 | s1a.h_sc_1a | s1a.h_sc_1a |
| 6 | f8959.unsupported, s1a.h_sc_1a | f8959.unsupported, s1a.h_sc_1a |
| 7 | f8959.unsupported, s1a.h_sc_1a | f8959.unsupported, s1a.h_sc_1a |
| 8 | sa.excluded_income | - |
| 10 | sa.excluded_income | - |
| 12 | sa.excluded_income | - |
| 13 | f8959.unsupported, s1a.h_sc_1a, sa.excluded_income | f8959.unsupported, s1a.h_sc_1a |
| 14b | s1a.h_sc_1a | s1a.h_sc_1a |
| 14c | s1a.h_sc_1a | s1a.h_sc_1a |
| 15 | s1a.h_sc_1a | s1a.h_sc_1a |
| 16 | sa.excluded_income | - |
| 18 | sa.excluded_income | - |
| 20 | sa.excluded_income | - |
| 21 | s1a.h_sc_1a, sa.excluded_income | s1a.h_sc_1a |
| 25 | sa.excluded_income | - |
| 27 | sa.excluded_income | - |
| 29 | sa.excluded_income | - |
| 30 | sa.excluded_income | - |
| 31 | sa.excluded_income | - |
| 33 | sa.excluded_income | - |
| 34 | sa.excluded_income | - |
| 35 | sa.excluded_income | - |
| 36a | sa.excluded_income | - |
| 36b | sa.excluded_income | - |
| 37 | sa.excluded_income | - |
| 38 | f8959.unsupported, s1a.h_sc_1a, sa.excluded_income | f8959.unsupported, s1a.h_sc_1a |

## Raw second transcription

```yaml
```yaml
lines:
  - id: s1a.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: s1a.line1
    printed: "1"
    label: "Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}

  - id: s1a.line2a
    printed: "2a"
    label: "Enter any income from Puerto Rico that you excluded"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.excluded_income]
    note: "Excluded Puerto Rico income is outside the tool's scope (screened by sa.excluded_income). Only the case with no such income is encoded, so the line is zero and the tool refuses when the screen is answered yes."

  - id: s1a.line2b
    printed: "2b"
    label: "Enter the amount from Form 2555, line 45"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.excluded_income]
    note: "Form 2555 is outside the tool's scope (screened by sa.excluded_income). Only the case with no Form 2555 is encoded."

  - id: s1a.line2c
    printed: "2c"
    label: "Enter the amount from Form 2555, line 50"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.excluded_income]
    note: "Form 2555 is outside the tool's scope (screened by sa.excluded_income). Only the case with no Form 2555 is encoded."

  - id: s1a.line2d
    printed: "2d"
    label: "Enter the amount from Form 4563, line 15"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.excluded_income]
    note: "Form 4563 is outside the tool's scope (screened by sa.excluded_income). Only the case with no Form 4563 is encoded."

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

  # ---------------- Part II No Tax on Tips ----------------
  - id: s1a.h_tip_employers
    printed: "(helper)"
    label: "Number of employers from which you (and your spouse) with a valid SSN received qualified tips as an employee"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.tip_employers
      where: {op: test, eq: [person.work_ssn, {const: true}]}
    note: "Assumes person.tip_employers counts that person's Qualified Tips From More Than One Employer Worksheet rows. Only persons with an SSN valid for employment are counted, because the spouse who received the tips must have a valid SSN."

  - id: s1a.h_tip_total
    printed: "(helper)"
    label: "Qualified Tips From More Than One Employer Worksheet, line 2 (total of column (d)) for persons with a valid SSN"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.tip_total
      where: {op: test, eq: [person.work_ssn, {const: true}]}
    note: "Assumes person.tip_total is the person's total of worksheet column (d) (tipjob.col_d). The supplied interface does not define it, so this reading was chosen."

  - id: s1a.h_tip_one
    printed: "(helper)"
    label: "Received tips as an employee with respect to employment with only one employer"
    type: Bool
    expr: {op: test, eq: [s1a.h_tip_employers, {const: 1, type: Count}]}

  - id: s1a.line4a
    printed: "4a"
    label: "Enter qualified tips included on Form W-2, box 7 (enter -0- if you received tips as an employee with respect to employment with more than one employer)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.h_tip_one, {const: true}]}
          then: s1a.h_tip_total
        - guard: {op: test, eq: [s1a.h_tip_one, {const: false}]}
          then: s1a.h_zero
    note: "With one employer, the worksheet row's column (d) is the greater of column (b) and column (c). Form 4137 (column (c)) is refused, so column (d) equals the W-2 or Form 4070 amount the filer chose. That amount is used for line 4a. With more than one employer, -0- is entered, as the form says."

  - id: s1a.line4b
    printed: "4b"
    label: "Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [f8959.unsupported]
    note: "Form 4137 (unreported or allocated tips) is outside the tool's scope (screened by f8959.unsupported). Only the case where Form 4137 is not filed is encoded."

  - id: s1a.h_4c_one
    printed: "(helper)"
    label: "Larger of line 4a or line 4b"
    type: NonNegDollars
    expr: {op: larger_of, of: [s1a.line4a, s1a.line4b]}

  - id: s1a.line4c
    printed: "4c"
    label: "If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions (Qualified Tips From More Than One Employer Worksheet, line 2)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.h_tip_one, {const: true}]}
          then: s1a.h_4c_one
        - guard: {op: test, eq: [s1a.h_tip_one, {const: false}]}
          then: s1a.h_tip_total

  - id: s1a.h_sc_1a_count
    printed: "(helper)"
    label: "Number of Schedule C businesses whose income includes qualified tips or qualified overtime reported on Form 1099-NEC or 1099-MISC to be deducted on Schedule 1-A"
    type: Count
    expr: {op: sum_over, collection: person, field: person.sc_1a}
    note: "Assumes person.sc_1a counts that person's Schedule C entries answered yes to sc.tips_ot."

  - id: s1a.h_sc_1a
    printed: "(helper)"
    label: "Any trade or business tips or 1099 overtime claimed for Schedule 1-A"
    type: Bool
    expr: {op: test, gt: [s1a.h_sc_1a_count, {const: 0, type: Count}]}

  - id: s1a.line5
    printed: "5"
    label: "Qualified tips received in the course of a trade or business. Qualified tip amount included in Form 1099-NEC, box 1; Form 1099-MISC, box 3; or Form 1099-K, box 1a. Do not enter more than the net profit from the trade or business"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [s1a.h_sc_1a]
    note: "The tool does not compute qualified tips received in a trade or business, including the net income limitation and the Multiple Trades or Businesses Worksheet. It refuses when any Schedule C reports such tips. The sc.tips_ot screen also covers 1099 overtime, so the refusal reaches that case too."

  - id: s1a.line6
    printed: "6"
    label: "Add lines 4c and 5"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line4c, s1a.line5]}

  - id: s1a.h_tips_max
    printed: "(helper)"
    label: "$25,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.tips_max}

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

  - id: s1a.h_base_joint
    printed: "(helper)"
    label: "$300,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_joint}

  - id: s1a.h_base_other
    printed: "(helper)"
    label: "$150,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_other}

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

  - id: s1a.h_10pos
    printed: "(helper)"
    label: "Line 10 if more than zero, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line10, take: s1a.h_zero}

  - id: s1a.h_10_thousands
    printed: "(helper)"
    label: "Line 10 decreased to the next lower multiple of $1,000 (line 11 times $1,000)"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_10pos, unit: 100000, rule: down}
    note: "Line 11 (divide by $1,000 and decrease to a whole number) is a pure number. It is kept as line 10 rounded down to a $1,000 multiple, and line 12 then multiplies by $100 per $1,000 (1/10)."

  - id: s1a.line12
    printed: "12"
    label: "Multiply line 11 by $100"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_10_thousands, rate: {param: s1a.hundred_per_thousand}}
    note: "When line 10 is zero or less, the IRS skips lines 11 and 12. This line is then zero, so line 13 equals line 7, as the instructions require."

  - id: s1a.h_13_figured
    printed: "(helper)"
    label: "Subtract line 12 from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line7, take: s1a.line12}

  - id: s1a.h_tips_ok
    printed: "(helper)"
    label: "Claiming the qualified tips deduction (received qualified tips as an employee; not married filing separately)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [s1a.tips, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfs"}]}

  - id: s1a.line13
    printed: "13"
    label: "Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.h_tips_ok, {const: true}]}
          then: s1a.h_13_figured
        - guard: {op: test, eq: [s1a.h_tips_ok, {const: false}]}
          then: s1a.h_zero
    note: "The rule 'If married, you must file jointly to claim this deduction' is applied as zero for married filing separately. The valid-SSN rule is applied by counting only persons with an SSN valid for employment."

  # ---------------- Part III No Tax on Overtime ----------------
  - id: s1a.line14a
    printed: "14a"
    label: "Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ot_total
      where: {op: test, eq: [person.work_ssn, {const: true}]}
    note: "Assumes person.ot_total is the person's Qualified Overtime Compensation From More Than One Employer Worksheet total (column (b), otjob.col_b). The spouses' totals are added (worksheet line 2). Only persons with an SSN valid for employment are counted."

  - id: s1a.line14b
    printed: "14b"
    label: "Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [s1a.h_sc_1a]
    note: "Overtime reported on Form 1099-NEC or 1099-MISC is screened with Schedule C (sc.tips_ot) and not computed. The tool refuses when it is claimed."

  - id: s1a.line14c
    printed: "14c"
    label: "Add lines 14a and 14b"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line14a, s1a.line14b]}

  - id: s1a.h_ot_max_joint
    printed: "(helper)"
    label: "$25,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_joint}

  - id: s1a.h_ot_max_other
    printed: "(helper)"
    label: "$12,500"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_other}

  - id: s1a.h_ot_max
    printed: "(helper)"
    label: "$12,500 ($25,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_ot_max_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_ot_max_other

  - id: s1a.line15
    printed: "15"
    label: "Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [s1a.line14c, s1a.h_ot_max]}

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

  - id: s1a.h_18pos
    printed: "(helper)"
    label: "Line 18 if more than zero, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line18, take: s1a.h_zero}

  - id: s1a.h_18_thousands
    printed: "(helper)"
    label: "Line 18 decreased to the next lower multiple of $1,000 (line 19 times $1,000)"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_18pos, unit: 100000, rule: down}

  - id: s1a.line20
    printed: "20"
    label: "Multiply line 19 by $100"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_18_thousands, rate: {param: s1a.hundred_per_thousand}}

  - id: s1a.h_21_figured
    printed: "(helper)"
    label: "Subtract line 20 from line 15. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line15, take: s1a.line20}

  - id: s1a.h_ot_ok
    printed: "(helper)"
    label: "Claiming the qualified overtime compensation deduction (received qualified overtime; not married filing separately)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [s1a.overtime, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfs"}]}

  - id: s1a.line21
    printed: "21"
    label: "Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.h_ot_ok, {const: true}]}
          then: s1a.h_21_figured
        - guard: {op: test, eq: [s1a.h_ot_ok, {const: false}]}
          then: s1a.h_zero
    note: "The rule 'If married, you must file jointly to claim this deduction' is applied as zero for married filing separately."

  # ---------------- Part IV No Tax on Car Loan Interest ----------------
  - id: s1a.line23
    printed: "23"
    label: "Add lines 22a and 22b, column (iii)"
    type: NonNegDollars
    expr: {op: sum_over, collection: carloan, field: carloan.col_iii}
    note: "All loans entered are added, including any beyond two VINs that are reported on an attached statement as the instructions direct."

  - id: s1a.h_car_max
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_max}

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

  - id: s1a.h_car_base_joint
    printed: "(helper)"
    label: "$200,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_joint}

  - id: s1a.h_car_base_other
    printed: "(helper)"
    label: "$100,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_other}

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

  - id: s1a.h_27pos
    printed: "(helper)"
    label: "Line 27 if more than zero, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line27, take: s1a.h_zero}

  - id: s1a.h_27_thousands
    printed: "(helper)"
    label: "Line 27 increased to the next higher multiple of $1,000 (line 28 times $1,000)"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_27pos, unit: 100000, rule: up}
    note: "Line 28 rounds up (for example 0.05 to 1). It is kept as line 27 rounded up to a $1,000 multiple, and line 29 multiplies by $200 per $1,000 (1/5). When line 27 is zero or less, this is zero, so line 30 equals line 24."

  - id: s1a.line29
    printed: "29"
    label: "Multiply line 28 by $200"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_27_thousands, rate: {param: s1a.two_hundred_per_thousand}}

  - id: s1a.h_30_figured
    printed: "(helper)"
    label: "Subtract line 29 from line 24. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line24, take: s1a.line29}

  - id: s1a.line30
    printed: "30"
    label: "Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.carloan, {const: true}]}
          then: s1a.h_30_figured
        - guard: {op: test, eq: [s1a.carloan, {const: false}]}
          then: s1a.h_zero
    note: "The supplied text states no married-filing-jointly or SSN requirement for Part IV, so none is applied. The only gate is the s1a.carloan question."

  # ---------------- Part V Enhanced Deduction for Seniors ----------------
  - id: s1a.line31
    printed: "31"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}

  - id: s1a.h_sen_base_joint
    printed: "(helper)"
    label: "$150,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_joint}

  - id: s1a.h_sen_base_other
    printed: "(helper)"
    label: "$75,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_other}

  - id: s1a.line32
    printed: "32"
    label: "Enter $75,000 ($150,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_sen_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_sen_base_other

  - id: s1a.line33
    printed: "33"
    label: "Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35"
    type: Dollars
    expr: {op: subtract, from: s1a.line31, take: s1a.line32}

  - id: s1a.h_33pos
    printed: "(helper)"
    label: "Line 33 if more than zero, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line33, take: s1a.h_zero}

  - id: s1a.line34
    printed: "34"
    label: "Multiply line 33 by 6% (0.06)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_33pos, rate: {param: s1a.senior_rate}}
    note: "When line 33 is zero or less, this is zero, so line 35 is $6,000, as the form directs."

  - id: s1a.h_senior_amount
    printed: "(helper)"
    label: "$6,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_amount}

  - id: s1a.line35
    printed: "35"
    label: "Subtract line 34 from $6,000. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.h_senior_amount, take: s1a.line34}

  - id: s1a.h_sen_tp_count
    printed: "(helper)"
    label: "Taxpayer with a valid SSN, born before January 2, 1961, who did not die in 2025 before reaching age 65"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.work_ssn, {const: true}]}
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, eq: [person.died_before_65, {const: false}]}

  - id: s1a.h_36a_ok
    printed: "(helper)"
    label: "You qualify for the enhanced deduction for seniors (and are not married filing separately)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [s1a.h_sen_tp_count, {const: 1, type: Count}]}
        - {op: test, ne: [f1040.status, {const: "mfs"}]}

  - id: s1a.line36a
    printed: "36a"
    label: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.h_36a_ok, {const: true}]}
          then: s1a.line35
        - guard: {op: test, eq: [s1a.h_36a_ok, {const: false}]}
          then: s1a.h_zero
    note: "Applies the instructions' rules that a person who died in 2025 before reaching 65 doesn't qualify, and 'If married, you must file jointly' (zero for married filing separately)."

  - id: s1a.h_sen_sp_count
    printed: "(helper)"
    label: "Spouse with a valid SSN, born before January 2, 1961, who did not die in 2025 before reaching age 65"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.work_ssn, {const: true}]}
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, eq: [person.died_before_65, {const: false}]}

  - id: s1a.h_36b_ok
    printed: "(helper)"
    label: "Married filing jointly and your spouse qualifies for the enhanced deduction for seniors"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, ge: [s1a.h_sen_sp_count, {const: 1, type: Count}]}

  - id: s1a.line36b
    printed: "36b"
    label: "If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.h_36b_ok, {const: true}]}
          then: s1a.line35
        - guard: {op: test, eq: [s1a.h_36b_ok, {const: false}]}
          then: s1a.h_zero

  - id: s1a.line37
    printed: "37"
    label: "Enhanced deduction for seniors. Add lines 36a and 36b"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line36a, s1a.line36b]}

  # ---------------- Part VI ----------------
  - id: s1a.line38
    printed: "38"
    label: "Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form 1040-NR, line 13c"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line13, s1a.line21, s1a.line30, s1a.line37]}
```
```
