# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | bf49cc71a35038787fbf85f0fd1283d5743f25be9dcdb4c50adf0b6718790d5d |
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
{"line": "19(g)"}
```

Ruling: representation; project retained. MACRS on 2025 property, half-year or mid-quarter by the same test, zero for earlier property on both sides; the second writes the 2025 and mid-quarter tests as one guard.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "14"}
```

Ruling: representation; project retained. The special allowance on 2025 property: 100% (or 40% before January 20, 2025) or 40% by election, or none, of column (c) less the section 179 election, zero for earlier property, on both sides; the guards are merged differently.

### asset.s179_2025 — Section 179 elected on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Line 6 excludes listed property; the section 179 cost of listed property goes in line 26 column (i).

Ruling: equivalent within the totals; project retained. The second excludes listed property here; the project keeps the 2025 election for every 2025 asset and divides it at the sums: line 6 takes property that is not listed (sc.f6, where listed is false) and line 29, through line 26 column (i), listed property (sc.f29), as i4562 p. 5, Line 6 says ('Do not include any listed property on line 6').

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

Second transcription's note: Pub. 946: the depreciable basis for the mid-quarter test reflects section 179 and personal use but not the special allowance.

Ruling: equivalent; project retained. Fourth-quarter 2025 property's basis after the section 179 election, zero otherwise, on both sides (Pub. 946 p. 41); written as nested against merged guards.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Line 2 counts the total cost of eligible section 179 property, not just the amount elected, and includes listed property. Eligible property is used more than 50% in the business; its business cost is column (c) before section 179.

Ruling: equivalent; project retained. Column (c) for 2025 property used more than 50% in business and zero otherwise on both sides; the guards are merged differently.

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

Ruling: representation; project retained. MACRS on earlier property within its recovery period, zero for 2025 property and after the last recovery year, on both sides. The second names its own tables (recovery_year_in_2025, macrs_last_recovery_year, and p946_appendix_b_gds_recovery_period for the class lookup), which are the project's recovery_year, macrs_last_year and class_lives.

### (d) — Recovery period under GDS for the asset class
Status: **DISAGREE**

Project:

```json
{"keys": [{"line": "(a)"}], "op": "keyed_lookup", "table": "class_lives"}
```

Second:

```json
{"keys": [{"line": "(a)"}], "op": "keyed_lookup", "table": "pub946_appendix_b_gds_period"}
```

Second transcription's note: Pub. 946 Appendix B: the Table B-2 class is used when the property is specifically included under the activity, otherwise Table B-1. The asset.class input already reflects that choice. Classes outside the tool's 3/5/7/10/15/20-year GDS classes map to "outside" and are refused on the lines that depend on this one.

Ruling: representation; project retained. The same lookup of the GDS recovery period by asset class in Pub. 946 Appendix B (p. 98); the second names the table p946_appendix_b_gds_recovery_period where the project's is class_lives, checked against a second transcription of Tables B-1 and B-2 (reviews/2025/tables/class_lives.json).

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special 
Status: **DISAGREE**

Project:

```json
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}
```

Second transcription's note: i4562 line 19 column (c) says to multiply the cost or other basis by the percentage of business/investment use. A whole-number percentage over 100 is exact to two decimal places. Basis reductions other than section 179 and the special allowance (credits and so on) are among the screened situations.

