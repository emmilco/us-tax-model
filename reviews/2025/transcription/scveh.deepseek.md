# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 0487c576caac5f65483e554cb86521cd068bd0947d13b4a712b73796767ce13c |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | ac5ee9848d8a3b1556dbba6398f1debf9bbf2558eb575b6044648fbeb5132edc |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 55812896d927256ba9c411debba4b3892548772c0dbf99c208b83ba573413953 |
| printed lines compared | 21 |
| agree / disagree / missing | 0 / 21 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 31, 34, 37, 41, 59, 60, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 31, 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- scveh.scveh.bus_cost: part 'scveh.miles_business' is not money
- scveh.scveh.bus_cost: whole operand is not money
- scveh.scveh.h_operating_business: part 'scveh.miles_business' is not money
- scveh.scveh.h_operating_business: whole operand is not money
- scveh.scveh.h_lease_business: part 'scveh.miles_business' is not money
- scveh.scveh.h_lease_business: whole operand is not money
- scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money
- scveh.scveh.h_adjusted_max_passenger: whole operand is not money

## Lines

### scveh.bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "25"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "25"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "20"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### scveh.s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "10"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "13"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"line": "44a"}, "places": 3, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.h_operating_business", "message": "scveh.scveh.h_operating_business: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_operating_business", "message": "scveh.scveh.h_operating_business: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"line": "44a"}, "places": 3, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.h_lease_business", "message": "scveh.scveh.h_lease_business: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_lease_business", "message": "scveh.scveh.h_lease_business: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 13 — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"expression": {"amount": {"line": "(d)"}, "op": "prorate", "part": {"line": "44a"}, "places": 3, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}]}
```

Second transcription's note: The worksheet does not state a rounding for the business/investment-use percentage; the ratio of business miles to total miles is rounded to three decimal places.

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}]}
```

Second transcription's note: For a vehicle not subject to the passenger-automobile limits, no table limit applies; the maximum is taken as the business/investment cost.

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"amount": {"line": "7"}, "op": "prorate", "part": {"line": "44a"}, "places": 3, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project:

```json
{"from": {"line": "9 (scveh.line9w)"}, "op": "subtract_floor0", "take": {"line": "10"}}
```

Second:

```json
{"expression": {"from": {"line": "9 (scveh.line9w)"}, "op": "subtract_floor0", "take": {"line": "10"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_179"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_179"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"expression": {"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "14"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 16 — Special depreciation allowance
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "11"}, "op": "subtract_floor0", "take": {"line": "16"}}
```

Second:

```json
{"expression": {"from": {"line": "11"}, "op": "subtract_floor0", "take": {"line": "25"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "16"}}
```

Second:

