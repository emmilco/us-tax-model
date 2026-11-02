# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | de71694a147c7c3bc8ba666607b076bfb703eabaad271690f98b5bea0cc887ea |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 6deb4487b305cf04a895b4d5d1c409dea71aa25ee079693d1d895f2518ba16a5 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 103e55b3bcbc53d0e7997d1a372e081370d4d144fc6e7d0b6e75adb1b119f82e |
| printed lines compared | 21 |
| agree / disagree / missing | 8 / 13 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). The candidate also reads scveh.bonus_same or scveh.cost where the source does not need them. Triage executable-triage-v2 (triage/scveh.json): 2291 of 2373 comparisons agree; on completed returns {"candidate-unknown": 2, "value": 4}.

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). The candidate also reads scveh.bonus_same or scveh.cost where the source does not need them. Triage executable-triage-v2 (triage/scveh.json): 1872 of 2373 comparisons agree; on completed returns {"candidate-unknown": 2, "value": 148}.

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

Second transcription's note: The basis reflects personal use and section 179 but not the special allowance, as Pub. 946 states. Worksheet line 15 is exactly that amount.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 2108 of 2373 comparisons agree; on completed returns {"value": 1}.

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 2164 of 2373 comparisons agree; on completed returns {"value": 4}.

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

Second transcription's note: Worksheet 1 counts all eligible section 179 property, not only the elected amount. The text does not say whether line 2 uses full or business cost for a vehicle; chose business cost, following line 6 column (b).

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 2177 of 2373 comparisons agree; on completed returns {"value": 4}.

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

Second transcription's note: The rule barring actual expenses on a leased vehicle after earlier use of the standard mileage rate has no matching input for leased vehicles, so it is not tested here.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 1721 of 2373 comparisons agree; on completed returns {"value": 145}.

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 2223 of 2373 comparisons agree; on completed returns {"value": 5}.

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

