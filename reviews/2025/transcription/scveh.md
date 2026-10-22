# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9b4f6d2d3cd5bc885a56573d747e6bdac6fda68418b3ad2c94a0e8f6ab1ea227 |
| subject sha256 | 25b8001143dac766acd7f514d3f53d4894bfd1ece58090817f608708a9ad2267 |
| printed lines compared | 21 |
| agree / disagree / missing | 9 / 12 / 0 |
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
Status: **AGREE**

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "19"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"line": "7"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"const": 1}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1}], "op": "keyed_lookup", "table": "pub946.macrs_gds_by_convention"}}], "op": "sum"}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "pub946.macrs_gds_by_convention"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "pub946.macrs_gds_by_convention"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "pub946.macrs_gds_by_convention"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "pub946.macrs_gds_by_convention"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "pub946.macrs_gds_by_convention"}}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"const": 1}, {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "larger_of"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); project retained. The business-use percentage differs in precision: the second rounds to 4 places, the project uses 6 places, half-up, the owner's ruling on i4562 p. 14, Column (c) (no precision is given); the second's divisor (the larger of 1 and total miles) differs only with no miles, refused for actual expenses (scveh.no_miles). The other differences are value-neutral: for a vehicle that is not a passenger automobile the second takes line 19, which it sets to zero for a 2019 vehicle as the project's column (h) does; for a passenger automobile placed in service in 2019 it reads line 7 (the limit keyed at year 6) where the project reads auto_limit at the recovery year, 7, and tables/2025/auto_limit.yaml gives $5,760 for both ('4th & later' repeated); it takes the first-year amount from its table at year 1 without the special allowance, which is the project's auto_limit_first_nobonus ($10,100 for 2019; a 2019 vehicle that took the allowance is refused by scveh.screen); and it sums the years in another order.

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "10"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent; project retained. Line 15 for an owned vehicle on actual expenses placed in service in the fourth quarter of 2025, zero otherwise, on both sides: the second writes line 15 out as line 13 less line 10 floored at zero, which is the project's scveh.line15 (line 13 less line 14) because line 14 is line 10 for a 2025 vehicle; the project lists q1 to q3 for zero and the second tests q4, and the quarter enumeration is exactly q1 to q4 (params/2025.yaml).

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "10"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent; project retained. Line 15 for an owned 2025 vehicle on actual expenses, zero otherwise, on both sides; the second writes line 15 out as line 13 less line 10 floored at zero, which is the project's scveh.line15 (line 13 less line 14, line 14 being line 10 for a 2025 vehicle), and merges the guards.

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "13"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open: whether the full cost or the business portion counts as the cost of section 179 property. Chosen: the business cost (line 13, as in Form 4562 line 6 column (b), 'Cost (business use only)'). Only vehicles used more than 50% for business reach here, because lower use is refused.

Ruling: equivalent; project retained. Line 13 for a 2025 vehicle on actual expenses and owned, zero otherwise, on both sides; use of 50% or less is refused on line 13.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"const": 1}, {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "larger_of"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); project retained. The business-use percentage differs in precision: the second rounds business miles over total miles to 4 places; the project uses 6 places, half-up, the owner's ruling amb.2025.vehicle_business_pct on i4562 p. 14, Column (c) ('dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles the vehicle is driven for all purposes'; no precision is given). The second's divisor, the larger of 1 and the total miles, differs from the project's total only when no miles are entered, a vehicle on actual expenses the project refuses (scveh.no_miles). The standard mileage branch is the same.

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"const": 1}, {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "larger_of"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open: a lease of 30 days or more may require a reduction by the inclusion amount (Pub. 463), and none of the inputs provided covers it. Chosen: no reduction is made. Under the standard mileage rate, lease payments are not deducted.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); project retained. The business-use percentage differs in precision: the second rounds business miles over total miles to 4 places; the project uses 6 places, half-up, the owner's ruling amb.2025.vehicle_business_pct on i4562 p. 14, Column (c) ('dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles the vehicle is driven for all purposes'; no precision is given). The second's divisor, the larger of 1 and the total miles, differs from the project's total only when no miles are entered, a vehicle on actual expenses the project refuses (scveh.no_miles). The lease inclusion amount the second leaves uncomputed (i1040sc p. 8, Lines 20a and 20b, 'you may have to reduce your deduction by the inclusion amount') is refused in the project by the business screen sc.special ('an inclusion amount for leased property').

