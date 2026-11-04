# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 188f739e19ea7dc521c63b15d0fde95ed4b810efe83f27d6daadeea1427e3f84 |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 4351550bba0ad0ad66189ef59fb0dc3db70260625eedc6b897a96239a76dbe7a |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7c9c68d06a7816fe0aa0609dd888de0a8606da885e8a28bebd8ea4d71ead01a6 |
| printed lines compared | 21 |
| agree / disagree / missing | 6 / 15 / 0 |
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

## Lines

### scveh.bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "25"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"line": "16"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"line": "25"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars: classm.scveh.1 and classm.f8962.5.gpt biz_b car_2 $9,918.86/$9,918.39, classm.scveh.5 car_1 $4,998.73/$4,998.50, generated 242 car_1 $6,634.96/$6,634.72. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 2,206 of 2,504 agree; on completed returns 44 value, 2 candidate-unknown (partials of stage14.veh.suv_179 without suv and stage14.veh.2025_179_limit without bonus_same). The remaining differences are records withholding an answer the interview asks of the vehicle (suv, bonus_same, owned, placed_date) and the project's cited vehicle screens on refused returns.

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}], "test": "any"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"line": "20"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars: classm.f8962.4.deepseek car_2 $782.01/$782.03, classm.f8880.2.deepseek spouse car_2 $3,795.31/$3,795.21, classm.asset.1 biz_b car_1 $4,223.68/$4,223.81. The candidate now figures the unrecovered-basis deduction after the recovery period (the backlog-round refusal is gone), agreeing with the project's amb.2025.auto_unrecovered_basis amount to the cent precision. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 1,921 of 2,504 agree; on completed returns 101 value, 2 candidate-unknown (partials). The remaining differences are records withholding an answer the interview asks of the vehicle (suv, bonus_same, owned, placed_date) and the project's cited vehicle screens on refused returns.

### scveh.s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Elected amount before the return-level dollar and business income limits of Form 4562 Part I; only an owned vehicle placed in service in 2025 under actual expenses.

Ruling: representation; i4562 p. 5, Line 6, Column (c), and p. 16, Column (i). The backlog-round employee_use requirement is gone from this line. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 2,331 of 2,504 agree; the one completed-return difference is a partial of stage14.veh.suv_179 withholding scveh.suv, asked of that vehicle; no producible record differs. The remaining differences are records withholding an answer the interview asks of the vehicle (suv, bonus_same, owned, placed_date) and the project's cited vehicle screens on refused returns.

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars: generated 242 car_1 $16,587.41/$16,586.79, the only completed difference (same as the backlog-round ruling). Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 2,176 of 2,504 agree. The remaining differences are records withholding an answer the interview asks of the vehicle (suv, bonus_same, owned, placed_date) and the project's cited vehicle screens on refused returns.

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

Second transcription's note: A vehicle using the standard mileage rate is not depreciated under MACRS and is left out of the mid-quarter test.

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars: classm.scveh.1 and classm.f8962.5.gpt biz_b car_2 $24,797.16/$24,795.98, classm.scveh.5 car_1 $4,998.73/$4,998.50, generated 242 $16,587.41/$16,586.79. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 2,170 of 2,504 agree; on completed returns 44 value, 1 candidate-unknown (partial without suv). The remaining differences are records withholding an answer the interview asks of the vehicle (suv, bonus_same, owned, placed_date) and the project's cited vehicle screens on refused returns.

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

Second transcription's note: Open: line 2 includes listed property from Part V; the cost is read as the business-use cost (line 6 column (b)), and only an owned vehicle depreciated with actual expenses is counted, since the interface supplies no basis for standard-mileage vehicles.

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars (same pairs as scveh.mq_total: classm.scveh.1 biz_b car_2 $24,797.16/$24,795.98, generated 242 $16,587.41/$16,586.79). Both count only an owned 2025 vehicle on actual expenses, at its business-use cost (i4562 p. 4, Line 2). Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 2,159 of 2,504 agree; on completed returns 44 value.

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

