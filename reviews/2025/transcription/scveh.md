# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0487c576caac5f65483e554cb86521cd068bd0947d13b4a712b73796767ce13c |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | ac5ee9848d8a3b1556dbba6398f1debf9bbf2558eb575b6044648fbeb5132edc |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 55812896d927256ba9c411debba4b3892548772c0dbf99c208b83ba573413953 |
| printed lines compared | 21 |
| agree / disagree / missing | 4 / 17 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 31, 34, 37, 41, 59, 60, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 31, 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

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

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars. The candidate also reads answers the source does not need there (scveh.screen, one completed return). executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 2,814 of 3,051 agree; 121 candidate-unknown, 71 project-refuses, 27 value, 10 project-unknown, 8 candidate-refuses; on completed returns: 5 value, 1 candidate-unknown. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.scveh.1 sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.scveh.5 sc[biz_a].scveh[car_1] $4,998.73/$4,998.50; generated 242 sc[biz_a].scveh[car_1] $6,634.96/$6,634.72.

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "20"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars. The candidate refuses an owned actual-expense vehicle past its recovery period (h_post_recovery), where the project computes the unrecovered-basis deduction under amb.2025.auto_unrecovered_basis (owner accepted; p946 chapter 5, Deductions After the Recovery Period). executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 2,196 of 3,051 agree; 367 value, 324 candidate-refuses, 89 candidate-unknown, 70 project-refuses, 5 project-unknown; on completed returns: 93 candidate-refuses, 69 value, 1 candidate-unknown. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_1] $58.66/$58.64; classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.f8880.2.deepseek sc[biz_a].scveh[car_2] $3,795.31/$3,795.21; classm.f8962.5.gpt sc[biz_b].scveh[car_1] $58.66/$58.64; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.asset.1 sc[biz_a].scveh[car_2] $6,577.09/$6,576.87; classm.f8880.2 sc[biz_a].scveh[car_2] $3,795.31/$3,795.21; classm.sc.1 sc[biz_a].scveh[car_1] $2,074.40/$2,074.46; classm.scveh.1 sc[biz_b].scveh[car_1] $58.66/$58.64; classm.scveh.1 sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.f8962.4 sc[biz_a].scveh[car_2] $782.01/$782.03; generated 97 sc[biz_a].scveh[car_1] $2,858.08/$2,858.14; generated 162 sc[biz_a].scveh[car_1] $3,860.27/$3,860.44; generated 238 sc[biz_a].scveh[car_2] $2,810.65/$2,810.81; generated 242 sc[biz_a].scveh[car_1] $497.62/$497.60; generated 253 sc[biz_a].scveh[car_1] $11,106.35/$11,106.81; generated 254 sc[biz_a].scveh[car_1] $5,592.24/$5,592.11; generated 261 sc[biz_a].scveh[car_1] $5,774.77/$5,774.59; generated 355 sc[biz_a].scveh[car_1] $5,484.46/$5,484.37; generated 403 sc[biz_a].scveh[car_1] $907.12/$907.16; generated 482 sc[biz_a].scveh[car_2] $1,566.01/$1,566.00; and 48 partial records built on those bases with the same pairs.

### scveh.s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "10"}
```

Ruling: model error; i4562 p. 5, Line 6, Column (c). The candidate needs scveh.employee_use for standard-mileage vehicles, where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4, "the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen"); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use. That requirement is a model error. It also asks scveh.screen of vehicles that do not read it. No value differs on a completed return. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 1,928 of 3,051 agree; 895 candidate-unknown, 125 project-unknown, 72 project-refuses, 29 candidate-refuses, 2 value; on completed returns: 198 candidate-unknown.

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}, "op": "subtract_floor0", "take": {"line": "10"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 2,777 of 3,051 agree; 179 project-unknown, 71 project-refuses, 23 value, 1 candidate-unknown; on completed returns: 1 value. Completed-return value differences (project/candidate): generated 242 sc[biz_a].scveh[car_1] $16,587.41/$16,586.79.

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}, "op": "subtract_floor0", "take": {"line": "10"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate prorates at four places (hundredths of a percent, the register's rejected second reading). The project takes line 15 (business cost less section 179) for an owned 2025 actual-expense vehicle; the candidate figures the same at four places. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 2,723 of 3,051 agree; 137 project-unknown, 81 candidate-unknown, 72 project-refuses, 35 value, 3 candidate-refuses; on completed returns: 5 value. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.scveh.1 sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.scveh.5 sc[biz_a].scveh[car_1] $4,998.73/$4,998.50; generated 242 sc[biz_a].scveh[car_1] $16,587.41/$16,586.79.

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Line 2 includes listed property. The text gives no rule for a vehicle on the standard mileage rate. This transcription counts only an owned vehicle placed in service in 2025 and depreciated under actual expenses, at its business-use cost.

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate prorates at four places (hundredths of a percent, the register's rejected second reading). Both count only an owned 2025 vehicle on actual expenses, at its business-use cost (i4562 p. 4, Line 2). executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 2,704 of 3,051 agree; 140 project-unknown, 86 project-refuses, 83 candidate-unknown, 38 value; on completed returns: 5 value. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.scveh.1 sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.scveh.5 sc[biz_a].scveh[car_1] $4,998.73/$4,998.50; generated 242 sc[biz_a].scveh[car_1] $16,587.41/$16,586.79.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "ne"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}], "op": "sum"}}], "op": "choose"}
```

