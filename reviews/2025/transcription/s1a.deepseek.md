# Transcription agreement — s1a

Second transcription of `Schedule 1-A (Form 1040) — Additional Deductions` by an isolated model (spec 6.5), compared line by line with `forms/2025/s1a.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 8c13f0d9ed735f74319d7028043cd8bd6cac173b049cf63314d91115efbef2ef |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 1623116cb1640efb3050727a89613bb1d38171f8dd2ee02ac5ff22192f383dce |
| printed lines compared | 43 |
| agree / disagree / missing | 10 / 33 / 0 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 1}], "test": "le"}, "then": {"collection": "person", "field": "person.tip_reported", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "eq"}, "then": {"collection": "tipjob", "field": "tipjob.amount", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Reads the single tipjob entry when there is exactly one employer; multiple-employer amounts are handled through line 4c.

Ruling: open

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "eq"}, "then": {"collection": "tipjob", "field": "tipjob.col_c", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Reads the single tipjob entry when there is exactly one employer; multiple-employer amounts are handled through line 4c.

Ruling: open

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 1}], "test": "le"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"collection": "tipjob", "field": "tipjob.col_d", "op": "sum_over", "where": null}}], "op": "choose"}
```

Ruling: open

### 5 — Qualified tips received in the course of a trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Second transcription's note: The supplied interface does not provide nonemployee trade-or-business tip amounts; this slice treats line 5 as zero.

Ruling: open

### 6 — Add lines 4c and 5
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}
```

Ruling: open

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}
```

Ruling: open

### 8 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: open

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.base_other"}}], "op": "choose"}
```

Ruling: open

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "8"}, "op": "subtract", "take": {"line": "9"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "8"}, "op": "subtract", "take": {"line": "9"}}
```

Ruling: open

### 12 — Multiply line 11 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "8"}, "op": "subtract_floor0", "take": {"line": "9"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"line": "10"}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Second transcription's note: Line 11 is the floor of line 10 divided by $1,000; the helper computes the same amount as line 12.

Ruling: open

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "8"}, {"line": "9"}], "test": "le"}, "then": {"line": "7"}}, {"guard": {"args": [{"line": "9"}, {"line": "8"}], "test": "lt"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "10"}, {"const": 0}], "test": "le"}, "then": {"line": "7"}}, {"guard": {"args": [{"const": 0}, {"line": "10"}], "test": "lt"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"amount": {"of": {"line": "10"}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}}], "op": "choose"}
```

Ruling: open

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"collection": "person", "field": "person.ot_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"collection": "otjob", "field": "otjob.col_b", "op": "sum_over", "where": null}}], "op": "choose"}
```

Ruling: open

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Second transcription's note: The supplied interface provides no payor-level 1099 overtime amount; this slice treats line 14b as zero.

Ruling: open

### 14c — Add lines 14a and 14b
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}
```

Ruling: open

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.ot_max_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.ot_max_other"}}], "op": "choose"}], "op": "smaller_of"}
```

Ruling: open

### 16 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: open

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.base_other"}}], "op": "choose"}
```

Ruling: open

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "16"}, "op": "subtract", "take": {"line": "17"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "16"}, "op": "subtract", "take": {"line": "17"}}
```

Ruling: open

### 20 — Multiply line 19 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "16"}, "op": "subtract_floor0", "take": {"line": "17"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "18"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "18"}], "test": "lt"}, "then": {"amount": {"of": {"line": "18"}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}], "op": "choose"}
```

Second transcription's note: Line 19 is the floor of line 18 divided by $1,000; the helper computes line 20 directly.

Ruling: open

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "16"}, {"line": "17"}], "test": "le"}, "then": {"line": "15"}}, {"guard": {"args": [{"line": "17"}, {"line": "16"}], "test": "lt"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "18"}, {"const": 0}], "test": "le"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": 0}, {"line": "18"}], "test": "lt"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}], "op": "choose"}
```

Ruling: open

### 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

### 29 — Multiply line 28 by $200
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"amount": {"of": {"from": {"line": "25"}, "op": "subtract_floor0", "take": {"line": "26"}}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "27"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "27"}], "test": "lt"}, "then": {"amount": {"of": {"line": "27"}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}}], "op": "choose"}
```

Second transcription's note: Line 28 is line 27 divided by $1,000 rounded up to the next higher whole number; the helper computes line 29 directly.

Ruling: open

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "25"}, {"line": "26"}], "test": "le"}, "then": {"line": "24"}}, {"guard": {"args": [{"line": "26"}, {"line": "25"}], "test": "lt"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "27"}, {"const": 0}], "test": "le"}, "then": {"line": "24"}}, {"guard": {"args": [{"const": 0}, {"line": "27"}], "test": "lt"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}], "op": "choose"}
```

