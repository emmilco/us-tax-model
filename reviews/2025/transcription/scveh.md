# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | abc7568cf718f4463948d6ee5181b0c073d416c0d228ebb557fb43c656538dec |
| printed lines compared | 21 |
| agree / disagree / missing | 6 / 15 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 61, 62, 63 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### scveh.bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "25"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "25"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent; project retained. A vehicle that is not a passenger automobile takes line 16, one that is takes line 25, on both sides: the project chooses here, the second chooses inside its line 25.

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"of": [{"line": "7"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"const": 1}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1}], "op": "keyed_lookup", "table": "p946.macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "p946.macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "p946.macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "p946.macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "p946.macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "p946.macrs_gds"}}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "ne"}], "test": "any"}, "then": {"line": "20"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; project retained. The 2019 vehicle's first year after the recovery period follows the Pub. 946 automobile worksheet on both sides (pp. 61–62): year one the lesser of the limit and the section 179 deduction plus the MACRS amount, years 2 to 6 the lesser of each limit and the table amount, the unrecovered basis cost less their total, and 2025 the lesser of the later-years limit and that, times business use. The second names its own tables and key constants and reads line 7 where the project reads the same later-years limit; its ratio is at four places where the owner ruled six (3c).

### scveh.s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Depreciable basis reflects personal use and section 179 but not the special allowance (Pub. 946 caution), which is line 15. Vehicles on the standard mileage rate and leased vehicles are taken as not MACRS property of the filer.

Ruling: equivalent; project retained. Line 15 for a fourth-quarter 2025 vehicle on actual expenses and owned, zero otherwise, on both sides; nested against merged guards.

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent; project retained. Line 15 for a 2025 vehicle on actual expenses and owned, zero otherwise, on both sides; nested against merged guards.

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"line": "13"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Form 4562 line 2 includes listed property from Part V. Listed property used 50% or less does not qualify for section 179, and the business-use cost (line 13) is used. An owned vehicle on the standard mileage rate is not counted, because its year placed in service is collected only for depreciation; this is a scope choice.

Ruling: equivalent; project retained. Line 13 for a 2025 vehicle on actual expenses and owned, zero otherwise, on both sides; use of 50% or less is refused on line 13.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second transcription's note: The rule that actual expenses are required for five or more vehicles used simultaneously has no input, so it is not encoded.

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles to six decimal places, half-up (owner ruling 3c; amb.2025 register); the second rounds the ratio to four places, its own reading of an open point it noted.

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The standard mileage rate excludes rent or lease payments, so that case is zero. The reduction by the inclusion amount for leases of 30 days or more has no input and is not encoded.

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles to six decimal places, half-up (owner ruling 3c; amb.2025 register); the second rounds the ratio to four places, its own reading of an open point it noted. Otherwise the same.

### 13 — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}
```

Second transcription's note: Line 8 (business/investment-use percentage) is business miles divided by total miles. The rounding is not stated; chose 4 decimal places. Line 12 is the cost input, which is not reduced for any vehicle credit.

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles to six decimal places, half-up (owner ruling 3c; amb.2025 register); the second rounds the ratio to four places, its own reading of an open point it noted.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "i4562.table2_2025_bonus"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "i4562.table2_2025"}}, {"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The limits apply only to passenger automobiles. For other vehicles, lines 7, 9, 11 and 17 are zero and are not used.

Ruling: representation; project retained. For a 2025 vehicle the first-year limit with or without the special allowance, and for an earlier vehicle the limit for its recovery year, on both sides (i4562 Limits for passenger automobiles; Pub. 946 p. 59); the second names its own tables and merges the guards.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}
```

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles to six decimal places, half-up (owner ruling 3c; amb.2025 register); the second rounds the ratio to four places, its own reading of an open point it noted.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Enter -0- if this is not the year placed in service. This uses the elected amount. The Form 4562 Part I business income limitation is not applied here.

Ruling: equivalent; project retained. The section 179 deduction for a 2025 vehicle, capped at line 9 for a passenger automobile, zero otherwise, on both sides; nested against merged guards.

### 11 — Subtract line 10 from line 9
Status: **AGREE**

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

