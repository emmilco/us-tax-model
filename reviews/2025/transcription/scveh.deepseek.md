# Transcription agreement — scveh

Second transcription of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/scveh.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | c59a7e59958816d75b465ffbeb8aeff7778f2e7c8033958d3a49cb8e99934769 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 25b8001143dac766acd7f514d3f53d4894bfd1ece58090817f608708a9ad2267 |
| printed lines compared | 21 |
| agree / disagree / missing | 2 / 19 / 0 |
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
{"line": "25"}
```

Ruling: open

### scveh.macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "19"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"of": [{"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}, {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year2"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year3"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year4"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year5"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "auto_limit"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"param": "sc.year6"}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "smaller_of"}, {"of": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}, {"of": [{"input": "scveh.prior_179"}, {"amount": {"from": {"line": "(d)"}, "op": "subtract_floor0", "take": {"input": "scveh.prior_179"}}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"const": 1}], "op": "keyed_lookup", "table": "macrs_gds"}}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}}], "op": "smaller_of"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "20"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "20"}
```

Ruling: open

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

Ruling: open

### scveh.mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "scveh.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "scveh.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}, {"param": "sc.year4"}], "op": "smaller_of"}, {"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "f4562.macrs_5_mq"}}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### scveh.mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "19"}
```

Ruling: open

### scveh.cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "13"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": true}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "13"}
```

Ruling: open

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"input": "scveh.operating"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}], "op": "sum"}}, {"guard": {"args": [{"const": "standard"}, {"input": "scveh.method"}], "test": "eq"}, "then": {"of": [{"input": "scveh.parking"}, {"amount": {"param": "sc.mileage_rate"}, "count": {"line": "44a"}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}
```

Ruling: open

### 20a — Rent or lease of this vehicle (business portion)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "eq"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "scveh.lease"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "actual"}, {"input": "scveh.method"}], "test": "ne"}, {"args": [{"const": false}, {"input": "scveh.owned"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 13 — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"amount": {"line": "(d)"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second transcription's note: Business/investment-use percentage is figured from business, commuting and other miles and rounded to four decimal places where the IRS text does not state a rounding rule.

Ruling: open

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "auto_limit_first_nobonus"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"keys": [{"line": "(b)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "auto_limit"}}], "op": "choose"}
```

Second:

```json
{"keys": [{"line": "(b)"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}, {"param": "sc.year4"}], "op": "smaller_of"}, {"input": "scveh.bonus_choice"}], "op": "keyed_lookup", "table": "f4562.table2"}
```

Second transcription's note: The passenger automobile limit table is read with the placed-in-service year, the tax-year-in-service key (capped at 4th or later) and the bonus choice.

Ruling: open

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Second:

```json
{"amount": {"line": "7"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, "places": 4, "whole": {"of": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "op": "sum"}}
```

Ruling: open

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"line": "(i)"}}, {"guard": {"args": [{"const": true}, {"input": "scveh.passenger"}], "test": "eq"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}], "test": "lt"}, "then": {"of": [{"line": "(i)"}, {"line": "9 (scveh.line9w)"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project:

```json
{"from": {"line": "9 (scveh.line9w)"}, "op": "subtract_floor0", "take": {"line": "10"}}
```

Second:

```json
{"from": {"line": "9 (scveh.line9w)"}, "op": "subtract", "take": {"line": "10"}}
```

Ruling: open

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
{"from": {"line": "13"}, "op": "subtract", "take": {"line": "14"}}
```

Ruling: open

### 16 — Special depreciation allowance
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "scveh.after_jan19"}], "test": "eq"}, "then": {"line": "15"}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "11"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"amount": {"line": "15"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"line": "15"}}, {"guard": {"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "scveh.bonus_choice"}], "test": "eq"}, {"args": [{"amount": {"const": 1}, "count": {"line": "44a"}, "op": "multiply_count"}, {"of": [{"amount": {"const": 1}, "count": {"line": "44b"}, "op": "multiply_count"}, {"amount": {"const": 1}, "count": {"line": "44c"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "smaller_of"}
```

Ruling: open

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "11"}, {"line": "16"}], "op": "smaller_of"}
```

Second:

```json
{"line": "16"}
```

Ruling: open

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "11"}, "op": "subtract_floor0", "take": {"line": "16"}}
```

Second:

```json
{"from": {"line": "11"}, "op": "subtract", "take": {"line": "16"}}
```

Ruling: open

