# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 06abea8be894d6a6666394df8fc8bf29fbb0768fe574263e05739176f6147852 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a413fa53ac13ebe968a805afbc8c962ce627d4f513bc1fc0f3b64129793373c8 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d614d4d87b66cb4cd34e8dce8ac2569e3b7834748a6043d6487924f06650393e |
| printed lines compared | 16 |
| agree / disagree / missing | 1 / 15 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- asset.asset.basis: part 'asset.pct' is not money
- asset.asset.basis: whole operand is not money

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "17"}, {"line": "19(g)"}, {"line": "26(h)"}, {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### asset.s179_2025 — Section 179 elected on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The per-asset section 179 amount is the current-year elected cost; the business income limitation and allocation are made on the business's Form 4562 line 12.

Ruling: representation; triage found no difference. Triage executable-triage-v2 (triage/asset.deepseek.json): 1589 of 1589 comparisons agree; on completed returns no difference.

### asset.mq_q4 — Mid-quarter test basis, fourth quarter
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "asset.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, "then": {"line": "(c)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: The IRS text does not separately name a cumulative prior-depreciation figure. This helper is the current-year MACRS depreciation for property placed in service before 2025, the amount otherwise carried to line 17 or line 26(h).

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### (d) — Recovery period under GDS for the asset class
Status: **AGREE**

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **DISAGREE**

Project:

```json
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"expression": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: Read as the business/investment basis before section 179 and special allowance reductions; the Form 4562 column (c) basis after those reductions is asset.col19c.

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: Line 14 is used only for property not reported in Part V; listed property's allowance is on line 25.

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: representation; triage found no difference. Triage executable-triage-v2 (triage/asset.deepseek.json): 1589 of 1589 comparisons agree; on completed returns no difference.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: Line 19(c) is taken as the current-year basis after section 179 and special depreciation allowance, and is zero for property not placed in service in 2025 or reported in Part V.

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: Line 19(g) only for non-listed property placed in service in 2025; listed property is on line 26(h).

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: Line 17 only for non-listed MACRS property placed in service before 2025; listed property prior-year depreciation is on line 26(h).

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1589 records; this adjudicates the declaration, not the tax reading.

## Raw second transcription

```yaml
lines:
  - id: asset.period
    printed: "(d)"
    label: "Recovery period"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}
  - id: asset.basis
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.pct, whole: {const: 100, type: Count}, places: 2}
    note: "Read as the business/investment basis before section 179 and special allowance reductions; the Form 4562 column (c) basis after those reductions is asset.col19c."
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property placed in service during the tax year"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bonus_line14_choose, take: {const: 0}}
    note: "Line 14 is used only for property not reported in Part V; listed property's allowance is on line 25."
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_f25_choose, take: {const: 0}}
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_f26i_choose, take: {const: 0}}
  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_col19c_choose, take: {const: 0}}
    note: "Line 19(c) is taken as the current-year basis after section 179 and special depreciation allowance, and is zero for property not placed in service in 2025 or reported in Part V."
  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_macrs2025_choose, take: {const: 0}}
    note: "Line 19(g) only for non-listed property placed in service in 2025; listed property is on line 26(h)."
  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS depreciation on assets placed in service in prior years"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_macrs_prior_choose, take: {const: 0}}
    note: "Line 17 only for non-listed MACRS property placed in service before 2025; listed property prior-year depreciation is on line 26(h)."
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_dep_listed_choose, take: {const: 0}}
  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: asset.h_year1
    printed: "(helper)"
    label: "Recovery year one"
    type: Count
    expr: {op: param, ref: sc.year1}
  - id: asset.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: asset.h_is2025
    printed: "(helper)"
    label: "Whether the property was placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.h_is_q4
    printed: "(helper)"
    label: "Whether the property was placed in service in the fourth quarter"
    type: Bool
    expr: {op: test, eq: [asset.quarter, {const: "q4"}]}
  - id: asset.h_bonus_basis
    printed: "(helper)"
    label: "Basis after section 179 before special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.s179_2025}
  - id: asset.h_bonus_40
    printed: "(helper)"
    label: "Special depreciation allowance at 40 percent"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_bonus_basis, rate: {param: sc.bonus_rate_40}}
  - id: asset.h_bonus_current
    printed: "(helper)"
    label: "Special depreciation allowance for property placed in service in 2025"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_zero
        - guard: {op: test, all: [{op: test, eq: [asset.bonus_choice, {const: "full"}]}, {op: test, eq: [asset.after_jan19, {const: true}]}]}
          then: asset.h_bonus_basis
        - guard:
            op: test
            all:
              - {op: test, ne: [asset.bonus_choice, {const: "none"}]}
              - {op: test, not: {op: test, all: [{op: test, eq: [asset.bonus_choice, {const: "full"}]}, {op: test, eq: [asset.after_jan19, {const: true}]}]}}
          then: asset.h_bonus_40
  - id: asset.h_bonus_choose
    printed: "(helper)"
    label: "Special depreciation allowance limited to the first year"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_bonus_current
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for 2025"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bonus_choose, take: {const: 0}}
  - id: asset.h_s179_choose
    printed: "(helper)"
    label: "Section 179 amount for 2025"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 deduction for 2025"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_s179_choose, take: {const: 0}}
    note: "The per-asset section 179 amount is the current-year elected cost; the business income limitation and allocation are made on the business's Form 4562 line 12."
  - id: asset.h_after_bonus
    printed: "(helper)"
    label: "Basis after section 179 and special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bonus_basis, take: asset.bonus_2025}
  - id: asset.h_col19c_choose
    printed: "(helper)"
    label: "Line 19(c) basis"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025_nonlisted, {const: true}]}
          then: asset.h_after_bonus
        - guard: {op: test, eq: [asset.h_is2025_nonlisted, {const: false}]}
          then: asset.h_zero
  - id: asset.h_prior_basis1
    printed: "(helper)"
    label: "Basis after prior section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.prior_179}
  - id: asset.h_prior_basis
    printed: "(helper)"
    label: "Basis after prior section 179 and prior special allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_prior_basis1, take: asset.prior_bonus}
  - id: asset.h_recovery_year
    printed: "(helper)"
    label: "Recovery year in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.h_last_year
    printed: "(helper)"
    label: "Last year of recovery"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}
  - id: asset.h_prior_beyond
    printed: "(helper)"
    label: "Whether the recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [asset.h_recovery_year, asset.h_last_year]}
  - id: asset.h_prior_rate
    printed: "(helper)"
    label: "Prior-property MACRS rate"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_recovery_year]}
  - id: asset.h_prior_macrs_full
    printed: "(helper)"
    label: "Prior-property MACRS before recovery-end check"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_prior_basis, rate: asset.h_prior_rate}
  - id: asset.h_prior_macrs_choose
    printed: "(helper)"
    label: "Prior-property MACRS with recovery-end cutoff"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_prior_beyond, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.h_prior_beyond, {const: false}]}
          then: asset.h_prior_macrs_full
  - id: asset.h_prior_macrs
    printed: "(helper)"
    label: "Current-year MACRS for property placed in service before 2025"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_prior_macrs_choose, take: {const: 0}}
  - id: asset.h_dep_prior_choose
    printed: "(helper)"
    label: "Prior-property depreciation helper"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_prior_macrs
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Depreciation for property placed in service before 2025"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_dep_prior_choose, take: {const: 0}}
    note: "The IRS text does not separately name a cumulative prior-depreciation figure. This helper is the current-year MACRS depreciation for property placed in service before 2025, the amount otherwise carried to line 17 or line 26(h)."
  - id: asset.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}
  - id: asset.h_mq_threshold
    printed: "(helper)"
    label: "Forty percent of total current-year depreciable bases"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.mq_total, rate: {param: sc.bonus_rate_40}}
    note: "The 40 percent mid-quarter threshold is computed with the 40/100 year parameter."
  - id: asset.h_mq_applies
    printed: "(helper)"
    label: "Whether the mid-quarter convention applies"
    type: Bool
    expr: {op: test, gt: [sc.mq_q4, asset.h_mq_threshold]}
  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "Current-year half-year MACRS rate"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year1]}
  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Current-year mid-quarter MACRS rate"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_year1]}
  - id: asset.h_current_macrs_hy
    printed: "(helper)"
    label: "Current-year MACRS under the half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after_bonus, rate: asset.h_rate_hy}
  - id: asset.h_current_macrs_mq
    printed: "(helper)"
    label: "Current-year MACRS under the mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after_bonus, rate: asset.h_rate_mq}
  - id: asset.h_current_macrs_choose
    printed: "(helper)"
    label: "Current-year MACRS convention choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_mq_applies, {const: true}]}
          then: asset.h_current_macrs_mq
        - guard: {op: test, eq: [asset.h_mq_applies, {const: false}]}
          then: asset.h_current_macrs_hy
  - id: asset.h_current_macrs
    printed: "(helper)"
    label: "Current-year regular MACRS"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_current_macrs_choose, take: {const: 0}}
  - id: asset.h_is2025_nonlisted
    printed: "(helper)"
    label: "Whether this is non-listed property placed in service in 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: false}]}]}
  - id: asset.h_is_prior_nonlisted
    printed: "(helper)"
    label: "Whether this is non-listed property placed in service before 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: false}]}, {op: test, eq: [asset.listed, {const: false}]}]}
  - id: asset.h_macrs2025_choose
    printed: "(helper)"
    label: "Line 19(g) MACRS choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025_nonlisted, {const: true}]}
          then: asset.h_current_macrs
        - guard: {op: test, eq: [asset.h_is2025_nonlisted, {const: false}]}
          then: asset.h_zero
  - id: asset.h_macrs_prior_choose
    printed: "(helper)"
    label: "Line 17 MACRS choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_prior_nonlisted, {const: true}]}
          then: asset.h_prior_macrs
        - guard: {op: test, eq: [asset.h_is_prior_nonlisted, {const: false}]}
          then: asset.h_zero
  - id: asset.h_listed_regular_choose
    printed: "(helper)"
    label: "Listed-property regular depreciation choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_current_macrs
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_prior_macrs
  - id: asset.h_listed_regular
    printed: "(helper)"
    label: "Listed-property regular depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_listed_regular_choose, take: {const: 0}}
  - id: asset.h_dep_listed_choose
    printed: "(helper)"
    label: "Line 26(h) depreciation choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_listed_regular
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
  - id: asset.h_bonus_line14_choose
    printed: "(helper)"
    label: "Line 14 special allowance choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.bonus_2025
  - id: asset.h_f25_choose
    printed: "(helper)"
    label: "Line 25 special allowance choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
  - id: asset.h_listed_2025
    printed: "(helper)"
    label: "Whether this is listed property placed in service in 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.h_is2025, {const: true}]}]}
  - id: asset.h_f26i_choose
    printed: "(helper)"
    label: "Line 26(i) elected section 179 cost choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_listed_2025, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.h_listed_2025, {const: false}]}
          then: asset.h_zero
  - id: asset.h_cost179_choose
    printed: "(helper)"
    label: "Section 179 cost eligible for 2025"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.basis
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
  - id: asset.cost179
    printed: "(helper)"
    label: "Cost for section 179 line 2"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_cost179_choose, take: {const: 0}}
  - id: asset.h_mq_total_choose
    printed: "(helper)"
    label: "Mid-quarter total basis choice"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_bonus_basis
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
  - id: asset.mq_total
    printed: "(helper)"
    label: "Total depreciable basis placed in service in 2025 for the mid-quarter test"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_mq_total_choose, take: {const: 0}}
  - id: asset.h_mq_q4_choose
    printed: "(helper)"
    label: "Fourth-quarter basis choice for the mid-quarter test"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.h_is_q4, {const: true}]}]}
          then: asset.h_bonus_basis
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.h_is_q4, {const: true}]}]}}
          then: asset.h_zero
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Fourth-quarter depreciable basis for the mid-quarter test"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_mq_q4_choose, take: {const: 0}}
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Total depreciation and section 179 deduction for 2025"
    type: NonNegDollars
    expr: {op: sum, of: [asset.s179_2025, asset.bonus_2025, asset.macrs2025, asset.macrs_prior, asset.dep_listed]}
```
