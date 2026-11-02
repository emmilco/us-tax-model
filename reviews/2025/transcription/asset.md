# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4662d0f05f157c9eeccfef3381641f281bc5f15e545c65c5288c0b870d116cd7 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a3cc2098cd10664eddbdb0b0c1aba14ec81d9f4948810f7cc66a7defef9dd1f4 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | bd4ca2151f405573538c0fa0fab0e154c0d1c2f8d2daef9fa7e59d2481ca07ba |
| printed lines compared | 16 |
| agree / disagree / missing | 2 / 14 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The interface name does not define this result. Chosen: regular MACRS depreciation for 2025 on property placed in service in 2025, whether or not it is listed, excluding section 179 and the special allowance. Assumes a calendar tax year.

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate reads asset.bonus_same on returns that claim no allowance, an answer the source does not need there, so it is unknown where the project gives the amount. Differences on partial records withhold an answer the interview asks, so the interview cannot produce them. Triage executable-triage-v2 (triage/asset.json): 1618 of 1710 comparisons agree; on completed returns {"candidate-unknown": 4}.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The interface name does not define this result. Chosen: this asset's 2025 special allowance whether or not it is listed, split between lines 14 and 25 below. Property acquired before January 20, 2025 is limited to 40%, so a 'full' answer for it gives 40%. All table recovery periods are 20 years or less.

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate reads asset.bonus_same on returns that claim no allowance, an answer the source does not need there, so it is unknown where the project gives the amount. Differences on partial records withhold an answer the interview asks, so the interview cannot produce them. Triage executable-triage-v2 (triage/asset.json): 1556 of 1710 comparisons agree; on completed returns {"candidate-unknown": 4}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Per Pub. 946, this basis reflects the section 179 reduction and the personal-use part but not any special allowance. Listed property is included because nothing in the text excludes it from the mid-quarter test.