### 16 — Special depreciation allowance
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: 100% applies if acquired after January 19, 2025 and the 40% election is not made. 40% applies if acquired before January 20, 2025, or under the 40% election. Zero applies if not placed in service in 2025, not qualified property (50% or less use), or elected out.

Ruling: equivalent within scope; project retained. The special allowance for 2025 vehicles: 100% when acquired after January 19, 2025 and the full allowance is chosen, 40% when acquired earlier or by election, none when elected out, on both sides, with the guards arranged differently; the second's zero for use of 50% or less is a case the project refuses (scveh low_use).

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}}], "op": "choose"}
```

Ruling: representation; project retained. For a passenger automobile both take the smaller of lines 11 and 16. Vehicles that are not passenger automobiles are not subject to the worksheet's limits (Pub. 946 pp. 61–62, Depreciation Worksheet for Passenger Automobiles): their depreciation and special allowance take line 19 and line 16 directly (scveh.macrs_heavy, scveh.bonus_o), so the worksheet line shown for them is not used.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

### 18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"param": "sc.conv_hy"}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"const": "mq1"}}, {"guard": {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"const": "mq2"}}, {"guard": {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"const": "mq3"}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"const": "mq4"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_conv"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}], "op": "keyed_lookup", "table": "p946.macrs_gds"}}}], "op": "choose"}
```

Second transcription's note: For a 2019 vehicle the recovery period ended before 2025, so there is no table rate. Any deduction is the unrecovered basis (helpers below).

