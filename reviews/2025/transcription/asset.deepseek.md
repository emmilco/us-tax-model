# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | e1743bd11f13a326138990155b6fc9d394696336559999f620f6cba8c5161f90 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0f1df70975dae8df7b1ffdb285589a51a9f6b67c79822b31fe1d630b33de9de6 |
| printed lines compared | 16 |
| agree / disagree / missing | 1 / 15 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 98 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object
- malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- malformed expression (project schema): data/alternatives/1/guard/not/all/0 must be object, data/alternatives/1/guard/not/all/0 must be object, data/alternatives/1/guard/not/all/0 must be object
- malformed expression (project schema): data/alternatives/2/guard/all/1 must be object, data/alternatives/2/guard/all/1 must be object, data/alternatives/2/guard/all/1 must be object
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- malformed expression (project schema): data/alternatives/1/guard/not/all/1 must be object, data/alternatives/1/guard/not/all/1 must be object, data/alternatives/1/guard/not/all/1 must be object
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object
- malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object
- malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object
- malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- asset.asset.f25: malformed expression
- asset.asset.f26i: malformed expression
- asset.asset.col19c: malformed expression
- asset.asset.macrs2025: malformed expression
- asset.asset.macrs_prior: malformed expression
- asset.asset.dep_listed: malformed expression
- asset.asset.s179_2025: malformed expression
- asset.asset.mq_q4: malformed expression
- asset.asset.cost179: malformed expression
- asset.asset.dep_prior: atom 'opaque' is not implemented in this stage
- asset.asset.dep_prior: atom 'opaque' has no checker support in this stage
- asset.asset.h_listed_low: malformed expression
- asset.asset.h_179_ok: malformed expression
- asset.asset.on_19: malformed expression
- asset.asset.on_17: malformed expression
- asset.asset.h_bonus_fullcase: malformed expression
- asset.asset.mqbase: malformed expression
- asset.asset.h_current_dep: malformed expression

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "17"}, {"line": "19(g)"}, {"line": "26(h)"}], "op": "sum"}, "invalid_model_types": [{"line": "asset.f25", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object"}, {"line": "asset.macrs2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.macrs_prior", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/0 must be object, data/alternatives/1/guard/not/all/0 must be object, data/alternatives/1/guard/not/all/0 must be object"}, {"line": "asset.dep_listed", "message": "malformed expression (project schema): data/alternatives/2/guard/all/1 must be object, data/alternatives/2/guard/all/1 must be object, data/alternatives/2/guard/all/1 must be object"}, {"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.on_19", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.h_bonus_fullcase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_current_dep", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.f25", "message": "asset.asset.f25: malformed expression"}, {"line": "asset.macrs2025", "message": "asset.asset.macrs2025: malformed expression"}, {"line": "asset.macrs_prior", "message": "asset.asset.macrs_prior: malformed expression"}, {"line": "asset.dep_listed", "message": "asset.asset.dep_listed: malformed expression"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.on_19", "message": "asset.asset.on_19: malformed expression"}, {"line": "asset.h_bonus_fullcase", "message": "asset.asset.h_bonus_fullcase: malformed expression"}, {"line": "asset.h_current_dep", "message": "asset.asset.h_current_dep: malformed expression"}]}
```

Ruling: open

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "14"}, {"line": "25"}], "op": "sum"}, "invalid_model_types": [{"line": "asset.f25", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object"}, {"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.h_bonus_fullcase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.f25", "message": "asset.asset.f25: malformed expression"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.h_bonus_fullcase", "message": "asset.asset.h_bonus_fullcase: malformed expression"}]}
```

Ruling: open

### asset.s179_2025 — Section 179 elected on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}]}
```

Ruling: open

### asset.mq_q4 — Mid-quarter test basis, fourth quarter
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "asset.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.mq_q4", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/1 must be object, data/alternatives/1/guard/not/all/1 must be object, data/alternatives/1/guard/not/all/1 must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.mqbase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.mq_q4", "message": "asset.asset.mq_q4: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.mqbase", "message": "asset.asset.mqbase: malformed expression"}]}
```

Ruling: open

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.mqbase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.mqbase", "message": "asset.asset.mqbase: malformed expression"}]}
```

Ruling: open

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"line": "(c)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.cost179", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.cost179", "message": "asset.asset.cost179: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}]}
```

Ruling: open

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"expression": {"unknown": "{\"name\": \"macrs_accumulated_depreciation_before_2025\", \"op\": \"opaque\"}"}, "invalid_model_types": [{"line": "asset.dep_prior", "message": "asset.asset.dep_prior: atom 'opaque' is not implemented in this stage"}, {"line": "asset.dep_prior", "message": "asset.asset.dep_prior: atom 'opaque' has no checker support in this stage"}]}
```

Second transcription's note: The archived text does not give a single printed prior-years depreciation line. The amount is the sum of the MACRS table rates for the earlier recovery years applied to the property's unadjusted basis, together with any prior section 179 and special depreciation allowance; the model has no loop over prior years, so this is represented as an opaque helper.

Ruling: open

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
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"const": 100}}
```

Ruling: open

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"input": "asset.after_jan19"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.h_bonus_fullcase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.h_bonus_fullcase", "message": "asset.asset.h_bonus_fullcase: malformed expression"}]}
```

Ruling: open

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"input": "asset.after_jan19"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.f25", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object"}, {"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.h_bonus_fullcase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.f25", "message": "asset.asset.f25: malformed expression"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.h_bonus_fullcase", "message": "asset.asset.h_bonus_fullcase: malformed expression"}]}
```

Ruling: open

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.f26i", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object"}, {"line": "asset.f26i", "message": "asset.asset.f26i: malformed expression"}]}
```

Ruling: open

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"of": [{"line": "14"}, {"line": "25"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.f25", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object"}, {"line": "asset.col19c", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.on_19", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.h_bonus_fullcase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.f25", "message": "asset.asset.f25: malformed expression"}, {"line": "asset.col19c", "message": "asset.asset.col19c: malformed expression"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.on_19", "message": "asset.asset.on_19: malformed expression"}, {"line": "asset.h_bonus_fullcase", "message": "asset.asset.h_bonus_fullcase: malformed expression"}]}
```