### 13 — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"const": 1}, {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "larger_of"}}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); project retained. The business-use percentage differs in precision: the second rounds business miles over total miles to 4 places; the project uses 6 places, half-up, the owner's ruling amb.2025.vehicle_business_pct on i4562 p. 14, Column (c) ('dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles the vehicle is driven for all purposes'; no precision is given). The second's divisor, the larger of 1 and the total miles, differs from the project's total only when no miles are entered, a vehicle on actual expenses the project refuses (scveh.no_miles). Otherwise the same: the cost times the business-use percentage.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "p946.passenger_limits_bonus_first"}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"keys": [{"line": "(b)"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}], "op": "keyed_lookup", "table": "p946.passenger_limits"}}, {"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The worksheet limits apply only to passenger automobiles. For a vehicle not subject to the limits, lines 7, 9, 11, 17, 20 and 25 are zero or not used, and its column (h) comes from line 19.

Ruling: representation; project retained. The same limits from the same Pub. 946 table (i4562 Table 2): for a 2025 vehicle $20,200 with the special allowance and $12,200 without (the project's auto_limit and auto_limit_first_nobonus), and for earlier vehicles the limit of their 2025 recovery year; the second splits the table by allowance and keys 2019 and 2020 vehicles at year 6 where the project keys 2019 at year 7, and tables/2025/auto_limit.yaml gives the same $5,760 for 2019 at years 6 and 7. The second also enters zero for a vehicle that is not a passenger automobile; the project's line 7 is read only through line 9 of the automobile worksheet, which column (h) and the special allowance use only for a passenger automobile (scveh.macrs_pass, scveh.bonus_v).

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"const": 1}, {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "larger_of"}}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); project retained. The business-use percentage differs in precision: the second rounds business miles over total miles to 4 places; the project uses 6 places, half-up, the owner's ruling amb.2025.vehicle_business_pct on i4562 p. 14, Column (c) ('dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles the vehicle is driven for all purposes'; no precision is given). The second's divisor, the larger of 1 and the total miles, differs from the project's total only when no miles are entered, a vehicle on actual expenses the project refuses (scveh.no_miles). Otherwise the same: line 7 times the business-use percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

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
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent; project retained. For a 2025 vehicle, 100% of line 15 when acquired after January 19, 2025 and the full allowance is chosen, 40% when acquired earlier or when the 40% allowance is elected, zero when elected out, on both sides, with the guards arranged differently (the bonus_choice enumeration is exactly full, forty, none, params/2025.yaml); zero for an earlier vehicle on both sides.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}], "op": "keyed_lookup", "table": "pub946.macrs_gds_by_convention"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}], "op": "keyed_lookup", "table": "pub946.macrs_gds_by_convention"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.quarter"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}], "op": "keyed_lookup", "table": "pub946.macrs_gds_mq_by_quarter"}}}], "op": "choose"}}], "op": "choose"}
```

Ruling: equivalent; project retained. Line 18 times the rate chosen by the same convention and recovery-year tests: for 2025 the half-year or mid-quarter rate by the same mid-quarter test, for 2020 to 2024 the rate of the prior convention at the 2025 recovery year, and zero for a 2019 vehicle, the worksheet not being used after the recovery period (Pub. 946 p. 61; BUG-0059), the vehicle's depreciation being figured from the unrecovered basis on both sides. The second spells out the recovery year by placed-in-service year where the project reads the recovery_year table, and names its rate table differently.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.h_dep_refuse | scveh.h_dep_refuse |
| scveh.macrs | scveh.h_dep_refuse | scveh.h_dep_refuse |
| scveh.s179_2025 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| scveh.mq_q4 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| scveh.mq_total | scveh.h_dep_refuse | scveh.h_dep_refuse |
| scveh.cost179 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 9 (scveh.line9) | scveh.h_smr_bad | scveh.h_smr_bad |
| 13 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 7 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 9 (scveh.line9w) | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 10 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 11 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 14 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 15 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 16 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 25 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 17 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 18 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 19 | scveh.h_dep_refuse | scveh.h_dep_refuse |
| 20 | scveh.h_dep_refuse | scveh.h_dep_refuse |

## Raw second transcription

```yaml
```yaml
lines:
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: scveh.h_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: scveh.h_bm_c
    printed: "(helper)"
    label: "Business miles, as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}
  - id: scveh.h_cm_c
    printed: "(helper)"
    label: "Commuting miles, as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}
  - id: scveh.h_om_c
    printed: "(helper)"
    label: "Other miles, as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}
  - id: scveh.h_nonbus_c
    printed: "(helper)"
    label: "Commuting and other miles, as cents"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_cm_c, scveh.h_om_c]}
  - id: scveh.h_total_c
    printed: "(helper)"
    label: "Total miles driven for all purposes, as cents (i4562 column (c))"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_bm_c, scveh.h_cm_c, scveh.h_om_c]}
  - id: scveh.h_whole
    printed: "(helper)"
    label: "Total miles as the divisor of the business/investment-use percentage (at least one cent)"
    type: NonNegDollars
    expr: {op: larger_of, of: [scveh.h_total_c, scveh.h_cent]}
    note: "Open: the IRS text does not cover a vehicle with no miles at all. Chosen: the divisor is at least one, so with no miles the business share comes out as zero and nothing divides by zero."
  - id: scveh.h_over_half
    printed: "(helper)"
    label: "Business use is more than 50% (business miles more than commuting and other miles)"
    type: Bool
    expr: {op: test, gt: [scveh.h_bm_c, scveh.h_nonbus_c]}
  - id: scveh.h_low_use
    printed: "(helper)"
    label: "Business use is 50% or less"
    type: Bool
    expr: {op: test, not: {op: test, eq: [scveh.h_over_half, {const: true}]}}
  - id: scveh.h_actual
    printed: "(helper)"
    label: "Actual expenses are deducted for this vehicle"
    type: Bool
    expr: {op: test, eq: [scveh.method, {const: "actual"}]}
  - id: scveh.h_owned_actual
    printed: "(helper)"
    label: "Owned and on actual expenses (depreciation is claimed)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_actual, {const: true}]}, {op: test, eq: [scveh.owned, {const: true}]}]}
  - id: scveh.h_leased_actual
    printed: "(helper)"
    label: "Leased and on actual expenses"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_actual, {const: true}]}, {op: test, eq: [scveh.owned, {const: false}]}]}
  - id: scveh.h_smr_bad
    printed: "(helper)"
    label: "The standard mileage rate is chosen but not available for this vehicle"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.method, {const: "standard"}]}, {op: test, eq: [scveh.smr_ok, {const: false}]}]}
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
    label: "Business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.h_bm_c, whole: scveh.h_whole, places: 4}
    note: "Open: the business portion is not defined for line 9. Chosen: the mileage ratio of i4562 column (c) (business miles divided by total miles), rounded to 4 decimal places (0.01%), since no rounding is stated."
  - id: scveh.h_line9_actual
    printed: "(helper)"
    label: "Business portion of operating expenses plus parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_operating_business, scveh.parking]}
    note: "Open: the text says to add parking fees and tolls only under the standard mileage rate. Chosen: the business parking fees and tolls are also included under actual expenses (they are a business operating cost of the vehicle)."
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.method, {const: "standard"}]}, then: scveh.h_line9_standard}
        - {guard: {op: test, eq: [scveh.method, {const: "actual"}]}, then: scveh.h_line9_actual}
    refuses: [scveh.h_smr_bad]
  - id: scveh.h_lease_business
    printed: "(helper)"
    label: "The business portion of the lease payments"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.h_bm_c, whole: scveh.h_whole, places: 4}
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease of this vehicle (business portion)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_leased_actual, {const: true}]}, then: scveh.h_lease_business}
        - {guard: {op: test, eq: [scveh.h_leased_actual, {const: false}]}, then: scveh.h_zero}
    note: "Open: a lease of 30 days or more may require a reduction by the inclusion amount (Pub. 463), and none of the inputs provided covers it. Chosen: no reduction is made. Under the standard mileage rate, lease payments are not deducted."
  - id: scveh.h_is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2025"}]}
  - id: scveh.h_is2019
    printed: "(helper)"
    label: "Placed in service in 2019 (2025 is after the recovery period)"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2019"}]}
  - id: scveh.h_too_old
    printed: "(helper)"
    label: "Placed in service before 2019"
    type: Bool
    expr:
      op: test
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
  - id: scveh.h_suv_cap
    printed: "(helper)"
    label: "SUV section 179 limit ($31,300)"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_bus_cost_raw
    printed: "(helper)"
    label: "Multiply column (d) by the percentage in column (c)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.h_bm_c, whole: scveh.h_whole, places: 4}
  - id: scveh.h_s179_bad
    printed: "(helper)"
    label: "The section 179 election is more than the business cost, more than $31,300 for an SUV, or made for a vehicle not placed in service in 2025"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [scveh.s179_elect, scveh.h_bus_cost_raw]}
        - {op: test, all: [{op: test, eq: [scveh.passenger, {const: false}]}, {op: test, eq: [scveh.suv, {const: true}]}, {op: test, gt: [scveh.s179_elect, scveh.h_suv_cap]}]}
        - {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: false}]}, {op: test, gt: [scveh.s179_elect, scveh.h_zero]}]}
  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "The special allowance choice differs within the 5-year class"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.bonus_same, {const: false}]}]}
  - id: scveh.h_dep_refuse
    printed: "(helper)"
    label: "This vehicle's depreciation is outside this tool"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_owned_actual, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [scveh.screen, {const: true}]}
            - {op: test, eq: [scveh.h_too_old, {const: true}]}
            - {op: test, eq: [scveh.h_low_use, {const: true}]}
            - {op: test, eq: [scveh.h_s179_bad, {const: true}]}
            - {op: test, eq: [scveh.h_bonus_mixed, {const: true}]}
    note: "Listed property used 50% or less (straight line over the ADS period, with no section 179 deduction and no special allowance) is not computed here, so it is refused rather than computed."
  - id: scveh.line13
    printed: "13"
    label: "Business/investment cost (cost times business use)"
    type: NonNegDollars
    expr: {op: copy, from: scveh.h_bus_cost_raw}
    refuses: [scveh.h_dep_refuse]
  - id: scveh.h_k1
    printed: "(helper)"
    label: "Year 1 of the recovery period"
    type: Count
    expr: {op: param, ref: sc.year1}
  - id: scveh.h_k2
    printed: "(helper)"
    label: "Year 2 of the recovery period"
    type: Count
    expr: {op: param, ref: sc.year2}
  - id: scveh.h_k3
    printed: "(helper)"
    label: "Year 3 of the recovery period"
    type: Count
    expr: {op: param, ref: sc.year3}
  - id: scveh.h_k4
    printed: "(helper)"
    label: "Year 4 of the recovery period"
    type: Count
    expr: {op: param, ref: sc.year4}
  - id: scveh.h_k5
    printed: "(helper)"
    label: "Year 5 of the recovery period"
    type: Count
    expr: {op: param, ref: sc.year5}
  - id: scveh.h_k6
    printed: "(helper)"
    label: "Year 6 of the recovery period"
    type: Count
    expr: {op: param, ref: sc.year6}
  - id: scveh.h_year
    printed: "(helper)"
    label: "Number of tax years in which this automobile has been in service, counting 2025"
    type: Count
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.placed, {const: "y2025"}]}, then: scveh.h_k1}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2024"}]}, then: scveh.h_k2}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2023"}]}, then: scveh.h_k3}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2022"}]}, then: scveh.h_k4}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2021"}]}, then: scveh.h_k5}
        - {guard: {op: test, eq: [scveh.placed, {const: "y2020"}]}, then: scveh.h_k6}
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
          then: scveh.h_k6
    note: "A 2019 vehicle is in its 7th year. Year 6 is used only to look up its passenger automobile limit, because the '4th & later' amount is the same for every later year. Its MACRS line 19 is zero and its deduction comes from the after-recovery-period rule."
  - id: scveh.h_claims_bonus
    printed: "(helper)"
    label: "A special depreciation allowance is taken for a 2025 vehicle"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, ne: [scveh.bonus_choice, {const: "none"}]}]}
  - id: scveh.h_lim_first_bonus
    printed: "(helper)"
    label: "First-year limit if you take the special depreciation allowance ($20,200 for 2025)"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: p946.passenger_limits_bonus_first, keys: [scveh.placed]}
    note: "Table id chosen here: the first-year amounts with the special allowance, from Pub. 946's 'Maximum Depreciation Deduction for Passenger Automobiles' (2025: $20,200) and the i4562 Table 2 footnote."
  - id: scveh.h_lim_table
    printed: "(helper)"
    label: "Limit from the table for the date placed in service and the year of service (no special allowance in the first year)"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_year]}
    note: "Table id chosen here: Pub. 946 / i4562 Table 2, keyed by year placed in service (2018–2025) and year of service. Year 1 holds the footnoted amount without the special allowance (2025: $12,200; 2019: $10,100). Years 4 and later repeat the '4th & later' amount (2019–2020: $5,760)."
  - id: scveh.h_lim_2025
    printed: "(helper)"
    label: "Limit for a 2025 vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_claims_bonus, {const: true}]}, then: scveh.h_lim_first_bonus}
        - {guard: {op: test, eq: [scveh.h_claims_bonus, {const: false}]}, then: scveh.h_lim_table}
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.h_zero}
        - {guard: {op: test, all: [{op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}]}, then: scveh.h_lim_2025}
        - {guard: {op: test, all: [{op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: false}]}]}, then: scveh.h_lim_table}
    refuses: [scveh.h_dep_refuse]
    note: "The worksheet limits apply only to passenger automobiles. For a vehicle not subject to the limits, lines 7, 9, 11, 17, 20 and 25 are zero or not used, and its column (h) comes from line 19."
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Adjusted maximum depreciation deduction (line 7 times the business/investment-use percentage)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.h_bm_c, whole: scveh.h_whole, places: 4}
  - id: scveh.h_s179_line10
    printed: "(helper)"
    label: "The section 179 election, not more than line 9"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.line9w]}
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_zero}
        - {guard: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.passenger, {const: true}]}]}, then: scveh.h_s179_line10}
        - {guard: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.passenger, {const: false}]}]}, then: scveh.s179_elect}
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
  - id: scveh.h_bonus_full
    printed: "(helper)"
    label: "100% special allowance"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line15}
  - id: scveh.h_bonus_forty
    printed: "(helper)"
    label: "40% special allowance"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}
  - id: scveh.h_bonus_2025
    printed: "(helper)"
    label: "Special allowance for a 2025 vehicle: 100% if acquired after January 19, 2025 without the 40% election; 40% otherwise; zero if elected out"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.bonus_choice, {const: "none"}]}, then: scveh.h_zero}
        - {guard: {op: test, all: [{op: test, eq: [scveh.bonus_choice, {const: "full"}]}, {op: test, eq: [scveh.after_jan19, {const: true}]}]}, then: scveh.h_bonus_full}
        - guard:
            op: test
            all:
              - {op: test, ne: [scveh.bonus_choice, {const: "none"}]}
              - {op: test, not: {op: test, all: [{op: test, eq: [scveh.bonus_choice, {const: "full"}]}, {op: test, eq: [scveh.after_jan19, {const: true}]}]}}
          then: scveh.h_bonus_forty
    note: "Open: what applies to the 'forty' answer for a vehicle acquired before January 20, 2025. Chosen: 40%, the only allowance such property gets."
  - id: scveh.line16
    printed: "16"
    label: "Special depreciation allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_bonus_2025}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.line25
    printed: "25"
    label: "Special depreciation allowance allowed (not more than line 11)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line16, scveh.line11]}
  - id: scveh.line17
    printed: "17"
    label: "Limit on the MACRS depreciation (line 11 less line 16)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line11, take: scveh.line16}
  - id: scveh.line18
    printed: "18"
    label: "Basis for depreciation (line 15 less line 16)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line15, take: scveh.line16}
  - id: scveh.h_y5
    printed: "(helper)"
    label: "Five-year property (automobiles, light general purpose trucks)"
    type: Enum(macrs_period)
    expr: {op: param, ref: sc.period_y5}
  - id: scveh.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: scveh.h_rate_hy
    printed: "(helper)"
    label: "MACRS rate, half-year convention, for the 2025 year of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_by_convention, keys: [scveh.h_y5, scveh.h_hy, scveh.h_year]}
    note: "Table id chosen here: the Pub. 946 Appendix A GDS 200% DB tables (half-year and the four mid-quarter tables), keyed by recovery period, convention and year of recovery."
  - id: scveh.h_rate_mq
    printed: "(helper)"
    label: "MACRS rate, mid-quarter convention for the quarter placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_mq_by_quarter, keys: [scveh.h_y5, scveh.quarter, scveh.h_year]}
    note: "Table id chosen here: the same Pub. 946 mid-quarter tables, keyed by recovery period, quarter placed in service and year of recovery."
  - id: scveh.h_rate_prior
    printed: "(helper)"
    label: "MACRS rate for the 2025 year of recovery, convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_by_convention, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_year]}
  - id: scveh.h_line19_hy
    printed: "(helper)"
    label: "Line 18 times the half-year rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_hy}
  - id: scveh.h_line19_mq
    printed: "(helper)"
    label: "Line 18 times the mid-quarter rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_mq}
  - id: scveh.h_line19_prior
    printed: "(helper)"
    label: "Line 18 (unadjusted basis) times the rate for the 2025 year of recovery"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_prior}
  - id: scveh.h_line19_2025
    printed: "(helper)"
    label: "Line 19 for a 2025 vehicle, half-year or mid-quarter"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [mq.applies, {const: true}]}, then: scveh.h_line19_mq}
        - {guard: {op: test, eq: [mq.applies, {const: false}]}, then: scveh.h_line19_hy}
  - id: scveh.line19
    printed: "19"
    label: "Tentative MACRS depreciation deduction (line 18 times line 6)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_line19_2025}
        - {guard: {op: test, any: [{op: test, eq: [scveh.h_is2019, {const: true}]}, {op: test, eq: [scveh.h_too_old, {const: true}]}]}, then: scveh.h_zero}
        - {guard: {op: test, not: {op: test, any: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.h_is2019, {const: true}]}, {op: test, eq: [scveh.h_too_old, {const: true}]}]}}, then: scveh.h_line19_prior}
  - id: scveh.line20
    printed: "20"
    label: "MACRS depreciation deduction (the lesser of line 17 or line 19)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}
  - id: scveh.h_b100
    printed: "(helper)"
    label: "Cost less the section 179 deduction (as if used 100% for business)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.prior_179}
    note: "Open: the section 179 deduction 'that would have been allowable' at 100% use is not given. Chosen: the section 179 deduction actually claimed in the year placed in service."
  - id: scveh.h_r1
    printed: "(helper)"
    label: "MACRS rate for year 1"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_by_convention, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k1]}
  - id: scveh.h_r2
    printed: "(helper)"
    label: "MACRS rate for year 2"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_by_convention, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k2]}
  - id: scveh.h_r3
    printed: "(helper)"
    label: "MACRS rate for year 3"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_by_convention, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k3]}
  - id: scveh.h_r4
    printed: "(helper)"
    label: "MACRS rate for year 4"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_by_convention, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k4]}
  - id: scveh.h_r5
    printed: "(helper)"
    label: "MACRS rate for year 5"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_by_convention, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k5]}
  - id: scveh.h_r6
    printed: "(helper)"
    label: "MACRS rate for year 6"
    type: Rate
    expr: {op: keyed_lookup, table: pub946.macrs_gds_by_convention, keys: [scveh.h_y5, scveh.prior_conv, scveh.h_k6]}
  - id: scveh.h_l1
    printed: "(helper)"
    label: "Year 1 limit (no special allowance)"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k1]}
  - id: scveh.h_l2
    printed: "(helper)"
    label: "Year 2 limit"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k2]}
  - id: scveh.h_l3
    printed: "(helper)"
    label: "Year 3 limit"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k3]}
  - id: scveh.h_l4
    printed: "(helper)"
    label: "Year 4 limit"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k4]}
  - id: scveh.h_l5
    printed: "(helper)"
    label: "Year 5 limit"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k5]}
  - id: scveh.h_l6
    printed: "(helper)"
    label: "Year 6 limit"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: p946.passenger_limits, keys: [scveh.placed, scveh.h_k6]}
  - id: scveh.h_t1
    printed: "(helper)"
    label: "Year 1 MACRS amount as if used 100% for business"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r1}
  - id: scveh.h_t1s
    printed: "(helper)"
    label: "Year 1 section 179 deduction plus MACRS amount"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.prior_179, scveh.h_t1]}
  - id: scveh.h_d1
    printed: "(helper)"
    label: "Year 1 deduction allowable at 100% business use (the lesser of the amount or the limit)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_l1, scveh.h_t1s]}
  - id: scveh.h_t2
    printed: "(helper)"
    label: "Year 2 MACRS amount as if used 100% for business"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r2}
  - id: scveh.h_d2
    printed: "(helper)"
    label: "Year 2 deduction allowable at 100% business use"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_l2, scveh.h_t2]}
  - id: scveh.h_t3
    printed: "(helper)"
    label: "Year 3 MACRS amount as if used 100% for business"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r3}
  - id: scveh.h_d3
    printed: "(helper)"
    label: "Year 3 deduction allowable at 100% business use"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_l3, scveh.h_t3]}
  - id: scveh.h_t4
    printed: "(helper)"
    label: "Year 4 MACRS amount as if used 100% for business"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r4}
  - id: scveh.h_d4
    printed: "(helper)"
    label: "Year 4 deduction allowable at 100% business use"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_l4, scveh.h_t4]}
  - id: scveh.h_t5
    printed: "(helper)"
    label: "Year 5 MACRS amount as if used 100% for business"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r5}
  - id: scveh.h_d5
    printed: "(helper)"
    label: "Year 5 deduction allowable at 100% business use"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_l5, scveh.h_t5]}
  - id: scveh.h_t6
    printed: "(helper)"
    label: "Year 6 MACRS amount as if used 100% for business"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b100, rate: scveh.h_r6}
  - id: scveh.h_d6
    printed: "(helper)"
    label: "Year 6 deduction allowable at 100% business use"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_l6, scveh.h_t6]}
  - id: scveh.h_d_total
    printed: "(helper)"
    label: "Deductions allowable during the recovery period at 100% business use"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_d1, scveh.h_d2, scveh.h_d3, scveh.h_d4, scveh.h_d5, scveh.h_d6]}
  - id: scveh.h_unrecovered
    printed: "(helper)"
    label: "Unrecovered basis at the end of the recovery period"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.h_d_total}
  - id: scveh.h_post_amount
    printed: "(helper)"
    label: "The lesser of the limit or the unrecovered basis"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line7, scveh.h_unrecovered]}
  - id: scveh.h_post
    printed: "(helper)"
    label: "2025 deduction after the recovery period (times the business/investment-use percentage)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.h_post_amount, part: scveh.h_bm_c, whole: scveh.h_whole, places: 4}
  - id: scveh.h_macrs_pass
    printed: "(helper)"
    label: "Column (h) for a passenger automobile"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2019, {const: true}]}, then: scveh.h_post}
        - {guard: {op: test, eq: [scveh.h_is2019, {const: false}]}, then: scveh.line20}
  - id: scveh.h_macrs_v
    printed: "(helper)"
    label: "Column (h): passenger automobile, or a vehicle not subject to the limits (line 19)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: true}]}, then: scveh.h_macrs_pass}
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.line19}
    note: "Pub. 946: no depreciation after the recovery period for listed property other than passenger automobiles, so a 2019 vehicle not subject to the limits gets zero (line 19)."
  - id: scveh.h_bonus_v
    printed: "(helper)"
    label: "Special allowance for this vehicle (line 25)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: true}]}, then: scveh.line25}
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.line16}
  - id: scveh.bonus
    printed: "(helper)"
    label: "Line 25: special allowance of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_owned_actual, {const: true}]}, then: scveh.h_bonus_v}
        - {guard: {op: test, eq: [scveh.h_owned_actual, {const: false}]}, then: scveh.h_zero}
  - id: scveh.macrs
    printed: "(helper)"
    label: "Column (h): depreciation of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_owned_actual, {const: true}]}, then: scveh.h_macrs_v}
        - {guard: {op: test, eq: [scveh.h_owned_actual, {const: false}]}, then: scveh.h_zero}
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Column (i): elected section 179 cost of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_owned_actual, {const: true}]}, then: scveh.line10}
        - {guard: {op: test, eq: [scveh.h_owned_actual, {const: false}]}, then: scveh.h_zero}
    note: "Column (i) is subject to the limits for passenger automobiles, so it is line 10 (the election capped at line 9 for a passenger automobile)."
  - id: scveh.h_owned_actual_2025
    printed: "(helper)"
    label: "Owned, on actual expenses and placed in service in 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_owned_actual, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}]}
  - id: scveh.h_q4_2025
    printed: "(helper)"
    label: "Owned, on actual expenses and placed in service October to December 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_owned_actual_2025, {const: true}]}, {op: test, eq: [scveh.quarter, {const: "q4"}]}]}
  - id: scveh.h_mq_basis
    printed: "(helper)"
    label: "Depreciable basis for the mid-quarter test (business portion less section 179, before the special allowance)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line13, take: scveh.line10}
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Mid-quarter test basis, fourth quarter of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_q4_2025, {const: true}]}, then: scveh.h_mq_basis}
        - {guard: {op: test, eq: [scveh.h_q4_2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Mid-quarter test basis, 2025 of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_owned_actual_2025, {const: true}]}, then: scveh.h_mq_basis}
        - {guard: {op: test, eq: [scveh.h_owned_actual_2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025 of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_owned_actual_2025, {const: true}]}, then: scveh.line13}
        - {guard: {op: test, eq: [scveh.h_owned_actual_2025, {const: false}]}, then: scveh.h_zero}
    note: "Open: whether the full cost or the business portion counts as the cost of section 179 property. Chosen: the business cost (line 13, as in Form 4562 line 6 column (b), 'Cost (business use only)'). Only vehicles used more than 50% for business reach here, because lower use is refused."
```
```
