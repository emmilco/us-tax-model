# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | de71694a147c7c3bc8ba666607b076bfb703eabaad271690f98b5bea0cc887ea |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 6deb4487b305cf04a895b4d5d1c409dea71aa25ee079693d1d895f2518ba16a5 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 103e55b3bcbc53d0e7997d1a372e081370d4d144fc6e7d0b6e75adb1b119f82e |
| printed lines compared | 21 |
| agree / disagree / missing | 0 / 21 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- scveh.scveh.bus_cost: part 'scveh.miles_business' is not money
- scveh.scveh.bus_cost: whole operand is not money
- scveh.scveh.line9w: part 'scveh.miles_business' is not money
- scveh.scveh.line9w: whole operand is not money
- scveh.scveh.h_operating_bus: part 'scveh.miles_business' is not money
- scveh.scveh.h_operating_bus: whole operand is not money
- scveh.scveh.h_lease_bus: part 'scveh.miles_business' is not money
- scveh.scveh.h_lease_bus: whole operand is not money

## Lines

### scveh.bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "25"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "16"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "20"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### scveh.s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "10"}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "13"}}, {"guard": {"args": [{"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"line": "44a"}, "places": 9, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.h_operating_bus", "message": "scveh.scveh.h_operating_bus: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_operating_bus", "message": "scveh.scveh.h_operating_bus: whole operand is not money"}]}
```

Second transcription's note: For actual expenses, applies the business-mileage fraction to operating expenses and adds business parking/tolls; standard uses 70 cents per business mile plus parking/tolls. A standard-mileage method is refused when scveh.smr_ok is false.

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"line": "44a"}, "places": 9, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.h_lease_bus", "message": "scveh.scveh.h_lease_bus: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_lease_bus", "message": "scveh.scveh.h_lease_bus: whole operand is not money"}]}
```