Ruling: open

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"of": [{"line": "14"}, {"line": "25"}], "op": "sum"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"of": [{"line": "14"}, {"line": "25"}], "op": "sum"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.f25", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object"}, {"line": "asset.macrs2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.on_19", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.h_bonus_fullcase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_current_dep", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.f25", "message": "asset.asset.f25: malformed expression"}, {"line": "asset.macrs2025", "message": "asset.asset.macrs2025: malformed expression"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.on_19", "message": "asset.asset.on_19: malformed expression"}, {"line": "asset.h_bonus_fullcase", "message": "asset.asset.h_bonus_fullcase: malformed expression"}, {"line": "asset.h_current_dep", "message": "asset.asset.h_current_dep: malformed expression"}]}
```

Ruling: open

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.macrs_prior", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/0 must be object, data/alternatives/1/guard/not/all/0 must be object, data/alternatives/1/guard/not/all/0 must be object"}, {"line": "asset.macrs_prior", "message": "asset.asset.macrs_prior: malformed expression"}]}
```

Ruling: open

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"of": [{"line": "14"}, {"line": "25"}], "op": "sum"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"of": [{"line": "14"}, {"line": "25"}], "op": "sum"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.f25", "message": "malformed expression (project schema): data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object, data/alternatives/1/guard/not/all/2 must be object"}, {"line": "asset.dep_listed", "message": "malformed expression (project schema): data/alternatives/2/guard/all/1 must be object, data/alternatives/2/guard/all/1 must be object, data/alternatives/2/guard/all/1 must be object"}, {"line": "asset.s179_2025", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_179_ok", "message": "malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object"}, {"line": "asset.h_bonus_fullcase", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.h_current_dep", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "asset.f25", "message": "asset.asset.f25: malformed expression"}, {"line": "asset.dep_listed", "message": "asset.asset.dep_listed: malformed expression"}, {"line": "asset.s179_2025", "message": "asset.asset.s179_2025: malformed expression"}, {"line": "asset.h_179_ok", "message": "asset.asset.h_179_ok: malformed expression"}, {"line": "asset.h_bonus_fullcase", "message": "asset.asset.h_bonus_fullcase: malformed expression"}, {"line": "asset.h_current_dep", "message": "asset.asset.h_current_dep: malformed expression"}]}
```

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.h_listed_low | asset.h_bonus_mixed, asset.h_listed_low |
| asset.bonus_2025 | asset.h_bonus_mixed | asset.h_bonus_mixed |
| 14 | asset.h_bonus_mixed | asset.h_bonus_mixed |
| 25 | asset.h_bonus_mixed | asset.h_bonus_mixed |
| 19(c) | asset.h_bonus_mixed | asset.h_bonus_mixed |
| 19(g) | asset.h_bonus_mixed | asset.h_bonus_mixed |
| 26(h) | asset.h_bonus_mixed, asset.h_listed_low | asset.h_bonus_mixed, asset.h_listed_low |

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
    label: "Basis for depreciation (business/investment use only), before the section 179 expense deduction and special depreciation allowance"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_cents, whole: {const: 100}, places: 2}
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property placed in service during the tax year"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: false}]}]}, then: asset.h_bonus_current}, {guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: false}]}]}}, then: asset.h_zero}]}
    refuses: [asset.h_bonus_mixed]
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}, asset.h_over_half]}, then: asset.h_bonus_current}, {guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}, asset.h_over_half]}}, then: asset.h_zero}]}
    refuses: [asset.h_bonus_mixed]
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost for listed property"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}, asset.h_over_half]}, then: asset.s179}, {guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}, asset.h_over_half]}}, then: asset.h_zero}]}
  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.on_19, then: asset.h_basis_after_bonus}, {guard: {op: test, eq: [asset.on_19, {const: false}]}, then: asset.h_zero}]}
  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction for assets placed in service in 2025 under MACRS"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.on_19, then: asset.h_current_dep}, {guard: {op: test, eq: [asset.on_19, {const: false}]}, then: asset.h_zero}]}
  - id: asset.macrs_prior
    printed: "17"
    label: "Depreciation for tangible property placed in service in prior years and depreciated under MACRS"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, all: [asset.on_17, asset.h_done_false]}, then: asset.macrs_prior_live}, {guard: {op: test, not: {op: test, all: [asset.on_17, asset.h_done_false]}}, then: asset.h_zero}]}
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction for listed property used more than 50% in a qualified business use"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [asset.listed, {const: false}]}, then: asset.h_zero}, {guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.is2025, {const: true}]}]}, then: asset.h_current_dep}, {guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, asset.h_not_2025, asset.h_done_false]}, then: asset.macrs_prior_live}, {guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, asset.h_not_2025, {op: test, eq: [asset.done, {const: true}]}]}, then: asset.h_zero}]}
    refuses: [asset.h_listed_low]
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Total MACRS depreciation for 2025 on this property"
    type: NonNegDollars
    expr: {op: sum, of: [asset.macrs2025, asset.macrs_prior, asset.dep_listed]}
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Total special depreciation allowance for 2025 on this property"
    type: NonNegDollars
    expr: {op: sum, of: [asset.bonus, asset.f25]}
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 expense deduction for 2025 on this property"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.h_179_ok, then: asset.s179}, {guard: {op: test, eq: [asset.h_179_ok, {const: false}]}, then: asset.h_zero}]}
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis placed in service in the last 3 months of 2025 for the mid-quarter convention test"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, asset.h_quarter_q4]}, then: asset.mqbase}, {guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, asset.h_quarter_q4]}}, then: asset.h_zero}]}
  - id: asset.mq_total
    printed: "(helper)"
    label: "Total depreciable basis placed in service in 2025 for the mid-quarter convention test"
    type: NonNegDollars
    expr: {op: copy, from: asset.mqbase}
  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.h_179_ok, then: asset.basis}, {guard: {op: test, eq: [asset.h_179_ok, {const: false}]}, then: asset.h_zero}]}
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Depreciation allowed or allowable for this property before 2025"
    type: NonNegDollars
    expr: {op: opaque, name: "macrs_accumulated_depreciation_before_2025"}
    note: "The archived text does not give a single printed prior-years depreciation line. The amount is the sum of the MACRS table rates for the earlier recovery years applied to the property's unadjusted basis, together with any prior section 179 and special depreciation allowance; the model has no loop over prior years, so this is represented as an opaque helper."
  - id: asset.h_one_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: asset.h_pct_cents
    printed: "(helper)"
    label: "Business use percentage expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_one_cent, count: asset.pct}
  - id: asset.is2025
    printed: "(helper)"
    label: "Property placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.h_not_2025
    printed: "(helper)"
    label: "Property not placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.is2025, {const: false}]}
  - id: asset.h_listed_true
    printed: "(helper)"
    label: "Listed property"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: true}]}
  - id: asset.h_listed_false
    printed: "(helper)"
    label: "Not listed property"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: false}]}
  - id: asset.h_over_half
    printed: "(helper)"
    label: "Business use more than 50%"
    type: Bool
    expr: {op: test, gt: [asset.pct, {const: 50, type: Count}]}
  - id: asset.h_listed_low
    printed: "(helper)"
    label: "Listed property used 50% or less in the business"
    type: Bool
    expr: {op: test, all: [asset.h_listed_true, {op: test, le: [asset.pct, {const: 50, type: Count}]}]}
  - id: asset.h_not_listed_low
    printed: "(helper)"
    label: "Not listed property used 50% or less in the business"
    type: Bool
    expr: {op: test, eq: [asset.h_listed_low, {const: false}]}
  - id: asset.h_179_ok
    printed: "(helper)"
    label: "Property eligible for the section 179 election in 2025"
    type: Bool
    expr: {op: test, all: [asset.is2025, asset.h_not_listed_low]}
  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "Special depreciation allowance choice is not the same for the recovery period class"
    type: Bool
    expr: {op: test, eq: [asset.bonus_same, {const: false}]}
  - id: asset.on_19
    printed: "(helper)"
    label: "Property reported in line 19"
    type: Bool
    expr: {op: test, all: [asset.is2025, asset.h_listed_false]}
  - id: asset.on_17
    printed: "(helper)"
    label: "Property reported in line 17"
    type: Bool
    expr: {op: test, all: [asset.h_not_2025, asset.h_listed_false]}
  - id: asset.h_quarter_q4
    printed: "(helper)"
    label: "Placed in service in the fourth quarter"
    type: Bool
    expr: {op: test, eq: [asset.quarter, {const: "q4"}]}
  - id: asset.qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}
  - id: asset.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: asset.h_year1
    printed: "(helper)"
    label: "First recovery year"
    type: Count
    expr: {op: param, ref: sc.year1}
  - id: asset.h_after_s179
    printed: "(helper)"
    label: "Basis after the 2025 section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.s179_2025}
  - id: asset.h_after_prior179
    printed: "(helper)"
    label: "Basis after the prior-year section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.prior_179}
  - id: asset.h_basis_prior
    printed: "(helper)"
    label: "Basis after prior-year section 179 and special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after_prior179, take: asset.prior_bonus}
  - id: asset.h_bonus_total
    printed: "(helper)"
    label: "Special depreciation allowance included in the current-year basis"
    type: NonNegDollars
    expr: {op: sum, of: [asset.bonus, asset.f25]}
  - id: asset.h_basis_after_bonus
    printed: "(helper)"
    label: "Basis after the section 179 expense deduction and special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after_s179, take: asset.h_bonus_total}
  - id: asset.h_bonus_full
    printed: "(helper)"
    label: "Special depreciation allowance at 100%"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_after_s179}
  - id: asset.h_bonus_forty
    printed: "(helper)"
    label: "Special depreciation allowance at 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after_s179, rate: {param: sc.bonus_rate_40}}
  - id: asset.h_bonus_fullcase
    printed: "(helper)"
    label: "Special depreciation allowance for a full election"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.after_jan19, then: asset.h_bonus_full}, {guard: {op: test, eq: [asset.after_jan19, {const: false}]}, then: asset.h_bonus_forty}]}
    note: "The archived text allows 100% only for property acquired after January 19, 2025; for an earlier acquisition in the applicable 2017-2025 window the allowance is 40%, so the full choice resolves to 40% when after_jan19 is false."
  - id: asset.h_bonus_current
    printed: "(helper)"
    label: "Current-year special depreciation allowance before line placement"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [asset.bonus_choice, {const: "full"}]}, then: asset.h_bonus_fullcase}, {guard: {op: test, eq: [asset.bonus_choice, {const: "forty"}]}, then: asset.h_bonus_forty}, {guard: {op: test, eq: [asset.bonus_choice, {const: "none"}]}, then: asset.h_zero}]}
  - id: asset.mqbase
    printed: "(helper)"
    label: "Depreciable basis for the mid-quarter convention test"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.is2025, then: asset.h_after_s179}, {guard: {op: test, eq: [asset.is2025, {const: false}]}, then: asset.h_zero}]}
  - id: asset.h_mq_threshold
    printed: "(helper)"
    label: "40% of the total depreciable basis placed in service in 2025"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.mq_total, rate: {param: sc.bonus_rate_40}}
  - id: asset.h_midquarter
    printed: "(helper)"
    label: "Mid-quarter convention applies"
    type: Bool
    expr: {op: test, gt: [sc.mq_q4, asset.h_mq_threshold]}
  - id: asset.rate_hy
    printed: "(helper)"
    label: "MACRS rate using the half-year convention for the first recovery year"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year1]}
  - id: asset.rate_mq
    printed: "(helper)"
    label: "MACRS rate using the mid-quarter convention for the first recovery year"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.qconv, asset.h_year1]}
  - id: asset.h_current_hy
    printed: "(helper)"
    label: "Current-year MACRS depreciation using the half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_after_bonus, rate: asset.rate_hy}
  - id: asset.h_current_mq
    printed: "(helper)"
    label: "Current-year MACRS depreciation using the mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_after_bonus, rate: asset.rate_mq}
  - id: asset.h_current_dep
    printed: "(helper)"
    label: "Current-year MACRS depreciation under the applicable convention"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.h_midquarter, then: asset.h_current_mq}, {guard: {op: test, eq: [asset.h_midquarter, {const: false}]}, then: asset.h_current_hy}]}
  - id: asset.year
    printed: "(helper)"
    label: "Recovery year in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.last
    printed: "(helper)"
    label: "Last year of recovery"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}
  - id: asset.done
    printed: "(helper)"
    label: "Recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [asset.year, asset.last]}
  - id: asset.h_done_false
    printed: "(helper)"
    label: "Recovery period has not ended before 2025"
    type: Bool
    expr: {op: test, eq: [asset.done, {const: false}]}
  - id: asset.rate_prior
    printed: "(helper)"
    label: "MACRS rate for a prior-year asset in 2025"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.year]}
  - id: asset.macrs_prior_live
    printed: "(helper)"
    label: "Current-year MACRS depreciation for a prior-year asset"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_prior, rate: asset.rate_prior}
```
