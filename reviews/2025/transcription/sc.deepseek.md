# Transcription agreement — sc

Second transcription of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` by an isolated model (spec 6.5), compared line by line with `forms/2025/sc.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 06db6ce208dcba8711a2edc4fe93c80fe46579a5600832344e51ce379d9959e5 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 6bf480b5cfb41265b354e11eb2541dc66fc9b7af9b492d9d2103d9163fa2e879 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | f2becc16c3eeae8f68992cc2f01efbff5b42801963cbe3b20f870db4d59276b6 |
| printed lines compared | 55 |
| agree / disagree / missing | 20 / 35 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| i4562 | 2025 | 4, 5, 9, 10, 13, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 9, 10, 13, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i1040gi | 2025; printed date 2026-02-25 | 94, 95, 104, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 95, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4, 6 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4, 6 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- sc.sc.ho_line2: operand 'sc.ho_sqft' is not money
- sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve
- sc.sc.ho_line2: declared count but the expression produces money

## Lines

### sc.one — One business
Status: **AGREE**

### sc.rrta — This business's owner has railroad retirement compensation
Status: **AGREE**

### sc.line31_pre179 — Line 31 without the section 179 expense deduction
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"line": "30"}}
```

Second:

```json
{"expression": {"of": [{"line": "12 (sc.s179_allowed)"}, {"line": "31"}], "op": "sum"}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. Two differences. (1) Inside Form 4562 line 28, the second sums asset.f25 over the listed assets where the project sums asset.bonus_2025. asset.f25 is a display line, shown only for listed property placed in service in 2025 (asset.on_26_2025), and copies asset.bonus for every asset; for listed property placed in service before 2025, asset.bonus is the allowance elected in the year of placement (asset.bonus_choice is asked of every asset, for the basis), which is not a 2025 line 25 amount ('If you placed in service certain qualified listed property during the tax year, you may be able to deduct the special depreciation allowance', i4562 p. 13, Line 25). asset.bonus_2025 is that allowance for 2025 property and zero otherwise, so the project is right and the second over-counts an earlier year's allowance. (2) As ruled before: both figure line 31 before the section 179 deduction for Pub. 946's two income limits (pp. 17-19, Steps 1 to 5); the project subtracts the home office deduction of line 30 as figured, the second refigures it inside this line from the worksheet; the line-30 value is the same.

### sc.result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "31"}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. The project's choose has one alternative whose guard (line 31 at least zero, or less than zero) always holds; it is line 31 on both sides. The choose carries the refusals that reach this line (statutory employee income, box 32b, and the others on sc.result).

### sc.f6 — Section 179 elected on property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "asset", "field": "asset.s179", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"value": 6}.

### sc.f14 — Special allowance on property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "asset", "field": "asset.bonus", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"value": 850}.

### sc.f17 — MACRS on earlier property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs_prior", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-refuses": 2, "candidate-unknown": 47, "value": 1258}.

### sc.f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-unknown": 3, "project-refuses": 2, "value": 4}.

### sc.f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-unknown": 300, "value": 143}.

### sc.f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-refuses": 1, "candidate-unknown": 109, "project-refuses": 3, "value": 196}.

### sc.f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-unknown": 51, "value": 6}.

### sc.f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-unknown": 2, "project-refuses": 1, "value": 14}.

### sc.f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"project-refuses": 1, "value": 195}.

### sc.f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}}
```

Ruling: representation — executable triage (T-143) agrees on all 3973 comparisons on the valid line. The earlier by-reading ruling is superseded.

### sc.f25 — Line 25 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-refuses": 2, "project-refuses": 104, "project-unknown": 1, "value": 944}. project retained. Form 4562 line 25 for the business: the second sums asset.f25 over the listed assets where the project sums asset.bonus_2025. asset.f25 is a display line, shown only for listed property placed in service in 2025 (asset.on_26_2025), and copies asset.bonus for every asset; for listed property placed in service before 2025, asset.bonus is the allowance elected in the year of placement (asset.bonus_choice is asked of every asset, for the basis), which is not a 2025 line 25 amount ('If you placed in service certain qualified listed property during the tax year, you may be able to deduct the special depreciation allowance', i4562 p. 13, Line 25). asset.bonus_2025 is that allowance for 2025 property and zero otherwise, so the project is right and the second over-counts an earlier year's allowance. The vehicle term (scveh.bonus) is the same on both sides.

### sc.f26h — Column (h), line 26, for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-refuses": 6, "project-refuses": 105, "value": 1285}. project retained. Column (h) of line 26 summed over the business's listed assets and vehicles on both sides. Listed property used 50% or less (Form 4562 line 27) is refused on both the asset and the vehicle (asset.yaml, scveh.yaml), so the second's filter for more than 50% business use selects the same entries within scope.

### sc.f28 — Line 28 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}
```

Second:

```json
{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": null}, {"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-refuses": 6, "project-refuses": 105, "value": 1786}. project retained. Line 28 (lines 25 and 26 column (h)) on both sides, summed in another order; within it the second sums asset.f25 over the listed assets where the project sums asset.bonus_2025. asset.f25 is a display line, shown only for listed property placed in service in 2025 (asset.on_26_2025), and copies asset.bonus for every asset; for listed property placed in service before 2025, asset.bonus is the allowance elected in the year of placement (asset.bonus_choice is asked of every asset, for the basis), which is not a 2025 line 25 amount ('If you placed in service certain qualified listed property during the tax year, you may be able to deduct the special depreciation allowance', i4562 p. 13, Line 25). asset.bonus_2025 is that allowance for 2025 property and zero otherwise, so the project is right and the second over-counts an earlier year's allowance.

### sc.f29 — Line 29 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "asset", "field": "asset.f26i", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"project-refuses": 102, "value": 233}. project retained. Line 29 for the business: the second sums asset.f26i over the listed assets where the project sums asset.s179_2025. asset.f26i is a display line, shown only for listed property placed in service in 2025 (asset.on_26_2025), and copies asset.s179, which is asked of every asset; column (i) of line 26 is the section 179 cost elected in 2025 ('Enter the amount you elect to expense', i4562 p. 16, Column (i)), so for listed property placed in service before 2025 the second would carry an earlier year's election into line 29. asset.s179_2025 is the election on 2025 property and zero otherwise. The vehicle term (scveh.s179_2025) is the same on both sides.

### sc.mq_q4 — mq_q4 of this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"project-refuses": 99, "value": 5}.

### sc.mq_total — mq_total of this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_total", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "asset", "field": "asset.mq_total", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"project-refuses": 102, "value": 21}.

### sc.cost179 — cost179 of this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.cost179", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.cost179", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "asset", "field": "asset.cost179", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"project-refuses": 100, "value": 23}.

### sc.profit_pos — Net profit of this business (zero for a loss)
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"expression": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. The project selects line 31 under a guard that holds for every value (line 31 at least zero, or less than zero) and floors it at zero; the second takes the larger of zero and line 31. Both are line 31 when it is positive and zero otherwise.

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **AGREE**

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **AGREE**

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **AGREE**

### 9 (sc.line9) — Car and truck expenses
Status: **AGREE**

### 12 (sc.line12) — Depletion
Status: **AGREE**

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "12 (sc.s179_allowed)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}
```

Second:

```json
{"collection": "f4562", "field": "f4562.line22", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-unknown": 821, "project-refuses": 264}. project retained. Form 4562 line 22 for the business (line 12, lines 14 to 17, line 19 column (g), line 21) on both sides, with line 21 (line 28) summed in another order; within it the second sums asset.f25 over the listed assets where the project sums asset.bonus_2025. asset.f25 is a display line, shown only for listed property placed in service in 2025 (asset.on_26_2025), and copies asset.bonus for every asset; for listed property placed in service before 2025, asset.bonus is the allowance elected in the year of placement (asset.bonus_choice is asked of every asset, for the basis), which is not a 2025 line 25 amount ('If you placed in service certain qualified listed property during the tax year, you may be able to deduct the special depreciation allowance', i4562 p. 13, Line 25). asset.bonus_2025 is that allowance for 2025 property and zero otherwise, so the project is right and the second over-counts an earlier year's allowance. Lines 15, 16 and 20 are refused on the asset (asset.screen), as the second's note says.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "sc.rent_equipment"}, {"collection": "scveh", "field": "scveh.line20a", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"input": "sc.rent_equipment"}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"project-refuses": 1, "value": 154}.

### 24b — Deductible meals
Status: **AGREE**

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

### 27b — Other expenses (from line 48)
Status: **AGREE**

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

### 3a — Maximum allowable amount (per square foot)
Status: **AGREE**

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "30(b)"}, {"param": "sc.ho_max_sqft"}], "test": "le"}, "then": {"amount": {"line": "3a"}, "count": {"line": "30(b)"}, "op": "multiply_count"}}, {"guard": {"args": [{"param": "sc.ho_max_sqft"}, {"line": "30(b)"}], "test": "lt"}, "then": {"amount": {"line": "3a"}, "count": {"param": "sc.ho_max_sqft"}, "op": "multiply_count"}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"line": "3a"}, "count": {"of": [{"line": "30(b)"}, {"ref": "sc.ho_max_sqft"}], "op": "smaller_of"}, "op": "multiply_count"}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. $5 times the smaller of the square footage and 300 (i1040sc Simplified Method Worksheet); the project chooses by an interval on the footage, the second takes the smaller of the two counts.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.ho_line4)"}, {"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}, {"ref": "s179.line10"}], "op": "sum"}}], "test": "le"}, "then": {"line": "4 (sc.ho_line4)"}}, {"guard": {"args": [{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}, {"ref": "s179.line10"}], "op": "sum"}}, {"line": "4 (sc.ho_line4)"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": 0}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}, {"ref": "s179.line10"}], "op": "sum"}], "test": "eq"}, "then": {"of": [{"line": "4 (sc.ho_line4)"}, {"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"const": 0}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}, {"ref": "s179.line10"}], "op": "sum"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"of": [{"line": "1 (sc.ho_line1)"}, {"line": "4 (sc.ho_line4)"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. The smaller of worksheet lines 1 and 4 on both sides. The project tests whether line 4 can exceed line 1 under the most section 179 deduction the business could take (its 2025 elections plus the carryover, since BUG-0060) and refuses where the two limits of Pub. 946 (p. 19) interact (sc.ho_both); the second takes the smaller of the two lines directly. Equal on every return the project computes.

### 30 — Expenses for business use of your home
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"line": "5 (sc.ho_line5)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"line": "5 (sc.ho_line5)"}}], "op": "choose"}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section).

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **DISAGREE**

Project:

```json
{"from": {"line": "29"}, "op": "subtract", "take": {"line": "30"}}
```

Second:

```json
{"expression": {"from": {"line": "29"}, "op": "subtract", "take": {"line": "30"}}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section).

### 40 — Add lines 35 through 39
Status: **AGREE**

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"ref": "s179.line12"}, {"ref": "s179.line8"}], "test": "eq"}, "then": {"of": [{"of": [{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}}, {"guard": {"args": [{"ref": "s179.line12"}, {"ref": "s179.line8"}], "test": "ne"}, "then": {"ref": "s179.line12"}}], "op": "choose"}
```

Second:

```json
{"collection": "f4562", "field": "f4562.line12", "op": "sum_over", "where": null}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-unknown": 821, "project-refuses": 271}.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **AGREE**

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **AGREE**

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"expression": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. The project selects line 31 under a guard that holds for every value (line 31 at least zero, or less than zero) and floors it at zero; the second takes the larger of zero and line 31. Both are line 31 when it is positive and zero otherwise.

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **AGREE**

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 6, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 3, "whole": {"line": "5 (sc.f7206_line5)"}}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. Schedule 1 line 15 times line 4 over line 5 on both sides. The project rounds the ratio to six places (amb.2025.f7206_ratio_places, an agent reading for owner review in TASKS.md); the second to four.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **DISAGREE**

