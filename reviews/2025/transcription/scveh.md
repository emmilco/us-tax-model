# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
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
{"line": "20"}
```

Second transcription's note: Read as the worksheet's line 20 (MACRS depreciation, column (h)). The special allowance (line 25) and the section 179 amount (column (i)) are reported separately.

Ruling: ambiguity (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"); the reply copies line 20, the lesser of line 17 and line 19, where its own line 19 puts the business share of the unrecovered basis after the recovery period (p946 p. 61, Deductions After the Recovery Period, "you can deduct that unrecovered basis after the recovery period ends"), the reading the refresh round found to reach the project's scveh.post amount (amb.2025.auto_unrecovered_basis) to the precision of the business-use percentage, which the reply rounds to 4 places and the project to 6. Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

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

Second transcription's note: Uses basis after the section 179 reduction and personal use, before any special allowance (Pub. 946 caution). Vehicles under the standard mileage rate are not depreciated under MACRS and are excluded.

Ruling: ambiguity (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"); same line and candidate as the refresh-round ruling: line 15 of an owned actual-expense vehicle placed in the fourth quarter of 2025, zero otherwise; amounts can differ only through the business-use precision of line 13 (4 places in the reply, 6 in the project).
Reviewed in: pass 193dc67d867c

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

Ruling: ambiguity (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"); same line and candidate as the refresh-round ruling (line 15 of an owned actual-expense 2025 vehicle); differences only through the business-use precision of line 13.
Reviewed in: pass 193dc67d867c

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

Second transcription's note: Two points are open. First, whether the business-use cost is meant: I chose it, as for column (b) 'Cost (business use only)'. Second, whether an owned 2025 vehicle under the standard mileage rate is section 179 property: the closed interface gives no cost for it, so it is excluded.

Ruling: ambiguity (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"); same line and candidate as the refresh-round ruling: line 13 for an owned actual-expense 2025 vehicle (i4562 p. 4, Line 2), zero otherwise; differences only through the business-use precision.
Reviewed in: pass 193dc67d867c

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

Second transcription's note: For actual expenses, the i1040sc text names gasoline, oil, repairs, insurance, license plates, 'etc.', and does not mention parking and tolls. I add the business parking and tolls in full, because that input is already limited to business use. The business portion of operating expenses uses the mileage business-use ratio (Form 4562 column (c) method). No rounding is printed, so I round it to 4 places (a percentage to two decimals).

Ruling: ambiguity (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"); the reply's line 9 is the project's (standard mileage: rate times business miles plus parking and tolls; actual: business share of operating expenses plus parking and tolls) with the business share rounded to 4 places instead of 6. The refresh round's model error (scveh.employee_use needed for standard-mileage vehicles) is gone: the reply's scveh.h_emp tests actual expenses first, the project's scveh.employee_bad. Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

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

Second transcription's note: Under the standard mileage rate, lease payments are not deducted, and an owned vehicle has no rent, so both give zero. The lease inclusion amount is not encoded here; it falls under the Schedule C-level screen sc.special, which cannot be referenced from this entry.

Ruling: ambiguity (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"); the business share of the lease payments of a leased actual-expense vehicle, zero otherwise, as the project, at 4 places instead of 6. The lease inclusion amount is refused by sc.special ("an inclusion amount for leased property"). The refresh round's model error (scveh.employee_use needed for standard-mileage vehicles) is gone: the reply's scveh.h_emp tests actual expenses first, the project's scveh.employee_bad. Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

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

Ruling: ambiguity (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"); cost times the business-use percentage (4 places against the project's 6); the reply enters zero for a vehicle that is not owned on actual expenses, where the project's line is hidden. The refresh round's model error (scveh.employee_use needed for standard-mileage vehicles) is gone: the reply's scveh.h_emp tests actual expenses first, the project's scveh.employee_bad. Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": 4, "type": "Count"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "le"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"const": 4, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"line": "(d)"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The worksheet covers passenger automobiles only. Other vehicles have no limit, so I enter the full cost; the limit-driven lines (9, 11, 17) then never bind, and line 20 equals line 19. A 2025 vehicle with no special allowance uses the footnote limit ($12,200). Rows for the 4th and later years are read with year key 4 ('4 or more').

Ruling: representation; p946 Depreciation Worksheet for Passenger Automobiles, line 7. For a passenger automobile the reply's limit is the project's (the first-year limit without the allowance for a 2025 vehicle with no special allowance, otherwise the table for the recovery year, year 4 and later read as one row); for a vehicle that is not a passenger automobile it enters the cost and the project the table amount, a line the project hides there and does not use for such a vehicle (its line 10 takes the election directly). Zero for a vehicle not depreciated, also hidden. The refresh round's model error (scveh.employee_use needed for standard-mileage vehicles) is gone: the reply's scveh.h_emp tests actual expenses first, the project's scveh.employee_bad. Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

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

Second transcription's note: Line 8 (business/investment-use percentage) is business miles divided by total miles (i4562 column (c)). No rounding is printed, so I round it to 4 places.

Ruling: ambiguity (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"); line 7 times the business-use percentage, as the project, at 4 places instead of 6. The refresh round's model error (scveh.employee_use needed for standard-mileage vehicles) is gone: the reply's scveh.h_emp tests actual expenses first, the project's scveh.employee_bad. Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"input": "scveh.s179_elect"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"input": "scveh.s179_elect"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}
```