Ruling: representation; p946 p. 34: "the total depreciable bases of MACRS property you placed in service during the last 3 months". representation; every difference is on a partial or refused record: refusals sit on different lines and the withheld answers are ones the interview asks. No completed return differs. Triage executable-triage-v2 (triage/asset.json): 1579 of 1710 comparisons agree; on completed returns no difference.

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; p946 p. 34, the same test over the entire year. representation; every difference is on a partial or refused record: refusals sit on different lines and the withheld answers are ones the interview asks. No completed return differs. Triage executable-triage-v2 (triage/asset.json): 1645 of 1710 comparisons agree; on completed returns no difference.

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, "then": {"line": "(c)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open points. (1) The interface has no question on whether an item meets the section 179 property definition, so all unscreened 2025 property counts, except that qualified improvement property counts only when an amount is elected for it. (2) The more-than-50% use test is worded as a limit on the election, not in the definition, so property used 50% or less still counts if it is not listed. (3) Cost is the business-use cost, following line 6 column (b).

Ruling: model error; i4562 p. 3, Part I: "used predominantly (more than 50%) in your trade or business". The candidate counts non-listed property at 2% business use (witness classm.f8995.3: project $0, candidate $886.60); its reading of qualified improvement property without an election is right and is BUG-0303, fixed before this run. Differences on partial records withhold an answer the interview asks, so the interview cannot produce them. Triage executable-triage-v2 (triage/asset.json): 1571 of 1710 comparisons agree; on completed returns {"value": 2}.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The interface name does not define this result. Chosen: regular MACRS depreciation for 2025 on property placed in service before 2025, whether or not it is listed. It is zero after the last table year of the recovery period, because depreciation ends once the basis is recovered.

Ruling: representation; i4562 p. 9, Line 17: "enter the deductions for the current year". representation; every difference is on a partial or refused record: refusals sit on different lines and the withheld answers are ones the interview asks. No completed return differs. Triage executable-triage-v2 (triage/asset.json): 1603 of 1710 comparisons agree; on completed returns no difference.

### (d) — Recovery period under GDS for the asset class
Status: **AGREE**

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **DISAGREE**

Project:

```json
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"of": [{"input": "asset.prior_179"}, {"input": "asset.prior_bonus"}], "op": "sum"}}}], "op": "choose"}
```

Second transcription's note: Open: the printed (c) and 19(c) are both basis figures. Chosen: (c) is the depreciable basis the allowance percentage applies to, and 19(c) is that amount less the 2025 allowance. For earlier property, both are the unadjusted basis Pub. 946 applies the table rates to.

Ruling: representation; i4562 p. 11, Column (c): "multiply the cost or other basis of the property by the percentage of business/investment use". The project shows the amount before section 179 under this marker and the form's reduced column (c) at 19(c); the candidate nets section 179 here. The value difference is in this intermediate only and reaches no printed tax amount by a different route: both reach column (g) on the same basis. Triage executable-triage-v2 (triage/asset.json): 1168 of 1710 comparisons agree; on completed returns {"value": 64}.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate reads asset.bonus_same on returns that claim no allowance, an answer the source does not need there, so it is unknown where the project gives the amount. Differences on partial records withhold an answer the interview asks, so the interview cannot produce them. Triage executable-triage-v2 (triage/asset.json): 1562 of 1710 comparisons agree; on completed returns {"candidate-unknown": 4}.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: representation; i4562 p. 13, Line 25. representation; every difference is on a partial or refused record: refusals sit on different lines and the withheld answers are ones the interview asks. No completed return differs. Triage executable-triage-v2 (triage/asset.json): 1674 of 1710 comparisons agree; on completed returns no difference.

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

Ruling: representation; i4562 p. 5, Line 6: "Enter the elected section 179 cost of listed property in column (i) of line 26". representation; every difference is on a partial or refused record: refusals sit on different lines and the withheld answers are ones the interview asks. No completed return differs. Triage executable-triage-v2 (triage/asset.json): 1669 of 1710 comparisons agree; on completed returns no difference.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j: "Use lines 19a through 19j only for assets placed in service during the tax year beginning in 2025"; "For listed property, use Part V". The candidate shows an amount on the column for prior-year and listed property, where the project hides the line; it also reads bonus_same without need. Triage executable-triage-v2 (triage/asset.json): 929 of 1710 comparisons agree; on completed returns {"candidate-shows-skipped": 90, "candidate-unknown": 4}.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate reads asset.bonus_same on returns that claim no allowance, an answer the source does not need there, so it is unknown where the project gives the amount. Differences on partial records withhold an answer the interview asks, so the interview cannot produce them. Triage executable-triage-v2 (triage/asset.json): 1612 of 1710 comparisons agree; on completed returns {"candidate-unknown": 4}.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i4562 p. 9, Line 17. representation; every difference is on a partial or refused record: refusals sit on different lines and the withheld answers are ones the interview asks. No completed return differs. Triage executable-triage-v2 (triage/asset.json): 1591 of 1710 comparisons agree; on completed returns no difference.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}}], "op": "choose"}
```

Ruling: representation; i4562 p. 15, Column (h). representation; every difference is on a partial or refused record: refusals sit on different lines and the withheld answers are ones the interview asks. No completed return differs. Triage executable-triage-v2 (triage/asset.json): 1704 of 1710 comparisons agree; on completed returns no difference.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| asset.bonus_2025 | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| asset.s179_2025 | asset.h_low_listed, asset.h_s179_bad, asset.screen | asset.h_low_listed, asset.h_s179_bad, asset.screen |
| asset.mq_q4 | asset.h_low_listed, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_low_listed, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.mq_total | asset.h_low_listed, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_low_listed, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.cost179 | asset.h_low_listed, asset.h_pct_bad, asset.screen | asset.h_low_listed, asset.h_pct_bad, asset.screen |
| asset.dep_prior | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.h_low_listed, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_low_listed, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 14 | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 25 | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 26(i) | asset.h_low_listed, asset.h_s179_bad, asset.screen | asset.h_low_listed, asset.h_s179_bad, asset.screen |
| 19(c) | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 19(g) | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 17 | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 26(h) | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_low_listed, asset.h_outside, asset.h_pct_bad, asset.h_prior_bad, asset.h_s179_bad, asset.screen |

## Raw second transcription

```yaml
lines:
  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: asset.h_is2025
    printed: "(helper)"
    label: "Placed in service during the 2025 tax year"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.h_low_listed
    printed: "(helper)"
    label: "Listed property used 50% or less in a qualified business use (line 27, straight line over the ADS recovery period)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.listed, {const: true}]}
        - {op: test, le: [asset.pct, {const: 50, type: Count}]}
    note: "Line 27 requires the ADS straight line method, which this interface does not compute (no line 27 result is requested, and ADS is outside the screened scope). Such property is refused rather than computed."
  - id: asset.h_pct_bad
    printed: "(helper)"
    label: "Business use percentage is not a whole number from 1 to 100"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, lt: [asset.pct, {const: 1, type: Count}]}
        - {op: test, gt: [asset.pct, {const: 100, type: Count}]}
  - id: asset.h_cent
    printed: "(helper)"
    label: "One cent, used to express the percentage as money for the division"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: asset.h_pct_c
    printed: "(helper)"
    label: "Business/investment use percentage, expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}
  - id: asset.h_bus_cost
    printed: "(helper)"
    label: "Multiply the cost or other basis of the property by the percentage of business/investment use"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_c, whole: {param: sc.hundred_cents}, places: 2}
    refuses:
      - asset.screen
      - asset.h_low_listed
      - {when: asset.h_pct_bad, when_known: true}
  - id: asset.period
    printed: "(d)"
    label: "Column (d)—Recovery period"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}
    refuses: [asset.screen]
  - id: asset.h_outside
    printed: "(helper)"
    label: "The recovery period is not one the MACRS percentage tables here cover"
    type: Bool
    expr: {op: test, eq: [asset.period, {const: "outside"}]}
  - id: asset.h_s179_bad
    printed: "(helper)"
    label: "Elected section 179 cost is more than the business cost, or is elected for property not used more than 50% in the business"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - op: test
          any:
            - {op: test, gt: [asset.s179, asset.h_bus_cost]}
            - op: test
              all:
                - {op: test, gt: [asset.s179, {const: 0}]}
                - {op: test, le: [asset.pct, {const: 50, type: Count}]}
  - id: asset.h_after179
    printed: "(helper)"
    label: "Business/investment portion of the cost, less the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.s179}
    refuses:
      - {when: asset.h_s179_bad, when_known: true}
  - id: asset.h_prior_sum
    printed: "(helper)"
    label: "Section 179 amount and special depreciation allowance taken in the year placed in service"
    type: NonNegDollars
    expr: {op: sum, of: [asset.prior_179, asset.prior_bonus]}
  - id: asset.h_prior_bad
    printed: "(helper)"
    label: "Earlier section 179 amount and special allowance are more than the business cost"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: false}]}
        - {op: test, gt: [asset.h_prior_sum, asset.h_bus_cost]}
  - id: asset.h_prior_after
    printed: "(helper)"
    label: "Business/investment portion of the cost, less the section 179 deduction and special allowance of the year placed in service (unadjusted basis)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.h_prior_sum}
    refuses:
      - {when: asset.h_prior_bad, when_known: true}
  - id: asset.basis
    printed: "(c)"
    label: "Depreciable basis: the business/investment portion of the cost or other basis, less any credits and deductions allocable to the property (before any special depreciation allowance of 2025)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_after179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_prior_after
    refuses: [asset.screen, asset.h_low_listed]
    note: "Open: the printed (c) and 19(c) are both basis figures. Chosen: (c) is the depreciable basis the allowance percentage applies to, and 19(c) is that amount less the 2025 allowance. For earlier property, both are the unadjusted basis Pub. 946 applies the table rates to."
  - id: asset.h_no_bonus
    printed: "(helper)"
    label: "No special depreciation allowance in 2025: not placed in service in 2025, or elected out for the class"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [asset.h_is2025, {const: false}]}
        - {op: test, eq: [asset.bonus_choice, {const: "none"}]}
  - id: asset.h_bonus_100
    printed: "(helper)"
    label: "Qualified property acquired after January 19, 2025, with the 100% special depreciation allowance"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
        - {op: test, eq: [asset.after_jan19, {const: true}]}
  - id: asset.h_bonus_40
    printed: "(helper)"
    label: "Depreciable basis multiplied by 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: {param: sc.bonus_rate_40}}
  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "The special allowance choice is not the same for all property in the class placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.bonus_same, {const: false}]}
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Figure the special depreciation allowance by multiplying the depreciable basis of the property by the applicable percentage"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_no_bonus, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_no_bonus, {const: false}]}
              - {op: test, eq: [asset.h_bonus_100, {const: true}]}
          then: asset.basis
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_no_bonus, {const: false}]}
              - {op: test, eq: [asset.h_bonus_100, {const: false}]}
          then: asset.h_bonus_40
    refuses: [asset.screen, asset.h_low_listed, asset.h_outside, asset.h_bonus_mixed]
    note: "The interface name does not define this result. Chosen: this asset's 2025 special allowance whether or not it is listed, split between lines 14 and 25 below. Property acquired before January 20, 2025 is limited to 40%, so a 'full' answer for it gives 40%. All table recovery periods are 20 years or less."
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
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
  - id: asset.s179_2025
    printed: "(helper)"
    label: "The amount you elect to expense under section 179 for property placed in service during the tax year"
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
      - asset.h_low_listed
      - {when: asset.h_s179_bad, when_known: true}
    note: "The interface name does not define this result. Chosen: this asset's 2025 elected cost whether or not it is listed. It is the elected amount, before the Form 4562 lines 5 and 11 limits, which apply to the taxpayer rather than the item."
  - id: asset.f26i
    printed: "26(i)"
    label: "Column (i)—Elected section 179 cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
  - id: asset.col19c
    printed: "19(c)"
    label: "Column (c)—Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.bonus_2025}
  - id: asset.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.h_last_year
    printed: "(helper)"
    label: "Last year of recovery of the recovery period"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}
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
    label: "Applicable rate from the appropriate table, half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year]}
  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Applicable rate from the appropriate table, mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_year]}
  - id: asset.h_dep_hy
    printed: "(helper)"
    label: "Multiply column (c) by the applicable rate, half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_rate_hy}
  - id: asset.h_dep_mq
    printed: "(helper)"
    label: "Multiply column (c) by the applicable rate, mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_rate_mq}
  - id: asset.h_dep_figured
    printed: "(helper)"
    label: "Depreciation deduction under the convention that applies"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [mq.applies, {const: true}]}
          then: asset.h_dep_mq
        - guard: {op: test, eq: [mq.applies, {const: false}]}
          then: asset.h_dep_hy
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Depreciation deduction for property placed in service during the 2025 tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_dep_figured
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_low_listed, asset.h_outside]
    note: "The interface name does not define this result. Chosen: regular MACRS depreciation for 2025 on property placed in service in 2025, whether or not it is listed, excluding section 179 and the special allowance. Assumes a calendar tax year."
  - id: asset.macrs2025
    printed: "19(g)"
    label: "Column (g)—Depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.dep_2025
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "Applicable rate from the appropriate table, convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_year]}
  - id: asset.h_dep_prior_figured
    printed: "(helper)"
    label: "Multiply the basis for depreciation by the applicable rate for the year of recovery"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_rate_prior}
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Deduction for the current year for tangible property placed in service in tax years beginning before 2025 and depreciated under MACRS"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, gt: [asset.h_year, asset.h_last_year]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, le: [asset.h_year, asset.h_last_year]}
          then: asset.h_dep_prior_figured
    refuses: [asset.screen, asset.h_low_listed, asset.h_outside]
    note: "The interface name does not define this result. Chosen: regular MACRS depreciation for 2025 on property placed in service before 2025, whether or not it is listed. It is zero after the last table year of the recovery period, because depreciation ends once the basis is recovered."
  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.dep_prior
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
  - id: asset.h_dep_all
    printed: "(helper)"
    label: "Depreciation deduction for the property, whenever placed in service"
    type: NonNegDollars
    expr: {op: sum, of: [asset.dep_2025, asset.dep_prior]}
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Column (h)—Depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_dep_all
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
  - id: asset.h_q4
    printed: "(helper)"
    label: "Placed in service during the last 3 months of the tax year"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.quarter, {const: "q4"}]}
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance) of MACRS property placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_q4, {const: true}]}
          then: asset.h_after179
        - guard: {op: test, eq: [asset.h_q4, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_low_listed]
    note: "Per Pub. 946, this basis reflects the section 179 reduction and the personal-use part but not any special allowance. Listed property is included because nothing in the text excludes it from the mid-quarter test."
  - id: asset.mq_total
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance) of MACRS property placed in service during the entire tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_after179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_low_listed]
  - id: asset.h_cost179_counts
    printed: "(helper)"
    label: "Section 179 property placed in service during the tax year; qualified improvement property counts only if you elect to treat it as section 179 property"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - op: test
          any:
            - {op: test, ne: [asset.class, {const: "cqip"}]}
            - {op: test, gt: [asset.s179, {const: 0}]}
  - id: asset.cost179
    printed: "(helper)"
    label: "Total cost of section 179 property placed in service during the tax year (Form 4562, line 2), including listed property, and not just the amount for which you are making the election"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_cost179_counts, {const: true}]}
          then: asset.h_bus_cost
        - guard: {op: test, eq: [asset.h_cost179_counts, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_low_listed]
    note: "Open points. (1) The interface has no question on whether an item meets the section 179 property definition, so all unscreened 2025 property counts, except that qualified improvement property counts only when an amount is elected for it. (2) The more-than-50% use test is worded as a limit on the election, not in the definition, so property used 50% or less still counts if it is not listed. (3) Cost is the business-use cost, following line 6 column (b)."
```
