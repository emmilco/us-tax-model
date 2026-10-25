# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 9dcec2c9530597d67760b96e15c55ec2a859d99914a5a2be51bd6cfd0acbcaad |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0f1df70975dae8df7b1ffdb285589a51a9f6b67c79822b31fe1d630b33de9de6 |
| printed lines compared | 16 |
| agree / disagree / missing | 1 / 15 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 98 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"input": "asset.listed"}, "then": {"line": "26(h)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: open

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"input": "asset.listed"}, "then": {"line": "25"}}, {"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"line": "14"}}], "op": "choose"}
```

Ruling: open

### asset.s179_2025 — Section 179 elected on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"input": "asset.listed"}, "then": {"line": "26(i)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### asset.mq_q4 — Mid-quarter test basis, fourth quarter
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "asset.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"line": "(c)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"line": "(c)"}, {"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}], "test": "le"}, {"args": [{"input": "asset.listed"}], "test": "not"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"input": "asset.listed"}, {"args": [{"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}, {"line": "(c)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"line": "(c)"}}], "op": "choose"}
```

Ruling: open

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"line": "17"}
```

Second transcription's note: The archived pages do not provide an accumulated prior-year depreciation figure for a single asset; this helper is the line 17 current-year amount for prior-year non-listed property.

Ruling: open

### (d) — Recovery period under GDS for the asset class
Status: **DISAGREE**

Project:

```json
{"keys": [{"line": "(a)"}], "op": "keyed_lookup", "table": "class_lives"}
```

Second:

```json
{"keys": [{"line": "(a)"}], "op": "keyed_lookup", "table": "asset_class_period"}
```

Second transcription's note: The archived pages identify the recovery period through Pub. 946 Appendix B; the complete class-to-period table is not reproduced here, so the pinned table asset_class_period is used.

Ruling: open

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special 
Status: **DISAGREE**

Project:

```json
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}
```

Second transcription's note: Business basis is cost times business-use percentage, rounded to the cent.

Ruling: open

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"input": "asset.listed"}, {"args": [{"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}, {"line": "(c)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"line": "(c)"}, {"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}], "test": "le"}, {"args": [{"input": "asset.listed"}], "test": "not"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"input": "asset.listed"}, {"args": [{"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}, {"line": "(c)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"line": "(c)"}, {"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}], "test": "le"}, {"args": [{"input": "asset.listed"}], "test": "not"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"amount": {"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}], "op": "keyed_lookup", "table": "macrs_rate"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}], "op": "keyed_lookup", "table": "macrs_rate"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_life"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}], "op": "keyed_lookup", "table": "macrs_rate"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_life"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "asset.listed"}, {"args": [{"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}, {"line": "(c)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"amount": {"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}], "op": "keyed_lookup", "table": "macrs_rate"}}}, {"guard": {"args": [{"args": [{"args": [{"input": "asset.listed"}, {"args": [{"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}, {"line": "(c)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"input": "asset.after_jan19"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}], "op": "keyed_lookup", "table": "macrs_rate"}}}, {"guard": {"args": [{"args": [{"args": [{"input": "asset.listed"}, {"args": [{"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}, {"line": "(c)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_life"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}], "op": "keyed_lookup", "table": "macrs_rate"}}}, {"guard": {"args": [{"args": [{"input": "asset.listed"}, {"args": [{"line": "(c)"}, {"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "asset.listed"}, {"args": [{"amount": {"input": "asset.cost"}, "op": "multiply_rate", "rate": {"param": "sc.meals_rate"}}, {"line": "(c)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_life"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_count"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Only line 26 (listed property used more than 50% in qualified business use) is computed; line 27 for 50% or less is outside this slice.

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.listed_low, asset.screen | asset.screen |
| asset.bonus_2025 | asset.bonus_mixed, asset.screen | asset.screen |
| asset.s179_2025 | asset.screen | asset.screen |
| asset.mq_q4 | asset.screen | asset.screen |
| asset.mq_total | asset.screen | asset.screen |
| asset.cost179 | asset.screen | asset.screen |
| asset.dep_prior | asset.screen | asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.screen | asset.screen |
| 14 | asset.bonus_mixed, asset.screen | asset.screen |
| 25 | asset.bonus_mixed, asset.screen | asset.screen |
| 26(i) | asset.screen | asset.screen |
| 19(c) | asset.screen | asset.screen |
| 19(g) | asset.screen | asset.screen |
| 17 | asset.screen | asset.screen |
| 26(h) | asset.listed_low, asset.screen | asset.screen |

## Raw second transcription

```yaml
lines:
  - id: asset.period
    printed: "(d)"
    label: "Recovery period"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: asset_class_period, keys: [asset.class]}
    refuses: [asset.screen]
    note: "The archived pages identify the recovery period through Pub. 946 Appendix B; the complete class-to-period table is not reproduced here, so the pinned table asset_class_period is used."
  - id: asset.basis
    printed: "(c)"
    label: "Cost or other basis (business/investment use only)"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.pct_c, part: asset.cent, whole: asset.hundred, places: 2}
    refuses: [asset.screen]
    note: "Business basis is cost times business-use percentage, rounded to the cent."
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.not_listed_2025, then: asset.bonus_fullcase}, {guard: {op: test, eq: [asset.not_listed_2025, {const: false}]}, then: asset.zero}]}
    refuses: [asset.screen, asset.bonus_mixed]
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for listed property"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.listed_over_2025, then: asset.bonus_fullcase}, {guard: {op: test, eq: [asset.listed_over_2025, {const: false}]}, then: asset.zero}]}
    refuses: [asset.screen, asset.bonus_mixed]
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost for listed property"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.listed_over_2025, then: asset.s179}, {guard: {op: test, eq: [asset.listed_over_2025, {const: false}]}, then: asset.zero}]}
    refuses: [asset.screen]
  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.on_19, then: asset.ub}, {guard: {op: test, eq: [asset.on_19, {const: false}]}, then: asset.zero}]}
    refuses: [asset.screen]
  - id: asset.macrs2025
    printed: "19(g)"
    label: "MACRS depreciation for 2025 property"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, all: [asset.on_19, asset.mq_applies]}, then: asset.macrs_mq}, {guard: {op: test, all: [asset.on_19, {op: test, eq: [asset.mq_applies, {const: false}]}]}, then: asset.macrs_hy}, {guard: {op: test, eq: [asset.on_19, {const: false}]}, then: asset.zero}]}
    refuses: [asset.screen]
  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS depreciation for prior-year property"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.on_17_live, then: asset.macrs_prior_live}, {guard: asset.on_17_done, then: asset.zero}, {guard: asset.not_on_17, then: asset.zero}]}
    refuses: [asset.screen]
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation for listed property"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.not_listed, then: asset.zero}, {guard: asset.listed_low, then: asset.zero}, {guard: asset.listed_over_2025_mq, then: asset.dep_listed_2025_mq}, {guard: asset.listed_over_2025_hy, then: asset.dep_listed_2025_hy}, {guard: asset.prior_done, then: asset.zero}, {guard: asset.prior_live, then: asset.dep_listed_prior_live}]}
    refuses: [asset.screen, asset.listed_low]
    note: "Only line 26 (listed property used more than 50% in qualified business use) is computed; line 27 for 50% or less is outside this slice."
  - id: asset.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: asset.cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: asset.hundred
    printed: "(helper)"
    label: "One hundred cents"
    type: NonNegDollars
    expr: {op: param, ref: sc.hundred_cents}
  - id: asset.pct_c
    printed: "(helper)"
    label: "Cost times business-use percentage"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.cost, count: asset.pct}
  - id: asset.pct_bad
    printed: "(helper)"
    label: "Business-use percentage outside 1 to 100"
    type: Bool
    expr: {op: test, any: [{op: test, lt: [asset.pct, {const: 1}]}, {op: test, gt: [asset.pct, {const: 100}]}]}
  - id: asset.half
    printed: "(helper)"
    label: "Half of cost"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.cost, rate: {param: sc.meals_rate}}
  - id: asset.over_half
    printed: "(helper)"
    label: "Business use more than 50%"
    type: Bool
    expr: {op: test, gt: [asset.basis, asset.half]}
  - id: asset.listed_low
    printed: "(helper)"
    label: "Listed property used 50% or less"
    type: Bool
    expr: {op: test, all: [asset.listed, {op: test, eq: [asset.over_half, {const: false}]}]}
  - id: asset.not_listed
    printed: "(helper)"
    label: "Not listed property"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: false}]}
  - id: asset.is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.is_q4
    printed: "(helper)"
    label: "Placed in service in the fourth quarter"
    type: Bool
    expr: {op: test, eq: [asset.quarter, {const: "q4"}]}
  - id: asset.on_19
    printed: "(helper)"
    label: "Line 19 applies"
    type: Bool
    expr: {op: test, all: [asset.is2025, asset.not_listed]}
  - id: asset.on_17
    printed: "(helper)"
    label: "Line 17 applies"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.is2025, {const: false}]}, asset.not_listed]}
  - id: asset.listed_over
    printed: "(helper)"
    label: "Listed property used more than 50%"
    type: Bool
    expr: {op: test, all: [asset.listed, asset.over_half]}
  - id: asset.on_26_2025
    printed: "(helper)"
    label: "Line 26 applies for 2025 listed property"
    type: Bool
    expr: {op: test, all: [asset.is2025, asset.listed_over]}
  - id: asset.year
    printed: "(helper)"
    label: "Current year in the recovery period"
    type: Count
    expr: {op: keyed_lookup, table: placed_year_count, keys: [asset.placed]}
  - id: asset.last
    printed: "(helper)"
    label: "Recovery period in years"
    type: Count
    expr: {op: keyed_lookup, table: macrs_life, keys: [asset.period]}
  - id: asset.done
    printed: "(helper)"
    label: "Recovery period has ended"
    type: Bool
    expr: {op: test, gt: [asset.year, asset.last]}
  - id: asset.qconv
    printed: "(helper)"
    label: "Mid-quarter convention from quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}
  - id: asset.s179_bad
    printed: "(helper)"
    label: "Section 179 election exceeds business basis"
    type: Bool
    expr: {op: test, gt: [asset.s179, asset.basis]}
  - id: asset.after179
    printed: "(helper)"
    label: "Basis after section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.s179}
  - id: asset.bonus_mixed
    printed: "(helper)"
    label: "Mixed special allowance choices in the recovery-period class"
    type: Bool
    expr: {op: test, all: [{op: test, ne: [asset.bonus_choice, {const: "none"}]}, {op: test, eq: [asset.bonus_same, {const: false}]}]}
  - id: asset.rate40
    printed: "(helper)"
    label: "40% special allowance rate"
    type: Rate
    expr: {op: param, ref: sc.bonus_rate_40}
  - id: asset.bonus_full
    printed: "(helper)"
    label: "100% special allowance"
    type: NonNegDollars
    expr: {op: copy, from: asset.after179}
  - id: asset.bonus_forty
    printed: "(helper)"
    label: "40% special allowance"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.after179, rate: asset.rate40}
  - id: asset.bonus_fullcase
    printed: "(helper)"
    label: "Special allowance amount"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [asset.bonus_choice, {const: "none"}]}, then: asset.zero}, {guard: {op: test, all: [asset.after_jan19, {op: test, eq: [asset.bonus_choice, {const: "full"}]}]}, then: asset.bonus_full}, {guard: {op: test, all: [asset.after_jan19, {op: test, eq: [asset.bonus_choice, {const: "forty"}]}]}, then: asset.bonus_forty}, {guard: {op: test, all: [{op: test, eq: [asset.after_jan19, {const: false}]}, {op: test, ne: [asset.bonus_choice, {const: "none"}]}]}, then: asset.bonus_forty}]}
    note: "For property acquired before January 20, 2025, the archived text limits the allowance to 40% (or 60% for long-production/aircraft, which is outside this slice); this reads a 'full' choice before that date as the 40% allowance."
  - id: asset.ub
    printed: "(helper)"
    label: "Unrecovered basis for regular depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.after179, take: asset.bonus_fullcase}
  - id: asset.hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: asset.rate_hy
    printed: "(helper)"
    label: "Half-year MACRS rate"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_rate, keys: [asset.period, asset.hy, asset.year]}
  - id: asset.rate_mq
    printed: "(helper)"
    label: "Mid-quarter MACRS rate"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_rate, keys: [asset.period, asset.qconv, asset.year]}
  - id: asset.macrs_hy
    printed: "(helper)"
    label: "MACRS depreciation using half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.rate_hy}
  - id: asset.macrs_mq
    printed: "(helper)"
    label: "MACRS depreciation using mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.rate_mq}
  - id: asset.mqbase
    printed: "(helper)"
    label: "Basis for mid-quarter test"
    type: NonNegDollars
    expr: {op: copy, from: asset.after179}
  - id: asset.mq_q4_2025
    printed: "(helper)"
    label: "Fourth-quarter basis placed in service in 2025"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, all: [asset.is2025, asset.is_q4]}, then: asset.mqbase}, {guard: {op: test, not: {op: test, all: [asset.is2025, asset.is_q4]}}, then: asset.zero}]}
  - id: asset.mq_total_2025
    printed: "(helper)"
    label: "Total basis placed in service in 2025"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.is2025, then: asset.mqbase}, {guard: {op: test, eq: [asset.is2025, {const: false}]}, then: asset.zero}]}
  - id: asset.mq_q4_all
    printed: "(helper)"
    label: "All fourth-quarter bases in this business"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_q4}
  - id: asset.mq_total_all
    printed: "(helper)"
    label: "All 2025 bases in this business"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_total}
  - id: asset.mq_threshold
    printed: "(helper)"
    label: "40% of all 2025 bases"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.mq_total_all, rate: {param: sc.bonus_rate_40}}
  - id: asset.mq_applies
    printed: "(helper)"
    label: "Mid-quarter convention applies"
    type: Bool
    expr: {op: test, gt: [asset.mq_q4_all, asset.mq_threshold]}
  - id: asset.ub_prior_a
    printed: "(helper)"
    label: "Prior-year basis after prior section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.prior_179}
  - id: asset.ub_prior
    printed: "(helper)"
    label: "Prior-year basis after prior section 179 and bonus"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.ub_prior_a, take: asset.prior_bonus}
  - id: asset.rate_prior
    printed: "(helper)"
    label: "Prior-year property MACRS rate"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_rate, keys: [asset.period, asset.prior_conv, asset.year]}
  - id: asset.macrs_prior_live
    printed: "(helper)"
    label: "Live prior-year MACRS depreciation"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.ub_prior, rate: asset.rate_prior}
  - id: asset.on_17_done
    printed: "(helper)"
    label: "Prior-year property and recovery period ended"
    type: Bool
    expr: {op: test, all: [asset.on_17, asset.done]}
  - id: asset.on_17_live
    printed: "(helper)"
    label: "Prior-year property and recovery period not ended"
    type: Bool
    expr: {op: test, all: [asset.on_17, {op: test, eq: [asset.done, {const: false}]}]}
  - id: asset.not_on_17
    printed: "(helper)"
    label: "Line 17 does not apply"
    type: Bool
    expr: {op: test, eq: [asset.on_17, {const: false}]}
  - id: asset.dep_listed_2025_mq
    printed: "(helper)"
    label: "Listed property 2025 depreciation, mid-quarter"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.ub, rate: asset.rate_mq}
  - id: asset.dep_listed_2025_hy
    printed: "(helper)"
    label: "Listed property 2025 depreciation, half-year"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.ub, rate: asset.rate_hy}
  - id: asset.dep_listed_prior_live
    printed: "(helper)"
    label: "Listed property prior-year depreciation"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.ub_prior, rate: asset.rate_prior}
  - id: asset.listed_over_2025
    printed: "(helper)"
    label: "Listed property used more than 50% and placed in 2025"
    type: Bool
    expr: {op: test, all: [asset.listed_over, asset.is2025]}
  - id: asset.listed_over_prior
    printed: "(helper)"
    label: "Listed property used more than 50% and placed before 2025"
    type: Bool
    expr: {op: test, all: [asset.listed_over, {op: test, eq: [asset.is2025, {const: false}]}]}
  - id: asset.listed_over_2025_mq
    printed: "(helper)"
    label: "Listed property 2025 and mid-quarter"
    type: Bool
    expr: {op: test, all: [asset.listed_over_2025, asset.mq_applies]}
  - id: asset.listed_over_2025_hy
    printed: "(helper)"
    label: "Listed property 2025 and half-year"
    type: Bool
    expr: {op: test, all: [asset.listed_over_2025, {op: test, eq: [asset.mq_applies, {const: false}]}]}
  - id: asset.prior_done
    printed: "(helper)"
    label: "Listed prior-year property with recovery period ended"
    type: Bool
    expr: {op: test, all: [asset.listed_over_prior, asset.done]}
  - id: asset.prior_live
    printed: "(helper)"
    label: "Listed prior-year property with recovery period not ended"
    type: Bool
    expr: {op: test, all: [asset.listed_over_prior, {op: test, eq: [asset.done, {const: false}]}]}
  - id: asset.not_listed_2025
    printed: "(helper)"
    label: "Not listed property placed in 2025"
    type: Bool
    expr: {op: test, all: [asset.not_listed, asset.is2025]}
  - id: asset.not_listed_prior
    printed: "(helper)"
    label: "Not listed property placed before 2025"
    type: Bool
    expr: {op: test, all: [asset.not_listed, {op: test, eq: [asset.is2025, {const: false}]}]}
  - id: asset.eligible179_2025
    printed: "(helper)"
    label: "Section 179 eligible cost for 2025"
    type: Bool
    expr: {op: test, any: [asset.listed_over_2025, asset.not_listed_2025]}
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Current-year depreciation for this property"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.listed, then: asset.dep_listed}, {guard: asset.not_listed_2025, then: asset.macrs2025}, {guard: asset.not_listed_prior, then: asset.macrs_prior}]}
    refuses: [asset.screen]
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for 2025"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.listed, then: asset.f25}, {guard: asset.not_listed, then: asset.bonus}]}
    refuses: [asset.screen, asset.bonus_mixed]
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 amount for 2025"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.listed, then: asset.f26i}, {guard: asset.not_listed_2025, then: asset.s179}, {guard: asset.not_listed_prior, then: asset.zero}]}
    refuses: [asset.screen]
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Fourth-quarter basis for mid-quarter test"
    type: NonNegDollars
    expr: {op: copy, from: asset.mq_q4_2025}
  - id: asset.mq_total
    printed: "(helper)"
    label: "Total basis for mid-quarter test"
    type: NonNegDollars
    expr: {op: copy, from: asset.mq_total_2025}
  - id: asset.cost179
    printed: "(helper)"
    label: "Section 179 eligible cost"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: asset.eligible179_2025, then: asset.basis}, {guard: {op: test, eq: [asset.eligible179_2025, {const: false}]}, then: asset.zero}]}
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Depreciation for prior-year property"
    type: NonNegDollars
    expr: {op: copy, from: asset.macrs_prior}
    note: "The archived pages do not provide an accumulated prior-year depreciation figure for a single asset; this helper is the line 17 current-year amount for prior-year non-listed property."
```