Project:

```json
{"from": {"line": "4 (sc.f7206_line4)"}, "op": "subtract_floor0", "take": {"line": "7 (sc.f7206_line7)"}}
```

Second:

```json
{"expression": {"from": {"line": "4 (sc.f7206_line4)"}, "op": "subtract_floor0", "take": {"line": "7 (sc.f7206_line7)"}}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. Line 7 is this business's share of the deductible part of self-employment tax, which is less than its net profit on line 4, so line 4 less line 7 is never negative and the project's floor at zero changes nothing.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 6, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}
```

Ruling: model error — executable triage (T-143): 3973 comparisons; differences by kind {"candidate-refuses": 393, "candidate-unknown": 41, "project-refuses": 266, "project-unknown": 2513}. project retained. Schedule 1 line 16 times line 4 over line 5 on both sides (amb.2025.f7206_plan_attribution); the project also enters zero for a person with no Schedule C, which cannot occur within this collection. The project rounds the ratio to six places (amb.2025.f7206_ratio_places, an agent reading for owner review in TASKS.md); the second to four.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **DISAGREE**

Project:

```json
{"from": {"line": "8 (sc.f7206_line8)"}, "op": "subtract_floor0", "take": {"line": "9 (sc.f7206_line9)"}}
```

Second:

```json
{"expression": {"from": {"line": "8 (sc.f7206_line8)"}, "op": "subtract_floor0", "take": {"line": "9 (sc.f7206_line9)"}}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. Form 7206 (2025) line 10 reads 'Subtract line 9 from line 8' with no floor; the project floors it at zero. The values differ only when line 9 (the plan contribution attributable to the business) exceeds line 8; then line 13 copies line 10 (lines 11 and 12, an S corporation and Form 2555, are refused) and line 14 is 'the smaller of line 3 or line 13', so the second would enter a negative amount as the self-employed health insurance deduction on Schedule 1 line 17, which is not a deduction; the project enters zero, the only amount the line can carry.

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **DISAGREE**

Project:

```json
{"line": "10 (sc.f7206_line10)"}
```

Second:

```json
{"expression": {"from": {"line": "10 (sc.f7206_line10)"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. Line 12 (Form 2555) is refused and line 11 (S corporation) does not apply, so line 13 is line 10 on both sides.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"of": [{"line": "13 (sc.f7206_line13)"}, {"line": "3 (sc.f7206_line3)"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"line": "13 (sc.f7206_line13)"}, {"line": "3 (sc.f7206_line3)"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section).

### 1(c) — Qualified business income or (loss) of this business
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract", "take": {"of": [{"line": "14 (sc.f7206_line14)"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}], "op": "sum"}}
```

Second:

```json
{"expression": {"line": "31"}, "invalid_model_types": [{"line": "sc.ho_line2", "message": "sc.sc.ho_line2: operand 'sc.ho_sqft' is not money"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: reference 'sc.ho_max_sqft' does not resolve"}, {"line": "sc.ho_line2", "message": "sc.sc.ho_line2: declared count but the expression produces money"}]}
```

Second transcription's note: The archived Schedule C and Form 8995 pages do not give a business-by-business allocation of the person-level deductions (deductible part of self-employment tax, self-employed health insurance, and retirement plan contributions) that reduce QBI. This line reports the Schedule C net profit or loss before those person-level reductions.

Ruling: model error — T-143 records 3973 comparisons as candidate-invalid; the declaration, or the ho_line2/line 31 chain it depends on, fails current validation (see the log's type-check section). project retained. Both subtract from line 31 the deductible part of self-employment tax, the SEP or SIMPLE deduction and the health insurance deduction attributable to the business (i8995 p. 2; amb.2025.qbi_attribution). The second uses Form 7206 lines 7, 9 and 14 for the first two; the project's sc.qbi_se and sc.qbi_plan prorate the same amounts by the same ratio (net profit over person.positive_profits, which is Form 7206 line 5), so the comparison sees references on one side and their expansion on the other.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sc.line31_pre179 | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| sc.result | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| sc.profit_pos | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| 12 (sc.line12) | sc.special | sc.special |
| 27a | sc.special | sc.special |
| 28 | sc.special | sc.special |
| 29 | sc.special | sc.special |
| 1 (sc.ho_line1) | sc.special | sc.special |
| 5 (sc.ho_line5) | sc.special | sc.special |
| 30 | sc.ho_other, sc.special | sc.ho_other, sc.special |
| 31 | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| 4 (sc.f7206_line4) | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| 7 (sc.f7206_line7) | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| 8 (sc.f7206_line8) | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| 10 (sc.f7206_line10) | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| 13 (sc.f7206_line13) | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| 14 (sc.f7206_line14) | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |
| 1(c) | sc.at_risk, sc.ho_other, sc.passive, sc.special | sc.at_risk, sc.ho_other, sc.passive, sc.special |

## Raw second transcription

```yaml
lines:
  - id: sc.line3
    printed: "3 (sc.line3)"
    label: "Subtract line 2 from line 1"
    type: Dollars
    expr: {op: subtract, from: sc.line1, take: sc.line2}
  - id: sc.line4
    printed: "4 (sc.line4)"
    label: "Cost of goods sold (from line 42)"
    type: Dollars
    expr: {op: copy, from: sc.line42}
  - id: sc.line5
    printed: "5 (sc.line5)"
    label: "Gross profit. Subtract line 4 from line 3"
    type: Dollars
    expr: {op: subtract, from: sc.line3, take: sc.line4}
  - id: sc.line7
    printed: "7 (sc.line7)"
    label: "Gross income. Add lines 5 and 6"
    type: Dollars
    expr: {op: sum, of: [sc.line5, sc.line6]}
  - id: sc.line9
    printed: "9 (sc.line9)"
    label: "Car and truck expenses (see instructions)"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.line9}
  - id: sc.line12
    printed: "12 (sc.line12)"
    label: "Depletion"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    refuses: [sc.special]
  - id: sc.line13
    printed: "13 (sc.line13)"
    label: "Depreciation and section 179 expense deduction (not included in Part III) (see instructions)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line22}
  - id: sc.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment"
    type: NonNegDollars
    expr: {op: copy, from: sc.rent_equipment}
  - id: sc.line24b
    printed: "24b"
    label: "Deductible meals (see instructions)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_meals50, sc.h_meals80, sc.meals_100]}
  - id: sc.line27a
    printed: "27a"
    label: "Energy efficient commercial bldgs deduction (attach Form 7205)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    refuses: [sc.special]
  - id: sc.line27b
    printed: "27b"
    label: "Other expenses (from line 48)"
    type: NonNegDollars
    expr: {op: copy, from: sc.line48}
  - id: sc.line28
    printed: "28"
    label: "Total expenses before expenses for business use of home. Add lines 8 through 27b"
    type: NonNegDollars
    expr: {op: sum, of: [sc.line8, sc.line9, sc.line10, sc.line11, sc.line12, sc.line13, sc.line14, sc.line15, sc.line16a, sc.line16b, sc.line17, sc.line18, sc.line19, sc.line20a, sc.line20b, sc.line21, sc.line22, sc.line23, sc.line24a, sc.line24b, sc.line25, sc.line26, sc.line27a, sc.line27b]}
  - id: sc.line29
    printed: "29"
    label: "Tentative profit or (loss). Subtract line 28 from line 7"
    type: Dollars
    expr: {op: subtract, from: sc.line7, take: sc.line28}
  - id: sc.ho_rate
    printed: "3a"
    label: "Maximum allowable amount"
    type: NonNegDollars
    expr: {op: param, ref: sc.ho_rate}
  - id: sc.ho_line4
    printed: "4 (sc.ho_line4)"
    label: "Multiply line 2 by line 3c"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sc.ho_rate, count: sc.ho_line2}
  - id: sc.ho_line1
    printed: "1 (sc.ho_line1)"
    label: "Enter the amount of the gross income limitation"
    type: Dollars
    expr: {op: copy, from: sc.ho_line1_source}
  - id: sc.ho_line5
    printed: "5 (sc.ho_line5)"
    label: "Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4 here and include that amount on Schedule C, line 30. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.ho_smaller, take: {const: 0}}
  - id: sc.line30
    printed: "30"
    label: "Expenses for business use of your home. Do not report these expenses elsewhere. Attach Form 8829 unless using the simplified method"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [sc.ho_uses, {const: true}]}, then: sc.ho_line5}, {guard: {op: test, eq: [sc.ho_uses, {const: false}]}, then: sc.h_zero}]}
    refuses: [sc.ho_other]
  - id: sc.line31
    printed: "31"
    label: "Net profit or (loss). Subtract line 30 from line 29"
    type: Dollars
    expr: {op: subtract, from: sc.line29, take: sc.line30}
    refuses: [sc.at_risk, sc.passive]
  - id: sc.line40
    printed: "40"
    label: "Add lines 35 through 39"
    type: NonNegDollars
    expr: {op: sum, of: [sc.line35, sc.line36, sc.line37, sc.line38, sc.line39]}
  - id: sc.line42
    printed: "42"
    label: "Cost of goods sold. Subtract line 41 from line 40. Enter the result here and on line 4"
    type: Dollars
    expr: {op: subtract, from: sc.line40, take: sc.line41}
  - id: sc.s179_allowed
    printed: "12 (sc.s179_allowed)"
    label: "Section 179 expense deduction"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line12}
  - id: sc.f7206_line2
    printed: "2 (sc.f7206_line2)"
    label: "For coverage under a qualified long-term care insurance contract, enter for each person covered the smaller of (a) or (b)"
    type: NonNegDollars
    expr: {op: sum_over, collection: ltc, field: ltc.amount}
  - id: sc.f7206_line3
    printed: "3 (sc.f7206_line3)"
    label: "Add lines 1 and 2"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f7206_line1, sc.f7206_line2]}
  - id: sc.f7206_line4
    printed: "4 (sc.f7206_line4)"
    label: "Enter your net profit and any other earned income from the trade or business under which the insurance plan is established"
    type: NonNegDollars
    expr: {op: copy, from: sc.profit_pos}
  - id: sc.f7206_line5
    printed: "5 (sc.f7206_line5)"
    label: "Enter the total of all net profits from Schedule C, Schedule F, or Schedule K-1 plus any other income allocable to the profitable businesses"
    type: NonNegDollars
    expr: {op: copy, from: person.positive_profits}
  - id: sc.f7206_line7
    printed: "7 (sc.f7206_line7)"
    label: "Multiply Schedule 1, line 15, deductible part of self-employment tax, by the percentage on line 6"
    type: NonNegDollars
    expr: {op: prorate, amount: person.se_line13, part: sc.f7206_line4, whole: sc.f7206_line5, places: 3}
  - id: sc.f7206_line8
    printed: "8 (sc.f7206_line8)"
    label: "Subtract line 7 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line4, take: sc.f7206_line7}
  - id: sc.f7206_line9
    printed: "9 (sc.f7206_line9)"
    label: "Enter the amount from Schedule 1, line 16, self-employed SEP, SIMPLE, and qualified plans, attributable to the same trade or business in which the insurance plan is established"
    type: NonNegDollars
    expr: {op: copy, from: person.plan_deduction}
  - id: sc.f7206_line10
    printed: "10 (sc.f7206_line10)"
    label: "Subtract line 9 from line 8"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line8, take: sc.f7206_line9}
  - id: sc.f7206_line13
    printed: "13 (sc.f7206_line13)"
    label: "Subtract line 12 from line 10 or line 11, whichever applies"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line10, take: {const: 0}}
  - id: sc.f7206_line14
    printed: "14 (sc.f7206_line14)"
    label: "Self-employed health insurance deduction. Enter the smaller of line 3 or line 13 here and on Schedule 1, line 17"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.f7206_line3, sc.f7206_line13]}
  - id: sc.qbi
    printed: "1(c)"
    label: "Qualified business income or (loss)"
    type: Dollars
    expr: {op: copy, from: sc.line31}
    note: "The archived Schedule C and Form 8995 pages do not give a business-by-business allocation of the person-level deductions (deductible part of self-employment tax, self-employed health insurance, and retirement plan contributions) that reduce QBI. This line reports the Schedule C net profit or loss before those person-level reductions."

  - id: sc.one
    printed: "(helper)"
    label: "Count of this business"
    type: Count
    expr: {op: param, ref: sc.one}
  - id: sc.rrta
    printed: "(helper)"
    label: "Railroad retirement compensation indicator for this person"
    type: Bool
    expr: {op: copy, from: person.rrta}
  - id: sc.line31_pre179
    printed: "(helper)"
    label: "Net profit or loss before the section 179 expense deduction"
    type: Dollars
    expr: {op: sum, of: [sc.line31, sc.s179_allowed]}
  - id: sc.result
    printed: "(helper)"
    label: "Schedule C net profit or loss reported on Schedule 1, line 3, and Schedule SE, line 2"
    type: Dollars
    expr: {op: copy, from: sc.line31}
  - id: sc.f6
    printed: "(helper)"
    label: "Total elected section 179 cost of property"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.s179}
  - id: sc.f14
    printed: "(helper)"
    label: "Special depreciation allowance for qualified property"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.bonus}
  - id: sc.f17
    printed: "(helper)"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs_prior}
  - id: sc.f19_y3
    printed: "(helper)"
    label: "MACRS depreciation deduction for 3-year property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y3"}]}}
  - id: sc.f19_y5
    printed: "(helper)"
    label: "MACRS depreciation deduction for 5-year property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y5"}]}}
  - id: sc.f19_y7
    printed: "(helper)"
    label: "MACRS depreciation deduction for 7-year property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y7"}]}}
  - id: sc.f19_y10
    printed: "(helper)"
    label: "MACRS depreciation deduction for 10-year property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y10"}]}}
  - id: sc.f19_y15
    printed: "(helper)"
    label: "MACRS depreciation deduction for 15-year property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y15"}]}}
  - id: sc.f19_y20
    printed: "(helper)"
    label: "MACRS depreciation deduction for 20-year property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y20"}]}}
  - id: sc.f19_y15sl
    printed: "(helper)"
    label: "MACRS depreciation deduction for 15-year straight line property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y15sl"}]}}
  - id: sc.f25
    printed: "(helper)"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year and used more than 50% in a qualified business use"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.f25}
  - id: sc.f26h
    printed: "(helper)"
    label: "Depreciation deduction for listed property used more than 50% in a qualified business use"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.dep_listed}
  - id: sc.f28
    printed: "(helper)"
    label: "Total listed property depreciation. Add amounts in column (h), lines 25 through 27"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f25, sc.f26h]}
  - id: sc.f29
    printed: "(helper)"
    label: "Total elected section 179 cost of listed property"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.f26i}
  - id: sc.mq_q4
    printed: "(helper)"
    label: "Total mid-quarter fourth-quarter depreciable basis"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_q4}
  - id: sc.mq_total
    printed: "(helper)"
    label: "Total mid-quarter depreciable basis"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_total}
  - id: sc.cost179
    printed: "(helper)"
    label: "Total cost of section 179 property placed in service"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.cost179}
  - id: sc.profit_pos
    printed: "(helper)"
    label: "Positive net profit from this business"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.line31, take: {const: 0}}

  - id: sc.h_meals50
    printed: "(helper)"
    label: "Business meals subject to the 50% limit, after applying the percentage"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_50, rate: {param: sc.meals_rate}}
  - id: sc.h_meals80
    printed: "(helper)"
    label: "Business meals subject to the 80% limit, after applying the percentage"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_80, rate: {param: sc.meals_rate_dot}}
  - id: sc.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sc.ho_line2
    printed: "(helper)"
    label: "Allowable square footage for the qualified business use, not more than 300 square feet"
    type: Count
    expr: {op: smaller_of, of: [sc.ho_sqft, sc.ho_max_sqft]}
  - id: sc.ho_line1_source
    printed: "(helper)"
    label: "Gross income limitation source amount from Schedule C, line 29"
    type: Dollars
    expr: {op: copy, from: sc.line29}
  - id: sc.ho_smaller
    printed: "(helper)"
    label: "Smaller of the gross income limitation and the simplified method amount"
    type: Dollars
    expr: {op: smaller_of, of: [sc.ho_line1, sc.ho_line4]}
```
