# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 1e804de2adc85ee0a1874085d1130512e80b77a7fd9917cf96441ecf0be4432c |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 6023d39afd72d44d611985d10019122c4a9b45cf5ee0dbc879ec411f98cf2c80 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 131072 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 9ee21d333a313ab2156e18b7d8e7c0397d069fb44a24764a8c399efa55575472 |
| printed lines compared | 16 |
| agree / disagree / missing | 1 / 15 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

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
{"expression": {"of": [{"line": "17"}, {"line": "19(g)"}, {"line": "26(h)"}], "op": "sum"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "14"}, {"line": "25"}], "op": "sum"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### asset.s179_2025 — Section 179 elected on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error — the candidate computes section 179 from a basis built with asset.pct (a Count) in a money operation, the same declaration error that invalidates asset.basis; triage: 1628 comparisons, one value difference and candidate-unknown records. The project computes the basis with the percentage applied as a rate. The line is not in the invalid closure only because its own declaration parses.

### asset.mq_q4 — Mid-quarter test basis, fourth quarter
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "asset.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"line": "(c)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: The supplied interface does not include accumulated prior depreciation; this carries the current-year deduction for property placed in service before 2025, including prior-placed listed property where the supplied inputs determine it.

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

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

Second transcription's note: The business-use percentage is supplied as a whole-number Count; this computes cost times that percentage over 100, rounded half-up to the cent.

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: For property acquired before January 20, 2025, the 'full' choice is read as the applicable 40% allowance; the 'forty' choice is the elected 40% allowance.

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"expression": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_bonus"}}], "op": "choose"}}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: No credit or other basis-reduction inputs are supplied; those reductions are taken as zero.

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.basis", "message": "asset.asset.basis: part 'asset.pct' is not money"}, {"line": "asset.basis", "message": "asset.asset.basis: whole operand is not money"}]}
```

Second transcription's note: Only line 26 (listed property used more than 50% in a qualified business use) is represented; line 27 for 50% or less is outside the supplied line set, so this line is zero in that case.

Ruling: model error — the candidate's asset.basis applies asset.pct (a Count, whole percent) as a money operand ("part 'asset.pct' is not money"), so the host type check rejects the declaration and its dependency closure (T-143 candidate-invalid; 0 comparisons for this line). This adjudicates the declaration, not the tax reading; the project applies the percentage as a rate.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |
| asset.bonus_2025 | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |
| asset.mq_q4 | asset.screen | asset.screen |
| asset.mq_total | asset.screen | asset.screen |
| asset.cost179 | asset.screen | asset.screen |
| asset.dep_prior | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.screen | asset.screen |
| 14 | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |
| 25 | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |
| 26(i) | asset.screen | asset.screen |
| 19(c) | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |
| 19(g) | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |
| 17 | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |
| 26(h) | asset.bonus_same, asset.screen | asset.bonus_same, asset.screen |

## Raw second transcription

```yaml
lines:
  - id: asset.period
    printed: "(d)"
    label: "Recovery period"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}
    refuses: [asset.screen]
  - id: asset.basis
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.pct, whole: {const: 100, type: Count}, places: 2}
    refuses: [asset.screen]
    note: "The business-use percentage is supplied as a whole-number Count; this computes cost times that percentage over 100, rounded half-up to the cent."
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.h_is_listed, {const: false}]}
          then: asset.h_bonus_allowed
    refuses: [asset.screen, asset.bonus_same]
    note: "For property acquired before January 20, 2025, the 'full' choice is read as the applicable 40% allowance; the 'forty' choice is the elected 40% allowance."
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.h_bonus_allowed
        - guard: {op: test, eq: [asset.h_is_listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.bonus_same]
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.h_is_listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_basis_after_s179, take: asset.h_bonus_used}
    refuses: [asset.screen, asset.bonus_same]
    note: "No credit or other basis-reduction inputs are supplied; those reductions are taken as zero."
  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.h_current_nonlisted_mq, {const: true}]}
          then: asset.h_macrs_2025_mq
        - guard: {op: test, eq: [asset.h_current_nonlisted_hy, {const: true}]}
          then: asset.h_macrs_2025_hy
    refuses: [asset.screen]
  - id: asset.macrs_prior
    printed: "17"
    label: "Depreciation deduction for prior-year MACRS assets"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.h_prior_nonlisted_active, {const: true}]}
          then: asset.h_dep_prior_raw
        - guard: {op: test, eq: [asset.h_prior_nonlisted_inactive, {const: true}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_listed, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is_listed, {const: true}]}
              - {op: test, eq: [asset.h_pct_over50, {const: false}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.h_listed_qbu_2025_mq, {const: true}]}
          then: asset.h_macrs_2025_mq
        - guard: {op: test, eq: [asset.h_listed_qbu_2025_hy, {const: true}]}
          then: asset.h_macrs_2025_hy
        - guard: {op: test, eq: [asset.h_listed_qbu_prior_active, {const: true}]}
          then: asset.h_dep_prior_raw
        - guard: {op: test, eq: [asset.h_listed_qbu_prior_inactive, {const: true}]}
          then: asset.h_zero
    refuses: [asset.screen]
    note: "Only line 26 (listed property used more than 50% in a qualified business use) is represented; line 27 for 50% or less is outside the supplied line set, so this line is zero in that case."
  - id: asset.h_is2025
    printed: "(helper)"
    label: "Whether the property was placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.h_after_jan19
    printed: "(helper)"
    label: "Whether the property was acquired after January 19, 2025"
    type: Bool
    expr: {op: test, eq: [asset.after_jan19, {const: true}]}
  - id: asset.h_choice_full
    printed: "(helper)"
    label: "Whether the full special allowance choice was made"
    type: Bool
    expr: {op: test, eq: [asset.bonus_choice, {const: "full"}]}
  - id: asset.h_choice_forty
    printed: "(helper)"
    label: "Whether the 40% special allowance choice was made"
    type: Bool
    expr: {op: test, eq: [asset.bonus_choice, {const: "forty"}]}
  - id: asset.h_choice_none
    printed: "(helper)"
    label: "Whether no special allowance was elected"
    type: Bool
    expr: {op: test, eq: [asset.bonus_choice, {const: "none"}]}
  - id: asset.h_is_listed
    printed: "(helper)"
    label: "Whether the property is listed property"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: true}]}
  - id: asset.h_pct_over50
    printed: "(helper)"
    label: "Whether the business-use percentage is more than 50%"
    type: Bool
    expr: {op: test, gt: [asset.pct, {const: 50, type: Count}]}
  - id: asset.h_is_q4
    printed: "(helper)"
    label: "Whether the property was placed in service in the fourth quarter"
    type: Bool
    expr: {op: test, eq: [asset.quarter, {const: "q4"}]}
  - id: asset.h_recovery_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.h_last_year
    printed: "(helper)"
    label: "Last year of recovery for this recovery period"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}
  - id: asset.h_recovery_active
    printed: "(helper)"
    label: "Whether the recovery period has not ended before 2025"
    type: Bool
    expr: {op: test, le: [asset.h_recovery_year, asset.h_last_year]}
  - id: asset.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: asset.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}
  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "MACRS rate using the half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_recovery_year]}
  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "MACRS rate using the mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_recovery_year]}
  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "MACRS rate using the convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_recovery_year]}
  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: asset.h_s179_used
    printed: "(helper)"
    label: "Section 179 amount used in the basis for this property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.prior_179
  - id: asset.h_basis_after_s179
    printed: "(helper)"
    label: "Basis after section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.h_s179_used}
  - id: asset.h_bonus_full
    printed: "(helper)"
    label: "Special allowance at 100%"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_basis_after_s179}
  - id: asset.h_bonus_forty
    printed: "(helper)"
    label: "Special allowance at 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_after_s179, rate: {param: sc.bonus_rate_40}}
  - id: asset.h_bonus_total_2025
    printed: "(helper)"
    label: "Special depreciation allowance before listed-property screening"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_choice_none, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_after_jan19, {const: true}]}
              - {op: test, eq: [asset.h_choice_full, {const: true}]}
          then: asset.h_bonus_full
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_after_jan19, {const: true}]}
              - {op: test, eq: [asset.h_choice_forty, {const: true}]}
          then: asset.h_bonus_forty
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_after_jan19, {const: false}]}
              - {op: test, eq: [asset.h_choice_none, {const: false}]}
          then: asset.h_bonus_forty
  - id: asset.h_bonus_allowed
    printed: "(helper)"
    label: "Special depreciation allowance allowed for this property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is_listed, {const: true}]}
              - {op: test, eq: [asset.h_pct_over50, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is_listed, {const: true}]}
                - {op: test, eq: [asset.h_pct_over50, {const: false}]}
          then: asset.h_bonus_total_2025
  - id: asset.h_bonus_used
    printed: "(helper)"
    label: "Special allowance included in the basis for depreciation"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_bonus_allowed
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.prior_bonus
  - id: asset.h_dep_prior_raw
    printed: "(helper)"
    label: "MACRS deduction for a prior-year asset using its prior convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_rate_prior}
  - id: asset.h_macrs_2025_hy
    printed: "(helper)"
    label: "2025 MACRS deduction using the half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_rate_hy}
  - id: asset.h_macrs_2025_mq
    printed: "(helper)"
    label: "2025 MACRS deduction using the mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_rate_mq}
  - id: asset.h_mq_threshold
    printed: "(helper)"
    label: "40% of total 2025 depreciable basis for the mid-quarter test"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.mq_total, rate: {param: sc.bonus_rate_40}}
  - id: asset.h_mq_applies
    printed: "(helper)"
    label: "Whether the mid-quarter convention applies"
    type: Bool
    expr: {op: test, gt: [sc.mq_q4, asset.h_mq_threshold]}
  - id: asset.h_current_nonlisted_mq
    printed: "(helper)"
    label: "Current-year nonlisted property with mid-quarter convention"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.h_is_listed, {const: false}]}
        - {op: test, eq: [asset.h_mq_applies, {const: true}]}
  - id: asset.h_current_nonlisted_hy
    printed: "(helper)"
    label: "Current-year nonlisted property with half-year convention"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.h_is_listed, {const: false}]}
        - {op: test, eq: [asset.h_mq_applies, {const: false}]}
  - id: asset.h_prior_nonlisted_active
    printed: "(helper)"
    label: "Prior-year nonlisted property still within its recovery period"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: false}]}
        - {op: test, eq: [asset.h_is_listed, {const: false}]}
        - {op: test, eq: [asset.h_recovery_active, {const: true}]}
  - id: asset.h_prior_nonlisted_inactive
    printed: "(helper)"
    label: "Prior-year nonlisted property whose recovery period has ended"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: false}]}
        - {op: test, eq: [asset.h_is_listed, {const: false}]}
        - {op: test, eq: [asset.h_recovery_active, {const: false}]}
  - id: asset.h_listed_qbu
    printed: "(helper)"
    label: "Listed property used more than 50% in a qualified business use"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is_listed, {const: true}]}
        - {op: test, eq: [asset.h_pct_over50, {const: true}]}
  - id: asset.h_listed_qbu_2025
    printed: "(helper)"
    label: "Listed property used more than 50% placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_listed_qbu, {const: true}]}
        - {op: test, eq: [asset.h_is2025, {const: true}]}
  - id: asset.h_listed_qbu_prior
    printed: "(helper)"
    label: "Listed property used more than 50% placed in service before 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_listed_qbu, {const: true}]}
        - {op: test, eq: [asset.h_is2025, {const: false}]}
  - id: asset.h_listed_qbu_prior_active
    printed: "(helper)"
    label: "Prior-year listed property used more than 50% still within recovery"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_listed_qbu_prior, {const: true}]}
        - {op: test, eq: [asset.h_recovery_active, {const: true}]}
  - id: asset.h_listed_qbu_prior_inactive
    printed: "(helper)"
    label: "Prior-year listed property used more than 50% with recovery ended"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_listed_qbu_prior, {const: true}]}
        - {op: test, eq: [asset.h_recovery_active, {const: false}]}
  - id: asset.h_listed_qbu_2025_mq
    printed: "(helper)"
    label: "2025 listed property used more than 50% with mid-quarter convention"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_listed_qbu_2025, {const: true}]}
        - {op: test, eq: [asset.h_mq_applies, {const: true}]}
  - id: asset.h_listed_qbu_2025_hy
    printed: "(helper)"
    label: "2025 listed property used more than 50% with half-year convention"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_listed_qbu_2025, {const: true}]}
        - {op: test, eq: [asset.h_mq_applies, {const: false}]}
  - id: asset.h_dep_listed_prior_allowed
    printed: "(helper)"
    label: "Current-year depreciation on prior-year listed property used more than 50%"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_listed_qbu_prior_active, {const: true}]}
          then: asset.h_dep_prior_raw
        - guard: {op: test, eq: [asset.h_listed_qbu_prior_active, {const: false}]}
          then: asset.h_zero
  - id: asset.h_mq_basis
    printed: "(helper)"
    label: "Depreciable basis includible in the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is_listed, {const: true}]}
              - {op: test, eq: [asset.h_pct_over50, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is_listed, {const: true}]}
                - {op: test, eq: [asset.h_pct_over50, {const: false}]}
          then: asset.h_basis_after_s179
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 deduction for 2025 for this property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_pct_over50, {const: true}]}
          then: asset.s179
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is2025, {const: true}]}
                - {op: test, eq: [asset.h_pct_over50, {const: true}]}
          then: asset.h_zero
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Fourth-quarter 2025 depreciable basis for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_is_q4, {const: true}]}
          then: asset.h_mq_basis
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is2025, {const: true}]}
                - {op: test, eq: [asset.h_is_q4, {const: true}]}
          then: asset.h_zero
  - id: asset.mq_total
    printed: "(helper)"
    label: "Total 2025 depreciable basis for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_mq_basis
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_pct_over50, {const: true}]}
          then: asset.basis
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is2025, {const: true}]}
                - {op: test, eq: [asset.h_pct_over50, {const: true}]}
          then: asset.h_zero
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Total depreciation deduction for 2025 for this property"
    type: NonNegDollars
    expr: {op: sum, of: [asset.macrs2025, asset.macrs_prior, asset.dep_listed]}
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Total special depreciation allowance for 2025 for this property"
    type: NonNegDollars
    expr: {op: sum, of: [asset.bonus, asset.f25]}
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Current-year depreciation on property placed in service before 2025"
    type: NonNegDollars
    expr: {op: sum, of: [asset.macrs_prior, asset.h_dep_listed_prior_allowed]}
    note: "The supplied interface does not include accumulated prior depreciation; this carries the current-year deduction for property placed in service before 2025, including prior-placed listed property where the supplied inputs determine it."
```
