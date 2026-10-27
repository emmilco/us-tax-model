# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | d1d2413d5db1621beca7e98e866058cf44b4b3f46294a33e66c0bf2f026cceac |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a5906492e14561e0cba8e8b6072f530f37c0f9eeaa5e29c43336a2ff5c69b4d6 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 016358a1ec33902f8aa13a91658676dd71689874d310b2ead345f0ba5a761fb7 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0f1df70975dae8df7b1ffdb285589a51a9f6b67c79822b31fe1d630b33de9de6 |
| printed lines compared | 16 |
| agree / disagree / missing | 2 / 14 / 0 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The interface name is not defined by the text. I read it as regular MACRS depreciation of 2025 property, not counting the section 179 deduction or the special allowance, for listed and nonlisted property alike.

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 2,023 of 2,045 comparisons agree (1,730 of 1,749 in scope); 19 candidate-unknown; 2 candidate-refuses; 1 project-refuses. No value differs: the candidate's MACRS (mid-quarter test from person.mq_q4 x 5 against person.mq_total x 2, as p946 p. 34, mid-quarter convention: "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year ... are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year") gives the project's amount on every reached record. The candidate-unknown records withhold asset.bonus_same on 2025 property whose asset.bonus_choice is none (every one, checked by rebuilding each witness): the candidate's model-declared gate h_bonus_mixed reads it whatever the choice, but with the class elected out the allowance is zero, the interview does not ask it (evaluated with the full profile's targets), and a class mixing elections is still caught on the property whose choice is full or forty, where the project asks it; the candidate requires an answer the source does not need. Witnesses: stage14.asset.mq_not without bonus_same (project $1,200.00, candidate unknown), classm.f8889.2.deepseek without bonus_same ($6,797.32). The 2 candidate-refuses records (stage14.asset.refuse_bonus_mixed without after_jan19 / bonus_choice) are the cited bonus-mixed refusal the project also makes on the complete base record; only the order of questions differs (scope). The project-refuses record (stage14.asset.refuse_listed_low without screen) is the cited asset.listed_low refusal (i4562 p. 14): scope. Project stands.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Total special allowance for this asset, listed or not. Lines 14 and 25 give the split.

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,982 of 2,045 comparisons agree (1,970 of 2,031 in scope); 37 project-unknown; 24 candidate-unknown; 2 candidate-refuses. No value differs. The candidate-unknown records withhold asset.bonus_same on 2025 property whose asset.bonus_choice is none (every one, checked by rebuilding each witness): the candidate's model-declared gate h_bonus_mixed reads it whatever the choice, but with the class elected out the allowance is zero, the interview does not ask it (evaluated with the full profile's targets), and a class mixing elections is still caught on the property whose choice is full or forty, where the project asks it; the candidate requires an answer the source does not need. (24 records, e.g. stage14.asset.mq_not without bonus_same.) The 37 project-unknown records withhold asset.placed, which the interview asks of every asset (asked on all 30 whose base is not refused) and the project's guard reads first; the candidate's guards reach zero through bonus_choice none without it: representation. The 2 candidate-refuses records (stage14.asset.refuse_bonus_mixed without after_jan19 / bonus_choice) are the cited bonus-mixed refusal the project also makes on the complete base record; only the order of questions differs (scope). Project stands.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The second guard is written so that it holds when the property is not 2025 property. For such property the quarter answer is not needed.

Ruling: representation; p946 p. 34, mid-quarter convention: "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year ... are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 2,004 of 2,045 comparisons agree (2,004 of 2,045 in scope); 41 project-unknown. No value differs; every difference is a partial record withholding asset.placed, which the interview asks of every asset (35 of 41 asked, the rest on refused bases), and which the candidate does not need when the quarter is not October to December. Observed equivalence on the sample; project stands.

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; Caution: the basis "reflects the reduction in basis for amounts expensed under section 179 ... However, it does not reflect any reduction in basis for any special depreciation allowance". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 2,044 of 2,045 comparisons agree (2,029 of 2,029 in scope); 1 project-refuses. The only difference (stage14.asset.refuse_listed_low without screen) is the project's cited asset.listed_low refusal (i4562 p. 14-15), where the candidate waits for the screen; the two expressions differ only in a redundant guard. Project stands.

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"line": "(c)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Worksheet 1 counts all eligible section 179 property, not only the amount elected, and includes listed property. Under the text, qualified improvement property is section 179 property only if the election is made. The interface cannot tell whether it was, so I counted it like other property.