Second transcription's note: The text lists parking fees and tolls only under the standard mileage rate. Under actual expenses, line 9 includes 'the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.' The parking input covers business use only and is excluded from the operating input, so this transcription also adds it in full under actual expenses.

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars. The candidate unknowns withhold owned or lease_smr_before on refused or incomplete records. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 2,302 of 3,051 agree; 721 value, 25 candidate-unknown, 2 project-refuses, 1 candidate-refuses; on completed returns: 104 value. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_1] $934.67/$934.66; classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $3,162.05/$3,161.90; classm.f8880.2.deepseek sc[biz_a].scveh[car_1] $5,267.97/$5,267.93; classm.f8880.2.deepseek sc[biz_a].scveh[car_2] $3,659.27/$3,659.16; classm.f8962.5.gpt sc[biz_b].scveh[car_1] $934.67/$934.66; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $3,162.05/$3,161.90; classm.asset.1 sc[biz_a].scveh[car_2] $6,432.87/$6,432.66; classm.asset.1 sc[biz_b].scveh[car_1] $2,811.72/$2,811.81; classm.f8880.2 sc[biz_a].scveh[car_1] $5,267.97/$5,267.93; classm.f8880.2 sc[biz_a].scveh[car_2] $3,659.27/$3,659.16; classm.f8995.3 sc[biz_b].scveh[car_1] $5,640.43/$5,640.50; classm.sc.1 sc[biz_a].scveh[car_1] $3,919.68/$3,919.79; classm.scveh.1 sc[biz_b].scveh[car_1] $934.67/$934.66; classm.scveh.1 sc[biz_b].scveh[car_2] $3,162.05/$3,161.90; classm.f8962.4 sc[biz_a].scveh[car_2] $3,606.45/$3,606.54; generated 97 sc[biz_a].scveh[car_1] $2,466.72/$2,466.77; generated 163 sc[biz_a].scveh[car_1] $5,649.88/$5,649.48; generated 238 sc[biz_a].scveh[car_2] $5,577.32/$5,577.63; generated 242 sc[biz_a].scveh[car_1] $2,494.97/$2,494.87; generated 253 sc[biz_a].scveh[car_1] $6,445.22/$6,445.46; generated 254 sc[biz_a].scveh[car_1] $1,903.08/$1,903.03; generated 261 sc[biz_a].scveh[car_1] $6,901.10/$6,900.88; generated 293 sc[biz_a].scveh[car_1] $3,595.28/$3,595.44; generated 355 sc[biz_a].scveh[car_1] $7,644.53/$7,644.40; generated 355 sc[biz_a].scveh[car_2] $1,603.23/$1,603.14; generated 402 sc[biz_a].scveh[car_1] $1,092.56/$1,092.60; generated 403 sc[biz_a].scveh[car_1] $8,216.51/$8,216.84; generated 494 sc[biz_a].scveh[car_2] $472.66/$472.64; and 76 partial records built on those bases with the same pairs.

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

Second transcription's note: For a lease of 30 days or more, the deduction may have to be reduced by the inclusion amount (Pub. 463). The text supplied here gives no way to figure that amount, so it is not computed. Under the standard mileage rate, no lease payments are deducted.

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars. The candidate refusals at scveh.employee_use are on refused records. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 2,891 of 3,051 agree; 134 value, 20 candidate-refuses, 5 candidate-unknown, 1 project-refuses; on completed returns: 5 value. Completed-return value differences (project/candidate): classm.s8812.3.deepseek sc[biz_a].scveh[car_1] $1,370.09/$1,370.15; classm.s8812.3 sc[biz_a].scveh[car_1] $1,370.09/$1,370.15; generated 293 sc[biz_a].scveh[car_1] $2,045.22/$2,045.31; generated 355 sc[biz_a].scveh[car_2] $1,548.41/$1,548.33; generated 494 sc[biz_a].scveh[car_2] $2,102.97/$2,102.89.