Ruling: model error; the candidate needs scveh.employee_use for standard-mileage vehicles (classm.f1040.6.deepseek spouse car_1, classm.f8863.2.deepseek, classm.eic.3.deepseek, classm.f4952.2.deepseek car_1), where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use (same as the backlog-round ruling). The value differences are the business-use precision (amb.2025.vehicle_business_pct): classm.f8962.4.deepseek car_2 $3,606.45/$3,606.54, classm.asset.1 car_2 $6,432.87/$6,432.66. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 1,334 of 2,504 agree; on completed returns 150 candidate-unknown, 107 value.

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

Ruling: model error; the candidate needs scveh.employee_use for standard-mileage vehicles (classm.f1040.6.deepseek spouse car_1, classm.f8863.2.deepseek, classm.eic.3.deepseek, classm.f4952.2.deepseek car_1), where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use (same as the backlog-round ruling). The value differences are the business-use precision (amb.2025.vehicle_business_pct): classm.s8812.3 and .deepseek car_1 $1,370.09/$1,370.15, generated 293 $2,045.22/$2,045.31, generated 355 and 494 car_2. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 1,614 of 2,504 agree; on completed returns 150 candidate-unknown, 19 value.

### 13 — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; the candidate needs scveh.employee_use for standard-mileage vehicles (classm.f1040.6.deepseek spouse car_1, classm.f8863.2.deepseek, classm.eic.3.deepseek, classm.f4952.2.deepseek car_1), where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use (same as the backlog-round ruling). The value differences are the business-use precision (amb.2025.vehicle_business_pct): classm.f8960.1.deepseek, classm.g28.1.deepseek, classm.sd.1.deepseek, classm.u1250.1.deepseek, classm.clcw26.1.deepseek car_1 $2,565.15/$2,565.00, classm.f8962.4.deepseek car_2 $13,576.58/$13,576.90. Project unknowns and refusals on completed returns are worksheet lines of vehicles that do not read them (scveh.bonus_v, scveh.macrs_pass). Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 1,245 of 2,504 agree; on completed returns 150 candidate-unknown, 136 value.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Vehicles placed in service before 2025 are screened if a special allowance was claimed earlier; their later-year limits are the same with or without it. A 2025 vehicle with a 40% or 100% allowance uses the table's first-year amount ($20,200).

Ruling: model error; same as the backlog-round ruling. Pub. 946 Depreciation Worksheet for Passenger Automobiles, line 7. No value differs; the candidate needs scveh.employee_use for standard-mileage vehicles (classm.f1040.6.deepseek spouse car_1, classm.f8863.2.deepseek, classm.eic.3.deepseek, classm.f4952.2.deepseek car_1), where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use (same as the backlog-round ruling). Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 1,688 of 2,504 agree; on completed returns 150 candidate-unknown.

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

Ruling: model error; the candidate needs scveh.employee_use for standard-mileage vehicles (classm.f1040.6.deepseek spouse car_1, classm.f8863.2.deepseek, classm.eic.3.deepseek, classm.f4952.2.deepseek car_1), where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use (same as the backlog-round ruling). The value differences are the business-use precision (amb.2025.vehicle_business_pct): classm.f8960.1.deepseek and four siblings car_1 $2,955.05/$2,954.88, classm.f8962.4.deepseek car_2 $5,363.59/$5,363.71. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 1,137 of 2,504 agree; on completed returns 154 candidate-unknown, 134 value.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; p946 pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 10, "Section 179 deduction claimed this year (not more than line 9)", and i4562 p. 16, Column (i). The candidate enters $0 on the passenger-automobile worksheet line for a vehicle that is not a passenger automobile and takes the election on line 14 directly; the project carries the election through line 10 for every owned actual-expense vehicle. The one completed difference, stage14.veh.suv_179 suv (project $31,300.00, candidate $0.00, and four partials of it), reaches no other amount: both line 14 values are $31,300.00. The backlog-round employee_use requirement is gone from this line. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 2,303 of 2,504 agree; on completed returns 5 value.

