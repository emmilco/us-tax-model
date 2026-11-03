# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5254fc31a17eb3c41ce003fdee716fa102b2cbe662ce1a1e7a70b98cd36bd08e |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | f1af0533c5c8927cf21ba8b2dd2e7d060f1e6b01f1817d198ef9494ca9fa4ab5 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 21ed42ae791e3370832f9db89dc59af7b9c11eac73013dc57226b7d810990087 |
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
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 60, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- model changed a published result type
- scveh.scveh.bus_cost: part 'scveh.miles_business' is not money
- scveh.scveh.bus_cost: whole operand is not money
- scveh.scveh.line9w: part 'scveh.miles_business' is not money
- scveh.scveh.line9w: whole operand is not money
- scveh.scveh.operating_business: part 'scveh.miles_business' is not money
- scveh.scveh.operating_business: whole operand is not money
- scveh.scveh.lease_actual: part 'scveh.miles_business' is not money
- scveh.scveh.lease_actual: whole operand is not money

## Lines

### scveh.bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "25"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"line": "25"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"line": "20"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.rate", "message": "model changed a published result type"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### scveh.s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "13"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"line": "44a"}, "places": 3, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.operating_business", "message": "scveh.scveh.operating_business: part 'scveh.miles_business' is not money"}, {"line": "scveh.operating_business", "message": "scveh.scveh.operating_business: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"line": "44a"}, "places": 3, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.lease_actual", "message": "scveh.scveh.lease_actual: part 'scveh.miles_business' is not money"}, {"line": "scveh.lease_actual", "message": "scveh.scveh.lease_actual: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

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