### 13 — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "20"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "25"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second transcription's note: This vehicle's section 179 amount (Form 4562 line 26 column (i)) reaches Schedule C line 13 through Form 4562 line 12, after the business income limit. It is therefore reported through scveh.s179_2025 and not added here. This line holds the vehicle's line 25 and line 26(h) amounts.

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars. The candidate refuses an owned actual-expense vehicle past its recovery period (h_post_recovery), where the project computes the unrecovered-basis deduction under amb.2025.auto_unrecovered_basis (owner accepted; p946 chapter 5, Deductions After the Recovery Period). The other completed value differences are standard-mileage vehicles, where the candidate enters $0 and the project figures the worksheet line it does not read for them. Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 271 of 3,051 agree; 1,379 value, 606 project-refuses, 333 candidate-refuses, 239 project-unknown, 223 candidate-unknown; on completed returns: 184 value, 93 candidate-refuses, 82 project-refuses, 34 project-unknown. Completed-return value differences (project/candidate): classm.f4952.2.deepseek sc[biz_a].scveh[car_1] $30,291.48/$0.00; classm.f8962.5.deepseek sc[biz_a].scveh[car_1] $43,355.22/$0.00; classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $24,797.16/$12,893.91; classm.f8962.5.deepseek sc[biz_b].scveh[car_1] $7,534.44/$58.64; classm.f8880.2.deepseek sc[biz_a].scveh[car_2] $34,471.51/$3,795.21; classm.f1040.4.deepseek sc[biz_a].scveh[car_1] $27,603.48/$14,353.81; classm.f1040.6.deepseek sc[biz_a].scveh[car_1] $14,090.51/$0.00; classm.eic.3.deepseek sc[biz_a].scveh[car_1] $79,387.12/$0.00; classm.f8962.5.gpt sc[biz_a].scveh[car_1] $43,355.22/$0.00; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $24,797.16/$12,893.91; classm.f8962.5.gpt sc[biz_b].scveh[car_1] $7,534.44/$58.64; classm.asset.1 sc[biz_a].scveh[car_2] $20,553.41/$6,576.87; classm.f8880.2 sc[biz_a].scveh[car_2] $34,471.51/$3,795.21; classm.f8995.2 sc[biz_a].scveh[car_1] $63,926.73/$0.00; classm.f8995.2 sc[biz_a].scveh[car_2] $34,635.63/$1,995.01; classm.f8995.3 sc[biz_b].scveh[car_1] $3,600.35/$207.38; classm.sc.1 sc[biz_a].scveh[car_1] $18,006.95/$2,074.46; classm.scveh.1 sc[biz_a].scveh[car_1] $43,355.22/$0.00; classm.scveh.1 sc[biz_b].scveh[car_2] $24,797.16/$12,893.91; classm.scveh.1 sc[biz_b].scveh[car_1] $7,534.44/$58.64; classm.scveh.5 sc[biz_a].scveh[car_1] $4,998.73/$4,998.50; classm.se.2 sc[biz_a].scveh[car_1] $16,893.62/$0.00; classm.sli.4 sc[biz_a].scveh[car_1] $57,010.47/$0.00; classm.ssb.4 sc[biz_a].scveh[car_1] $57,010.47/$0.00; classm.f1040.4 sc[biz_a].scveh[car_1] $27,603.48/$14,353.81; classm.f1040.6 sc[biz_a].scveh[car_1] $14,090.51/$0.00; classm.f8962.4 sc[biz_a].scveh[car_2] $13,576.58/$782.03; mutation.t2.mfj_sdtw_skip23 sc[biz_a].scveh[car_1] $30,291.48/$0.00; stage14.veh.2025_bonus sc[rides].scveh[car] $32,000.00/$16,160.00; stage14.veh.2025_mq_nobonus sc[rides].scveh[car] $30,000.00/$1,500.00; stage14.veh.2023_prior sc[rides].scveh[car] $15,000.00/$2,880.00; stage14.veh.suv_179 sc[haul].scveh[suv] $70,000.00/$38,700.00; stage14.veh.2025_nobonus_hy sc[r].scveh[car] $27,000.00/$5,400.00; stage14.veh.2025_179_limit sc[r].scveh[car] $90,000.00/$7,200.00; stage14.veh.2025_forty sc[r].scveh[car] $30,000.00/$15,600.00; stage14.veh.2022_mq sc[r].scveh[car] $50,000.00/$6,460.00; stage14.veh.2024_prior179 sc[r].scveh[car] $10,500.00/$2,720.00; stage14.veh.heavy_prior sc[r].scveh[truck] $60,000.00/$11,520.00; f2.t101.credit_disallowed_eic_zero sc[biz_a].scveh[car_1] $57,010.47/$0.00; generated 20 sc[biz_a].scveh[car_2] $50,864.16/$0.00; generated 97 sc[biz_a].scveh[car_1] $25,958.97/$2,858.14; generated 162 sc[biz_a].scveh[car_1] $33,509.26/$3,860.44; generated 170 sc[biz_a].scveh[car_1] $48,784.72/$0.00; generated 238 sc[biz_a].scveh[car_1] $51,947.34/$0.00; generated 238 sc[biz_a].scveh[car_2] $18,017.00/$2,810.81; generated 242 sc[biz_a].scveh[car_1] $16,587.41/$7,132.32; generated 253 sc[biz_a].scveh[car_1] $69,176.40/$11,106.81; generated 253 sc[biz_a].scveh[car_2] $29,103.43/$0.00; generated 254 sc[biz_a].scveh[car_1] $48,543.77/$5,592.11; generated 261 sc[biz_a].scveh[car_1] $45,131.58/$5,774.59; generated 261 sc[biz_a].scveh[car_2] $7,267.98/$0.00; generated 355 sc[biz_a].scveh[car_1] $70,346.47/$5,484.37; generated 402 sc[biz_b].scveh[car_1] $59,352.35/$0.00; generated 403 sc[biz_a].scveh[car_1] $65,733.34/$907.16; generated 403 sc[biz_a].scveh[car_2] $21,874.16/$0.00; generated 482 sc[biz_a].scveh[car_2] $4,121.09/$1,566.00; generated 482 sc[biz_b].scveh[car_1] $31,922.51/$0.00; and 127 partial records built on those bases with the same pairs.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Ruling: model error; Pub. 946 Depreciation Worksheet for Passenger Automobiles, line 7. No value differs. The candidate needs scveh.employee_use for standard-mileage vehicles, where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4, "the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen"); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use. That requirement is a model error. Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 1,709 of 3,051 agree; 598 project-refuses, 587 candidate-unknown, 132 project-unknown, 25 candidate-refuses; on completed returns: 99 candidate-unknown, 85 project-refuses, 2 project-unknown.

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

Second transcription's note: Line 8 is the business/investment-use percentage: business miles divided by total miles (i4562 column (c)). The text does not state its precision. This transcription rounds the ratio to 4 decimal places (a percentage to two decimals).