Ruling: representation; i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 2,040 of 2,045 comparisons agree (2,038 of 2,043 in scope); 5 project-unknown. No value differs: both count the business cost of 2025 property used more than 50%. The 5 project-unknown records withhold asset.placed, asked of every asset (3 asked; 2 on refused bases); the candidate reaches zero from the percentage first. Project stands.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The interface name is not defined by the text. I read it as current-year MACRS on property placed in service before 2025, listed or not.

Ruling: representation; i4562 p. 9, Line 17: "For tangible property placed in service in tax years beginning before 2025 and depreciated under MACRS ... enter the deductions for the current year". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 2,045 of 2,045 comparisons agree (2,045 of 2,045 in scope); no difference: the candidate's restated line 17 agrees on every record (observed on the sample, including 11 listed assets placed before 2025). Project stands.

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
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}
```

Second transcription's note: The printed marker (c) was supplied without its meaning. I read it as the business/investment-use cost (cost times the percentage in column (c)), which is the starting point for line 19 column (c) and line 26 column (e). The ratio pct/100 is exact to 2 places.

Ruling: representation; i4562 p. 11, Column (c): "multiply the cost or other basis of the property by the percentage of business/investment use". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 2,044 of 2,045 comparisons agree (2,030 of 2,030 in scope); 1 project-refuses. The candidate prorates to 2 places, the project to 6; asset.pct is a whole percent, so pct/100 is exact at 2 places and the products are equal. The single difference (stage14.asset.refuse_listed_low without screen) is the project's cited asset.listed_low refusal (i4562 p. 14-15): scope. Project stands.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; f4562 p. 1, line 14: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,487 of 2,045 comparisons agree (1,476 of 2,030 in scope); 340 value; 108 project-unknown; 106 candidate-unknown; 2 candidate-refuses; 2 project-refuses. All 340 value differences are on entries where the project's line is not reported (asset.on_19 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.bonus_2025 filtered by asset.listed (sc.f14, sc.f25_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.asset.1 item_1 placed before 2025 ($2,130.00 against $0.00), classm.asset.2 item_1 listed ($19,315.00 against $0.00): representation. The candidate-unknown records withhold asset.bonus_same on 2025 property whose asset.bonus_choice is none (every one, checked by rebuilding each witness): the candidate's model-declared gate h_bonus_mixed reads it whatever the choice, but with the class elected out the allowance is zero, the interview does not ask it (evaluated with the full profile's targets), and a class mixing elections is still caught on the property whose choice is full or forty, where the project asks it; the candidate requires an answer the source does not need. (21 records, all bonus_choice none; e.g. stage14.asset.mq_not without bonus_same.) The other candidate-unknown records on asset.listed or asset.placed withhold answers the interview asks of every asset (the full-profile evaluation asks them wherever the base return is not refused); the project needs them too, for shown_when and its sums: representation; the project-unknown records are all on entries where the project line is not reported (shown_when false) and withhold answers that only the hidden value reads; no printed amount: representation. The 2 candidate-refuses records (stage14.asset.refuse_bonus_mixed without after_jan19 / bonus_choice) are the cited bonus-mixed refusal the project also makes on the complete base record; only the order of questions differs (scope). The 2 project-refuses records are the cited asset.bonus_mixed refusal: scope. Project stands.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: representation; i4562 p. 13, Line 25: "If you placed in service certain qualified listed property during the tax year, you may be able to deduct the special depreciation allowance". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,096 of 2,045 comparisons agree (1,096 of 2,032 in scope); 644 value; 226 project-unknown; 66 candidate-unknown; 13 project-refuses. All 644 value differences are on entries where the project's line is not reported (asset.on_26_2025 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.bonus_2025 filtered by asset.listed (sc.f25_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.f8889.4.deepseek item_2 not listed ($48,573.00 against $0.00), classm.asset.1 item_1 placed before 2025 ($2,130.00 against $0.00). The 13 project-refuses records are the cited asset.bonus_mixed refusal (i4562 p. 7): scope. The project-unknown records are all on entries where the project line is not reported (shown_when false) and withhold answers that only the hidden value reads; no printed amount: representation. The 3 candidate-unknown records withholding bonus_same on listed 2025 property with bonus_choice none repeat the model error ruled at line 14; the rest withhold asset.listed or asset.placed, which the interview asks of every asset where the base is not refused: representation. Project stands.

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

Ruling: representation; i4562 p. 5, Line 6: "Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,681 of 2,045 comparisons agree (1,681 of 2,045 in scope); 232 value; 72 candidate-unknown; 60 project-unknown. All 232 value differences are on entries where the project's line is not reported (asset.on_26_2025 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.s179_2025 filtered by asset.listed (sc.f6, sc.f29_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.asset.2 item_1 not listed ($3,189.00 against $0.00), classm.asset.3 item_1 ($7,925.00 against $0.00). The 60 project-unknown records withhold asset.s179 on entries where the line is not reported; the 72 candidate-unknown records on asset.listed or asset.placed withhold answers the interview asks of every asset (the full-profile evaluation asks them wherever the base return is not refused); the project needs them too, for shown_when and its sums: representation. Project stands.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: This is the depreciation basis of 2025 property. Listed property reports the same figure in line 26 column (e) rather than on line 19, but the value is computed either way.

Ruling: model error; i4562 p. 11, Column (c): "multiply the cost or other basis of the property by the percentage of business/investment use" ... "Any special depreciation allowance included on line 14"; i4562 p. 9, Lines 19a Through 19j: "Use lines 19a through 19j only for assets placed in service during the tax year beginning in 2025"; p. 9: "For listed property, use Part V.". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,431 of 2,045 comparisons agree (1,404 of 2,013 in scope); 361 value; 163 project-unknown; 85 candidate-unknown; 3 project-refuses; 2 candidate-refuses. All 361 value differences are on entries where the project's line is not reported (asset.on_19 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". No Schedule C sum reads 19(c); asset.ub, which feeds the MACRS amounts, is compared through 19(g) and asset.dep_2025; no printed amount differs. Witnesses: classm.f8889.2.deepseek item_1 listed and placed before 2025 ($38,615.00 against $0.00), classm.asset.1 item_1 placed before 2025 ($3,195.00 against $0.00). The candidate-unknown records withhold asset.bonus_same on 2025 property whose asset.bonus_choice is none (every one, checked by rebuilding each witness): the candidate's model-declared gate h_bonus_mixed reads it whatever the choice, but with the class elected out the allowance is zero, the interview does not ask it (evaluated with the full profile's targets), and a class mixing elections is still caught on the property whose choice is full or forty, where the project asks it; the candidate requires an answer the source does not need. (23 records.) The other candidate-unknown records on asset.listed or asset.placed withhold answers the interview asks of every asset (the full-profile evaluation asks them wherever the base return is not refused); the project needs them too, for shown_when and its sums: representation; the project-unknown records are all on entries where the project line is not reported (shown_when false) and withhold answers that only the hidden value reads; no printed amount: representation. The 2 candidate-refuses records (stage14.asset.refuse_bonus_mixed without after_jan19 / bonus_choice) are the cited bonus-mixed refusal the project also makes on the complete base record; only the order of questions differs (scope). The 3 project-refuses records are the cited asset.listed_low and asset.bonus_mixed refusals: scope. Project stands.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j: "Use lines 19a through 19j only for assets placed in service during the tax year beginning in 2025"; p. 9: "For listed property, use Part V."; p946 p. 34, mid-quarter convention: "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year ... are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,198 of 2,045 comparisons agree (923 of 1,539 in scope); 418 project-unknown; 229 project-refuses; 141 value; 57 candidate-unknown; 2 candidate-refuses. All 141 value differences are on entries where the project's line is not reported (asset.on_19 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.dep_2025 by recovery period (sc.f19_*), which agrees in value on every record, which triage compares separately, so no printed amount differs. Witnesses: classm.asset.1 item_1 placed before 2025 ($363.27 against $0.00), classm.asset.4 item_1 ($5.90 against $0.00). The 229 project-refuses records are hidden values reached through the mid-quarter test, which reads a vehicle's cited scveh.low_use refusal (i4562 p. 14-15), or the asset's cited asset.listed_low / asset.bonus_mixed: the return refuses there anyway: scope. The project-unknown records are all on entries where the project line is not reported (shown_when false) and withhold answers that only the hidden value reads; no printed amount: representation. The candidate-unknown records withhold asset.bonus_same on 2025 property whose asset.bonus_choice is none (every one, checked by rebuilding each witness): the candidate's model-declared gate h_bonus_mixed reads it whatever the choice, but with the class elected out the allowance is zero, the interview does not ask it (evaluated with the full profile's targets), and a class mixing elections is still caught on the property whose choice is full or forty, where the project asks it; the candidate requires an answer the source does not need. (17 records.) The 2 candidate-refuses records (stage14.asset.refuse_bonus_mixed without after_jan19 / bonus_choice) are the cited bonus-mixed refusal the project also makes on the complete base record; only the order of questions differs (scope). Project stands.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i4562 p. 9, Line 17: "For tangible property placed in service in tax years beginning before 2025 and depreciated under MACRS ... enter the deductions for the current year"; p. 9: "For listed property, use Part V.". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 723 of 2,045 comparisons agree (723 of 2,033 in scope); 948 value; 304 project-unknown; 58 candidate-unknown; 12 project-refuses. All 948 value differences are on entries where the project's line is not reported (asset.on_17 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.dep_prior filtered by asset.listed (sc.f17) and asset.dep_listed (sc.f26_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.f8889.2.deepseek item_2, a 2025 asset ($6,797.32 against $0.00), classm.f8889.4.deepseek item_1 ($1,168.88 against $0.00). The 12 project-refuses records are the cited asset.listed_low refusal (i4562 p. 14-15): scope. The project-unknown records are all on entries where the project line is not reported (shown_when false) and withhold answers that only the hidden value reads; no printed amount: representation; the 58 candidate-unknown records on asset.listed or asset.placed withhold answers the interview asks of every asset (the full-profile evaluation asks them wherever the base return is not refused); the project needs them too, for shown_when and its sums: representation. Project stands.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}}], "op": "choose"}
```

