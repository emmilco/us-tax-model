# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 98a932f4b419d32b838d18b08c53ed58d1c599cbbb51148505547e23cc378ed4 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a413fa53ac13ebe968a805afbc8c962ce627d4f513bc1fc0f3b64129793373c8 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 885639a0718f865e47c02a6977f6ac48d5b6df18b6a7b446823729d88f053675 |
| printed lines compared | 16 |
| agree / disagree / missing | 2 / 14 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- asset.asset.h_business_cost: part 'asset.pct' is not money
- asset.asset.h_business_cost: whole operand is not money

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

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
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, "then": {"line": "(c)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

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
{"expression": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: scope; all differences are on refused or partial records; no completed return differs. Triage executable-triage-v2 (triage/asset.deepseek.json): 1783 of 1864 comparisons agree; on completed returns no difference.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}, {"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}], "test": "le"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"input": "asset.pct"}, "places": 2, "whole": {"const": 100, "type": "Count"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: part 'asset.pct' is not money"}, {"line": "asset.h_business_cost", "message": "asset.asset.h_business_cost: whole operand is not money"}]}
```

Ruling: model error on the declaration; the line or a line it depends on fails the host check, so it was not executed. This adjudicates the declaration, not the tax reading. Triage executable-triage-v2 (triage/asset.deepseek.json): candidate-invalid on all 1864 records; this adjudicates the declaration, not the tax reading.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.screen | asset.h_bonus_mixed, asset.screen |
| asset.bonus_2025 | asset.h_bonus_mixed, asset.screen | asset.h_bonus_mixed, asset.screen |
| asset.s179_2025 | asset.screen | asset.screen |
| asset.mq_q4 | asset.screen | asset.screen |
| asset.mq_total | asset.screen | asset.screen |
| asset.cost179 | asset.screen | asset.screen |
| asset.dep_prior | asset.screen | asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.h_bonus_mixed, asset.screen | asset.h_bonus_mixed, asset.screen |
| 14 | asset.h_bonus_mixed, asset.screen | asset.h_bonus_mixed, asset.screen |
| 25 | asset.h_bonus_mixed, asset.screen | asset.h_bonus_mixed, asset.screen |
| 26(i) | asset.screen | asset.screen |
| 19(c) | asset.h_bonus_mixed, asset.screen | asset.h_bonus_mixed, asset.screen |
| 19(g) | asset.h_bonus_mixed, asset.screen | asset.h_bonus_mixed, asset.screen |
| 17 | asset.screen | asset.screen |
| 26(h) | asset.h_bonus_mixed, asset.screen | asset.h_bonus_mixed, asset.screen |

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
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_placed2025, {const: true}]}
          then: asset.h_basis_current
        - guard: {op: test, eq: [asset.h_placed2025, {const: false}]}
          then: asset.h_basis_prior
    refuses: [asset.screen]
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property placed in service during the tax year (other than listed property)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.h_is_listed, {const: false}]}
          then: asset.bonus_2025
    refuses: [asset.screen, asset.h_bonus_mixed]
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.h_is_listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_bonus_mixed]
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.h_is_listed, {const: false}]}
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
              - {op: test, eq: [asset.h_placed2025, {const: true}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_basis_current
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_placed2025, {const: true}]}
                - {op: test, eq: [asset.listed, {const: false}]}
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
              - {op: test, eq: [asset.h_placed2025, {const: true}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_regular_current
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_placed2025, {const: true}]}
                - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS depreciation on property placed in service in prior years"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_prior_placed, {const: true}]}
              - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_regular_prior
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_prior_placed, {const: true}]}
                - {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction for listed property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_listed, {const: true}]}
          then: asset.h_listed_regular
        - guard: {op: test, eq: [asset.h_is_listed, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Total 2025 depreciation and section 179 deduction for this property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_placed2025, {const: true}]}
          then: asset.h_dep_2025_sum
        - guard: {op: test, eq: [asset.h_placed2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_bonus_mixed]
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for 2025 for this property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_placed2025, {const: true}]}
          then: asset.h_bonus_after
        - guard: {op: test, eq: [asset.h_placed2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen, asset.h_bonus_mixed]
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 cost elected for this property in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_placed2025, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.h_placed2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
    note: "The slice supplies the elected section 179 amount; the business-income limitation and allocation are applied in the enclosing Schedule C Form 4562 summary."
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis placed in service in the fourth quarter for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_placed2025, {const: true}]}
              - {op: test, eq: [asset.h_q4, {const: true}]}
          then: asset.h_after179_current
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [asset.h_placed2025, {const: true}]}
                - {op: test, eq: [asset.h_q4, {const: true}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.mq_total
    printed: "(helper)"
    label: "Total depreciable basis placed in service in 2025 for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_placed2025, {const: true}]}
          then: asset.h_after179_current
        - guard: {op: test, eq: [asset.h_placed2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.cost179
    printed: "(helper)"
    label: "Business cost of section 179 property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_placed2025, {const: true}]}
          then: asset.h_business_cost
        - guard: {op: test, eq: [asset.h_placed2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Current-year depreciation for this property placed in service before 2025"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_regular_prior}
    refuses: [asset.screen]
  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: asset.h_rate_40
    printed: "(helper)"
    label: "Forty percent rate"
    type: Rate
    expr: {op: param, ref: sc.bonus_rate_40}
  - id: asset.h_conv_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: asset.h_year1
    printed: "(helper)"
    label: "Recovery year 1"
    type: Count
    expr: {op: param, ref: sc.year1}
  - id: asset.h_placed2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.h_prior_placed
    printed: "(helper)"
    label: "Placed in service before 2025"
    type: Bool
    expr: {op: test, eq: [asset.h_placed2025, {const: false}]}
  - id: asset.h_is_listed
    printed: "(helper)"
    label: "Listed property"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: true}]}
  - id: asset.h_not_listed
    printed: "(helper)"
    label: "Not listed property"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: false}]}
  - id: asset.h_q4
    printed: "(helper)"
    label: "Placed in service in the fourth quarter"
    type: Bool
    expr: {op: test, eq: [asset.quarter, {const: "q4"}]}
  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "Special depreciation choice is not the same for all property in the class"
    type: Bool
    expr:
      op: test
      not:
        op: test
        eq: [asset.bonus_same, {const: true}]
  - id: asset.h_business_cost
    printed: "(helper)"
    label: "Business/investment cost before section 179 and special depreciation"
    type: NonNegDollars
    expr:
      op: prorate
      amount: asset.cost
      part: asset.pct
      whole: {const: 100, type: Count}
      places: 2
  - id: asset.h_after179_current
    printed: "(helper)"
    label: "Business cost reduced by section 179 elected for 2025"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_business_cost, take: asset.s179}
  - id: asset.h_after179_prior
    printed: "(helper)"
    label: "Business cost reduced by section 179 claimed in the placed-in-service year"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_business_cost, take: asset.prior_179}
  - id: asset.h_basis_current
    printed: "(helper)"
    label: "Basis for depreciation for a 2025 asset after section 179 and special depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after179_current, take: asset.bonus_2025}
  - id: asset.h_basis_prior
    printed: "(helper)"
    label: "Basis for depreciation for a prior-year asset after prior section 179 and special depreciation"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after179_prior, take: asset.prior_bonus}
  - id: asset.h_bonus_40
    printed: "(helper)"
    label: "Special depreciation allowance at 40 percent"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after179_current, rate: asset.h_rate_40}
  - id: asset.h_bonus_100
    printed: "(helper)"
    label: "Special depreciation allowance at 100 percent"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_after179_current}
  - id: asset.h_bonus_after
    printed: "(helper)"
    label: "Special depreciation allowance before limiting to 2025 placements"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.after_jan19, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
          then: asset.h_bonus_100
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.after_jan19, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "forty"}]}
          then: asset.h_bonus_40
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.after_jan19, {const: false}]}
              - {op: test, ne: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_bonus_40
  - id: asset.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention by quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}
  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "MACRS rate for 2025 asset under half-year convention"
    type: Rate
    expr:
      op: keyed_lookup
      table: macrs_gds
      keys: [asset.period, asset.h_conv_hy, asset.h_year1]
  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "MACRS rate for 2025 asset under mid-quarter convention"
    type: Rate
    expr:
      op: keyed_lookup
      table: macrs_gds
      keys: [asset.period, asset.h_qconv, asset.h_year1]
  - id: asset.h_dep_hy
    printed: "(helper)"
    label: "MACRS depreciation for 2025 asset under half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_current, rate: asset.h_rate_hy}
  - id: asset.h_dep_mq
    printed: "(helper)"
    label: "MACRS depreciation for 2025 asset under mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_current, rate: asset.h_rate_mq}
  - id: asset.h_mq_threshold
    printed: "(helper)"
    label: "40 percent of total mid-quarter test basis"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.mq_total, rate: asset.h_rate_40}
  - id: asset.h_mq_applies
    printed: "(helper)"
    label: "Mid-quarter convention applies"
    type: Bool
    expr: {op: test, gt: [sc.mq_q4, asset.h_mq_threshold]}
  - id: asset.h_current_macrs
    printed: "(helper)"
    label: "Regular MACRS depreciation for a 2025 asset"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_mq_applies, {const: true}]}
          then: asset.h_dep_mq
        - guard: {op: test, eq: [asset.h_mq_applies, {const: false}]}
          then: asset.h_dep_hy
  - id: asset.h_recovery_year
    printed: "(helper)"
    label: "Recovery year in 2025 for the placed-in-service year"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.h_prior_rate
    printed: "(helper)"
    label: "MACRS rate for a prior-year asset"
    type: Rate
    expr:
      op: keyed_lookup
      table: macrs_gds
      keys: [asset.period, asset.prior_conv, asset.h_recovery_year]
  - id: asset.h_prior_macrs
    printed: "(helper)"
    label: "Regular MACRS depreciation for a prior-year asset"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_basis_prior, rate: asset.h_prior_rate}
  - id: asset.h_regular_current
    printed: "(helper)"
    label: "Regular MACRS depreciation for a 2025 asset, zero if not placed in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_placed2025, {const: true}]}
          then: asset.h_current_macrs
        - guard: {op: test, eq: [asset.h_placed2025, {const: false}]}
          then: asset.h_zero
  - id: asset.h_regular_prior
    printed: "(helper)"
    label: "Regular MACRS depreciation for a prior-year asset, zero if placed in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_prior_placed, {const: true}]}
          then: asset.h_prior_macrs
        - guard: {op: test, eq: [asset.h_prior_placed, {const: false}]}
          then: asset.h_zero
  - id: asset.h_listed_regular
    printed: "(helper)"
    label: "Regular MACRS depreciation for listed property"
    type: NonNegDollars
    expr: {op: sum, of: [asset.h_regular_current, asset.h_regular_prior]}
  - id: asset.h_dep_2025_sum
    printed: "(helper)"
    label: "Section 179, special depreciation allowance and regular depreciation for a 2025 asset"
    type: NonNegDollars
    expr: {op: sum, of: [asset.s179_2025, asset.bonus_2025, asset.h_regular_current]}
```