```json
{"expression": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "25"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Second transcription's note: After the recovery period ends, the worksheet’s rate-table method no longer determines the unrecovered-basis deduction; the supplied inputs do not provide the prior-year allowed depreciation needed for that case.

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_adjusted_max_passenger", "message": "scveh.scveh.h_adjusted_max_passenger: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.h_operating_business, scveh.h_lease_business and scveh.h_adjusted_max_passenger prorate by mile counts as money ("part 'scveh.miles_business' is not money"), and this line depends on one of them, so it was not executed. This adjudicates the declaration, not the tax reading. executable-triage-v2 (reviews/2025/transcription/triage/scveh.deepseek.json, rerun today): candidate-invalid on all 321 records.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.h_bonus_mixed, scveh.screen | scveh.h_bonus_mixed, scveh.screen |
| scveh.macrs | scveh.h_bonus_mixed, scveh.screen | scveh.h_bonus_mixed, scveh.screen |
| scveh.s179_2025 | scveh.screen | scveh.screen |
| scveh.mq_q4 | scveh.screen | scveh.screen |
| scveh.mq_total | scveh.screen | scveh.screen |
| scveh.cost179 | scveh.screen | scveh.screen |
| 9 (scveh.line9) | scveh.h_actual_lease_bad, scveh.h_std_bad, scveh.screen | scveh.h_actual_lease_bad, scveh.h_std_bad, scveh.screen |
| 20a | scveh.h_actual_lease_bad, scveh.screen | scveh.h_actual_lease_bad, scveh.screen |
| 13 | scveh.screen | scveh.screen |
| 7 | scveh.screen | scveh.screen |
| 9 (scveh.line9w) | scveh.screen | scveh.screen |
| 10 | scveh.screen | scveh.screen |
| 11 | scveh.screen | scveh.screen |
| 14 | scveh.screen | scveh.screen |
| 15 | scveh.screen | scveh.screen |
| 16 | scveh.h_bonus_mixed, scveh.screen | scveh.h_bonus_mixed, scveh.screen |
| 25 | scveh.h_bonus_mixed, scveh.screen | scveh.h_bonus_mixed, scveh.screen |
| 17 | scveh.h_bonus_mixed, scveh.screen | scveh.h_bonus_mixed, scveh.screen |
| 18 | scveh.h_bonus_mixed, scveh.screen | scveh.h_bonus_mixed, scveh.screen |
| 19 | scveh.h_bonus_mixed, scveh.screen | scveh.h_bonus_mixed, scveh.screen |
| 20 | scveh.h_bonus_mixed, scveh.screen | scveh.h_bonus_mixed, scveh.screen |

## Raw second transcription

```yaml
lines:
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.method, {const: "standard"}]}
          then: scveh.h_standard_line9
        - guard: {op: test, eq: [scveh.method, {const: "actual"}]}
          then: scveh.h_actual_line9
    refuses: [scveh.screen, scveh.h_std_bad, scveh.h_actual_lease_bad]
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.method, {const: "standard"}]}
          then: scveh.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.method, {const: "actual"}]}
              - {op: test, eq: [scveh.owned, {const: true}]}
          then: scveh.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.method, {const: "actual"}]}
              - {op: test, eq: [scveh.owned, {const: false}]}
          then: scveh.h_lease_business
    refuses: [scveh.screen, scveh.h_actual_lease_bad]
  - id: scveh.bus_cost
    printed: "13"
    label: "Business/investment cost (cost or other basis × business/investment-use percentage)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.miles_business, whole: scveh.h_total_miles, places: 3}
    refuses: [scveh.screen]
    note: "The worksheet does not state a rounding for the business/investment-use percentage; the ratio of business miles to total miles is rounded to three decimal places."
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.passenger, {const: true}]}
          then: scveh.h_line7_passenger
        - guard: {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.bus_cost
    refuses: [scveh.screen]
    note: "For a vehicle not subject to the passenger-automobile limits, no table limit applies; the maximum is taken as the business/investment cost."
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Adjusted maximum depreciation deduction (line 7 × business/investment-use percentage)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.passenger, {const: true}]}
          then: scveh.h_adjusted_max_passenger
        - guard: {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.bus_cost
    refuses: [scveh.screen]
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.owned, {const: true}]}
          then: scveh.h_min_179
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [scveh.placed, {const: "y2025"}]}
                - {op: test, eq: [scveh.owned, {const: true}]}
          then: scveh.h_zero
    refuses: [scveh.screen]
  - id: scveh.line11
    printed: "11"
    label: "Limit on the amount you can deduct for depreciation (including any special depreciation allowance) (line 9 minus line 10)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line9w, take: scveh.line10}
    refuses: [scveh.screen]
  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.placed, {const: "y2025"}]}
          then: scveh.line10
        - guard: {op: test, not: {op: test, eq: [scveh.placed, {const: "y2025"}]}}
          then: scveh.prior_179
    refuses: [scveh.screen]
  - id: scveh.line15
    printed: "15"
    label: "Tentative basis for depreciation (line 13 minus line 14)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.bus_cost, take: scveh.line14}
    refuses: [scveh.screen]
  - id: scveh.line16
    printed: "16"
    label: "Special depreciation allowance (line 15 × applicable percentage, if applicable)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.owned, {const: true}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
          then: scveh.line15
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.owned, {const: true}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "forty"}]}
          then: scveh.h_bonus_forty
        - guard:
            op: test
            not:
              op: test
              any:
                - op: test
                  all:
                    - {op: test, eq: [scveh.placed, {const: "y2025"}]}
                    - {op: test, eq: [scveh.owned, {const: true}]}
                    - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
                - op: test
                  all:
                    - {op: test, eq: [scveh.placed, {const: "y2025"}]}
                    - {op: test, eq: [scveh.owned, {const: true}]}
                    - {op: test, eq: [scveh.bonus_choice, {const: "forty"}]}
          then: scveh.h_zero
    refuses: [scveh.screen, scveh.h_bonus_mixed]
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Total special depreciation allowance for qualified listed property"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line16, scveh.line11]}
    refuses: [scveh.screen]
  - id: scveh.line17
    printed: "17"
    label: "Limit on the amount you can deduct for MACRS depreciation (line 11 minus line 25)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line11, take: scveh.bonus_allowed}
    refuses: [scveh.screen]
  - id: scveh.line18
    printed: "18"
    label: "Basis for depreciation (line 15 minus line 25)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line15, take: scveh.bonus_allowed}
    refuses: [scveh.screen]
  - id: scveh.line19
    printed: "19"
    label: "Tentative MACRS depreciation deduction (line 18 × depreciation rate)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_macrs_rate}
    refuses: [scveh.screen]
    note: "After the recovery period ends, the worksheet’s rate-table method no longer determines the unrecovered-basis deduction; the supplied inputs do not provide the prior-year allowed depreciation needed for that case."
  - id: scveh.line20
    printed: "20"
    label: "MACRS depreciation deduction (lesser of line 17 or line 19)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}
    refuses: [scveh.screen]
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: scveh.h_total_miles
    printed: "(helper)"
    label: "Total miles driven in 2025"
    type: Count
    expr: {op: sum, of: [scveh.miles_business, scveh.miles_commuting, scveh.miles_other]}
  - id: scveh.h_mileage_rate
    printed: "(helper)"
    label: "2025 business standard mileage rate"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}
  - id: scveh.h_mileage_amount
    printed: "(helper)"
    label: "Business miles × standard mileage rate"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_mileage_rate, count: scveh.miles_business}
  - id: scveh.h_standard_line9
    printed: "(helper)"
    label: "Standard mileage amount plus parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_mileage_amount, scveh.parking]}
  - id: scveh.h_operating_business
    printed: "(helper)"
    label: "Business portion of operating expenses"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.miles_business, whole: scveh.h_total_miles, places: 3}
  - id: scveh.h_actual_line9
    printed: "(helper)"
    label: "Actual expenses business portion plus parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_operating_business, scveh.parking]}
  - id: scveh.h_lease_business
    printed: "(helper)"
    label: "Business portion of lease payments"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.miles_business, whole: scveh.h_total_miles, places: 3}
  - id: scveh.h_recovery_year
    printed: "(helper)"
    label: "Year of recovery in 2025 by year placed in service"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [scveh.placed]}
  - id: scveh.h_period
    printed: "(helper)"
    label: "MACRS recovery period for the vehicle"
    type: Enum(macrs_period)
    expr: {op: param, ref: sc.period_y5}
  - id: scveh.h_limit_table
    printed: "(helper)"
    label: "Passenger automobile limit from the applicable table"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_recovery_year]}
  - id: scveh.h_limit_nobonus
    printed: "(helper)"
    label: "First-year passenger automobile limit without the special depreciation allowance"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit_first_nobonus, keys: [scveh.placed]}
  - id: scveh.h_line7_passenger
    printed: "(helper)"
    label: "Passenger automobile maximum depreciation deduction for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "none"}]}
          then: scveh.h_limit_nobonus
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [scveh.placed, {const: "y2025"}]}
                - {op: test, eq: [scveh.bonus_choice, {const: "none"}]}
          then: scveh.h_limit_table
  - id: scveh.h_adjusted_max_passenger
    printed: "(helper)"
    label: "Passenger automobile limit adjusted for business/investment use"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.miles_business, whole: scveh.h_total_miles, places: 3}
  - id: scveh.h_suv_limit
    printed: "(helper)"
    label: "Section 179 dollar limit for SUVs and certain other vehicles"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_s179_after_suv
    printed: "(helper)"
    label: "Section 179 elected amount after the SUV limit, if applicable"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.suv, {const: true}]}
          then: scveh.h_min_suv
        - guard: {op: test, eq: [scveh.suv, {const: false}]}
          then: scveh.s179_elect
  - id: scveh.h_min_suv
    printed: "(helper)"
    label: "Smaller of elected section 179 cost or SUV limit"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.h_suv_limit]}
  - id: scveh.h_min_179
    printed: "(helper)"
    label: "Section 179 amount not more than line 9"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_s179_after_suv, scveh.line9w]}
  - id: scveh.h_bonus_forty
    printed: "(helper)"
    label: "40% special depreciation allowance on the tentative basis"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}
  - id: scveh.h_macrs_rate
    printed: "(helper)"
    label: "MACRS GDS rate for 5-year property, convention, and recovery year"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_recovery_year]}
  - id: scveh.h_std_bad
    printed: "(helper)"
    label: "Standard mileage rate not available for this vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "standard"}]}
        - {op: test, eq: [scveh.smr_ok, {const: false}]}
  - id: scveh.h_actual_lease_bad
    printed: "(helper)"
    label: "Actual expenses not available for a leased vehicle previously using the standard mileage rate"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: false}]}
        - {op: test, eq: [scveh.lease_smr_before, {const: true}]}
  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "The special depreciation allowance choice is not the same for all 5-year property"
    type: Bool
    expr: {op: test, eq: [scveh.bonus_same, {const: false}]}
  - id: scveh.bonus
    printed: "(helper)"
    label: "Special depreciation allowance for this vehicle"
    type: NonNegDollars
    expr: {op: copy, from: scveh.bonus_allowed}
  - id: scveh.macrs
    printed: "(helper)"
    label: "MACRS depreciation for this vehicle"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line20}
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Section 179 deduction claimed for this vehicle for 2025"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line10}
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Basis of this vehicle placed in service in the fourth quarter of 2025, for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.quarter, {const: "q4"}]}
          then: scveh.line15
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [scveh.placed, {const: "y2025"}]}
                - {op: test, eq: [scveh.quarter, {const: "q4"}]}
          then: scveh.h_zero
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Basis of this vehicle placed in service in 2025, for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.placed, {const: "y2025"}]}
          then: scveh.line15
        - guard: {op: test, not: {op: test, eq: [scveh.placed, {const: "y2025"}]}}
          then: scveh.h_zero
  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.owned, {const: true}]}
          then: scveh.bus_cost
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [scveh.placed, {const: "y2025"}]}
                - {op: test, eq: [scveh.owned, {const: true}]}
          then: scveh.h_zero
```
