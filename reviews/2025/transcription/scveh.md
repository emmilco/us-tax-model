# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5f6ceba5d641a62ef3f5c2b6272ae35d2b4e75ea0e809361bbdfa7127be89cc9 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 849034d5f218a4d960cffda96f2863fd026904c3e0c16cc037940e48382040f2 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 91dba7afb747e63ea0fd232952204e9c58e4f1a6edb5c5bc6072e9cc601dc840 |
| printed lines compared | 21 |
| agree / disagree / missing | 7 / 14 / 0 |
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

Second transcription's note: The pages do not define this interface name. Read as this vehicle's Form 4562 line 25 amount.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). The candidate also reads answers the source does not need there (scveh.screen, scveh.cost). Triage executable-triage-v2 (triage/scveh.json): 3021 of 3164 comparisons agree; on completed returns {"candidate-unknown": 2, "value": 6}.

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

Second transcription's note: The pages do not define this interface name. Read as this vehicle's line 26 column (h) amount.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). The candidate also reads answers the source does not need there (scveh.screen, scveh.cost). Triage executable-triage-v2 (triage/scveh.json): 2343 of 3164 comparisons agree; on completed returns {"candidate-unknown": 2, "value": 161}.

### scveh.s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "10"}}, {"guard": {"args": [{"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The pages do not define this interface name. Read as the amount elected for a vehicle placed in service in 2025, after the limits for passenger automobiles and SUVs, and before the Form 4562 lines 5 and 11 limits, which apply to the taxpayer.

Ruling: representation; refusals and withheld answers on refused or partial records only; no completed return differs. Triage executable-triage-v2 (triage/scveh.json): 2943 of 3164 comparisons agree; on completed returns no difference.

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

Second transcription's note: Pub. 946: the depreciable basis for the mid-quarter test reflects section 179 and personal use, but not the special allowance. That is worksheet line 15. A vehicle on the standard mileage rate is not depreciated, so it counts as zero.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 2799 of 3164 comparisons agree; on completed returns {"value": 1}.

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 2853 of 3164 comparisons agree; on completed returns {"value": 6}.

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

Second transcription's note: The pages do not define this interface name. Read as the Form 4562 line 2 amount: the full eligible cost, not just the elected amount, at the business-use cost of Part I column (b). A vehicle on the standard mileage rate or a leased vehicle counts as zero; the supplied text does not settle that exclusion.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 2853 of 3164 comparisons agree; on completed returns {"value": 6}.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"alternatives": [{"guard": {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}], "op": "choose"}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). The candidate's lease refusal is the same rule as scveh.lease_smr_bad (BUG-0312). Triage executable-triage-v2 (triage/scveh.json): 2161 of 3164 comparisons agree; on completed returns {"value": 156}.

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The lease inclusion amount for a term of 30 days or more is outside this document; the sc.special screen covers it.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). Triage executable-triage-v2 (triage/scveh.json): 2953 of 3164 comparisons agree; on completed returns {"value": 5}.

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

