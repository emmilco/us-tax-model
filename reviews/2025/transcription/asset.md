# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 06abea8be894d6a6666394df8fc8bf29fbb0768fe574263e05739176f6147852 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 7f3ed487882a9681ff478d706ee7c99cdfb5dc2fa923e45b53bd1da1a045eb72 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d614d4d87b66cb4cd34e8dce8ac2569e3b7834748a6043d6487924f06650393e |
| printed lines compared | 16 |
| agree / disagree / missing | 2 / 14 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: This is read as the regular MACRS deduction for 2025 property. It is line 19(g) for non-listed property or line 26(h) for listed property, and excludes section 179 and the special allowance, which are separate interfaces. The convention comes from the return-level 40% mid-quarter test (mq.applies).

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/asset.json): 1557 of 1589 comparisons agree; on completed returns {"candidate-unknown": 7}.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The allowance rate is 100% for qualified property acquired after January 19, 2025, unless the 40% election is made. Property acquired after September 27, 2017, and before January 20, 2025, is limited to 40%. Property for which the taxpayer elected out gets 0%. The rate is applied to the depreciable basis, which is the business part of the cost minus section 179.

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/asset.json): 1483 of 1589 comparisons agree; on completed returns {"candidate-unknown": 7}.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; p946 p. 34: "the total depreciable bases of MACRS property you placed in service during the last 3 months". All differences are on refused or partial records; no completed return differs. Triage executable-triage-v2 (triage/asset.json): 1579 of 1589 comparisons agree; on completed returns no difference.

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

Ruling: representation; p946 p. 34, the same test over the entire year. All differences are on refused or partial records; no completed return differs. Triage executable-triage-v2 (triage/asset.json): 1547 of 1589 comparisons agree; on completed returns no difference.

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, "then": {"line": "(c)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}}, {"guard": {"args": [{"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Line 2 asks for the total cost of all section 179 property, not just elected property. The closed interface does not say whether property with a zero election is section 179 property, so only property with an election is counted. Unelected section 179 property is therefore left out of line 2. This is a limitation of the interface.

Ruling: model error; i4562 p. 4, Line 2: "Enter the total cost of all section 179 property you placed in service during the tax year (including the total cost of qualified real property that you elect to treat as section 179 property)". Only qualified real property needs an election to count; the candidate counts only property with an election, as its note concedes. Triage executable-triage-v2 (triage/asset.json): 888 of 1589 comparisons agree; on completed returns {"value": 118}.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: This is read as the current-year MACRS deduction for earlier-year property. It is line 17 for non-listed property or line 26(h) for listed property. Once the table's recovery period has ended, prior plus current depreciation cannot exceed basis, so zero is entered.

Ruling: representation; i4562 p. 9, Line 17: "enter the deductions for the current year". All differences are on refused or partial records; no completed return differs. Triage executable-triage-v2 (triage/asset.json): 1578 of 1589 comparisons agree; on completed returns no difference.

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
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}}], "op": "choose"}
```

Second transcription's note: Pub. 946 says table rates apply to the unadjusted basis each year. That basis is the cost minus any section 179 deduction and any special allowance taken, not reduced by MACRS depreciation. For earlier-year property it is rebuilt from the amounts claimed in the year placed in service. A changed business-use percentage is screened out.

Ruling: representation; i4562 p. 11, Column (c). The project shows the amount before section 179 under this marker and the reduced column (c) at 19(c); the candidate nets section 179 and, on the witnesses, also drops unelected property through its line 2 reading. Both reach column (g) on the project basis only through the project lines. Triage executable-triage-v2 (triage/asset.json): 831 of 1589 comparisons agree; on completed returns {"candidate-unknown": 7, "value": 129}.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/asset.json): 1479 of 1589 comparisons agree; on completed returns {"candidate-unknown": 6}.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error; i4562 p. 13, Line 25. The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/asset.json): 1559 of 1589 comparisons agree; on completed returns {"candidate-unknown": 1}.

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

Ruling: representation; i4562 p. 5, Line 6: "Enter the elected section 179 cost of listed property in column (i) of line 26". All differences are on refused or partial records; no completed return differs. Triage executable-triage-v2 (triage/asset.json): 1562 of 1589 comparisons agree; on completed returns no difference.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j: "Use lines 19a through 19j only for assets placed in service during the tax year beginning in 2025". The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/asset.json): 1571 of 1589 comparisons agree; on completed returns {"candidate-unknown": 6}.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/asset.json): 1564 of 1589 comparisons agree; on completed returns {"candidate-unknown": 6}.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i4562 p. 9, Line 17. All differences are on refused or partial records; no completed return differs. Triage executable-triage-v2 (triage/asset.json): 1583 of 1589 comparisons agree; on completed returns no difference.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}}], "op": "choose"}
```