Second transcription's note: I use the elected amount (Form 4562 column (i)). The return-level dollar and business-income limits are applied on Form 4562 Part I (line 12), not here.

Ruling: representation (+ scope); p946 Depreciation Worksheet, line 10, "Section 179 deduction claimed this year (not more than line 9)"; i4562 p. 16, Column (i), "subject to the limits for passenger automobiles" and "You cannot elect to expense more than $31,300 of the cost of any SUVs". The reply takes the smaller of its column (i) and line 9; for a passenger automobile that is the project's, and for another vehicle line 9 is its business cost, so the result is the election, as the project. An election above the business cost or the SUV limit, which the reply caps, the project refuses (scveh.s179_bad). Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"input": "scveh.prior_179"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; p946 Depreciation Worksheet, line 14, "Section 179 deduction claimed in the year you placed the car in service": line 10 for a 2025 vehicle, scveh.prior_179 for an earlier one, as the project; zero for a vehicle not depreciated, where the line is hidden.
Reviewed in: pass 193dc67d867c

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The rate is 100% when the vehicle was acquired after January 19, 2025, and the 40% election was not made. It is 40% for property acquired before January 20, 2025, or when the 40% election was made.

Ruling: model error and ambiguity; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The rates are the project's (100% after January 19 unless 40% is elected, 40% otherwise, none for none), with the business-use precision (amb.2025.vehicle_business_pct (owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles"). Model error: the reply's line 16 refuses on scveh.h_bonus_mixed (a 2025 depreciated vehicle and scveh.bonus_same false) whatever the choice, so it asks scveh.bonus_same of a vehicle whose choice is none; the project asks it only on the full and forty branches (scveh.bonus_full, scveh.bonus_forty refuse on scveh.bonus_mixed). Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}, {"from": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}], "op": "smaller_of"}], "op": "sum"}}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Line 6 comes from the GDS 5-year tables: half-year or mid-quarter for 2025 (mq.applies), and the original convention for earlier years. If the recovery period ended before 2025, i4562 says to enter the unrecovered basis. Here that is figured at 100% use under Pub. 946 (cost less the section 179 deduction less the deductions allowable each year at the limits) and multiplied by the business percentage; line 20 then applies the limit from line 17. A non-passenger vehicle has nothing left after its recovery period.

Ruling: representation; same reading as the refresh-round ruling: p946 p. 61, Deductions After the Recovery Period, "you can deduct that unrecovered basis after the recovery period ends", and worksheet line 19, "Multiply line 18 by line 6". The reply puts the business share of the unrecovered basis on line 19 after the recovery period and limits it at line 20; the project enters $0 there and deducts the unrecovered basis outside the worksheet (scveh.post, amb.2025.auto_unrecovered_basis). Within the recovery period both take the table rate (half-year or mid-quarter in 2025, the original convention earlier). Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

