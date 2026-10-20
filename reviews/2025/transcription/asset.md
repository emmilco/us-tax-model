# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 36189ae083f60aa9bff091240ec34f27785cab074cd52c3f81486ac50d7fd24d |
| printed lines compared | 13 |
| agree / disagree / missing | 2 / 11 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
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
Status: **AGREE**

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

Second transcription's note: Line 2 asks for the total cost of all section 179 property, including listed property, and not just the amount elected. Section 179 property must be used more than 50% in the business. The business-use cost is used here (line 6 column (b), "Cost (business use only)").

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
{"keys": [{"line": "(a)"}], "op": "keyed_lookup", "table": "pub946_appendix_b_gds_recovery_period"}
```

Second transcription's note: The text gives the GDS recovery period as a lookup by class life (i4562 column (d) table and Pub. 946 Appendix B). I read this as one table keyed by asset class. Classes this tool does not cover map to "outside".

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

Second transcription's note: The percentage is a whole number, so dividing by 100 at two decimal places is exact.

Ruling: equivalent; project retained. asset.pct is a whole number from 1 to 100, so the ratio pct/100 is exact at two places and the six places the project uses give the same value.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The allowance applies only in the first year. For listed property the same amount belongs on line 25 instead of line 14. This line holds the allowance for the property, and the business-level totals split it by asset.listed.

Ruling: representation; project retained. The special allowance figured identically; the project figures each per-asset amount for every asset and selects 2025 property, prior-year property and listed property where the totals are taken (asset.dep_2025, asset.bonus_2025, asset.dep_prior, asset.dep_listed, and the where-filters of the sc sums for Form 4562 lines 14, 17, 19, 25 and 26); the second zeroes the same amounts on the asset itself.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1}], "op": "keyed_lookup", "table": "macrs_gds_percentage"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_to_midquarter_convention"}, {"const": 1}], "op": "keyed_lookup", "table": "macrs_gds_percentage"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Lines 19a-19j are only for assets placed in service in 2025 and exclude listed property, which is reported in Part V. This line holds the amount for the property, and the business-level totals exclude listed property by asset.listed.

Ruling: representation; project retained. MACRS on 2025 property by the mid-quarter test (Pub. 946 p. 34, Which Convention Applies), on the basis less the section 179 election and the special allowance; the project figures each per-asset amount for every asset and selects 2025 property, prior-year property and listed property where the totals are taken (asset.dep_2025, asset.bonus_2025, asset.dep_prior, asset.dep_listed, and the where-filters of the sc sums for Form 4562 lines 14, 17, 19, 25 and 26); the second zeroes the same amounts on the asset itself.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_to_recovery_year_2025"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_recovery_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_to_recovery_year_2025"}], "op": "keyed_lookup", "table": "macrs_gds_percentage"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_recovery_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "placed_year_to_recovery_year_2025"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Per Pub. 946 the table rates apply to the unadjusted basis, and the same business-use basis as in the year placed in service is assumed. The text does not say what to enter once the recovery period has ended (only for automobiles), so the entry here is zero. Listed property is excluded at the business level by asset.listed.

Ruling: representation; project retained. MACRS for earlier property from the Pub. 946 tables by period, convention and recovery year, on the basis less earlier section 179 and special allowance; the project figures each per-asset amount for every asset and selects 2025 property, prior-year property and listed property where the totals are taken (asset.dep_2025, asset.bonus_2025, asset.dep_prior, asset.dep_listed, and the where-filters of the sc sums for Form 4562 lines 14, 17, 19, 25 and 26); the second zeroes the same amounts on the asset itself.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"of": [{"line": "17"}, {"line": "19(g)"}], "op": "sum"}}], "op": "choose"}
```

Second transcription's note: The business/investment use percentage is used as the qualified business use percentage. The text says the qualified percentage may be smaller, and no separate input exists for it.

