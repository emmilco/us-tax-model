# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3bd958c1cda7b95c1eefe8deed517d8b2b0fa71fac8a0a039a084661fd161b3f |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 77448d9efd60568e88aa320de925a9afc86c212f00c2169ecf0b3b8c7ae5ce82 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 6ff28f69c232cb157b95a0aa2bfb0fc389f458f23dadbb47104466a281c7c6d4 |
| printed lines compared | 16 |
| agree / disagree / missing | 2 / 14 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 32, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, f1040, f4952, household, refund, s1, sa, scope |
| named line | f5329 |
| shared page | f4562, mq, person, s179, sc, scveh |

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The pages do not define this interface. My reading: the regular MACRS deduction for property placed in service in 2025, listed or not, without the section 179 deduction or the special allowance.

Ruling: model error; the pass reply's asset.h_bonus_mixed (placed in 2025 and asset.bonus_same false) refuses asset.bonus_2025 whatever asset.bonus_choice is, so it asks asset.bonus_same of 2025 property whose choice is none; the project asks it only on the full and forty branches (asset.bonus_full, asset.bonus_forty refuse on asset.bonus_mixed). i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year" makes the same-class question matter only where an allowance is claimed. Same point as the backlog and refresh rulings. The values are now representation: the reply's dep_2025 is the table rate times its (c), which for 2025 property is cost times business use less the section 179 cost and the special allowance, the project's 19(g) basis (asset.ub); the refresh round's added line 14 is gone (i4562 p. 9, Line 17 and Lines 19a Through 19j). Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: My reading: this is this property's total 2025 special depreciation allowance (line 14 when not listed, line 25 when listed). The allowance applies only in the year the property is placed in service. Every GDS recovery period handled here is 20 years or less.

Ruling: model error; the pass reply's asset.h_bonus_mixed (placed in 2025 and asset.bonus_same false) refuses asset.bonus_2025 whatever asset.bonus_choice is, so it asks asset.bonus_same of 2025 property whose choice is none; the project asks it only on the full and forty branches (asset.bonus_full, asset.bonus_forty refuse on asset.bonus_mixed). i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year" makes the same-class question matter only where an allowance is claimed. Same point as the backlog and refresh rulings. Values: 100% for full after January 19, 40% for forty or before January 20, none for none, on the basis after section 179, the project's reading. Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### asset.s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**
Reviewed in: pass 752f59790b4e

### asset.mq_q4 — Mid-quarter test basis, fourth quarter
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "asset.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; same line and candidate as the refresh-round ruling. p946 p. 34, "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year"; both take the business cost less the section 179 cost of 2025 property placed in the fourth quarter.
Reviewed in: pass 752f59790b4e

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; same line and candidate as the refresh-round ruling (p946 p. 34, the same test over the whole year).
Reviewed in: pass 752f59790b4e

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open point: line 2 says 'total cost of all section 179 property', but line 6 column (b) is 'Cost (business use only)'. I use the business-use cost. I do not leave out property used 50% or less in the business, because the definition of section 179 property does not include the more-than-50% test (that test limits the election).

Ruling: model error; i4562 p. 4, Line 2, "Enter the total cost of all section 179 property you placed in service during the tax year", and Worksheet 1, "include the total amount of eligible section 179 property"; p946 p. 16, Partial business use, "you can elect the section 179 deduction only if you use the property more than 50% for business in the year you place it in service". The reply now counts 2025 property used 50% or less (its note says so); such property is not eligible, and the project counts the business cost only when asset.over_half (asset.cost179_2025). The difference reaches Form 4562 line 2 for a 2025 asset used 50% or less (and the line 5 threshold only above $4,000,000 of cost). Project stands. Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: The pages do not define this interface. My reading: the MACRS deduction for property placed in service before 2025, listed or not.

Ruling: representation; i4562 p. 9, Line 17, "enter the deductions for the current year". For property placed before 2025 the reply takes the table rate (the convention used when placed in service, the recovery year from asset.placed) times the business cost less the earlier section 179 deduction and special allowance, zero after the recovery period; the project's line 17 reads the same answers (asset.prior_179, asset.prior_bonus). The reply's bonus refusal is not reached for property placed before 2025 (asset.h_bonus_mixed is false there). Same reading as the refresh-round ruling. Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### (d) — Recovery period under GDS for the asset class
Status: **AGREE**
Reviewed in: pass 752f59790b4e

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **DISAGREE**