Second transcription's note: Worksheet line 8, the business/investment-use percentage, is carried inside each prorate as business miles over total miles. The vehicle credits that reduce line 12 are screened out, so line 12 is the cost input.

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 955 of 3164 comparisons agree; on completed returns {"project-refuses": 72, "project-unknown": 14, "value": 359}.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}}, {"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(d)"}}], "op": "choose"}
```

Second transcription's note: The limits apply only to passenger automobiles, and the text gives no figure for other vehicles. Chosen: for those, line 7 carries the vehicle's cost, a stand-in that makes line 9 equal the business cost and so never binds. After the recovery period the '4th & later' figure applies, looked up with year 4.

Ruling: representation; line 7 is a worksheet line for passenger automobiles, figured for every vehicle and read only on the scveh.passenger branches (checked on stage14.veh.suv_179 with passenger answered both ways: allowance $20,200 and $70,000). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 1967 of 3164 comparisons agree; on completed returns {"candidate-unknown": 9, "project-refuses": 75, "project-unknown": 17, "value": 73}.

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

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 534 of 3164 comparisons agree; on completed returns {"candidate-unknown": 9, "project-refuses": 75, "project-unknown": 1, "value": 429}.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"of": [{"line": "9 (scveh.line9w)"}, {"of": [{"line": "13"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "(i)"}, {"param": "s179.suv_limit"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.suv"}], "test": "ne"}], "test": "any"}, "then": {"line": "(i)"}}], "op": "choose"}], "op": "smaller_of"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; the section 179 deduction on both sides. The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 2611 of 3164 comparisons agree; on completed returns {"project-refuses": 75, "project-unknown": 16}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}], "test": "any"}, {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"line": "15"}}], "op": "choose"}
```

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. Triage executable-triage-v2 (triage/scveh.json): 2417 of 3164 comparisons agree; on completed returns {"project-refuses": 75, "project-unknown": 22, "value": 6}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, {"args": [{"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"input": "scveh.prior_179"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}, {"from": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}], "op": "smaller_of"}], "op": "sum"}}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"param": "sc.period_y5"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second transcription's note: Worksheet line 6 cannot be one line because choose does not select rates or conventions, so one product is written for each convention. After the recovery period, a passenger automobile uses unrecovered basis; other listed property gets no deduction (Pub. 946 caution).

Ruling: ambiguity (owner ruling amb.2025.vehicle_business_pct); the project rounds the business-use percentage to 6 places, the candidate differently; i4562 p. 14, Column (c). The project-side refusal and unknown records are vehicles on the standard mileage rate, where this depreciation line is not read, so the return completes. A 2019 vehicle is figured from unrecovered basis (scveh.post; p946 p. 61; BUG-0059). Triage executable-triage-v2 (triage/scveh.json): 1344 of 3164 comparisons agree; on completed returns {"candidate-unknown": 1, "project-refuses": 75, "project-unknown": 7, "value": 259}.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| scveh.macrs | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| scveh.s179_2025 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| scveh.mq_q4 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| scveh.mq_total | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| scveh.cost179 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 9 (scveh.line9) | scveh.h_lease_bad, scveh.h_smr_bad | scveh.h_lease_bad, scveh.h_smr_bad |
| 20a | scveh.h_lease_bad | scveh.h_lease_bad |
| 13 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 7 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 9 (scveh.line9w) | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 10 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 11 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 14 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 15 | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 16 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 25 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 17 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 18 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 19 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |
| 20 | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened | scveh.h_bonus_mixed, scveh.h_low_use, scveh.h_placed_early, scveh.h_screened |

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
    label: "One cent, to express a mile count as money for the division"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: scveh.h_biz_c
    printed: "(helper)"
    label: "Business miles (line 44a), expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}
  - id: scveh.h_comm_c
    printed: "(helper)"
    label: "Commuting miles (line 44b), expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}
  - id: scveh.h_other_c
    printed: "(helper)"
    label: "Other miles (line 44c), expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}
  - id: scveh.h_total_c
    printed: "(helper)"
    label: "Total number of miles the vehicle is driven for all purposes, expressed in cents"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_biz_c, scveh.h_comm_c, scveh.h_other_c]}
  - id: scveh.h_has_miles
    printed: "(helper)"
    label: "The vehicle was driven during the year"
    type: Bool
    expr: {op: test, gt: [scveh.h_total_c, {const: 0}]}
  - id: scveh.h_smr_bad
    printed: "(gate)"
    label: "Standard mileage rate taken, but the conditions for taking it are not met"
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
  - id: scveh.h_mile_rate
    printed: "(helper)"
    label: "Standard mileage rate, 70 cents per mile"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}
  - id: scveh.h_mileage
    printed: "(helper)"
    label: "Multiply the number of business miles driven by 0.70"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_mile_rate, count: scveh.miles_business}
  - id: scveh.h_standard
    printed: "(helper)"
    label: "Add to this amount your parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_mileage, scveh.parking]}
  - id: scveh.h_op_figured
    printed: "(helper)"
    label: "Business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc."
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.operating, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}
    note: "The Schedule C instructions say 'business portion' without a method. Chosen: the mileage ratio from Form 4562 column (c). The text states no rounding for the percentage; chosen: four decimal places of the ratio (a percentage to two decimals), used throughout this document."
  - id: scveh.h_op_bus
    printed: "(helper)"
    label: "Business portion of operating expenses (zero if the vehicle was not driven)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_has_miles, {const: true}]}, then: scveh.h_op_figured}
        - {guard: {op: test, eq: [scveh.h_has_miles, {const: false}]}, then: scveh.h_zero}
  - id: scveh.h_actual
    printed: "(helper)"
    label: "Actual expenses for line 9: business portion of operating expenses plus business parking fees and tolls"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_op_bus, scveh.parking]}
    note: "The actual-expense text lists gasoline, oil, repairs, insurance, license plates, 'etc.' and does not name parking and tolls. The operating input excludes them and the parking input is already business-only, so it is added in full."
  - id: scveh.line9
    printed: "9 (scveh.line9)"
    label: "Car and truck expenses"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.method, {const: "standard"}]}, then: scveh.h_standard}
        - {guard: {op: test, eq: [scveh.method, {const: "actual"}]}, then: scveh.h_actual}
    refuses: [scveh.h_smr_bad, scveh.h_lease_bad]
  - id: scveh.h_lease_gate
    printed: "(helper)"
    label: "Leased vehicle for which actual expenses are deducted"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: false}]}
  - id: scveh.h_lease_figured
    printed: "(helper)"
    label: "The business portion of your rental cost"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.lease, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}
  - id: scveh.h_lease_bus
    printed: "(helper)"
    label: "Business portion of lease payments (zero if the vehicle was not driven)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_has_miles, {const: true}]}, then: scveh.h_lease_figured}
        - {guard: {op: test, eq: [scveh.h_has_miles, {const: false}]}, then: scveh.h_zero}
  - id: scveh.line20a
    printed: "20a"
    label: "Rent or lease: vehicles, machinery, and equipment"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_lease_gate, {const: true}]}, then: scveh.h_lease_bus}
        - {guard: {op: test, eq: [scveh.h_lease_gate, {const: false}]}, then: scveh.h_zero}
    refuses: [scveh.h_lease_bad]
    note: "The lease inclusion amount for a term of 30 days or more is outside this document; the sc.special screen covers it."
  - id: scveh.h_dep
    printed: "(helper)"
    label: "Owned vehicle for which actual expenses are deducted, so depreciation is shown on line 13"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: true}]}
  - id: scveh.h_screened
    printed: "(gate)"
    label: "A depreciated vehicle in a situation this tool does not compute"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - {op: test, eq: [scveh.screen, {const: true}]}
  - id: scveh.h_placed_early
    printed: "(gate)"
    label: "A depreciated vehicle placed in service before 2019"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [scveh.placed, {const: "y2005"}]}
            - {op: test, eq: [scveh.placed, {const: "y2006"}]}
            - {op: test, eq: [scveh.placed, {const: "y2007"}]}
            - {op: test, eq: [scveh.placed, {const: "y2008"}]}
            - {op: test, eq: [scveh.placed, {const: "y2009"}]}
            - {op: test, eq: [scveh.placed, {const: "y2010"}]}
            - {op: test, eq: [scveh.placed, {const: "y2011"}]}
            - {op: test, eq: [scveh.placed, {const: "y2012"}]}
            - {op: test, eq: [scveh.placed, {const: "y2013"}]}
            - {op: test, eq: [scveh.placed, {const: "y2014"}]}
            - {op: test, eq: [scveh.placed, {const: "y2015"}]}
            - {op: test, eq: [scveh.placed, {const: "y2016"}]}
            - {op: test, eq: [scveh.placed, {const: "y2017"}]}
            - {op: test, eq: [scveh.placed, {const: "y2018"}]}
  - id: scveh.h_two
    printed: "(helper)"
    label: "Two"
    type: Count
    expr: {op: param, ref: sc.count2}
  - id: scveh.h_biz_x2
    printed: "(helper)"
    label: "Business miles times two, to test business use of more than 50% exactly"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_biz_c, count: scveh.h_two}
  - id: scveh.h_over50
    printed: "(helper)"
    label: "Property used more than 50% in a qualified business use"
    type: Bool
    expr: {op: test, gt: [scveh.h_biz_x2, scveh.h_total_c]}
  - id: scveh.h_low_use
    printed: "(gate)"
    label: "A depreciated vehicle used 50% or less in a qualified business use (Form 4562, line 27)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - {op: test, eq: [scveh.h_over50, {const: false}]}
    note: "Line 27 requires straight line depreciation over the ADS recovery period. The table catalog has only GDS percentages and the worksheet slice covers line 26, so this case refuses."
  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.cost, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}
    refuses: [scveh.h_screened, scveh.h_placed_early, scveh.h_low_use]
    note: "Worksheet line 8, the business/investment-use percentage, is carried inside each prorate as business miles over total miles. The vehicle credits that reduce line 12 are screened out, so line 12 is the cost input."
  - id: scveh.h_is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2025"}]}
  - id: scveh.h_bonus_claimed
    printed: "(helper)"
    label: "Placed in service in 2025 and a special depreciation allowance is claimed"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_is2025, {const: true}]}
        - {op: test, ne: [scveh.bonus_choice, {const: "none"}]}
  - id: scveh.h_y1
    printed: "(helper)"
    label: "First year in service"
    type: Count
    expr: {op: param, ref: sc.year1}
  - id: scveh.h_y2
    printed: "(helper)"
    label: "Second year"
    type: Count
    expr: {op: param, ref: sc.year2}
  - id: scveh.h_y3
    printed: "(helper)"
    label: "Third year"
    type: Count
    expr: {op: param, ref: sc.year3}
  - id: scveh.h_y4
    printed: "(helper)"
    label: "Fourth year; the limit tables use one figure for the 4th and later years"
    type: Count
    expr: {op: param, ref: sc.year4}
  - id: scveh.h_y5
    printed: "(helper)"
    label: "Fifth year"
    type: Count
    expr: {op: param, ref: sc.year5}
  - id: scveh.h_y6
    printed: "(helper)"
    label: "Sixth year"
    type: Count
    expr: {op: param, ref: sc.year6}
  - id: scveh.h_period
    printed: "(helper)"
    label: "5-year property (automobiles and light general purpose trucks)"
    type: Enum(macrs_period)
    expr: {op: param, ref: sc.period_y5}
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
  - id: scveh.h_within
    printed: "(helper)"
    label: "2025 is within the recovery period"
    type: Bool
    expr: {op: test, le: [scveh.h_year, scveh.h_last]}
  - id: scveh.h_lim_bonus
    printed: "(helper)"
    label: "First-year maximum with the special depreciation allowance"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y1]}
  - id: scveh.h_lim_first
    printed: "(helper)"
    label: "First-year maximum without the special depreciation allowance"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit_first_nobonus, keys: [scveh.placed]}
  - id: scveh.h_lim_year
    printed: "(helper)"
    label: "Maximum for the 2025 year of recovery"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_year]}
  - id: scveh.h_lim2
    printed: "(helper)"
    label: "Maximum for the second year"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y2]}
  - id: scveh.h_lim3
    printed: "(helper)"
    label: "Maximum for the third year"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y3]}
  - id: scveh.h_lim4
    printed: "(helper)"
    label: "Maximum for the 4th and later years"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: auto_limit, keys: [scveh.placed, scveh.h_y4]}
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
              - {op: test, eq: [scveh.h_bonus_claimed, {const: true}]}
          then: scveh.h_lim_bonus
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [scveh.h_bonus_claimed, {const: false}]}
          then: scveh.h_lim_first
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.h_within, {const: true}]}
          then: scveh.h_lim_year
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.passenger, {const: true}]}
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.h_within, {const: false}]}
          then: scveh.h_lim4
    refuses: [scveh.h_screened, scveh.h_placed_early, scveh.h_low_use]
    note: "The limits apply only to passenger automobiles, and the text gives no figure for other vehicles. Chosen: for those, line 7 carries the vehicle's cost, a stand-in that makes line 9 equal the business cost and so never binds. After the recovery period the '4th & later' figure applies, looked up with year 4."
  - id: scveh.line9w
    printed: "9 (scveh.line9w)"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.line7, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}
  - id: scveh.h_suv_max
    printed: "(helper)"
    label: "The most you can elect to expense for an SUV or certain other vehicles"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_elect_suv
    printed: "(helper)"
    label: "Elected section 179 cost, limited to $31,300"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.h_suv_max]}
  - id: scveh.h_is_suv
    printed: "(helper)"
    label: "Vehicle subject to the $31,300 section 179 limit"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.passenger, {const: false}]}
        - {op: test, eq: [scveh.suv, {const: true}]}
  - id: scveh.h_elect_cap
    printed: "(helper)"
    label: "Elected section 179 cost after the SUV limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is_suv, {const: true}]}, then: scveh.h_elect_suv}
        - {guard: {op: test, eq: [scveh.h_is_suv, {const: false}]}, then: scveh.s179_elect}
  - id: scveh.h_elect_bus
    printed: "(helper)"
    label: "Elected section 179 cost, not more than the business cost"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_elect_cap, scveh.bus_cost]}
  - id: scveh.h_line10_2025
    printed: "(helper)"
    label: "Section 179 deduction claimed this year (not more than line 9)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_elect_bus, scveh.line9w]}
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.h_line10_2025}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.h_zero}
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
        - {guard: {op: test, eq: [scveh.h_is2025, {const: true}]}, then: scveh.line10}
        - {guard: {op: test, eq: [scveh.h_is2025, {const: false}]}, then: scveh.prior_179}
  - id: scveh.line15
    printed: "15"
    label: "Subtract line 14 from line 13. This is your tentative basis for depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.bus_cost, take: scveh.line14}
  - id: scveh.h_bonus_mixed
    printed: "(gate)"
    label: "The special allowance choice is not the same for all 5-year property placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - {op: test, eq: [scveh.h_is2025, {const: true}]}
        - {op: test, eq: [scveh.bonus_same, {const: false}]}
  - id: scveh.h_bonus_full
    printed: "(helper)"
    label: "Property acquired after January 19, 2025, with the 100% special depreciation allowance"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_is2025, {const: true}]}
        - {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
        - {op: test, eq: [scveh.after_jan19, {const: true}]}
  - id: scveh.h_bonus_forty
    printed: "(helper)"
    label: "Property with the 40% special depreciation allowance: acquired before January 20, 2025, or electing 40% instead of 100%"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_bonus_claimed, {const: true}]}
        - {op: test, eq: [scveh.h_bonus_full, {const: false}]}
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
        - {guard: {op: test, eq: [scveh.h_bonus_full, {const: true}]}, then: scveh.line15}
        - {guard: {op: test, eq: [scveh.h_bonus_forty, {const: true}]}, then: scveh.h_bonus40}
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_bonus_full, {const: false}]}
              - {op: test, eq: [scveh.h_bonus_forty, {const: false}]}
          then: scveh.h_zero
    refuses: [scveh.h_bonus_mixed]
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year, limited to worksheet line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line16, scveh.line11]}
    note: "The worksheet covers line 16 equal to or less than line 11 but not greater. Chosen: when line 16 is greater, the allowance is held to line 11, as the overall limit on depreciation requires."
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
    label: "Depreciation rate from the tables, half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_conv_hy, scveh.h_year]}
  - id: scveh.h_rate_mq
    printed: "(helper)"
    label: "Depreciation rate from the tables, mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.h_qconv, scveh.h_year]}
  - id: scveh.h_rate_prior
    printed: "(helper)"
    label: "Depreciation rate from the tables, convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_year]}
  - id: scveh.h_m_hy
    printed: "(helper)"
    label: "Multiply line 18 by line 6, half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_hy}
  - id: scveh.h_m_mq
    printed: "(helper)"
    label: "Multiply line 18 by line 6, mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_mq}
  - id: scveh.h_m_prior
    printed: "(helper)"
    label: "Multiply line 18 by line 6, convention used in the year placed in service"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_prior}
  - id: scveh.h_b
    printed: "(helper)"
    label: "Basis for the recovery period at 100% business use: cost less the section 179 deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.prior_179}
  - id: scveh.h_lim1_net
    printed: "(helper)"
    label: "First-year maximum left after the section 179 deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.h_lim_first, take: scveh.prior_179}
  - id: scveh.h_r1
    printed: "(helper)"
    label: "Table rate, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y1]}
  - id: scveh.h_r2
    printed: "(helper)"
    label: "Table rate, year 2"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y2]}
  - id: scveh.h_r3
    printed: "(helper)"
    label: "Table rate, year 3"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y3]}
  - id: scveh.h_r4
    printed: "(helper)"
    label: "Table rate, year 4"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y4]}
  - id: scveh.h_r5
    printed: "(helper)"
    label: "Table rate, year 5"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y5]}
  - id: scveh.h_r6
    printed: "(helper)"
    label: "Table rate, year 6"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [scveh.h_period, scveh.prior_conv, scveh.h_y6]}
  - id: scveh.h_t1
    printed: "(helper)"
    label: "Depreciation figured at 100% business use, year 1"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b, rate: scveh.h_r1}
  - id: scveh.h_t2
    printed: "(helper)"
    label: "Depreciation figured at 100% business use, year 2"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b, rate: scveh.h_r2}
  - id: scveh.h_t3
    printed: "(helper)"
    label: "Depreciation figured at 100% business use, year 3"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b, rate: scveh.h_r3}
  - id: scveh.h_t4
    printed: "(helper)"
    label: "Depreciation figured at 100% business use, year 4"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b, rate: scveh.h_r4}
  - id: scveh.h_t5
    printed: "(helper)"
    label: "Depreciation figured at 100% business use, year 5"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b, rate: scveh.h_r5}
  - id: scveh.h_t6
    printed: "(helper)"
    label: "Depreciation figured at 100% business use, year 6"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.h_b, rate: scveh.h_r6}
  - id: scveh.h_a1
    printed: "(helper)"
    label: "Depreciation allowed, year 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_t1, scveh.h_lim1_net]}
  - id: scveh.h_a2
    printed: "(helper)"
    label: "Depreciation allowed, year 2"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_t2, scveh.h_lim2]}
  - id: scveh.h_a3
    printed: "(helper)"
    label: "Depreciation allowed, year 3"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_t3, scveh.h_lim3]}
  - id: scveh.h_a4
    printed: "(helper)"
    label: "Depreciation allowed, year 4"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_t4, scveh.h_lim4]}
  - id: scveh.h_a5
    printed: "(helper)"
    label: "Depreciation allowed, year 5"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_t5, scveh.h_lim4]}
  - id: scveh.h_a6
    printed: "(helper)"
    label: "Depreciation allowed, year 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.h_t6, scveh.h_lim4]}
  - id: scveh.h_recovered
    printed: "(helper)"
    label: "Section 179 deduction and depreciation over the recovery period at 100% business use"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.prior_179, scveh.h_a1, scveh.h_a2, scveh.h_a3, scveh.h_a4, scveh.h_a5, scveh.h_a6]}
  - id: scveh.h_unrecovered
    printed: "(helper)"
    label: "Unrecovered basis"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.cost, take: scveh.h_recovered}
    note: "Pub. 946 defines unrecovered basis using amounts allowable 'if ... the passenger automobile limits had not applied', but its worked example ($31,500 less $16,935) subtracts the amounts as limited, and unlimited amounts would leave nothing to deduct. Chosen: the example, with the limits applied at 100% business use. Within the 2019 to 2025 scope, only a 2019 vehicle reaches this path, and 2025 is its first year after the recovery period, so no post-recovery deductions need subtracting."
  - id: scveh.h_after_bus
    printed: "(helper)"
    label: "Unrecovered basis times the business/investment-use percentage"
    type: NonNegDollars
    expr: {op: prorate, amount: scveh.h_unrecovered, part: scveh.h_biz_c, whole: scveh.h_total_c, places: 4}
    note: "Pub. 946's example allows the unrecovered basis times the business percentage ($14,565 x 60%) when use is below 100%; the yearly limit comes through lines 7 and 9."
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
              - {op: test, eq: [mq.applies, {const: false}]}
          then: scveh.h_m_hy
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: true}]}
          then: scveh.h_m_mq
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.h_within, {const: true}]}
          then: scveh.h_m_prior
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.h_within, {const: false}]}
              - {op: test, eq: [scveh.passenger, {const: true}]}
          then: scveh.h_after_bus
        - guard:
            op: test
            all:
              - {op: test, eq: [scveh.h_is2025, {const: false}]}
              - {op: test, eq: [scveh.h_within, {const: false}]}
              - {op: test, eq: [scveh.passenger, {const: false}]}
          then: scveh.h_zero
    note: "Worksheet line 6 cannot be one line because choose does not select rates or conventions, so one product is written for each convention. After the recovery period, a passenger automobile uses unrecovered basis; other listed property gets no deduction (Pub. 946 caution)."
  - id: scveh.line20
    printed: "20"
    label: "Enter the lesser of line 17 or line 19. This is your MACRS depreciation deduction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.line17, scveh.line19]}
  - id: scveh.bonus
    printed: "(helper)"
    label: "Form 4562, line 25, for this vehicle: special depreciation allowance (zero if no depreciation is claimed)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.bonus_allowed}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
    note: "The pages do not define this interface name. Read as this vehicle's Form 4562 line 25 amount."
  - id: scveh.macrs
    printed: "(helper)"
    label: "Form 4562, line 26, column (h), for this vehicle: depreciation deduction (zero if no depreciation is claimed)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep, {const: true}]}, then: scveh.line20}
        - {guard: {op: test, eq: [scveh.h_dep, {const: false}]}, then: scveh.h_zero}
    note: "The pages do not define this interface name. Read as this vehicle's line 26 column (h) amount."
  - id: scveh.h_dep2025
    printed: "(helper)"
    label: "A depreciated vehicle placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep, {const: true}]}
        - {op: test, eq: [scveh.h_is2025, {const: true}]}
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Form 4562, line 26, column (i), for this vehicle: elected section 179 cost for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep2025, {const: true}]}, then: scveh.line10}
        - {guard: {op: test, eq: [scveh.h_dep2025, {const: false}]}, then: scveh.h_zero}
    note: "The pages do not define this interface name. Read as the amount elected for a vehicle placed in service in 2025, after the limits for passenger automobiles and SUVs, and before the Form 4562 lines 5 and 11 limits, which apply to the taxpayer."
  - id: scveh.h_q4
    printed: "(helper)"
    label: "A depreciated vehicle placed in service during the last 3 months of 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_dep2025, {const: true}]}
        - {op: test, eq: [scveh.quarter, {const: "q4"}]}
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Depreciable basis of this vehicle if placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_q4, {const: true}]}, then: scveh.line15}
        - {guard: {op: test, eq: [scveh.h_q4, {const: false}]}, then: scveh.h_zero}
    note: "Pub. 946: the depreciable basis for the mid-quarter test reflects section 179 and personal use, but not the special allowance. That is worksheet line 15. A vehicle on the standard mileage rate is not depreciated, so it counts as zero."
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Depreciable basis of this vehicle if placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep2025, {const: true}]}, then: scveh.line15}
        - {guard: {op: test, eq: [scveh.h_dep2025, {const: false}]}, then: scveh.h_zero}
  - id: scveh.cost179
    printed: "(helper)"
    label: "Cost of this vehicle counted as section 179 property placed in service in 2025 (Form 4562, line 2)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [scveh.h_dep2025, {const: true}]}, then: scveh.bus_cost}
        - {guard: {op: test, eq: [scveh.h_dep2025, {const: false}]}, then: scveh.h_zero}
    note: "The pages do not define this interface name. Read as the Form 4562 line 2 amount: the full eligible cost, not just the elected amount, at the business-use cost of Part I column (b). A vehicle on the standard mileage rate or a leased vehicle counts as zero; the supplied text does not settle that exclusion."
```
```