Ruling: representation; project retained. Column (h) is the asset's MACRS (2025 or earlier) without the special allowance on both sides; the project figures each per-asset amount for every asset and selects 2025 property, prior-year property and listed property where the totals are taken (asset.dep_2025, asset.bonus_2025, asset.dep_prior, asset.dep_listed, and the where-filters of the sc sums for Form 4562 lines 14, 17, 19, 25 and 26); the second zeroes the same amounts on the asset itself.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.bonus_2025 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.s179_2025 | asset.h_s179_bad | asset.h_s179_bad |
| asset.mq_q4 | asset.h_pct_bad, asset.screen | asset.h_pct_bad, asset.screen |
| asset.mq_total | asset.h_pct_bad, asset.screen | asset.h_pct_bad, asset.screen |
| asset.cost179 | asset.h_pct_bad, asset.screen | asset.h_pct_bad, asset.screen |
| asset.dep_prior | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.h_pct_bad, asset.screen | asset.h_pct_bad, asset.screen |
| 14 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 19(g) | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 17 | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen |
| 26(h) | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |

## Raw second transcription

```yaml
```yaml
lines:
  - id: asset.line(d)
    printed: "(d)"
    label: "Recovery period. Determine the recovery period from the following table (Recovery Period for Most Property), using the classification found from the property's class life (Pub. 946, Appendix B, Tables B-1 and B-2)"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: pub946_appendix_b_gds_recovery_period, keys: [asset.class]}
    refuses: [asset.screen]
    note: "The text gives the GDS recovery period as a lookup by class life (i4562 column (d) table and Pub. 946 Appendix B). I read this as one table keyed by asset class. Classes this tool does not cover map to \"outside\"."

  - id: asset.h_outside
    printed: "(helper)"
    label: "The asset class is outside this tool"
    type: Bool
    expr: {op: test, eq: [asset.line(d), {const: "outside"}]}

  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

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

  - id: asset.h_half
    printed: "(helper)"
    label: "Fifty percent, as cents"
    type: NonNegDollars
    expr: {op: param, ref: sc.fifty_cents}

  - id: asset.h_pct_c
    printed: "(helper)"
    label: "The percentage of business/investment use, as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}

  - id: asset.h_pct_bad
    printed: "(helper)"
    label: "The business use percentage is more than 100"
    type: Bool
    expr: {op: test, gt: [asset.h_pct_c, asset.h_hundred]}

  - id: asset.h_over_half
    printed: "(helper)"
    label: "Used predominantly (more than 50%) in your trade or business"
    type: Bool
    expr: {op: test, gt: [asset.h_pct_c, asset.h_half]}

  - id: asset.h_listed_low
    printed: "(helper)"
    label: "Listed property used 50% or less in a qualified business use (line 27; straight line over the ADS recovery period)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, not: {op: test, eq: [asset.h_over_half, {const: true}]}}]}
    note: "The tool does not compute line 27 (ADS straight line). This property is refused rather than computed."

  - id: asset.line(c)
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only). Multiply the cost or other basis of the property by the percentage of business/investment use (before the section 179 expense deduction and any special depreciation allowance)"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_c, whole: asset.h_hundred, places: 2}
    refuses: [asset.screen, asset.h_pct_bad]
    note: "The percentage is a whole number, so dividing by 100 at two decimal places is exact."

  - id: asset.h_is2025
    printed: "(helper)"
    label: "Placed in service during the tax year beginning in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}

  - id: asset.h_s179_bad
    printed: "(helper)"
    label: "The section 179 election is more than the business cost, or is made for property not used more than 50% in the business or not placed in service in 2025"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [asset.s179, asset.line(c)]}
        - {op: test, all: [{op: test, gt: [asset.s179, {const: 0}]}, {op: test, not: {op: test, eq: [asset.h_over_half, {const: true}]}}]}
        - {op: test, all: [{op: test, gt: [asset.s179, {const: 0}]}, {op: test, not: {op: test, eq: [asset.h_is2025, {const: true}]}}]}

  - id: asset.h_after179
    printed: "(helper)"
    label: "Depreciable basis: business/investment basis less the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.line(c), take: asset.s179}
    note: "The section 179 amount used is the amount elected (column (c) of line 6), as the text says (\"Enter the amount you elect to expense. You can depreciate the amount you do not expense\")."

  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "The special allowance choice differs within a class of 2025 property"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.bonus_same, {const: false}]}]}
    note: "The election out (and the 40% election) applies to all property in a class placed in service during the year. An answer that differs within a class is refused."

  - id: asset.h_rate40
    printed: "(helper)"
    label: "40% special depreciation allowance"
    type: Rate
    expr: {op: param, ref: sc.bonus_rate_40}

  - id: asset.h_bonus_forty
    printed: "(helper)"
    label: "40% of the depreciable basis"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after179, rate: asset.h_rate40}

  - id: asset.h_bonus_fullcase
    printed: "(helper)"
    label: "Allowance when claimed: 100% if acquired after January 19, 2025; otherwise limited to 40%"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.after_jan19, {const: true}]}, then: asset.h_after179}
        - {guard: {op: test, eq: [asset.after_jan19, {const: false}]}, then: asset.h_bonus_forty}

  - id: asset.h_bonus
    printed: "(helper)"
    label: "Special depreciation allowance: depreciable basis times the applicable percentage"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.bonus_choice, {const: "full"}]}, then: asset.h_bonus_fullcase}
        - {guard: {op: test, eq: [asset.bonus_choice, {const: "forty"}]}, then: asset.h_bonus_forty}
        - {guard: {op: test, eq: [asset.bonus_choice, {const: "none"}]}, then: asset.h_zero}
    note: "Every GDS period in this tool is 20 years or less, so the property is treated as qualified property. The exceptions (listed property used 50% or less, disposed-of or converted property, ADS) are refused through asset.h_listed_low and asset.screen."

  - id: asset.line14
    printed: "14"
    label: "Special depreciation allowance for qualified property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_bonus}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
    refuses: [asset.screen, asset.h_outside, asset.h_pct_bad, asset.h_listed_low, asset.h_s179_bad, asset.h_bonus_mixed]
    note: "The allowance applies only in the first year. For listed property the same amount belongs on line 25 instead of line 14. This line holds the allowance for the property, and the business-level totals split it by asset.listed."

  - id: asset.h_ub
    printed: "(helper)"
    label: "Basis for MACRS depreciation (column (c) after the section 179 deduction and any special depreciation allowance included on line 14)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after179, take: asset.line14}

  - id: asset.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}

  - id: asset.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_to_midquarter_convention, keys: [asset.quarter]}

  - id: asset.h_year1
    printed: "(helper)"
    label: "First year of recovery"
    type: Count
    expr: {op: param, ref: sc.year1}

  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "Applicable rate from the appropriate table, half-year convention, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds_percentage, keys: [asset.line(d), asset.h_hy, asset.h_year1]}

  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Applicable rate from the appropriate table, mid-quarter convention, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds_percentage, keys: [asset.line(d), asset.h_qconv, asset.h_year1]}

  - id: asset.h_macrs_hy
    printed: "(helper)"
    label: "Multiply column (c) by the applicable rate (half-year convention)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_ub, rate: asset.h_rate_hy}

  - id: asset.h_macrs_mq
    printed: "(helper)"
    label: "Multiply column (c) by the applicable rate (mid-quarter convention)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_ub, rate: asset.h_rate_mq}

  - id: asset.h_macrs2025
    printed: "(helper)"
    label: "MACRS depreciation for 2025 property, under the convention that applies"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [mq.applies, {const: true}]}, then: asset.h_macrs_mq}
        - {guard: {op: test, eq: [mq.applies, {const: false}]}, then: asset.h_macrs_hy}
    note: "Whether the mid-quarter convention applies is decided for all 2025 MACRS property together (mq.applies, from asset.mq_q4 and asset.mq_total), not for each item."

  - id: asset.line19(g)
    printed: "19(g)"
    label: "Depreciation deduction. Multiply column (c) by the applicable rate from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_macrs2025}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
    refuses: [asset.screen, asset.h_outside, asset.h_pct_bad, asset.h_listed_low, asset.h_s179_bad, asset.h_bonus_mixed]
    note: "Lines 19a-19j are only for assets placed in service in 2025 and exclude listed property, which is reported in Part V. This line holds the amount for the property, and the business-level totals exclude listed property by asset.listed."

  - id: asset.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025 (from the year placed in service)"
    type: Count
    expr: {op: keyed_lookup, table: placed_year_to_recovery_year_2025, keys: [asset.placed]}

  - id: asset.h_last
    printed: "(helper)"
    label: "Last year of recovery for the recovery period (the year that includes the final part of the recovery period)"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_recovery_year, keys: [asset.line(d)]}

  - id: asset.h_done
    printed: "(helper)"
    label: "The recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [asset.h_year, asset.h_last]}

  - id: asset.h_ub_prior_a
    printed: "(helper)"
    label: "Business basis less the section 179 deduction claimed"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.line(c), take: asset.prior_179}

  - id: asset.h_ub_prior
    printed: "(helper)"
    label: "Unadjusted basis (reduced by any section 179 deduction and any special depreciation allowance taken)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_ub_prior_a, take: asset.prior_bonus}

  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "Applicable rate from the percentage table for the 2025 year of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds_percentage, keys: [asset.line(d), asset.prior_conv, asset.h_year]}

  - id: asset.h_macrs_prior_live
    printed: "(helper)"
    label: "Apply the table rate to the property's unadjusted basis"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_ub_prior, rate: asset.h_rate_prior}

  - id: asset.line17
    printed: "17"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_zero}
        - guard: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: false}]}, {op: test, eq: [asset.h_done, {const: true}]}]}
          then: asset.h_zero
        - guard: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: false}]}, {op: test, eq: [asset.h_done, {const: false}]}]}
          then: asset.h_macrs_prior_live
    refuses: [asset.screen, asset.h_outside, asset.h_pct_bad, asset.h_listed_low]
    note: "Per Pub. 946 the table rates apply to the unadjusted basis, and the same business-use basis as in the year placed in service is assumed. The text does not say what to enter once the recovery period has ended (only for automobiles), so the entry here is zero. Listed property is excluded at the business level by asset.listed."

  - id: asset.h_dep_total
    printed: "(helper)"
    label: "MACRS depreciation of this property for 2025 (placed in service in 2025 or earlier)"
    type: NonNegDollars
    expr: {op: sum, of: [asset.line19(g), asset.line17]}

  - id: asset.line26(h)
    printed: "26(h)"
    label: "Depreciation deduction. For property used more than 50% in a qualified business use and placed in service after 1986, figure column (h) by following the instructions for line 19, column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.listed, {const: true}]}, then: asset.h_dep_total}
        - {guard: {op: test, eq: [asset.listed, {const: false}]}, then: asset.h_zero}
    refuses: [asset.screen, asset.h_outside, asset.h_pct_bad, asset.h_listed_low]
    note: "The business/investment use percentage is used as the qualified business use percentage. The text says the qualified percentage may be smaller, and no separate input exists for it."

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
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.s179}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
    refuses: [asset.h_s179_bad]

  - id: asset.mq_total
    printed: "(helper)"
    label: "Mid-quarter test basis, all of 2025 (depreciable basis after section 179 and personal use, before any special depreciation allowance)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_after179}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}

  - id: asset.mq_q4
    printed: "(helper)"
    label: "Mid-quarter test basis, fourth quarter (placed in service during the last 3 months of the tax year)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.quarter, {const: "q4"}]}]}
          then: asset.h_after179
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.quarter, {const: "q4"}]}]}}
          then: asset.h_zero

  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025 (business use only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.h_over_half, {const: true}]}]}
          then: asset.line(c)
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.h_is2025, {const: true}]}, {op: test, eq: [asset.h_over_half, {const: true}]}]}}
          then: asset.h_zero
    note: "Line 2 asks for the total cost of all section 179 property, including listed property, and not just the amount elected. Section 179 property must be used more than 50% in the business. The business-use cost is used here (line 6 column (b), \"Cost (business use only)\")."

  - id: asset.dep_prior
    printed: "(helper)"
    label: "MACRS on property placed in service before 2025"
    type: NonNegDollars
    expr: {op: copy, from: asset.line17}
```
```