Ruling: equivalent; project retained. Line 18 times the rate chosen by the same convention and recovery-year tests; the second chooses the rate and multiplies once, the project chooses between products, the same value in every branch.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "19"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "17"}, {"line": "19"}], "op": "smaller_of"}}], "op": "choose"}
```

Second transcription's note: Vehicles not subject to the passenger automobile limits take line 19 without the line 17 limit.

Ruling: representation; project retained. For a passenger automobile both take the smaller of lines 17 and 19. Vehicles that are not passenger automobiles are not subject to the worksheet's limits (Pub. 946 pp. 61–62, Depreciation Worksheet for Passenger Automobiles): their depreciation and special allowance take line 19 and line 16 directly (scveh.macrs_heavy, scveh.bonus_o), so the worksheet line shown for them is not used.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.h_dep_refused | scveh.h_dep_refused |
| scveh.macrs | scveh.h_dep_refused | scveh.h_dep_refused |
| scveh.s179_2025 | scveh.h_dep_refused | scveh.h_dep_refused |
| scveh.mq_q4 | scveh.h_dep_refused | scveh.h_dep_refused |
| scveh.mq_total | scveh.h_dep_refused | scveh.h_dep_refused |
| scveh.cost179 | scveh.h_dep_refused | scveh.h_dep_refused |
| 9 (scveh.line9) | scveh.h_no_miles_actual, scveh.h_smr_bad | scveh.h_no_miles_actual, scveh.h_smr_bad |
| 20a | scveh.h_no_miles_actual | scveh.h_no_miles_actual |
| 7 | scveh.h_dep_refused | scveh.h_dep_refused |
| 9 (scveh.line9w) | scveh.h_dep_refused | scveh.h_dep_refused |
| 10 | scveh.h_dep_refused | scveh.h_dep_refused |
| 11 | scveh.h_dep_refused | scveh.h_dep_refused |
| 14 | scveh.h_dep_refused | scveh.h_dep_refused |
| 15 | scveh.h_dep_refused | scveh.h_dep_refused |
| 16 | scveh.h_dep_refused | scveh.h_dep_refused |
| 25 | scveh.h_dep_refused | scveh.h_dep_refused |
| 17 | scveh.h_dep_refused | scveh.h_dep_refused |
| 18 | scveh.h_dep_refused | scveh.h_dep_refused |
| 19 | scveh.h_dep_refused | scveh.h_dep_refused |
| 20 | scveh.h_dep_refused | scveh.h_dep_refused |

## Raw second transcription

```yaml
```yaml
lines:
  # ---------- Mileage and method helpers ----------
  - id: scveh.h_cent
    printed: "(helper)"
    label: "One cent (used to carry mileage as a money amount)"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: scveh.h_bm_c
    printed: "(helper)"
    label: "Business miles (line 44a), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}
  - id: scveh.h_cm_c
    printed: "(helper)"
    label: "Commuting miles (line 44b), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}
  - id: scveh.h_om_c
    printed: "(helper)"
    label: "Other miles (line 44c), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}
  - id: scveh.h_nonbus_c
    printed: "(helper)"
    label: "Commuting and other miles, as cents"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_cm_c, scveh.h_om_c]}
  - id: scveh.h_total_c
    printed: "(helper)"
    label: "Total number of miles the vehicle is driven for all purposes, as cents"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_bm_c, scveh.h_cm_c, scveh.h_om_c]}
  - id: scveh.h_no_miles
    printed: "(helper)"
    label: "No miles driven (business-use percentage cannot be figured)"
    type: Bool
    expr: {op: test, eq: [scveh.h_total_c, {const: 0}]}
  - id: scveh.h_is_standard
    printed: "(helper)"
    label: "You take the standard mileage rate"
    type: Bool
    expr: {op: test, eq: [scveh.method, {const: "standard"}]}
  - id: scveh.h_is_actual
    printed: "(helper)"
    label: "You deduct actual expenses"
    type: Bool
    expr: {op: test, eq: [scveh.method, {const: "actual"}]}
  - id: scveh.h_actual_owned
    printed: "(helper)"
    label: "Owned vehicle, actual expenses (depreciation shown on line 13)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_is_actual, {const: true}]}, {op: test, eq: [scveh.owned, {const: true}]}]}
  - id: scveh.h_actual_leased
    printed: "(helper)"
    label: "Leased vehicle, actual expenses (lease payments shown on line 20a)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_is_actual, {const: true}]}, {op: test, eq: [scveh.owned, {const: false}]}]}
  - id: scveh.h_no_miles_actual
    printed: "(helper)"
    label: "Actual expenses with no miles entered"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_is_actual, {const: true}]}, {op: test, eq: [scveh.h_no_miles, {const: true}]}]}
  - id: scveh.h_smr_bad
    printed: "(helper)"
    label: "Standard mileage rate chosen but not available (owned: not used in the first year; leased: not used for the entire lease period)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_is_standard, {const: true}]}, {op: test, eq: [scveh.smr_ok, {const: false}]}]}
  - id: scveh.h_rate
    printed: "(helper)"
    label: "Standard mileage rate, 70 cents per mile"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}
  - id: scveh.h_smr_amount
    printed: "(helper)"
    label: "Multiply the number of business miles driven by 0.70"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_rate, count: scveh.miles_business}
  - id: scveh.h_line9_standard
    printed: "(helper)"
    label: "Add to this amount your parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_smr_amount, scveh.parking]}
  - id: scveh.h_operating_business
    printed: "(helper)"
    label: "The business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
    note: "The business portion is taken as business miles over total miles (the i4562 column (c) rule). The rounding of the ratio is not stated; chose 4 decimal places."
  - id: scveh.h_line9_actual
    printed: "(helper)"
    label: "Business portion of operating expenses plus business parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_operating_business, scveh.parking]}
    note: "For actual expenses the text lists gasoline, oil, repairs, insurance, license plates 'etc.' and says nothing of parking and tolls. Chose to include business parking fees and tolls under 'etc.'"
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  # ---------- Schedule C line 9 ----------
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is_standard, {const: true}]}, then: scveh.h_line9_standard}
        - {guard: {op: test, eq: [scveh.h_is_actual, {const: true}]}, then: scveh.h_line9_actual}
    refuses: [scveh.h_smr_bad, scveh.h_no_miles_actual]
    note: "The rule that actual expenses are required for five or more vehicles used simultaneously has no input, so it is not encoded."

  # ---------- Schedule C line 20a ----------
  - id: scveh.h_lease_business
    printed: "(helper)"
    label: "The business portion of your rental cost"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease of this vehicle (business portion)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_actual_leased, {const: true}]}, then: scveh.h_lease_business}
        - {guard: {op: test, eq: [scveh.h_actual_leased, {const: false}]}, then: scveh.h_zero}
    refuses: [scveh.h_no_miles_actual]
    note: "The standard mileage rate excludes rent or lease payments, so that case is zero. The reduction by the inclusion amount for leases of 30 days or more has no input and is not encoded."

  # ---------- Depreciation screening helpers ----------
  - id: scveh.h_over_half
    printed: "(helper)"
    label: "Business use more than 50% (business miles more than commuting plus other miles)"
    type: Bool
    expr: {op: test, gt: [scveh.h_bm_c, scveh.h_nonbus_c]}
  - id: scveh.h_is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2025"}]}
  - id: scveh.h_is2019
    printed: "(helper)"
    label: "Placed in service in 2019 (the recovery period ended before 2025)"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2019"}]}
  - id: scveh.h_too_old
    printed: "(helper)"
    label: "Owned, actual expenses, placed in service before 2019"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_actual_owned, {const: true}]}
        - op: test
          not:
            op: test
            any:
              - {op: test, eq: [scveh.placed, {const: "y2019"}]}
              - {op: test, eq: [scveh.placed, {const: "y2020"}]}
              - {op: test, eq: [scveh.placed, {const: "y2021"}]}
              - {op: test, eq: [scveh.placed, {const: "y2022"}]}
              - {op: test, eq: [scveh.placed, {const: "y2023"}]}
              - {op: test, eq: [scveh.placed, {const: "y2024"}]}
              - {op: test, eq: [scveh.placed, {const: "y2025"}]}
  - id: scveh.h_screened
    printed: "(helper)"
    label: "Owned, actual expenses, and a screening condition applies"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_actual_owned, {const: true}]}, {op: test, eq: [scveh.screen, {const: true}]}]}
  - id: scveh.h_low_use
    printed: "(helper)"
    label: "Owned, actual expenses, used 50% or less in a qualified business use (line 27, ADS straight line)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_actual_owned, {const: true}]}, {op: test, eq: [scveh.h_over_half, {const: false}]}]}
    note: "The text has property used 50% or less depreciated straight line over the ADS period. This transcription does not compute that case and refuses it."
  - id: scveh.h_suv_cap
    printed: "(helper)"
    label: "You cannot elect to expense more than $31,300 of the cost of any SUVs"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_s179_bad
    printed: "(helper)"
    label: "The section 179 election is more than the business cost, made when not allowed, or over the SUV limit"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_actual_owned, {const: true}]}
        - op: test
          any:
            - {op: test, gt: [scveh.s179_elect, scveh.line13]}
            - op: test
              all:
                - {op: test, gt: [scveh.s179_elect, {const: 0}]}
                - {op: test, not: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.h_over_half, {const: true}]}]}}
            - op: test
              all:
                - {op: test, eq: [scveh.passenger, {const: false}]}
                - {op: test, eq: [scveh.suv, {const: true}]}
                - {op: test, gt: [scveh.s179_elect, scveh.h_suv_cap]}
  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "The special allowance choice is not the same for all 5-year property placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_actual_owned, {const: true}]}
        - {op: test, eq: [scveh.h_is2025, {const: true}]}
        - {op: test, eq: [scveh.h_over_half, {const: true}]}
        - {op: test, eq: [scveh.bonus_same, {const: false}]}
  - id: scveh.h_dep_refused
    printed: "(helper)"
    label: "This vehicle's depreciation is outside this tool"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [scveh.h_screened, {const: true}]}
        - {op: test, eq: [scveh.h_too_old, {const: true}]}
        - {op: test, eq: [scveh.h_low_use, {const: true}]}
        - {op: test, eq: [scveh.h_s179_bad, {const: true}]}
        - {op: test, eq: [scveh.h_bonus_mixed, {const: true}]}
  - id: scveh.h_claims_bonus
    printed: "(helper)"
    label: "A special depreciation allowance is taken (placed in service in 2025, qualified property, not elected out)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_is2025, {const: true}]}
        - {op: test, eq: [scveh.h_over_half, {const: true}]}
        - {op: test, ne: [scveh.bonus_choice, {const: "none"}]}

  # ---------- Part I ----------
  - id: scveh.line13
    printed: "13"
    label: "Business/investment cost (cost times business use)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
    note: "Line 8 (business/investment-use percentage) is business miles divided by total miles. The rounding is not stated; chose 4 decimal places. Line 12 is the cost input, which is not reduced for any vehicle credit."
  - id: scveh.h_lim_table
    printed: "(helper)"
    label: "Limit on depreciation and section 179 for 2025 by the year placed in service (Table 2; no special allowance)"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: i4562.table2_2025, keys: [scveh.placed]}
    note: "Pinned rows (2025 tax year, number of years in service): y2025 $12,200; y2024 $19,800; y2023 $11,700; y2022 $6,460; y2021 $5,860; y2020 $5,760; y2019 $5,760. Tables 1 and 2 agree for 2018 and 2019."
  - id: scveh.h_lim_first_bonus
    printed: "(helper)"
    label: "If you take the special depreciation allowance ... placed in service in 2025, the limit is $20,200"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: i4562.table2_2025_bonus, keys: [scveh.placed]}
    note: "Pinned row: y2025 $20,200."
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_claims_bonus, {const: true}]}]}
          then: scveh.h_lim_first_bonus
        - guard: {op: test, all: [{op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_claims_bonus, {const: false}]}]}
          then: scveh.h_lim_table
        - guard: {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.h_zero
    refuses: [scveh.h_dep_refused]
    note: "The limits apply only to passenger automobiles. For other vehicles, lines 7, 9, 11 and 17 are zero and are not used."
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Adjusted maximum depreciation deduction (line 7 times the business/investment-use percentage)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
  - id: scveh.h_s179_capped
    printed: "(helper)"
    label: "Section 179 elected, not more than line 9"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.line9w]}
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.h_over_half, {const: true}]}, {op: test, eq: [scveh.passenger, {const: true}]}]}
          then: scveh.h_s179_capped
        - guard: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.h_over_half, {const: true}]}, {op: test, eq: [scveh.passenger, {const: false}]}]}
          then: scveh.s179_elect
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.h_over_half, {const: true}]}]}}
          then: scveh.h_zero
    note: "Enter -0- if this is not the year placed in service. This uses the elected amount. The Form 4562 Part I business income limitation is not applied here."

  # ---------- Part II ----------
  - id: scveh.line11
    printed: "11"
    label: "Subtract line 10 from line 9"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line9w, take: scveh.line10}
  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.line10}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.prior_179}
  - id: scveh.line15
    printed: "15"
    label: "Tentative basis for depreciation (line 13 less line 14)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line13, take: scveh.line14}
  - id: scveh.h_bonus_forty
    printed: "(helper)"
    label: "Line 15 times 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}
  - id: scveh.h_bonus_100case
    printed: "(helper)"
    label: "Acquired after January 19, 2025, and the 100% allowance is claimed"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.after_jan19, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "full"}]}]}
  - id: scveh.line16
    printed: "16"
    label: "Special depreciation allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_claims_bonus, {const: true}]}, {op: test, eq: [scveh.h_bonus_100case, {const: true}]}]}
          then: scveh.line15
        - guard: {op: test, all: [{op: test, eq: [scveh.h_claims_bonus, {const: true}]}, {op: test, eq: [scveh.h_bonus_100case, {const: false}]}]}
          then: scveh.h_bonus_forty
        - guard: {op: test, eq: [scveh.h_claims_bonus, {const: false}]}
          then: scveh.h_zero
    note: "100% applies if acquired after January 19, 2025 and the 40% election is not made. 40% applies if acquired before January 20, 2025, or under the 40% election. Zero applies if not placed in service in 2025, not qualified property (50% or less use), or elected out."
  - id: scveh.h_line25_pass
    printed: "(helper)"
    label: "The smaller of line 16 or line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line16, scveh.line11]}
  - id: scveh.line25
    printed: "25"
    label: "Special depreciation allowance allowed (not more than line 11)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: true}]}, then: scveh.h_line25_pass}
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.line16}

  # ---------- Part III ----------
  - id: scveh.line17
    printed: "17"
    label: "Limit on the MACRS depreciation (line 11 less line 16)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line11, take: scveh.line16}
    note: "If line 16 equals or exceeds line 11 the worksheet stops, so this line is zero."
  - id: scveh.line18
    printed: "18"
    label: "Basis for depreciation (line 15 less line 16)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line15, take: scveh.line16}
  - id: scveh.h_y5
    printed: "(helper)"
    label: "5-year property (automobiles, light general purpose trucks)"
    type: Enum(macrs_period)
    expr: {op: param, ref: sc.period_y5}
  - id: scveh.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: scveh.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.quarter, {const: "q1"}]}, then: {const: "mq1"}}
        - {guard: {op: test, eq: [scveh.quarter, {const: "q2"}]}, then: {const: "mq2"}}
        - {guard: {op: test, eq: [scveh.quarter, {const: "q3"}]}, then: {const: "mq3"}}
        - {guard: {op: test, eq: [scveh.quarter, {const: "q4"}]}, then: {const: "mq4"}}
  - id: scveh.h_conv2025
    printed: "(helper)"
    label: "Convention for 2025 property: mid-quarter if the October to December bases exceed 40% of all 2025 bases, otherwise half-year"
    type: Enum(macrs_convention)
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [mq.applies, {const: true}]}, then: scveh.h_qconv}
        - {guard: {op: test, eq: [mq.applies, {const: false}]}, then: scveh.h_hy}
  - id: scveh.h_conv
    printed: "(helper)"
    label: "Line 5. Method and convention (convention)"
    type: Enum(macrs_convention)
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_conv2025}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.prior_conv}
  - id: scveh.h_year
    printed: "(helper)"
    label: "Year of the recovery period in 2025"
    type: Count
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.placed, {const: "y2025"}]}, then: {param: sc.year1}}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2024"}]}, then: {param: sc.year2}}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2023"}]}, then: {param: sc.year3}}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2022"}]}, then: {param: sc.year4}}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2021"}]}, then: {param: sc.year5}}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2020"}]}, then: {param: sc.year6}}
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: [scveh.placed, {const: "y2025"}]}
                - {op: test, eq: [scveh.placed, {const: "y2024"}]}
                - {op: test, eq: [scveh.placed, {const: "y2023"}]}
                - {op: test, eq: [scveh.placed, {const: "y2022"}]}
                - {op: test, eq: [scveh.placed, {const: "y2021"}]}
                - {op: test, eq: [scveh.placed, {const: "y2020"}]}
          then: {const: 0}
    note: "Year 0 has no table row. It is used only for 2019 vehicles (after the recovery period, line 19 not used) and for refused years."
  - id: scveh.h_rate6
    printed: "(helper)"
    label: "Line 6. Depreciation rate (from tables)"
    type: Rate
    expr: {op: keyed_lookup, table: p946.macrs_gds, keys: [scveh.h_y5, scveh.h_conv, scveh.h_year]}
  - id: scveh.h_line19_figured
    printed: "(helper)"
    label: "Multiply line 18 by line 6"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate6}
  - id: scveh.line19
    printed: "19"
    label: "Tentative MACRS depreciation deduction (line 18 times line 6)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2019, {const: true}]}, then: scveh.h_zero}
        - {guard: {op: test, eq: [scveh.h_is2019, {const: false}]}, then: scveh.h_line19_figured}
    note: "For a 2019 vehicle the recovery period ended before 2025, so there is no table rate. Any deduction is the unrecovered basis (helpers below)."
  - id: scveh.h_line20_pass
    printed: "(helper)"
    label: "The lesser of line 17 or line 19"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}
  - id: scveh.line20
    printed: "20"
    label: "MACRS depreciation deduction (the lesser of line 17 or line 19)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: true}]}, then: scveh.h_line20_pass}
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.line19}
    note: "Vehicles not subject to the passenger automobile limits take line 19 without the line 17 limit."

  # ---------- Deductions after the recovery period (2019 passenger automobile) ----------
  - id: scveh.h_b100
    printed: "(helper)"
    label: "Cost less the section 179 deduction (as if used 100% for business)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.prior_179}
  - {id: scveh.h_k1, printed: "(helper)", label: "Year 1", type: Count, expr: {op: param, ref: sc.year1}}
  - {id: scveh.h_k2, printed: "(helper)", label: "Year 2", type: Count, expr: {op: param, ref: sc.year2}}
  - {id: scveh.h_k3, printed: "(helper)", label: "Year 3", type: Count, expr: {op: param, ref: sc.year3}}
  - {id: scveh.h_k4, printed: "(helper)", label: "Year 4", type: Count, expr: {op: param, ref: sc.year4}}
  - {id: scveh.h_k5, printed: "(helper)", label: "Year 5", type: Count, expr: {op: param, ref: sc.year5}}
  - {id: scveh.h_k6, printed: "(helper)", label: "Year 6", type: Count, expr: {op: param, ref: sc.year6}}
  - {id: scveh.h_r1, printed: "(helper)", label: "Percentage, year 1", type: Rate, expr: {op: keyed_lookup, table: p946.macrs_gds, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k1]}}
  - {id: scveh.h_r2, printed: "(helper)", label: "Percentage, year 2", type: Rate, expr: {op: keyed_lookup, table: p946.macrs_gds, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k2]}}
  - {id: scveh.h_r3, printed: "(helper)", label: "Percentage, year 3", type: Rate, expr: {op: keyed_lookup, table: p946.macrs_gds, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k3]}}
  - {id: scveh.h_r4, printed: "(helper)", label: "Percentage, year 4", type: Rate, expr: {op: keyed_lookup, table: p946.macrs_gds, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k4]}}
  - {id: scveh.h_r5, printed: "(helper)", label: "Percentage, year 5", type: Rate, expr: {op: keyed_lookup, table: p946.macrs_gds, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k5]}}
  - {id: scveh.h_r6, printed: "(helper)", label: "Percentage, year 6", type: Rate, expr: {op: keyed_lookup, table: p946.macrs_gds, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k6]}}
  - {id: scveh.h_t1, printed: "(helper)", label: "Amount, year 1", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r1}}
  - {id: scveh.h_t2, printed: "(helper)", label: "Amount, year 2", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r2}}
  - {id: scveh.h_t3, printed: "(helper)", label: "Amount, year 3", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r3}}
  - {id: scveh.h_t4, printed: "(helper)", label: "Amount, year 4", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r4}}
  - {id: scveh.h_t5, printed: "(helper)", label: "Amount, year 5", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r5}}
  - {id: scveh.h_t6, printed: "(helper)", label: "Amount, year 6", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r6}}
  - id: scveh.h_t1s
    printed: "(helper)"
    label: "Year 1 section 179 deduction plus MACRS amount"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.prior_179, scveh.h_t1]}
  - {id: scveh.h_l1, printed: "(helper)", label: "Limit, year 1", type: NonNegDollars, expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k1]}, note: "Pinned 2019 rows (no special allowance, as screened): year 1 $10,100; 2 $16,100; 3 $9,700; 4-6 $5,760."}
  - {id: scveh.h_l2, printed: "(helper)", label: "Limit, year 2", type: NonNegDollars, expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k2]}}
  - {id: scveh.h_l3, printed: "(helper)", label: "Limit, year 3", type: NonNegDollars, expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k3]}}
  - {id: scveh.h_l4, printed: "(helper)", label: "Limit, year 4", type: NonNegDollars, expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k4]}}
  - {id: scveh.h_l5, printed: "(helper)", label: "Limit, year 5", type: NonNegDollars, expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k5]}}
  - {id: scveh.h_l6, printed: "(helper)", label: "Limit, year 6", type: NonNegDollars, expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k6]}}
  - {id: scveh.h_d1, printed: "(helper)", label: "Allowed, year 1", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t1s, scveh.h_l1]}}
  - {id: scveh.h_d2, printed: "(helper)", label: "Allowed, year 2", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t2, scveh.h_l2]}}
  - {id: scveh.h_d3, printed: "(helper)", label: "Allowed, year 3", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t3, scveh.h_l3]}}
  - {id: scveh.h_d4, printed: "(helper)", label: "Allowed, year 4", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t4, scveh.h_l4]}}
  - {id: scveh.h_d5, printed: "(helper)", label: "Allowed, year 5", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t5, scveh.h_l5]}}
  - {id: scveh.h_d6, printed: "(helper)", label: "Allowed, year 6", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t6, scveh.h_l6]}}
  - id: scveh.h_d_total
    printed: "(helper)"
    label: "Total"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_d1, scveh.h_d2, scveh.h_d3, scveh.h_d4, scveh.h_d5, scveh.h_d6]}
    note: "Pub. 946 says unrecovered basis is reduced by deductions allowable at 100% use 'and the passenger automobile limits had not applied'. Its own example reduces basis by the limited 'Allowed' amounts. Chose the example: amounts at 100% use, limited."
  - id: scveh.h_unrecovered
    printed: "(helper)"
    label: "Unrecovered basis at the end of the recovery period"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.h_d_total}
  - id: scveh.h_post_amount
    printed: "(helper)"
    label: "The lesser of the limit or your remaining unrecovered basis"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line7, scveh.h_unrecovered]}
  - id: scveh.h_post
    printed: "(helper)"
    label: "Deduction after the recovery period, times the business/investment-use percentage"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.h_post_amount, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
    note: "The text gives the 100%-use rule (lesser of the limit or unrecovered basis). For less than 100% use, chose to apply the percentage to that lesser amount, consistent with the 60% example."
  - id: scveh.h_macrs_owned
    printed: "(helper)"
    label: "Column (h) for an owned vehicle on actual expenses"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_is2019, {const: true}]}]}
          then: scveh.h_post
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_is2019, {const: true}]}]}}
          then: scveh.line20
    note: "A non-passenger vehicle has no unrecovered basis after the recovery period (line 19, and so line 20, is zero for 2019)."

  # ---------- Intermediate values for other forms ----------
  - id: scveh.bonus
    printed: "(helper)"
    label: "Line 25: special allowance of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_actual_owned, {const: true}]}, then: scveh.line25}
        - {guard: {op: test, eq: [scveh.h_actual_owned, {const: false}]}, then: scveh.h_zero}
    refuses: [scveh.h_dep_refused]
  - id: scveh.macrs
    printed: "(helper)"
    label: "Column (h): depreciation of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_actual_owned, {const: true}]}, then: scveh.h_macrs_owned}
        - {guard: {op: test, eq: [scveh.h_actual_owned, {const: false}]}, then: scveh.h_zero}
    refuses: [scveh.h_dep_refused]
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Column (i): elected section 179 cost of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_actual_owned, {const: true}]}, then: scveh.line10}
        - {guard: {op: test, eq: [scveh.h_actual_owned, {const: false}]}, then: scveh.h_zero}
    refuses: [scveh.h_dep_refused]
    note: "Column (i) is subject to the limits for passenger automobiles, so it is line 10."
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Mid-quarter test basis, fourth quarter of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_actual_owned, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.quarter, {const: "q4"}]}]}
          then: scveh.line15
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.h_actual_owned, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.quarter, {const: "q4"}]}]}}
          then: scveh.h_zero
    refuses: [scveh.h_dep_refused]
    note: "Depreciable basis reflects personal use and section 179 but not the special allowance (Pub. 946 caution), which is line 15. Vehicles on the standard mileage rate and leased vehicles are taken as not MACRS property of the filer."
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Mid-quarter test basis, 2025 of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_actual_owned, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}]}
          then: scveh.line15
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.h_actual_owned, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}]}}
          then: scveh.h_zero
    refuses: [scveh.h_dep_refused]
  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025 of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_actual_owned, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.h_over_half, {const: true}]}]}
          then: scveh.line13
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.h_actual_owned, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.h_over_half, {const: true}]}]}}
          then: scveh.h_zero
    refuses: [scveh.h_dep_refused]
    note: "Form 4562 line 2 includes listed property from Part V. Listed property used 50% or less does not qualify for section 179, and the business-use cost (line 13) is used. An owned vehicle on the standard mileage rate is not counted, because its year placed in service is collected only for depreciation; this is a scope choice."
```
```
