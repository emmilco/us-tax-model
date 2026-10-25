# Transcription agreement — sc

Second transcription of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` by an isolated model (spec 6.5), compared line by line with `forms/2025/sc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d3d357457ae71f3d486343c8a59bd8cb3b80ea1c175c2fb8ede30ea4b74eea04 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | f2becc16c3eeae8f68992cc2f01efbff5b42801963cbe3b20f870db4d59276b6 |
| printed lines compared | 55 |
| agree / disagree / missing | 14 / 34 / 7 |
| extra printed lines in second | 3, 4, 5, 7, 9, 12, 13 |

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
{"line": "(screen)"}
```

Second transcription's note: The supplied Schedule C text has no separate RRTA input for this business. The statutory-employee flag is the supplied flag that removes this business from Schedule SE, so it is used for this RRTA self-employment screening helper.

Ruling: open

### sc.line31_pre179 — Line 31 without the section 179 expense deduction
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"line": "30"}}
```

Second:

```json
{"from": {"from": {"line": "7"}, "op": "subtract", "take": {"from": {"line": "28"}, "op": "subtract", "take": {"line": "12 (sc.s179_allowed)"}}}, "op": "subtract", "take": {"line": "30"}}
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
{"line": "31"}
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
{"collection": "f4562", "field": "f4562.line19a", "op": "sum_over", "where": null}
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
{"collection": "f4562", "field": "f4562.line19b", "op": "sum_over", "where": null}
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
{"collection": "f4562", "field": "f4562.line19c", "op": "sum_over", "where": null}
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
{"collection": "f4562", "field": "f4562.line19d", "op": "sum_over", "where": null}
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
{"collection": "f4562", "field": "f4562.line19e", "op": "sum_over", "where": null}
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
{"collection": "f4562", "field": "f4562.line19f", "op": "sum_over", "where": null}
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

Second transcription's note: The supplied Form 4562 lines do not print a separate 15-year straight-line line. This helper totals asset entries whose MACRS period is y15sl and is not added again to Schedule C line 13 because line 19e already covers 15-year property.

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
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"collection": "asset", "field": "asset.mq_q4", "op": "sum_over", "where": null}
```

Ruling: open

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

Ruling: open

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

Ruling: open

