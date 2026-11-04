# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 188f739e19ea7dc521c63b15d0fde95ed4b810efe83f27d6daadeea1427e3f84 |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 34ddfdc71b3fb5a11f16519f891b0fc7a18bb3edc7571147402676b84f153868 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7c9c68d06a7816fe0aa0609dd888de0a8606da885e8a28bebd8ea4d71ead01a6 |
| printed lines compared | 21 |
| agree / disagree / missing | 0 / 21 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 17, 31, 34, 37, 41, 59, 60, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, dcprov, dependent, f1040, f2441, f4952, f5329, f8960, f8995, g28, household, qbi, refund, s1, s1a, s2, sa, sales, scope, sd, sdtw, u1250 |
| named line | ltc, s8812 |
| shared page | asset, carloan, f4562, mq, person, s179, sc |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'
- scveh.scveh.bus_cost: part 'scveh.miles_business' is not money
- scveh.scveh.bus_cost: whole operand is not money
- scveh.scveh.line9w: part 'scveh.miles_business' is not money
- scveh.scveh.line9w: whole operand is not money
- scveh.scveh.h_actual_operating: part 'scveh.miles_business' is not money
- scveh.scveh.h_actual_operating: whole operand is not money
- scveh.scveh.h_lease_business: part 'scveh.miles_business' is not money
- scveh.scveh.h_lease_business: whole operand is not money
- scveh.scveh.cost179: instance def 'undefined' does not exist
- scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity

## Lines

### scveh.bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "25"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "11"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Second transcription's note: The passenger automobile limit caps the special depreciation allowance; this uses the smaller of the computed allowance and line 11.

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "20"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### scveh.s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "10"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "10"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "10"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"unknown": "{\"of\": [\"scveh.bus_cost\", \"scveh.h_suv_limit\"], \"op\": \"smaller_of\"}"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"line": "44a"}, "places": 6, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.h_actual_operating", "message": "scveh.scveh.h_actual_operating: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_actual_operating", "message": "scveh.scveh.h_actual_operating: whole operand is not money"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"line": "44a"}, "places": 6, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.h_lease_business", "message": "scveh.scveh.h_lease_business: part 'scveh.miles_business' is not money"}, {"line": "scveh.h_lease_business", "message": "scveh.scveh.h_lease_business: whole operand is not money"}]}
```

Second transcription's note: The lease inclusion amount mentioned in the Schedule C line 20a instructions for a lease of 30 days or more is not supplied by the interface and is not applied.

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 13 — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"expression": {"amount": {"line": "(d)"}, "op": "prorate", "part": {"line": "44a"}, "places": 6, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}, "invalid_model_types": [{"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}]}
```

