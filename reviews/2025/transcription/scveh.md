# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5254fc31a17eb3c41ce003fdee716fa102b2cbe662ce1a1e7a70b98cd36bd08e |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | f1af0533c5c8927cf21ba8b2dd2e7d060f1e6b01f1817d198ef9494ca9fa4ab5 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 21ed42ae791e3370832f9db89dc59af7b9c11eac73013dc57226b7d810990087 |
| printed lines compared | 21 |
| agree / disagree / missing | 7 / 14 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 60, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### scveh.bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "25"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "25"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 2892 of 3173 comparisons agree; on completed returns {"value": 6}.

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "19"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"line": "20"}}, {"guard": {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"amount": {"from": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}, {"from": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}], "op": "smaller_of"}], "op": "sum"}}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 2220 of 3173 comparisons agree; on completed returns {"value": 167}.

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

Ruling: representation; All differences are on refused or partial records; no completed return differs. Triage executable-triage-v2 (triage/scveh.json): 2938 of 3173 comparisons agree; on completed returns no difference.

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 2923 of 3173 comparisons agree; on completed returns {"value": 1}.

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 2164 of 3173 comparisons agree; on completed returns {"value": 162}.

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

Second transcription's note: With the standard mileage rate, lease payments are not deducted. The inclusion amount for a vehicle leased 30 days or more is not figured (no inputs are provided for it).

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 2962 of 3173 comparisons agree; on completed returns {"value": 5}.

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 561 of 3173 comparisons agree; on completed returns {"project-refuses": 72, "project-unknown": 38, "value": 368}.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The limits apply only to passenger automobiles. For other vehicles the worksheet limit lines are not used, and zero is shown here.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 721 of 3173 comparisons agree; on completed returns {"candidate-unknown": 1, "project-refuses": 75, "project-unknown": 23, "value": 246}.

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 265 of 3173 comparisons agree; on completed returns {"candidate-unknown": 1, "project-refuses": 75, "project-unknown": 7, "value": 446}.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}, "then": {"of": [{"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: An election above the limits (line 9 for passenger automobiles, $31,300 for SUVs, business cost) is capped rather than refused. This is the elected amount; the business income limit (Form 4562 line 11) applies at return level.

Ruling: representation; The project-side refusal or unknown records are entries where the line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 2391 of 3173 comparisons agree; on completed returns {"project-refuses": 75, "project-unknown": 23}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "10"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "scveh.prior_179"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 2300 of 3173 comparisons agree; on completed returns {"project-refuses": 75, "project-unknown": 29, "value": 16}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 2274 of 3173 comparisons agree; on completed returns {"project-refuses": 75, "project-unknown": 23, "value": 6}.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "16"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The worksheet's note says only 'if line 16 is equal to line 11, stop'. Because the allowance is included in the overall limit for passenger automobiles, a line 16 above line 11 was read as limited to line 11.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 2271 of 3173 comparisons agree; on completed returns {"project-refuses": 75, "project-unknown": 23, "value": 7}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Project-side refusal or unknown records are standard-mileage vehicles, where the line is not read. Triage executable-triage-v2 (triage/scveh.json): 938 of 3173 comparisons agree; on completed returns {"project-refuses": 75, "project-unknown": 43, "value": 221}.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

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
| 9 (scveh.line9) | scveh.h_lease_bad, scveh.h_smr_bad | scveh.h_lease_bad, scveh.h_smr_bad |
| 20a | scveh.h_lease_bad | scveh.h_lease_bad |
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
```yaml
lines:
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: scveh.h_cent
    printed: "(helper)"
    label: "One cent (unit for expressing miles as an amount)"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: scveh.h_rate
    printed: "(helper)"
    label: "Standard mileage rate for 2025 (70 cents per mile)"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}
  - id: scveh.h_mb
    printed: "(helper)"
    label: "Business miles (line 44a), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}
  - id: scveh.h_mc
    printed: "(helper)"
    label: "Commuting miles (line 44b), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}
  - id: scveh.h_mo
    printed: "(helper)"
    label: "Other miles (line 44c), as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}
  - id: scveh.h_mt
    printed: "(helper)"
    label: "Total number of miles the vehicle is driven for all purposes, as cents"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_mb, scveh.h_mc, scveh.h_mo]}
  - id: scveh.h_std
    printed: "(helper)"
    label: "You take the standard mileage rate"
    type: Bool
    expr: {op: test, eq: [scveh.method, {const: "standard"}]}
  - id: scveh.h_actual
    printed: "(helper)"
    label: "You deduct actual expenses"
    type: Bool
    expr: {op: test, eq: [scveh.method, {const: "actual"}]}
  - id: scveh.h_smr_bad
    printed: "(helper)"
    label: "Standard mileage rate chosen but not allowed (not used in the first year for an owned vehicle, not for the entire lease period, or five or more vehicles used simultaneously)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_std, {const: true}]}
        - {op: test, eq: [scveh.smr_ok, {const: false}]}
  - id: scveh.h_lease_bad
    printed: "(helper)"
    label: "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_actual, {const: true}]}
        - {op: test, eq: [scveh.owned, {const: false}]}
        - {op: test, eq: [scveh.lease_smr_before, {const: true}]}
  - id: scveh.h_smr_amt
    printed: "(helper)"
    label: "Multiply the number of business miles driven by 0.70"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_rate, count: scveh.miles_business}
  - id: scveh.h_std9
    printed: "(helper)"
    label: "Add to this amount your parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_smr_amt, scveh.parking]}
  - id: scveh.h_op_bus
    printed: "(helper)"
    label: "Business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.h_mb, whole: scveh.h_mt, places: 4}
    note: "The business portion is taken as business miles divided by total miles (i4562 column (c) rule for vehicles). The text sets no rounding for the percentage; 4 decimal places (a percentage to two decimals) was chosen, and the same is used on every business-use line."
  - id: scveh.h_act9
    printed: "(helper)"
    label: "Actual expenses: business portion of operating expenses plus business parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_op_bus, scveh.parking]}
    note: "The actual-expense instruction lists gasoline, oil, repairs, insurance, license plates 'etc.' and does not mention parking and tolls. The parking input is limited to business use and is excluded from operating expenses, so it was read as deductible under either method."
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses (see instructions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_std, {const: true}]}, then: scveh.h_std9}
        - {guard: {op: test, eq: [scveh.h_std, {const: false}]}, then: scveh.h_act9}
    refuses: [scveh.h_smr_bad, scveh.h_lease_bad]
  - id: scveh.h_leased_actual
    printed: "(helper)"
    label: "Leased vehicle with actual expenses"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_actual, {const: true}]}
        - {op: test, eq: [scveh.owned, {const: false}]}
  - id: scveh.h_lease_bus
    printed: "(helper)"
    label: "Business portion of the lease payments"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.h_mb, whole: scveh.h_mt, places: 4}
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment (this vehicle's business portion of rental cost)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_leased_actual, {const: true}]}, then: scveh.h_lease_bus}
        - {guard: {op: test, eq: [scveh.h_leased_actual, {const: false}]}, then: scveh.h_zero}
    refuses: [scveh.h_lease_bad]
    note: "With the standard mileage rate, lease payments are not deducted. The inclusion amount for a vehicle leased 30 days or more is not figured (no inputs are provided for it)."
  - id: scveh.h_dep
    printed: "(helper)"
    label: "You own the vehicle and deduct actual expenses (depreciation is claimed)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: true}]}
  - id: scveh.h_is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2025"}]}
  - id: scveh.h_period
    printed: "(helper)"
    label: "Recovery period: 5-year property (automobiles, light general purpose trucks)"
    type: Enum(macrs_period)
    expr: {op: param, ref: sc.period_y5}
  - id: scveh.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: scveh.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [scveh.placed]}
  - id: scveh.h_last
    printed: "(helper)"
    label: "Last year of recovery for 5-year property"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [scveh.h_period]}
  - id: scveh.h_post
    printed: "(helper)"
    label: "The recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [scveh.h_year, scveh.h_last]}
  - id: scveh.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [scveh.quarter]}
  - id: scveh.h_bus_cost_dep
    printed: "(helper)"
    label: "Multiply line 12 (cost or other basis) by line 8 (business/investment-use percentage)"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.h_mb, whole: scveh.h_mt, places: 4}
    refuses: [scveh.screen]
  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_bus_cost_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
  - id: scveh.h_lim_table
    printed: "(helper)"
    label: "Maximum depreciation deduction for this year from the passenger automobile table"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_year]}
    note: "For a 2019 vehicle in 2025 (7th year) the '4th & later' amount is read from the table by year 7; the table is assumed to carry that year."
  - id: scveh.h_lim_nobonus
    printed: "(helper)"
    label: "First-year maximum when no special depreciation allowance is claimed"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit_first_nobonus, keys: [scveh.placed]}
  - id: scveh.h_line7_2025
    printed: "(helper)"
    label: "2025 first-year limit: $20,200 with the special depreciation allowance, $12,200 without"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.bonus_choice, {const: "none"}]}, then: scveh.h_lim_nobonus}
        - {guard: {op: test, ne: [scveh.bonus_choice, {const: "none"}]}, then: scveh.h_lim_table}
  - id: scveh.h_line7_dep
    printed: "(helper)"
    label: "Maximum depreciation deduction for this year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_line7_2025}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_lim_table}
  - id: scveh.h_line7_pass
    printed: "(helper)"
    label: "Maximum depreciation deduction (passenger automobiles only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: true}]}, then: scveh.h_line7_dep}
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.h_zero}
    refuses: [scveh.screen]
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_line7_pass}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
    note: "The limits apply only to passenger automobiles. For other vehicles the worksheet limit lines are not used, and zero is shown here."
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.h_mb, whole: scveh.h_mt, places: 4}
  - id: scveh.h_elect_cap
    printed: "(helper)"
    label: "Elected section 179 cost, not more than the business cost"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.bus_cost]}
  - id: scveh.h_l10_pass
    printed: "(helper)"
    label: "Section 179 deduction claimed this year (not more than line 9)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_elect_cap, scveh.line9w]}
  - id: scveh.h_suv_limit
    printed: "(helper)"
    label: "You cannot elect to expense more than $31,300 of the cost of any SUV"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_l10_suv
    printed: "(helper)"
    label: "Elected section 179 cost of an SUV, not more than $31,300"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_elect_cap, scveh.h_suv_limit]}
  - id: scveh.h_l10_nonpass
    printed: "(helper)"
    label: "Elected section 179 cost of a vehicle not subject to the passenger automobile limits"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.suv, {const: true}]}, then: scveh.h_l10_suv}
        - {guard: {op: test, eq: [scveh.suv, {const: false}]}, then: scveh.h_elect_cap}
  - id: scveh.h_l10_2025
    printed: "(helper)"
    label: "Section 179 deduction for a vehicle placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: true}]}, then: scveh.h_l10_pass}
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.h_l10_nonpass}
  - id: scveh.h_l10_dep
    printed: "(helper)"
    label: "Enter -0- if this is not the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_l10_2025}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_l10_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
    note: "An election above the limits (line 9 for passenger automobiles, $31,300 for SUVs, business cost) is capped rather than refused. This is the elected amount; the business income limit (Form 4562 line 11) applies at return level."
  - id: scveh.line11
    printed: "11"
    label: "Subtract line 10 from line 9. This is the limit on the amount you can deduct for depreciation (including any special depreciation allowance)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.line9w, take: scveh.line10}
  - id: scveh.h_l14_dep
    printed: "(helper)"
    label: "Section 179 deduction claimed in the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.line10}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.prior_179}
  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_l14_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
  - id: scveh.line15
    printed: "15"
    label: "Subtract line 14 from line 13. This is your tentative basis for depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.bus_cost, take: scveh.line14}
  - id: scveh.h_b40
    printed: "(helper)"
    label: "40% special depreciation allowance"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}
  - id: scveh.h_b_full
    printed: "(helper)"
    label: "Special allowance claimed: 100% if acquired after January 19, 2025, otherwise 40%"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.after_jan19, {const: true}]}, then: scveh.line15}
        - {guard: {op: test, eq: [scveh.after_jan19, {const: false}]}, then: scveh.h_b40}
  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "The special allowance choice is not the same for all 5-year property placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [scveh.bonus_same, {const: false}]}
  - id: scveh.h_l16_2025
    printed: "(helper)"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.bonus_choice, {const: "full"}]}, then: scveh.h_b_full}
        - {guard: {op: test, eq: [scveh.bonus_choice, {const: "forty"}]}, then: scveh.h_b40}
        - {guard: {op: test, eq: [scveh.bonus_choice, {const: "none"}]}, then: scveh.h_zero}
    refuses: [scveh.h_bonus_mixed]
  - id: scveh.h_l16_dep
    printed: "(helper)"
    label: "Enter -0- if this is not the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_l16_2025}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.line16
    printed: "16"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. This is your special depreciation allowance. Enter -0- if this is not the year you placed the car in service, the car is not qualified property, or you elected not to claim a special depreciation allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_l16_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
  - id: scveh.h_ba_pass
    printed: "(helper)"
    label: "Special allowance limited to line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line16, scveh.line11]}
  - id: scveh.h_ba_dep
    printed: "(helper)"
    label: "Special depreciation allowance for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: true}]}, then: scveh.h_ba_pass}
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.line16}
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year and used more than 50% in a qualified business use (this vehicle)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_ba_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
    note: "The worksheet's note says only 'if line 16 is equal to line 11, stop'. Because the allowance is included in the overall limit for passenger automobiles, a line 16 above line 11 was read as limited to line 11."
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
  - id: scveh.h_rate_hy
    printed: "(helper)"
    label: "Depreciation rate (from tables), half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_hy, scveh.h_year]}
  - id: scveh.h_rate_mq
    printed: "(helper)"
    label: "Depreciation rate (from tables), mid-quarter convention for the quarter placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_qconv, scveh.h_year]}
  - id: scveh.h_rate_prior
    printed: "(helper)"
    label: "Depreciation rate (from tables), convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_year]}
  - id: scveh.h_m_hy
    printed: "(helper)"
    label: "Multiply line 18 by line 6 (half-year convention)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_hy}
  - id: scveh.h_m_mq
    printed: "(helper)"
    label: "Multiply line 18 by line 6 (mid-quarter convention)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_mq}
  - id: scveh.h_m_prior
    printed: "(helper)"
    label: "Multiply line 18 by line 6 (convention of the year placed in service)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_prior}
  - id: scveh.h_m_2025
    printed: "(helper)"
    label: "Tentative MACRS depreciation for a vehicle placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [mq.applies, {const: true}]}, then: scveh.h_m_mq}
        - {guard: {op: test, eq: [mq.applies, {const: false}]}, then: scveh.h_m_hy}
  - id: scveh.h_m_inrec
    printed: "(helper)"
    label: "Tentative MACRS depreciation within the recovery period"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_m_2025}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_m_prior}
  - id: scveh.h_l19_dep
    printed: "(helper)"
    label: "Tentative MACRS depreciation (none from the tables after the recovery period)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_post, {const: true}]}, then: scveh.h_zero}
        - {guard: {op: test, eq: [scveh.h_post, {const: false}]}, then: scveh.h_m_inrec}
  - id: scveh.line19
    printed: "19"
    label: "Multiply line 18 by line 6. This is your tentative MACRS depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_l19_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
  - id: scveh.line20
    printed: "20"
    label: "Enter the lesser of line 17 or line 19. This is your MACRS depreciation deduction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}
  - id: scveh.h_base
    printed: "(helper)"
    label: "Cost or other basis less the section 179 deduction (basis as if used 100% for business)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.prior_179}
  - {id: scveh.h_y1, printed: "(helper)", label: "Recovery year 1", type: Count, expr: {op: param, ref: sc.year1}}
  - {id: scveh.h_y2, printed: "(helper)", label: "Recovery year 2", type: Count, expr: {op: param, ref: sc.year2}}
  - {id: scveh.h_y3, printed: "(helper)", label: "Recovery year 3", type: Count, expr: {op: param, ref: sc.year3}}
  - {id: scveh.h_y4, printed: "(helper)", label: "Recovery year 4", type: Count, expr: {op: param, ref: sc.year4}}
  - {id: scveh.h_y5, printed: "(helper)", label: "Recovery year 5", type: Count, expr: {op: param, ref: sc.year5}}
  - {id: scveh.h_y6, printed: "(helper)", label: "Recovery year 6", type: Count, expr: {op: param, ref: sc.year6}}
  - {id: scveh.h_r1, printed: "(helper)", label: "Rate, recovery year 1", type: Rate, expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y1]}}
  - {id: scveh.h_r2, printed: "(helper)", label: "Rate, recovery year 2", type: Rate, expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y2]}}
  - {id: scveh.h_r3, printed: "(helper)", label: "Rate, recovery year 3", type: Rate, expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y3]}}
  - {id: scveh.h_r4, printed: "(helper)", label: "Rate, recovery year 4", type: Rate, expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y4]}}
  - {id: scveh.h_r5, printed: "(helper)", label: "Rate, recovery year 5", type: Rate, expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y5]}}
  - {id: scveh.h_r6, printed: "(helper)", label: "Rate, recovery year 6", type: Rate, expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y6]}}
  - {id: scveh.h_t1, printed: "(helper)", label: "Depreciation at 100% use, year 1", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_base, rate: scveh.h_r1}}
  - {id: scveh.h_t2, printed: "(helper)", label: "Depreciation at 100% use, year 2", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_base, rate: scveh.h_r2}}
  - {id: scveh.h_t3, printed: "(helper)", label: "Depreciation at 100% use, year 3", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_base, rate: scveh.h_r3}}
  - {id: scveh.h_t4, printed: "(helper)", label: "Depreciation at 100% use, year 4", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_base, rate: scveh.h_r4}}
  - {id: scveh.h_t5, printed: "(helper)", label: "Depreciation at 100% use, year 5", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_base, rate: scveh.h_r5}}
  - {id: scveh.h_t6, printed: "(helper)", label: "Depreciation at 100% use, year 6", type: NonNegDollars, expr: {op: multiply_rate, amount: scveh.h_base, rate: scveh.h_r6}}
  - {id: scveh.h_l1a, printed: "(helper)", label: "First-year limit less the section 179 deduction", type: NonNegDollars, expr: {op: subtract_floor0, from: scveh.h_lim_nobonus, take: scveh.prior_179}}
  - {id: scveh.h_lm2, printed: "(helper)", label: "Limit, year 2", type: NonNegDollars, expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y2]}}
  - {id: scveh.h_lm3, printed: "(helper)", label: "Limit, year 3", type: NonNegDollars, expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y3]}}
  - {id: scveh.h_lm4, printed: "(helper)", label: "Limit, year 4", type: NonNegDollars, expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y4]}}
  - {id: scveh.h_lm5, printed: "(helper)", label: "Limit, year 5", type: NonNegDollars, expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y5]}}
  - {id: scveh.h_lm6, printed: "(helper)", label: "Limit, year 6", type: NonNegDollars, expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y6]}}
  - {id: scveh.h_a1, printed: "(helper)", label: "Allowable depreciation at 100% use, year 1", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t1, scveh.h_l1a]}}
  - {id: scveh.h_a2, printed: "(helper)", label: "Allowable depreciation at 100% use, year 2", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t2, scveh.h_lm2]}}
  - {id: scveh.h_a3, printed: "(helper)", label: "Allowable depreciation at 100% use, year 3", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t3, scveh.h_lm3]}}
  - {id: scveh.h_a4, printed: "(helper)", label: "Allowable depreciation at 100% use, year 4", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t4, scveh.h_lm4]}}
  - {id: scveh.h_a5, printed: "(helper)", label: "Allowable depreciation at 100% use, year 5", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t5, scveh.h_lm5]}}
  - {id: scveh.h_a6, printed: "(helper)", label: "Allowable depreciation at 100% use, year 6", type: NonNegDollars, expr: {op: smaller_of, of: [scveh.h_t6, scveh.h_lm6]}}
  - id: scveh.h_prior_dep
    printed: "(helper)"
    label: "Depreciation that would have been allowable at 100% business use during the recovery period"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_a1, scveh.h_a2, scveh.h_a3, scveh.h_a4, scveh.h_a5, scveh.h_a6]}
  - id: scveh.h_unrec
    printed: "(helper)"
    label: "Unrecovered basis: cost or other basis reduced by depreciation and section 179 deductions that would have been allowable at 100% use with the limits applied"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.h_base, take: scveh.h_prior_dep}
    note: "This covers only a 2019 vehicle in its 7th year (the only case in scope after the recovery period); no prior special allowance, because it is screened."
  - id: scveh.h_unrec_bus
    printed: "(helper)"
    label: "Unrecovered basis times the business/investment-use percentage"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.h_unrec, part: scveh.h_mb, whole: scveh.h_mt, places: 4}
  - id: scveh.h_post_ded
    printed: "(helper)"
    label: "Deduction after the recovery period: lesser of the reduced maximum deduction or the remaining unrecovered basis"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line9w, scveh.h_unrec_bus]}
    note: "The texts do not say how business use under 100% applies to the unrecovered basis. Both the limit and the unrecovered basis were multiplied by the business-use percentage."
  - id: scveh.h_macrs_pass
    printed: "(helper)"
    label: "MACRS depreciation of a passenger automobile"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_post, {const: true}]}, then: scveh.h_post_ded}
        - {guard: {op: test, eq: [scveh.h_post, {const: false}]}, then: scveh.line20}
  - id: scveh.h_macrs_dep
    printed: "(helper)"
    label: "MACRS depreciation of this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.passenger, {const: true}]}, then: scveh.h_macrs_pass}
        - {guard: {op: test, eq: [scveh.passenger, {const: false}]}, then: scveh.line19}
  - id: scveh.macrs
    printed: "(helper)"
    label: "Form 4562 line 26, column (h): depreciation deduction for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_macrs_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
  - id: scveh.bonus
    printed: "(helper)"
    label: "Form 4562 line 25: special depreciation allowance for this vehicle"
    type: NonNegDollars
    expr: {op: copy, from: scveh.bonus_allowed}
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Form 4562 line 26, column (i): elected section 179 cost for this vehicle (to line 7)"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line10}
  - id: scveh.h_mqt_dep
    printed: "(helper)"
    label: "Depreciable basis (after section 179, before special allowance) of a vehicle placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.line15}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Depreciable basis of this vehicle placed in service during the tax year (mid-quarter test)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_mqt_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
    note: "Per Pub. 946, the basis reflects the section 179 reduction and excludes personal use, but not the special allowance (line 15 of the worksheet)."
  - id: scveh.h_q4
    printed: "(helper)"
    label: "Placed in service during the last 3 months of the tax year"
    type: Bool
    expr: {op: test, eq: [scveh.quarter, {const: "q4"}]}
  - id: scveh.h_mq4_2025
    printed: "(helper)"
    label: "Depreciable basis if placed in service in the fourth quarter"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_q4, {const: true}]}, then: scveh.line15}
        - {guard: {op: test, eq: [scveh.h_q4, {const: false}]}, then: scveh.h_zero}
  - id: scveh.h_mq4_dep
    printed: "(helper)"
    label: "Fourth-quarter depreciable basis of a 2025 vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_mq4_2025}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Depreciable basis of this vehicle placed in service during the last 3 months of the tax year (mid-quarter test)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_mq4_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
  - id: scveh.h_c179_dep
    printed: "(helper)"
    label: "Business cost of a vehicle placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.bus_cost}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost of this listed property (Part V) placed in service during the tax year, included in Form 4562 line 2 and Worksheet 1 line 1"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.h_c179_dep}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
    note: "Line 2 says to include 'any listed property from Part V' but does not say whether full or business cost. The business-use cost was chosen, consistent with line 6 column (b) 'Cost (business use only)'. Only owned vehicles placed in service in 2025 are counted."
```
```
