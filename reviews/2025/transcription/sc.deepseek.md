# Transcription agreement — sc

Second transcription of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` by an isolated model (spec 6.5), compared line by line with `forms/2025/sc.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 632f9e265413f19f5e52a4fa88b2d14ad89617becb42bc96eafb64e13b73e392 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 05f45aa981f458eb86c17a381396370038b4a6a90a758cb7b45a42678650b81d |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 131072 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 4607a00dac7de74c9c7fb227b2ed575b6dbe22cdd9463e03f53f0a97e1b9a8a0 |
| printed lines compared | 55 |
| agree / disagree / missing | 22 / 33 / 0 |
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
- malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object
- malformed expression (project schema): data/all/0 must be object, data/all/0 must be object, data/all/0 must be object
- sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money
- sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money
- sc.sc.h_ho_sqft_capped: declared count but the expression produces money
- sc.sc.h_at_risk_bad: malformed expression
- sc.sc.h_passive_bad: malformed expression

## Lines

### sc.one — One business
Status: **AGREE**

### sc.rrta — This business's owner has railroad retirement compensation
Status: **DISAGREE**

Project:

```json
{"ref": "person.rrta"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.rrta"}], "test": "eq"}], "test": "all"}
```

Ruling: open

### sc.line31_pre179 — Line 31 without the section 179 expense deduction
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"line": "30"}}
```

Second:

```json
{"expression": {"of": [{"line": "12 (sc.s179_allowed)"}, {"line": "31"}], "op": "sum"}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

### sc.result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}
```

Second:

```json
{"expression": {"line": "31"}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

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

Ruling: open

### sc.f14 — Special allowance on property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "f4562", "field": "f4562.line14", "op": "sum_over", "where": null}
```

Ruling: open

### sc.f17 — MACRS on earlier property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "f4562", "field": "f4562.line17", "op": "sum_over", "where": null}
```

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

### sc.f25 — Line 25 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "f4562", "field": "f4562.line25", "op": "sum_over", "where": null}
```

Ruling: open

### sc.f26h — Column (h), line 26, for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "f4562", "field": "f4562.line26h", "op": "sum_over", "where": null}
```

Ruling: open

### sc.f28 — Line 28 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}
```

Second:

```json
{"collection": "f4562", "field": "f4562.line28", "op": "sum_over", "where": null}
```

Ruling: open

### sc.f29 — Line 29 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "f4562", "field": "f4562.line29", "op": "sum_over", "where": null}
```

Ruling: open

### sc.mq_q4 — mq_q4 of this business
Status: **AGREE**

### sc.mq_total — mq_total of this business
Status: **AGREE**

### sc.cost179 — cost179 of this business
Status: **AGREE**

### sc.profit_pos — Net profit of this business (zero for a loss)
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"expression": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

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

Ruling: open

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

Ruling: open

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
{"expression": {"amount": {"line": "3a"}, "count": {"of": [{"line": "30(b)"}, {"param": "sc.ho_max_sqft"}], "op": "smaller_of"}, "op": "multiply_count"}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

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
{"expression": {"from": {"of": [{"line": "1 (sc.ho_line1)"}, {"line": "4 (sc.ho_line4)"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

### 30 — Expenses for business use of your home
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"line": "5 (sc.ho_line5)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"line": "5 (sc.ho_line5)"}}], "op": "choose"}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **DISAGREE**

Project:

```json
{"from": {"line": "29"}, "op": "subtract", "take": {"line": "30"}}
```

Second:

```json
{"expression": {"from": {"line": "29"}, "op": "subtract", "take": {"line": "30"}}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

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

Ruling: open

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
{"expression": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

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
{"expression": {"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"ref": "s1.line15"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 9, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Second transcription's note: Form 7206 line 6 does not state a rounding rule; this line applies prorate with 9 decimal places to the line 4/line 5 ratio.

Ruling: open

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **DISAGREE**

Project:

```json
{"from": {"line": "4 (sc.f7206_line4)"}, "op": "subtract_floor0", "take": {"line": "7 (sc.f7206_line7)"}}
```

Second:

```json
{"expression": {"from": {"line": "4 (sc.f7206_line4)"}, "op": "subtract_floor0", "take": {"line": "7 (sc.f7206_line7)"}}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 6, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Second:

```json
{"ref": "s1.line16"}
```

Second transcription's note: The supplied interface provides only the Schedule 1 line 16 total, not a per-business allocation; this line uses that total.

Ruling: open

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **DISAGREE**

Project:

```json
{"from": {"line": "8 (sc.f7206_line8)"}, "op": "subtract_floor0", "take": {"line": "9 (sc.f7206_line9)"}}
```

Second:

```json
{"expression": {"from": {"line": "8 (sc.f7206_line8)"}, "op": "subtract_floor0", "take": {"line": "9 (sc.f7206_line9)"}}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **DISAGREE**

Project:

```json
{"line": "10 (sc.f7206_line10)"}
```

Second:

```json
{"expression": {"line": "10 (sc.f7206_line10)"}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"of": [{"line": "13 (sc.f7206_line13)"}, {"line": "3 (sc.f7206_line3)"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"of": [{"line": "13 (sc.f7206_line13)"}, {"line": "3 (sc.f7206_line3)"}], "op": "smaller_of"}}], "op": "choose"}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Ruling: open

### 1(c) — Qualified business income or (loss) of this business
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract", "take": {"of": [{"line": "14 (sc.f7206_line14)"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}], "op": "sum"}}
```

Second:

```json
{"expression": {"line": "31"}, "invalid_model_types": [{"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.ho_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: operand 'sc.h_ho_max_sqft' is not money"}, {"line": "sc.h_ho_sqft_capped", "message": "sc.sc.h_ho_sqft_capped: declared count but the expression produces money"}]}
```

Second transcription's note: The supplied text and inputs do not provide a per-business allocation of the deductible part of self-employment tax, retirement plan contributions, or similar QBI reductions; this line reports the Schedule C net profit as the business's QBI.

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sc.line31_pre179 | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| sc.result | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| sc.profit_pos | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| 12 (sc.line12) | sc.special | sc.special |
| 27a | sc.special | sc.special |
| 28 | sc.special | sc.special |
| 29 | sc.special | sc.special |
| 1 (sc.ho_line1) | sc.special | sc.special |
| 5 (sc.ho_line5) | sc.special | sc.special |
| 30 | sc.h_ho_bad, sc.special | sc.h_ho_bad, sc.special |
| 31 | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| 4 (sc.f7206_line4) | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| 7 (sc.f7206_line7) | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| 8 (sc.f7206_line8) | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| 10 (sc.f7206_line10) | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| 13 (sc.f7206_line13) | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| 14 (sc.f7206_line14) | sc.h_at_risk_bad, sc.h_hi_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_hi_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |
| 1(c) | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special | sc.h_at_risk_bad, sc.h_ho_bad, sc.h_passive_bad, sc.special |

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
    label: "Car and truck expenses"
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
    label: "Depreciation and section 179 expense deduction (not included in Part III)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line22}
  - id: sc.line20a
    printed: "20a"
    label: "Rent or lease: vehicles, machinery, and equipment"
    type: NonNegDollars
    expr: {op: copy, from: sc.rent_equipment}
  - id: sc.line24b
    printed: "24b"
    label: "Deductible meals"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_meals_50_ded, sc.h_meals_80_ded, sc.meals_100]}
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
    expr: {op: multiply_count, amount: sc.ho_rate, count: sc.h_ho_sqft_capped}
  - id: sc.ho_line1
    printed: "1 (sc.ho_line1)"
    label: "Enter the amount of the gross income limitation"
    type: Dollars
    expr: {op: copy, from: sc.line29}
  - id: sc.ho_line5
    printed: "5 (sc.ho_line5)"
    label: "Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4 here and include that amount on Schedule C, line 30. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.h_ho_line5_raw, take: {const: 0}}
  - id: sc.line30
    printed: "30"
    label: "Expenses for business use of your home"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sc.ho_uses, {const: false}]}
          then: sc.h_zero
        - guard: {op: test, eq: [sc.ho_uses, {const: true}]}
          then: sc.ho_line5
    refuses: [sc.h_ho_bad]
  - id: sc.line31
    printed: "31"
    label: "Net profit or (loss). Subtract line 30 from line 29"
    type: Dollars
    expr: {op: copy, from: sc.h_line31_pre}
    refuses: [sc.special, sc.h_at_risk_bad, sc.h_passive_bad]
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
    expr: {op: subtract_floor0, from: sc.line31, take: {const: 0}}
  - id: sc.f7206_line5
    printed: "5 (sc.f7206_line5)"
    label: "Enter the total of all net profits from Schedule C, Schedule F, or Schedule K-1, plus other income allocable to profitable businesses. Do not include net losses"
    type: NonNegDollars
    expr: {op: copy, from: person.positive_profits}
  - id: sc.f7206_line7
    printed: "7 (sc.f7206_line7)"
    label: "Multiply Schedule 1 line 15, deductible part of self-employment tax, by the percentage on line 6"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sc.f7206_line4, {const: 0}]}
          then: sc.h_zero
        - guard: {op: test, ne: [sc.f7206_line4, {const: 0}]}
          then: sc.h_f7206_line7_calc
    note: "Form 7206 line 6 does not state a rounding rule; this line applies prorate with 9 decimal places to the line 4/line 5 ratio."
  - id: sc.f7206_line8
    printed: "8 (sc.f7206_line8)"
    label: "Subtract line 7 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line4, take: sc.f7206_line7}
  - id: sc.f7206_line9
    printed: "9 (sc.f7206_line9)"
    label: "Enter the amount, if any, from Schedule 1 line 16 attributable to the same trade or business in which the insurance plan is established"
    type: NonNegDollars
    expr: {op: copy, from: s1.line16}
    note: "The supplied interface provides only the Schedule 1 line 16 total, not a per-business allocation; this line uses that total."
  - id: sc.f7206_line10
    printed: "10 (sc.f7206_line10)"
    label: "Subtract line 9 from line 8"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line8, take: sc.f7206_line9}
  - id: sc.f7206_line13
    printed: "13 (sc.f7206_line13)"
    label: "Subtract line 12 from line 10 or line 11, whichever applies"
    type: NonNegDollars
    expr: {op: copy, from: sc.f7206_line10}
  - id: sc.f7206_line14
    printed: "14 (sc.f7206_line14)"
    label: "Self-employed health insurance deduction. Enter the smaller of line 3 or line 13 here and on Schedule 1, line 17"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sc.hi_uses, {const: false}]}
          then: sc.h_zero
        - guard: {op: test, eq: [sc.hi_uses, {const: true}]}
          then: sc.h_f7206_min
    refuses: [sc.h_hi_bad]
  - id: sc.qbi
    printed: "1(c)"
    label: "Qualified business income or (loss)"
    type: Dollars
    expr: {op: copy, from: sc.line31}
    note: "The supplied text and inputs do not provide a per-business allocation of the deductible part of self-employment tax, retirement plan contributions, or similar QBI reductions; this line reports the Schedule C net profit as the business's QBI."
  - id: sc.one
    printed: "(helper)"
    label: "Count of this business"
    type: Count
    expr: {op: param, ref: sales.one}
  - id: sc.rrta
    printed: "(helper)"
    label: "This business's income is railroad retirement compensation reported as a statutory employee"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [sc.statutory, {const: true}]}, {op: test, eq: [person.rrta, {const: true}]}]}
  - id: sc.line31_pre179
    printed: "(helper)"
    label: "Net profit before section 179"
    type: Dollars
    expr: {op: sum, of: [sc.line31, sc.s179_allowed]}
  - id: sc.result
    printed: "(helper)"
    label: "Schedule C net profit or loss after limitations"
    type: Dollars
    expr: {op: copy, from: sc.line31}
  - id: sc.f6
    printed: "(helper)"
    label: "Total elected cost of section 179 property (Form 4562 line 6, column (c))"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.s179}
  - id: sc.f14
    printed: "(helper)"
    label: "Special depreciation allowance for qualified property (Form 4562 line 14)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line14}
  - id: sc.f17
    printed: "(helper)"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025 (Form 4562 line 17)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line17}
  - id: sc.f19_y3
    printed: "(helper)"
    label: "3-year property MACRS deduction (Form 4562 line 19a, column (g))"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y3"}]}}
  - id: sc.f19_y5
    printed: "(helper)"
    label: "5-year property MACRS deduction (Form 4562 line 19b, column (g))"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y5"}]}}
  - id: sc.f19_y7
    printed: "(helper)"
    label: "7-year property MACRS deduction (Form 4562 line 19c, column (g))"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y7"}]}}
  - id: sc.f19_y10
    printed: "(helper)"
    label: "10-year property MACRS deduction (Form 4562 line 19d, column (g))"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y10"}]}}
  - id: sc.f19_y15
    printed: "(helper)"
    label: "15-year property MACRS deduction (Form 4562 line 19e, column (g))"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y15"}]}}
  - id: sc.f19_y20
    printed: "(helper)"
    label: "20-year property MACRS deduction (Form 4562 line 19f, column (g))"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y20"}]}}
  - id: sc.f19_y15sl
    printed: "(helper)"
    label: "15-year straight-line property MACRS deduction"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.macrs2025, where: {op: test, eq: [asset.period, {const: "y15sl"}]}}
  - id: sc.f25
    printed: "(helper)"
    label: "Special depreciation allowance for qualified listed property (Form 4562 line 25)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line25}
  - id: sc.f26h
    printed: "(helper)"
    label: "Depreciation deduction for listed property used more than 50% in a qualified business use (Form 4562 line 26(h))"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line26h}
  - id: sc.f28
    printed: "(helper)"
    label: "Total listed property depreciation (Form 4562 line 28)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line28}
  - id: sc.f29
    printed: "(helper)"
    label: "Elected section 179 cost of listed property (Form 4562 line 29)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line29}
  - id: sc.mq_q4
    printed: "(helper)"
    label: "Fourth-quarter depreciable basis for mid-quarter convention"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_asset_mq_q4, sc.h_scveh_mq_q4]}
  - id: sc.mq_total
    printed: "(helper)"
    label: "Total depreciable basis for mid-quarter convention"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_asset_mq_total, sc.h_scveh_mq_total]}
  - id: sc.cost179
    printed: "(helper)"
    label: "Total cost of section 179 property placed in service"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_asset_cost179, sc.h_scveh_cost179]}
  - id: sc.profit_pos
    printed: "(helper)"
    label: "Positive net profit"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.line31, take: {const: 0}}
  - id: sc.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sc.h_ho_max_sqft
    printed: "(helper)"
    label: "Maximum allowable square footage"
    type: Count
    expr: {op: param, ref: sc.ho_max_sqft}
  - id: sc.h_ho_sqft_capped
    printed: "(helper)"
    label: "Allowable square footage, not more than 300 square feet"
    type: Count
    expr: {op: smaller_of, of: [sc.ho_sqft, sc.h_ho_max_sqft]}
  - id: sc.h_meals_50_ded
    printed: "(helper)"
    label: "Meals subject to the 50% limit, deductible amount"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_50, rate: {param: sc.meals_rate}}
  - id: sc.h_meals_80_ded
    printed: "(helper)"
    label: "Meals subject to the 80% limit, deductible amount"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_80, rate: {param: sc.meals_rate_dot}}
  - id: sc.h_ho_line5_raw
    printed: "(helper)"
    label: "Smaller of line 1 or line 4 before the zero floor"
    type: Dollars
    expr: {op: smaller_of, of: [sc.ho_line1, sc.ho_line4]}
  - id: sc.h_ho_bad
    printed: "(helper)"
    label: "Home office simplified method is unsupported for this home office"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [sc.ho_uses, {const: true}]}, {op: test, eq: [sc.ho_other, {const: true}]}]}
  - id: sc.h_line31_pre
    printed: "(helper)"
    label: "Net profit or loss before at-risk and passive activity limits"
    type: Dollars
    expr: {op: subtract, from: sc.line29, take: sc.line30}
  - id: sc.h_line31_loss
    printed: "(helper)"
    label: "Whether the Schedule C result before limitations is a loss"
    type: Bool
    expr: {op: test, lt: [sc.h_line31_pre, {const: 0}]}
  - id: sc.h_at_risk_bad
    printed: "(helper)"
    label: "Loss with some investment not at risk; Form 6198 required"
    type: Bool
    expr: {op: test, all: [sc.h_line31_loss, {op: test, eq: [sc.at_risk, {const: false}]}]}
  - id: sc.h_passive_bad
    printed: "(helper)"
    label: "Loss from a passive activity; Form 8582 required"
    type: Bool
    expr: {op: test, all: [sc.h_line31_loss, {op: test, eq: [sc.passive, {const: false}]}]}
  - id: sc.h_f7206_line7_calc
    printed: "(helper)"
    label: "Form 7206 line 7 prorated amount"
    type: NonNegDollars
    expr: {op: prorate, amount: s1.line15, part: sc.f7206_line4, whole: sc.f7206_line5, places: 9}
  - id: sc.h_f7206_min
    printed: "(helper)"
    label: "Smaller of Form 7206 line 3 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.f7206_line3, sc.f7206_line13]}
  - id: sc.h_hi_bad
    printed: "(helper)"
    label: "Health insurance deduction is unsupported for this business"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [sc.hi_uses, {const: true}]}, {op: test, eq: [sc.hi_screen, {const: true}]}]}
  - id: sc.h_asset_mq_q4
    printed: "(helper)"
    label: "Asset fourth-quarter depreciable basis"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_q4}
  - id: sc.h_scveh_mq_q4
    printed: "(helper)"
    label: "Vehicle fourth-quarter depreciable basis"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.mq_q4}
  - id: sc.h_asset_mq_total
    printed: "(helper)"
    label: "Asset total depreciable basis"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_total}
  - id: sc.h_scveh_mq_total
    printed: "(helper)"
    label: "Vehicle total depreciable basis"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.mq_total}
  - id: sc.h_asset_cost179
    printed: "(helper)"
    label: "Asset section 179 cost"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.cost179}
  - id: sc.h_scveh_cost179
    printed: "(helper)"
    label: "Vehicle section 179 cost"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.cost179}
```