Second transcription's note: The text does not say how to round the business/investment-use percentage (line 8). Chose 4 decimal places (a percentage to two decimals) wherever the percentage is applied. Line 12 is the cost input, since vehicle credits are screened out.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 1030 of 2373 comparisons agree; on completed returns {"project-unknown": 9, "value": 396}.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": 4, "type": "Count"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"const": 4, "type": "Count"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(d)"}}], "op": "choose"}
```

Second transcription's note: The limits do not apply to a vehicle that is not a passenger automobile, and the worksheet has no entry for that case. Chose the vehicle's cost here so that no limit binds later in the worksheet.

Ruling: representation; line 7 is a worksheet line for passenger automobiles, figured for every vehicle and read only on the scveh.passenger branches (p946 worksheet; i4562 p. 14). The candidate zeroes it for other vehicles and needs scveh.passenger on returns that never ask it. The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 1506 of 2373 comparisons agree; on completed returns {"candidate-unknown": 10, "project-refuses": 107, "project-unknown": 24, "value": 41}.

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. The candidate also reads scveh.bonus_same or scveh.cost where the source does not need them. Triage executable-triage-v2 (triage/scveh.json): 311 of 2373 comparisons agree; on completed returns {"candidate-unknown": 10, "project-refuses": 107, "value": 481}.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"of": [{"line": "9 (scveh.line9w)"}, {"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}], "op": "smaller_of"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"of": [{"line": "(i)"}, {"line": "13"}], "op": "smaller_of"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: An election above line 9, the business cost or the $31,300 limit is reduced to the limit and not refused. The Form 4562 line 11 business income limit is applied outside this per-vehicle slice, so this line does not reflect it.

Ruling: representation; the section 179 deduction on both sides. The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 1882 of 2373 comparisons agree; on completed returns {"project-refuses": 106, "project-unknown": 22}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: A vehicle acquired before January 20, 2025 is limited to 40% even when the answer is 'full'.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. The candidate also reads scveh.bonus_same or scveh.cost where the source does not need them. Triage executable-triage-v2 (triage/scveh.json): 1775 of 2373 comparisons agree; on completed returns {"candidate-unknown": 2, "project-refuses": 106, "project-unknown": 33, "value": 4}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}, {"from": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}], "op": "smaller_of"}], "op": "sum"}}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second transcription's note: After the recovery period the table rate has no entry. A passenger automobile uses its business share of unrecovered basis, following the Pub. 946 example; other listed property gets no deduction.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate to 4; i4562 p. 14, Column (c). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. The candidate also reads scveh.bonus_same or scveh.cost where the source does not need them. A 2019 vehicle is figured from unrecovered basis (scveh.post; p946 p. 61; BUG-0059). Triage executable-triage-v2 (triage/scveh.json): 1267 of 2373 comparisons agree; on completed returns {"candidate-unknown": 2, "project-refuses": 7, "value": 311}.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen |
| scveh.macrs | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen |
| scveh.s179_2025 | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| scveh.mq_q4 | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| scveh.mq_total | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| scveh.cost179 | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| 9 (scveh.line9) | scveh.h_smr_bad | scveh.h_smr_bad |
| 13 | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| 10 | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| 11 | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| 14 | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| 15 | scveh.h_low_use, scveh.screen | scveh.h_low_use, scveh.screen |
| 16 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen |
| 25 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen |
| 17 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen |
| 18 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen |
| 19 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen |
| 20 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen | scveh.h_bonus_mixed, scveh.h_low_use, scveh.screen |

## Raw second transcription

```yaml
```yaml
lines:
  # ---- helpers: business-use percentage (miles carried as cents so prorate can divide them) ----
  - id: scveh.h_cent
    printed: "(helper)"
    label: "One cent per mile, used to carry miles as a money amount for the percentage"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: scveh.h_biz_c
    printed: "(helper)"
    label: "Business miles (line 44a) in cents-per-mile units"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}
  - id: scveh.h_comm_c
    printed: "(helper)"
    label: "Commuting miles (line 44b) in cents-per-mile units"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}
  - id: scveh.h_other_c
    printed: "(helper)"
    label: "Other miles (line 44c) in cents-per-mile units"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}
  - id: scveh.h_total_c
    printed: "(helper)"
    label: "Total number of miles the vehicle is driven for all purposes"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_biz_c, scveh.h_comm_c, scveh.h_other_c]}
  - id: scveh.h_two
    printed: "(helper)"
    label: "Two, for the more-than-50% test"
    type: Count
    expr: {op: param, ref: sc.count2}
  - id: scveh.h_biz_x2
    printed: "(helper)"
    label: "Twice the business miles"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_biz_c, count: scveh.h_two}
  - id: scveh.h_low_use
    printed: "(helper)"
    label: "Property used 50% or less in a qualified business use (Form 4562 line 27)"
    type: Bool
    expr: {op: test, le: [scveh.h_biz_x2, scveh.h_total_c]}
    note: "Line 27 requires straight line over the ADS recovery period, and no ADS table is supplied. An owned vehicle deducting actual expenses at 50% or less is refused, not computed."

  # ---- helpers: path gates ----
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: scveh.h_smr_bad
    printed: "(helper)"
    label: "Standard mileage rate chosen but the conditions to take it are not met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "standard"}]}
        - {op: test, eq: [scveh.smr_ok, {const: false}]}
  - id: scveh.h_deprec
    printed: "(helper)"
    label: "Owned vehicle with actual expenses: depreciation applies"
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
  - id: scveh.h_bonus_mixed
    printed: "(helper)"
    label: "The special allowance choice is not the same for all property in the class"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_is2025, {const: true}]}
        - {op: test, eq: [scveh.bonus_same, {const: false}]}
  - id: scveh.h_suv_applies
    printed: "(helper)"
    label: "SUV or certain other vehicle subject to the $31,300 section 179 limit"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.passenger, {const: false}]}
        - {op: test, eq: [scveh.suv, {const: true}]}

  # ---- helpers: Schedule C line 9 and line 20a ----
  - id: scveh.h_mile_rate
    printed: "(helper)"
    label: "Business standard mileage rate, 70 cents per mile"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}
  - id: scveh.h_mileage
    printed: "(helper)"
    label: "Multiply the number of business miles driven by 0.70"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_mile_rate, count: scveh.miles_business}
  - id: scveh.h_line9_std
    printed: "(helper)"
    label: "Add to this amount your parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_mileage, scveh.parking]}
  - id: scveh.h_oper_biz
    printed: "(helper)"
    label: "The business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}
    note: "The instructions do not say how the business portion is measured or rounded for actual expenses. Chose business miles over total miles, the Form 4562 column (c) measure, with the ratio to 4 decimal places."
  - id: scveh.h_line9_act
    printed: "(helper)"
    label: "Business portion of operating expenses plus business parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_oper_biz, scveh.parking]}
    note: "The actual-expense text does not name parking and tolls. The input is already the business-use amount and excludes them from operating expenses, so it is added without proration."
  - id: scveh.h_lease_biz
    printed: "(helper)"
    label: "The business portion of your rental cost"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}

  # ---- helpers: recovery year and table keys ----
  - id: scveh.h_period
    printed: "(helper)"
    label: "5-year property (automobiles and light general purpose trucks)"
    type: Enum(macrs_period)
    expr: {op: param, ref: sc.period_y5}
    note: "All vehicles in this slice are treated as 5-year property, the class the interface's special allowance question names for vehicles."
  - id: scveh.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [scveh.placed]}
  - id: scveh.h_last
    printed: "(helper)"
    label: "Last year of recovery of 5-year property"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [scveh.h_period]}
  - id: scveh.h_done
    printed: "(helper)"
    label: "The recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [scveh.h_year, scveh.h_last]}
  - id: scveh.h_y1
    printed: "(helper)"
    label: "Recovery year 1"
    type: Count
    expr: {op: param, ref: sc.year1}
  - id: scveh.h_y2
    printed: "(helper)"
    label: "Recovery year 2"
    type: Count
    expr: {op: param, ref: sc.year2}
  - id: scveh.h_y3
    printed: "(helper)"
    label: "Recovery year 3"
    type: Count
    expr: {op: param, ref: sc.year3}
  - id: scveh.h_y4
    printed: "(helper)"
    label: "Recovery year 4 (the 4th and later year column of the limits table)"
    type: Count
    expr: {op: param, ref: sc.year4}
  - id: scveh.h_y5
    printed: "(helper)"
    label: "Recovery year 5"
    type: Count
    expr: {op: param, ref: sc.year5}
  - id: scveh.h_y6
    printed: "(helper)"
    label: "Recovery year 6"
    type: Count
    expr: {op: param, ref: sc.year6}

  # ---- helpers: passenger automobile limits ----
  - id: scveh.h_lim_first_nobonus
    printed: "(helper)"
    label: "First-year limit if you elected not to claim any special depreciation allowance"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit_first_nobonus, keys: [scveh.placed]}
  - id: scveh.h_lim_by_year
    printed: "(helper)"
    label: "Maximum depreciation deduction for the date placed in service and this year of recovery"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_year]}
  - id: scveh.h_lim_y2
    printed: "(helper)"
    label: "Maximum depreciation deduction, 2nd year"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y2]}
  - id: scveh.h_lim_y3
    printed: "(helper)"
    label: "Maximum depreciation deduction, 3rd year"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y3]}
  - id: scveh.h_lim_later
    printed: "(helper)"
    label: "Maximum depreciation deduction, 4th and later years"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y4]}

  # ---- helpers: section 179 caps ----
  - id: scveh.h_suv_limit
    printed: "(helper)"
    label: "You cannot elect to expense more than $31,300 of the cost of any SUVs and certain other vehicles"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_179_a
    printed: "(helper)"
    label: "Elected section 179 cost, not more than the business cost"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.bus_cost]}
  - id: scveh.h_179_b
    printed: "(helper)"
    label: "Section 179 deduction claimed this year (not more than line 9)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_179_a, scveh.line9w]}
  - id: scveh.h_179_suv
    printed: "(helper)"
    label: "Section 179 deduction, not more than the SUV limit"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_179_b, scveh.h_suv_limit]}

  # ---- helpers: special allowance and regular MACRS ----
  - id: scveh.h_rate40
    printed: "(helper)"
    label: "40% special depreciation allowance percentage"
    type: Rate
    expr: {op: param, ref: sc.bonus_rate_40}
  - id: scveh.h_b40
    printed: "(helper)"
    label: "Multiply line 15 by 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: scveh.h_rate40}
  - id: scveh.h_conv_hy
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
    label: "Depreciation rate from tables, half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_conv_hy, scveh.h_year]}
  - id: scveh.h_rate_mq
    printed: "(helper)"
    label: "Depreciation rate from tables, mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_qconv, scveh.h_year]}
  - id: scveh.h_rate_prior
    printed: "(helper)"
    label: "Depreciation rate from tables, convention of the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_year]}
  - id: scveh.h_tent_hy
    printed: "(helper)"
    label: "Multiply line 18 by line 6, half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_hy}
  - id: scveh.h_tent_mq
    printed: "(helper)"
    label: "Multiply line 18 by line 6, mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_mq}
  - id: scveh.h_tent_prior
    printed: "(helper)"
    label: "Multiply line 18 by line 6, convention of the year placed in service"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_prior}

  # ---- helpers: unrecovered basis after the recovery period (Pub. 946 ch. 5) ----
  - id: scveh.h_u_base
    printed: "(helper)"
    label: "Cost or other basis reduced by section 179 deductions"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.prior_179}
    note: "Unrecovered basis uses the depreciation that would have been allowable at 100% use. The closed interface supplies only the section 179 amount claimed, so that amount is used as the allowable amount."
  - id: scveh.h_u_lim1
    printed: "(helper)"
    label: "First-year limit without the special allowance"
    type: NonNegDollars
    expr: {op: copy, from: scveh.h_lim_first_nobonus}
  - id: scveh.h_u_lim1_net
    printed: "(helper)"
    label: "First-year limit less the section 179 deduction claimed"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.h_u_lim1, take: scveh.prior_179}
  - id: scveh.h_u_r1
    printed: "(helper)"
    label: "Depreciation rate, recovery year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y1]}
  - id: scveh.h_u_r2
    printed: "(helper)"
    label: "Depreciation rate, recovery year 2"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y2]}
  - id: scveh.h_u_r3
    printed: "(helper)"
    label: "Depreciation rate, recovery year 3"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y3]}
  - id: scveh.h_u_r4
    printed: "(helper)"
    label: "Depreciation rate, recovery year 4"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y4]}
  - id: scveh.h_u_r5
    printed: "(helper)"
    label: "Depreciation rate, recovery year 5"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y5]}
  - id: scveh.h_u_r6
    printed: "(helper)"
    label: "Depreciation rate, recovery year 6"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y6]}
  - id: scveh.h_u_t1
    printed: "(helper)"
    label: "Table depreciation at 100% use, recovery year 1"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_u_base, rate: scveh.h_u_r1}
  - id: scveh.h_u_t2
    printed: "(helper)"
    label: "Table depreciation at 100% use, recovery year 2"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_u_base, rate: scveh.h_u_r2}
  - id: scveh.h_u_t3
    printed: "(helper)"
    label: "Table depreciation at 100% use, recovery year 3"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_u_base, rate: scveh.h_u_r3}
  - id: scveh.h_u_t4
    printed: "(helper)"
    label: "Table depreciation at 100% use, recovery year 4"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_u_base, rate: scveh.h_u_r4}
  - id: scveh.h_u_t5
    printed: "(helper)"
    label: "Table depreciation at 100% use, recovery year 5"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_u_base, rate: scveh.h_u_r5}
  - id: scveh.h_u_t6
    printed: "(helper)"
    label: "Table depreciation at 100% use, recovery year 6"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_u_base, rate: scveh.h_u_r6}
  - id: scveh.h_u_a1
    printed: "(helper)"
    label: "Depreciation allowable at 100% use, recovery year 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_u_t1, scveh.h_u_lim1_net]}
  - id: scveh.h_u_a2
    printed: "(helper)"
    label: "Depreciation allowable at 100% use, recovery year 2"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_u_t2, scveh.h_lim_y2]}
  - id: scveh.h_u_a3
    printed: "(helper)"
    label: "Depreciation allowable at 100% use, recovery year 3"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_u_t3, scveh.h_lim_y3]}
  - id: scveh.h_u_a4
    printed: "(helper)"
    label: "Depreciation allowable at 100% use, recovery year 4"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_u_t4, scveh.h_lim_later]}
  - id: scveh.h_u_a5
    printed: "(helper)"
    label: "Depreciation allowable at 100% use, recovery year 5"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_u_t5, scveh.h_lim_later]}
  - id: scveh.h_u_a6
    printed: "(helper)"
    label: "Depreciation allowable at 100% use, recovery year 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_u_t6, scveh.h_lim_later]}
  - id: scveh.h_u_dep
    printed: "(helper)"
    label: "Total depreciation allowable over the recovery period at 100% use"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_u_a1, scveh.h_u_a2, scveh.h_u_a3, scveh.h_u_a4, scveh.h_u_a5, scveh.h_u_a6]}
  - id: scveh.h_unrecovered
    printed: "(helper)"
    label: "Unrecovered basis"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.h_u_base, take: scveh.h_u_dep}
    note: "Only a vehicle placed in service in 2019 is past its recovery period in 2025, and 2025 is its first such year, so no earlier post-recovery deduction reduces this amount."
  - id: scveh.h_post_tent
    printed: "(helper)"
    label: "Unrecovered basis times the business/investment-use percentage"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.h_unrecovered, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}

  # ---- printed lines ----
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.method, {const: "standard"}]}
          then: scveh.h_line9_std
        - guard: {op: test, eq: [scveh.method, {const: "actual"}]}
          then: scveh.h_line9_act
    refuses: [scveh.h_smr_bad]
    note: "The rule barring actual expenses on a leased vehicle after earlier use of the standard mileage rate has no matching input for leased vehicles, so it is not tested here."
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.method, {const: "actual"}]}
              - {op: test, eq: [scveh.owned, {const: false}]}
          then: scveh.h_lease_biz
        - guard:
            op: test
            any:
              - {op: test, eq: [scveh.method, {const: "standard"}]}
              - {op: test, eq: [scveh.owned, {const: true}]}
          then: scveh.h_zero
  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}
    refuses: [scveh.screen, scveh.h_low_use]
    note: "The text does not say how to round the business/investment-use percentage (line 8). Chose 4 decimal places (a percentage to two decimals) wherever the percentage is applied. Line 12 is the cost input, since vehicle credits are screened out."
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.cost
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "none"}]}
          then: scveh.h_lim_first_nobonus
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, ne: [scveh.bonus_choice, {const: "none"}]}
          then: scveh.h_lim_by_year
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, lt: [scveh.h_year, {const: 4, type: Count}]}
          then: scveh.h_lim_by_year
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, ge: [scveh.h_year, {const: 4, type: Count}]}
          then: scveh.h_lim_later
    note: "The limits do not apply to a vehicle that is not a passenger automobile, and the worksheet has no entry for that case. Chose the vehicle's cost here so that no limit binds later in the worksheet."
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [scveh.h_suv_applies, {const: true}]}
          then: scveh.h_179_suv
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [scveh.h_suv_applies, {const: false}]}
          then: scveh.h_179_b
        - guard: {op: test, eq: [scveh.h_is2025, {const: false}]}
          then: scveh.h_zero
    note: "An election above line 9, the business cost or the $31,300 limit is reduced to the limit and not refused. The Form 4562 line 11 business income limit is applied outside this per-vehicle slice, so this line does not reflect it."
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
    expr: {op: subtract_floor0, from: scveh.bus_cost, take: scveh.line14}
  - id: scveh.line16
    printed: "16"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. This is your special depreciation allowance. Enter -0- if this is not the year you placed the car in service, the car is not qualified property, or you elected not to claim a special depreciation allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
              - {op: test, eq: [scveh.after_jan19, {const: true}]}
          then: scveh.line15
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - op: test
                any:
                  - {op: test, eq: [scveh.bonus_choice, {const: "forty"}]}
                  - op: test
                    all:
                      - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
                      - {op: test, eq: [scveh.after_jan19, {const: false}]}
          then: scveh.h_b40
        - guard:
            op: test
            any:
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.bonus_choice, {const: "none"}]}
          then: scveh.h_zero
    refuses: [scveh.h_bonus_mixed]
    note: "A vehicle acquired before January 20, 2025 is limited to 40% even when the answer is 'full'."
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Special depreciation allowance for qualified listed property, limited to the amount on worksheet line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line16, scveh.line11]}
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
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: true}]}
          then: scveh.h_tent_mq
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: false}]}
          then: scveh.h_tent_hy
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.h_done, {const: false}]}
          then: scveh.h_tent_prior
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.h_done, {const: true}]}
              - {op: test, eq: [scveh.passenger, {const: true}]}
          then: scveh.h_post_tent
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.h_done, {const: true}]}
              - {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.h_zero
    note: "After the recovery period the table rate has no entry. A passenger automobile uses its business share of unrecovered basis, following the Pub. 946 example; other listed property gets no deduction."
  - id: scveh.line20
    printed: "20"
    label: "Enter the lesser of line 17 or line 19. This is your MACRS depreciation deduction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}

  # ---- result interfaces ----
  - id: scveh.bonus
    printed: "(helper)"
    label: "Special depreciation allowance claimed for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_deprec, {const: true}]}
          then: scveh.bonus_allowed
        - guard: {op: test, eq: [scveh.h_deprec, {const: false}]}
          then: scveh.h_zero
  - id: scveh.macrs
    printed: "(helper)"
    label: "MACRS depreciation deduction for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_deprec, {const: true}]}
          then: scveh.line20
        - guard: {op: test, eq: [scveh.h_deprec, {const: false}]}
          then: scveh.h_zero
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Elected section 179 cost of this vehicle for 2025 (Form 4562 line 26, column (i))"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_deprec, {const: true}]}
          then: scveh.line10
        - guard: {op: test, eq: [scveh.h_deprec, {const: false}]}
          then: scveh.h_zero
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Depreciable basis of this vehicle if placed in service during the last 3 months of the tax year (mid-quarter test)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_deprec, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [scveh.quarter, {const: "q4"}]}
          then: scveh.line15
        - guard:
            op: test
            any:
              - {op: test, eq: [scveh.h_deprec, {const: false}]}
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, ne: [scveh.quarter, {const: "q4"}]}
          then: scveh.h_zero
    note: "The basis reflects personal use and section 179 but not the special allowance, as Pub. 946 states. Worksheet line 15 is exactly that amount."
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Depreciable basis of this vehicle if placed in service during the tax year (mid-quarter test)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_deprec, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
          then: scveh.line15
        - guard:
            op: test
            any:
              - {op: test, eq: [scveh.h_deprec, {const: false}]}
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
          then: scveh.h_zero
  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service during the tax year, including listed property from Part V (Form 4562 line 2)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_deprec, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
          then: scveh.bus_cost
        - guard:
            op: test
            any:
              - {op: test, eq: [scveh.h_deprec, {const: false}]}
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
          then: scveh.h_zero
    note: "Worksheet 1 counts all eligible section 179 property, not only the elected amount. The text does not say whether line 2 uses full or business cost for a vehicle; chose business cost, following line 6 column (b)."
```
```