Ruling: open

### 31 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: open

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.senior_base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.senior_base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.senior_base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.senior_base_other"}}], "op": "choose"}
```

Ruling: open

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "31"}, "op": "subtract", "take": {"line": "32"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "31"}, "op": "subtract", "take": {"line": "32"}}
```

Ruling: open

### 34 — Multiply line 33 by 6% (0.06)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"line": "32"}}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "33"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "33"}], "test": "lt"}, "then": {"amount": {"line": "33"}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}}], "op": "choose"}
```

Ruling: open

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"line": "31"}, {"line": "32"}], "test": "le"}, "then": {"param": "s1a.senior_amount"}}, {"guard": {"args": [{"line": "32"}, {"line": "31"}], "test": "lt"}, "then": {"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "33"}, {"const": 0}], "test": "le"}, "then": {"param": "s1a.senior_amount"}}, {"guard": {"args": [{"const": 0}, {"line": "33"}], "test": "lt"}, "then": {"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}}], "op": "choose"}
```

Ruling: open

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"line": "35"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "35"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The supplied interface does not provide a scalar taxpayer selector; this reads the person entry whose role is taxpayer.

Ruling: open

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"line": "35"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}, "then": {"line": "35"}}, {"guard": {"args": [{"args": [{"const": false}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The supplied interface does not provide a scalar spouse selector; this reads the person entry whose role is spouse.

Ruling: open

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **AGREE**

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
    note: "The closed interface supplies no Puerto Rico excluded-income amount; this slice treats it as zero."
  - id: s1a.line2b
    printed: "2b"
    label: "Enter the amount from Form 2555, line 45"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Form 2555 is outside the supplied interface; this slice treats the amount as zero."
  - id: s1a.line2c
    printed: "2c"
    label: "Enter the amount from Form 2555, line 50"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Form 2555 is outside the supplied interface; this slice treats the amount as zero."
  - id: s1a.line2d
    printed: "2d"
    label: "Enter the amount from Form 4563, line 15"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Form 4563 is outside the supplied interface; this slice treats the amount as zero."
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
        - guard: {op: test, eq: [s1a.h_tip_count, {const: 1}]}
          then: s1a.h_tip_amount_sum
        - guard: {op: test, ne: [s1a.h_tip_count, {const: 1}]}
          then: s1a.h_zero
    note: "Reads the single tipjob entry when there is exactly one employer; multiple-employer amounts are handled through line 4c."
  - id: s1a.line4b
    printed: "4b"
    label: "Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.h_tip_count, {const: 1}]}
          then: s1a.h_tip_col_c_sum
        - guard: {op: test, ne: [s1a.h_tip_count, {const: 1}]}
          then: s1a.h_zero
    note: "Reads the single tipjob entry when there is exactly one employer; multiple-employer amounts are handled through line 4c."
  - id: s1a.line4c
    printed: "4c"
    label: "If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c. If you received tips as an employee in more than one occupation, see the instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.tips, {const: true}]}
          then: s1a.h_tip_col_d_sum
        - guard: {op: test, eq: [s1a.tips, {const: false}]}
          then: s1a.h_zero
  - id: s1a.line5
    printed: "5"
    label: "Qualified tips received in the course of a trade or business. Qualified tip amount included in Form 1099-NEC, box 1; Form 1099-MISC, box 3; or Form 1099-K, box 1a. Do not enter more than the net profit from the trade or business. If you received qualified tips in the course of more than one trade or business or in more than one occupation, see instructions"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "The supplied interface does not provide nonemployee trade-or-business tip amounts; this slice treats line 5 as zero."
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
    expr: {op: copy, from: s1a.h_base}
  - id: s1a.line10
    printed: "10"
    label: "Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13"
    type: Dollars
    expr: {op: subtract, from: s1a.line8, take: s1a.line9}
  - id: s1a.line12
    printed: "12"
    label: "Multiply line 11 by $100"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_tips_line12}
    note: "Line 11 is the floor of line 10 divided by $1,000; the helper computes the same amount as line 12."
  - id: s1a.line13
    printed: "13"
    label: "Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line10, {const: 0}]}
          then: s1a.line7
        - guard: {op: test, gt: [s1a.line10, {const: 0}]}
          then: s1a.h_tips_sub
  - id: s1a.line14a
    printed: "14a"
    label: "Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.overtime, {const: true}]}
          then: s1a.h_ot_col_b_sum
        - guard: {op: test, eq: [s1a.overtime, {const: false}]}
          then: s1a.h_zero
  - id: s1a.line14b
    printed: "14b"
    label: "Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3 (see instructions)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "The supplied interface provides no payor-level 1099 overtime amount; this slice treats line 14b as zero."
  - id: s1a.line14c
    printed: "14c"
    label: "Add lines 14a and 14b"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line14a, s1a.line14b]}
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
    expr: {op: copy, from: s1a.h_base}
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
        - guard: {op: test, gt: [s1a.line18, {const: 0}]}
          then: s1a.h_ot_line20
        - guard: {op: test, le: [s1a.line18, {const: 0}]}
          then: s1a.h_zero
    note: "Line 19 is the floor of line 18 divided by $1,000; the helper computes line 20 directly."
  - id: s1a.line21
    printed: "21"
    label: "Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line18, {const: 0}]}
          then: s1a.line15
        - guard: {op: test, gt: [s1a.line18, {const: 0}]}
          then: s1a.h_ot_sub
  - id: s1a.line23
    printed: "23"
    label: "Add lines 22a and 22b, column (iii)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.carloan, {const: true}]}
          then: s1a.h_car_col_iii_sum
        - guard: {op: test, eq: [s1a.carloan, {const: false}]}
          then: s1a.h_zero
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
    expr: {op: copy, from: s1a.h_car_base}
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
        - guard: {op: test, gt: [s1a.line27, {const: 0}]}
          then: s1a.h_car_line29
        - guard: {op: test, le: [s1a.line27, {const: 0}]}
          then: s1a.h_zero
    note: "Line 28 is line 27 divided by $1,000 rounded up to the next higher whole number; the helper computes line 29 directly."
  - id: s1a.line30
    printed: "30"
    label: "Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line27, {const: 0}]}
          then: s1a.line24
        - guard: {op: test, gt: [s1a.line27, {const: 0}]}
          then: s1a.h_car_sub
  - id: s1a.line31
    printed: "31"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}
  - id: s1a.line32
    printed: "32"
    label: "Enter $75,000 ($150,000 if married filing jointly)"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_senior_base}
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
        - guard: {op: test, gt: [s1a.line33, {const: 0}]}
          then: s1a.h_senior_product
        - guard: {op: test, le: [s1a.line33, {const: 0}]}
          then: s1a.h_zero
  - id: s1a.line35
    printed: "35"
    label: "Subtract line 34 from $6,000. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line33, {const: 0}]}
          then: s1a.h_senior_amount
        - guard: {op: test, gt: [s1a.line33, {const: 0}]}
          then: s1a.h_senior_sub
  - id: s1a.line36a
    printed: "36a"
    label: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, ne: [f1040.status, {const: "mfs"}]}
              - {op: test, eq: [person.role, {const: "taxpayer"}]}
              - {op: test, eq: [person.work_ssn, {const: true}]}
              - {op: test, eq: [person.age65, {const: true}]}
          then: s1a.line35
        - guard:
            op: test
            any:
              - {op: test, eq: [f1040.status, {const: "mfs"}]}
              - {op: test, ne: [person.role, {const: "taxpayer"}]}
              - {op: test, eq: [person.work_ssn, {const: false}]}
              - {op: test, eq: [person.age65, {const: false}]}
          then: s1a.h_zero
    note: "The supplied interface does not provide a scalar taxpayer selector; this reads the person entry whose role is taxpayer."
  - id: s1a.line36b
    printed: "36b"
    label: "If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [f1040.status, {const: "mfj"}]}
              - {op: test, eq: [person.role, {const: "spouse"}]}
              - {op: test, eq: [person.work_ssn, {const: true}]}
              - {op: test, eq: [person.age65, {const: true}]}
          then: s1a.line35
        - guard:
            op: test
            any:
              - {op: test, ne: [f1040.status, {const: "mfj"}]}
              - {op: test, ne: [person.role, {const: "spouse"}]}
              - {op: test, eq: [person.work_ssn, {const: false}]}
              - {op: test, eq: [person.age65, {const: false}]}
          then: s1a.h_zero
    note: "The supplied interface does not provide a scalar spouse selector; this reads the person entry whose role is spouse."
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

  # Helpers
  - id: s1a.h_zero
    printed: "(helper)"
    label: "Zero amount helper"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: s1a.h_tips_max
    printed: "(helper)"
    label: "Maximum qualified tips deduction"
    type: NonNegDollars
    expr: {op: param, ref: s1a.tips_max}
  - id: s1a.h_base_joint
    printed: "(helper)"
    label: "MAGI base amount for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_joint}
  - id: s1a.h_base_other
    printed: "(helper)"
    label: "MAGI base amount for all other filing statuses"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_other}
  - id: s1a.h_base
    printed: "(helper)"
    label: "MAGI base amount by filing status"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_other
  - id: s1a.h_ot_max_joint
    printed: "(helper)"
    label: "Maximum qualified overtime deduction for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_joint}
  - id: s1a.h_ot_max_other
    printed: "(helper)"
    label: "Maximum qualified overtime deduction for other filing statuses"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_other}
  - id: s1a.h_ot_max
    printed: "(helper)"
    label: "Maximum qualified overtime deduction by filing status"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_ot_max_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_ot_max_other
  - id: s1a.h_car_max
    printed: "(helper)"
    label: "Maximum qualified passenger vehicle loan interest deduction"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_max}
  - id: s1a.h_car_base_joint
    printed: "(helper)"
    label: "Car loan MAGI base amount for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_joint}
  - id: s1a.h_car_base_other
    printed: "(helper)"
    label: "Car loan MAGI base amount for other filing statuses"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_other}
  - id: s1a.h_car_base
    printed: "(helper)"
    label: "Car loan MAGI base amount by filing status"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_car_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_car_base_other
  - id: s1a.h_senior_base_joint
    printed: "(helper)"
    label: "Senior deduction MAGI base amount for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_joint}
  - id: s1a.h_senior_base_other
    printed: "(helper)"
    label: "Senior deduction MAGI base amount for other filing statuses"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_other}
  - id: s1a.h_senior_base
    printed: "(helper)"
    label: "Senior deduction MAGI base amount by filing status"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_senior_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_senior_base_other
  - id: s1a.h_senior_amount
    printed: "(helper)"
    label: "Maximum enhanced deduction for seniors per person"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_amount}
  - id: s1a.h_tip_count
    printed: "(helper)"
    label: "Number of tipjob entries"
    type: Count
    expr: {op: sum_over, collection: tipjob, field: tipjob.one}
  - id: s1a.h_tip_amount_sum
    printed: "(helper)"
    label: "Total qualified tips reported by employers on Form W-2 or Forms 4070"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.amount}
  - id: s1a.h_tip_col_c_sum
    printed: "(helper)"
    label: "Total qualified tips reported on Form 4137 for employer entries"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_c}
  - id: s1a.h_tip_col_d_sum
    printed: "(helper)"
    label: "Total of the greater of column (b) or column (c) for tipjob entries"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_d}
  - id: s1a.h_ot_col_b_sum
    printed: "(helper)"
    label: "Total qualified overtime reported on Form W-2 box 1 for overtime job entries"
    type: NonNegDollars
    expr: {op: sum_over, collection: otjob, field: otjob.col_b}
  - id: s1a.h_car_col_iii_sum
    printed: "(helper)"
    label: "Total qualified passenger vehicle loan interest in column (iii)"
    type: NonNegDollars
    expr: {op: sum_over, collection: carloan, field: carloan.col_iii}
  - id: s1a.h_tips_round
    printed: "(helper)"
    label: "Line 10 rounded down to the next $1,000"
    type: Dollars
    expr: {op: round, of: s1a.line10, unit: 100000, rule: down}
  - id: s1a.h_tips_line12
    printed: "(helper)"
    label: "Line 12: $100 per whole $1,000 of line 10"
    type: Dollars
    expr: {op: multiply_rate, amount: s1a.h_tips_round, rate: {param: s1a.hundred_per_thousand}}
  - id: s1a.h_tips_sub
    printed: "(helper)"
    label: "Line 7 less line 12, not below zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line7, take: s1a.h_tips_line12}
  - id: s1a.h_ot_round
    printed: "(helper)"
    label: "Line 18 rounded down to the next $1,000"
    type: Dollars
    expr: {op: round, of: s1a.line18, unit: 100000, rule: down}
  - id: s1a.h_ot_line20
    printed: "(helper)"
    label: "Line 20: $100 per whole $1,000 of line 18"
    type: Dollars
    expr: {op: multiply_rate, amount: s1a.h_ot_round, rate: {param: s1a.hundred_per_thousand}}
  - id: s1a.h_ot_sub
    printed: "(helper)"
    label: "Line 15 less line 20, not below zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line15, take: s1a.line20}
  - id: s1a.h_car_round
    printed: "(helper)"
    label: "Line 27 rounded up to the next $1,000"
    type: Dollars
    expr: {op: round, of: s1a.line27, unit: 100000, rule: up}
  - id: s1a.h_car_line29
    printed: "(helper)"
    label: "Line 29: $200 per whole $1,000 of line 27"
    type: Dollars
    expr: {op: multiply_rate, amount: s1a.h_car_round, rate: {param: s1a.two_hundred_per_thousand}}
  - id: s1a.h_car_sub
    printed: "(helper)"
    label: "Line 24 less line 29, not below zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line24, take: s1a.line29}
  - id: s1a.h_senior_product
    printed: "(helper)"
    label: "Line 33 multiplied by 6%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.line33, rate: {param: s1a.senior_rate}}
  - id: s1a.h_senior_sub
    printed: "(helper)"
    label: "$6,000 less line 34, not below zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.h_senior_amount, take: s1a.line34}
```