### (i) — Column (i): elected section 179 cost of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "scveh.s179_elect"}, {"line": "13"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"of": [{"input": "scveh.s179_elect"}, {"line": "13"}], "op": "smaller_of"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"of": [{"input": "scveh.s179_elect"}, {"line": "13"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The election is capped at the business cost, at the passenger automobile limit (line 9) for a passenger automobile, and at $31,300 for an SUV.

Ruling: scope; i4562 p. 16, Column (i)—Elected section 179 cost: "Enter the amount you elect to expense for section 179 property used more than 50% in a qualified business use (subject to the limits for passenger automobiles)" and "You cannot elect to expense more than $31,300 of the cost of any SUVs". The round-2 change prints at (i) the election as limited on line 10 (scveh.s179_2025, shown for owned actual-expense vehicles), which matches this text (regression stage14.veh.2025_179_over_line9). The reply caps the election at the business cost, at $31,300 for an SUV and at line 9 for a passenger automobile; the project computes the same where the election is within those limits and refuses above the business cost or the SUV limit (scveh.s179_bad, remedy "A section 179 election must not exceed the business cost, or $31,300 for an SUV"). No supported return differs. Ruled from reading the pass reply (.transcription/scveh.lines-dcabfc147add) against the project; triage was not rerun.
Reviewed in: pass 193dc67d867c

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| scveh.cost179 | scveh.h_emp, scveh.h_screen_on | scveh.h_emp, scveh.h_screen_on |
| 9 (scveh.line9) | scveh.h_emp, scveh.h_lease_bad, scveh.h_smr_bad | scveh.h_emp, scveh.h_lease_bad, scveh.h_smr_bad |
| 20a | scveh.h_emp, scveh.h_lease_bad | scveh.h_emp, scveh.h_lease_bad |
| 13 | scveh.h_emp, scveh.h_screen_on | scveh.h_emp, scveh.h_screen_on |
| 7 | scveh.h_screen_on | scveh.h_screen_on |
| 9 (scveh.line9w) | scveh.h_emp, scveh.h_screen_on | scveh.h_emp, scveh.h_screen_on |
| 10 | scveh.h_emp, scveh.h_screen_on | scveh.h_emp, scveh.h_screen_on |
| 11 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| 14 | scveh.h_emp, scveh.h_screen_on | scveh.h_emp, scveh.h_screen_on |
| 15 | scveh.employee_use, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_low, scveh.h_screen_hit |
| 16 | scveh.h_bonus_mixed | scveh.h_bonus_mixed |
| 25 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| 17 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| 18 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| 19 | scveh.h_screen_on | scveh.h_screen_on |
| 20 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_low, scveh.h_screen_hit |
| (i) | scveh.h_emp, scveh.h_screen_on | scveh.h_emp, scveh.h_screen_on |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| scveh.bonus | 7425f6d51ea90cd9ff72eb27f0672df7d12a3c8ffbf698178ef8ea753f0813d5 |
| scveh.macrs | b52cadf7cefe3eb0ad52beffe4299cb633ea5f2ebec12a61b11d28b9e5c892b4 |
| scveh.mq_q4 | e87c38f3de8e892ef89051ca425237c2d3a88b6d4d57ee2e21908fa5595e9a17 |
| scveh.mq_total | 752b0c852ae65f8534b69da55b0914ae392ddce0969666870089d5369c742390 |
| scveh.cost179 | b9284c906dde91d30404268244a3106631d7484d8be955cb87ad42ee49be8236 |
| 9 (scveh.line9) | fd6e93271a636af56e83875440f8d5c4eea11b772e292ead8b47fcf8150191b0 |
| 20a | ebb99519f2d5422d5c05df554aaeb027a8b92e1e4de17caef875df759a068f14 |
| 13 | ad30e20ce61b6a9d0ca5a29b93f47bf52f3c76d33c1b486f7cbafcc7e06222ed |
| 7 | 6cc8374bc617cf3381181ce68d0538dc0deeaec49b3db3177057474eafa91d7d |
| 9 (scveh.line9w) | ec8cbef8abc7fb1b525a9fab1bfdfda47ecea99038fd0372d66f0e0514763fb0 |
| 10 | d099b0bcb8868574f75d226d5f0bfebb1c10b7a88f871e825f0c2e616a9810fa |
| 11 | f3e85797dfa9c61ea3dba37c314323ade46f8815f1298e9f52d7e60c8aeab545 |
| 14 | 0549e960f8fc2e8c6b1f5b99cd77778f90463bf84df53fe4e22dd0aa4d5a3a37 |
| 15 | a07da2424e619aba780a22a10702d061aae34c157ecf41cafc82ac4bb7c9f562 |
| 16 | 8e3a1cdbbeb58ab6168efa48f53c372e713274a160ce32900c215a597e0f7fa0 |
| 25 | 746e62ed919bd87a00c9a145d958aa5f66e4986d17ae5f57ddef1b37c4df1311 |
| 17 | 16b79e629877618e290196ee418fcbf21e616d1bf1be09fa597cf20c99ce86bd |
| 18 | 4edd35878a26aa88e85f5910fc2362247442845083a0182877e97e9fb46b791e |
| 19 | 26dc224ba739a8efa871c8b6bd6fe48bb4779a13a30ad9e1cb5663f7ecd3871d |
| 20 | 206cd08b7782f70880b7f6e9387d474514acd62177736cd6b68d74001d9b1b1f |
| (i) | 1804b7a1bb1465ecf3dd57c2712dd1eaa18d2d7f94fa9113e0da7062080426d4 |
| (rest of the document) | 228bd5866d2384f5dcd66bb73109f0d7b60abe097d790ea6a014d7c89bede259 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| scveh.macrs | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| scveh.mq_q4 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| scveh.mq_total | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| scveh.cost179 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 9 (scveh.line9) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 20a | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 13 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 7 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 9 (scveh.line9w) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 10 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 14 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 16 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 19 | 14ab4862811584dfd01cb4c921ce8aa19deac170e103f50c05485c1ee3465442 |
| (i) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 193dc67d867c

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines scveh.macrs, scveh.mq_q4, scveh.mq_total, scveh.cost179, 9 (scveh.line9), 20a, 13, 7, 9 (scveh.line9w), 10, 14, 16, 19, (i) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 193dc67d867cc3a749cbc057c5a026dbef81302755adc392de64010b3d0512b1 |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | dc6d6c293629154da75bb2709ea80fa7beb6694c46cd93a3b63deabedbeb2011 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | e88a75a29e5db638cf2f47d23a535c6427e9d07253fd354b057d59b2ef01d967 |
| receipt | .transcription/scveh.lines-dcabfc147add |
| printed lines compared | 14 |
| agree / disagree / missing | 0 / 14 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 17, 31, 34, 37, 41, 59, 60, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dcprov, dependent, f1040, f2441, f5329, household, s1, s1a, s2, sa, scope |
| named line | ltc |
| shared page | asset, carloan, f4562, mq, person, s179, sc |