Ruling: equivalent; project retained. asset.pct is a whole number from 1 to 100, so the ratio pct/100 is exact at two places and the six places the project uses give the same value.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent on every value the form reports; project retained (owner, T-030). The second writes the condition under which Form 4562 reports this asset on the line into the expression and enters zero otherwise; the project figures the asset's amount and shows the line on the values sheet only under the same condition, shown_when asset.on_19 (2025 property that is not listed), leaving it out otherwise (the owner's choice). Where the line is shown the two expressions are the same; the transcription comparison sees expressions only, not shown_when.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent on every value the form reports; project retained (owner, T-030). The second writes the condition under which Form 4562 reports this asset on the line into the expression and enters zero otherwise; the project figures the asset's amount and shows the line on the values sheet only under the same condition, shown_when asset.on_26_2025 (listed property placed in service in 2025), leaving it out otherwise (the owner's choice). Where the line is shown the two expressions are the same; the transcription comparison sees expressions only, not shown_when.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent on every value the form reports; project retained (owner, T-030). The second writes the condition under which Form 4562 reports this asset on the line into the expression and enters zero otherwise; the project figures the asset's amount and shows the line on the values sheet only under the same condition, shown_when asset.on_26_2025 (listed property placed in service in 2025), leaving it out otherwise (the owner's choice). Where the line is shown the two expressions are the same; the transcription comparison sees expressions only, not shown_when.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent on every value the form reports; project retained (owner, T-030). The second writes the condition under which Form 4562 reports this asset on the line into the expression and enters zero otherwise; the project figures the asset's amount and shows the line on the values sheet only under the same condition, shown_when asset.on_19 (2025 property that is not listed), leaving it out otherwise (the owner's choice). Where the line is shown the two expressions are the same; the transcription comparison sees expressions only, not shown_when.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1}], "op": "keyed_lookup", "table": "pub946_appendix_a_gds_rates"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "mq_convention_by_quarter"}, {"const": 1}], "op": "keyed_lookup", "table": "pub946_appendix_a_gds_rates"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent on every value the form reports; project retained (owner, T-030). The second writes the condition under which Form 4562 reports this asset on the line into the expression and enters zero otherwise; the project figures the asset's amount and shows the line on the values sheet only under the same condition, shown_when asset.on_19 (2025 property that is not listed), leaving it out otherwise (the owner's choice). Where the line is shown the two expressions are the same; the transcription comparison sees expressions only, not shown_when.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year_in_2025"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_recovery_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year_in_2025"}], "op": "keyed_lookup", "table": "pub946_appendix_a_gds_rates"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_recovery_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year_in_2025"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: equivalent on every value the form reports; project retained (owner, T-030). The second writes the condition under which Form 4562 reports this asset on the line into the expression and enters zero otherwise; the project figures the asset's amount and shows the line on the values sheet only under the same condition, shown_when asset.on_17 (property placed in service before 2025 that is not listed), leaving it out otherwise (the owner's choice). Where the line is shown the two expressions are the same; the transcription comparison sees expressions only, not shown_when.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1}], "op": "keyed_lookup", "table": "pub946_appendix_a_gds_rates"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "mq_convention_by_quarter"}, {"const": 1}], "op": "keyed_lookup", "table": "pub946_appendix_a_gds_rates"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year_in_2025"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_recovery_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year_in_2025"}], "op": "keyed_lookup", "table": "pub946_appendix_a_gds_rates"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_recovery_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year_in_2025"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: For listed property used more than 50% in a qualified business use and placed in service after 1986, column (h) is figured by following the line 19 column (g) instructions.

Ruling: project retained (owner, T-030). The second reports column (h) only for listed property placed in service in 2025; the project shows it for all listed property (shown_when asset.listed), as Form 4562 is filed for 'Depreciation on any vehicle or other listed property (regardless of when it was placed in service)' (i4562 p. 2, Who Must File) and Part V carries it. For listed property placed in service in 2025 the two agree.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.bonus_2025 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.s179_2025 | asset.h_s179_bad | asset.h_s179_bad |
| asset.mq_q4 | asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.mq_total | asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.cost179 | asset.h_pct_bad, asset.screen | asset.h_pct_bad, asset.screen |
| asset.dep_prior | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.h_pct_bad, asset.screen | asset.h_pct_bad, asset.screen |
| 14 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 25 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 26(i) | asset.h_listed_low, asset.h_s179_bad | asset.h_listed_low, asset.h_s179_bad |
| 19(c) | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 19(g) | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 17 | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen |
| 26(h) | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |

## Raw second transcription

