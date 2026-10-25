# Transcription agreement — ira

Second transcription of `IRA Deduction Worksheet — Schedule 1, Line 20` by an isolated model (spec 6.5), compared line by line with `forms/2025/ira.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a357420864004c973d6754f81a45e964b05dbc9ab242de065018bc64157657e1 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 73d69e1a339b596759a13fbe27014c5001245845d806c3c823008847d474da26 |
| printed lines compared | 22 |
| agree / disagree / missing | 6 / 16 / 0 |
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
{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}
```

Second:

```json
{"args": [{"ref": "person.ira_work_plan"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Ruling: open

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

Ruling: open

### 1a — Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"ref": "person.ira_work_plan"}
```

Second transcription's note: Taxpayer retirement plan coverage is taken from person.ira_work_plan; the closed input interface does not provide a separate line for it.

Ruling: open

### 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": false}, {"const": true}], "test": "eq"}
```

Second transcription's note: Spouse retirement plan coverage is not provided by the closed input interface; treated as false. This understates deductions when a spouse is covered on a joint return.

Ruling: open

### 2a — Enter the amount shown below that applies to you (your IRA)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"ref": "person.ira_work_plan"}], "test": "not"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"ref": "f1040.separated_spouses"}], "test": "not"}], "test": "all"}, "then": {"param": "ira.full_narrow"}}, {"guard": {"args": [{"args": [{"ref": "f1040.separated_spouses"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"from": {"param": "ira.line2_not_covered"}, "op": "subtract", "take": {"const": 15700000}}}, {"guard": {"args": [{"args": [{"ref": "person.ira_work_plan"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Ruling: open

### 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ira.line2"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line6", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "2a"}, "op": "subtract_floor0", "take": {"line": "5"}}
```

Ruling: open

### 6b — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line6", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "2b"}, "op": "subtract_floor0", "take": {"line": "5"}}
```

Ruling: open

### 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.ira_line7", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"ref": "person.ira_work_plan"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"line": "2a"}, {"line": "5"}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"ref": "person.ira_work_plan"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"line": "5"}, {"line": "2a"}], "test": "lt"}, {"args": [{"line": "6a"}, {"alternatives": [{"guard": {"args": [{"ref": "person.ira_work_plan"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "person.ira_work_plan"}], "test": "not"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"ref": "person.ira_age50"}, {"ref": "person.ira_work_plan"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.rate_40"}}, {"guard": {"args": [{"ref": "person.ira_age50"}, {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"ref": "person.ira_work_plan"}], "test": "not"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"ref": "person.ira_work_plan"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "person.ira_age50"}], "test": "not"}], "test": "all"}, "then": {"param": "ira.rate_35"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"ref": "person.ira_work_plan"}], "test": "not"}], "test": "any"}, {"args": [{"ref": "person.ira_age50"}], "test": "not"}], "test": "all"}, "then": {"param": "ira.rate_70"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "person.ira_work_plan"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"ref": "person.ira_work_plan"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "person.ira_work_plan"}], "test": "not"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"line": "6a"}], "test": "le"}, {"args": [{"line": "5"}, {"line": "2a"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "person.ira_work_plan"}], "test": "not"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"ref": "person.ira_age50"}, "then": {"param": "ira.limit_50"}}, {"guard": {"args": [{"ref": "person.ira_age50"}], "test": "not"}, "then": {"param": "ira.limit"}}], "op": "choose"}}], "op": "choose"}
```

Ruling: open

### 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.ira_line7", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"ref": "person.ira_work_plan"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"line": "5"}, {"line": "2b"}], "test": "lt"}, {"args": [{"line": "6b"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.rate_70"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_40"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.rate_35"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}, {"args": [{"ref": "person.ira_work_plan"}], "test": "not"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"ref": "person.ira_work_plan"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"const": true}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"line": "6b"}], "test": "le"}, {"args": [{"line": "5"}, {"line": "2b"}], "test": "lt"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"const": true}], "test": "eq"}, "then": {"param": "ira.limit_50"}}, {"guard": {"args": [{"const": false}, {"const": true}], "test": "ne"}, "then": {"param": "ira.limit"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "person.ira_work_plan"}, {"args": [{"const": false}, {"const": true}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"line": "2b"}, {"line": "5"}], "test": "le"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 8 — Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "person", "field": "person.box1", "op": "sum_over", "where": null}, {"ref": "s1.line2a"}], "op": "sum"}
```

Second:

```json
{"of": [{"collection": "person", "field": "wages", "op": "sum_over", "where": null}, {"ref": "s1.line2a"}], "op": "sum"}
```

Second transcription's note: Nontaxable combat pay is not in the closed interface; omitted. Refuses when ira.special is true because nonqualified deferred compensation cannot be excluded.

Ruling: open

### 9 — Enter the earned income you (and your spouse if filing jointly) received as a self-employe
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_se", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "person", "field": "ira_se", "op": "sum_over", "where": null}
```