##### Raw second transcription

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
          then: scveh.h_smr_total
        - guard: {op: test, eq: [scveh.method, {const: "actual"}]}
          then: scveh.h_actual_total
    refuses: [scveh.h_smr_bad, scveh.h_lease_bad, scveh.h_emp]
    note: "For actual expenses, the i1040sc text names gasoline, oil, repairs, insurance, license plates, 'etc.', and does not mention parking and tolls. I add the business parking and tolls in full, because that input is already limited to business use. The business portion of operating expenses uses the mileage business-use ratio (Form 4562 column (c) method). No rounding is printed, so I round it to 4 places (a percentage to two decimals)."

  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment (business portion of your rental cost) — this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.owned, {const: false}]}]}
          then: scveh.h_lease_bus
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.owned, {const: false}]}]}}
          then: scveh.h_zero
    refuses: [scveh.h_lease_bad, scveh.h_emp]
    note: "Under the standard mileage rate, lease payments are not deducted, and an owned vehicle has no rent, so both give zero. The lease inclusion amount is not encoded here; it falls under the Schedule C-level screen sc.special, which cannot be referenced from this entry."

  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_depr, {const: true}]}
          then: scveh.h_bus_cost_calc
        - guard: {op: test, eq: [scveh.h_depr, {const: false}]}
          then: scveh.h_zero
    refuses: [scveh.h_screen_on, scveh.h_emp]
    shown_when: scveh.h_depr

  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_depr, {const: false}]}
          then: scveh.h_zero
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.passenger, {const: false}]}]}
          then: scveh.cost
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_nb, {const: true}]}]}
          then: scveh.h_lim_first_nb
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_nb, {const: false}]}, {op: test, ge: [scveh.h_year, {const: 4, type: Count}]}]}
          then: scveh.h_lim_y4
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.passenger, {const: true}]}, {op: test, eq: [scveh.h_nb, {const: false}]}, {op: test, lt: [scveh.h_year, {const: 4, type: Count}]}]}
          then: scveh.h_lim_year
    refuses: [scveh.h_screen_on]
    shown_when: scveh.h_depr
    note: "The worksheet covers passenger automobiles only. Other vehicles have no limit, so I enter the full cost; the limit-driven lines (9, 11, 17) then never bind, and line 20 equals line 19. A 2025 vehicle with no special allowance uses the footnote limit ($12,200). Rows for the 4th and later years are read with year key 4 ('4 or more')."

  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}
    refuses: [scveh.h_emp]
    shown_when: scveh.h_depr
    note: "Line 8 (business/investment-use percentage) is business miles divided by total miles (i4562 column (c)). No rounding is printed, so I round it to 4 places."

  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_2025, scveh.line9w]}
    shown_when: scveh.h_depr
    note: "I use the elected amount (Form 4562 column (i)). The return-level dollar and business-income limits are applied on Form 4562 Part I (line 12), not here."

  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new_depr, {const: true}]}
          then: scveh.line10
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.h_new_depr, {const: false}]}]}
          then: scveh.prior_179
        - guard: {op: test, eq: [scveh.h_depr, {const: false}]}
          then: scveh.h_zero
    shown_when: scveh.h_depr

  - id: scveh.line16
    printed: "16"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. This is your special depreciation allowance. Enter -0- if this is not the year you placed the car in service, the car is not qualified property, or you elected not to claim a special depreciation allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new_depr, {const: false}]}
          then: scveh.h_zero
        - guard: {op: test, all: [{op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "none"}]}]}
          then: scveh.h_zero
        - guard: {op: test, all: [{op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "full"}]}, {op: test, eq: [scveh.after_jan19, {const: true}]}]}
          then: scveh.line15
        - guard: {op: test, all: [{op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, any: [{op: test, all: [{op: test, eq: [scveh.bonus_choice, {const: "full"}]}, {op: test, eq: [scveh.after_jan19, {const: false}]}]}, {op: test, eq: [scveh.bonus_choice, {const: "forty"}]}]}]}
          then: scveh.h_bonus40
    refuses: [scveh.h_bonus_mixed]
    shown_when: scveh.h_depr
    note: "The rate is 100% when the vehicle was acquired after January 19, 2025, and the 40% election was not made. It is 40% for property acquired before January 20, 2025, or when the 40% election was made."

  - id: scveh.line19
    printed: "19"
    label: "Multiply line 18 by line 6. This is your tentative MACRS depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_depr, {const: false}]}
          then: scveh.h_zero
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.h_after, {const: true}]}, {op: test, eq: [scveh.passenger, {const: true}]}]}
          then: scveh.h_unrec_bus
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.h_after, {const: true}]}, {op: test, eq: [scveh.passenger, {const: false}]}]}
          then: scveh.h_zero
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.h_after, {const: false}]}, {op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, eq: [mq.applies, {const: true}]}]}
          then: scveh.h_m_mq
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.h_after, {const: false}]}, {op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, eq: [mq.applies, {const: false}]}]}
          then: scveh.h_m_hy
        - guard: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.h_after, {const: false}]}, {op: test, eq: [scveh.h_new_depr, {const: false}]}]}
          then: scveh.h_m_prior
    refuses: [scveh.h_screen_on]
    shown_when: scveh.h_depr
    note: "Line 6 comes from the GDS 5-year tables: half-year or mid-quarter for 2025 (mq.applies), and the original convention for earlier years. If the recovery period ended before 2025, i4562 says to enter the unrecovered basis. Here that is figured at 100% use under Pub. 946 (cost less the section 179 deduction less the deductions allowable each year at the limits) and multiplied by the business percentage; line 20 then applies the limit from line 17. A non-passenger vehicle has nothing left after its recovery period."

  - id: scveh.s179_2025
    printed: "(i)"
    label: "Elected section 179 cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new_depr, {const: true}]}
          then: scveh.h_elect
        - guard: {op: test, eq: [scveh.h_new_depr, {const: false}]}
          then: scveh.h_zero
    shown_when: scveh.h_new_depr
    note: "The election is capped at the business cost, at the passenger automobile limit (line 9) for a passenger automobile, and at $31,300 for an SUV."

  - id: scveh.macrs
    printed: "(helper)"
    label: "Depreciation deduction, Form 4562 line 26 column (h), for this vehicle"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line20}
    note: "Read as the worksheet's line 20 (MACRS depreciation, column (h)). The special allowance (line 25) and the section 179 amount (column (i)) are reported separately."

  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Depreciable basis of this vehicle if placed in service in the last 3 months of 2025 (mid-quarter test)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, eq: [scveh.quarter, {const: "q4"}]}]}
          then: scveh.line15
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, eq: [scveh.quarter, {const: "q4"}]}]}}
          then: scveh.h_zero
    note: "Uses basis after the section 179 reduction and personal use, before any special allowance (Pub. 946 caution). Vehicles under the standard mileage rate are not depreciated under MACRS and are excluded."

  - id: scveh.mq_total
    printed: "(helper)"
    label: "Depreciable basis of this vehicle if placed in service in 2025 (mid-quarter test)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new_depr, {const: true}]}
          then: scveh.line15
        - guard: {op: test, eq: [scveh.h_new_depr, {const: false}]}
          then: scveh.h_zero

  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost of this vehicle as section 179 property placed in service in 2025 (Form 4562 line 2, listed property from Part V)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_new_depr, {const: true}]}
          then: scveh.bus_cost
        - guard: {op: test, eq: [scveh.h_new_depr, {const: false}]}
          then: scveh.h_zero
    note: "Two points are open. First, whether the business-use cost is meant: I chose it, as for column (b) 'Cost (business use only)'. Second, whether an owned 2025 vehicle under the standard mileage rate is section 179 property: the closed interface gives no cost for it, so it is excluded."

  # ---------- helpers ----------
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: scveh.h_cent
    printed: "(helper)"
    label: "One cent per mile (to express miles as a money-scaled amount)"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}

  - id: scveh.h_mb_c
    printed: "(helper)"
    label: "Business miles (scaled)"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}

  - id: scveh.h_mc_c
    printed: "(helper)"
    label: "Commuting miles (scaled)"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}

  - id: scveh.h_mo_c
    printed: "(helper)"
    label: "Other miles (scaled)"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}

  - id: scveh.h_mt_c
    printed: "(helper)"
    label: "Total miles driven for all purposes (scaled)"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_mb_c, scveh.h_mc_c, scveh.h_mo_c]}

  - id: scveh.h_rate70
    printed: "(helper)"
    label: "Standard mileage rate, 70 cents per mile"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}

  - id: scveh.h_smr_amt
    printed: "(helper)"
    label: "Multiply the number of business miles driven by 0.70"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_rate70, count: scveh.miles_business}

  - id: scveh.h_smr_total
    printed: "(helper)"
    label: "Add to this amount your parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_smr_amt, scveh.parking]}

  - id: scveh.h_op_bus
    printed: "(helper)"
    label: "Business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}

  - id: scveh.h_actual_total
    printed: "(helper)"
    label: "Actual expenses: business operating expenses plus business parking and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_op_bus, scveh.parking]}

  - id: scveh.h_lease_bus
    printed: "(helper)"
    label: "Business portion of lease payments for this vehicle"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}

  - id: scveh.h_smr_bad
    printed: "(helper)"
    label: "Standard mileage rate claimed but not allowed for this vehicle"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.method, {const: "standard"}]}, {op: test, eq: [scveh.smr_ok, {const: false}]}]}

  - id: scveh.h_lease_bad
    printed: "(helper)"
    label: "Actual expenses for a leased vehicle after the standard mileage rate was used, or a 2025 conversion"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.owned, {const: false}]}, {op: test, eq: [scveh.lease_smr_before, {const: true}]}]}

  - id: scveh.h_emp
    printed: "(helper)"
    label: "Actual expenses with employee personal use (business percentage not figured by miles)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.employee_use, {const: true}]}]}

  - id: scveh.h_depr
    printed: "(helper)"
    label: "Owned vehicle with actual expenses (depreciation claimed)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.owned, {const: true}]}]}

  - id: scveh.h_new_depr
    printed: "(helper)"
    label: "Depreciated vehicle placed in service in 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.placed, {const: "y2025"}]}]}

  - id: scveh.h_screen_on
    printed: "(helper)"
    label: "Depreciated vehicle outside the tool's scope"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_depr, {const: true}]}, {op: test, eq: [scveh.screen, {const: true}]}]}

  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "Special allowance choice differs within 2025 5-year property"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, eq: [scveh.bonus_same, {const: false}]}]}

  - id: scveh.h_nb
    printed: "(helper)"
    label: "Placed in service in 2025 and elected not to claim any special allowance"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_new_depr, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "none"}]}]}

  - id: scveh.h_year
    printed: "(helper)"
    label: "Number of tax years in which this automobile has been in service (year of recovery in 2025)"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [scveh.placed]}

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

  - id: scveh.h_lim_first_nb
    printed: "(helper)"
    label: "First-year limit if you elected not to claim any special depreciation allowance"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit_first_nobonus, keys: [scveh.placed]}

  - id: scveh.h_lim_year
    printed: "(helper)"
    label: "Limit for the year of service (1st to 3rd year)"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_year]}

  - id: scveh.h_lim_y4
    printed: "(helper)"
    label: "Limit for the 4th and later years"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y4]}

  - id: scveh.h_bus_cost_calc
    printed: "(helper)"
    label: "Cost or other basis multiplied by the business/investment-use percentage"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}

  - id: scveh.h_elect_cap1
    printed: "(helper)"
    label: "Elected section 179 cost, not more than the business cost"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.bus_cost]}

  - id: scveh.h_suv_lim
    printed: "(helper)"
    label: "SUV section 179 limit ($31,300)"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}

  - id: scveh.h_elect_suv
    printed: "(helper)"
    label: "Elected section 179 cost of an SUV, not more than $31,300"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_elect_cap1, scveh.h_suv_lim]}

  - id: scveh.h_elect_pass
    printed: "(helper)"
    label: "Elected section 179 cost of a passenger automobile, subject to the limit"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_elect_cap1, scveh.line9w]}

  - id: scveh.h_elect
    printed: "(helper)"
    label: "Elected section 179 cost after vehicle limits"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.passenger, {const: true}]}
          then: scveh.h_elect_pass
        - guard: {op: test, all: [{op: test, eq: [scveh.passenger, {const: false}]}, {op: test, eq: [scveh.suv, {const: true}]}]}
          then: scveh.h_elect_suv
        - guard: {op: test, all: [{op: test, eq: [scveh.passenger, {const: false}]}, {op: test, eq: [scveh.suv, {const: false}]}]}
          then: scveh.h_elect_cap1

  - id: scveh.h_bonus40
    printed: "(helper)"
    label: "Line 15 multiplied by 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}

  - id: scveh.h_period
    printed: "(helper)"
    label: "Recovery period: 5-year property (automobiles)"
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
    expr: {op: keyed_lookup, table: quarter_convention, keys: [scveh.quarter]}

  - id: scveh.h_last
    printed: "(helper)"
    label: "Last year of recovery for 5-year property"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [scveh.h_period]}

  - id: scveh.h_after
    printed: "(helper)"
    label: "The recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [scveh.h_year, scveh.h_last]}

  - id: scveh.h_rate_hy
    printed: "(helper)"
    label: "Depreciation rate, half-year convention (Table A-1)"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_hy, scveh.h_year]}

  - id: scveh.h_rate_mq
    printed: "(helper)"
    label: "Depreciation rate, mid-quarter convention (Tables A-2 to A-5)"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_qconv, scveh.h_year]}

  - id: scveh.h_rate_prior
    printed: "(helper)"
    label: "Depreciation rate, convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_year]}

  - id: scveh.h_m_hy
    printed: "(helper)"
    label: "Line 18 multiplied by the half-year rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_hy}

  - id: scveh.h_m_mq
    printed: "(helper)"
    label: "Line 18 multiplied by the mid-quarter rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_mq}

  - id: scveh.h_m_prior
    printed: "(helper)"
    label: "Line 18 multiplied by the rate for the year of recovery"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_prior}

  - id: scveh.h_b0
    printed: "(helper)"
    label: "Cost reduced by the section 179 deduction (at 100% business use)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.prior_179}

  - id: scveh.h_l1net
    printed: "(helper)"
    label: "First-year limit less the section 179 deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.h_lim_first_nb, take: scveh.prior_179}

  - id: scveh.h_r1
    printed: "(helper)"
    label: "Rate, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y1]}

  - id: scveh.h_r2
    printed: "(helper)"
    label: "Rate, year 2"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y2]}

  - id: scveh.h_r3
    printed: "(helper)"
    label: "Rate, year 3"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y3]}

  - id: scveh.h_r4
    printed: "(helper)"
    label: "Rate, year 4"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y4]}

  - id: scveh.h_r5
    printed: "(helper)"
    label: "Rate, year 5"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y5]}

  - id: scveh.h_r6
    printed: "(helper)"
    label: "Rate, year 6"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y6]}

  - id: scveh.h_p1
    printed: "(helper)"
    label: "MACRS amount, year 1 (100% use)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b0, rate: scveh.h_r1}

  - id: scveh.h_p2
    printed: "(helper)"
    label: "MACRS amount, year 2 (100% use)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b0, rate: scveh.h_r2}

  - id: scveh.h_p3
    printed: "(helper)"
    label: "MACRS amount, year 3 (100% use)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b0, rate: scveh.h_r3}

  - id: scveh.h_p4
    printed: "(helper)"
    label: "MACRS amount, year 4 (100% use)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b0, rate: scveh.h_r4}

  - id: scveh.h_p5
    printed: "(helper)"
    label: "MACRS amount, year 5 (100% use)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b0, rate: scveh.h_r5}

  - id: scveh.h_p6
    printed: "(helper)"
    label: "MACRS amount, year 6 (100% use)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b0, rate: scveh.h_r6}

  - id: scveh.h_lim2
    printed: "(helper)"
    label: "Limit, 2nd year"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y2]}

  - id: scveh.h_lim3
    printed: "(helper)"
    label: "Limit, 3rd year"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y3]}

  - id: scveh.h_d1
    printed: "(helper)"
    label: "Allowable depreciation, year 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_l1net, scveh.h_p1]}

  - id: scveh.h_d2
    printed: "(helper)"
    label: "Allowable depreciation, year 2"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim2, scveh.h_p2]}

  - id: scveh.h_d3
    printed: "(helper)"
    label: "Allowable depreciation, year 3"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim3, scveh.h_p3]}

  - id: scveh.h_d4
    printed: "(helper)"
    label: "Allowable depreciation, year 4"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim_y4, scveh.h_p4]}

  - id: scveh.h_d5
    printed: "(helper)"
    label: "Allowable depreciation, year 5"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim_y4, scveh.h_p5]}

  - id: scveh.h_d6
    printed: "(helper)"
    label: "Allowable depreciation, year 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_lim_y4, scveh.h_p6]}

  - id: scveh.h_dsum
    printed: "(helper)"
    label: "Total depreciation allowable during the recovery period (100% use)"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_d1, scveh.h_d2, scveh.h_d3, scveh.h_d4, scveh.h_d5, scveh.h_d6]}

  - id: scveh.h_unrec
    printed: "(helper)"
    label: "Unrecovered basis at the end of the recovery period"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.h_b0, take: scveh.h_dsum}
    note: "Pub. 946: cost reduced by the depreciation and section 179 deductions that would have been allowable at 100% business use under the limits. No special allowance is included, because an earlier-year allowance is screened out."

  - id: scveh.h_unrec_bus
    printed: "(helper)"
    label: "Unrecovered basis multiplied by the business/investment-use percentage"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.h_unrec, part: scveh.h_mb_c, whole: scveh.h_mt_c, places: 4}
```
```

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