### 11 — Subtract line 10 from line 9
Status: **AGREE**

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_179"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"input": "scveh.prior_179"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; p946 Depreciation Worksheet, line 14, "Section 179 deduction claimed in the year you placed the car in service". Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 2,381 of 2,504 agree; the one completed-return difference is a partial of stage14.veh.suv_179 withholding scveh.suv, asked of that vehicle; no producible record differs.

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: 100% for property acquired after January 19, 2025 unless the 40% election is made; 40% for property acquired after September 27, 2017 and before January 20, 2025.

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars: classm.scveh.1 and classm.f8962.5.gpt biz_b car_2 $9,918.86/$9,918.39, classm.scveh.5 car_1 $4,998.73/$4,998.50, generated 242 $6,634.96/$6,634.72. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 2,179 of 2,504 agree; on completed returns 44 value, 2 candidate-unknown (partials). The remaining differences are records withholding an answer the interview asks of the vehicle (suv, bonus_same, owned, placed_date) and the project's cited vehicle screens on refused returns.

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: After the recovery period the unrecovered basis (business portion) stands in for the table amount; line 20 then limits it to line 17.

Ruling: representation; p946 p. 61, Deductions After the Recovery Period, "you can deduct that unrecovered basis after the recovery period ends", and the worksheet's line 19, "Multiply line 18 by line 6" (a table rate the worksheet has none of after the recovery period). The candidate puts the business share of the unrecovered basis on line 19 and limits it by line 20; the project enters $0 on line 19 for a vehicle past its recovery period and deducts the unrecovered basis outside the worksheet (scveh.post, amb.2025.auto_unrecovered_basis). The one large completed difference, classm.asset.1 biz_b car_1 (placed 2019; project $0.00, candidate $10,789.30), reaches the deduction identically to the cent precision (scveh.macrs $4,223.68/$4,223.81). The other value differences are the business-use precision (amb.2025.vehicle_business_pct): classm.f8962.4.deepseek car_2 $782.01/$782.03, classm.asset.1 biz_a car_2 $6,577.09/$6,576.87. Triage executable-triage-v2 (`../triage/scveh.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 1,227 partial records): 1,924 of 2,504 agree; on completed returns 107 value, 2 candidate-unknown (partials).

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| scveh.macrs | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| scveh.s179_2025 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| scveh.mq_q4 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| scveh.mq_total | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| scveh.cost179 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| 9 (scveh.line9) | scveh.employee_use, scveh.h_lease_bad, scveh.h_smr_bad | scveh.employee_use, scveh.h_lease_bad, scveh.h_smr_bad |
| 20a | scveh.employee_use, scveh.h_lease_bad | scveh.employee_use, scveh.h_lease_bad |
| 13 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| 7 | scveh.employee_use, scveh.h_screen_hit | scveh.employee_use, scveh.h_screen_hit |
| 9 (scveh.line9w) | scveh.employee_use, scveh.h_screen_hit | scveh.employee_use, scveh.h_screen_hit |
| 10 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| 11 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| 14 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| 15 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| 16 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| 25 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| 17 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| 18 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| 19 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| 20 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |

## Raw second transcription