Second transcription's note: Lease payments are deducted for actual expenses only and only when the vehicle is not owned.

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### 13 — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"expression": {"amount": {"line": "(d)"}, "op": "prorate", "part": {"line": "44a"}, "places": 9, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}]}
```

Second transcription's note: Business-use percentage is business miles divided by total miles (business + commuting + other), rounded to 9 decimal places.

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(d)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 1, "type": "Count"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 1, "type": "Count"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 1, "type": "Count"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "ne"}], "test": "any"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: For a non-passenger vehicle not subject to passenger automobile limits, cost is used as a nonbinding maximum. For a passenger automobile, the first-year no-special-allowance limit is used when no special allowance applies; later-year limits use auto_limit.

Ruling: representation; line 7 is a worksheet line for passenger automobiles, figured for every vehicle and read only on the scveh.passenger branches; the project-side refusals are standard-mileage vehicles where the line is not read. Triage executable-triage-v2 (triage/scveh.deepseek.json): 2290 of 3685 comparisons agree; on completed returns {"candidate-unknown": 16, "project-refuses": 134, "project-unknown": 21, "value": 72}.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"expression": {"amount": {"line": "7"}, "op": "prorate", "part": {"line": "44a"}, "places": 9, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Second transcription's note: Section 179 is zero unless actual expenses are used and the vehicle was placed in service in 2025; an SUV election is limited to $31,300.

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

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

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

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

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

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

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### 16 — Special depreciation allowance
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Second transcription's note: For property acquired before January 20, 2025, the applicable special allowance is 40%, not 100%.

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

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

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

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

Second transcription's note: Uses the allowed special allowance on line 25, capped at line 11, so the passenger automobile limit is not exceeded.

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

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

Second transcription's note: Uses the allowed special allowance on line 25.

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; scveh.bus_cost, scveh.line9w, scveh.h_operating_bus and scveh.h_lease_bus prorate by miles as money ("part 'scveh.miles_business' is not money"), so the line or its dependency closure was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/scveh.deepseek.json): candidate-invalid on all 3685 records; this adjudicates the declaration, not the tax reading.

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
| 9 (scveh.line9) | scveh.h_smr_bad, scveh.screen | scveh.h_smr_bad, scveh.screen |
| 20a | scveh.screen | scveh.screen |
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
    label: "Car and truck expenses."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.method, {const: "standard"}]
          then: scveh.h_standard_amount
        - guard:
            op: test
            eq: [scveh.method, {const: "actual"}]
          then: scveh.h_actual_amount
    refuses: [scveh.screen, scveh.h_smr_bad]
    note: "For actual expenses, applies the business-mileage fraction to operating expenses and adds business parking/tolls; standard uses 70 cents per business mile plus parking/tolls. A standard-mileage method is refused when scveh.smr_ok is false."
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.method, {const: "actual"}]
              - op: test
                eq: [scveh.owned, {const: false}]
          then: scveh.h_lease_bus
        - guard:
            op: test
            any:
              - op: test
                eq: [scveh.method, {const: "standard"}]
              - op: test
                eq: [scveh.owned, {const: true}]
          then: scveh.h_zero
    refuses: [scveh.screen]
    note: "Lease payments are deducted for actual expenses only and only when the vehicle is not owned."
  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost."
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.cost
      part: scveh.miles_business
      whole: scveh.h_total_miles
      places: 9
    refuses: [scveh.screen]
    note: "Business-use percentage is business miles divided by total miles (business + commuting + other), rounded to 9 decimal places."
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.passenger, {const: true}]
          then: scveh.h_passenger_limit
        - guard:
            op: test
            eq: [scveh.passenger, {const: false}]
          then: scveh.cost
    refuses: [scveh.screen]
    note: "For a non-passenger vehicle not subject to passenger automobile limits, cost is used as a nonbinding maximum. For a passenger automobile, the first-year no-special-allowance limit is used when no special allowance applies; later-year limits use auto_limit."
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction."
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.line7
      part: scveh.miles_business
      whole: scveh.h_total_miles
      places: 9
    refuses: [scveh.screen]
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.method, {const: "actual"}]
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
          then: scveh.h_s179_possible
        - guard:
            op: test
            any:
              - op: test
                eq: [scveh.method, {const: "standard"}]
              - op: test
                ne: [scveh.placed, {const: "y2025"}]
          then: scveh.h_zero
    refuses: [scveh.screen]
    note: "Section 179 is zero unless actual expenses are used and the vehicle was placed in service in 2025; an SUV election is limited to $31,300."
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
            ne: [scveh.placed, {const: "y2025"}]
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
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. This is your special depreciation allowance."
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
                eq: [scveh.bonus_choice, {const: "none"}]
          then: scveh.h_zero
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.bonus_choice, {const: "forty"}]
          then: scveh.h_bonus_forty
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.bonus_choice, {const: "full"}]
              - op: test
                eq: [scveh.after_jan19, {const: true}]
          then: scveh.h_bonus_full
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.bonus_choice, {const: "full"}]
              - op: test
                eq: [scveh.after_jan19, {const: false}]
          then: scveh.h_bonus_forty
        - guard:
            op: test
            ne: [scveh.placed, {const: "y2025"}]
          then: scveh.h_zero
    refuses: [scveh.h_bonus_mixed, scveh.screen]
    note: "For property acquired before January 20, 2025, the applicable special allowance is 40%, not 100%."
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Special depreciation allowance for listed property. Enter on line 25 your total special depreciation allowance for all qualified listed property."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [scveh.line16, scveh.line11]
    refuses: [scveh.screen]
  - id: scveh.line17
    printed: "17"
    label: "Subtract line 16 from line 11. This is the limit on the amount you can deduct for MACRS depreciation."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: scveh.line11
      take: scveh.bonus_allowed
    refuses: [scveh.screen]
    note: "Uses the allowed special allowance on line 25, capped at line 11, so the passenger automobile limit is not exceeded."
  - id: scveh.line18
    printed: "18"
    label: "Subtract line 16 from line 15. This is your basis for depreciation."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: scveh.line15
      take: scveh.bonus_allowed
    refuses: [scveh.screen]
    note: "Uses the allowed special allowance on line 25."
  - id: scveh.line19
    printed: "19"
    label: "Multiply line 18 by line 6. This is your tentative MACRS depreciation deduction."
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: scveh.line18
      rate: scveh.h_macrs_rate
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
    label: "Special depreciation allowance before the passenger automobile limit."
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.line16
  - id: scveh.macrs
    printed: "(helper)"
    label: "MACRS depreciation deduction for the vehicle."
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.line20
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Section 179 deduction claimed for this vehicle for 2025."
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.line10
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Business cost for the fourth-quarter mid-quarter test."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.method, {const: "actual"}]
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
              - op: test
                eq: [scveh.quarter, {const: "q4"}]
          then: scveh.line15
        - guard:
            op: test
            any:
              - op: test
                eq: [scveh.method, {const: "standard"}]
              - op: test
                ne: [scveh.placed, {const: "y2025"}]
              - op: test
                ne: [scveh.quarter, {const: "q4"}]
          then: scveh.h_zero
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Business cost for the mid-quarter test."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.method, {const: "actual"}]
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
          then: scveh.line15
        - guard:
            op: test
            any:
              - op: test
                eq: [scveh.method, {const: "standard"}]
              - op: test
                ne: [scveh.placed, {const: "y2025"}]
          then: scveh.h_zero
  - id: scveh.cost179
    printed: "(helper)"
    label: "Business cost of section 179 property placed in service in 2025."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.method, {const: "actual"}]
              - op: test
                eq: [scveh.placed, {const: "y2025"}]
          then: scveh.bus_cost
        - guard:
            op: test
            any:
              - op: test
                eq: [scveh.method, {const: "standard"}]
              - op: test
                ne: [scveh.placed, {const: "y2025"}]
          then: scveh.h_zero

  - id: scveh.h_total_miles
    printed: "(helper)"
    label: "Total 2025 miles for the vehicle."
    type: Count
    expr:
      op: sum
      of: [scveh.miles_business, scveh.miles_commuting, scveh.miles_other]
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero amount."
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
  - id: scveh.h_mileage_rate
    printed: "(helper)"
    label: "2025 business standard mileage rate."
    type: NonNegDollars
    expr:
      op: param
      ref: sc.mileage_rate
  - id: scveh.h_mileage_amount
    printed: "(helper)"
    label: "Business miles times the standard mileage rate."
    type: NonNegDollars
    expr:
      op: multiply_count
      amount: scveh.h_mileage_rate
      count: scveh.miles_business
  - id: scveh.h_standard_amount
    printed: "(helper)"
    label: "Standard mileage amount plus parking and tolls."
    type: NonNegDollars
    expr:
      op: sum
      of: [scveh.h_mileage_amount, scveh.parking]
  - id: scveh.h_operating_bus
    printed: "(helper)"
    label: "Business portion of operating expenses."
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.operating
      part: scveh.miles_business
      whole: scveh.h_total_miles
      places: 9
  - id: scveh.h_actual_amount
    printed: "(helper)"
    label: "Actual operating expenses plus parking and tolls."
    type: NonNegDollars
    expr:
      op: sum
      of: [scveh.h_operating_bus, scveh.parking]
  - id: scveh.h_lease_bus
    printed: "(helper)"
    label: "Business portion of lease payments."
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.lease
      part: scveh.miles_business
      whole: scveh.h_total_miles
      places: 9
  - id: scveh.h_rec_year
    printed: "(helper)"
    label: "Year of recovery in 2025."
    type: Count
    expr:
      op: keyed_lookup
      table: recovery_year
      keys: [scveh.placed]
  - id: scveh.h_period
    printed: "(helper)"
    label: "MACRS recovery period."
    type: Enum(macrs_period)
    expr:
      op: param
      ref: sc.period_y5
  - id: scveh.h_conv
    printed: "(helper)"
    label: "MACRS convention for the vehicle."
    type: Enum(macrs_convention)
    expr:
      op: copy
      from: scveh.prior_conv
  - id: scveh.h_macrs_rate
    printed: "(helper)"
    label: "MACRS depreciation rate for the vehicle."
    type: Rate
    expr:
      op: keyed_lookup
      table: macrs_gds
      keys: [scveh.h_period, scveh.h_conv, scveh.h_rec_year]
  - id: scveh.h_limit_std
    printed: "(helper)"
    label: "Passenger automobile limit from the standard table."
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: auto_limit
      keys: [scveh.placed, scveh.h_rec_year]
  - id: scveh.h_limit_nobonus
    printed: "(helper)"
    label: "First-year passenger automobile limit without the special depreciation allowance."
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: auto_limit_first_nobonus
      keys: [scveh.placed]
  - id: scveh.h_special_applies
    printed: "(helper)"
    label: "Whether a special depreciation allowance applies for 2025."
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [scveh.placed, {const: "y2025"}]
        - op: test
          ne: [scveh.bonus_choice, {const: "none"}]
  - id: scveh.h_passenger_limit
    printed: "(helper)"
    label: "Passenger automobile limit for the current recovery year."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.h_rec_year, {const: 1, type: Count}]
              - op: test
                eq: [scveh.h_special_applies, {const: false}]
          then: scveh.h_limit_nobonus
        - guard:
            op: test
            all:
              - op: test
                eq: [scveh.h_rec_year, {const: 1, type: Count}]
              - op: test
                eq: [scveh.h_special_applies, {const: true}]
          then: scveh.h_limit_std
        - guard:
            op: test
            ne: [scveh.h_rec_year, {const: 1, type: Count}]
          then: scveh.h_limit_std
  - id: scveh.h_suv_limit
    printed: "(helper)"
    label: "Section 179 limit for SUVs and certain other vehicles."
    type: NonNegDollars
    expr:
      op: param
      ref: s179.suv_limit
  - id: scveh.h_suv_cap
    printed: "(helper)"
    label: "Section 179 elected amount limited by the SUV limit."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [scveh.s179_elect, scveh.h_suv_limit]
  - id: scveh.h_s179_cap
    printed: "(helper)"
    label: "Section 179 cap before the line 9 limit."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [scveh.suv, {const: true}]
          then: scveh.h_suv_cap
        - guard:
            op: test
            eq: [scveh.suv, {const: false}]
          then: scveh.s179_elect
  - id: scveh.h_s179_possible
    printed: "(helper)"
    label: "Section 179 amount not more than line 9."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [scveh.h_s179_cap, scveh.line9w]
  - id: scveh.h_smr_bad
    printed: "(helper)"
    label: "Standard mileage rate is not allowed for this vehicle."
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [scveh.method, {const: "standard"}]
        - op: test
          eq: [scveh.smr_ok, {const: false}]
  - id: scveh.h_bonus_full
    printed: "(helper)"
    label: "Special depreciation allowance at 100%."
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.line15
  - id: scveh.h_bonus_forty
    printed: "(helper)"
    label: "Special depreciation allowance at 40%."
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: scveh.line15
      rate: {param: sc.bonus_rate_40}
  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "Special depreciation choice is not the same for all 5-year property placed in service in 2025."
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [scveh.placed, {const: "y2025"}]
        - op: test
          ne: [scveh.bonus_choice, {const: "none"}]
        - op: test
          eq: [scveh.bonus_same, {const: false}]
```