```yaml
```yaml
lines:
  - id: asset.line(d)
    printed: "(d)"
    label: "Recovery period under GDS for the asset class"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: pub946_appendix_b_gds_period, keys: [asset.class]}
    refuses: [asset.screen]
    note: "Pub. 946 Appendix B: the Table B-2 class is used when the property is specifically included under the activity, otherwise Table B-1. The asset.class input already reflects that choice. Classes outside the tool's 3/5/7/10/15/20-year GDS classes map to \"outside\" and are refused on the lines that depend on this one."

  - id: asset.h_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}

  - id: asset.h_hundred
    printed: "(helper)"
    label: "One hundred cents (100%)"
    type: NonNegDollars
    expr: {op: param, ref: sc.hundred_cents}

  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: asset.h_pct_c
    printed: "(helper)"
    label: "The business/investment use percentage, as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}

  - id: asset.h_pct_bad
    printed: "(helper)"
    label: "The business use percentage is more than 100"
    type: Bool
    expr: {op: test, gt: [asset.h_pct_c, asset.h_hundred]}

  - id: asset.h_over_half
    printed: "(helper)"
    label: "Used more than 50% in the business (predominantly)"
    type: Bool
    expr: {op: test, gt: [asset.h_pct_c, {param: sc.fifty_cents}]}

  - id: asset.h_listed_low
    printed: "(helper)"
    label: "Listed property used 50% or less in a qualified business use (line 27)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, not: {op: test, eq: [asset.h_over_half, {const: true}]}}]}
    note: "The tool does not compute line 27 (ADS straight line), so this case is refused. The qualified business use percentage is taken to be the same as the business/investment use percentage."

  - id: asset.h_outside
    printed: "(helper)"
    label: "The asset class is outside this tool"
    type: Bool
    expr: {op: test, eq: [asset.line(d), {const: "outside"}]}

  - id: asset.h_is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}

  - id: asset.h_on_19
    printed: "(helper)"
    label: "Reported on lines 6, 14 and 19 (placed in service in 2025, not listed property)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: asset.h_on_17
    printed: "(helper)"
    label: "Reported on line 17 (placed in service before 2025, not listed property)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: false}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: asset.h_on_26_2025
    printed: "(helper)"
    label: "Reported on lines 25 and 26 column (i) (listed property placed in service in 2025)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}]}

  - id: asset.line(c)
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only), before section 179 and the special allowance"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_c, whole: asset.h_hundred, places: 2}
    refuses: [asset.screen, asset.h_pct_bad]
    note: "i4562 line 19 column (c) says to multiply the cost or other basis by the percentage of business/investment use. A whole-number percentage over 100 is exact to two decimal places. Basis reductions other than section 179 and the special allowance (credits and so on) are among the screened situations."

  - id: asset.h_s179_bad
    printed: "(helper)"
    label: "The section 179 election is more than the business cost, or is made for property not placed in service in 2025 or not used more than 50% in the business"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [asset.s179, asset.line(c)]}
        - {op: test, all: [{op: test, gt: [asset.s179, {const: 0}]}, {op: test, eq: [asset.h_is2025, {const: false}]}]}
        - {op: test, all: [{op: test, gt: [asset.s179, {const: 0}]}, {op: test, eq: [asset.h_over_half, {const: false}]}]}

  - id: asset.h_after179
    printed: "(helper)"
    label: "Depreciable basis: business basis less the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.line(c), take: asset.s179}
    refuses: [asset.h_s179_bad]

  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "The special allowance choice is not the same for all property of this class placed in service in 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.bonus_same, {const: false}]}]}

  - id: asset.h_bonus_full
    printed: "(helper)"
    label: "100% special depreciation allowance"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_after179}

  - id: asset.h_bonus_forty
    printed: "(helper)"
    label: "40% special depreciation allowance"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after179, rate: {param: sc.bonus_rate_40}}

  - id: asset.h_bonus_fullcase
    printed: "(helper)"
    label: "The allowance when claimed: 100% if acquired after January 19, 2025; otherwise limited to 40%"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.after_jan19, {const: true}]}, then: asset.h_bonus_full}
        - {guard: {op: test, eq: [asset.after_jan19, {const: false}]}, then: asset.h_bonus_forty}

  - id: asset.h_bonus_raw
    printed: "(helper)"
    label: "Special depreciation allowance by the choice made for the class"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.bonus_choice, {const: "full"}]}, then: asset.h_bonus_fullcase}
        - {guard: {op: test, eq: [asset.bonus_choice, {const: "forty"}]}, then: asset.h_bonus_forty}
        - {guard: {op: test, eq: [asset.bonus_choice, {const: "none"}]}, then: asset.h_zero}
    note: "Property acquired before January 20, 2025 gets 40% whether \"full\" or \"forty\" is chosen. The 60% rate for long production period property and certain aircraft is not encoded; that property is among the screened situations."

  - id: asset.h_bonus
    printed: "(helper)"
    label: "Special depreciation allowance for this property (first year only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_bonus_raw}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
    refuses: [asset.h_outside, asset.h_bonus_mixed, asset.h_listed_low]

  - id: asset.line14
    printed: "14"
    label: "Special depreciation allowance for this property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_on_19, {const: true}]}, then: asset.h_bonus}
        - {guard: {op: test, eq: [asset.h_on_19, {const: false}]}, then: asset.h_zero}

  - id: asset.line25
    printed: "25"
    label: "Special depreciation allowance for this listed property (line 25)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_on_26_2025, {const: true}]}, then: asset.h_bonus}
        - {guard: {op: test, eq: [asset.h_on_26_2025, {const: false}]}, then: asset.h_zero}
    refuses: [asset.h_listed_low]

  - id: asset.line26(i)
    printed: "26(i)"
    label: "Elected section 179 cost of this listed property (column (i))"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_on_26_2025, {const: true}]}, then: asset.s179}
        - {guard: {op: test, eq: [asset.h_on_26_2025, {const: false}]}, then: asset.h_zero}
    refuses: [asset.h_s179_bad, asset.h_listed_low]

  - id: asset.h_ub
    printed: "(helper)"
    label: "Basis for MACRS depreciation (after section 179 and the special allowance)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after179, take: asset.h_bonus}

  - id: asset.line19(c)
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only), column (c), after the section 179 deduction and the special allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_on_19, {const: true}]}, then: asset.h_ub}
        - {guard: {op: test, eq: [asset.h_on_19, {const: false}]}, then: asset.h_zero}
    refuses: [asset.h_outside]

  - id: asset.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}

  - id: asset.h_year1
    printed: "(helper)"
    label: "Year 1 of the recovery period"
    type: Count
    expr: {op: param, ref: sc.year1}

  - id: asset.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: mq_convention_by_quarter, keys: [asset.quarter]}

  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "MACRS rate, half-year convention, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: pub946_appendix_a_gds_rates, keys: [asset.line(d), asset.h_hy, asset.h_year1]}

  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "MACRS rate, mid-quarter convention for the quarter placed in service, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: pub946_appendix_a_gds_rates, keys: [asset.line(d), asset.h_qconv, asset.h_year1]}

  - id: asset.h_macrs_hy
    printed: "(helper)"
    label: "MACRS depreciation, half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_ub, rate: asset.h_rate_hy}

  - id: asset.h_macrs_mq
    printed: "(helper)"
    label: "MACRS depreciation, mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_ub, rate: asset.h_rate_mq}

  - id: asset.h_macrs2025
    printed: "(helper)"
    label: "MACRS depreciation for 2025 property (column (c) times the applicable table rate)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [mq.applies, {const: true}]}, then: asset.h_macrs_mq}
        - {guard: {op: test, eq: [mq.applies, {const: false}]}, then: asset.h_macrs_hy}
    refuses: [asset.h_outside, asset.h_listed_low]
    note: "Whether the mid-quarter convention applies is decided for all MACRS property placed in service in 2025 together (mq.applies), not for each item."

  - id: asset.line19(g)
    printed: "19(g)"
    label: "MACRS depreciation for 2025 property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_on_19, {const: true}]}, then: asset.h_macrs2025}
        - {guard: {op: test, eq: [asset.h_on_19, {const: false}]}, then: asset.h_zero}

  - id: asset.h_ub_prior_a
    printed: "(helper)"
    label: "Business basis less the section 179 deduction elected in the year placed in service"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.line(c), take: asset.prior_179}

  - id: asset.h_ub_prior
    printed: "(helper)"
    label: "Unadjusted basis (less section 179 and the special depreciation allowance taken)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_ub_prior_a, take: asset.prior_bonus}

  - id: asset.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025 (2025 less the year placed in service, plus 1)"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year_in_2025, keys: [asset.placed]}

  - id: asset.h_last
    printed: "(helper)"
    label: "Last year of recovery for the recovery period (recovery period plus 1 under HY/MQ)"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_recovery_year, keys: [asset.line(d)]}

  - id: asset.h_done
    printed: "(helper)"
    label: "The recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [asset.h_year, asset.h_last]}

  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "MACRS rate for the 2025 year of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: pub946_appendix_a_gds_rates, keys: [asset.line(d), asset.prior_conv, asset.h_year]}

  - id: asset.h_macrs_prior_live
    printed: "(helper)"
    label: "MACRS depreciation for 2025 (unadjusted basis times the table rate)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_ub_prior, rate: asset.h_rate_prior}

  - id: asset.h_macrs_prior
    printed: "(helper)"
    label: "MACRS deduction for 2025 on property placed in service before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_done, {const: true}]}, then: asset.h_zero}
        - {guard: {op: test, eq: [asset.h_done, {const: false}]}, then: asset.h_macrs_prior_live}
    refuses: [asset.h_outside, asset.h_listed_low]
    note: "Pub. 946 says table rates apply to the unadjusted basis every year. The business-use percentage is assumed to be the same as in the year placed in service."

  - id: asset.line17
    printed: "17"
    label: "MACRS deduction for 2025 on property placed in service before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_on_17, {const: true}]}, then: asset.h_macrs_prior}
        - {guard: {op: test, eq: [asset.h_on_17, {const: false}]}, then: asset.h_zero}

  - id: asset.line26(h)
    printed: "26(h)"
    label: "Depreciation of this listed property (column (h))"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.h_is2025, {const: true}]}]}, then: asset.h_macrs2025}
        - {guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.h_is2025, {const: false}]}]}, then: asset.h_macrs_prior}
        - {guard: {op: test, eq: [asset.listed, {const: false}]}, then: asset.h_zero}
    refuses: [asset.h_listed_low]
    note: "For listed property used more than 50% in a qualified business use and placed in service after 1986, column (h) is figured by following the line 19 column (g) instructions."

  - id: asset.dep_2025
    printed: "(helper)"
    label: "MACRS on 2025 property"
    type: NonNegDollars
    expr: {op: copy, from: asset.line19(g)}

  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special allowance on 2025 property"
    type: NonNegDollars
    expr: {op: copy, from: asset.line14}

  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 elected on 2025 property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_on_19, {const: true}]}, then: asset.s179}
        - {guard: {op: test, eq: [asset.h_on_19, {const: false}]}, then: asset.h_zero}
    refuses: [asset.h_s179_bad]
    note: "Line 6 excludes listed property; the section 179 cost of listed property goes in line 26 column (i)."

  - id: asset.mq_q4
    printed: "(helper)"
    label: "Mid-quarter test basis, fourth quarter"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.quarter, {const: "q4"}]}]}, then: asset.h_after179}
        - {guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.quarter, {const: "q4"}]}]}}, then: asset.h_zero}
    note: "Pub. 946: the depreciable basis for the mid-quarter test reflects section 179 and personal use but not the special allowance."

  - id: asset.mq_total
    printed: "(helper)"
    label: "Mid-quarter test basis, all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_after179}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}

  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.h_over_half, {const: true}]}]}, then: asset.line(c)}
        - {guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.h_over_half, {const: true}]}]}}, then: asset.h_zero}
    note: "Line 2 counts the total cost of eligible section 179 property, not just the amount elected, and includes listed property. Eligible property is used more than 50% in the business; its business cost is column (c) before section 179."

  - id: asset.dep_prior
    printed: "(helper)"
    label: "MACRS on property placed in service before 2025"
    type: NonNegDollars
    expr: {op: copy, from: asset.line17}
```
```