Second transcription's note: Self-employment earned income is taken from person.ira_se; refuses when ira.se_capital is true because only material-income-producing-factor businesses are supported.

Ruling: open

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
{"collection": "person", "field": "ira_trad", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}
```

Second transcription's note: Refuses when the KBH spousal IRA limit applies because the text directs to Pub. 590-A.

Ruling: open

### 11b — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"collection": "person", "field": "ira_trad", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Second transcription's note: Refuses when the KBH spousal IRA limit applies because the text directs to Pub. 590-A.

Ruling: open

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

Second transcription's note: Refuses when the filer wants to deduct a smaller amount (ira.deduct_less).

Ruling: open

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

Second transcription's note: Refuses when the filer wants to deduct a smaller amount (ira.deduct_less).

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ira.line20 | ira.deduct_less, ira.h_kbh_stop, ira.se_capital, ira.special | ira.deduct_less, ira.h_kbh_stop, ira.se_capital, ira.special |
| 8 | ira.special | ira.special |
| 9 | ira.se_capital | ira.se_capital |
| 10 | ira.se_capital, ira.special | ira.se_capital, ira.special |
| 11a | ira.h_kbh_stop | ira.h_kbh_stop |
| 11b | ira.h_kbh_stop | ira.h_kbh_stop |
| 12a | ira.deduct_less, ira.h_kbh_stop, ira.se_capital, ira.special | ira.deduct_less, ira.h_kbh_stop, ira.se_capital, ira.special |
| 12b | ira.deduct_less, ira.h_kbh_stop, ira.se_capital, ira.special | ira.deduct_less, ira.h_kbh_stop, ira.se_capital, ira.special |

## Raw second transcription

```yaml
lines:
  - id: ira.line1a
    printed: "1a"
    label: "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?"
    type: Bool
    expr: {op: copy, from: ira.h_covered_tax}
    note: "Taxpayer retirement plan coverage is taken from person.ira_work_plan; the closed input interface does not provide a separate line for it."
  - id: ira.line1b
    printed: "1b"
    label: "If married filing jointly, was your spouse covered by a retirement plan?"
    type: Bool
    expr: {op: copy, from: ira.h_covered_spouse}
    note: "Spouse retirement plan coverage is not provided by the closed input interface; treated as false. This understates deductions when a spouse is covered on a joint return."
  - id: ira.line2a
    printed: "2a"
    label: "Enter the amount shown below that applies to you."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [ira.h_mfj, {op: test, not: ira.h_covered_tax}]}
          then: ira.h_246
        - guard: {op: test, all: [ira.h_mfj, ira.h_covered_tax]}
          then: ira.h_146
        - guard: ira.h_qss
          then: ira.h_146
        - guard: ira.h_mfs_apart
          then: ira.h_89k
        - guard: ira.h_mfs_together
          then: ira.h_10k
        - guard: ira.h_single
          then: ira.h_89k
        - guard: ira.h_hoh
          then: ira.h_89k
  - id: ira.line2b
    printed: "2b"
    label: "Enter the amount shown below that applies to you."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [ira.h_mfj, {op: test, not: ira.h_covered_spouse}]}
          then: ira.h_246
        - guard: ira.h_mfj
          then: ira.h_146
        - guard: {op: test, not: ira.h_mfj}
          then: ira.h_zero
  - id: ira.line3
    printed: "3"
    label: "Enter the amount from Form 1040 or 1040-SR, line 9."
    type: Dollars
    expr: {op: copy, from: f1040.line9}
  - id: ira.line4
    printed: "4"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25."
    type: NonNegDollars
    expr: {op: sum, of: [s1.line11, s1.line13, s1.line15, s1.line16, s1.line17, s1.line18, s1.line19a, s1.line25]}
    note: "Schedule 1 lines 12, 14 and 23 are not in the closed interface; treated as zero. Only supported lines are summed."
  - id: ira.line5
    printed: "5"
    label: "Subtract line 4 from line 3. If married filing jointly, enter the result in both columns."
    type: Dollars
    expr: {op: subtract, from: ira.line3, take: ira.line4}
  - id: ira.line6a
    printed: "6a"
    label: "Is the amount on line 5 less than the amount on line 2? Yes. Subtract line 5 from line 2 in each column."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ira.line2a, take: ira.line5}
  - id: ira.line6b
    printed: "6b"
    label: "Is the amount on line 5 less than the amount on line 2? Yes. Subtract line 5 from line 2 in each column."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ira.line2b, take: ira.line5}
  - id: ira.line7a
    printed: "7a"
    label: "Multiply lines 6a and 6b by the percentage below that applies to you. If the result isn't a multiple of $10, increase it to the next multiple of $10. If the result is $200 or more, enter the result. But if it is less than $200, enter $200."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: ira.h_skip_tax
          then: ira.h_limit_a
        - guard: {op: test, all: [{op: test, not: ira.h_skip_tax}, {op: test, not: ira.h_6a_ok}]}
          then: ira.h_zero
        - guard: {op: test, all: [{op: test, not: ira.h_skip_tax}, ira.h_6a_ok, {op: test, ge: [ira.line6a, ira.h_thresh_a]}]}
          then: ira.h_limit_a
        - guard: {op: test, all: [{op: test, not: ira.h_skip_tax}, ira.h_6a_ok, {op: test, lt: [ira.line6a, ira.h_thresh_a]}]}
          then: ira.h_line7a_figured
  - id: ira.line7b
    printed: "7b"
    label: "Multiply lines 6a and 6b by the percentage below that applies to you. If the result isn't a multiple of $10, increase it to the next multiple of $10. If the result is $200 or more, enter the result. But if it is less than $200, enter $200."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, not: ira.h_mfj}
          then: ira.h_zero
        - guard: {op: test, all: [ira.h_mfj, ira.h_skip_spouse]}
          then: ira.h_limit_b
        - guard: {op: test, all: [ira.h_mfj, {op: test, not: ira.h_skip_spouse}, {op: test, not: ira.h_6b_ok}]}
          then: ira.h_zero
        - guard: {op: test, all: [ira.h_mfj, {op: test, not: ira.h_skip_spouse}, ira.h_6b_ok, {op: test, ge: [ira.line6b, ira.h_thresh_b]}]}
          then: ira.h_limit_b
        - guard: {op: test, all: [ira.h_mfj, {op: test, not: ira.h_skip_spouse}, ira.h_6b_ok, {op: test, lt: [ira.line6b, ira.h_thresh_b]}]}
          then: ira.h_line7b_figured
  - id: ira.line8
    printed: "8"
    label: "Enter the total of your (and your spouse's if filing jointly): Wages, salaries, tips, etc.; Alimony and separate maintenance payments; Nontaxable combat pay."
    type: NonNegDollars
    expr: {op: sum, of: [ira.h_wages_total, s1.line2a]}
    refuses: [ira.special]
    note: "Nontaxable combat pay is not in the closed interface; omitted. Refuses when ira.special is true because nonqualified deferred compensation cannot be excluded."
  - id: ira.line9
    printed: "9"
    label: "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner."
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: ira_se}
    refuses: [ira.se_capital]
    note: "Self-employment earned income is taken from person.ira_se; refuses when ira.se_capital is true because only material-income-producing-factor businesses are supported."
  - id: ira.line10
    printed: "10"
    label: "Add lines 8 and 9."
    type: NonNegDollars
    expr: {op: sum, of: [ira.line8, ira.line9]}
  - id: ira.line11a
    printed: "11a"
    label: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your IRA."
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: ira_trad, where: {op: test, eq: [person.role, {const: "taxpayer"}]}}
    refuses: [ira.h_kbh_stop]
    note: "Refuses when the KBH spousal IRA limit applies because the text directs to Pub. 590-A."
  - id: ira.line11b
    printed: "11b"
    label: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your spouse's IRA."
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: ira_trad, where: {op: test, eq: [person.role, {const: "spouse"}]}}
    refuses: [ira.h_kbh_stop]
    note: "Refuses when the KBH spousal IRA limit applies because the text directs to Pub. 590-A."
  - id: ira.line12a
    printed: "12a"
    label: "Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct."
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.h_12a_base, ira.line11a]}
    refuses: [ira.deduct_less]
    note: "Refuses when the filer wants to deduct a smaller amount (ira.deduct_less)."
  - id: ira.line12b
    printed: "12b"
    label: "Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct."
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.h_12b_base, ira.line11b]}
    refuses: [ira.deduct_less]
    note: "Refuses when the filer wants to deduct a smaller amount (ira.deduct_less)."
  - id: ira.h_mfj
    printed: "(helper)"
    label: "Filing status is married filing jointly"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfj"}]}
  - id: ira.h_qss
    printed: "(helper)"
    label: "Filing status is qualifying surviving spouse"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "qss"}]}
  - id: ira.h_mfs
    printed: "(helper)"
    label: "Filing status is married filing separately"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}
  - id: ira.h_single
    printed: "(helper)"
    label: "Filing status is single"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "single"}]}
  - id: ira.h_hoh
    printed: "(helper)"
    label: "Filing status is head of household"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "hoh"}]}
  - id: ira.h_mfs_apart
    printed: "(helper)"
    label: "Married filing separately and lived apart from spouse all year"
    type: Bool
    expr: {op: test, all: [ira.h_mfs, f1040.separated_spouses]}
  - id: ira.h_mfs_together
    printed: "(helper)"
    label: "Married filing separately and lived with spouse at some time"
    type: Bool
    expr: {op: test, all: [ira.h_mfs, {op: test, not: f1040.separated_spouses}]}
  - id: ira.h_joint_type
    printed: "(helper)"
    label: "Joint-type filing status (MFJ or QSS)"
    type: Bool
    expr: {op: test, any: [ira.h_mfj, ira.h_qss]}
  - id: ira.joint
    printed: "(helper)"
    label: "Return is married filing jointly"
    type: Bool
    expr: {op: copy, from: ira.h_mfj}
  - id: ira.joint_type
    printed: "(helper)"
    label: "Return is a joint-type status (MFJ or QSS)"
    type: Bool
    expr: {op: copy, from: ira.h_joint_type}
  - id: ira.h_covered_tax
    printed: "(helper)"
    label: "Taxpayer was covered by a retirement plan"
    type: Bool
    expr: {op: copy, from: person.ira_work_plan}
    note: "Taken from person.ira_work_plan; the closed interface does not provide a separate line."
  - id: ira.h_covered_spouse
    printed: "(helper)"
    label: "Spouse was covered by a retirement plan"
    type: Bool
    expr: {op: test, eq: [{const: false}, {const: true}]}
    note: "Not provided by the closed interface; treated as false."
  - id: ira.anyone_covered
    printed: "(helper)"
    label: "Either spouse was covered by a retirement plan"
    type: Bool
    expr: {op: test, any: [ira.h_covered_tax, {op: test, all: [ira.h_mfj, ira.h_covered_spouse]}]}
  - id: ira.h_246
    printed: "(helper)"
    label: "Phase-out threshold for a person not covered by a plan"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2_not_covered}
  - id: ira.h_146
    printed: "(helper)"
    label: "Phase-out threshold for MFJ or QSS"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2}
  - id: ira.h_89k
    printed: "(helper)"
    label: "Phase-out threshold for single, HOH, or MFS living apart"
    type: NonNegDollars
    expr: {op: subtract, from: {param: ira.line2_not_covered}, take: {const: 15700000}}
    note: "Derived constant $89,000 (24600000 - 15700000)."
  - id: ira.h_10k
    printed: "(helper)"
    label: "Ten thousand dollars"
    type: NonNegDollars
    expr: {op: param, ref: ira.full_narrow}
  - id: ira.h_20k
    printed: "(helper)"
    label: "Twenty thousand dollars"
    type: NonNegDollars
    expr: {op: param, ref: ira.full_joint}
  - id: ira.h_zero
    printed: "(helper)"
    label: "Zero dollars"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: ira.h_min
    printed: "(helper)"
    label: "Minimum line 7 amount of $200"
    type: NonNegDollars
    expr: {op: param, ref: ira.min}
  - id: ira.h_limit_under50
    printed: "(helper)"
    label: "IRA limit for age under 50"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit}
  - id: ira.h_limit_over50
    printed: "(helper)"
    label: "IRA limit for age 50 or older"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit_50}
  - id: ira.h_age50_tax
    printed: "(helper)"
    label: "Taxpayer is age 50 or older at end of 2025"
    type: Bool
    expr: {op: copy, from: person.ira_age50}
    note: "Taken from person.ira_age50; the closed interface does not provide a separate line."
  - id: ira.h_age50_spouse
    printed: "(helper)"
    label: "Spouse is age 50 or older at end of 2025"
    type: Bool
    expr: {op: test, eq: [{const: false}, {const: true}]}
    note: "Not provided by the closed interface; treated as false."
  - id: ira.h_limit_a
    printed: "(helper)"
    label: "IRA limit for taxpayer"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: ira.h_age50_tax
          then: ira.h_limit_over50
        - guard: {op: test, not: ira.h_age50_tax}
          then: ira.h_limit_under50
  - id: ira.h_limit_b
    printed: "(helper)"
    label: "IRA limit for spouse"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: ira.h_age50_spouse
          then: ira.h_limit_over50
        - guard: {op: test, not: ira.h_age50_spouse}
          then: ira.h_limit_under50
  - id: ira.h_rate70
    printed: "(helper)"
    label: "Rate 70%"
    type: Rate
    expr: {op: param, ref: ira.rate_70}
  - id: ira.h_rate80
    printed: "(helper)"
    label: "Rate 80%"
    type: Rate
    expr: {op: param, ref: ira.rate_80}
  - id: ira.h_rate35
    printed: "(helper)"
    label: "Rate 35%"
    type: Rate
    expr: {op: param, ref: ira.rate_35}
  - id: ira.h_rate40
    printed: "(helper)"
    label: "Rate 40%"
    type: Rate
    expr: {op: param, ref: ira.rate_40}
  - id: ira.h_rate_a
    printed: "(helper)"
    label: "Applicable percentage for taxpayer column"
    type: Rate
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, any: [{op: test, not: ira.h_covered_tax}, {op: test, not: ira.h_joint_type}]}, ira.h_age50_tax]}
          then: ira.h_rate80
        - guard: {op: test, all: [{op: test, any: [{op: test, not: ira.h_covered_tax}, {op: test, not: ira.h_joint_type}]}, {op: test, not: ira.h_age50_tax}]}
          then: ira.h_rate70
        - guard: {op: test, all: [ira.h_covered_tax, ira.h_joint_type, ira.h_age50_tax]}
          then: ira.h_rate40
        - guard: {op: test, all: [ira.h_covered_tax, ira.h_joint_type, {op: test, not: ira.h_age50_tax}]}
          then: ira.h_rate35
  - id: ira.h_rate_b
    printed: "(helper)"
    label: "Applicable percentage for spouse column"
    type: Rate
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, any: [{op: test, not: ira.h_covered_spouse}, {op: test, not: ira.h_mfj}]}, ira.h_age50_spouse]}
          then: ira.h_rate80
        - guard: {op: test, all: [{op: test, any: [{op: test, not: ira.h_covered_spouse}, {op: test, not: ira.h_mfj}]}, {op: test, not: ira.h_age50_spouse}]}
          then: ira.h_rate70
        - guard: {op: test, all: [ira.h_covered_spouse, ira.h_mfj, ira.h_age50_spouse]}
          then: ira.h_rate40
        - guard: {op: test, all: [ira.h_covered_spouse, ira.h_mfj, {op: test, not: ira.h_age50_spouse}]}
          then: ira.h_rate35
  - id: ira.h_6a_ok
    printed: "(helper)"
    label: "Line 5 is less than line 2a"
    type: Bool
    expr: {op: test, lt: [ira.line5, ira.line2a]}
  - id: ira.h_6b_ok
    printed: "(helper)"
    label: "Line 5 is less than line 2b"
    type: Bool
    expr: {op: test, lt: [ira.line5, ira.line2b]}
  - id: ira.h_skip_tax
    printed: "(helper)"
    label: "Skip lines 2 through 6 for taxpayer"
    type: Bool
    expr: {op: test, all: [{op: test, not: ira.h_covered_tax}, {op: test, any: [{op: test, not: ira.h_mfj}, {op: test, not: ira.h_covered_spouse}]}]}
  - id: ira.h_skip_spouse
    printed: "(helper)"
    label: "Skip lines 2 through 6 for spouse"
    type: Bool
    expr: {op: test, all: [ira.h_mfj, {op: test, not: ira.h_covered_tax}, {op: test, not: ira.h_covered_spouse}]}
  - id: ira.h_thresh_a
    printed: "(helper)"
    label: "Threshold for taxpayer line 6a"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, not: ira.h_joint_type}
          then: ira.h_10k
        - guard: {op: test, all: [ira.h_joint_type, {op: test, not: ira.h_covered_tax}]}
          then: ira.h_10k
        - guard: {op: test, all: [ira.h_joint_type, ira.h_covered_tax]}
          then: ira.h_20k
  - id: ira.h_thresh_b
    printed: "(helper)"
    label: "Threshold for spouse line 6b"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, not: ira.h_mfj}
          then: ira.h_10k
        - guard: {op: test, all: [ira.h_mfj, {op: test, not: ira.h_covered_spouse}]}
          then: ira.h_10k
        - guard: {op: test, all: [ira.h_mfj, ira.h_covered_spouse]}
          then: ira.h_20k
  - id: ira.h_line7a_product
    printed: "(helper)"
    label: "Line 6a times applicable rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: ira.h_rate_a}
  - id: ira.h_line7a_rounded
    printed: "(helper)"
    label: "Line 7a product rounded up to next $10"
    type: NonNegDollars
    expr: {op: round, of: ira.h_line7a_product, unit: 1000, rule: up}
  - id: ira.h_line7a_figured
    printed: "(helper)"
    label: "Line 7a figured amount (at least $200)"
    type: NonNegDollars
    expr: {op: larger_of, of: [ira.h_line7a_rounded, ira.h_min]}
  - id: ira.h_line7b_product
    printed: "(helper)"
    label: "Line 6b times applicable rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: ira.h_rate_b}
  - id: ira.h_line7b_rounded
    printed: "(helper)"
    label: "Line 7b product rounded up to next $10"
    type: NonNegDollars
    expr: {op: round, of: ira.h_line7b_product, unit: 1000, rule: up}
  - id: ira.h_line7b_figured
    printed: "(helper)"
    label: "Line 7b figured amount (at least $200)"
    type: NonNegDollars
    expr: {op: larger_of, of: [ira.h_line7b_rounded, ira.h_min]}
  - id: ira.h_wages_total
    printed: "(helper)"
    label: "Total wages, salaries, tips, etc. of all persons"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: wages}
  - id: ira.h_se_total
    printed: "(helper)"
    label: "Total self-employment earned income for IRA purposes"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: ira_se}
  - id: ira.h_12a_base
    printed: "(helper)"
    label: "Smaller of line 7a and line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.line7a, ira.line10]}
  - id: ira.h_12b_base
    printed: "(helper)"
    label: "Smaller of line 7b and line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.line7b, ira.line10]}
  - id: ira.h_kbh_none
    printed: "(helper)"
    label: "KBH limit if neither spouse is age 50 or older"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_none}
  - id: ira.h_kbh_one
    printed: "(helper)"
    label: "KBH limit if one spouse is age 50 or older"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_one}
  - id: ira.h_kbh_both
    printed: "(helper)"
    label: "KBH limit if both spouses are age 50 or older"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_both}
  - id: ira.h_kbh_limit
    printed: "(helper)"
    label: "Applicable KBH spousal IRA limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [ira.h_age50_tax, ira.h_age50_spouse]}
          then: ira.h_kbh_both
        - guard: {op: test, all: [{op: test, any: [ira.h_age50_tax, ira.h_age50_spouse]}, {op: test, not: {op: test, all: [ira.h_age50_tax, ira.h_age50_spouse]}}]}
          then: ira.h_kbh_one
        - guard: {op: test, all: [{op: test, not: ira.h_age50_tax}, {op: test, not: ira.h_age50_spouse}]}
          then: ira.h_kbh_none
  - id: ira.h_kbh_stop
    printed: "(helper)"
    label: "Line 10 is below the KBH spousal IRA limit"
    type: Bool
    expr: {op: test, all: [ira.h_mfj, {op: test, lt: [ira.line10, ira.h_kbh_limit]}]}
  - id: ira.line20
    printed: "(helper)"
    label: "Total IRA deduction (line 12a plus line 12b)"
    type: NonNegDollars
    expr: {op: sum, of: [ira.line12a, ira.line12b]}
```