### 18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "16"}}
```

Second:

```json
{"from": {"line": "15"}, "op": "subtract", "take": {"line": "16"}}
```

Ruling: open

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"keys": [{"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"param": "sc.period_y5"}, {"input": "scveh.prior_conv"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "13"}, "op": "subtract_floor0", "take": {"line": "14"}}}, {"guard": {"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "eq"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}, {"param": "sc.year4"}], "op": "smaller_of"}, {"input": "scveh.quarter"}], "op": "keyed_lookup", "table": "f4562.macrs_5_mq"}}}, {"guard": {"args": [{"const": "q4"}, {"input": "scveh.quarter"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}, {"param": "sc.year4"}], "op": "smaller_of"}], "op": "keyed_lookup", "table": "f4562.macrs_5_hy"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"line": "18"}, "op": "multiply_rate", "rate": {"keys": [{"input": "scveh.prior_conv"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2019"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "y2020"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"param": "sc.year6"}}, {"guard": {"args": [{"const": "y2021"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year5"}}, {"guard": {"args": [{"const": "y2022"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year4"}}, {"guard": {"args": [{"const": "y2023"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year3"}}, {"guard": {"args": [{"const": "y2024"}, {"line": "(b)"}], "test": "eq"}, "then": {"param": "sc.year2"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}, {"param": "sc.year4"}], "op": "smaller_of"}], "op": "keyed_lookup", "table": "f4562.macrs_5_prior"}}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: For a vehicle placed in service in 2019 the recovery period has ended; the provided inputs do not include prior-year MACRS amounts, so the unrecovered basis shown here is cost less prior section 179 only.

Ruling: open

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| scveh.bonus | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| scveh.macrs | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| scveh.s179_2025 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| scveh.mq_q4 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| scveh.mq_total | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| scveh.cost179 | scveh.h_no_miles | scveh.h_no_miles |
| 9 (scveh.line9) | scveh.h_no_miles, scveh.h_smr_bad | scveh.h_no_miles, scveh.h_smr_bad |
| 13 | scveh.h_no_miles | scveh.h_no_miles |
| 9 (scveh.line9w) | scveh.h_no_miles | scveh.h_no_miles |
| 10 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 11 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 14 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 15 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 16 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 25 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 17 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 18 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 19 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |
| 20 | scveh.h_no_miles, scveh.h_s179_bad | scveh.h_no_miles, scveh.h_s179_bad |

## Raw second transcription

```yaml
lines:
  - id: scveh.line9
    printed: "9"
    label: "Car and truck expenses (see instructions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.method, {const: "standard"}]}
          then: scveh.h_line9_standard
        - guard: {op: test, eq: [scveh.method, {const: "actual"}]}
          then: scveh.h_line9_actual
  - id: scveh.line20a
    printed: "20a"
    label: "Vehicles, machinery, and equipment"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_is_actual_leased, {const: true}]}
          then: scveh.h_lease_business
        - guard: {op: test, eq: [scveh.h_is_actual_leased, {const: false}]}
          then: scveh.h_zero
  - id: scveh.bus_cost
    printed: "13"
    label: "Multiply line 12 by line 8. This is your business/investment cost."
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.cost
      part: scveh.h_bm_c
      whole: scveh.h_total_c
      places: 4
    refuses: [scveh.h_no_miles]
    note: "Business/investment-use percentage is figured from business, commuting and other miles and rounded to four decimal places where the IRS text does not state a rounding rule."
  - id: scveh.line7
    printed: "7"
    label: "Maximum depreciation deduction for this year from the appropriate table"
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: f4562.table2
      keys: [scveh.placed, scveh.h_year_key, scveh.bonus_choice]
    note: "The passenger automobile limit table is read with the placed-in-service year, the tax-year-in-service key (capped at 4th or later) and the bonus choice."
  - id: scveh.line9w
    printed: "9"
    label: "Multiply line 7 by line 8. This is your adjusted maximum depreciation deduction."
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.line7
      part: scveh.h_bm_c
      whole: scveh.h_total_c
      places: 4
    refuses: [scveh.h_no_miles]
  - id: scveh.line10
    printed: "10"
    label: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_is2025, {const: true}]}
          then: scveh.h_s179_2025_ok
        - guard: {op: test, eq: [scveh.h_is2025, {const: false}]}
          then: scveh.h_zero
    refuses: [scveh.h_s179_bad]
  - id: scveh.line11
    printed: "11"
    label: "Subtract line 10 from line 9. This is the limit on the amount you can deduct for depreciation (including any special depreciation allowance)."
    type: NonNegDollars
    expr:
      op: subtract
      from: scveh.line9w
      take: scveh.line10
  - id: scveh.line14
    printed: "14"
    label: "Section 179 deduction claimed in the year you placed the car in service."
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
    label: "Subtract line 14 from line 13. This is your tentative basis for depreciation."
    type: NonNegDollars
    expr:
      op: subtract
      from: scveh.bus_cost
      take: scveh.line14
  - id: scveh.line16
    printed: "16"
    label: "Multiply line 15 by the applicable percentage if the special depreciation allowance applies. This is your special depreciation allowance. Enter -0- if this is not the year you placed the car in service, the car is not qualified property, or you elected not to claim a special depreciation allowance."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [scveh.h_bonus_2025, scveh.line11]
  - id: scveh.bonus_allowed
    printed: "25"
    label: "Enter on line 25 your total special depreciation allowance for all qualified listed property."
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.line16
  - id: scveh.line17
    printed: "17"
    label: "Subtract line 16 from line 11. This is the limit on the amount you can deduct for MACRS depreciation."
    type: NonNegDollars
    expr:
      op: subtract
      from: scveh.line11
      take: scveh.line16
  - id: scveh.line18
    printed: "18"
    label: "Subtract line 16 from line 15. This is your basis for depreciation."
    type: NonNegDollars
    expr:
      op: subtract
      from: scveh.line15
      take: scveh.line16
  - id: scveh.line19
    printed: "19"
    label: "Multiply line 18 by line 6. This is your tentative MACRS depreciation deduction."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_too_old, {const: true}]}
          then: scveh.h_unrecovered
        - guard: {op: test, eq: [scveh.h_too_old, {const: false}]}
          then: scveh.h_line19_normal
    note: "For a vehicle placed in service in 2019 the recovery period has ended; the provided inputs do not include prior-year MACRS amounts, so the unrecovered basis shown here is cost less prior section 179 only."
  - id: scveh.line20
    printed: "20"
    label: "Enter the lesser of line 17 or line 19. This is your MACRS depreciation deduction."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [scveh.line17, scveh.line19]
  - id: scveh.bonus
    printed: "(helper)"
    label: "Allowed special depreciation allowance for this vehicle"
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.bonus_allowed
  - id: scveh.macrs
    printed: "(helper)"
    label: "Allowed MACRS depreciation for this vehicle"
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.line20
  - id: scveh.s179_2025
    printed: "(helper)"
    label: "Section 179 deduction for this vehicle for 2025"
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.line10
  - id: scveh.mq_q4
    printed: "(helper)"
    label: "Mid-quarter fourth-quarter MACRS amount for this vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.quarter, {const: "q4"}]}
          then: scveh.h_line19_mq
        - guard: {op: test, ne: [scveh.quarter, {const: "q4"}]}
          then: scveh.h_zero
  - id: scveh.mq_total
    printed: "(helper)"
    label: "Total mid-quarter MACRS amount for this vehicle"
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.line19
  - id: scveh.cost179
    printed: "(helper)"
    label: "Business/investment cost of this vehicle for section 179"
    type: NonNegDollars
    expr:
      op: copy
      from: scveh.bus_cost
  - id: scveh.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: scveh.h_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: scveh.h_bm_c
    printed: "(helper)"
    label: "Business miles expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_business}
  - id: scveh.h_cm_c
    printed: "(helper)"
    label: "Commuting miles expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_commuting}
  - id: scveh.h_om_c
    printed: "(helper)"
    label: "Other miles expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_cent, count: scveh.miles_other}
  - id: scveh.h_nonbusiness_c
    printed: "(helper)"
    label: "Nonbusiness miles expressed in cents"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_cm_c, scveh.h_om_c]}
  - id: scveh.h_total_c
    printed: "(helper)"
    label: "Total miles expressed in cents"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_bm_c, scveh.h_nonbusiness_c]}
  - id: scveh.h_no_miles
    printed: "(helper)"
    label: "No total miles entered"
    type: Bool
    expr: {op: test, eq: [scveh.h_total_c, scveh.h_zero]}
  - id: scveh.h_over_half
    printed: "(helper)"
    label: "Business use is more than 50 percent"
    type: Bool
    expr: {op: test, gt: [scveh.h_bm_c, scveh.h_nonbusiness_c]}
  - id: scveh.h_smr_bad
    printed: "(helper)"
    label: "Standard mileage rate eligibility is not met"
    type: Bool
    expr: {op: test, eq: [scveh.smr_ok, {const: false}]}
  - id: scveh.h_rate
    printed: "(helper)"
    label: "2025 standard mileage rate"
    type: NonNegDollars
    expr: {op: param, ref: sc.mileage_rate}
  - id: scveh.h_smr_amount
    printed: "(helper)"
    label: "Business miles times the standard mileage rate"
    type: NonNegDollars
    expr: {op: multiply_count, amount: scveh.h_rate, count: scveh.miles_business}
  - id: scveh.h_operating_business
    printed: "(helper)"
    label: "Business portion of operating expenses"
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.operating
      part: scveh.h_bm_c
      whole: scveh.h_total_c
      places: 4
  - id: scveh.h_line9_standard
    printed: "(helper)"
    label: "Schedule C line 9 under the standard mileage rate"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_smr_amount, scveh.parking]}
    refuses: [scveh.h_smr_bad]
  - id: scveh.h_line9_actual
    printed: "(helper)"
    label: "Schedule C line 9 under actual expenses"
    type: NonNegDollars
    expr: {op: sum, of: [scveh.h_operating_business, scveh.parking]}
    refuses: [scveh.h_no_miles]
  - id: scveh.h_is_actual_leased
    printed: "(helper)"
    label: "Actual expenses and leased vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.method, {const: "actual"}]}
        - {op: test, eq: [scveh.owned, {const: false}]}
  - id: scveh.h_lease_business
    printed: "(helper)"
    label: "Business portion of lease payments"
    type: NonNegDollars
    expr:
      op: prorate
      amount: scveh.lease
      part: scveh.h_bm_c
      whole: scveh.h_total_c
      places: 4
  - id: scveh.h_is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2025"}]}
  - id: scveh.h_y1
    printed: "(helper)"
    label: "Count one"
    type: Count
    expr: {op: param, ref: sc.year1}
  - id: scveh.h_y2
    printed: "(helper)"
    label: "Count two"
    type: Count
    expr: {op: param, ref: sc.year2}
  - id: scveh.h_y3
    printed: "(helper)"
    label: "Count three"
    type: Count
    expr: {op: param, ref: sc.year3}
  - id: scveh.h_y4
    printed: "(helper)"
    label: "Count four"
    type: Count
    expr: {op: param, ref: sc.year4}
  - id: scveh.h_y5
    printed: "(helper)"
    label: "Count five"
    type: Count
    expr: {op: param, ref: sc.year5}
  - id: scveh.h_y6
    printed: "(helper)"
    label: "Count six"
    type: Count
    expr: {op: param, ref: sc.year6}
  - id: scveh.h_year
    printed: "(helper)"
    label: "Tax year in service, capped at six"
    type: Count
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.placed, {const: "y2025"}]}
          then: scveh.h_y1
        - guard: {op: test, eq: [scveh.placed, {const: "y2024"}]}
          then: scveh.h_y2
        - guard: {op: test, eq: [scveh.placed, {const: "y2023"}]}
          then: scveh.h_y3
        - guard: {op: test, eq: [scveh.placed, {const: "y2022"}]}
          then: scveh.h_y4
        - guard: {op: test, eq: [scveh.placed, {const: "y2021"}]}
          then: scveh.h_y5
        - guard: {op: test, eq: [scveh.placed, {const: "y2020"}]}
          then: scveh.h_y6
        - guard: {op: test, eq: [scveh.placed, {const: "y2019"}]}
          then: scveh.h_y6
  - id: scveh.h_year_key
    printed: "(helper)"
    label: "Tax year in service key for the limit table, capped at fourth or later"
    type: Count
    expr: {op: smaller_of, of: [scveh.h_year, scveh.h_y4]}
  - id: scveh.h_suv_cap
    printed: "(helper)"
    label: "Section 179 limit for SUVs and certain other vehicles"
    type: NonNegDollars
    expr: {op: param, ref: s179.suv_limit}
  - id: scveh.h_s179_bad
    printed: "(helper)"
    label: "Section 179 election exceeds an applicable limit"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [scveh.s179_elect, scveh.bus_cost]}
        - op: test
          all:
            - {op: test, eq: [scveh.suv, {const: true}]}
            - {op: test, gt: [scveh.s179_elect, scveh.h_suv_cap]}
  - id: scveh.h_s179_min
    printed: "(helper)"
    label: "Section 179 election limited by the worksheet line 9 amount"
    type: NonNegDollars
    expr: {op: smaller_of, of: [scveh.s179_elect, scveh.line9w]}
  - id: scveh.h_s179_2025_ok
    printed: "(helper)"
    label: "Section 179 amount allowed before the business-income limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_over_half, {const: true}]}
          then: scveh.h_s179_min
        - guard: {op: test, eq: [scveh.h_over_half, {const: false}]}
          then: scveh.h_zero
  - id: scveh.h_bonus_full
    printed: "(helper)"
    label: "Special depreciation allowance at 100 percent"
    type: NonNegDollars
    expr: {op: copy, from: scveh.line15}
  - id: scveh.h_bonus_forty
    printed: "(helper)"
    label: "Special depreciation allowance at 40 percent"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line15, rate: {param: sc.bonus_rate_40}}
  - id: scveh.h_bonus_fullcase
    printed: "(helper)"
    label: "Special depreciation allowance under the elected choice"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.bonus_choice, {const: "full"}]}
          then: scveh.h_bonus_full
        - guard: {op: test, eq: [scveh.bonus_choice, {const: "forty"}]}
          then: scveh.h_bonus_forty
        - guard: {op: test, eq: [scveh.bonus_choice, {const: "none"}]}
          then: scveh.h_zero
  - id: scveh.h_claims_bonus
    printed: "(helper)"
    label: "Special depreciation allowance applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [scveh.h_is2025, {const: true}]}
        - {op: test, eq: [scveh.h_over_half, {const: true}]}
        - {op: test, ne: [scveh.bonus_choice, {const: "none"}]}
  - id: scveh.h_bonus_2025
    printed: "(helper)"
    label: "Tentative special depreciation allowance for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_claims_bonus, {const: true}]}
          then: scveh.h_bonus_fullcase
        - guard: {op: test, eq: [scveh.h_claims_bonus, {const: false}]}
          then: scveh.h_zero
  - id: scveh.h_rate_hy
    printed: "(helper)"
    label: "MACRS 5-year half-year rate for the tax year in service"
    type: Rate
    expr: {op: keyed_lookup, table: f4562.macrs_5_hy, keys: [scveh.h_year_key]}
  - id: scveh.h_rate_mq
    printed: "(helper)"
    label: "MACRS 5-year mid-quarter rate for the tax year in service and quarter"
    type: Rate
    expr: {op: keyed_lookup, table: f4562.macrs_5_mq, keys: [scveh.h_year_key, scveh.quarter]}
  - id: scveh.h_rate_prior
    printed: "(helper)"
    label: "MACRS 5-year rate for the prior convention and tax year in service"
    type: Rate
    expr: {op: keyed_lookup, table: f4562.macrs_5_prior, keys: [scveh.prior_conv, scveh.h_year_key]}
  - id: scveh.h_line19_hy
    printed: "(helper)"
    label: "MACRS depreciation using the half-year rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_hy}
  - id: scveh.h_line19_mq
    printed: "(helper)"
    label: "MACRS depreciation using the mid-quarter rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_mq}
  - id: scveh.h_line19_prior
    printed: "(helper)"
    label: "MACRS depreciation for a prior-year placed vehicle"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: scveh.line18, rate: scveh.h_rate_prior}
  - id: scveh.h_line19_2025
    printed: "(helper)"
    label: "MACRS depreciation for a 2025 placed vehicle"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.quarter, {const: "q4"}]}
          then: scveh.h_line19_mq
        - guard: {op: test, ne: [scveh.quarter, {const: "q4"}]}
          then: scveh.h_line19_hy
  - id: scveh.h_line19_normal
    printed: "(helper)"
    label: "Tentative MACRS depreciation before the line 20 limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [scveh.h_is2025, {const: true}]}
          then: scveh.h_line19_2025
        - guard: {op: test, eq: [scveh.h_is2025, {const: false}]}
          then: scveh.h_line19_prior
  - id: scveh.h_too_old
    printed: "(helper)"
    label: "Vehicle placed in service in 2019, beyond the 5-year recovery period"
    type: Bool
    expr: {op: test, eq: [scveh.placed, {const: "y2019"}]}
  - id: scveh.h_unrecovered
    printed: "(helper)"
    label: "Unrecovered basis for a vehicle whose recovery period has ended"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: scveh.bus_cost, take: scveh.line14}
```