Second transcription's note: The business-use fraction is figured from the mileage counts and rounded to six decimal places because the model has no exact count-division atom.

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(d)"}}], "op": "choose"}
```

Ruling: model error; p946 pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 7, "Maximum depreciation deduction for this year from the appropriate table". The line executes (it depends on no invalid line). Under BUG-0398 the project shows line 7 only for an owned actual-expense passenger automobile (scveh.on_auto_limits), the vehicles the limits apply to; the candidate shows the limit for standard-mileage vehicles (classm.s8812.3.deepseek car_1 $19,800.00, generated 20) and enters the vehicle's column (d) cost for vehicles that are not passenger automobiles (stage14.veh.suv_179 $70,000.00, stage14.veh.heavy_prior and heavy_2019 trucks $60,000.00), amounts the worksheet's limit does not have; the project's visibility is right. It also needs scveh.employee_use or scveh.screen for standard-mileage vehicles (classm.f1040.6.deepseek, classm.f8863.2.deepseek, classm.eic.3.deepseek), answers the source does not need there. Triage `../triage/scveh.deepseek.json` (refresh round): 670 of 2,501 agree; on completed returns 158 candidate-unknown, 119 candidate-shows-skipped.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"expression": {"amount": {"line": "7"}, "op": "prorate", "part": {"line": "44a"}, "places": 6, "whole": {"of": [{"line": "44a"}, {"line": "44b"}, {"line": "44c"}], "op": "sum"}}, "invalid_model_types": [{"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"of": [{"line": "(i)"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"unknown": "{\"of\": [\"scveh.bus_cost\", \"scveh.h_suv_limit\"], \"op\": \"smaller_of\"}"}}], "op": "choose"}], "op": "smaller_of"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project:

```json
{"from": {"line": "9 (scveh.line9w)"}, "op": "subtract_floor0", "take": {"line": "10"}}
```

Second:

```json
{"expression": {"from": {"line": "9 (scveh.line9w)"}, "op": "subtract_floor0", "take": {"line": "10"}}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_179"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_179"}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"expression": {"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "14"}}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 16 — Special depreciation allowance
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "11"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "11"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "11"}, "op": "subtract_floor0", "take": {"line": "16"}}
```

Second:

```json
{"expression": {"from": {"line": "11"}, "op": "subtract_floor0", "take": {"line": "16"}}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "16"}}
```

Second:

```json
{"expression": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "16"}}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "scveh.cost179", "message": "malformed expression (project schema): data/alternatives/0/then must be string, data/alternatives/0/then must have required property 'def', data/alternatives/0/then must have required property 'bind'"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: part 'scveh.miles_business' is not money"}, {"line": "scveh.bus_cost", "message": "scveh.scveh.bus_cost: whole operand is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: part 'scveh.miles_business' is not money"}, {"line": "scveh.line9w", "message": "scveh.scveh.line9w: whole operand is not money"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: instance def 'undefined' does not exist"}, {"line": "scveh.cost179", "message": "scveh.scveh.cost179: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error on the declaration; the reply has validation errors: scveh.bus_cost and scveh.line9w prorate by mile counts as money ("part 'scveh.miles_business' is not money") and scveh.cost179 is malformed ("data/alternatives/0/then must be string"); this line is one of them or depends on one, so it was not executed (triage `../triage/scveh.deepseek.json`: candidate invalid, 2,501 records, 439 on completed returns). This adjudicates the declaration, not the tax reading; same as the backlog-round ruling.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| scveh.macrs | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen |
| scveh.s179_2025 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| scveh.mq_q4 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| scveh.mq_total | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| scveh.cost179 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 9 (scveh.line9) | scveh.employee_use, scveh.h_actual_invalid, scveh.h_standard_invalid, scveh.screen | scveh.employee_use, scveh.h_actual_invalid, scveh.h_standard_invalid, scveh.screen |
| 20a | scveh.employee_use, scveh.h_actual_invalid, scveh.screen | scveh.employee_use, scveh.h_actual_invalid, scveh.screen |
| 13 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 7 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 9 (scveh.line9w) | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 10 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 11 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 14 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 15 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 16 | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen |
| 25 | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen |
| 17 | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen |
| 18 | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen |
| 19 | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen |
| 20 | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed_2025, scveh.screen |

## Raw second transcription

```yaml
```yaml
lines:
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses (see instructions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.method, {const: "standard"}]}
          then: scveh.h_standard_total
        - guard: {op: test, eq: [scveh.method, {const: "actual"}]}
          then: scveh.h_actual_total
    refuses: [scveh.screen, scveh.employee_use, scveh.h_standard_invalid, scveh.h_actual_invalid]
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: a Vehicles, machinery, and equipment"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.method, {const: "actual"}]}
              - {op: test, eq: [scveh.owned, {const: false}]}
          then: scveh.h_lease_business
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [scveh.method, {const: "actual"}]}
                - {op: test, eq: [scveh.owned, {const: false}]}
          then: scveh.h_zero
    refuses: [scveh.screen, scveh.employee_use, scveh.h_actual_invalid]
    shown_when: scveh.h_show_20a
    note: "The lease inclusion amount mentioned in the Schedule C line 20a instructions for a lease of 30 days or more is not supplied by the interface and is not applied."
  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.miles_business, whole: scveh.h_total_miles, places: 6}
    refuses: [scveh.screen, scveh.employee_use]
    shown_when: scveh.h_show_depreciation
    note: "The business-use fraction is figured from the mileage counts and rounded to six decimal places because the model has no exact count-division atom."
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.h_has_bonus, {const: true}]}
          then: scveh.h_auto_limit_with_bonus
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.h_has_bonus, {const: false}]}
          then: scveh.h_auto_limit_first_nobonus
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, ne: [scveh.placed, {const: "y2025"}]}
          then: scveh.h_auto_limit_with_bonus
        - guard: {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.h_no_passenger_limit
    refuses: [scveh.screen, scveh.employee_use]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.miles_business, whole: scveh.h_total_miles, places: 6}
    refuses: [scveh.screen, scveh.employee_use]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.placed, {const: "y2025"}]}
          then: scveh.h_s179_this_year
        - guard: {op: test, ne: [scveh.placed, {const: "y2025"}]}
          then: scveh.h_zero
    refuses: [scveh.screen, scveh.employee_use]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line11
    printed: "11"
    label: "Subtract line 10 from line 9. This is the limit on the amount you can deduct for depreciation (including any special depreciation allowance)."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line9w, take: scveh.line10}
    refuses: [scveh.screen, scveh.employee_use]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.placed, {const: "y2025"}]}
          then: scveh.line10
        - guard: {op: test, ne: [scveh.placed, {const: "y2025"}]}
          then: scveh.prior_179
    refuses: [scveh.screen, scveh.employee_use]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line15
    printed: "15"
    label: "Subtract line 14 from line 13. This is your tentative basis for depreciation."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.bus_cost, take: scveh.line14}
    refuses: [scveh.screen, scveh.employee_use]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line16
    printed: "16"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. This is your special depreciation allowance."
    type: NonNegDollars
    expr: {op: copy, from: scveh.bonus}
    refuses: [scveh.screen, scveh.h_bonus_mixed_2025]
    shown_when: scveh.h_show_depreciation
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Enter on line 25 your total special depreciation allowance for all qualified listed property."
    type: NonNegDollars
    expr: {op: copy, from: scveh.bonus}
    refuses: [scveh.screen, scveh.h_bonus_mixed_2025]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line17
    printed: "17"
    label: "Subtract line 16 from line 11. This is the limit on the amount you can deduct for MACRS depreciation."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line11, take: scveh.line16}
    refuses: [scveh.screen, scveh.h_bonus_mixed_2025]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line18
    printed: "18"
    label: "Subtract line 16 from line 15. This is your basis for depreciation."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line15, take: scveh.line16}
    refuses: [scveh.screen, scveh.h_bonus_mixed_2025]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line19
    printed: "19"
    label: "Multiply line 18 by line 6. This is your tentative MACRS depreciation deduction."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.h_mq_applies, {const: true}]}
          then: scveh.h_macrs_mq
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.h_mq_applies, {const: false}]}
          then: scveh.h_macrs_hy
        - guard: {op: test, ne: [scveh.placed, {const: "y2025"}]}
          then: scveh.h_macrs_prior
    refuses: [scveh.screen, scveh.h_bonus_mixed_2025]
    shown_when: scveh.h_show_depreciation
  - id: scveh.line20
    printed: "20"
    label: "Enter the lesser of line 17 or line 19. This is your MACRS depreciation deduction."
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}
    refuses: [scveh.screen, scveh.h_bonus_mixed_2025]
    shown_when: scveh.h_show_depreciation
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: scveh.h_mileage_rate
    printed: "(helper)"
    label: "Business standard mileage rate"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}
  - id: scveh.h_total_miles
    printed: "(helper)"
    label: "Total miles driven"
    type: Count
    expr: {op: sum, of: [scveh.miles_business, scveh.miles_commuting, scveh.miles_other]}
  - id: scveh.h_standard_amount
    printed: "(helper)"
    label: "Business miles times the standard mileage rate"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_mileage_rate, count: scveh.miles_business}
  - id: scveh.h_standard_total
    printed: "(helper)"
    label: "Standard mileage amount plus parking and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_standard_amount, scveh.parking]}
  - id: scveh.h_actual_operating
    printed: "(helper)"
    label: "Business portion of operating expenses"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.miles_business, whole: scveh.h_total_miles, places: 6}
  - id: scveh.h_actual_total
    printed: "(helper)"
    label: "Actual operating expenses plus parking and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_actual_operating, scveh.parking]}
  - id: scveh.h_lease_business
    printed: "(helper)"
    label: "Business portion of lease payments"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.miles_business, whole: scveh.h_total_miles, places: 6}
  - id: scveh.h_standard_invalid
    printed: "(helper)"
    label: "Standard mileage rate not available"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "standard"}]}
        - {op: test, eq: [scveh.smr_ok, {const: false}]}
  - id: scveh.h_actual_invalid
    printed: "(helper)"
    label: "Actual expenses not available for this leased vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: false}]}
        - {op: test, eq: [scveh.lease_smr_before, {const: true}]}
  - id: scveh.h_show_depreciation
    printed: "(helper)"
    label: "Show the depreciation worksheet lines"
    type: Bool
    expr: {op: test, eq: [scveh.method, {const: "actual"}]}
  - id: scveh.h_show_20a
    printed: "(helper)"
    label: "Show line 20a for an actual-expense leased vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: false}]}
  - id: scveh.h_recovery_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [scveh.placed]}
  - id: scveh.h_auto_limit_with_bonus
    printed: "(helper)"
    label: "Passenger automobile limit from the applicable table"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_recovery_year]}
  - id: scveh.h_auto_limit_first_nobonus
    printed: "(helper)"
    label: "First-year passenger automobile limit without the special depreciation allowance"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit_first_nobonus, keys: [scveh.placed]}
  - id: scveh.h_no_passenger_limit
    printed: "(helper)"
    label: "No passenger automobile limit"
    type: NonNegDollars
    expr: {op: copy, from: scveh.cost}
  - id: scveh.h_has_bonus
    printed: "(helper)"
    label: "A special depreciation allowance is claimed for this 2025 vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.placed, {const: "y2025"}]}
        - {op: test, ne: [scveh.bonus_choice, {const: "none"}]}
  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "The bonus choice is not the same for all 5-year property"
    type: Bool
    expr: {op: test, not: {op: test, eq: [scveh.bonus_same, {const: true}]}}
  - id: scveh.h_bonus_mixed_2025
    printed: "(helper)"
    label: "The bonus choice issue applies to this 2025 vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.placed, {const: "y2025"}]}
        - {op: test, eq: [scveh.h_bonus_mixed, {const: true}]}
  - id: scveh.h_suv_limit
    printed: "(helper)"
    label: "Section 179 limit for SUVs and certain other vehicles"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_period
    printed: "(helper)"
    label: "5-year property recovery period"
    type: Enum(macrs_period)
    expr: {op: param, ref: sc.period_y5}
  - id: scveh.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: scveh.h_qconv_mq
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [scveh.quarter]}
  - id: scveh.h_macrs_rate_mq
    printed: "(helper)"
    label: "MACRS rate under the mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_qconv_mq, scveh.h_recovery_year]}
  - id: scveh.h_macrs_rate_hy
    printed: "(helper)"
    label: "MACRS rate under the half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_hy, scveh.h_recovery_year]}
  - id: scveh.h_macrs_rate_prior
    printed: "(helper)"
    label: "MACRS rate under the prior convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_recovery_year]}
  - id: scveh.h_mq_threshold
    printed: "(helper)"
    label: "Forty percent of the business total depreciable bases"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.mq_total, rate: {param: sc.bonus_rate_40}}
  - id: scveh.h_mq_applies
    printed: "(helper)"
    label: "The mid-quarter convention applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.placed, {const: "y2025"}]}
        - {op: test, gt: [sc.mq_q4, scveh.h_mq_threshold]}
  - id: scveh.h_s179_elected_capped
    printed: "(helper)"
    label: "Elected section 179 cost after the SUV limit"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.cost179]}
  - id: scveh.h_s179_this_year
    printed: "(helper)"
    label: "Current-year section 179 deduction before the placed-in-service check"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_s179_elected_capped, scveh.line9w]}
  - id: scveh.h_bonus_forty_amount
    printed: "(helper)"
    label: "Forty percent special depreciation allowance"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}
  - id: scveh.h_bonus_raw
    printed: "(helper)"
    label: "Special depreciation allowance before the passenger automobile limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
              - {op: test, eq: [scveh.after_jan19, {const: true}]}
          then: scveh.line15
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
              - {op: test, eq: [scveh.after_jan19, {const: false}]}
          then: scveh.h_bonus_forty_amount
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "forty"}]}
          then: scveh.h_bonus_forty_amount
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "none"}]}
          then: scveh.h_zero
        - guard: {op: test, ne: [scveh.placed, {const: "y2025"}]}
          then: scveh.h_zero
  - id: scveh.h_macrs_mq
    printed: "(helper)"
    label: "Tentative MACRS depreciation under the mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_macrs_rate_mq}
  - id: scveh.h_macrs_hy
    printed: "(helper)"
    label: "Tentative MACRS depreciation under the half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_macrs_rate_hy}
  - id: scveh.h_macrs_prior
    printed: "(helper)"
    label: "Tentative MACRS depreciation under the prior convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_macrs_rate_prior}
  - id: scveh.h_mq_total_2025
    printed: "(helper)"
    label: "Vehicle depreciable basis for the mid-quarter test"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.bus_cost, take: scveh.line10}
  - id: scveh.cost179
    printed: "(helper)"
    label: "Vehicle cost eligible for section 179 after the SUV limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.suv, {const: true}]}
          then:
            op: smaller_of
            of: [scveh.bus_cost, scveh.h_suv_limit]
        - guard: {op: test, eq: [scveh.suv, {const: false}]}
          then: scveh.bus_cost
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Section 179 deduction for this vehicle for 2025"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line10}
  - id: scveh.bonus
    printed: "(helper)"
    label: "Special depreciation allowance allowed for this vehicle"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_bonus_raw, scveh.line11]}
    note: "The passenger automobile limit caps the special depreciation allowance; this uses the smaller of the computed allowance and line 11."
  - id: scveh.macrs
    printed: "(helper)"
    label: "MACRS depreciation for this vehicle for 2025"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line20}
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Vehicle depreciable basis placed in service in 2025 for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.placed, {const: "y2025"}]}
          then: scveh.h_mq_total_2025
        - guard: {op: test, ne: [scveh.placed, {const: "y2025"}]}
          then: scveh.h_zero
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
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.quarter, {const: "q4"}]}
          then: scveh.mq_total
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [scveh.placed, {const: "y2025"}]}
                - {op: test, eq: [scveh.quarter, {const: "q4"}]}
          then: scveh.h_zero
```
```