Ruling: model error; The candidate needs scveh.employee_use for standard-mileage vehicles, where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4, "the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen"); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use. That requirement is a model error. The value differences are the business-use precision (ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars.) Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 417 of 3,051 agree; 1,424 value, 598 project-refuses, 587 candidate-unknown, 25 candidate-refuses; on completed returns: 194 value, 99 candidate-unknown, 85 project-refuses. Completed-return value differences (project/candidate): classm.f4952.1.deepseek sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.f4952.2.deepseek sc[biz_a].scveh[car_2] $18,705.66/$18,705.20; classm.f8960.1.deepseek sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.g28.1.deepseek sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.sd.1.deepseek sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.u1250.1.deepseek sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.clcw26.1.deepseek sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $14,007.35/$14,006.68; classm.f8962.5.deepseek sc[biz_b].scveh[car_1] $3,988.45/$3,988.22; classm.f8880.2.deepseek sc[biz_a].scveh[car_1] $5,729.52/$5,729.47; classm.f8880.2.deepseek sc[biz_a].scveh[car_2] $5,619.31/$5,619.15; classm.s8812.3.deepseek sc[biz_a].scveh[car_1] $12,802.13/$12,802.68; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $14,007.35/$14,006.68; classm.f8962.5.gpt sc[biz_b].scveh[car_1] $3,988.45/$3,988.22; classm.asset.1 sc[biz_a].scveh[car_2] $18,499.75/$18,499.14; classm.asset.1 sc[biz_b].scveh[car_1] $4,223.68/$4,223.81; classm.f8880.2 sc[biz_a].scveh[car_1] $5,729.52/$5,729.47; classm.f8880.2 sc[biz_a].scveh[car_2] $5,619.31/$5,619.15; classm.f8960.1 sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.f8995.3 sc[biz_b].scveh[car_1] $4,081.48/$4,081.54; classm.g28.1 sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.sc.1 sc[biz_a].scveh[car_1] $5,810.61/$5,810.78; classm.scveh.1 sc[biz_b].scveh[car_2] $14,007.35/$14,006.68; classm.scveh.1 sc[biz_b].scveh[car_1] $3,988.45/$3,988.22; classm.scveh.5 sc[biz_a].scveh[car_1] $20,194.87/$20,193.94; classm.sd.1 sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.sdtw.1 sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.u1250.1 sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.clcw26.1 sc[biz_a].scveh[car_1] $2,955.05/$2,954.88; classm.f8962.4 sc[biz_a].scveh[car_2] $5,363.59/$5,363.71; mutation.t2.mfj_sdtw_skip23 sc[biz_a].scveh[car_2] $18,705.66/$18,705.20; generated 20 sc[biz_a].scveh[car_1] $9,211.53/$9,211.41; generated 20 sc[biz_a].scveh[car_2] $4,852.44/$4,852.75; generated 97 sc[biz_a].scveh[car_1] $5,486.01/$5,486.13; generated 97 sc[biz_a].scveh[car_2] $5,290.05/$5,289.98; generated 162 sc[biz_a].scveh[car_1] $5,049.33/$5,049.56; generated 163 sc[biz_a].scveh[car_1] $3,849.68/$3,849.41; generated 170 sc[biz_a].scveh[car_1] $4,226.31/$4,226.23; generated 170 sc[biz_a].scveh[car_2] $5,325.91/$5,325.70; generated 238 sc[biz_a].scveh[car_1] $11,127.27/$11,127.62; generated 238 sc[biz_a].scveh[car_2] $6,842.94/$6,843.33; generated 242 sc[biz_a].scveh[car_1] $16,653.51/$16,652.88; generated 253 sc[biz_a].scveh[car_1] $11,106.35/$11,106.81; generated 253 sc[biz_a].scveh[car_2] $4,843.54/$4,843.58; generated 254 sc[biz_a].scveh[car_1] $5,947.86/$5,947.72; generated 261 sc[biz_a].scveh[car_1] $5,774.77/$5,774.59; generated 261 sc[biz_a].scveh[car_2] $11,763.37/$11,763.24; generated 293 sc[biz_a].scveh[car_1] $3,299.03/$3,299.18; generated 355 sc[biz_a].scveh[car_1] $5,484.46/$5,484.37; generated 355 sc[biz_a].scveh[car_2] $4,152.04/$4,151.81; generated 402 sc[biz_a].scveh[car_1] $4,606.13/$4,606.27; generated 402 sc[biz_b].scveh[car_1] $4,962.52/$4,962.24; generated 403 sc[biz_a].scveh[car_1] $4,732.80/$4,732.99; generated 403 sc[biz_a].scveh[car_2] $7,067.64/$7,067.97; generated 482 sc[biz_a].scveh[car_2] $13,824.52/$13,824.36; generated 482 sc[biz_b].scveh[car_1] $16,248.45/$16,247.88; generated 494 sc[biz_a].scveh[car_2] $10,040.96/$10,040.58; and 137 partial records built on those bases with the same pairs.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "(i)"}, {"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"of": [{"line": "(i)"}, {"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}], "op": "smaller_of"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"of": [{"line": "(i)"}, {"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}], "op": "smaller_of"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Vehicles that are not passenger automobiles are not subject to the line 9 limit. For them, this line holds the elected column (i) cost, capped at the business cost. For an SUV it is also capped at the $31,300 limit.

Ruling: model error; no value differs on a completed return. The candidate needs scveh.employee_use for standard-mileage vehicles, where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4, "the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen"); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use. That requirement is a model error. Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 1,715 of 3,051 agree; 600 project-refuses, 585 candidate-unknown, 141 project-unknown, 8 candidate-refuses, 2 value; on completed returns: 99 candidate-unknown, 85 project-refuses, 3 project-unknown.

### 11 — Subtract line 10 from line 9
Status: **AGREE**

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"from": {"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Ruling: model error; The candidate needs scveh.employee_use for standard-mileage vehicles, where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4, "the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen"); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use. That requirement is a model error. The value differences are the business-use precision (ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate prorates at four places (hundredths of a percent, the register's rejected second reading).) Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 633 of 3,051 agree; 1,250 value, 601 project-refuses, 525 candidate-unknown, 39 project-unknown, 3 candidate-refuses; on completed returns: 160 value, 88 candidate-unknown, 85 project-refuses, 2 project-unknown. Completed-return value differences (project/candidate): classm.f4952.1.deepseek sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.f8960.1.deepseek sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.g28.1.deepseek sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.sd.1.deepseek sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.u1250.1.deepseek sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.clcw26.1.deepseek sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.f8962.5.deepseek sc[biz_b].scveh[car_1] $1,018.44/$1,018.00; classm.f8880.2.deepseek sc[biz_a].scveh[car_1] $4,973.54/$4,973.50; classm.f8880.2.deepseek sc[biz_a].scveh[car_2] $34,471.51/$34,470.54; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.f8962.5.gpt sc[biz_b].scveh[car_1] $1,018.44/$1,018.00; classm.asset.1 sc[biz_a].scveh[car_2] $20,553.41/$20,552.73; classm.asset.1 sc[biz_b].scveh[car_1] $47,588.21/$47,589.70; classm.f8880.2 sc[biz_a].scveh[car_1] $4,973.54/$4,973.50; classm.f8880.2 sc[biz_a].scveh[car_2] $34,471.51/$34,470.54; classm.f8960.1 sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.f8995.3 sc[biz_b].scveh[car_1] $3,600.35/$3,600.40; classm.g28.1 sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.sc.1 sc[biz_a].scveh[car_1] $18,006.95/$18,007.46; classm.scveh.1 sc[biz_b].scveh[car_2] $24,797.16/$24,795.98; classm.scveh.1 sc[biz_b].scveh[car_1] $1,018.44/$1,018.00; classm.scveh.5 sc[biz_a].scveh[car_1] $4,998.73/$4,998.50; classm.sd.1 sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.sdtw.1 sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.u1250.1 sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.clcw26.1 sc[biz_a].scveh[car_1] $2,565.15/$2,565.00; classm.f8962.4 sc[biz_a].scveh[car_2] $13,576.58/$13,576.90; generated 20 sc[biz_a].scveh[car_2] $50,864.16/$50,867.48; generated 97 sc[biz_a].scveh[car_1] $25,958.97/$25,959.52; generated 162 sc[biz_a].scveh[car_1] $33,509.26/$33,510.77; generated 163 sc[biz_a].scveh[car_1] $1,522.33/$1,521.59; generated 170 sc[biz_a].scveh[car_1] $48,784.72/$48,783.77; generated 238 sc[biz_a].scveh[car_1] $51,947.34/$51,948.99; generated 238 sc[biz_a].scveh[car_2] $18,017.00/$18,018.02; generated 242 sc[biz_a].scveh[car_1] $16,587.41/$16,586.79; generated 253 sc[biz_a].scveh[car_1] $69,176.40/$69,179.24; generated 253 sc[biz_a].scveh[car_2] $29,103.43/$29,103.71; generated 254 sc[biz_a].scveh[car_1] $48,543.77/$48,542.66; generated 261 sc[biz_a].scveh[car_1] $45,131.58/$45,130.17; generated 261 sc[biz_a].scveh[car_2] $7,267.98/$7,267.90; generated 355 sc[biz_a].scveh[car_1] $61,868.32/$61,867.19; generated 402 sc[biz_a].scveh[car_1] $12,714.94/$12,715.33; generated 402 sc[biz_b].scveh[car_1] $53,406.12/$53,402.82; generated 403 sc[biz_a].scveh[car_1] $65,733.34/$65,735.98; generated 403 sc[biz_a].scveh[car_2] $21,874.16/$21,875.17; generated 482 sc[biz_a].scveh[car_2] $4,121.09/$4,121.04; generated 482 sc[biz_b].scveh[car_1] $31,922.51/$31,921.38; and 112 partial records built on those bases with the same pairs.

### 16 — Special depreciation allowance
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Property acquired after January 19, 2025 gets 100% unless the 40% election is made. Property acquired before January 20, 2025 (and after September 27, 2017, per the screen) is limited to 40%.

Ruling: ambiguity (amb.2025.vehicle_business_pct, owner's ruling); i4562 p. 14, Column (c), "determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles". The project prorates at six places, half-up; the candidate at another precision, so amounts differ by cents to a few dollars. The candidate unknowns withhold scveh.screen of vehicles that do not read it. Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 2,045 of 3,051 agree; 620 project-refuses, 202 project-unknown, 127 candidate-unknown, 46 value, 11 candidate-refuses; on completed returns: 85 project-refuses, 16 project-unknown, 5 candidate-unknown, 5 value. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.scveh.1 sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.scveh.5 sc[biz_a].scveh[car_1] $4,998.73/$4,998.50; generated 242 sc[biz_a].scveh[car_1] $6,634.96/$6,634.72.

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

Second transcription's note: Pub. 946 worksheet: if line 16 equals line 11, stop, because depreciation including the special allowance is limited to line 11. This transcription reads that as the smaller of line 16 or line 11 for passenger automobiles.

Ruling: model error; The candidate needs scveh.employee_use for standard-mileage vehicles, where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4, "the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen"); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use. That requirement is a model error. It also asks passenger and screen answers the project does not need. The value differences are the business-use precision (amb.2025.vehicle_business_pct) and stage14.veh.suv_179, a vehicle that is not a passenger automobile, where the worksheet line is not used (Pub. 946 pp. 61-62; the project takes line 16 directly, scveh.bonus_o) and the project shows $0. Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 1,936 of 3,051 agree; 604 project-refuses, 415 candidate-unknown, 44 value, 41 project-unknown, 11 candidate-refuses; on completed returns: 85 project-refuses, 68 candidate-unknown, 6 value, 5 project-unknown. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.scveh.1 sc[biz_b].scveh[car_2] $9,918.86/$9,918.39; classm.scveh.5 sc[biz_a].scveh[car_1] $4,998.73/$4,998.50; stage14.veh.suv_179 sc[haul].scveh[suv] $0.00/$38,700.00; generated 242 sc[biz_a].scveh[car_1] $6,634.96/$6,634.72.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second transcription's note: Deductions after the recovery period (unrecovered basis) need every prior year's allowable depreciation, which the closed input interface does not provide. Those years are refused.

Ruling: model error; The candidate needs scveh.employee_use for standard-mileage vehicles, where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4, "the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen"); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use. That requirement is a model error. The candidate refuses an owned actual-expense vehicle past its recovery period (h_post_recovery), where the project computes the unrecovered-basis deduction under amb.2025.auto_unrecovered_basis (owner accepted; p946 chapter 5, Deductions After the Recovery Period). The value differences are the business-use precision (amb.2025.vehicle_business_pct). Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 624 of 3,051 agree; 801 value, 599 candidate-refuses, 581 project-refuses, 429 candidate-unknown, 17 project-unknown; on completed returns: 162 candidate-refuses, 85 project-refuses, 76 value, 54 candidate-unknown. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_1] $58.66/$58.64; classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.f8880.2.deepseek sc[biz_a].scveh[car_2] $3,795.31/$3,795.21; classm.f8962.5.gpt sc[biz_b].scveh[car_1] $58.66/$58.64; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.asset.1 sc[biz_a].scveh[car_2] $6,577.09/$6,576.87; classm.f8880.2 sc[biz_a].scveh[car_2] $3,795.31/$3,795.21; classm.sc.1 sc[biz_a].scveh[car_1] $2,074.40/$2,074.46; classm.scveh.1 sc[biz_b].scveh[car_1] $58.66/$58.64; classm.scveh.1 sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.f8962.4 sc[biz_a].scveh[car_2] $782.01/$782.03; generated 20 sc[biz_a].scveh[car_2] $5,859.55/$5,859.93; generated 97 sc[biz_a].scveh[car_1] $2,858.08/$2,858.14; generated 162 sc[biz_a].scveh[car_1] $3,860.27/$3,860.44; generated 170 sc[biz_a].scveh[car_1] $5,620.00/$5,619.89; generated 238 sc[biz_a].scveh[car_1] $7,792.10/$7,792.35; generated 238 sc[biz_a].scveh[car_2] $2,810.65/$2,810.81; generated 242 sc[biz_a].scveh[car_1] $497.62/$497.60; generated 253 sc[biz_a].scveh[car_1] $12,451.75/$12,452.26; generated 253 sc[biz_a].scveh[car_2] $2,788.11/$2,788.14; generated 254 sc[biz_a].scveh[car_1] $5,592.24/$5,592.11; generated 261 sc[biz_a].scveh[car_1] $6,174.00/$6,173.81; generated 261 sc[biz_a].scveh[car_2] $1,453.60/$1,453.58; generated 355 sc[biz_a].scveh[car_1] $7,127.23/$7,127.10; generated 403 sc[biz_a].scveh[car_1] $907.12/$907.16; generated 403 sc[biz_a].scveh[car_2] $4,199.84/$4,200.03; generated 482 sc[biz_a].scveh[car_2] $1,566.01/$1,566.00; generated 482 sc[biz_b].scveh[car_1] $8,299.85/$8,299.56; and 48 partial records built on those bases with the same pairs.

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