Ruling: model error; i4562 p. 15, Column (h): "For property used more than 50% in a qualified business use (line 26) and placed in service after 1986, figure column (h) by following the instructions for line 19, column (g)". Triage executable-triage-v1 (triage/asset.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 716 of 2,045 comparisons agree (704 of 1,751 in scope); 516 value; 475 project-unknown; 282 project-refuses; 56 candidate-unknown. All 516 value differences are on entries where the project's line is not reported (asset.listed false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.dep_listed filtered by asset.listed (sc.f26_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.f8889.2.deepseek item_2 not listed ($6,797.32 against $0.00), classm.f8889.4.deepseek item_1 ($2,045.69 against $0.00). The 282 project-refuses records are project refusals are the cited gates asset.listed_low (i4562 p. 14-15), asset.bonus_mixed (p. 7), asset.s179_bad (p. 3, p. 5), asset.screened (pp. 8-12) and, through the mid-quarter test, scveh.low_use (p. 14-15): scope. The project-unknown records are all on entries where the project line is not reported (shown_when false) and withhold answers that only the hidden value reads; no printed amount: representation. 2 candidate-unknown records withhold bonus_same on listed 2025 property with bonus_choice none, the model error ruled at line 14; the rest withhold asset.listed or asset.placed, which the interview asks of every asset where the base is not refused: representation. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.bonus_2025 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.mq_q4 | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.mq_total | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| asset.cost179 | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen |
| asset.dep_prior | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen |
| (c) | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen |
| 14 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 25 | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 19(c) | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 19(g) | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |
| 17 | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen | asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.screen |
| 26(h) | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen | asset.h_bonus_mixed, asset.h_listed_low, asset.h_outside, asset.h_pct_bad, asset.h_s179_bad, asset.screen |

## Raw second transcription

```yaml
```yaml
lines:
  - id: asset.period
    printed: "(d)"
    label: "Column (d)—Recovery period. Determine the recovery period from the following table (classification by class life; see the Table of Class Lives and Recovery Periods in Pub. 946)"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}

  - id: asset.h_outside
    printed: "(helper)"
    label: "The recovery period is not one of the 3-, 5-, 7-, 10-, 15- or 20-year GDS classes this worksheet computes"
    type: Bool
    expr: {op: test, eq: [asset.period, {const: "outside"}]}

  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: asset.h_cent
    printed: "(helper)"
    label: "One cent per percentage point"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}

  - id: asset.h_hundred
    printed: "(helper)"
    label: "One hundred percent, in cents"
    type: NonNegDollars
    expr: {op: param, ref: sc.hundred_cents}

  - id: asset.h_pct_c
    printed: "(helper)"
    label: "Percentage of business/investment use, in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}

  - id: asset.h_pct_bad
    printed: "(helper)"
    label: "The business use percentage is not between 1 and 100"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [asset.pct, {const: 0, type: Count}]}
        - {op: test, gt: [asset.pct, {const: 100, type: Count}]}

  - id: asset.h_over_half
    printed: "(helper)"
    label: "Used predominantly (more than 50%) in your trade or business"
    type: Bool
    expr: {op: test, gt: [asset.pct, {const: 50, type: Count}]}

  - id: asset.h_listed_low
    printed: "(helper)"
    label: "Listed property used 50% or less in a qualified business use (line 27: straight line over the ADS recovery period; no section 179 deduction or special depreciation allowance)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.listed, {const: true}]}
        - {op: test, eq: [asset.h_over_half, {const: false}]}

  - id: asset.basis
    printed: "(c)"
    label: "Multiply the cost or other basis of the property by the percentage of business/investment use"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_c, whole: asset.h_hundred, places: 2}
    refuses: [asset.screen, asset.h_pct_bad, asset.h_listed_low, asset.h_outside]
    note: "The printed marker (c) was supplied without its meaning. I read it as the business/investment-use cost (cost times the percentage in column (c)), which is the starting point for line 19 column (c) and line 26 column (e). The ratio pct/100 is exact to 2 places."

  - id: asset.h_is2025
    printed: "(helper)"
    label: "Placed in service during the tax year beginning in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}

  - id: asset.h_s179_2025
    printed: "(helper)"
    label: "Section 179 expense deduction elected for this property in 2025 (line 6(c), or line 26 column (i) for listed property)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero

  - id: asset.h_s179_bad
    printed: "(helper)"
    label: "The elected section 179 cost is more than the business cost, or the property is not used more than 50% in the business"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [asset.h_s179_2025, asset.basis]}
        - op: test
          all:
            - {op: test, gt: [asset.h_s179_2025, {const: 0}]}
            - {op: test, eq: [asset.h_over_half, {const: false}]}

  - id: asset.h_after179
    printed: "(helper)"
    label: "Depreciable basis: business/investment portion of the cost less the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.h_s179_2025}
    refuses: [asset.h_s179_bad]
    note: "The text says to reduce by the 'section 179 expense deduction'. I used the amount elected for this property, not a share of the line 12 amount after the business income limit."

  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "The special depreciation allowance choice is not the same for all property in this class placed in service in 2025 (election out is made for the whole class)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.bonus_same, {const: false}]}

  - id: asset.h_rate40
    printed: "(helper)"
    label: "40% special depreciation allowance"
    type: Rate
    expr: {op: param, ref: sc.bonus_rate_40}

  - id: asset.h_bonus_full
    printed: "(helper)"
    label: "100% special depreciation allowance (qualified property acquired after January 19, 2025)"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_after179}

  - id: asset.h_bonus_forty
    printed: "(helper)"
    label: "40% special depreciation allowance (elected 40%, or acquired before January 20, 2025)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_after179, rate: asset.h_rate40}

  - id: asset.h_bonus_amt
    printed: "(helper)"
    label: "Figure the special depreciation allowance by multiplying the depreciable basis of the property by the applicable percentage"
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
          then: asset.h_bonus_full
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, ne: [asset.bonus_choice, {const: "none"}]}
              - op: test
                not:
                  op: test
                  all:
                    - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
                    - {op: test, eq: [asset.after_jan19, {const: true}]}
          then: asset.h_bonus_forty
    refuses: [asset.h_bonus_mixed]
    note: "Property acquired before January 20, 2025 and placed in service in 2025 gets 40% whether the answer is 'full' or 'forty'. All supported recovery periods (20 years or less) are qualified property."

  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_bonus_amt

  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year and used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_bonus_amt
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero

  - id: asset.f26i
    printed: "26(i)"
    label: "Column (i)—Elected section 179 cost (listed property used more than 50% in a qualified business use)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_s179_2025
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero

  - id: asset.h_ub
    printed: "(helper)"
    label: "Basis for depreciation of 2025 property: business cost less section 179 deduction less any special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_after179, take: asset.h_bonus_amt}

  - id: asset.col19c
    printed: "19(c)"
    label: "Column (c)—Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_ub
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    note: "This is the depreciation basis of 2025 property. Listed property reports the same figure in line 26 column (e) rather than on line 19, but the value is computed either way."

  - id: asset.h_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}

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
    label: "Applicable rate from the MACRS percentage table (half-year convention)"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year]}

  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Applicable rate from the MACRS percentage table (mid-quarter convention)"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_year]}

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

  - id: asset.h_macrs_new
    printed: "(helper)"
    label: "MACRS depreciation for 2025 on property placed in service in 2025 (mid-quarter convention if the 40% test is met, otherwise half-year)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: true}]}
          then: asset.h_macrs_mq
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [mq.applies, {const: false}]}
          then: asset.h_macrs_hy

  - id: asset.macrs2025
    printed: "19(g)"
    label: "Column (g)—Depreciation deduction (GDS property placed in service in 2025, other than listed property)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_macrs_new

  - id: asset.h_last
    printed: "(helper)"
    label: "Last year of recovery for the recovery period"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}

  - id: asset.h_done
    printed: "(helper)"
    label: "The recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [asset.h_year, asset.h_last]}

  - id: asset.h_ub_prior_a
    printed: "(helper)"
    label: "Business cost less the section 179 deduction claimed in the year placed in service"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.prior_179}

  - id: asset.h_ub_prior
    printed: "(helper)"
    label: "Unadjusted basis: business cost less section 179 deduction and special depreciation allowance (not reduced by earlier MACRS depreciation)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_ub_prior_a, take: asset.prior_bonus}

  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "Applicable rate from the MACRS percentage table for the convention used and the 2025 year of recovery"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_year]}

  - id: asset.h_macrs_prior_live
    printed: "(helper)"
    label: "Apply the table rate to the property's unadjusted basis"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_ub_prior, rate: asset.h_rate_prior}

  - id: asset.h_macrs_old
    printed: "(helper)"
    label: "MACRS deduction for 2025 on property placed in service in tax years beginning before 2025"
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
              - {op: test, eq: [asset.h_done, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.h_done, {const: false}]}
          then: asset.h_macrs_prior_live

  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025 (other than listed property)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_zero
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_macrs_old

  - id: asset.h_listed_dep
    printed: "(helper)"
    label: "Depreciation for this property in 2025, whatever year it was placed in service"
    type: NonNegDollars
    expr: {op: sum, of: [asset.h_macrs_new, asset.h_macrs_old]}

  - id: asset.dep_listed
    printed: "26(h)"
    label: "Column (h)—Depreciation deduction (listed property used more than 50% in a qualified business use; follow the instructions for line 19, column (g))"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: true}]}
          then: asset.h_listed_dep
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.h_zero

  - id: asset.dep_2025
    printed: "(helper)"
    label: "MACRS depreciation for 2025 on this property if placed in service in 2025 (line 19(g), or its line 26(h) share if listed)"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_macrs_new}
    note: "The interface name is not defined by the text. I read it as regular MACRS depreciation of 2025 property, not counting the section 179 deduction or the special allowance, for listed and nonlisted property alike."

  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for this property (line 14, or line 25 if listed)"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_bonus_amt}
    note: "Total special allowance for this asset, listed or not. Lines 14 and 25 give the split."

  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 cost elected for this property in 2025 (line 6(c), or line 26(i) if listed)"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_s179_2025}
    note: "Total elected section 179 cost, listed or not. Line 26(i) gives the listed part. This is the elected amount, before the line 11 business income limit."

  - id: asset.mq_total
    printed: "(helper)"
    label: "Depreciable basis (after section 179, before any special depreciation allowance, business portion only) of MACRS property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_after179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero

  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis (after section 179, before any special depreciation allowance) of MACRS property placed in service during the last 3 months of the tax year"
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
    note: "The second guard is written so that it holds when the property is not 2025 property. For such property the quarter answer is not needed."

  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service during the tax year (Worksheet 1 line 1 / Form 4562 line 2): business cost of property used more than 50% in the business"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.h_over_half, {const: true}]}
          then: asset.basis
        - guard:
            op: test
            any:
              - {op: test, eq: [asset.h_is2025, {const: false}]}
              - {op: test, eq: [asset.h_over_half, {const: false}]}
          then: asset.h_zero
    note: "Worksheet 1 counts all eligible section 179 property, not only the amount elected, and includes listed property. Under the text, qualified improvement property is section 179 property only if the election is made. The interface cannot tell whether it was, so I counted it like other property."

  - id: asset.dep_prior
    printed: "(helper)"
    label: "MACRS depreciation for 2025 on this property if placed in service before 2025 (line 17, or its line 26(h) share if listed)"
    type: NonNegDollars
    expr: {op: copy, from: asset.h_macrs_old}
    note: "The interface name is not defined by the text. I read it as current-year MACRS on property placed in service before 2025, listed or not."
```
```
