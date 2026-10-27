# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | 6bf29f49b34005a8425e724fc9374efe18af62cf63ac7475a525472d1774c74d |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0f1df70975dae8df7b1ffdb285589a51a9f6b67c79822b31fe1d630b33de9de6 |
| printed lines compared | 16 |
| agree / disagree / missing | 4 / 12 / 0 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "26(h)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,760 of 2,045 comparisons agree (1,504 of 1,744 in scope); 240 candidate-unknown; 38 project-refuses; 7 candidate-refuses. No value differs: the candidate takes 19(g) for nonlisted and 26(h) for listed 2025 property, and the project's asset.macrs2025 is the same amount. The candidate attaches its refusal gates (asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad) to every helper and printed line, so it reads asset.s179 and asset.bonus_same even for property placed before 2025, and asset.bonus_same for property with bonus_choice none; the interview asks neither there (checked against the full profile's targets on each rebuilt witness), and the source needs neither: i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business" (an election only for property placed in service during the tax year) and i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". Witnesses: classm.f8880.2 without s179 and without bonus_same (project computes, candidate unknown). Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error): representation. The 38 project-refuses records are hidden through the mid-quarter test reading the cited scveh.low_use, or asset.listed_low / s179_bad: scope. The 7 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope. Project stands.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,771 of 2,045 comparisons agree (1,760 of 2,017 in scope); 242 candidate-unknown; 16 candidate-refuses; 15 project-unknown; 1 project-refuses. No value differs. The candidate attaches its refusal gates (asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad) to every helper and printed line, so it reads asset.s179 and asset.bonus_same even for property placed before 2025, and asset.bonus_same for property with bonus_choice none; the interview asks neither there (checked against the full profile's targets on each rebuilt witness), and the source needs neither: i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business" (an election only for property placed in service during the tax year) and i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". Witness: classm.f8880.2 without bonus_same. Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error): representation. The 15 project-unknown records withhold asset.class, asked of every asset: representation. The 16 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope. Project stands.

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

Ruling: model error; p946 p. 34, mid-quarter convention: "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year ... are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,738 of 2,045 comparisons agree (1,738 of 2,033 in scope); 255 candidate-unknown; 40 project-unknown; 12 candidate-refuses. No value differs. The candidate requires asset.s179 on property placed before 2025 through its s179_bad gate (e.g. classm.f8880.2 without s179), an answer the interview does not ask and i4562 p. 3, Part I ties to property placed in service during the tax year. Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error): representation. The 40 project-unknown records withhold asset.placed, asked of every asset: representation. The 12 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business"; i4562 p. 4, Worksheet 1: "include the total amount of eligible section 179 property". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,839 of 2,045 comparisons agree (1,837 of 2,032 in scope); 107 value; 88 candidate-unknown; 11 candidate-refuses. All 107 value differences are 2025 property used 50% or less in the business (asset.over_half false on every witness), where the candidate counts the business cost as section 179 property and the project counts zero: classm.asset.1 item_2 at 1% use (project $0.00, candidate $56.07), stage14.asset.refuse_s179_half at 50% ($0.00 against $1,500.00). That property is not eligible section 179 property, and the amount reaches printed Form 4562 line 2 (s179.line2). The 88 candidate-unknown and 11 candidate-refuses records are its gate inputs and the cited refusals the project makes elsewhere: representation and scope. Project stands.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"line": "17"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"line": "26(h)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Line 17: "For tangible property placed in service in tax years beginning before 2025 and depreciated under MACRS ... enter the deductions for the current year". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,851 of 2,045 comparisons agree (1,851 of 2,032 in scope); 181 candidate-unknown; 13 candidate-refuses. No value differs (11 listed assets placed before 2025 in the sample agree). For listed property placed before 2025 the candidate takes its 26(h), whose gates require asset.s179 and asset.bonus_same (8 records, e.g. on stage14 and classm bases), answers the source does not need for property placed in an earlier year. Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error): representation. The 13 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope. Project stands.