Ruling: model error; The candidate needs scveh.employee_use for standard-mileage vehicles, where the project asks it only of actual-expense vehicles (scveh.operating_business; BUG-0371, owner decision A4, "the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen"); i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes", is the depreciation percentage, which a standard-mileage vehicle does not use. That requirement is a model error. The candidate refuses an owned actual-expense vehicle past its recovery period (h_post_recovery), where the project computes the unrecovered-basis deduction under amb.2025.auto_unrecovered_basis (owner accepted; p946 chapter 5, Deductions After the Recovery Period). The value differences are the business-use precision (amb.2025.vehicle_business_pct); for a vehicle that is not a passenger automobile the project takes line 19 directly (scveh.macrs_heavy). Project refusals and unknowns on completed returns are worksheet lines of standard-mileage or non-passenger vehicles, which the project figures for every entry but does not read there (scveh.bonus_v, scveh.macrs_pass), so the return completes. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/scveh.json; 1,495 fixtures, 500 generated returns seed 20261026, 1,331 partial records): 641 of 3,051 agree; 765 value, 583 project-refuses, 563 candidate-refuses, 486 candidate-unknown, 13 project-unknown; on completed returns: 159 candidate-refuses, 85 project-refuses, 76 value, 57 candidate-unknown. Completed-return value differences (project/candidate): classm.f8962.5.deepseek sc[biz_b].scveh[car_1] $58.66/$58.64; classm.f8962.5.deepseek sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.f8880.2.deepseek sc[biz_a].scveh[car_2] $3,795.31/$3,795.21; classm.f8962.5.gpt sc[biz_b].scveh[car_1] $58.66/$58.64; classm.f8962.5.gpt sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.asset.1 sc[biz_a].scveh[car_2] $6,577.09/$6,576.87; classm.f8880.2 sc[biz_a].scveh[car_2] $3,795.31/$3,795.21; classm.sc.1 sc[biz_a].scveh[car_1] $2,074.40/$2,074.46; classm.scveh.1 sc[biz_b].scveh[car_1] $58.66/$58.64; classm.scveh.1 sc[biz_b].scveh[car_2] $2,975.66/$2,975.52; classm.f8962.4 sc[biz_a].scveh[car_2] $782.01/$782.03; generated 20 sc[biz_a].scveh[car_2] $4,852.44/$4,852.75; generated 97 sc[biz_a].scveh[car_1] $2,858.08/$2,858.14; generated 162 sc[biz_a].scveh[car_1] $3,860.27/$3,860.44; generated 170 sc[biz_a].scveh[car_1] $4,226.31/$4,226.23; generated 238 sc[biz_a].scveh[car_1] $7,792.10/$7,792.35; generated 238 sc[biz_a].scveh[car_2] $2,810.65/$2,810.81; generated 242 sc[biz_a].scveh[car_1] $497.62/$497.60; generated 253 sc[biz_a].scveh[car_1] $11,106.35/$11,106.81; generated 253 sc[biz_a].scveh[car_2] $2,788.11/$2,788.14; generated 254 sc[biz_a].scveh[car_1] $5,592.24/$5,592.11; generated 261 sc[biz_a].scveh[car_1] $5,774.77/$5,774.59; generated 261 sc[biz_a].scveh[car_2] $1,453.60/$1,453.58; generated 355 sc[biz_a].scveh[car_1] $5,484.46/$5,484.37; generated 403 sc[biz_a].scveh[car_1] $907.12/$907.16; generated 403 sc[biz_a].scveh[car_2] $4,199.84/$4,200.03; generated 482 sc[biz_a].scveh[car_2] $1,566.01/$1,566.00; generated 482 sc[biz_b].scveh[car_1] $8,299.85/$8,299.56; and 48 partial records built on those bases with the same pairs.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen |
| scveh.macrs | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_post_recovery, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_post_recovery, scveh.screen |
| scveh.s179_2025 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| scveh.mq_q4 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| scveh.mq_total | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| scveh.cost179 | scveh.employee_use | scveh.employee_use |
| 9 (scveh.line9) | scveh.employee_use, scveh.h_lease_bad, scveh.h_smr_bad | scveh.employee_use, scveh.h_lease_bad, scveh.h_smr_bad |
| 20a | scveh.employee_use, scveh.h_lease_bad | scveh.employee_use, scveh.h_lease_bad |
| 13 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_post_recovery, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_post_recovery, scveh.screen |
| 7 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 9 (scveh.line9w) | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 10 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 11 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 14 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 15 | scveh.employee_use, scveh.screen | scveh.employee_use, scveh.screen |
| 16 | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen |
| 25 | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen |
| 17 | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen |
| 18 | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.screen |
| 19 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_post_recovery, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_post_recovery, scveh.screen |
| 20 | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_post_recovery, scveh.screen | scveh.employee_use, scveh.h_bonus_mixed, scveh.h_post_recovery, scveh.screen |

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
          then: scveh.h_smr_total
        - guard: {op: test, ne: [scveh.method, {const: "standard"}]}
          then: scveh.h_actual_total
    note: "The text lists parking fees and tolls only under the standard mileage rate. Under actual expenses, line 9 includes 'the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.' The parking input covers business use only and is excluded from the operating input, so this transcription also adds it in full under actual expenses."

  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment (business portion of rental cost of this vehicle)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.owned, {const: false}]}]}
          then: scveh.h_lease_bus
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.owned, {const: false}]}]}}
          then: scveh.h_zero
    refuses: [scveh.h_lease_bad]
    note: "For a lease of 30 days or more, the deduction may have to be reduced by the inclusion amount (Pub. 463). The text supplied here gives no way to figure that amount, so it is not computed. Under the standard mileage rate, no lease payments are deducted."

  - id: scveh.bus_cost
    printed: "13"
    label: "Depreciation and section 179 expense deduction — this vehicle's depreciation (special allowance plus MACRS)"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.bonus, scveh.macrs]}
    note: "This vehicle's section 179 amount (Form 4562 line 26 column (i)) reaches Schedule C line 13 through Form 4562 line 12, after the business income limit. It is therefore reported through scveh.s179_2025 and not added here. This line holds the vehicle's line 25 and line 26(h) amounts."

  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "none"}]}]}
          then: scveh.h_lim_nobonus
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "none"}]}]}}
          then: scveh.h_lim_bonus
    refuses: [scveh.screen, scveh.employee_use]

  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
    note: "Line 8 is the business/investment-use percentage: business miles divided by total miles (i4562 column (c)). The text does not state its precision. This transcription rounds the ratio to 4 decimal places (a percentage to two decimals)."

  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_dep2025, {const: true}]}, {op: test, eq: [scveh.passenger, {const: true}]}]}
          then: scveh.h_s179_pass
        - guard: {op: test, all: [{op: test, eq: [scveh.h_dep2025, {const: true}]}, {op: test, eq: [scveh.passenger, {const: false}]}, {op: test, eq: [scveh.suv, {const: true}]}]}
          then: scveh.h_s179_suv
        - guard: {op: test, all: [{op: test, eq: [scveh.h_dep2025, {const: true}]}, {op: test, eq: [scveh.passenger, {const: false}]}, {op: test, eq: [scveh.suv, {const: false}]}]}
          then: scveh.h_s179_cost
        - guard: {op: test, eq: [scveh.h_dep2025, {const: false}]}
          then: scveh.h_zero
    refuses: [scveh.screen, scveh.employee_use]
    note: "Vehicles that are not passenger automobiles are not subject to the line 9 limit. For them, this line holds the elected column (i) cost, capped at the business cost. For an SUV it is also capped at the $31,300 limit."

  - id: scveh.line11
    printed: "11"
    label: "Subtract line 10 from line 9. This is the limit on the amount you can deduct for depreciation (including any special depreciation allowance)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line9w, take: scveh.line10}

  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_is2025, {const: true}]}
          then: scveh.line10
        - guard: {op: test, eq: [scveh.h_is2025, {const: false}]}
          then: scveh.prior_179

  - id: scveh.line15
    printed: "15"
    label: "Subtract line 14 from line 13. This is your tentative basis for depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.h_bizcost, take: scveh.line14}

  - id: scveh.line16
    printed: "16"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. Enter -0- if this is not the year you placed the car in service, the car is not qualified property, or you elected not to claim a special depreciation allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_dep2025, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "full"}]}, {op: test, eq: [scveh.after_jan19, {const: true}]}]}
          then: scveh.line15
        - guard: {op: test, all: [{op: test, eq: [scveh.h_dep2025, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "full"}]}, {op: test, eq: [scveh.after_jan19, {const: false}]}]}
          then: scveh.h_b40
        - guard: {op: test, all: [{op: test, eq: [scveh.h_dep2025, {const: true}]}, {op: test, eq: [scveh.bonus_choice, {const: "forty"}]}]}
          then: scveh.h_b40
        - guard: {op: test, any: [{op: test, eq: [scveh.h_dep2025, {const: false}]}, {op: test, eq: [scveh.bonus_choice, {const: "none"}]}]}
          then: scveh.h_zero
    refuses: [scveh.screen, scveh.h_bonus_mixed]
    note: "Property acquired after January 19, 2025 gets 100% unless the 40% election is made. Property acquired before January 20, 2025 (and after September 27, 2017, per the screen) is limited to 40%."

  - id: scveh.bonus_allowed
    printed: "25"
    label: "Special depreciation allowance for qualified listed property (this vehicle)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.passenger, {const: true}]}
          then: scveh.h_bonus_lim
        - guard: {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.line16
    note: "Pub. 946 worksheet: if line 16 equals line 11, stop, because depreciation including the special allowance is limited to line 11. This transcription reads that as the smaller of line 16 or line 11 for passenger automobiles."

  - id: scveh.line17
    printed: "17"
    label: "Subtract line 16 from line 11. This is the limit on the amount you can deduct for MACRS depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line11, take: scveh.line16}

  - id: scveh.line18
    printed: "18"
    label: "Subtract line 16 from line 15. This is your basis for depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line15, take: scveh.line16}

  - id: scveh.line19
    printed: "19"
    label: "Multiply line 18 by line 6. This is your tentative MACRS depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [mq.applies, {const: false}]}]}
          then: scveh.h_dep_hy
        - guard: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [mq.applies, {const: true}]}]}
          then: scveh.h_dep_mq
        - guard: {op: test, eq: [scveh.h_is2025, {const: false}]}
          then: scveh.h_dep_prior
    refuses: [scveh.screen, scveh.h_post_recovery]
    note: "Deductions after the recovery period (unrecovered basis) need every prior year's allowable depreciation, which the closed input interface does not provide. Those years are refused."

  - id: scveh.line20
    printed: "20"
    label: "Enter the lesser of line 17 or line 19. This is your MACRS depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.passenger, {const: true}]}
          then: scveh.h_l20_pass
        - guard: {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.line19

  # ---- result interfaces ----
  - id: scveh.bonus
    printed: "(helper)"
    label: "This vehicle's special depreciation allowance (Form 4562 line 25)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_dep, {const: true}]}
          then: scveh.bonus_allowed
        - guard: {op: test, eq: [scveh.h_dep, {const: false}]}
          then: scveh.h_zero

  - id: scveh.macrs
    printed: "(helper)"
    label: "This vehicle's MACRS depreciation deduction (Form 4562 line 26 column (h))"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_dep, {const: true}]}
          then: scveh.line20
        - guard: {op: test, eq: [scveh.h_dep, {const: false}]}
          then: scveh.h_zero

  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Elected section 179 cost of this vehicle (Form 4562 line 26 column (i))"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line10}

  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost of this vehicle as section 179 property placed in service in 2025 (included on Form 4562 line 2)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_dep2025, {const: true}]}
          then: scveh.h_bizcost
        - guard: {op: test, eq: [scveh.h_dep2025, {const: false}]}
          then: scveh.h_zero
    note: "Line 2 includes listed property. The text gives no rule for a vehicle on the standard mileage rate. This transcription counts only an owned vehicle placed in service in 2025 and depreciated under actual expenses, at its business-use cost."

  - id: scveh.mq_total
    printed: "(helper)"
    label: "Depreciable basis (after section 179, business part only, before special allowance) of this vehicle placed in service in 2025, for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_dep2025, {const: true}]}
          then: scveh.h_mqbase
        - guard: {op: test, eq: [scveh.h_dep2025, {const: false}]}
          then: scveh.h_zero

  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Depreciable basis of this vehicle if placed in service in the last 3 months of 2025, for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [scveh.h_dep2025, {const: true}]}, {op: test, eq: [scveh.quarter, {const: "q4"}]}]}
          then: scveh.h_mqbase
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [scveh.h_dep2025, {const: true}]}, {op: test, eq: [scveh.quarter, {const: "q4"}]}]}}
          then: scveh.h_zero

  # ---- helpers ----
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: scveh.h_cent
    printed: "(helper)"
    label: "One cent per mile (mile counter)"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}

  - id: scveh.h_bm_c
    printed: "(helper)"
    label: "Business miles (44a), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}

  - id: scveh.h_cm_c
    printed: "(helper)"
    label: "Commuting miles (44b), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}

  - id: scveh.h_om_c
    printed: "(helper)"
    label: "Other miles (44c), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}

  - id: scveh.h_total_c
    printed: "(helper)"
    label: "Total miles driven for all purposes, as cents"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_bm_c, scveh.h_cm_c, scveh.h_om_c]}

  - id: scveh.h_smr_rate
    printed: "(helper)"
    label: "Business standard mileage rate, 70 cents per mile"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}

  - id: scveh.h_smr_miles
    printed: "(helper)"
    label: "Multiply the number of business miles driven by 0.70"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_smr_rate, count: scveh.miles_business}

  - id: scveh.h_smr_bad
    printed: "(helper)"
    label: "Standard mileage rate not allowed for this vehicle"
    type: Bool
    expr: {op: test, eq: [scveh.smr_ok, {const: false}]}

  - id: scveh.h_smr_total
    printed: "(helper)"
    label: "Add to this amount your parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_smr_miles, scveh.parking]}
    refuses: [scveh.h_smr_bad]

  - id: scveh.h_lease_bad
    printed: "(helper)"
    label: "Actual expenses claimed for a leased vehicle for which the standard mileage rate was used before"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.owned, {const: false}]}, {op: test, eq: [scveh.lease_smr_before, {const: true}]}]}

  - id: scveh.h_op_bus
    printed: "(helper)"
    label: "Business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
    refuses: [scveh.employee_use]

  - id: scveh.h_actual_total
    printed: "(helper)"
    label: "Actual car and truck expenses (business portion of operating expenses plus business parking and tolls)"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_op_bus, scveh.parking]}
    refuses: [scveh.h_lease_bad]

  - id: scveh.h_lease_bus
    printed: "(helper)"
    label: "Business portion of lease payments for this vehicle"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
    refuses: [scveh.employee_use, scveh.h_lease_bad]

  - id: scveh.h_dep
    printed: "(helper)"
    label: "Owned vehicle depreciated under actual expenses"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.method, {const: "actual"}]}, {op: test, eq: [scveh.owned, {const: true}]}]}

  - id: scveh.h_is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2025"}]}

  - id: scveh.h_dep2025
    printed: "(helper)"
    label: "Owned, actual expenses, placed in service in 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_dep, {const: true}]}, {op: test, eq: [scveh.h_is2025, {const: true}]}]}

  - id: scveh.h_bizcost
    printed: "(helper)"
    label: "Line 13: Multiply line 12 by line 8. This is your business/investment cost"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.h_bm_c, whole: scveh.h_total_c, places: 4}
    refuses: [scveh.employee_use]

  - id: scveh.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [scveh.placed]}

  - id: scveh.h_lim_bonus
    printed: "(helper)"
    label: "Maximum depreciation deduction for passenger automobiles for the date placed in service and year"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_year]}

  - id: scveh.h_lim_nobonus
    printed: "(helper)"
    label: "First-year maximum deduction if you elected not to claim any special depreciation allowance"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit_first_nobonus, keys: [scveh.placed]}

  - id: scveh.h_s179_cost
    printed: "(helper)"
    label: "Elected section 179 cost, not more than the business cost"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.h_bizcost]}

  - id: scveh.h_suv_limit
    printed: "(helper)"
    label: "Section 179 limit for SUVs and certain other vehicles ($31,300)"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}

  - id: scveh.h_s179_suv
    printed: "(helper)"
    label: "Elected section 179 cost of an SUV, not more than $31,300"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_s179_cost, scveh.h_suv_limit]}

  - id: scveh.h_s179_pass
    printed: "(helper)"
    label: "Section 179 deduction for a passenger automobile (not more than line 9)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_s179_cost, scveh.line9w]}

  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "Special allowance choice differs within the 5-year class"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: true}]}, {op: test, eq: [scveh.bonus_same, {const: false}]}]}

  - id: scveh.h_b40
    printed: "(helper)"
    label: "Line 15 multiplied by 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}

  - id: scveh.h_bonus_lim
    printed: "(helper)"
    label: "Smaller of line 16 or line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line16, scveh.line11]}

  - id: scveh.h_mqbase
    printed: "(helper)"
    label: "Business cost reduced by section 179 (depreciable basis before special allowance)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.h_bizcost, take: scveh.line10}

  - id: scveh.h_period
    printed: "(helper)"
    label: "Recovery period: automobiles and light general purpose trucks are 5-year property"
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

  - id: scveh.h_rate_hy
    printed: "(helper)"
    label: "Line 6 depreciation rate, half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_hy, scveh.h_year]}

  - id: scveh.h_rate_mq
    printed: "(helper)"
    label: "Line 6 depreciation rate, mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_qconv, scveh.h_year]}

  - id: scveh.h_rate_prior
    printed: "(helper)"
    label: "Line 6 depreciation rate, convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_year]}

  - id: scveh.h_dep_hy
    printed: "(helper)"
    label: "Line 18 multiplied by the half-year rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_hy}

  - id: scveh.h_dep_mq
    printed: "(helper)"
    label: "Line 18 multiplied by the mid-quarter rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_mq}

  - id: scveh.h_dep_prior
    printed: "(helper)"
    label: "Line 18 multiplied by the rate for the convention used when placed in service"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_prior}

  - id: scveh.h_last
    printed: "(helper)"
    label: "Last year of recovery for 5-year property"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [scveh.h_period]}

  - id: scveh.h_post_recovery
    printed: "(helper)"
    label: "2025 falls after the vehicle's recovery period (unrecovered basis rules)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [scveh.h_is2025, {const: false}]}, {op: test, gt: [scveh.h_year, scveh.h_last]}]}

  - id: scveh.h_l20_pass
    printed: "(helper)"
    label: "Lesser of line 17 or line 19"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}
```
```