Project:

```json
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}}], "op": "choose"}
```

Second transcription's note: For property placed in service before 2025, this is the unadjusted basis that the table rates apply to (Pub. 946: cost less the section 179 deduction and the special allowance, without subtracting earlier MACRS depreciation). It uses the current business-use percentage because the screen rules out any change in that percentage.

Ruling: model error; same candidate as the refresh-round ruling. the pass reply's asset.h_bonus_mixed (placed in 2025 and asset.bonus_same false) refuses asset.bonus_2025 whatever asset.bonus_choice is, so it asks asset.bonus_same of 2025 property whose choice is none; the project asks it only on the full and forty branches (asset.bonus_full, asset.bonus_forty refuse on asset.bonus_mixed). i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year" makes the same-class question matter only where an allowance is claimed. Same point as the backlog and refresh rulings. Values: the project shows at this marker the business basis before section 179 and the special allowance (its label; the reduced basis is 19(c)); the reply nets them here, so its amount differs for every 2025 asset with an election or allowance (i4562 p. 11, Column (c), "From that result, subtract any credits and deductions allocable to the property"; the project shows the subtraction at 19(c)).
Reviewed in: pass 752f59790b4e

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; the pass reply's asset.h_bonus_mixed (placed in 2025 and asset.bonus_same false) refuses asset.bonus_2025 whatever asset.bonus_choice is, so it asks asset.bonus_same of 2025 property whose choice is none; the project asks it only on the full and forty branches (asset.bonus_full, asset.bonus_forty refuse on asset.bonus_mixed). i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year" makes the same-class question matter only where an allowance is claimed. Same point as the backlog and refresh rulings. Values: the reply's line 14 is its allowance for 2025 property that is not listed, the project's reading (i4562 pp. 5-6, Line 14). Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error; the pass reply's asset.h_bonus_mixed (placed in 2025 and asset.bonus_same false) refuses asset.bonus_2025 whatever asset.bonus_choice is, so it asks asset.bonus_same of 2025 property whose choice is none; the project asks it only on the full and forty branches (asset.bonus_full, asset.bonus_forty refuse on asset.bonus_mixed). i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year" makes the same-class question matter only where an allowance is claimed. Same point as the backlog and refresh rulings. Values: the allowance for listed property placed in 2025, the project's line 25 (i4562 p. 13, Line 25, "If you placed in service certain qualified listed property during the tax year, you may be able to deduct the special depreciation allowance"). Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: representation; i4562 p. 5, Line 6, "Enter the elected section 179 cost of listed property in column (i) of line 26". The reply's column (i) is the elected cost of listed 2025 property, shown only for it; the project's line reads the same answers. Same reading as the refresh-round ruling. Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"line": "(c)"}
```

Ruling: model error; the pass reply's asset.h_bonus_mixed (placed in 2025 and asset.bonus_same false) refuses asset.bonus_2025 whatever asset.bonus_choice is, so it asks asset.bonus_same of 2025 property whose choice is none; the project asks it only on the full and forty branches (asset.bonus_full, asset.bonus_forty refuse on asset.bonus_mixed). i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year" makes the same-class question matter only where an allowance is claimed. Same point as the backlog and refresh rulings. Values: the reply copies its (c), for 2025 property the business cost less section 179 and the allowance, the project's 19(c) (asset.ub; i4562 p. 11, Column (c)). Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; the pass reply's asset.h_bonus_mixed (placed in 2025 and asset.bonus_same false) refuses asset.bonus_2025 whatever asset.bonus_choice is, so it asks asset.bonus_same of 2025 property whose choice is none; the project asks it only on the full and forty branches (asset.bonus_full, asset.bonus_forty refuse on asset.bonus_mixed). i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year" makes the same-class question matter only where an allowance is claimed. Same point as the backlog and refresh rulings. Values: the table rate (mid-quarter when mq.applies, else half-year) times the reduced basis, the project's reading (i4562 p. 9, Lines 19a Through 19j). Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i4562 p. 9, Line 17, "enter the deductions for the current year. To figure the deductions, see the instructions for line 19, column (g)". As asset.dep_prior: for property placed before 2025 and not listed the reply's amount is the project's; the bonus refusal is not reached there. Same reading as the refresh-round ruling. Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error; for listed property placed in 2025 the reply's column (h) reads its (c), which reaches asset.bonus_2025 and so asks asset.bonus_same when the choice is none (as at line 14; i4562 p. 7, Election out). For listed property placed earlier the amount is line 17's reading, the project's (i4562 p. 15, Column (h), "figure column (h) by following the instructions for line 19, column (g)"). Round-2 rulings are from reading the pass reply (.transcription/asset.lines-70ea95948c1d) against the project; triage was not rerun.
Reviewed in: pass 752f59790b4e

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| asset.bonus_2025 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| asset.s179_2025 | asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_s179_bad, asset.h_s179_over, asset.screen |
| asset.mq_q4 | asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_s179_bad, asset.h_s179_over, asset.screen |
| asset.mq_total | asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_s179_bad, asset.h_s179_over, asset.screen |
| asset.cost179 | asset.screen | asset.screen |
| asset.dep_prior | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| 14 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| 25 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| 26(i) | asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_s179_bad, asset.h_s179_over, asset.screen |
| 19(c) | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| 19(g) | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| 17 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |
| 26(h) | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.h_s179_over, asset.screen |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| asset.dep_2025 | b87bf380fa3f7e323f7fea236e98ccd58db9ce3dcc1320db2eacaee4993e3ae5 |
| asset.bonus_2025 | 9853882e3232fcc2560fcccde147ecade35b8597cc50012826d20d5b05d5af17 |
| asset.s179_2025 | 0e78d665496ecb734aeac489cfc6c3a51a8d8d7d4cd9ebc44331e54bc4fb4e54 |
| asset.mq_q4 | 74c25aa2abf2ec170df2a795b12516dac0d31a0b6f40381e8449e063c28a75bc |
| asset.mq_total | 2f97e451d41266252741f5b9ccfa5b1fce233469d814f28b3e3d3b0f606ac2d4 |
| asset.cost179 | 4b6be6a2ec5fdf0fd51c9b2f739c4af14f8a3b97318ae4248af1553192a7a414 |
| asset.dep_prior | e692c831a4e43902d96b999dc35c0146f11f71c7fd2facced0547ac5068a1f53 |
| (d) | 30d8467f77ce760e81a2850c398722a1193754cb1675b820a8b630c50143a099 |
| (c) | c7319a0140fe603a0a0d6885dd18a90ecc91916f9fa20f392d83f77e2e66f208 |
| 14 | 19af9aabaa47c93ca76cd9c0c7db96fe116b622ded37c861ae66bcc8e6742b81 |
| 25 | c3374b29da3a96e431ad058ca8283ba635ecbc9a69df93eee721097b0c55b469 |
| 26(i) | 506f080f534ca5adcb8863a218607bb5f1ec1bd6e2a6ca090c9d25b676fab544 |
| 19(c) | 05e3c03b192cf98ea0d18ba2c40c470331a42cac168015c129fc041ff62e56ad |
| 19(g) | c93d99ea120a63726ce0c0a5b27a0036c3354f3caaebed97ea946f7daf545026 |
| 17 | 4ee803502164abff09c35517381f499c164965ae6a9ba708f2bac237a3f7b8c4 |
| 26(h) | 14811301d9197c23d67f5bc110c70298f4a1b3af275cd1ce356a65b0d5b826b7 |
| (rest of the document) | c9708e5777e6b69e7558e632a0713a1496a425dc2a16eb800463caf770f116b1 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| asset.dep_2025 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| asset.bonus_2025 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| asset.s179_2025 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| asset.mq_q4 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| asset.mq_total | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| asset.cost179 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| asset.dep_prior | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (d) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (c) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 14 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 25 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 26(i) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 19(c) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 19(g) | 14ab4862811584dfd01cb4c921ce8aa19deac170e103f50c05485c1ee3465442 |
| 17 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 26(h) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 752f59790b4e

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines asset.dep_2025, asset.bonus_2025, asset.s179_2025, asset.mq_q4, asset.mq_total, asset.cost179, asset.dep_prior, (d), (c), 14, 25, 26(i), 19(c), 19(g), 17, 26(h) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 752f59790b4e1c82d68567ca4ce5aa540d66ccec0c85b6f4f8f515b4b710fb23 |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 2a605d1c9ccb832ac689a14c9906c9af955bf9b73e377198a12586acd73910e8 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 09e40eb85eee7286d785f0f46ce3575296ca5322e1414811ab3122c147143b77 |
| receipt | .transcription/asset.lines-70ea95948c1d |
| printed lines compared | 16 |
| agree / disagree / missing | 2 / 14 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 32, 33, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 33, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, f1040, household, scope |
| named line | s1 |
| shared page | f4562, mq, person, s179, sc, scveh |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: asset.h_outside
    printed: "(helper)"
    label: "The property's recovery period is not 3, 5, 7, 10, 15 or 20 years under GDS (for example 25-year water utility property or 50-year railroad gradings), so the percentage tables used here do not apply"
    type: Bool
    expr: {op: test, eq: [asset.period, {const: "outside"}]}
  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: asset.h_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: asset.h_pct_c
    printed: "(helper)"
    label: "Business/investment use percentage, written as cents (percent x 1 cent)"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}
  - id: asset.h_bus_cost
    printed: "(helper)"
    label: "Multiply the cost or other basis of the property by the percentage of business/investment use"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_c, whole: {param: sc.hundred_cents}, places: 2}
    refuses: [asset.screen]
  - id: asset.h_is2025
    printed: "(helper)"
    label: "Placed in service during the tax year beginning in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.h_s179_over
    printed: "(helper)"
    label: "Consistency check: the elected section 179 cost is more than the property's business cost"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, gt: [asset.s179, asset.h_bus_cost]}
  - id: asset.h_s179_bad
    printed: "(helper)"
    label: "Consistency check: a section 179 cost is elected for property that is not section 179 property, or that is not used predominantly (more than 50%) in the business"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, gt: [asset.s179, {const: 0}]}
        - op: test
          any:
            - {op: test, eq: [asset.not179, {const: true}]}
            - {op: test, le: [asset.pct, {const: 50, type: Count}]}
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Column (c)—Elected cost. Enter the amount you elect to expense (section 179 property placed in service during the tax year)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    refuses:
      - asset.screen
      - {when: asset.h_s179_over, when_known: true}
      - {when: asset.h_s179_bad, when_known: true}
    note: "Open point: the text does not say whether depreciable basis is reduced by the elected section 179 cost or only by the part that is allowed after the business income limit (line 11). I reduce it by the elected amount, and the other lines build on that."
  - id: asset.h_mq_basis
    printed: "(helper)"
    label: "Depreciable basis before any special depreciation allowance: business/investment portion of cost minus the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.s179_2025}
    refuses:
      - asset.screen
      - {when: asset.h_s179_over, when_known: true}
  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "The special depreciation allowance choice is not the same for all property in this class placed in service in 2025 (the election applies to all such property in the class)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.bonus_same, {const: false}]}
  - id: asset.h_bonus_40
    printed: "(helper)"
    label: "40% special depreciation allowance: depreciable basis multiplied by 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_mq_basis, rate: {param: sc.bonus_rate_40}}
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance: multiply the depreciable basis of the property by the applicable percentage (100% for qualified property acquired after January 19, 2025, or 40% if elected; 40% for qualified property acquired after September 27, 2017, and before January 20, 2025; none if you elected not to claim it)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
              - {op: test, eq: [asset.after_jan19, {const: true}]}
          then: asset.h_mq_basis
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - op: test
                any:
                  - {op: test, eq: [asset.bonus_choice, {const: "forty"}]}
                  - op: test
                    all:
                      - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
                      - {op: test, eq: [asset.after_jan19, {const: false}]}
          then: asset.h_bonus_40
        - guard:
            op: test
            any:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_outside, asset.h_bonus_mixed]
    note: "My reading: this is this property's total 2025 special depreciation allowance (line 14 when not listed, line 25 when listed). The allowance applies only in the year the property is placed in service. Every GDS recovery period handled here is 20 years or less."
  - id: asset.h_cur_basis
    printed: "(helper)"
    label: "Basis for depreciation, 2025 property: business/investment cost minus section 179 expense deduction minus special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_mq_basis, take: asset.bonus_2025}
  - id: asset.h_prior_a
    printed: "(helper)"
    label: "Business/investment cost minus the section 179 deduction claimed in the year placed in service"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.prior_179}
  - id: asset.h_prior_basis
    printed: "(helper)"
    label: "Unadjusted basis, earlier-year property: business/investment cost minus section 179 deduction minus special depreciation allowance taken"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_prior_a, take: asset.prior_bonus}
  - id: asset.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: asset.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter of 2025 in which the property was placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}
  - id: asset.h_year
    printed: "(helper)"
    label: "Year of the recovery period that 2025 is for this property"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.h_last
    printed: "(helper)"
    label: "Last year of the recovery period in the percentage table"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}
    refuses: [asset.h_outside]
  - id: asset.h_ended
    printed: "(helper)"
    label: "The recovery period ended before 2025 (the depreciable basis has been fully recovered)"
    type: Bool
    expr: {op: test, gt: [asset.h_year, asset.h_last]}
  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "Applicable rate from the MACRS percentage table, half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year]}
  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Applicable rate from the MACRS percentage table, mid-quarter convention for the quarter placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_year]}
  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "Applicable rate from the MACRS percentage table, convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_year]}
  - id: asset.h_dep_hy
    printed: "(helper)"
    label: "Multiply column (c) by the applicable rate (half-year convention)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: asset.h_rate_hy}
  - id: asset.h_dep_mq
    printed: "(helper)"
    label: "Multiply column (c) by the applicable rate (mid-quarter convention)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: asset.h_rate_mq}
  - id: asset.h_dep_prior_amt
    printed: "(helper)"
    label: "Multiply the unadjusted basis by the applicable rate (convention used when placed in service)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: asset.h_rate_prior}
  - id: asset.h_dep_cur
    printed: "(helper)"
    label: "Depreciation for 2025 property: mid-quarter convention if the depreciable bases of property placed in service in the last 3 months are more than 40% of the total, otherwise half-year convention"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [mq.applies, {const: true}]}
          then: asset.h_dep_mq
        - guard: {op: test, eq: [mq.applies, {const: false}]}
          then: asset.h_dep_hy
  - id: asset.h_dep_all
    printed: "(helper)"
    label: "MACRS depreciation deduction for this property for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_dep_cur
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.h_ended, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.h_ended, {const: false}]}
          then: asset.h_dep_prior_amt
    refuses: [asset.screen, asset.h_outside]
  - id: asset.h_show14
    printed: "(helper)"
    label: "Placed in service in 2025 and not listed property (reported on lines 14 and 19)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.listed, {const: false}]}
  - id: asset.h_show17
    printed: "(helper)"
    label: "Placed in service before 2025 and not listed property (reported on line 17)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: false}]}
        - {op: test, eq: [asset.listed, {const: false}]}
  - id: asset.h_show_l25
    printed: "(helper)"
    label: "Listed property placed in service in 2025 (lines 25 and 26(i))"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.listed, {const: true}]}

  - id: asset.period
    printed: "(d)"
    label: "Column (d)—Recovery period. Determine the recovery period (Pub. 946, Appendix B, Table of Class Lives and Recovery Periods)"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}
    refuses: [asset.screen]
  - id: asset.basis
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only): multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property (section 179 expense deduction, any special depreciation allowance)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_cur_basis
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_prior_basis
    refuses: [asset.screen, asset.h_outside]
    note: "For property placed in service before 2025, this is the unadjusted basis that the table rates apply to (Pub. 946: cost less the section 179 deduction and the special allowance, without subtracting earlier MACRS depreciation). It uses the current business-use percentage because the screen rules out any change in that percentage."
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_outside, asset.h_bonus_mixed]
    shown_when: asset.h_show14
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year and used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_outside, asset.h_bonus_mixed]
    shown_when: asset.h_show_l25
  - id: asset.f26i
    printed: "26(i)"
    label: "Column (i)—Elected section 179 cost. Enter the amount you elect to expense for section 179 property used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
    shown_when: asset.h_show_l25
  - id: asset.col19c
    printed: "19(c)"
    label: "Column (c)—Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr: {op: copy, from: asset.basis}
    refuses: [asset.screen, asset.h_outside]
    shown_when: asset.h_show14
  - id: asset.macrs2025
    printed: "19(g)"
    label: "Column (g)—Depreciation deduction. Multiply column (c) by the applicable rate from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_show14, {const: true}]}
          then: asset.h_dep_all
        - guard: {op: test, eq: [asset.h_show14, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_outside]
    shown_when: asset.h_show14
  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_show17, {const: true}]}
          then: asset.h_dep_all
        - guard: {op: test, eq: [asset.h_show17, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_outside]
    shown_when: asset.h_show17
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Column (h)—Depreciation deduction. For property used more than 50% in a qualified business use and placed in service after 1986, figure column (h) by following the instructions for line 19, column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_dep_all
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_outside]
    shown_when: asset.listed

  - id: asset.dep_2025
    printed: "(helper)"
    label: "MACRS depreciation deduction for this property placed in service in 2025 (line 19(g), or line 26(h) if listed)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_dep_all
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_outside]
    note: "The pages do not define this interface. My reading: the regular MACRS deduction for property placed in service in 2025, listed or not, without the section 179 deduction or the special allowance."
  - id: asset.dep_prior
    printed: "(helper)"
    label: "MACRS depreciation deduction for this property placed in service before 2025 (line 17, or line 26(h) if listed)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_dep_all
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_outside]
    note: "The pages do not define this interface. My reading: the MACRS deduction for property placed in service before 2025, listed or not."
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance, after section 179 and personal-use reduction) of this MACRS property if placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.quarter, {const: "q4"}]}
          then: asset.h_mq_basis
        - guard:
            op: test
            any:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, ne: [asset.quarter, {const: "q4"}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.mq_total
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance, after section 179 and personal-use reduction) of this MACRS property if placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_mq_basis
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service during the tax year (Form 4562, line 2, including listed property)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.not179, {const: false}]}
          then: asset.h_bus_cost
        - guard:
            op: test
            any:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.not179, {const: true}]}
          then: asset.h_zero
    refuses: [asset.screen]
    note: "Open point: line 2 says 'total cost of all section 179 property', but line 6 column (b) is 'Cost (business use only)'. I use the business-use cost. I do not leave out property used 50% or less in the business, because the definition of section 179 property does not include the more-than-50% test (that test limits the election)."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: asset.period
    printed: "(d)"
    label: "Recovery period. Determine the recovery period from the following table. See Pub. 946 for more information on the recovery period for MACRS property."
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}

  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: asset.h_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}

  - id: asset.h_pct_c
    printed: "(helper)"
    label: "Percentage of business/investment use, expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}

  - id: asset.h_bus_cost
    printed: "(helper)"
    label: "Multiply the cost or other basis of the property by the percentage of business/investment use"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_c, whole: {param: sc.hundred_cents}, places: 2}
    refuses: [asset.screen]

  - id: asset.h_is2025
    printed: "(helper)"
    label: "Placed in service during the tax year beginning in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}

  - id: asset.h_outside
    printed: "(helper)"
    label: "Recovery period not covered by the GDS percentage tables (more than 20 years, or real property)"
    type: Bool
    expr: {op: test, eq: [asset.period, {const: "outside"}]}

  - id: asset.h_is179prop
    printed: "(helper)"
    label: "Section 179 property placed in service during the tax year and used predominantly (more than 50%) in your trade or business"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.not179, {const: false}]}
        - {op: test, gt: [asset.pct, {const: 50, type: Count}]}
        - op: test
          any:
            - {op: test, ne: [asset.class, {const: "cqip"}]}
            - {op: test, gt: [asset.s179, {const: 0}]}
    note: "Qualified improvement property is section 179 property only if you elect to treat it so; the closed interface has no separate election, so an elected amount above zero on 6(c) is read as that election."

  - id: asset.h_s179_bad
    printed: "(helper)"
    label: "Elected section 179 cost is more than the business cost, or is entered for property that is not section 179 property placed in service in 2025 and used more than 50% in the business"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [asset.s179, asset.h_bus_cost]}
        - op: test
          all:
            - {op: test, gt: [asset.s179, {const: 0}]}
            - {op: test, eq: [asset.h_is179prop, {const: false}]}

  - id: asset.s179_2025
    printed: "(helper)"
    label: "Elected cost (section 179) for this property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.s179}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
    refuses: [{when: asset.h_s179_bad, when_known: true}]
    note: "The basis reduction uses the elected amount (column (c) of line 6 or column (i) of line 26). The text does not say how a section 179 amount that the business income limit (line 11) carries over to line 13 affects this property's basis, and this reading takes the elected amount."

  - id: asset.cost179
    printed: "(helper)"
    label: "Cost (business use only) of section 179 property placed in service during the tax year (Form 4562, line 2; Worksheet 1, line 1)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is179prop, {const: true}]}, then: asset.h_bus_cost}
        - {guard: {op: test, eq: [asset.h_is179prop, {const: false}]}, then: asset.h_zero}

  - id: asset.h_dep_base
    printed: "(helper)"
    label: "Depreciable basis before any special depreciation allowance: business/investment portion of cost reduced by the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.s179_2025}

  - id: asset.mq_total
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance) of MACRS property placed in service during the entire tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_dep_base}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}

  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance) of MACRS property placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.quarter, {const: "q4"}]}
          then: asset.h_dep_base
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is2025, {const: true}]}
                - {op: test, eq: [asset.quarter, {const: "q4"}]}
          then: asset.h_zero

  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "The special depreciation allowance choice is not the same for all property in this class placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.bonus_same, {const: false}]}

  - id: asset.h_bonus40
    printed: "(helper)"
    label: "40% special depreciation allowance: depreciable basis times 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_dep_base, rate: {param: sc.bonus_rate_40}}

  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for qualified property placed in service during the tax year: depreciable basis times the applicable percentage"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
              - {op: test, eq: [asset.after_jan19, {const: true}]}
          then: asset.h_dep_base
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - op: test
                any:
                  - op: test
                    all:
                      - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
                      - {op: test, eq: [asset.after_jan19, {const: false}]}
                  - {op: test, eq: [asset.bonus_choice, {const: "forty"}]}
          then: asset.h_bonus40
        - guard:
            op: test
            any:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_zero
    refuses: [asset.h_bonus_mixed, asset.h_outside]
    note: "Property acquired after September 27, 2017, and before January 20, 2025, gets 40% whether the choice is full or forty. Qualified property must have a recovery period of 20 years or less, so a period outside the tables is refused."

  - id: asset.h_basis25
    printed: "(helper)"
    label: "Basis for depreciation of property placed in service in 2025: business/investment cost less the section 179 expense deduction and any special depreciation allowance included on line 14 or 25"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_dep_base, take: asset.bonus_2025}

  - id: asset.h_pb1
    printed: "(helper)"
    label: "Business/investment cost less the section 179 deduction claimed in the year placed in service"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.prior_179}

  - id: asset.h_basis_prior
    printed: "(helper)"
    label: "Unadjusted basis of property placed in service before 2025: cost less the section 179 deduction claimed and any special depreciation allowance taken"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_pb1, take: asset.prior_bonus}

  - id: asset.basis
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only). To find the basis for depreciation, multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_basis25}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_basis_prior}

  - id: asset.h_show14
    printed: "(helper)"
    label: "Property placed in service in 2025 that is not listed property (lines 14 and 19)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.listed, {const: false}]}

  - id: asset.h_show25
    printed: "(helper)"
    label: "Listed property placed in service in 2025 (line 25)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.listed, {const: true}]}

  - id: asset.h_show17
    printed: "(helper)"
    label: "Property placed in service in tax years beginning before 2025 that is not listed property (line 17)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: false}]}
        - {op: test, eq: [asset.listed, {const: false}]}

  - id: asset.h_show26
    printed: "(helper)"
    label: "Listed property used more than 50% in a qualified business use (line 26)"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: true}]}

  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_show14, {const: true}]}, then: asset.bonus_2025}
        - {guard: {op: test, eq: [asset.h_show14, {const: false}]}, then: asset.h_zero}
    shown_when: asset.h_show14

  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year and used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_show25, {const: true}]}, then: asset.bonus_2025}
        - {guard: {op: test, eq: [asset.h_show25, {const: false}]}, then: asset.h_zero}
    shown_when: asset.h_show25

  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost. Enter the amount you elect to expense for section 179 property used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_show26, {const: true}]}, then: asset.s179_2025}
        - {guard: {op: test, eq: [asset.h_show26, {const: false}]}, then: asset.h_zero}
    shown_when: asset.h_show26

  - id: asset.h_year1
    printed: "(helper)"
    label: "First recovery year"
    type: Count
    expr: {op: param, ref: sc.year1}

  - id: asset.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}

  - id: asset.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}

  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "Applicable rate from Table A-1 (half-year convention), year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year1]}
    refuses: [asset.h_outside]

  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Applicable rate from Tables A-2 to A-5 (mid-quarter convention), year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_year1]}
    refuses: [asset.h_outside]

  - id: asset.h_dep25_hy
    printed: "(helper)"
    label: "Column (c) times the applicable rate, half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis25, rate: asset.h_rate_hy}

  - id: asset.h_dep25_mq
    printed: "(helper)"
    label: "Column (c) times the applicable rate, mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis25, rate: asset.h_rate_mq}

  - id: asset.h_dep25
    printed: "(helper)"
    label: "MACRS depreciation for property placed in service in 2025: multiply column (c) by the applicable rate from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [mq.applies, {const: true}]}, then: asset.h_dep25_mq}
        - {guard: {op: test, eq: [mq.applies, {const: false}]}, then: asset.h_dep25_hy}
    note: "The amount is multiplied to the cent, and the text does not fix whole-dollar rounding per asset. The return-level 40% test (mq.applies) selects the convention."

  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only only), line 19, for property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_show14, {const: true}]}, then: asset.h_basis25}
        - {guard: {op: test, eq: [asset.h_show14, {const: false}]}, then: asset.h_zero}
    shown_when: asset.h_show14

  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction. Multiply column (c) by the applicable rate from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_show14, {const: true}]}, then: asset.h_dep25}
        - {guard: {op: test, eq: [asset.h_show14, {const: false}]}, then: asset.h_zero}
    shown_when: asset.h_show14

  - id: asset.h_ry
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}

  - id: asset.h_last
    printed: "(helper)"
    label: "Last year of the recovery period in the percentage table"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}

  - id: asset.h_done
    printed: "(helper)"
    label: "Recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [asset.h_ry, asset.h_last]}

  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "Applicable rate from the table for the convention used in the year placed in service, for the 2025 year of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_ry]}
    refuses: [asset.h_outside]

  - id: asset.h_dep_prior_amt
    printed: "(helper)"
    label: "Unadjusted basis times the applicable table rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_prior, rate: asset.h_rate_prior}

  - id: asset.h_dep_prior
    printed: "(helper)"
    label: "MACRS deduction for the current year for property placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_done, {const: true}]}, then: asset.h_zero}
        - {guard: {op: test, eq: [asset.h_done, {const: false}]}, then: asset.h_dep_prior_amt}

  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_show17, {const: true}]}, then: asset.h_dep_prior}
        - {guard: {op: test, eq: [asset.h_show17, {const: false}]}, then: asset.h_zero}
    shown_when: asset.h_show17

  - id: asset.h_dep
    printed: "(helper)"
    label: "MACRS depreciation for this property for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_dep25}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_dep_prior}

  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction for property used more than 50% in a qualified business use (figure column (h) by following the instructions for line 19, column (g))"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_show26, {const: true}]}, then: asset.h_dep}
        - {guard: {op: test, eq: [asset.h_show26, {const: false}]}, then: asset.h_zero}
    shown_when: asset.h_show26

  - id: asset.h_macrs25_all
    printed: "(helper)"
    label: "MACRS depreciation of this property if placed in service in 2025 (listed or not)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_dep25}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}

  - id: asset.dep_2025
    printed: "(helper)"
    label: "Depreciation (special allowance and MACRS) for property placed in service in 2025"
    type: NonNegDollars
    expr: {op: sum, of: [asset.bonus_2025, asset.h_macrs25_all]}
    note: "The meaning of this interface is not fixed by the IRS pages. It is read as this property's 2025 depreciation other than section 179 when placed in service in 2025: line 14 or 25 plus line 19(g) or 26(h). The section 179 amount is excluded."

  - id: asset.dep_prior
    printed: "(helper)"
    label: "Depreciation for property placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_dep_prior}
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_zero}
    note: "The meaning of this interface is not fixed by the IRS pages. It is read as this property's 2025 MACRS deduction when placed in service before 2025 (line 17 or line 26(h)), the complement of asset.dep_2025. It is not accumulated prior-year depreciation, which the closed inputs cannot determine."
```
```