Second transcription's note: Listed property is reported in Part V whatever the year it was placed in service. Qualified business use of 50% or less (line 27) is screened out, so only line 26 is computed.

Ruling: model error; i4562 p. 15, Column (h). The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/asset.json): 1582 of 1589 comparisons agree; on completed returns {"candidate-unknown": 1}.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| asset.bonus_2025 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| asset.s179_2025 | asset.h_s179_bad | asset.h_s179_bad |
| asset.mq_q4 | asset.h_s179_bad, asset.screen | asset.h_s179_bad, asset.screen |
| asset.mq_total | asset.h_s179_bad, asset.screen | asset.h_s179_bad, asset.screen |
| asset.cost179 | asset.screen | asset.screen |
| asset.dep_prior | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| 14 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| 25 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| 26(i) | asset.h_s179_bad | asset.h_s179_bad |
| 19(c) | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| 19(g) | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| 17 | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |
| 26(h) | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_s179_bad, asset.screen |

## Raw second transcription

```yaml
```yaml
lines:
  - id: asset.period
    printed: "(d)"
    label: "Recovery period. Determine the recovery period from the following table. See Pub. 946 for more information on the recovery period for MACRS property."
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}
    refuses: [asset.screen]

  - id: asset.h_outside
    printed: "(helper)"
    label: "The GDS recovery period of this property is not one of 3, 5, 7, 10, 15, 20 years or 15 years straight line (qualified improvement property)"
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
    label: "Business/investment use percentage, expressed as cents for the division by 100"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}

  - id: asset.h_buscost
    printed: "(helper)"
    label: "Multiply the cost or other basis of the property by the percentage of business/investment use"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_c, whole: {param: sc.hundred_cents}, places: 2}
    refuses: [asset.screen]
    note: "The percentage is a whole number from 1 to 100, so the ratio pct/100 is exact at 2 places; the product is rounded half-up to the cent."

  - id: asset.h_is2025
    printed: "(helper)"
    label: "Property placed in service during the tax year beginning in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}

  - id: asset.h_s179_bad
    printed: "(gate)"
    label: "Section 179 elected for 2025 property not used predominantly (more than 50%) in the business, or elected cost more than the business cost"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, gt: [asset.s179, {const: 0}]}
        - op: test
          any:
            - {op: test, le: [asset.pct, {const: 50, type: Count}]}
            - {op: test, gt: [asset.s179, asset.h_buscost]}

  - id: asset.s179_2025
    printed: "(helper)"
    label: "Elected cost (section 179) for property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.s179}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
    refuses: [asset.h_s179_bad]
    note: "The section 179 election applies only to property placed in service during the tax year. The amount is the elected cost (line 6(c) / 26(i)); the business income limit of line 11 is applied at the business level (line 12), and basis is reduced by the elected amount (reading chosen)."

  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service during the tax year (business use only), for line 2"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, gt: [asset.s179, {const: 0}]}
          then: asset.h_buscost
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is2025, {const: true}]}
                - {op: test, gt: [asset.s179, {const: 0}]}
          then: asset.h_zero
    note: "Line 2 asks for the total cost of all section 179 property, not just elected property. The closed interface does not say whether property with a zero election is section 179 property, so only property with an election is counted. Unelected section 179 property is therefore left out of line 2. This is a limitation of the interface."

  - id: asset.h_mq_basis
    printed: "(helper)"
    label: "Depreciable basis before any special depreciation allowance (business part of cost minus section 179)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_buscost, take: asset.s179_2025}

  - id: asset.mq_total
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance) of MACRS property placed in service during the entire tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_mq_basis}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}

  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance) of MACRS property placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.quarter, {const: "q4"}]}
          then: asset.h_mq_basis
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, ne: [asset.quarter, {const: "q4"}]}
          then: asset.h_zero

  - id: asset.h_bonus_mixed
    printed: "(gate)"
    label: "Special allowance choice is not the same for all property in the class placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.bonus_same, {const: false}]}

  - id: asset.h_bonus_forty
    printed: "(helper)"
    label: "40% special depreciation allowance: depreciable basis multiplied by 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_mq_basis, rate: {param: sc.bonus_rate_40}}

  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for qualified property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_zero
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
          then: asset.h_bonus_forty
    refuses: [asset.h_bonus_mixed, asset.h_outside]
    note: "The allowance rate is 100% for qualified property acquired after January 19, 2025, unless the 40% election is made. Property acquired after September 27, 2017, and before January 20, 2025, is limited to 40%. Property for which the taxpayer elected out gets 0%. The rate is applied to the depreciable basis, which is the business part of the cost minus section 179."

  - id: asset.h_basis_2025
    printed: "(helper)"
    label: "Basis for depreciation of 2025 property: business part of cost minus section 179 and special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_mq_basis, take: asset.bonus_2025}

  - id: asset.h_basis_prior179
    printed: "(helper)"
    label: "Business part of cost minus the section 179 deduction claimed in the year placed in service"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_buscost, take: asset.prior_179}

  - id: asset.h_basis_prior
    printed: "(helper)"
    label: "Unadjusted basis of earlier-year property: business part of cost minus section 179 and special depreciation allowance taken"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_basis_prior179, take: asset.prior_bonus}

  - id: asset.basis
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_basis_2025}
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_basis_prior}
    refuses: [asset.h_outside]
    note: "Pub. 946 says table rates apply to the unadjusted basis each year. That basis is the cost minus any section 179 deduction and any special allowance taken, not reduced by MACRS depreciation. For earlier-year property it is rebuilt from the amounts claimed in the year placed in service. A changed business-use percentage is screened out."

  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.listed, {const: false}]}, then: asset.bonus_2025}
        - {guard: {op: test, eq: [asset.listed, {const: true}]}, then: asset.h_zero}

  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year and used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.listed, {const: true}]}, then: asset.bonus_2025}
        - {guard: {op: test, eq: [asset.listed, {const: false}]}, then: asset.h_zero}

  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.listed, {const: true}]}, then: asset.s179_2025}
        - {guard: {op: test, eq: [asset.listed, {const: false}]}, then: asset.h_zero}

  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.basis
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is2025, {const: true}]}
                - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero

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
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}

  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "Table rate, year 1, half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year1]}

  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Table rate, year 1, mid-quarter convention for the quarter placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_year1]}

  - id: asset.h_dep_hy
    printed: "(helper)"
    label: "Multiply column (c) by the applicable rate from the appropriate table (half-year convention)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: asset.h_rate_hy}

  - id: asset.h_dep_mq
    printed: "(helper)"
    label: "Multiply column (c) by the applicable rate from the appropriate table (mid-quarter convention)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: asset.h_rate_mq}

  - id: asset.dep_2025
    printed: "(helper)"
    label: "MACRS depreciation deduction for property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: false}]}, then: asset.h_zero}
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: true}]}
          then: asset.h_dep_mq
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: false}]}
          then: asset.h_dep_hy
    note: "This is read as the regular MACRS deduction for 2025 property. It is line 19(g) for non-listed property or line 26(h) for listed property, and excludes section 179 and the special allowance, which are separate interfaces. The convention comes from the return-level 40% mid-quarter test (mq.applies)."

  - id: asset.h_ryear
    printed: "(helper)"
    label: "Year of the recovery period in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}

  - id: asset.h_last
    printed: "(helper)"
    label: "Last year of the recovery period in the percentage table"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}

  - id: asset.h_done
    printed: "(helper)"
    label: "The recovery period ended before 2025 (all depreciable basis recovered)"
    type: Bool
    expr: {op: test, gt: [asset.h_ryear, asset.h_last]}

  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "Table rate for the 2025 year of recovery, convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_ryear]}

  - id: asset.h_dep_prior_amt
    printed: "(helper)"
    label: "Multiply the unadjusted basis by the applicable rate from the appropriate table"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: asset.h_rate_prior}

  - id: asset.dep_prior
    printed: "(helper)"
    label: "MACRS deduction for the current year for property placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.h_is2025, {const: true}]}, then: asset.h_zero}
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.h_done, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.h_done, {const: false}]}
          then: asset.h_dep_prior_amt
    note: "This is read as the current-year MACRS deduction for earlier-year property. It is line 17 for non-listed property or line 26(h) for listed property. Once the table's recovery period has ended, prior plus current depreciation cannot exceed basis, so zero is entered."

  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.dep_2025
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is2025, {const: true}]}
                - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero

  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.dep_prior
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_is2025, {const: false}]}
                - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero

  - id: asset.h_dep_both
    printed: "(helper)"
    label: "Depreciation deduction for this property (current-year MACRS, whenever placed in service)"
    type: NonNegDollars
    expr: {op: sum, of: [asset.dep_2025, asset.dep_prior]}

  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [asset.listed, {const: true}]}, then: asset.h_dep_both}
        - {guard: {op: test, eq: [asset.listed, {const: false}]}, then: asset.h_zero}
    note: "Listed property is reported in Part V whatever the year it was placed in service. Qualified business use of 50% or less (line 27) is screened out, so only line 26 is computed."
```
```
