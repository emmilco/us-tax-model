# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3e64eab45774239eda671795c98976ca929d033e56fc5fd3c40ebc6b1bb60898 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 344c75937b6aba10f80c6d238ccbaf82e173f9148dad2efca9ca78459f09a7ad |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 52a30454db4b0c144b97840cf9ff3c457473d885960981880109b47eafbb1433 |
| printed lines compared | 16 |
| agree / disagree / missing | 2 / 14 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Interface meaning inferred as the regular MACRS depreciation of 2025 property, listed or not, parallel to bonus_2025 and s179_2025.

Ruling: model error; The reply declares asset.period (column (d)) as refusing on its own helper asset.h_outside, which tests asset.period, so every line that reads the recovery period is a reference cycle and the candidate is unknown wherever it reaches it; p946 Table B-1 gives the period by class with no condition on itself, and the project refuses a class outside the tool at asset.outside. The candidate also asks asset.bonus_same of property whose bonus_choice is none, which the source does not need (i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year"). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,177 of 1,761 agree; 569 candidate-unknown, 15 project-refuses; on completed returns: 150 candidate-unknown.

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

Second transcription's note: Property acquired after September 27, 2017 and before January 20, 2025 is limited to 40% whether 'full' or 'forty' is answered; 100% applies only to property acquired after January 19, 2025 without the 40% election.

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate asks asset.bonus_same of property whose bonus_choice is none. The other differences are partial records withholding an answer the interview asks of the asset (placed, class, not179, listed) and cited refusals (asset.screened, asset.listed_low). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,670 of 1,761 agree; 52 project-unknown, 39 candidate-unknown; on completed returns: 9 candidate-unknown.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; p946 p. 34, "the total depreciable bases of MACRS property you placed in service during the last 3 months". The only differences are partial records withholding placed, class or not179, which the interview asks of the asset; no completed return differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,708 of 1,761 agree; 53 project-unknown; on completed returns: none.

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

Second transcription's note: Per Pub. 946, the mid-quarter test basis reflects the section 179 reduction and the personal-use part but not the special allowance.

Ruling: representation; p946 p. 34, the same test over the entire year. The only differences are cited refusals (asset.screened, asset.listed_low) and partial records withholding class, not179 or listed; no completed return differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,700 of 1,761 agree; 46 project-unknown, 15 project-refuses; on completed returns: none.

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

Second transcription's note: Line 2 says 'total cost'; line 6 column (b) is 'Cost (business use only)'. Chose the business-use cost. Section 179 property is counted whether or not an amount is elected, as the Worksheet 1 footnote directs.

Ruling: model error; i4562 p. 4, Line 2, "Enter the total cost of all section 179 property you placed in service during the tax year (including the total cost of qualified real property that you elect to treat as section 179 property)"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business". The candidate counts qualified improvement property with no election (stage14.asset.qip, project $0, candidate $30,000) and 2025 property used 50% or less. The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). The project line is the package's change (asset.is_section179 now requires not179 No); every completed difference is the candidate's, none traces to a project error. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,612 of 1,761 agree; 75 value, 31 project-unknown, 30 candidate-unknown, 13 project-refuses; on completed returns: 8 candidate-unknown, 6 value. Completed-return value differences (project/candidate): stage14.asset.qip sc[desk].asset[fitout] $0.00/$30,000.00; and 5 partial records built on those bases with the same pairs.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: Interface meaning inferred as the current-year MACRS deduction for earlier-year property, listed or not.

Ruling: model error; i4562 p. 9, Line 17, "enter the deductions for the current year". The reply declares asset.period (column (d)) as refusing on its own helper asset.h_outside, which tests asset.period, so every line that reads the recovery period is a reference cycle and the candidate is unknown wherever it reaches it; p946 Table B-1 gives the period by class with no condition on itself, and the project refuses a class outside the tool at asset.outside. No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,185 of 1,761 agree; 573 candidate-unknown, 3 project-refuses; on completed returns: 114 candidate-unknown.

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
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"of": [{"input": "asset.prior_179"}, {"input": "asset.prior_bonus"}], "op": "sum"}}}], "op": "choose"}
```

Ruling: model error; i4562 p. 11, Column (c). The values are representation: the project shows at this marker the business basis before section 179 and the special allowance (its label) and the reduced basis at 19(c); the candidate nets them here, so every completed value difference is an asset with an election or a special allowance (or fully expensed, candidate $0). The model error is the unknowns: the candidate asks asset.bonus_same of property whose bonus_choice is none (i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year"). executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 917 of 1,761 agree; 525 value, 217 candidate-unknown, 66 project-unknown, 18 candidate-refuses, 18 project-refuses; on completed returns: 103 value, 13 candidate-unknown. Completed-return value differences (project/candidate): classm.f4952.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.f8960.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.g28.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.sd.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.u1250.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.clcw26.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.f8880.2.deepseek sc[biz_a].asset[item_2] $39,115.00/$0.00; classm.eic.3.deepseek sc[biz_a].asset[item_1] $19,658.00/$8,740.00; classm.asset.1 sc[biz_b].asset[item_2] $46,295.40/$27,777.24; classm.asset.1 sc[biz_b].asset[item_1] $17,923.00/$8,292.60; classm.f8880.2 sc[biz_a].asset[item_2] $39,115.00/$0.00; classm.f8960.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.f8995.3 sc[biz_b].asset[item_1] $886.60/$531.96; classm.g28.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.ira.2 sc[biz_a].asset[item_1] $10,295.00/$0.00; classm.sd.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.sdtw.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.sli.4 sc[biz_a].asset[item_2] $46,663.00/$42,099.00; classm.ssb.4 sc[biz_a].asset[item_2] $46,663.00/$42,099.00; classm.u1250.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.clcw26.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.f8962.4 sc[biz_a].asset[item_2] $2,482.83/$1,489.70; mutation.t2.f8962_months_asset3 sc[biz_a].asset[item_1] $100.00/$0.00; stage14.asset.bonus_100 sc[desk].asset[saw] $20,000.00/$0.00; stage14.asset.bonus_40_before sc[desk].asset[pc] $10,000.00/$6,000.00; stage14.asset.bonus_40_elected sc[desk].asset[pc] $10,000.00/$6,000.00; stage14.asset.s179 sc[desk].asset[saw] $12,000.00/$7,000.00; stage14.asset.prior_179_full sc[desk].asset[saw] $10,000.00/$0.00; stage14.asset.prior_bonus_full sc[desk].asset[pc] $20,000.00/$0.00; stage14.asset.qip_elected sc[desk].asset[fitout] $30,000.00/$20,000.00; stage14.asset.s179_partial_use sc[d].asset[pc] $1,800.00/$800.00; stage14.asset.mq_bonus40 sc[d].asset[pc] $10,000.00/$6,000.00; stage14.asset.prior_179_bonus sc[d].asset[van] $16,000.00/$10,000.00; stage14.asset.listed_and_not sc[d].asset[cam] $2,400.00/$0.00; stage14.asset.listed_and_not sc[d].asset[pc] $2,000.00/$0.00; stage14.asset.listed_forty sc[d].asset[cam] $2,400.00/$1,200.00; stage14.asset.listed_forty sc[d].asset[pc] $2,000.00/$0.00; stage14.s179.election_and_carryover sc[d].asset[saw] $2,000.00/$0.00; stage14.ho.with_179 sc[h].asset[desk] $1,000.00/$0.00; stage14.s179.partial_election_carryover sc[d].asset[saw] $2,000.00/$1,000.00; f2.t101.credit_disallowed_eic_zero sc[biz_a].asset[item_2] $46,663.00/$42,099.00; generated 150 sc[biz_a].asset[item_2] $12,597.81/$6,295.77; generated 162 sc[biz_a].asset[item_1] $1,125.45/$675.27; generated 172 sc[biz_a].asset[item_1] $3,318.79/$1,991.27; generated 172 sc[biz_a].asset[item_2] $8,316.83/$0.00; generated 238 sc[biz_a].asset[item_1] $24,612.92/$0.00; generated 254 sc[biz_a].asset[item_1] $44,022.81/$0.00; generated 261 sc[biz_a].asset[item_1] $44,990.34/$0.00; generated 293 sc[biz_a].asset[item_1] $19,367.17/$0.00; generated 293 sc[biz_a].asset[item_2] $4,213.91/$2,528.35; generated 449 sc[biz_a].asset[item_2] $100.13/$0.00; generated 482 sc[biz_b].asset[item_1] $10,989.43/$10,691.55; and 51 partial records built on those bases with the same pairs.

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

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". The candidate asks asset.bonus_same of property whose bonus_choice is none. The other differences are partial records withholding an answer the interview asks of the asset (placed, class, not179, listed) and cited refusals (asset.screened, asset.listed_low). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,651 of 1,761 agree; 63 candidate-unknown, 47 project-unknown; on completed returns: 9 candidate-unknown.

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

Ruling: representation; i4562 p. 14, Line 25, "Enter on line 25 your total special depreciation allowance for all qualified listed property". The candidate's unknowns are records withholding asset.listed, which the interview asks of every asset, on refused or incomplete returns; no completed return differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,730 of 1,761 agree; 27 candidate-unknown, 4 project-unknown; on completed returns: none.

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

Ruling: representation; i4562 p. 5, Line 6, "Enter the elected section 179 cost of listed property in column (i) of line 26". The only differences are records withholding asset.listed, asked of every asset, on refused or incomplete returns; no completed return differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,735 of 1,761 agree; 26 candidate-unknown; on completed returns: none.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j, "Use lines 19a through 19j only for assets placed in service during the tax year beginning in 2025". The candidate asks asset.bonus_same of property whose bonus_choice is none (i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year"). The other differences are partial records withholding an answer the interview asks of the asset (placed, class, not179, listed) and cited refusals (asset.screened, asset.listed_low). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,682 of 1,761 agree; 37 project-unknown, 29 candidate-unknown, 13 project-refuses; on completed returns: 9 candidate-unknown.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j. The reply declares asset.period (column (d)) as refusing on its own helper asset.h_outside, which tests asset.period, so every line that reads the recovery period is a reference cycle and the candidate is unknown wherever it reaches it; p946 Table B-1 gives the period by class with no condition on itself, and the project refuses a class outside the tool at asset.outside. The candidate also asks asset.bonus_same of property whose bonus_choice is none, which the source does not need (i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year"). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,226 of 1,761 agree; 522 candidate-unknown, 13 project-refuses; on completed returns: 139 candidate-unknown.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Line 17. The reply declares asset.period (column (d)) as refusing on its own helper asset.h_outside, which tests asset.period, so every line that reads the recovery period is a reference cycle and the candidate is unknown wherever it reaches it; p946 Table B-1 gives the period by class with no condition on itself, and the project refuses a class outside the tool at asset.outside. No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,228 of 1,761 agree; 531 candidate-unknown, 2 project-refuses; on completed returns: 112 candidate-unknown.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error; i4562 p. 15, Column (h). The reply declares asset.period (column (d)) as refusing on its own helper asset.h_outside, which tests asset.period, so every line that reads the recovery period is a reference cycle and the candidate is unknown wherever it reaches it; p946 Table B-1 gives the period by class with no condition on itself, and the project refuses a class outside the tool at asset.outside. No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,658 of 1,761 agree; 101 candidate-unknown, 2 project-refuses; on completed returns: 13 candidate-unknown.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| asset.bonus_2025 | asset.h_bonus_mixed, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_s179_bad, asset.screen |
| asset.s179_2025 | asset.h_s179_bad | asset.h_s179_bad |
| asset.mq_q4 | asset.h_s179_bad, asset.screen | asset.h_s179_bad, asset.screen |
| asset.mq_total | asset.h_s179_bad, asset.screen | asset.h_s179_bad, asset.screen |
| asset.cost179 | asset.screen | asset.screen |
| asset.dep_prior | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| (d) | asset.h_outside | asset.h_outside |
| (c) | asset.h_bonus_mixed, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 14 | asset.h_bonus_mixed, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_s179_bad, asset.screen |
| 25 | asset.h_bonus_mixed, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_s179_bad, asset.screen |
| 26(i) | asset.h_s179_bad | asset.h_s179_bad |
| 19(c) | asset.h_bonus_mixed, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 19(g) | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 17 | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen |
| 26(h) | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.h_prior_bad, asset.h_s179_bad, asset.screen |

## Raw second transcription

```yaml
```yaml
lines:
  - id: asset.h_outside
    printed: "(helper)"
    label: "The property's GDS recovery period is not one of the 3-, 5-, 7-, 10-, 15- or 20-year classes figured with the MACRS percentage tables"
    type: Bool
    expr: {op: test, eq: [asset.period, {const: "outside"}]}
  - id: asset.period
    printed: "(d)"
    label: "Recovery period (Pub. 946, Appendix B, Tables B-1 and B-2)"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}
    refuses: [asset.h_outside]
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
  - id: asset.h_hundred
    printed: "(helper)"
    label: "One hundred cents"
    type: NonNegDollars
    expr: {op: param, ref: sc.hundred_cents}
  - id: asset.h_pct_cents
    printed: "(helper)"
    label: "Business/investment use percentage, held as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}
  - id: asset.h_bus_cost
    printed: "(helper)"
    label: "Multiply the cost or other basis of the property by the percentage of business/investment use"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_cents, whole: asset.h_hundred, places: 2}
    refuses: [asset.screen]
  - id: asset.h_is2025
    printed: "(helper)"
    label: "Placed in service during the tax year beginning in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.h_s179_bad
    printed: "(helper)"
    label: "The elected section 179 cost is more than the business cost, or the property is not section 179 property, or it is not used more than 50% in the business"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, gt: [asset.s179, {const: 0}]}
        - op: test
          any:
            - {op: test, gt: [asset.s179, asset.h_bus_cost]}
            - {op: test, eq: [asset.not179, {const: true}]}
            - {op: test, le: [asset.pct, {const: 50, type: Count}]}
    note: "The instructions require more than 50% business use for the election and allow only section 179 property; an elected amount violating these, or above the business cost (line 6 column (b)), is treated as an inconsistency that refuses."
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Elected section 179 cost of this property placed in service in 2025 (line 6(c), or line 26(i) for listed property)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    refuses:
      - {when: asset.h_s179_bad, when_known: true}
  - id: asset.h_after179
    printed: "(helper)"
    label: "Business/investment portion of cost reduced by the section 179 expense deduction (depreciable basis for the special allowance)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.s179_2025}
  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service during the tax year (Worksheet 1, line 1; Form 4562, line 2)"
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
    note: "Line 2 says 'total cost'; line 6 column (b) is 'Cost (business use only)'. Chose the business-use cost. Section 179 property is counted whether or not an amount is elected, as the Worksheet 1 footnote directs."
  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "The special allowance choice differs within the property's recovery period class"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.bonus_same, {const: false}]}
  - id: asset.h_bonus_forty
    printed: "(helper)"
    label: "Depreciable basis multiplied by 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after179, rate: {param: sc.bonus_rate_40}}
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for this qualified property placed in service in 2025 (depreciable basis times the applicable percentage)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
              - {op: test, eq: [asset.after_jan19, {const: true}]}
          then: asset.h_after179
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
    refuses: [asset.h_bonus_mixed]
    note: "Property acquired after September 27, 2017 and before January 20, 2025 is limited to 40% whether 'full' or 'forty' is answered; 100% applies only to property acquired after January 19, 2025 without the 40% election."
  - id: asset.h_basis2025
    printed: "(helper)"
    label: "Basis for depreciation of 2025 property: business cost less section 179 deduction and special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after179, take: asset.bonus_2025}
  - id: asset.h_prior_red
    printed: "(helper)"
    label: "Section 179 deduction and special allowance taken in the year placed in service"
    type: NonNegDollars
    expr: {op: sum, of: [asset.prior_179, asset.prior_bonus]}
  - id: asset.h_prior_bad
    printed: "(helper)"
    label: "Earlier section 179 deduction and special allowance exceed the business cost"
    type: Bool
    expr: {op: test, gt: [asset.h_prior_red, asset.h_bus_cost]}
  - id: asset.h_basis_prior
    printed: "(helper)"
    label: "Unadjusted basis of earlier-year property: business cost less section 179 deduction and special allowance claimed"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.h_prior_red}
    refuses:
      - {when: asset.h_prior_bad, when_known: true}
  - id: asset.basis
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_basis2025
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_basis_prior
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
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost (listed property)"
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
    label: "Basis for depreciation (business/investment use only), property placed in service in 2025"
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
            any:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
  - id: asset.mq_total
    printed: "(helper)"
    label: "Depreciable basis (before any special depreciation allowance) of MACRS property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_after179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    note: "Per Pub. 946, the mid-quarter test basis reflects the section 179 reduction and the personal-use part but not the special allowance."
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
          then: asset.h_after179
        - guard:
            op: test
            any:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, ne: [asset.quarter, {const: "q4"}]}
          then: asset.h_zero
  - id: asset.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.h_last
    printed: "(helper)"
    label: "Last year of recovery for the recovery period"
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
    label: "Table rate, half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year]}
  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Table rate, mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_year]}
  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "Table rate, convention used in the year placed in service"
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
  - id: asset.h_dep_prior
    printed: "(helper)"
    label: "Multiply the unadjusted basis by the applicable rate (convention used when placed in service)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: asset.h_rate_prior}
  - id: asset.h_dep
    printed: "(helper)"
    label: "MACRS depreciation deduction for this property for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: false}]}
          then: asset.h_dep_hy
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: true}]}
          then: asset.h_dep_mq
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, le: [asset.h_year, asset.h_last]}
          then: asset.h_dep_prior
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, gt: [asset.h_year, asset.h_last]}
          then: asset.h_zero
    note: "The convention for 2025 property is taken from the return-level mid-quarter test (mq.applies). Property past its last recovery year is fully depreciated and gets zero."
  - id: asset.dep_2025
    printed: "(helper)"
    label: "MACRS depreciation for this property placed in service in 2025 (listed or not)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_dep
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    note: "Interface meaning inferred as the regular MACRS depreciation of 2025 property, listed or not, parallel to bonus_2025 and s179_2025."
  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction (property other than listed property placed in service in 2025)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.dep_2025
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
  - id: asset.dep_prior
    printed: "(helper)"
    label: "MACRS depreciation for this property placed in service in tax years beginning before 2025 (listed or not)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_dep
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_zero
    note: "Interface meaning inferred as the current-year MACRS deduction for earlier-year property, listed or not."
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
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction (listed property used more than 50% in a qualified business use)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_dep
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
```
```