### (d) — Recovery period under GDS for the asset class
Status: **AGREE**

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **AGREE**

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; f4562 p. 1, line 14: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,343 of 2,045 comparisons agree (1,331 of 2,017 in scope); 348 value; 243 candidate-unknown; 95 project-unknown; 15 candidate-refuses; 1 project-refuses. All 348 value differences are on entries where the project's line is not reported (asset.on_19 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.bonus_2025 filtered by asset.listed (sc.f14, sc.f25_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.asset.1 item_1 placed before 2025 ($2,130.00 against $0.00), classm.asset.2 item_1 listed ($19,315.00 against $0.00). The candidate attaches its refusal gates (asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad) to every helper and printed line, so it reads asset.s179 and asset.bonus_same even for property placed before 2025, and asset.bonus_same for property with bonus_choice none; the interview asks neither there (checked against the full profile's targets on each rebuilt witness), and the source needs neither: i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business" (an election only for property placed in service during the tax year) and i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". (e.g. classm.f8880.2 without bonus_same.) Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error): representation. The 95 project-unknown records withhold answers only the hidden value reads, or asset.class on reported entries (asked of every asset): representation. The 15 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope; the project-refuses record is the cited asset.bonus_mixed. Project stands.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 13, Line 25: "If you placed in service certain qualified listed property during the tax year, you may be able to deduct the special depreciation allowance". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,043 of 2,045 comparisons agree (1,031 of 2,019 in scope); 631 value; 184 candidate-unknown; 173 project-unknown; 13 candidate-refuses; 1 project-refuses. All 631 value differences are on entries where the project's line is not reported (asset.on_26_2025 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.bonus_2025 filtered by asset.listed (sc.f25_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.f8889.4.deepseek item_2 not listed ($48,573.00 against $0.00), classm.asset.1 item_1 placed before 2025 ($2,130.00 against $0.00). The candidate attaches its refusal gates (asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad) to every helper and printed line, so it reads asset.s179 and asset.bonus_same even for property placed before 2025, and asset.bonus_same for property with bonus_choice none; the interview asks neither there (checked against the full profile's targets on each rebuilt witness), and the source needs neither: i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business" (an election only for property placed in service during the tax year) and i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". (e.g. classm.f8880.2 without bonus_same.) Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error): representation. The 173 project-unknown records are on entries where the line is not reported (one withholds asset.class, asked of every asset): representation. The 13 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope; the project-refuses record is the cited asset.bonus_mixed. Project stands.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i4562 p. 5, Line 6: "Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,546 of 2,045 comparisons agree (1,546 of 2,033 in scope); 296 candidate-unknown; 191 value; 12 candidate-refuses. All 191 value differences are on entries where the project's line is not reported (asset.on_26_2025 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.s179_2025 filtered by asset.listed (sc.f6, sc.f29_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.asset.2 item_1 not listed ($3,189.00 against $0.00), classm.asset.3 item_1 ($7,925.00 against $0.00). The 296 candidate-unknown records withhold placed, listed, screen, cost or pct, asked of every asset where the base is not refused (3 on generated 20261026/449, a fully recovered asset, are the gate-input model error ruled at asset.dep_2025). The 12 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope. Project stands.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 11, Column (c): "multiply the cost or other basis of the property by the percentage of business/investment use" ... "Any special depreciation allowance included on line 14"; i4562 p. 9, Lines 19a Through 19j: "Use lines 19a through 19j only for assets placed in service during the tax year beginning in 2025"; p. 9: "For listed property, use Part V.". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,451 of 2,045 comparisons agree (1,438 of 2,013 in scope); 413 value; 126 candidate-unknown; 36 project-unknown; 17 project-refuses; 2 candidate-refuses. All 413 value differences are on entries where the project's line is not reported (asset.on_19 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". No Schedule C sum reads 19(c); asset.ub, which feeds the MACRS amounts, is compared through 19(g) and asset.dep_2025; no printed amount differs. Witnesses: classm.f8889.2.deepseek item_1 listed, placed before 2025 ($38,615.00 against $0.00), classm.asset.1 item_1 ($3,195.00 against $0.00). The candidate attaches its refusal gates (asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad) to every helper and printed line, so it reads asset.s179 and asset.bonus_same even for property placed before 2025, and asset.bonus_same for property with bonus_choice none; the interview asks neither there (checked against the full profile's targets on each rebuilt witness), and the source needs neither: i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business" (an election only for property placed in service during the tax year) and i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". (e.g. classm.f8880.2 without bonus_same.) Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error): representation. The 36 project-unknown records are on entries where the line is not reported; the 17 project-refuses records are the cited asset.listed_low, asset.bonus_mixed and asset.s179_bad: scope; the 2 candidate refusals are the bonus-mixed refusal the project makes on the base record. Project stands.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j: "Use lines 19a through 19j only for assets placed in service during the tax year beginning in 2025"; p. 9: "For listed property, use Part V."; p946 p. 34, mid-quarter convention: "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year ... are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 1,245 of 2,045 comparisons agree (993 of 1,534 in scope); 306 project-unknown; 252 project-refuses; 139 value; 96 candidate-unknown; 7 candidate-refuses. All 139 value differences are on entries where the project's line is not reported (asset.on_19 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.dep_2025 by recovery period (sc.f19_*), which agrees in value on every record, which triage compares separately, so no printed amount differs. Witnesses: classm.asset.1 item_1 placed before 2025 ($363.27 against $0.00), classm.asset.4 item_1 ($5.90 against $0.00). The 252 project-refuses records are hidden values reached through the mid-quarter test reading a vehicle's cited scveh.low_use (i4562 p. 14-15), or the asset's cited listed_low / s179_bad: scope. The 306 project-unknown records are on entries where the line is not reported: representation. The candidate attaches its refusal gates (asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad) to every helper and printed line, so it reads asset.s179 and asset.bonus_same even for property placed before 2025, and asset.bonus_same for property with bonus_choice none; the interview asks neither there (checked against the full profile's targets on each rebuilt witness), and the source needs neither: i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business" (an election only for property placed in service during the tax year) and i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". (e.g. classm.f8880.2 without bonus_same.) Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error). The 7 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope. Project stands.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i4562 p. 9, Line 17: "For tangible property placed in service in tax years beginning before 2025 and depreciated under MACRS ... enter the deductions for the current year"; p. 9: "For listed property, use Part V.". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 822 of 2,045 comparisons agree (821 of 2,032 in scope); 983 value; 181 project-unknown; 47 candidate-unknown; 11 project-refuses; 1 candidate-refuses. All 983 value differences are on entries where the project's line is not reported (asset.on_17 false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.dep_prior filtered by asset.listed (sc.f17) and asset.dep_listed (sc.f26_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.f8889.2.deepseek item_2, a 2025 asset ($6,797.32 against $0.00), classm.f8889.4.deepseek item_1 ($1,168.88 against $0.00). The 181 project-unknown records are on entries where the line is not reported; the 11 project-refuses records are the cited asset.listed_low (i4562 p. 14-15): scope. The 47 candidate-unknown records withhold answers asked of every asset (2 on generated 20261026/449, the gate-input model error ruled at asset.dep_2025); the candidate refusal (stage14.asset.refuse_class) is the cited asset.outside refusal the project makes on that return: scope. Project stands.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 15, Column (h): "For property used more than 50% in a qualified business use (line 26) and placed in service after 1986, figure column (h) by following the instructions for line 19, column (g)". Triage executable-triage-v1 (triage/asset.deepseek.json; 1,083 fixtures, 500 generated returns seed 20261026, 893 partial records): 866 of 2,045 comparisons agree (846 of 1,744 in scope); 484 value; 274 project-refuses; 252 project-unknown; 162 candidate-unknown; 7 candidate-refuses. All 484 value differences are on entries where the project's line is not reported (asset.listed false, checked for every witness), where the candidate enters zero; spec/spec.md (shown_when): "the values sheet shows the line only when it is true ... The value is computed either way". The Schedule C sums read asset.dep_listed filtered by asset.listed (sc.f26_assets), which triage compares separately, so no printed amount differs. Witnesses: classm.f8889.2.deepseek item_2 not listed ($6,797.32 against $0.00), classm.f8889.4.deepseek item_1 ($2,045.69 against $0.00). The 274 project-refuses records are project refusals are the cited gates asset.listed_low (i4562 p. 14-15), asset.bonus_mixed (p. 7), asset.s179_bad (p. 3, p. 5), asset.screened (pp. 8-12) and, through the mid-quarter test, scveh.low_use (p. 14-15): scope. The 252 project-unknown records are on entries where the line is not reported: representation. The candidate attaches its refusal gates (asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad) to every helper and printed line, so it reads asset.s179 and asset.bonus_same even for property placed before 2025, and asset.bonus_same for property with bonus_choice none; the interview asks neither there (checked against the full profile's targets on each rebuilt witness), and the source needs neither: i4562 p. 3, Part I: "You can elect to expense part or all of the cost of section 179 property (defined earlier) that you placed in service during the tax year and used predominantly (more than 50%) in your trade or business" (an election only for property placed in service during the tax year) and i4562 p. 7, Election out: "You can elect, for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year". (e.g. classm.f8880.2 without s179.) Its other candidate-unknown records withhold class, cost, pct, screen, listed or placed, which the interview asks of every asset where the base is not refused (exception: generated 20261026/449, a fully recovered asset whose cost and percentage the source does not need, the same model error). The 7 candidate-refuses records are on refusal fixtures (stage14.asset.refuse_listed_low, refuse_pct, refuse_s179_over, refuse_class) or their partials, where the project refuses the same return with the same cited gate on another line: scope. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| asset.dep_2025 | asset.bonus_mixed, asset.listed_low, asset.outside, asset.pct_bad, asset.s179_bad, asset.screen | asset.outside, asset.pct_bad, asset.screen |
| asset.bonus_2025 | asset.bonus_mixed, asset.listed_low, asset.pct_bad, asset.s179_bad, asset.screen | asset.pct_bad, asset.screen |
| asset.s179_2025 | asset.listed_low, asset.s179_bad, asset.screen | asset.listed_low, asset.s179_bad, asset.screen |
| asset.mq_q4 | asset.listed_low, asset.outside, asset.pct_bad, asset.s179_bad, asset.screen | asset.outside, asset.pct_bad, asset.screen |
| asset.mq_total | asset.listed_low, asset.outside, asset.pct_bad, asset.s179_bad, asset.screen | asset.outside, asset.pct_bad, asset.screen |
| asset.cost179 | asset.listed_low, asset.outside, asset.pct_bad, asset.screen | asset.outside, asset.pct_bad, asset.screen |
| asset.dep_prior | asset.bonus_mixed, asset.listed_low, asset.outside, asset.pct_bad, asset.s179_bad, asset.screen | asset.bonus_mixed, asset.outside, asset.pct_bad, asset.s179_bad, asset.screen |
| (d) | asset.screen | asset.screen |
| (c) | asset.pct_bad, asset.screen | asset.pct_bad, asset.screen |
| 14 | asset.bonus_mixed, asset.listed_low, asset.pct_bad, asset.s179_bad, asset.screen | asset.pct_bad, asset.screen |
| 25 | asset.bonus_mixed, asset.listed_low, asset.pct_bad, asset.s179_bad, asset.screen | asset.pct_bad, asset.screen |
| 26(i) | asset.listed_low, asset.s179_bad, asset.screen | asset.listed_low, asset.s179_bad, asset.screen |
| 19(c) | asset.bonus_mixed, asset.listed_low, asset.outside, asset.pct_bad, asset.s179_bad, asset.screen | asset.outside, asset.pct_bad, asset.screen |
| 19(g) | asset.bonus_mixed, asset.listed_low, asset.outside, asset.pct_bad, asset.s179_bad, asset.screen | asset.outside, asset.pct_bad, asset.screen |
| 17 | asset.outside, asset.pct_bad, asset.screen | asset.outside, asset.pct_bad, asset.screen |
| 26(h) | asset.bonus_mixed, asset.listed_low, asset.outside, asset.pct_bad, asset.s179_bad, asset.screen | asset.outside, asset.pct_bad, asset.screen |

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
    expr: {op: prorate, amount: asset.cost, part: asset.pct_c, whole: asset.hundred, places: 6}
    refuses: [asset.screen, asset.pct_bad]
    note: "The archived text treats column (c) as the depreciable basis after section 179 and the special allowance; this line is read as the business/investment-use cost before those reductions, with line 19(c) below carrying the reduced basis."
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: false}]}]}
          then: asset.bonus_2025
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}]}
          then: asset.zero
        - guard: {op: test, eq: [asset.is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.bonus_mixed, asset.listed_low]
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for listed property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}]}
          then: asset.bonus_2025
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: false}]}]}
          then: asset.zero
        - guard: {op: test, eq: [asset.is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.bonus_mixed, asset.listed_low]
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost for listed property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}]}
          then: asset.s179_2025
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: false}]}]}
          then: asset.zero
        - guard: {op: test, eq: [asset.is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.s179_bad, asset.listed_low]
  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.on_19, {const: true}]}
          then: asset.ub
        - guard: {op: test, eq: [asset.on_19, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.outside, asset.pct_bad, asset.bonus_mixed, asset.s179_bad]
  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.on_19, {const: false}]}
          then: asset.zero
        - guard: {op: test, all: [{op: test, eq: [asset.on_19, {const: true}]}, {op: test, eq: [mq.applies, {const: true}]}]}
          then: asset.macrs_mq
        - guard: {op: test, all: [{op: test, eq: [asset.on_19, {const: true}]}, {op: test, eq: [mq.applies, {const: false}]}]}
          then: asset.macrs_hy
    refuses: [asset.screen, asset.outside, asset.pct_bad, asset.bonus_mixed, asset.s179_bad, asset.listed_low]
  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS depreciation for property placed in service before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.on_17, {const: false}]}
          then: asset.zero
        - guard: {op: test, all: [{op: test, eq: [asset.on_17, {const: true}]}, {op: test, eq: [asset.done, {const: true}]}]}
          then: asset.zero
        - guard: {op: test, all: [{op: test, eq: [asset.on_17, {const: true}]}, {op: test, eq: [asset.done, {const: false}]}]}
          then: asset.macrs_prior_live
    refuses: [asset.screen, asset.outside, asset.pct_bad]
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction for listed property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.listed, {const: false}]}
          then: asset.zero
        - guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.done, {const: true}]}]}
          then: asset.zero
        - guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.done, {const: false}]}, {op: test, eq: [mq.applies, {const: true}]}]}
          then: asset.macrs_mq
        - guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.done, {const: false}]}, {op: test, eq: [mq.applies, {const: false}]}]}
          then: asset.macrs_hy
        - guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.is2025, {const: false}]}, {op: test, eq: [asset.done, {const: true}]}]}
          then: asset.zero
        - guard: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.is2025, {const: false}]}, {op: test, eq: [asset.done, {const: false}]}]}
          then: asset.macrs_prior_live
    refuses: [asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad]
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Regular MACRS depreciation for property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: true}]}]}
          then: asset.dep_listed
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.listed, {const: false}]}]}
          then: asset.macrs2025
        - guard: {op: test, eq: [asset.is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.outside, asset.listed_low, asset.pct_bad, asset.bonus_mixed, asset.s179_bad]
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.is2025, {const: true}]}
          then: asset.bonus_fullcase
        - guard: {op: test, eq: [asset.is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.bonus_mixed, asset.listed_low, asset.pct_bad, asset.s179_bad]
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 elected cost for property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.is2025, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.s179_bad, asset.listed_low]
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Basis of 2025 property placed in service in the fourth quarter for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.quarter, {const: "q4"}]}]}
          then: asset.after179
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [asset.is2025, {const: true}]}, {op: test, eq: [asset.quarter, {const: "q4"}]}]}}
          then: asset.zero
    refuses: [asset.screen, asset.outside, asset.pct_bad, asset.s179_bad, asset.listed_low]
  - id: asset.mq_total
    printed: "(helper)"
    label: "Total basis of 2025 property for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.is2025, {const: true}]}
          then: asset.after179
        - guard: {op: test, eq: [asset.is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.outside, asset.pct_bad, asset.s179_bad, asset.listed_low]
  - id: asset.cost179
    printed: "(helper)"
    label: "Business cost of section 179 property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.is2025, {const: true}]}
          then: asset.basis
        - guard: {op: test, eq: [asset.is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen, asset.outside, asset.pct_bad, asset.listed_low]
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Regular MACRS depreciation for property placed in service before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: false}]}, {op: test, eq: [asset.listed, {const: true}]}]}
          then: asset.dep_listed
        - guard: {op: test, all: [{op: test, eq: [asset.is2025, {const: false}]}, {op: test, eq: [asset.listed, {const: false}]}]}
          then: asset.macrs_prior
        - guard: {op: test, eq: [asset.is2025, {const: true}]}
          then: asset.zero
    refuses: [asset.screen, asset.outside, asset.listed_low, asset.pct_bad]
  - id: asset.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: asset.cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: asset.hundred
    printed: "(helper)"
    label: "One dollar"
    type: NonNegDollars
    expr: {op: param, ref: sc.hundred_cents}
  - id: asset.half
    printed: "(helper)"
    label: "Fifty cents"
    type: NonNegDollars
    expr: {op: param, ref: sc.fifty_cents}
  - id: asset.pct_c
    printed: "(helper)"
    label: "Business-use percentage in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.cent, count: asset.pct}
  - id: asset.pct_bad
    printed: "(gate)"
    label: "Business-use percentage outside 1 to 100"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, lt: [asset.pct, {const: 1, type: Count}]}
        - {op: test, gt: [asset.pct, {const: 100, type: Count}]}
  - id: asset.over_half
    printed: "(helper)"
    label: "Business use is more than 50%"
    type: Bool
    expr: {op: test, gt: [asset.pct_c, asset.half]}
  - id: asset.listed_low
    printed: "(gate)"
    label: "Listed property used 50% or less in the business"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.listed, {const: true}]}
        - {op: test, not: {op: test, gt: [asset.pct_c, asset.half]}}
  - id: asset.is2025
    printed: "(helper)"
    label: "Placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.on_19
    printed: "(helper)"
    label: "Property placed in service in 2025 and not listed property"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.is2025, {const: true}]}
        - {op: test, eq: [asset.listed, {const: false}]}
  - id: asset.on_17
    printed: "(helper)"
    label: "Property placed in service before 2025 and not listed property"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.is2025, {const: false}]}
        - {op: test, eq: [asset.listed, {const: false}]}
  - id: asset.year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.last
    printed: "(helper)"
    label: "Last year of recovery"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}
  - id: asset.done
    printed: "(helper)"
    label: "Recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [asset.year, asset.last]}
  - id: asset.outside
    printed: "(gate)"
    label: "Recovery period is outside the supported MACRS periods"
    type: Bool
    expr: {op: test, eq: [asset.period, {const: "outside"}]}
  - id: asset.hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}
  - id: asset.qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}
  - id: asset.rate_hy
    printed: "(helper)"
    label: "MACRS rate using the half-year convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.hy, asset.year]}
  - id: asset.rate_mq
    printed: "(helper)"
    label: "MACRS rate using the mid-quarter convention"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.qconv, asset.year]}
  - id: asset.after179
    printed: "(helper)"
    label: "Basis after section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.s179}
  - id: asset.s179_bad
    printed: "(gate)"
    label: "Section 179 elected amount exceeds business basis"
    type: Bool
    expr: {op: test, gt: [asset.s179, asset.basis]}
  - id: asset.rate40
    printed: "(helper)"
    label: "Forty percent special depreciation allowance rate"
    type: Rate
    expr: {op: param, ref: sc.bonus_rate_40}
  - id: asset.bonus_full
    printed: "(helper)"
    label: "One hundred percent special depreciation allowance"
    type: NonNegDollars
    expr: {op: copy, from: asset.after179}
  - id: asset.bonus_forty
    printed: "(helper)"
    label: "Forty percent special depreciation allowance"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.after179, rate: asset.rate40}
  - id: asset.bonus_fullcase
    printed: "(helper)"
    label: "Special depreciation allowance before separating listed and nonlisted property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.zero
        - guard: {op: test, all: [{op: test, eq: [asset.bonus_choice, {const: "full"}]}, {op: test, eq: [asset.after_jan19, {const: true}]}]}
          then: asset.bonus_full
        - guard: {op: test, all: [{op: test, eq: [asset.bonus_choice, {const: "full"}]}, {op: test, eq: [asset.after_jan19, {const: false}]}]}
          then: asset.bonus_forty
        - guard: {op: test, eq: [asset.bonus_choice, {const: "forty"}]}
          then: asset.bonus_forty
  - id: asset.bonus_mixed
    printed: "(gate)"
    label: "Special depreciation allowance choice is not uniform for the recovery-period class"
    type: Bool
    expr: {op: test, eq: [asset.bonus_same, {const: false}]}
  - id: asset.ub
    printed: "(helper)"
    label: "Basis for regular depreciation after section 179 and special allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.after179, take: asset.bonus_2025}
  - id: asset.macrs_hy
    printed: "(helper)"
    label: "MACRS depreciation using the half-year convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.ub, rate: asset.rate_hy}
  - id: asset.macrs_mq
    printed: "(helper)"
    label: "MACRS depreciation using the mid-quarter convention"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.ub, rate: asset.rate_mq}
  - id: asset.ub_prior_a
    printed: "(helper)"
    label: "Prior-year basis after prior section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.prior_179}
  - id: asset.ub_prior
    printed: "(helper)"
    label: "Prior-year basis after prior section 179 and prior special allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.ub_prior_a, take: asset.prior_bonus}
  - id: asset.rate_prior
    printed: "(helper)"
    label: "MACRS rate using the convention in the placed-in-service year"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.year]}
  - id: asset.macrs_prior_live
    printed: "(helper)"
    label: "MACRS depreciation for prior property before the recovery-period check"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.ub_prior, rate: asset.rate_prior}
```