Second transcription's note: The IRS worksheet states the business/investment use percentage but does not state a rounding precision; this model rounds the mileage ratio to three decimal places.

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(d)"}}], "op": "choose"}
```

Ruling: model error; its amounts differ from the project on completed returns, where the Claude transcription, read independently, differs only through recorded ambiguities or read gates, so the weight of the readings is against this candidate. Triage executable-triage-v2 (triage/scveh.deepseek.json): 1618 of 2551 comparisons agree; on completed returns {"candidate-unknown": 15, "project-refuses": 41, "project-unknown": 12, "value": 69}.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"expression": {"amount": {"line": "7"}, "op": "prorate", "part": {"line": "44a"}, "places": 3, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Second transcription's note: The IRS worksheet states the business/investment use percentage but does not state a rounding precision; this model rounds the mileage ratio to three decimal places.

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"param": "s179.suv_limit"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project:

```json
{"from": {"line": "9 (scveh.line9w)"}, "op": "subtract_floor0", "take": {"line": "10"}}
```

Second:

```json
{"expression": {"from": {"line": "9 (scveh.line9w)"}, "op": "subtract_floor0", "take": {"line": "10"}}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_179"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_179"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"expression": {"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "14"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 16 — Special depreciation allowance
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "11"}, "op": "subtract_floor0", "take": {"line": "16"}}
```

Second:

```json
{"expression": {"from": {"line": "11"}, "op": "subtract_floor0", "take": {"line": "25"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Second transcription's note: The worksheet says to subtract line 16; the special depreciation allowance allowed is capped by line 11 and reported on line 25, so the capped amount is subtracted.

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "16"}}
```

Second:

```json
{"expression": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "25"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Second transcription's note: The worksheet says to subtract line 16; the special depreciation allowance allowed is capped by line 11 and reported on line 25, so the capped amount is subtracted.

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}, "invalid_model_types": [{"line": "scveh.rate", "message": "model changed a published result type"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.rate", "message": "model changed a published result type"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 2551 records; this adjudicates the declaration, not the tax reading.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen |
| scveh.macrs | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen |
| scveh.s179_2025 | scveh.screen | scveh.screen |
| scveh.mq_q4 | scveh.screen | scveh.screen |
| scveh.mq_total | scveh.screen | scveh.screen |
| scveh.cost179 | scveh.screen | scveh.screen |
| 9 (scveh.line9) | scveh.actual_lease_not_ok, scveh.screen, scveh.standard_not_ok | scveh.actual_lease_not_ok, scveh.screen, scveh.standard_not_ok |
| 20a | scveh.actual_lease_not_ok, scveh.screen | scveh.actual_lease_not_ok, scveh.screen |
| 13 | scveh.screen | scveh.screen |
| 7 | scveh.screen | scveh.screen |
| 9 (scveh.line9w) | scveh.screen | scveh.screen |
| 10 | scveh.screen | scveh.screen |
| 11 | scveh.screen | scveh.screen |
| 14 | scveh.screen | scveh.screen |
| 15 | scveh.screen | scveh.screen |
| 16 | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen |
| 25 | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen |
| 17 | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen |
| 18 | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen |
| 19 | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen |
| 20 | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen | scveh.bonus_bad, scveh.bonus_not_same, scveh.screen |

## Raw second transcription

```yaml
lines:
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses (see instructions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.method, {const: "standard"}]
          then: scveh.standard_total
        - guard:
            op: test
            eq: [scveh.method, {const: "actual"}]
          then: scveh.actual_total
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.method, {const: "actual"}]
          then: scveh.lease_actual
        - guard:
            op: test
            eq: [scveh.method, {const: "standard"}]
          then: scveh.zero
  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost."
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.cost
      part: scveh.miles_business
      whole: scveh.total_miles
      places: 3
    refuses: [scveh.screen]
    note: "The IRS worksheet states the business/investment use percentage but does not state a rounding precision; this model rounds the mileage ratio to three decimal places."
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.passenger, {const: false}]
          then: scveh.cost
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.passenger, {const: true}]
              - op: test
                eq: [scveh.year, {const: 1, type: Count}]
              - op: test
                eq: [scveh.bonus_choice, {const: "none"}]
          then: scveh.line7_nobonus
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.passenger, {const: true}]
              - op: test
                not:
                  op: test
                  all:
                    - op: test
                      eq: [scveh.year, {const: 1, type: Count}]
                    - op: test
                      eq: [scveh.bonus_choice, {const: "none"}]
          then: scveh.line7_limited
    refuses: [scveh.screen]
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction."
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.line7
      part: scveh.miles_business
      whole: scveh.total_miles
      places: 3
    refuses: [scveh.screen]
    note: "The IRS worksheet states the business/investment use percentage but does not state a rounding precision; this model rounds the mileage ratio to three decimal places."
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.placed, {const: "y2025"}]
          then: scveh.s179_current
        - guard:
            op: test
            not:
              op: test
              eq: [scveh.placed, {const: "y2025"}]
          then: scveh.zero
    refuses: [scveh.screen]
  - id: scveh.line11
    printed: "11"
    label: "Subtract line 10 from line 9. This is the limit on the amount you can deduct for depreciation (including any special depreciation allowance)."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: scveh.line9w
      take: scveh.line10
    refuses: [scveh.screen]
  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.placed, {const: "y2025"}]
          then: scveh.line10
        - guard:
            op: test
            not:
              op: test
              eq: [scveh.placed, {const: "y2025"}]
          then: scveh.prior_179
    refuses: [scveh.screen]
  - id: scveh.line15
    printed: "15"
    label: "Subtract line 14 from line 13. This is your tentative basis for depreciation."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: scveh.bus_cost
      take: scveh.line14
    refuses: [scveh.screen]
  - id: scveh.line16
    printed: "16"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. This is your special depreciation allowance. Enter -0- if this is not the year you placed the car in service, the car is not qualified property, or you elected not to claim a special depreciation allowance."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.bonus_choice, {const: "full"}]
          then: scveh.line15
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.bonus_choice, {const: "forty"}]
          then: scveh.bonus_forty
        - guard:
            op: test
            not:
              op: test
              any:
                - op: test
                  all:
                    - op: test
                      eq: [scveh.placed, {const: "y2025"}]
                    - op: test
                      eq: [scveh.bonus_choice, {const: "full"}]
                - op: test
                  all:
                    - op: test
                      eq: [scveh.placed, {const: "y2025"}]
                    - op: test
                      eq: [scveh.bonus_choice, {const: "forty"}]
          then: scveh.zero
    refuses: [scveh.screen, scveh.bonus_bad, scveh.bonus_not_same]
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Enter your total special depreciation allowance for all qualified listed property (Form 4562, line 25)."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [scveh.line16, scveh.line11]
    refuses: [scveh.screen, scveh.bonus_bad, scveh.bonus_not_same]
  - id: scveh.line17
    printed: "17"
    label: "Subtract the special depreciation allowance allowed from line 11. This is the limit on the amount you can deduct for MACRS depreciation."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: scveh.line11
      take: scveh.bonus_allowed
    refuses: [scveh.screen]
    note: "The worksheet says to subtract line 16; the special depreciation allowance allowed is capped by line 11 and reported on line 25, so the capped amount is subtracted."
  - id: scveh.line18
    printed: "18"
    label: "Subtract the special depreciation allowance allowed from line 15. This is your basis for depreciation."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: scveh.line15
      take: scveh.bonus_allowed
    refuses: [scveh.screen]
    note: "The worksheet says to subtract line 16; the special depreciation allowance allowed is capped by line 11 and reported on line 25, so the capped amount is subtracted."
  - id: scveh.line19
    printed: "19"
    label: "Multiply line 18 by line 6. This is your tentative MACRS depreciation deduction."
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: scveh.line18
      rate: scveh.rate
    refuses: [scveh.screen]
  - id: scveh.line20
    printed: "20"
    label: "Enter the lesser of line 17 or line 19. This is your MACRS depreciation deduction."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [scveh.line17, scveh.line19]
    refuses: [scveh.screen]
  - id: scveh.bonus
    printed: "(helper)"
    label: "Special depreciation allowance for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.method, {const: "actual"}]
          then: scveh.bonus_allowed
        - guard:
            op: test
            eq: [scveh.method, {const: "standard"}]
          then: scveh.zero
    refuses: [scveh.screen, scveh.bonus_bad, scveh.bonus_not_same]
  - id: scveh.macrs
    printed: "(helper)"
    label: "MACRS depreciation deduction for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.method, {const: "actual"}]
          then: scveh.line20
        - guard:
            op: test
            eq: [scveh.method, {const: "standard"}]
          then: scveh.zero
    refuses: [scveh.screen]
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Section 179 deduction claimed this year for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.method, {const: "actual"}]
          then: scveh.line10
        - guard:
            op: test
            eq: [scveh.method, {const: "standard"}]
          then: scveh.zero
    refuses: [scveh.screen]
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Vehicle depreciable basis placed in service in the fourth quarter for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.quarter, {const: "q4"}]
              - op: test
                eq: [scveh.method, {const: "actual"}]
          then: scveh.line15
        - guard:
            op: test
            not:
              op: test
              all:
                - op: test
                  eq: [scveh.placed, {const: "y2025"}]
                - op: test
                  eq: [scveh.quarter, {const: "q4"}]
                - op: test
                  eq: [scveh.method, {const: "actual"}]
          then: scveh.zero
    refuses: [scveh.screen]
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Vehicle depreciable basis placed in service in 2025 for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.method, {const: "actual"}]
          then: scveh.line15
        - guard:
            op: test
            not:
              op: test
              all:
                - op: test
                  eq: [scveh.placed, {const: "y2025"}]
                - op: test
                  eq: [scveh.method, {const: "actual"}]
          then: scveh.zero
    refuses: [scveh.screen]
  - id: scveh.cost179
    printed: "(helper)"
    label: "Section 179 cost of this vehicle placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.method, {const: "actual"}]
          then: scveh.bus_cost
        - guard:
            op: test
            not:
              op: test
              all:
                - op: test
                  eq: [scveh.placed, {const: "y2025"}]
                - op: test
                  eq: [scveh.method, {const: "actual"}]
          then: scveh.zero
    refuses: [scveh.screen]
  - id: scveh.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
  - id: scveh.mileage_rate
    printed: "(helper)"
    label: "Business standard mileage rate"
    type: NonNegDollars
    expr:
      op: param
      ref: sc.mileage_rate
  - id: scveh.total_miles
    printed: "(helper)"
    label: "Total miles driven in 2025"
    type: Count
    expr:
      op: sum
      of: [scveh.miles_business, scveh.miles_commuting, scveh.miles_other]
  - id: scveh.standard_miles
    printed: "(helper)"
    label: "Business miles times the standard mileage rate"
    type: NonNegDollars
    expr:
      op: multiply_count
      amount: scveh.mileage_rate
      count: scveh.miles_business
  - id: scveh.standard_total
    printed: "(helper)"
    label: "Standard mileage amount plus parking and tolls"
    type: NonNegDollars
    expr:
      op: sum
      of: [scveh.standard_miles, scveh.parking]
    refuses: [scveh.standard_not_ok]
  - id: scveh.operating_business
    printed: "(helper)"
    label: "Business portion of operating expenses"
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.operating
      part: scveh.miles_business
      whole: scveh.total_miles
      places: 3
  - id: scveh.actual_total
    printed: "(helper)"
    label: "Actual operating expenses business portion plus parking and tolls"
    type: NonNegDollars
    expr:
      op: sum
      of: [scveh.operating_business, scveh.parking]
    refuses: [scveh.screen, scveh.actual_lease_not_ok]
  - id: scveh.lease_actual
    printed: "(helper)"
    label: "Business portion of lease payments"
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.lease
      part: scveh.miles_business
      whole: scveh.total_miles
      places: 3
    refuses: [scveh.screen, scveh.actual_lease_not_ok]
  - id: scveh.standard_not_ok
    printed: "(helper)"
    label: "Standard mileage rate is selected but not permitted by the screening question"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [scveh.method, {const: "standard"}]
        - op: test
          eq: [scveh.smr_ok, {const: false}]
  - id: scveh.actual_lease_not_ok
    printed: "(helper)"
    label: "Actual expenses are selected for a leased vehicle that used the standard mileage rate in an earlier year"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [scveh.method, {const: "actual"}]
        - op: test
          eq: [scveh.owned, {const: false}]
        - op: test
          eq: [scveh.lease_smr_before, {const: true}]
  - id: scveh.year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr:
      op: keyed_lookup
      table: recovery_year
      keys: [scveh.placed]
  - id: scveh.period
    printed: "(helper)"
    label: "Recovery period for automobiles"
    type: Enum(macrs_period)
    expr:
      op: param
      ref: sc.period_y5
  - id: scveh.rate
    printed: "(helper)"
    label: "MACRS depreciation rate for this vehicle"
    type: Rate
    expr:
      op: keyed_lookup
      table: macrs_gds
      keys: [scveh.period, scveh.prior_conv, scveh.year]
  - id: scveh.line7_limited
    printed: "(helper)"
    label: "Maximum depreciation deduction with the special allowance from the table"
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: auto_limit
      keys: [scveh.placed, scveh.year]
  - id: scveh.line7_nobonus
    printed: "(helper)"
    label: "First-year maximum depreciation deduction without the special allowance"
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: auto_limit_first_nobonus
      keys: [scveh.placed]
  - id: scveh.suv_limit
    printed: "(helper)"
    label: "Section 179 limit for SUVs and certain other vehicles"
    type: NonNegDollars
    expr:
      op: param
      ref: s179.suv_limit
  - id: scveh.s179_suv_cap
    printed: "(helper)"
    label: "Section 179 elected cost after applying the SUV limit when applicable"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.suv, {const: true}]
          then: scveh.suv_limit
        - guard:
            op: test
            eq: [scveh.suv, {const: false}]
          then: scveh.s179_elect
  - id: scveh.s179_current
    printed: "(helper)"
    label: "Section 179 deduction claimed this year before the zero-for-prior-year rule"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [scveh.s179_suv_cap, scveh.line9w]
  - id: scveh.bonus_forty
    printed: "(helper)"
    label: "Special depreciation allowance at 40 percent"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: scveh.line15
      rate: {param: sc.bonus_rate_40}
  - id: scveh.bonus_bad
    printed: "(helper)"
    label: "Full special allowance was selected for property not acquired after January 19, 2025"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [scveh.bonus_choice, {const: "full"}]
        - op: test
          eq: [scveh.after_jan19, {const: false}]
  - id: scveh.bonus_not_same
    printed: "(helper)"
    label: "The special allowance choice is not the same for all 5-year property"
    type: Bool
    expr:
      op: test
      eq: [scveh.bonus_same, {const: false}]
```