### sc.profit_pos — Net profit of this business (zero for a loss)
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"of": [{"const": 0}, {"from": {"from": {"line": "7"}, "op": "subtract", "take": {"from": {"line": "28"}, "op": "subtract", "take": {"line": "12 (sc.s179_allowed)"}}}, "op": "subtract", "take": {"line": "30"}}], "op": "larger_of"}
```

Ruling: open

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MISSING**

Project:

```json
{"from": {"line": "1 (sc.line1)"}, "op": "subtract", "take": {"line": "2 (sc.line2)"}}
```

Second:

```json
None
```

Ruling: open

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MISSING**

Project:

```json
{"line": "42"}
```

Second:

```json
None
```

Ruling: open

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MISSING**

Project:

```json
{"from": {"line": "3 (sc.line3)"}, "op": "subtract", "take": {"line": "4 (sc.line4)"}}
```

Second:

```json
None
```

Ruling: open

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MISSING**

Project:

```json
{"of": [{"line": "5 (sc.line5)"}, {"line": "6"}], "op": "sum"}
```

Second:

```json
None
```

Ruling: open

### 9 (sc.line9) — Car and truck expenses
Status: **MISSING**

Project:

```json
{"collection": "scveh", "field": "scveh.line9", "op": "sum_over", "where": null}
```

Second:

```json
None
```

Ruling: open

### 12 (sc.line12) — Depletion
Status: **MISSING**

Project:

```json
{"const": 0}
```

Second:

```json
None
```

Ruling: open

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MISSING**

Project:

```json
{"of": [{"line": "12 (sc.s179_allowed)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}
```

Second:

```json
None
```

Ruling: open

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

### 24b — Deductible meals
Status: **AGREE**

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

### 27b — Other expenses (from line 48)
Status: **AGREE**

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "13 (sc.line13)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}], "op": "sum"}
```

Second:

```json
{"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12"}, {"line": "13"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9"}], "op": "sum"}
```

Ruling: open

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **DISAGREE**

Project:

```json
{"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"line": "28"}}
```

Second:

```json
{"from": {"line": "7"}, "op": "subtract", "take": {"line": "28"}}
```

Ruling: open

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
{"amount": {"line": "3a"}, "count": {"of": [{"line": "30(b)"}, {"param": "sc.ho_max_sqft"}], "op": "smaller_of"}, "op": "multiply_count"}
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
{"of": [{"const": 0}, {"of": [{"line": "1 (sc.ho_line1)"}, {"line": "4 (sc.ho_line4)"}], "op": "smaller_of"}], "op": "larger_of"}
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
{"alternatives": [{"guard": {"line": "(screen)"}, "then": {"line": "5 (sc.ho_line5)"}}, {"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

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
{"of": [{"const": 0}, {"line": "31"}], "op": "larger_of"}
```

Ruling: open

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **AGREE**

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 6, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"ref": "s1.line15"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 3, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Ruling: open

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **DISAGREE**

Project:

```json
{"from": {"line": "4 (sc.f7206_line4)"}, "op": "subtract_floor0", "take": {"line": "7 (sc.f7206_line7)"}}
```

Second:

```json
{"from": {"line": "4 (sc.f7206_line4)"}, "op": "subtract", "take": {"line": "7 (sc.f7206_line7)"}}
```

Ruling: open

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 6, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}, "op": "prorate", "part": {"of": [{"const": 0}, {"from": {"from": {"line": "7"}, "op": "subtract", "take": {"from": {"line": "28"}, "op": "subtract", "take": {"line": "12 (sc.s179_allowed)"}}}, "op": "subtract", "take": {"line": "30"}}], "op": "larger_of"}, "places": 3, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}
```

Ruling: open

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **DISAGREE**

Project:

```json
{"from": {"line": "8 (sc.f7206_line8)"}, "op": "subtract_floor0", "take": {"line": "9 (sc.f7206_line9)"}}
```

Second:

```json
{"from": {"line": "8 (sc.f7206_line8)"}, "op": "subtract", "take": {"line": "9 (sc.f7206_line9)"}}
```

Ruling: open

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **AGREE**

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"of": [{"line": "13 (sc.f7206_line13)"}, {"line": "3 (sc.f7206_line3)"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"line": "(screen)"}, "then": {"of": [{"line": "13 (sc.f7206_line13)"}, {"line": "3 (sc.f7206_line3)"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

### 1(c) — Qualified business income or (loss) of this business
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract", "take": {"of": [{"line": "14 (sc.f7206_line14)"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}], "op": "sum"}}
```

Second:

```json
{"from": {"line": "31"}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"line": "31"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "31"}], "test": "lt"}, "then": {"of": [{"line": "14 (sc.f7206_line14)"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}, "op": "prorate", "part": {"of": [{"const": 0}, {"from": {"from": {"line": "7"}, "op": "subtract", "take": {"from": {"line": "28"}, "op": "subtract", "take": {"line": "12 (sc.s179_allowed)"}}}, "op": "subtract", "take": {"line": "30"}}], "op": "larger_of"}, "places": 3, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"of": [{"const": 0}, {"from": {"from": {"line": "7"}, "op": "subtract", "take": {"from": {"line": "28"}, "op": "subtract", "take": {"line": "12 (sc.s179_allowed)"}}}, "op": "subtract", "take": {"line": "30"}}], "op": "larger_of"}, "places": 3, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}], "op": "sum"}}], "op": "choose"}}
```

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sc.line31_pre179 | sc.ho_screened, sc.special | sc.special |
| sc.result | sc.ho_screened, sc.loss_not_at_risk, sc.special | sc.loss_not_at_risk, sc.special |
| sc.profit_pos | sc.ho_screened, sc.special | sc.special |
| 27a | sc.special | sc.special |
| 28 | sc.special | sc.special |
| 29 | sc.special | sc.special |
| 1 (sc.ho_line1) | sc.special | sc.special |
| 5 (sc.ho_line5) | sc.special | sc.special |
| 30 | sc.ho_screened, sc.special | sc.special |
| 31 | sc.ho_screened, sc.special | sc.special |
| 4 (sc.f7206_line4) | sc.ho_screened, sc.special | sc.special |
| 7 (sc.f7206_line7) | sc.ho_screened, sc.special | sc.special |
| 8 (sc.f7206_line8) | sc.ho_screened, sc.special | sc.special |
| 10 (sc.f7206_line10) | sc.ho_screened, sc.special | sc.special |
| 13 (sc.f7206_line13) | sc.ho_screened, sc.special | sc.special |
| 14 (sc.f7206_line14) | sc.hi_screened, sc.ho_screened, sc.special | sc.special |
| 1(c) | sc.hi_screened, sc.ho_screened, sc.special | sc.special |

## Raw second transcription

```yaml
lines:
  - id: sc.line3
    printed: "3"
    label: "Subtract line 2 from line 1"
    type: Dollars
    expr: {op: subtract, from: sc.line1, take: sc.line2}
  - id: sc.line4
    printed: "4"
    label: "Cost of goods sold (from line 42)"
    type: Dollars
    expr: {op: copy, from: sc.line42}
  - id: sc.line5
    printed: "5"
    label: "Gross profit. Subtract line 4 from line 3"
    type: Dollars
    expr: {op: subtract, from: sc.line3, take: sc.line4}
  - id: sc.line7
    printed: "7"
    label: "Gross income. Add lines 5 and 6"
    type: Dollars
    expr: {op: sum, of: [sc.line5, sc.line6]}
  - id: sc.line9
    printed: "9"
    label: "Car and truck expenses"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.line9}
  - id: sc.line12
    printed: "12"
    label: "Depletion"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    refuses: [sc.special]
    note: "Only the no-depletion case is computed. The screening input sc.special covers depletion and the other unsupported special items."
  - id: sc.line13
    printed: "13"
    label: "Depreciation and section 179 expense deduction (not included in Part III)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.s179_allowed, sc.f14, sc.f17, sc.f19_y3, sc.f19_y5, sc.f19_y7, sc.f19_y10, sc.f19_y15, sc.f19_y20, sc.f28]}
    note: "Follows Form 4562 line 22 as supplied: section 179 line 12 plus lines 14 and 17, the MACRS line 19(g) amounts, and line 21 (line 28). The y15sl helper is not added again because the supplied Form 4562 line 19e 15-year category already includes 15-year straight-line property."
  - id: sc.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment"
    type: NonNegDollars
    expr: {op: sum, of: [sc.rent_equipment, sc.veh_lease]}
  - id: sc.line24b
    printed: "24b"
    label: "Deductible meals"
    type: NonNegDollars
    expr: {op: sum, of: [sc.meals_50_ded, sc.meals_80_ded, sc.meals_100]}
  - id: sc.line27a
    printed: "27a"
    label: "Energy efficient commercial buildings deduction (attach Form 7205)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    refuses: [sc.special]
    note: "Only the no-Form-7205 case is computed. The screening input sc.special covers the energy efficient commercial buildings deduction and the other unsupported special items."
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
    expr: {op: multiply_count, amount: sc.ho_rate, count: sc.ho_cap_sqft}
  - id: sc.ho_line1
    printed: "1 (sc.ho_line1)"
    label: "Enter the amount of the gross income limitation"
    type: Dollars
    expr: {op: copy, from: sc.line29}
    note: "The supplied worksheet text also adds or subtracts specified Form 8949, Schedule D and Form 4797 gains and losses allocable to the business. No inputs for those amounts are in this closed interface, so the supported case uses Schedule C line 29."
  - id: sc.ho_line5
    printed: "5 (sc.ho_line5)"
    label: "Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4 here and include that amount on Schedule C, line 30. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: larger_of, of: [sc.ho_min, sc.zero]}
  - id: sc.line30
    printed: "30"
    label: "Expenses for business use of your home. Do not report these expenses elsewhere. Attach Form 8829 unless using the simplified method."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: sc.ho_uses
          then: sc.ho_line5
        - guard: {op: test, eq: [sc.ho_uses, {const: false}]}
          then: sc.zero
    refuses: [sc.ho_screened]
  - id: sc.line31
    printed: "31"
    label: "Net profit or (loss). Subtract line 30 from line 29."
    type: Dollars
    expr: {op: subtract, from: sc.line29, take: sc.line30}
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
    expr: {op: larger_of, of: [sc.line31, sc.zero]}
  - id: sc.f7206_line5
    printed: "5 (sc.f7206_line5)"
    label: "Enter the total of all net profits from Schedule C, Schedule F, or Schedule K-1, plus any other income allocable to the profitable businesses. Don't include any net losses"
    type: NonNegDollars
    expr: {op: copy, from: person.positive_profits}
  - id: sc.f7206_line7
    printed: "7 (sc.f7206_line7)"
    label: "Multiply Schedule 1, line 15, deductible part of self-employment tax, by the percentage on line 6"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sc.f7206_line4, sc.zero]}
          then: sc.f7206_line7_calc
        - guard: {op: test, not: {op: test, gt: [sc.f7206_line4, sc.zero]}}
          then: sc.zero
  - id: sc.f7206_line8
    printed: "8 (sc.f7206_line8)"
    label: "Subtract line 7 from line 4"
    type: NonNegDollars
    expr: {op: subtract, from: sc.f7206_line4, take: sc.f7206_line7}
  - id: sc.f7206_line9
    printed: "9 (sc.f7206_line9)"
    label: "Enter the amount, if any, from Schedule 1, line 16, self-employed SEP, SIMPLE, and qualified plans, attributable to the same trade or business in which the insurance plan is established"
    type: NonNegDollars
    expr: {op: copy, from: sc.qbi_plan}
  - id: sc.f7206_line10
    printed: "10 (sc.f7206_line10)"
    label: "Subtract line 9 from line 8"
    type: NonNegDollars
    expr: {op: subtract, from: sc.f7206_line8, take: sc.f7206_line9}
  - id: sc.f7206_line13
    printed: "13 (sc.f7206_line13)"
    label: "Subtract line 12 from line 10 or 11, whichever applies"
    type: NonNegDollars
    expr: {op: copy, from: sc.f7206_line10}
    note: "The closed interface has no Form 2555 line 45 amount and no S-corporation Medicare-wage alternative, so line 13 is the line 10 amount."
  - id: sc.f7206_line14
    printed: "14 (sc.f7206_line14)"
    label: "Self-employed health insurance deduction. Enter the smaller of line 3 or line 13 here and on Schedule 1, line 17. Don't include this amount when figuring any medical expense deduction on Schedule A"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: sc.hi_uses
          then: sc.f7206_min
        - guard: {op: test, eq: [sc.hi_uses, {const: false}]}
          then: sc.zero
    refuses: [sc.hi_screened]
  - id: sc.qbi
    printed: "1(c)"
    label: "Net qualified business income or (loss) for the trade, business, or aggregation"
    type: Dollars
    expr: {op: subtract, from: sc.line31, take: sc.qbi_ded}
  - id: sc.zero
    printed: "(helper)"
    label: "Zero-valued money helper"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sc.one
    printed: "(helper)"
    label: "Count one helper"
    type: Count
    expr: {op: param, ref: sc.one}
  - id: sc.rrta
    printed: "(helper)"
    label: "Statutory employee indicator for this business"
    type: Bool
    expr: {op: copy, from: sc.statutory}
    note: "The supplied Schedule C text has no separate RRTA input for this business. The statutory-employee flag is the supplied flag that removes this business from Schedule SE, so it is used for this RRTA self-employment screening helper."
  - id: sc.veh_lease
    printed: "(helper)"
    label: "Business vehicle lease payments from Schedule C line 20a entries"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.line20a}
  - id: sc.meals_50_ded
    printed: "(helper)"
    label: "Deductible part of meals subject to the 50% limit"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_50, rate: {param: sc.meals_rate}}
  - id: sc.meals_80_ded
    printed: "(helper)"
    label: "Deductible part of meals subject to the 80% limit"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_80, rate: {param: sc.meals_rate_dot}}
  - id: sc.ho_cap_sqft
    printed: "(helper)"
    label: "Allowable square footage capped at 300"
    type: Count
    expr: {op: smaller_of, of: [sc.ho_sqft, {param: sc.ho_max_sqft}]}
  - id: sc.ho_min
    printed: "(helper)"
    label: "Smaller of simplified-method line 1 or line 4"
    type: Dollars
    expr: {op: smaller_of, of: [sc.ho_line1, sc.ho_line4]}
  - id: sc.ho_screened
    printed: "(helper)"
    label: "Home deduction uses a supported simplified-method case"
    type: Bool
    expr: {op: test, all: [sc.ho_uses, sc.ho_other]}
  - id: sc.line28_pre179
    printed: "(helper)"
    label: "Total expenses before section 179"
    type: NonNegDollars
    expr: {op: subtract, from: sc.line28, take: sc.s179_allowed}
  - id: sc.line29_pre179
    printed: "(helper)"
    label: "Tentative profit or loss before section 179"
    type: Dollars
    expr: {op: subtract, from: sc.line7, take: sc.line28_pre179}
  - id: sc.line31_pre179
    printed: "(helper)"
    label: "Net profit or loss before section 179"
    type: Dollars
    expr: {op: subtract, from: sc.line29_pre179, take: sc.line30}
  - id: sc.loss
    printed: "(helper)"
    label: "Schedule C line 31 is a loss"
    type: Bool
    expr: {op: test, lt: [sc.line31, sc.zero]}
  - id: sc.not_at_risk
    printed: "(helper)"
    label: "Some investment is not at risk"
    type: Bool
    expr: {op: test, eq: [sc.at_risk, {const: false}]}
  - id: sc.loss_not_at_risk
    printed: "(helper)"
    label: "Loss with some investment not at risk"
    type: Bool
    expr: {op: test, all: [sc.loss, sc.not_at_risk]}
  - id: sc.result
    printed: "(helper)"
    label: "Schedule C result after the supported at-risk screening"
    type: Dollars
    expr: {op: copy, from: sc.line31}
    refuses: [sc.loss_not_at_risk]
  - id: sc.f6
    printed: "(helper)"
    label: "Form 4562 line 6(c) elected section 179 cost total"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.s179}
  - id: sc.f14
    printed: "(helper)"
    label: "Form 4562 line 14 special depreciation allowance total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line14}
  - id: sc.f17
    printed: "(helper)"
    label: "Form 4562 line 17 MACRS deductions for prior-year assets total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line17}
  - id: sc.f19_y3
    printed: "(helper)"
    label: "Form 4562 line 19a 3-year property total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line19a}
  - id: sc.f19_y5
    printed: "(helper)"
    label: "Form 4562 line 19b 5-year property total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line19b}
  - id: sc.f19_y7
    printed: "(helper)"
    label: "Form 4562 line 19c 7-year property total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line19c}
  - id: sc.f19_y10
    printed: "(helper)"
    label: "Form 4562 line 19d 10-year property total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line19d}
  - id: sc.f19_y15
    printed: "(helper)"
    label: "Form 4562 line 19e 15-year property total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line19e}
  - id: sc.f19_y20
    printed: "(helper)"
    label: "Form 4562 line 19f 20-year property total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line19f}
  - id: sc.f19_y15sl
    printed: "(helper)"
    label: "15-year straight-line MACRS amount from asset entries"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where: {op: test, eq: [asset.period, {const: "y15sl"}]}
    note: "The supplied Form 4562 lines do not print a separate 15-year straight-line line. This helper totals asset entries whose MACRS period is y15sl and is not added again to Schedule C line 13 because line 19e already covers 15-year property."
  - id: sc.f25
    printed: "(helper)"
    label: "Form 4562 line 25 listed property special depreciation allowance total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line25}
  - id: sc.f26h
    printed: "(helper)"
    label: "Form 4562 line 26(h) listed property depreciation total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line26h}
  - id: sc.f28
    printed: "(helper)"
    label: "Form 4562 line 28 listed property total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line28}
  - id: sc.f29
    printed: "(helper)"
    label: "Form 4562 line 29 listed property elected section 179 cost total"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line29}
  - id: sc.mq_q4
    printed: "(helper)"
    label: "Mid-quarter Q4 amount from asset entries"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_q4}
  - id: sc.mq_total
    printed: "(helper)"
    label: "Mid-quarter total from asset entries"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_total}
  - id: sc.cost179
    printed: "(helper)"
    label: "Section 179 cost from asset entries"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.cost179}
  - id: sc.profit_pos
    printed: "(helper)"
    label: "Positive Schedule C profit before section 179"
    type: NonNegDollars
    expr: {op: larger_of, of: [sc.line31_pre179, sc.zero]}
  - id: sc.hi_screened
    printed: "(helper)"
    label: "Health insurance uses a supported case"
    type: Bool
    expr: {op: test, all: [sc.hi_uses, sc.hi_screen]}
  - id: sc.f7206_line7_calc
    printed: "(helper)"
    label: "Form 7206 line 7 calculated percentage allocation"
    type: NonNegDollars
    expr: {op: prorate, amount: s1.line15, part: sc.f7206_line4, whole: sc.f7206_line5, places: 3}
  - id: sc.f7206_min
    printed: "(helper)"
    label: "Smaller of Form 7206 line 3 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.f7206_line3, sc.f7206_line13]}
  - id: sc.qbi_se_calc
    printed: "(helper)"
    label: "Allocated deductible part of self-employment tax for QBI"
    type: NonNegDollars
    expr: {op: prorate, amount: person.se_line13, part: sc.profit_pos, whole: person.positive_profits, places: 3}
  - id: sc.qbi_se
    printed: "(helper)"
    label: "Deductible part of self-employment tax allocated to this business for QBI"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [person.positive_profits, sc.zero]}
          then: sc.qbi_se_calc
        - guard: {op: test, eq: [person.positive_profits, sc.zero]}
          then: sc.zero
  - id: sc.qbi_plan_calc
    printed: "(helper)"
    label: "Allocated retirement plan deduction for QBI"
    type: NonNegDollars
    expr: {op: prorate, amount: person.plan_deduction, part: sc.profit_pos, whole: person.positive_profits, places: 3}
  - id: sc.qbi_plan
    printed: "(helper)"
    label: "Retirement plan deduction allocated to this business for QBI"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [person.positive_profits, sc.zero]}
          then: sc.qbi_plan_calc
        - guard: {op: test, eq: [person.positive_profits, sc.zero]}
          then: sc.zero
  - id: sc.qbi_ded_calc
    printed: "(helper)"
    label: "QBI deductions allocated to this business"
    type: NonNegDollars
    expr: {op: sum, of: [sc.qbi_se, sc.qbi_plan, sc.f7206_line14]}
  - id: sc.qbi_ded
    printed: "(helper)"
    label: "QBI deductions allowed for this business"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sc.line31, sc.zero]}
          then: sc.qbi_ded_calc
        - guard: {op: test, not: {op: test, gt: [sc.line31, sc.zero]}}
          then: sc.zero
```
