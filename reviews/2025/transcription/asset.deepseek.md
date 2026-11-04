# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 52a30454db4b0c144b97840cf9ff3c457473d885960981880109b47eafbb1433 |
| printed lines compared | 16 |
| agree / disagree / missing | 1 / 15 / 0 |
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
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j. The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). Its other unknowns withhold asset.screen on refused or incomplete records. No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,622 of 1,761 agree; 76 candidate-unknown, 32 project-refuses, 30 project-unknown, 1 candidate-refuses; on completed returns: 9 candidate-unknown.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: For property placed in service in 2025 and acquired before January 20, 2025, the allowance is 40%; full is 100% only when acquired after January 19, 2025.

Ruling: model error; i4562 p. 5, Line 14, "The special depreciation allowance applies only for the first year the property is placed in service". The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,671 of 1,761 agree; 63 candidate-unknown, 22 project-unknown, 3 candidate-refuses, 2 project-refuses; on completed returns: 6 candidate-unknown.

### asset.s179_2025 — Section 179 elected on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 5, Line 6, Column (c), Elected cost. The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). The one value difference is on a partial record. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,648 of 1,761 agree; 108 candidate-unknown, 3 candidate-refuses, 1 project-unknown, 1 value; on completed returns: 8 candidate-unknown.

### asset.mq_q4 — Mid-quarter test basis, fourth quarter
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "asset.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; p946 p. 34, "the total depreciable bases of MACRS property you placed in service during the last 3 months". The differences are records withholding screen, not179, class or owned answers and screen refusals, all on refused or incomplete returns; no completed return differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,693 of 1,761 agree; 58 candidate-unknown, 7 project-unknown, 3 candidate-refuses; on completed returns: none.

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; p946 p. 34. The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,639 of 1,761 agree; 57 candidate-unknown, 34 project-unknown, 30 project-refuses, 1 candidate-refuses; on completed returns: 8 candidate-unknown.

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 4, Line 2, "(including the total cost of qualified real property that you elect to treat as section 179 property)". The candidate counts qualified improvement property with no election (stage14.asset.qip, project $0, candidate $30,000). The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,585 of 1,761 agree; 75 value, 57 candidate-unknown, 30 project-unknown, 13 project-refuses, 1 candidate-refuses; on completed returns: 8 candidate-unknown, 6 value. Completed-return value differences (project/candidate): stage14.asset.qip sc[desk].asset[fitout] $0.00/$30,000.00; and 5 partial records built on those bases with the same pairs.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Line 17. The candidate has no branch for property past its recovery period: it looks the rate up for a year the table does not have (for example ["y5","hy",17] on classm.f4952.2.deepseek) and is unknown, where the project enters $0 because the recovery period has ended. No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,461 of 1,761 agree; 290 candidate-unknown, 6 project-unknown, 2 candidate-refuses, 2 project-refuses; on completed returns: 40 candidate-unknown.

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
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}}], "op": "choose"}
```

Second transcription's note: Read as the basis for depreciation after section 179 and the special allowance for the year placed; line 19(c) reports it only for 2025 nonlisted GDS property.

Ruling: model error; i4562 p. 11, Column (c). The values are representation, as for the Claude reply: the project shows the basis before section 179 and the special allowance here and the reduced basis at 19(c). The model error is the unknowns. The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 925 of 1,761 agree; 536 value, 215 candidate-unknown, 67 project-unknown, 18 project-refuses; on completed returns: 99 value, 12 candidate-unknown. Completed-return value differences (project/candidate): classm.f4952.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.f8960.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.g28.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.sd.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.u1250.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.clcw26.1.deepseek sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.f8880.2.deepseek sc[biz_a].asset[item_2] $39,115.00/$0.00; classm.eic.3.deepseek sc[biz_a].asset[item_1] $19,658.00/$8,740.00; classm.asset.1 sc[biz_b].asset[item_2] $46,295.40/$27,777.24; classm.asset.1 sc[biz_b].asset[item_1] $17,923.00/$8,292.60; classm.f8880.2 sc[biz_a].asset[item_2] $39,115.00/$0.00; classm.f8960.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.g28.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.ira.2 sc[biz_a].asset[item_1] $10,295.00/$0.00; classm.sd.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.sdtw.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.sli.4 sc[biz_a].asset[item_2] $46,663.00/$42,099.00; classm.ssb.4 sc[biz_a].asset[item_2] $46,663.00/$42,099.00; classm.u1250.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; classm.clcw26.1 sc[biz_a].asset[item_1] $46,128.00/$0.00; mutation.t2.f8962_months_asset3 sc[biz_a].asset[item_1] $100.00/$0.00; stage14.asset.bonus_100 sc[desk].asset[saw] $20,000.00/$0.00; stage14.asset.bonus_40_before sc[desk].asset[pc] $10,000.00/$6,000.00; stage14.asset.bonus_40_elected sc[desk].asset[pc] $10,000.00/$6,000.00; stage14.asset.s179 sc[desk].asset[saw] $12,000.00/$7,000.00; stage14.asset.prior_179_full sc[desk].asset[saw] $10,000.00/$0.00; stage14.asset.prior_bonus_full sc[desk].asset[pc] $20,000.00/$0.00; stage14.asset.qip_elected sc[desk].asset[fitout] $30,000.00/$20,000.00; stage14.asset.s179_partial_use sc[d].asset[pc] $1,800.00/$800.00; stage14.asset.mq_bonus40 sc[d].asset[pc] $10,000.00/$6,000.00; stage14.asset.prior_179_bonus sc[d].asset[van] $16,000.00/$10,000.00; stage14.asset.listed_and_not sc[d].asset[cam] $2,400.00/$0.00; stage14.asset.listed_and_not sc[d].asset[pc] $2,000.00/$0.00; stage14.asset.listed_forty sc[d].asset[cam] $2,400.00/$1,200.00; stage14.asset.listed_forty sc[d].asset[pc] $2,000.00/$0.00; stage14.s179.election_and_carryover sc[d].asset[saw] $2,000.00/$0.00; stage14.ho.with_179 sc[h].asset[desk] $1,000.00/$0.00; stage14.s179.partial_election_carryover sc[d].asset[saw] $2,000.00/$1,000.00; f2.t101.credit_disallowed_eic_zero sc[biz_a].asset[item_2] $46,663.00/$42,099.00; generated 150 sc[biz_a].asset[item_2] $12,597.81/$6,295.77; generated 162 sc[biz_a].asset[item_1] $1,125.45/$675.27; generated 172 sc[biz_a].asset[item_1] $3,318.79/$1,991.27; generated 172 sc[biz_a].asset[item_2] $8,316.83/$0.00; generated 238 sc[biz_a].asset[item_1] $24,612.92/$0.00; generated 254 sc[biz_a].asset[item_1] $44,022.81/$0.00; generated 261 sc[biz_a].asset[item_1] $44,990.34/$0.00; generated 293 sc[biz_a].asset[item_1] $19,367.17/$0.00; generated 293 sc[biz_a].asset[item_2] $4,213.91/$2,528.35; generated 449 sc[biz_a].asset[item_2] $100.13/$0.00; generated 482 sc[biz_b].asset[item_1] $10,989.43/$10,691.55; and 49 partial records built on those bases with the same pairs.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 5, Line 14. The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,650 of 1,761 agree; 90 candidate-unknown, 16 project-unknown, 3 candidate-refuses, 2 project-refuses; on completed returns: 6 candidate-unknown.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: representation; i4562 p. 14, Line 25. All differences are records withholding screen or listed, or screen refusals, on refused or incomplete returns; no completed return differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,668 of 1,761 agree; 84 candidate-unknown, 6 project-unknown, 3 candidate-refuses; on completed returns: none.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: representation; i4562 p. 5, Line 6, "Enter the elected section 179 cost of listed property in column (i) of line 26". All differences are on refused or incomplete records; no completed return differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,669 of 1,761 agree; 89 candidate-unknown, 3 candidate-refuses; on completed returns: none.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j. The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,633 of 1,761 agree; 61 candidate-unknown, 37 project-unknown, 29 project-refuses, 1 candidate-refuses; on completed returns: 8 candidate-unknown.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j. The candidate asks asset.not179 of 2025 property used 50% or less in the business and of qualified improvement property with no election (classm.f8962.4 item_2 at 21%, classm.f8995.3 item_1 at 2%, stage14.asset.low_use_nonlisted, the fitout of stage14.asset.qip). The answer bears only on whether the property is section 179 property for Form 4562 line 2 and the election (p946 p. 17, "Land and land improvements do not qualify as section 179 property"; i4562 p. 3, Part I, "used predominantly (more than 50%) in your trade or business"), so the source does not need it for this line; the project asks it only for a 2025 asset used more than 50% or with an election (BUG-0370, checked here). No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,627 of 1,761 agree; 81 candidate-unknown, 29 project-refuses, 23 project-unknown, 1 candidate-refuses; on completed returns: 9 candidate-unknown.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Line 17. The candidate has no branch for property past its recovery period and looks up a rate the table does not have, so it is unknown where the project enters $0. No value differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,485 of 1,761 agree; 273 candidate-unknown, 2 candidate-refuses, 1 project-refuses; on completed returns: 40 candidate-unknown.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i4562 p. 15, Column (h). All differences are records withholding screen, cost or listed, or screen refusals, on refused or incomplete returns; no completed return differs. executable-triage-v2 (scratch rerun of triage.py's triage() with the witness cap lifted, /tmp/adj-bklg-asset-sc-scveh/triage/asset.deepseek.json; 1,495 fixtures, 500 generated returns seed 20261026, 830 partial records): 1,679 of 1,761 agree; 72 candidate-unknown, 5 project-unknown, 3 candidate-refuses, 2 project-refuses; on completed returns: none.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.screen | asset.screen |
| asset.bonus_2025 | asset.screen | asset.screen |
| asset.s179_2025 | asset.screen | asset.screen |
| asset.mq_q4 | asset.screen | asset.screen |
| asset.mq_total | asset.screen | asset.screen |
| asset.cost179 | asset.screen | asset.screen |
| asset.dep_prior | asset.screen | asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.screen | asset.screen |
| 14 | asset.screen | asset.screen |
| 25 | asset.screen | asset.screen |
| 26(i) | asset.screen | asset.screen |
| 19(c) | asset.screen | asset.screen |
| 19(g) | asset.screen | asset.screen |
| 17 | asset.screen | asset.screen |
| 26(h) | asset.screen | asset.screen |

## Raw second transcription

```yaml
lines:
  - id: asset.period
    printed: "(d)"
    label: "Recovery period"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}
    refuses: [asset.screen]
  - id: asset.basis
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_basis_dep}
    note: "Read as the basis for depreciation after section 179 and the special allowance for the year placed; line 19(c) reports it only for 2025 nonlisted GDS property."
    refuses: [asset.screen]
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.bonus_2025
    refuses: [asset.screen]
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for listed property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
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
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_basis_current
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
    refuses: [asset.screen]
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
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_regular_2025
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS depreciation for property placed in service before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, ne: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_regular_prior
        - guard: {op: test, eq: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, ne: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction for listed property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.listed, {const: true}]}
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
          then: asset.h_regular_2025
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.listed, {const: true}]}
              - {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_regular_prior
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Depreciation for 2025 for property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.placed, {const: "y2025"}]}
          then: asset.h_regular_2025
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
              - {op: test, eq: [asset.after_jan19, {const: true}]}
          then: asset.h_after_s179
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
              - {op: test, eq: [asset.after_jan19, {const: false}]}
          then: asset.h_forty_base
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.bonus_choice, {const: "forty"}]}
          then: asset.h_forty_base
    note: "For property placed in service in 2025 and acquired before January 20, 2025, the allowance is 40%; full is 100% only when acquired after January 19, 2025."
    refuses: [asset.screen]
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 deduction for 2025 for this property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.not179, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.not179, {const: false}]}
          then: asset.s179
    refuses: [asset.screen]
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis of 2025 property placed in service in the fourth quarter, before the special allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.quarter, {const: "q4"}]}
          then: asset.h_after_s179
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, ne: [asset.quarter, {const: "q4"}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.mq_total
    printed: "(helper)"
    label: "Depreciable basis of 2025 property, before the special allowance"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.placed, {const: "y2025"}]}
          then: asset.h_after_s179
    refuses: [asset.screen]
  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.not179, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.placed, {const: "y2025"}]}
              - {op: test, eq: [asset.not179, {const: false}]}
          then: asset.h_business_cost
    refuses: [asset.screen]
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Depreciation for 2025 for property placed in service before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_regular_prior
        - guard: {op: test, eq: [asset.placed, {const: "y2025"}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: asset.h_one_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: asset.h_cost_times_pct
    printed: "(helper)"
    label: "Cost times business-use percentage"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.cost, count: asset.pct}
  - id: asset.h_business_cost
    printed: "(helper)"
    label: "Business/investment portion of cost"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.h_cost_times_pct, part: asset.h_one_cent, whole: {param: sc.hundred_cents}, places: 2}
  - id: asset.h_after_s179
    printed: "(helper)"
    label: "Business cost reduced by 2025 section 179 deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_business_cost, take: asset.s179_2025}
  - id: asset.h_basis_current
    printed: "(helper)"
    label: "Basis for depreciation for property placed in service in 2025"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after_s179, take: asset.bonus_2025}
  - id: asset.h_prior_after_s179
    printed: "(helper)"
    label: "Business cost reduced by prior-year section 179 deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_business_cost, take: asset.prior_179}
  - id: asset.h_basis_prior
    printed: "(helper)"
    label: "Basis for depreciation for property placed in service before 2025"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_prior_after_s179, take: asset.prior_bonus}
  - id: asset.h_basis_dep
    printed: "(helper)"
    label: "Basis for depreciation"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.placed, {const: "y2025"}]}
          then: asset.h_basis_current
        - guard: {op: test, ne: [asset.placed, {const: "y2025"}]}
          then: asset.h_basis_prior
  - id: asset.h_forty_base
    printed: "(helper)"
    label: "Forty percent special depreciation allowance base"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after_s179, rate: {param: sc.bonus_rate_40}}
  - id: asset.h_conv_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: asset.h_conv_mq
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}
  - id: asset.h_recovery_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "MACRS rate, half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_conv_hy, asset.h_recovery_year]}
  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "MACRS rate, mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_conv_mq, asset.h_recovery_year]}
  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "MACRS rate for prior-year property using its placed-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_recovery_year]}
  - id: asset.h_dep_current_hy
    printed: "(helper)"
    label: "2025 depreciation, half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_current, rate: asset.h_rate_hy}
  - id: asset.h_dep_current_mq
    printed: "(helper)"
    label: "2025 depreciation, mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_current, rate: asset.h_rate_mq}
  - id: asset.h_regular_2025
    printed: "(helper)"
    label: "2025 regular MACRS depreciation for property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [mq.applies, {const: true}]}
          then: asset.h_dep_current_mq
        - guard: {op: test, eq: [mq.applies, {const: false}]}
          then: asset.h_dep_current_hy
  - id: asset.h_regular_prior
    printed: "(helper)"
    label: "2025 regular MACRS depreciation for property placed in service before 2025"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_prior, rate: asset.h_rate_prior}
```