```yaml
```yaml
lines:
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: scveh.h_cent
    printed: "(helper)"
    label: "One cent per mile, to express a mile count as a money amount for the business/investment use ratio"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: scveh.h_mb_c
    printed: "(helper)"
    label: "Business miles (44a) expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}
  - id: scveh.h_mc_c
    printed: "(helper)"
    label: "Commuting miles (44b) expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}
  - id: scveh.h_mo_c
    printed: "(helper)"
    label: "Other miles (44c) expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}
  - id: scveh.h_mt_c
    printed: "(helper)"
    label: "Total number of miles the vehicle is driven for all purposes (in cents)"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_mb_c, scveh.h_mc_c, scveh.h_mo_c]}
  - id: scveh.h_two
    printed: "(helper)"
    label: "Two"
    type: Count
    expr: {op: param, ref: sc.count2}
  - id: scveh.h_mb2
    printed: "(helper)"
    label: "Twice the business miles (in cents)"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_mb_c, count: scveh.h_two}
  - id: scveh.h_dep
    printed: "(helper)"
    label: "Owned vehicle for which actual expenses (including depreciation) are deducted"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: true}]}
  - id: scveh.h_new
    printed: "(helper)"
    label: "Depreciated vehicle placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - {op: test, eq: [scveh.placed, {const: "y2025"}]}
  - id: scveh.h_pass
    printed: "(helper)"
    label: "Depreciated vehicle that is a passenger automobile subject to the limits"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - {op: test, eq: [scveh.passenger, {const: true}]}
  - id: scveh.h_pass_new
    printed: "(helper)"
    label: "Passenger automobile placed in service in 2025 and depreciated"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_new, {const: true}]}
        - {op: test, eq: [scveh.passenger, {const: true}]}
  - id: scveh.h_smr_bad
    printed: "(gate)"
    label: "Standard mileage rate taken where it may not be used for 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "standard"}]}
        - {op: test, eq: [scveh.smr_ok, {const: false}]}
  - id: scveh.h_lease_bad
    printed: "(gate)"
    label: "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: false}]}
        - {op: test, eq: [scveh.lease_smr_before, {const: true}]}
  - id: scveh.h_screen_hit
    printed: "(gate)"
    label: "A depreciated vehicle in a situation this tool does not compute"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - {op: test, eq: [scveh.screen, {const: true}]}
  - id: scveh.h_low
    printed: "(gate)"
    label: "Business/investment use (business miles over total miles) is 50% or less"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - {op: test, le: [scveh.h_mb2, scveh.h_mt_c]}
    note: "Consistency check inferred from the column (c) mileage percentage and the screen's exclusion of use of 50% or less; it compares business miles with total miles (qualified business use cannot be larger)."
  - id: scveh.h_bonus_mixed
    printed: "(gate)"
    label: "The special depreciation allowance election differs within the 5-year property class"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_new, {const: true}]}
        - {op: test, eq: [scveh.bonus_same, {const: false}]}
  - id: scveh.h_smr_rate
    printed: "(helper)"
    label: "Business standard mileage rate for 2025 (70 cents per mile)"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}
  - id: scveh.h_smr_miles
    printed: "(helper)"
    label: "Multiply the number of business miles driven by 0.70"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_smr_rate, count: scveh.miles_business}
  - id: scveh.h_smr_total
    printed: "(helper)"
    label: "Add to this amount your parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_smr_miles, scveh.parking]}
  - id: scveh.h_op_bus
    printed: "(helper)"
    label: "The business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}
    note: "The business portion is taken as business miles over total miles (the column (c) rule); the text does not say how to round the ratio, read as 4 decimal places (a percentage to two decimals)."
  - id: scveh.h_actual_total
    printed: "(helper)"
    label: "Business portion of operating expenses plus business parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_op_bus, scveh.parking]}
    note: "The actual-expense instruction lists gasoline, oil, repairs, insurance, license plates 'etc.'; business parking fees and tolls (an input already limited to business use) are read as included on line 9 under actual expenses too."
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses (see instructions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.method, {const: "standard"}]}
          then: scveh.h_smr_total
        - guard: {op: test, eq: [scveh.method, {const: "actual"}]}
          then: scveh.h_actual_total
    refuses: [scveh.h_smr_bad, scveh.h_lease_bad, scveh.employee_use]
  - id: scveh.h_lease_bus
    printed: "(helper)"
    label: "The business portion of your rental cost (vehicle lease payments)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}
    note: "Any inclusion amount for a vehicle leased 30 days or more is outside this slice (Schedule C special screen); ratio rounded to 4 places as for line 9."
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment (this vehicle's business portion)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.method, {const: "actual"}]}
              - {op: test, eq: [scveh.owned, {const: false}]}
          then: scveh.h_lease_bus
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [scveh.method, {const: "actual"}]}
                - {op: test, eq: [scveh.owned, {const: false}]}
          then: scveh.h_zero
    refuses: [scveh.h_lease_bad, scveh.employee_use]
  - id: scveh.h_buscost_calc
    printed: "(helper)"
    label: "Multiply line 12 (cost or other basis) by line 8 (business/investment-use percentage)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}
    note: "Line 8 percentage = business miles / total miles (column (c)); rounding of the percentage is not stated, read as 4 decimal places."
  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_dep, {const: true}]}
          then: scveh.h_buscost_calc
        - guard: {op: test, eq: [scveh.h_dep, {const: false}]}
          then: scveh.h_zero
    refuses: [scveh.h_screen_hit, scveh.employee_use, {when: scveh.h_low, when_known: true}]
    shown_when: scveh.h_dep
  - id: scveh.h_period
    printed: "(helper)"
    label: "5-year property (automobiles, light general purpose trucks)"
    type: Enum(macrs_period)
    expr: {op: param, ref: sc.period_y5}
  - id: scveh.h_conv_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: scveh.h_y1
    printed: "(helper)"
    label: "Year 1"
    type: Count
    expr: {op: param, ref: sc.year1}
  - id: scveh.h_y2
    printed: "(helper)"
    label: "Year 2"
    type: Count
    expr: {op: param, ref: sc.year2}
  - id: scveh.h_y3
    printed: "(helper)"
    label: "Year 3"
    type: Count
    expr: {op: param, ref: sc.year3}
  - id: scveh.h_y4
    printed: "(helper)"
    label: "Year 4"
    type: Count
    expr: {op: param, ref: sc.year4}
  - id: scveh.h_y5
    printed: "(helper)"
    label: "Year 5"
    type: Count
    expr: {op: param, ref: sc.year5}
  - id: scveh.h_y6
    printed: "(helper)"
    label: "Year 6"
    type: Count
    expr: {op: param, ref: sc.year6}
  - id: scveh.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [scveh.placed]}
  - id: scveh.h_last
    printed: "(helper)"
    label: "Last year of the 5-year recovery period"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [scveh.h_period]}
  - id: scveh.h_done
    printed: "(helper)"
    label: "The recovery period ended before your tax year beginning in 2025"
    type: Bool
    expr: {op: test, gt: [scveh.h_year, scveh.h_last]}
  - id: scveh.h_lim_table
    printed: "(helper)"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_year]}
  - id: scveh.h_lim_nobonus
    printed: "(helper)"
    label: "If you elected not to claim any special depreciation allowance, the first-year maximum depreciation deduction"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit_first_nobonus, keys: [scveh.placed]}
  - id: scveh.h_nobonus_case
    printed: "(helper)"
    label: "Passenger automobile placed in service in 2025 for which you elected not to claim any special depreciation allowance"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_pass, {const: true}]}
        - {op: test, eq: [scveh.placed, {const: "y2025"}]}
        - {op: test, eq: [scveh.bonus_choice, {const: "none"}]}
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_pass, {const: false}]}
          then: scveh.h_zero
        - guard: {op: test, eq: [scveh.h_nobonus_case, {const: true}]}
          then: scveh.h_lim_nobonus
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_pass, {const: true}]}
              - {op: test, eq: [scveh.h_nobonus_case, {const: false}]}
          then: scveh.h_lim_table
    refuses: [scveh.h_screen_hit, scveh.employee_use]
    shown_when: scveh.h_pass
    note: "Vehicles placed in service before 2025 are screened if a special allowance was claimed earlier; their later-year limits are the same with or without it. A 2025 vehicle with a 40% or 100% allowance uses the table's first-year amount ($20,200)."
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}
    shown_when: scveh.h_pass
  - id: scveh.h_s179_c1
    printed: "(helper)"
    label: "Elected section 179 cost, not more than the business cost"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.bus_cost]}
  - id: scveh.h_l10_calc
    printed: "(helper)"
    label: "Section 179 deduction claimed this year (not more than line 9)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_s179_c1, scveh.line9w]}
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_pass_new, {const: true}]}
          then: scveh.h_l10_calc
        - guard: {op: test, eq: [scveh.h_pass_new, {const: false}]}
          then: scveh.h_zero
    shown_when: scveh.h_pass
  - id: scveh.line11
    printed: "11"
    label: "Subtract line 10 from line 9. This is the limit on the amount you can deduct for depreciation (including any special depreciation allowance)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line9w, take: scveh.line10}
    shown_when: scveh.h_pass
  - id: scveh.h_suvlim
    printed: "(helper)"
    label: "You cannot elect to expense more than $31,300 of the cost of any SUVs"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_s179_suv
    printed: "(helper)"
    label: "Elected section 179 cost of an SUV, not more than $31,300"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_s179_c1, scveh.h_suvlim]}
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Column (i)—Elected section 179 cost for this vehicle (subject to the limits for passenger automobiles)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new, {const: false}]}
          then: scveh.h_zero
        - guard: {op: test, eq: [scveh.h_pass_new, {const: true}]}
          then: scveh.line10
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_new, {const: true}]}
              - {op: test, eq: [scveh.passenger, {const: false}]}
              - {op: test, eq: [scveh.suv, {const: true}]}
          then: scveh.h_s179_suv
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_new, {const: true}]}
              - {op: test, eq: [scveh.passenger, {const: false}]}
              - {op: test, eq: [scveh.suv, {const: false}]}
          then: scveh.h_s179_c1
    note: "Elected amount before the return-level dollar and business income limits of Form 4562 Part I; only an owned vehicle placed in service in 2025 under actual expenses."
  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new, {const: true}]}
          then: scveh.s179_2025
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_dep, {const: true}]}
              - {op: test, ne: [scveh.placed, {const: "y2025"}]}
          then: scveh.prior_179
        - guard: {op: test, eq: [scveh.h_dep, {const: false}]}
          then: scveh.h_zero
    shown_when: scveh.h_dep
  - id: scveh.line15
    printed: "15"
    label: "Subtract line 14 from line 13. This is your tentative basis for depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.bus_cost, take: scveh.line14}
    shown_when: scveh.h_dep
  - id: scveh.h_bonus40
    printed: "(helper)"
    label: "Multiply line 15 by 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}
  - id: scveh.line16
    printed: "16"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. This is your special depreciation allowance. Enter -0- if this is not the year you placed the car in service, the car is not qualified property, or you elected not to claim a special depreciation allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new, {const: false}]}
          then: scveh.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_new, {const: true}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "none"}]}
          then: scveh.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_new, {const: true}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
              - {op: test, eq: [scveh.after_jan19, {const: true}]}
          then: scveh.line15
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_new, {const: true}]}
              - {op: test, ne: [scveh.bonus_choice, {const: "none"}]}
              - op: test
                not:
                  op: test
                  all:
                    - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
                    - {op: test, eq: [scveh.after_jan19, {const: true}]}
          then: scveh.h_bonus40
    refuses: [scveh.h_bonus_mixed]
    shown_when: scveh.h_dep
    note: "100% for property acquired after January 19, 2025 unless the 40% election is made; 40% for property acquired after September 27, 2017 and before January 20, 2025."
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Special depreciation allowance for this qualified listed property (line 16, limited to line 11)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line16, scveh.line11]}
    shown_when: scveh.h_pass
  - id: scveh.line17
    printed: "17"
    label: "Subtract line 16 from line 11. This is the limit on the amount you can deduct for MACRS depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line11, take: scveh.line16}
    shown_when: scveh.h_pass
  - id: scveh.line18
    printed: "18"
    label: "Subtract line 16 from line 15. This is your basis for depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line15, take: scveh.line16}
    shown_when: scveh.h_dep
  - id: scveh.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [scveh.quarter]}
  - id: scveh.h_rate_hy
    printed: "(helper)"
    label: "Depreciation rate (from tables), half-year convention, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_conv_hy, scveh.h_y1]}
  - id: scveh.h_rate_mq
    printed: "(helper)"
    label: "Depreciation rate (from tables), mid-quarter convention, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_qconv, scveh.h_y1]}
  - id: scveh.h_rate_prior
    printed: "(helper)"
    label: "Depreciation rate (from tables) for the 2025 year of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_year]}
  - id: scveh.h_l19_hy
    printed: "(helper)"
    label: "Multiply line 18 by line 6 (half-year rate)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_hy}
  - id: scveh.h_l19_mq
    printed: "(helper)"
    label: "Multiply line 18 by line 6 (mid-quarter rate)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_mq}
  - id: scveh.h_l19_prior
    printed: "(helper)"
    label: "Multiply line 18 by line 6 (rate for this year of recovery)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_prior}
  - id: scveh.h_basis100
    printed: "(helper)"
    label: "Cost or other basis less section 179 deduction, as if used 100% for business"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.prior_179}
  - id: scveh.h_r1
    printed: "(helper)"
    label: "Rate, year 1 of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y1]}
  - id: scveh.h_r2
    printed: "(helper)"
    label: "Rate, year 2 of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y2]}
  - id: scveh.h_r3
    printed: "(helper)"
    label: "Rate, year 3 of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y3]}
  - id: scveh.h_r4
    printed: "(helper)"
    label: "Rate, year 4 of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y4]}
  - id: scveh.h_r5
    printed: "(helper)"
    label: "Rate, year 5 of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y5]}
  - id: scveh.h_r6
    printed: "(helper)"
    label: "Rate, year 6 of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y6]}
  - id: scveh.h_t1
    printed: "(helper)"
    label: "MACRS depreciation at 100% use, year 1"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_basis100, rate: scveh.h_r1}
  - id: scveh.h_t2
    printed: "(helper)"
    label: "MACRS depreciation at 100% use, year 2"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_basis100, rate: scveh.h_r2}
  - id: scveh.h_t3
    printed: "(helper)"
    label: "MACRS depreciation at 100% use, year 3"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_basis100, rate: scveh.h_r3}
  - id: scveh.h_t4
    printed: "(helper)"
    label: "MACRS depreciation at 100% use, year 4"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_basis100, rate: scveh.h_r4}
  - id: scveh.h_t5
    printed: "(helper)"
    label: "MACRS depreciation at 100% use, year 5"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_basis100, rate: scveh.h_r5}
  - id: scveh.h_t6
    printed: "(helper)"
    label: "MACRS depreciation at 100% use, year 6"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_basis100, rate: scveh.h_r6}
  - id: scveh.h_t1p
    printed: "(helper)"
    label: "Section 179 deduction plus MACRS depreciation at 100% use, year 1"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_t1, scveh.prior_179]}
  - id: scveh.h_lim2
    printed: "(helper)"
    label: "Maximum depreciation deduction, year 2"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y2]}
  - id: scveh.h_lim3
    printed: "(helper)"
    label: "Maximum depreciation deduction, year 3"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y3]}
  - id: scveh.h_lim4
    printed: "(helper)"
    label: "Maximum depreciation deduction, year 4"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y4]}
  - id: scveh.h_lim5
    printed: "(helper)"
    label: "Maximum depreciation deduction, year 5"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y5]}
  - id: scveh.h_lim6
    printed: "(helper)"
    label: "Maximum depreciation deduction, year 6"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y6]}
  - id: scveh.h_a1
    printed: "(helper)"
    label: "Allowable section 179 and depreciation at 100% use, year 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim_nobonus, scveh.h_t1p]}
  - id: scveh.h_a2
    printed: "(helper)"
    label: "Allowable depreciation at 100% use, year 2"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim2, scveh.h_t2]}
  - id: scveh.h_a3
    printed: "(helper)"
    label: "Allowable depreciation at 100% use, year 3"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim3, scveh.h_t3]}
  - id: scveh.h_a4
    printed: "(helper)"
    label: "Allowable depreciation at 100% use, year 4"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim4, scveh.h_t4]}
  - id: scveh.h_a5
    printed: "(helper)"
    label: "Allowable depreciation at 100% use, year 5"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim5, scveh.h_t5]}
  - id: scveh.h_a6
    printed: "(helper)"
    label: "Allowable depreciation at 100% use, year 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim6, scveh.h_t6]}
  - id: scveh.h_asum
    printed: "(helper)"
    label: "Depreciation and section 179 deductions that would have been allowable at 100% business use during the recovery period"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_a1, scveh.h_a2, scveh.h_a3, scveh.h_a4, scveh.h_a5, scveh.h_a6]}
  - id: scveh.h_unrec
    printed: "(helper)"
    label: "Unrecovered basis: cost or other basis reduced by depreciation and section 179 deductions that would have been allowable at 100% use"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.h_asum}
    note: "Used only when the 5-year recovery period (6 tax years) ended before 2025, which for the supported years is a vehicle placed in service in 2019; no special allowance was claimed earlier (screen), so year 1 uses the no-allowance limit."
  - id: scveh.h_unrec_bus
    printed: "(helper)"
    label: "Business/investment portion of the unrecovered basis"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.h_unrec, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}
    note: "Open: the text says to deduct the lesser of the limit (reduced by the business percentage) or the unrecovered basis; the Pub. 946 example recovers the unrecovered basis at the business percentage, so the unrecovered basis is taken at that percentage."
  - id: scveh.line19
    printed: "19"
    label: "Multiply line 18 by line 6. This is your tentative MACRS depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_dep, {const: false}]}
          then: scveh.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_new, {const: true}]}
              - {op: test, eq: [mq.applies, {const: true}]}
          then: scveh.h_l19_mq
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_new, {const: true}]}
              - {op: test, eq: [mq.applies, {const: false}]}
          then: scveh.h_l19_hy
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_dep, {const: true}]}
              - {op: test, ne: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.h_done, {const: false}]}
          then: scveh.h_l19_prior
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_dep, {const: true}]}
              - {op: test, ne: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.h_done, {const: true}]}
          then: scveh.h_unrec_bus
    shown_when: scveh.h_dep
    note: "After the recovery period the unrecovered basis (business portion) stands in for the table amount; line 20 then limits it to line 17."
  - id: scveh.line20
    printed: "20"
    label: "Enter the lesser of line 17 or line 19. This is your MACRS depreciation deduction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}
    shown_when: scveh.h_pass
  - id: scveh.bonus
    printed: "(helper)"
    label: "Special depreciation allowance for this vehicle (Form 4562, line 25)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_dep, {const: false}]}
          then: scveh.h_zero
        - guard: {op: test, eq: [scveh.h_pass, {const: true}]}
          then: scveh.bonus_allowed
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_dep, {const: true}]}
              - {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.line16
  - id: scveh.h_macrs_np
    printed: "(helper)"
    label: "MACRS depreciation of a vehicle not subject to the passenger automobile limits (none after the recovery period)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, ne: [scveh.placed, {const: "y2025"}]}
              - {op: test, eq: [scveh.h_done, {const: true}]}
          then: scveh.h_zero
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, ne: [scveh.placed, {const: "y2025"}]}
                - {op: test, eq: [scveh.h_done, {const: true}]}
          then: scveh.line19
  - id: scveh.macrs
    printed: "(helper)"
    label: "MACRS depreciation deduction for this vehicle (Form 4562, line 26, column (h))"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_dep, {const: false}]}
          then: scveh.h_zero
        - guard: {op: test, eq: [scveh.h_pass, {const: true}]}
          then: scveh.line20
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_dep, {const: true}]}
              - {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.h_macrs_np
  - id: scveh.h_q4
    printed: "(helper)"
    label: "Placed in service in 2025 during the last 3 months of the tax year"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_new, {const: true}]}
        - {op: test, eq: [scveh.quarter, {const: "q4"}]}
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Depreciable basis (after section 179 and personal use, before special allowance) of this vehicle placed in service during the last 3 months of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_q4, {const: true}]}
          then: scveh.line15
        - guard: {op: test, eq: [scveh.h_q4, {const: false}]}
          then: scveh.h_zero
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Depreciable basis (after section 179 and personal use, before special allowance) of this vehicle placed in service during 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new, {const: true}]}
          then: scveh.line15
        - guard: {op: test, eq: [scveh.h_new, {const: false}]}
          then: scveh.h_zero
    note: "A vehicle using the standard mileage rate is not depreciated under MACRS and is left out of the mid-quarter test."
  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost (business use only) of this vehicle as section 179 property placed in service in 2025 (Form 4562, line 2)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new, {const: true}]}
          then: scveh.bus_cost
        - guard: {op: test, eq: [scveh.h_new, {const: false}]}
          then: scveh.h_zero
    note: "Open: line 2 includes listed property from Part V; the cost is read as the business-use cost (line 6 column (b)), and only an owned vehicle depreciated with actual expenses is counted, since the interface supplies no basis for standard-mileage vehicles."
```
```
