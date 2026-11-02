# Transcription agreement — sc

Second transcription of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` by an isolated model (spec 6.5), compared line by line with `forms/2025/sc.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 632f9e265413f19f5e52a4fa88b2d14ad89617becb42bc96eafb64e13b73e392 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 77ffe343af2fce8035d610ce0402f550201a497c7d9c1db36012de12ce11eb53 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 4607a00dac7de74c9c7fb227b2ed575b6dbe22cdd9463e03f53f0a97e1b9a8a0 |
| printed lines compared | 55 |
| agree / disagree / missing | 30 / 25 / 0 |
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
{"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}
```

Second transcription's note: The IRS pages do not define a per-business RRTA fact. Schedule SE line 8a combines railroad retirement compensation with wages only when there is self-employment income, so this flag is read as 'this business contributes to Schedule SE' (not statutory-employee income). This is an interpretation, not a determination from the text.

Ruling: open

### sc.line31_pre179 — Line 31 without the section 179 expense deduction
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"line": "30"}}
```

Second:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.bonus_allowed", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"from": {"of": [{"line": "4 (sc.ho_line4)"}, {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.bonus_allowed", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}}
```

Second transcription's note: Pub. 946 and i4562 line 11 say business taxable income is figured without regard to the section 179 deduction (and without the half SE tax deduction). The home office gross income limit is also refigured on this pre-179 income. That is a reading, chosen so the computation is not circular.

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
Status: **AGREE**

### sc.f14 — Special allowance on property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "asset", "field": "asset.bonus", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
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
{"collection": "asset", "field": "asset.macrs_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
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
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
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
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
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
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
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
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
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
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
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
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
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
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
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
{"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.bonus_allowed", "op": "sum_over", "where": null}], "op": "sum"}
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
{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}
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
{"of": [{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.bonus_allowed", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}
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
{"of": [{"collection": "asset", "field": "asset.f26i", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}
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
{"from": {"line": "31"}, "op": "subtract_floor0", "take": {"const": 0}}
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
{"of": [{"line": "12 (sc.s179_allowed)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.bonus_allowed", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}
```

Second transcription's note: This is Form 4562 line 22 for this business, composed directly from its parts. The section 179 part (line 12) is kept separate so that the section 179 business income limit can be figured without it (see sc.line31_pre179).

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
{"of": [{"amount": {"line": "3a"}, "count": {"line": "30(b)"}, "op": "multiply_count"}, {"amount": {"line": "3a"}, "count": {"param": "sc.ho_max_sqft"}, "op": "multiply_count"}], "op": "smaller_of"}
```

Second transcription's note: Line 2 is the smaller of the square feet used or 300 (full-year use only; part-year use is screened by sc.ho_other). Because $5 x min(a, 300) = min($5 x a, $5 x 300), this line takes the smaller of the two products.

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
{"from": {"of": [{"line": "1 (sc.ho_line1)"}, {"line": "4 (sc.ho_line4)"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: open

### 30 — Expenses for business use of your home
Status: **AGREE**

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"of": [{"of": [{"collection": "asset", "field": "asset.f26i", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "test": "lt"}, {"args": [{"ref": "s179.line12"}, {"ref": "s179.line8"}], "test": "ne"}], "test": "all"}, "then": {"ref": "s179.line12"}}, {"guard": {"args": [{"args": [{"ref": "s179.line12"}, {"ref": "s179.line8"}], "test": "eq"}, {"args": [{"of": [{"of": [{"collection": "asset", "field": "asset.f26i", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.f26i", "op": "sum_over", "where": null}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}, {"ref": "s179.line12"}], "op": "smaller_of"}}], "op": "choose"}
```

Second transcription's note: The i4562 line 12 instructions let you allocate the taxpayer-level deduction among businesses 'in any manner' without fixing a rule. The reading chosen: when the summary line 12 equals the total elected cost, each business gets its own elected cost. Otherwise (a limit or a carryover applies), a business with elections gets the whole summary amount. This relies on the s179.multi and s179.orphan gates to refuse cases with more than one such business or with a carryover but no electing business.

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
{"from": {"line": "31"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: A loss contributes no earned income, so the net profit is entered only if it is positive.

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
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 9, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Second transcription's note: When line 4 is zero the percentage is zero, and line 5 may also be zero, so the division is avoided.

Ruling: open

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **AGREE**

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 6, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 9, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Ruling: open

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **AGREE**

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **AGREE**

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **AGREE**

### 1(c) — Qualified business income or (loss) of this business
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract", "take": {"of": [{"line": "14 (sc.f7206_line14)"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}], "op": "sum"}}
```

Second:

```json
{"from": {"from": {"from": {"line": "31"}, "op": "subtract", "take": {"line": "7 (sc.f7206_line7)"}}, "op": "subtract", "take": {"line": "9 (sc.f7206_line9)"}}, "op": "subtract", "take": {"line": "14 (sc.f7206_line14)"}}
```

Second transcription's note: i8995 says QBI considers all items attributable to the business, including the deductible part of SE tax, the self-employed health insurance deduction and contributions to qualified retirement plans. The SE tax and plan deductions are attributed by the Form 7206 line 6 share (lines 7 and 9). The health insurance deduction is this business's Form 7206 line 14.

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sc.line31_pre179 | sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| sc.result | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| sc.profit_pos | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 3 (sc.line3) | sc.method_other, sc.spouse_owned, sc.statutory | sc.method_other, sc.spouse_owned, sc.statutory |
| 4 (sc.line4) | sc.inventory_other | - |
| 5 (sc.line5) | sc.inventory_other, sc.method_other, sc.spouse_owned, sc.statutory | sc.method_other, sc.spouse_owned, sc.statutory |
| 7 (sc.line7) | sc.inventory_other, sc.method_other, sc.spouse_owned, sc.statutory | sc.method_other, sc.spouse_owned, sc.statutory |
| 12 (sc.line12) | sc.special | sc.special |
| 27a | sc.special | sc.special |
| 28 | sc.special | sc.special |
| 29 | sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 1 (sc.ho_line1) | sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 5 (sc.ho_line5) | sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 30 | sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 31 | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 42 | sc.inventory_other | - |
| 4 (sc.f7206_line4) | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 7 (sc.f7206_line7) | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 8 (sc.f7206_line8) | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 9 (sc.f7206_line9) | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 10 (sc.f7206_line10) | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 13 (sc.f7206_line13) | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 14 (sc.f7206_line14) | sc.h_atrisk_limited, sc.h_hi_refuse, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_hi_refuse, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 1(c) | sc.h_atrisk_limited, sc.h_hi_refuse, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_atrisk_limited, sc.h_hi_refuse, sc.h_ho_refuse, sc.h_ho_sqft_bad, sc.h_passive_no, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sc.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: sc.line3
    printed: "3 (sc.line3)"
    label: "Subtract line 2 from line 1"
    type: Dollars
    expr: {op: subtract, from: sc.line1, take: sc.line2}
    refuses: [sc.method_other, sc.spouse_owned, sc.statutory]
    note: "The tool computes Schedule C only for a cash or accrual method with no change of method or section 263A capitalization, for a business not owned with a spouse, and for income that is not statutory-employee or notary income. Statutory-employee income is excluded from Schedule SE and is outside scope.schedule1, so it is refused here rather than routed separately."

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
    expr: {op: param, ref: ss.zero}
    refuses: [sc.special]
    note: "Depletion is screened by sc.special. The computed case has no depletion; filers with depletion are refused."

  - id: sc.h_dep_other
    printed: "(helper)"
    label: "Form 4562 depreciation other than the section 179 expense deduction (lines 14 through 17, 19 and 21)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f14, sc.f17, sc.f19_y3, sc.f19_y5, sc.f19_y7, sc.f19_y10, sc.f19_y15, sc.f19_y20, sc.f19_y15sl, sc.f28]}
    note: "Form 4562 line 22 adds line 12, lines 14 through 17, line 19 and line 20 column (g), and line 21 (line 21 = line 28). Lines 15, 16 and 20 (section 168(f)(1), ACRS and ADS property) are outside the screened scope and contribute nothing."

  - id: sc.line13
    printed: "13 (sc.line13)"
    label: "Depreciation and section 179 expense deduction (not included in Part III)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_dep_other, sc.s179_allowed]}
    note: "This is Form 4562 line 22 for this business, composed directly from its parts. The section 179 part (line 12) is kept separate so that the section 179 business income limit can be figured without it (see sc.line31_pre179)."

  - id: sc.h_veh_lease
    printed: "(helper)"
    label: "Vehicle lease payments (business portion)"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.line20a}

  - id: sc.line20a
    printed: "20a"
    label: "Rent or lease: vehicles, machinery, and equipment"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_veh_lease, sc.rent_equipment]}

  - id: sc.h_meals50
    printed: "(helper)"
    label: "Business meals deductible at 50%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_50, rate: {param: sc.meals_rate}}

  - id: sc.h_meals80
    printed: "(helper)"
    label: "Business meals deductible at 80% (DOT hours of service)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_80, rate: {param: sc.meals_rate_dot}}

  - id: sc.line24b
    printed: "24b"
    label: "Deductible meals"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_meals50, sc.h_meals80, sc.meals_100]}

  - id: sc.line27a
    printed: "27a"
    label: "Energy efficient commercial bldgs deduction (attach Form 7205)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sc.special]
    note: "Form 7205 is screened by sc.special. The computed case has no deduction."

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
    label: "Simplified method amount: maximum allowable amount ($5)"
    type: NonNegDollars
    expr: {op: param, ref: sc.ho_rate}
    note: "Line 3b is 1.0 because daycare use is screened by sc.ho_other, so line 3c equals line 3a."

  - id: sc.h_ho_max
    printed: "(helper)"
    label: "Maximum square footage (300)"
    type: Count
    expr: {op: param, ref: sc.ho_max_sqft}

  - id: sc.h_ho_actual
    printed: "(helper)"
    label: "Square feet used for business times line 3c"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sc.ho_rate, count: sc.ho_sqft}

  - id: sc.h_ho_cap
    printed: "(helper)"
    label: "300 square feet times line 3c"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sc.ho_rate, count: sc.h_ho_max}

  - id: sc.ho_line4
    printed: "4 (sc.ho_line4)"
    label: "Multiply line 2 by line 3c"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.h_ho_actual, sc.h_ho_cap]}
    note: "Line 2 is the smaller of the square feet used or 300 (full-year use only; part-year use is screened by sc.ho_other). Because $5 x min(a, 300) = min($5 x a, $5 x 300), this line takes the smaller of the two products."

  - id: sc.ho_line1
    printed: "1 (sc.ho_line1)"
    label: "Gross income limitation"
    type: Dollars
    expr: {op: copy, from: sc.line29}
    note: "Line E = line A (Schedule C line 29) + line B - line D. Gains and losses on Form 8949 or Form 4797 related to the business, and income from another place of business, are screened by sc.ho_other, so lines B and D are zero."

  - id: sc.h_ho_min
    printed: "(helper)"
    label: "Smaller of line 1 or line 4"
    type: Dollars
    expr: {op: smaller_of, of: [sc.ho_line1, sc.ho_line4]}

  - id: sc.ho_line5
    printed: "5 (sc.ho_line5)"
    label: "Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.h_ho_min, take: {const: 0}}

  - id: sc.h_ho_refuse
    printed: "(helper)"
    label: "Business use of home outside the simplified method as supported"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sc.ho_uses, {const: true}]}
        - {op: test, eq: [sc.ho_other, {const: true}]}

  - id: sc.h_ho_sqft_bad
    printed: "(helper)"
    label: "Business square footage is more than the home's total square footage"
    type: Bool
    expr: {op: test, gt: [sc.ho_sqft, sc.ho_home_sqft]}

  - id: sc.line30
    printed: "30"
    label: "Expenses for business use of your home"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sc.ho_uses, {const: true}]}
          then: sc.ho_line5
        - guard: {op: test, eq: [sc.ho_uses, {const: false}]}
          then: sc.h_zero
    refuses: [sc.h_ho_refuse, {when: sc.h_ho_sqft_bad, when_known: true}]

  - id: sc.h_passive_no
    printed: "(helper)"
    label: "Line G answered No (passive activity)"
    type: Bool
    expr: {op: test, eq: [sc.passive, {const: false}]}

  - id: sc.h_atrisk_limited
    printed: "(helper)"
    label: "Loss with some investment not at risk (box 32b)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, lt: [sc.line29, sc.line30]}
        - {op: test, eq: [sc.at_risk, {const: false}]}

  - id: sc.line31
    printed: "31"
    label: "Net profit or (loss). Subtract line 30 from line 29"
    type: Dollars
    expr: {op: subtract, from: sc.line29, take: sc.line30}
    refuses: [sc.h_passive_no, sc.h_atrisk_limited]
    note: "A passive activity (line G No) needs Form 8582, even for a profit. A loss with an investment that is not at risk (box 32b) needs Form 6198. Both are refused."

  - id: sc.line40
    printed: "40"
    label: "Add lines 35 through 39"
    type: NonNegDollars
    expr: {op: sum, of: [sc.line35, sc.line36, sc.line37, sc.line38, sc.line39]}

  - id: sc.line42
    printed: "42"
    label: "Cost of goods sold. Subtract line 41 from line 40"
    type: Dollars
    expr: {op: subtract, from: sc.line40, take: sc.line41}
    refuses: [sc.inventory_other]

  - id: sc.h_elected
    printed: "(helper)"
    label: "Total elected cost of section 179 property for this business (Form 4562 lines 6(c) and 7)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f6, sc.f29]}

  - id: sc.h_s179_own
    printed: "(helper)"
    label: "Elected section 179 cost of this business, not more than the allowed deduction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.h_elected, s179.line12]}

  - id: sc.s179_allowed
    printed: "12 (sc.s179_allowed)"
    label: "Section 179 expense deduction allocated to this business from the Summary Form 4562"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, gt: [sc.h_elected, {const: 0}]}
              - {op: test, ne: [s179.line12, s179.line8]}
          then: s179.line12
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, gt: [sc.h_elected, {const: 0}]}
                - {op: test, ne: [s179.line12, s179.line8]}
          then: sc.h_s179_own
    note: "The i4562 line 12 instructions let you allocate the taxpayer-level deduction among businesses 'in any manner' without fixing a rule. The reading chosen: when the summary line 12 equals the total elected cost, each business gets its own elected cost. Otherwise (a limit or a carryover applies), a business with elections gets the whole summary amount. This relies on the s179.multi and s179.orphan gates to refuse cases with more than one such business or with a carryover but no electing business."

  - id: sc.f7206_line2
    printed: "2 (sc.f7206_line2)"
    label: "Qualified long-term care insurance: total for each person of the smaller of payments or the age limit"
    type: NonNegDollars
    expr: {op: sum_over, collection: ltc, field: ltc.amount}

  - id: sc.f7206_line3
    printed: "3 (sc.f7206_line3)"
    label: "Add lines 1 and 2"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f7206_line1, sc.f7206_line2]}

  - id: sc.f7206_line4
    printed: "4 (sc.f7206_line4)"
    label: "Net profit and any other earned income from the trade or business under which the insurance plan is established"
    type: NonNegDollars
    expr: {op: copy, from: sc.profit_pos}
    note: "A loss contributes no earned income, so the net profit is entered only if it is positive."

  - id: sc.f7206_line5
    printed: "5 (sc.f7206_line5)"
    label: "Total of all net profits from Schedule C, line 31 (don't include any net losses)"
    type: NonNegDollars
    expr: {op: copy, from: person.positive_profits}
    note: "Read as the total positive Schedule C profits of the person who owns this business. Schedule F, Schedule K-1 and optional methods are screened."

  - id: sc.h_7206_l7_prorated
    printed: "(helper)"
    label: "Deductible part of self-employment tax times line 4 divided by line 5"
    type: NonNegDollars
    expr: {op: prorate, amount: person.se_line13, part: sc.f7206_line4, whole: sc.f7206_line5, places: 9}
    note: "Line 6 (line 4 divided by line 5) states no rounding, so the most precise available, 9 decimal places, is used. The form says Schedule 1 line 15. That is the per-person Schedule SE line 13 summed over spouses, so the owner's own Schedule SE line 13 is used, consistent with line 5 being the owner's profits."

  - id: sc.f7206_line7
    printed: "7 (sc.f7206_line7)"
    label: "Multiply Schedule 1, line 15, deductible part of self-employment tax, by the percentage on line 6"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sc.f7206_line4, {const: 0}]}
          then: sc.h_7206_l7_prorated
        - guard: {op: test, le: [sc.f7206_line4, {const: 0}]}
          then: sc.h_zero
    note: "When line 4 is zero the percentage is zero, and line 5 may also be zero, so the division is avoided."

  - id: sc.f7206_line8
    printed: "8 (sc.f7206_line8)"
    label: "Subtract line 7 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line4, take: sc.f7206_line7}
    note: "The form gives no floor. Line 7 cannot exceed line 4 in the supported cases, so the floor at zero has no effect."

  - id: sc.h_7206_l9_prorated
    printed: "(helper)"
    label: "Self-employed SEP/SIMPLE deduction attributed to this business"
    type: NonNegDollars
    expr: {op: prorate, amount: person.s16, part: sc.f7206_line4, whole: sc.f7206_line5, places: 9}
    note: "The form asks for the Schedule 1 line 16 amount 'attributable to the same trade or business' without saying how to attribute a person's plan deduction among several businesses. The reading chosen is the line 6 percentage (this business's share of positive profits)."

  - id: sc.f7206_line9
    printed: "9 (sc.f7206_line9)"
    label: "Self-employed SEP, SIMPLE, and qualified plans attributable to the same trade or business"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sc.f7206_line4, {const: 0}]}
          then: sc.h_7206_l9_prorated
        - guard: {op: test, le: [sc.f7206_line4, {const: 0}]}
          then: sc.h_zero

  - id: sc.f7206_line10
    printed: "10 (sc.f7206_line10)"
    label: "Subtract line 9 from line 8"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line8, take: sc.f7206_line9}

  - id: sc.f7206_line13
    printed: "13 (sc.f7206_line13)"
    label: "Subtract line 12 from line 10 or 11, whichever applies"
    type: NonNegDollars
    expr: {op: copy, from: sc.f7206_line10}
    note: "Line 11 (S corporation wages) and line 12 (Form 2555) are screened by sc.hi_screen, so this line is line 10."

  - id: sc.h_7206_min
    printed: "(helper)"
    label: "Smaller of line 3 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.f7206_line3, sc.f7206_line13]}

  - id: sc.h_hi_refuse
    printed: "(helper)"
    label: "Self-employed health insurance outside the supported cases"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sc.hi_uses, {const: true}]}
        - {op: test, eq: [sc.hi_screen, {const: true}]}

  - id: sc.f7206_line14
    printed: "14 (sc.f7206_line14)"
    label: "Self-employed health insurance deduction. Enter the smaller of line 3 or line 13"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sc.hi_uses, {const: true}]}
          then: sc.h_7206_min
        - guard: {op: test, eq: [sc.hi_uses, {const: false}]}
          then: sc.h_zero
    refuses: [sc.h_hi_refuse]

  - id: sc.h_qbi_a
    printed: "(helper)"
    label: "Net profit less the deductible part of self-employment tax attributable to the business"
    type: Dollars
    expr: {op: subtract, from: sc.line31, take: sc.f7206_line7}

  - id: sc.h_qbi_b
    printed: "(helper)"
    label: "Less self-employed retirement plan contributions attributable to the business"
    type: Dollars
    expr: {op: subtract, from: sc.h_qbi_a, take: sc.f7206_line9}

  - id: sc.qbi
    printed: "1(c)"
    label: "Qualified business income or (loss)"
    type: Dollars
    expr: {op: subtract, from: sc.h_qbi_b, take: sc.f7206_line14}
    note: "i8995 says QBI considers all items attributable to the business, including the deductible part of SE tax, the self-employed health insurance deduction and contributions to qualified retirement plans. The SE tax and plan deductions are attributed by the Form 7206 line 6 share (lines 7 and 9). The health insurance deduction is this business's Form 7206 line 14."

  - id: sc.one
    printed: "(helper)"
    label: "One (counts this Schedule C)"
    type: Count
    expr: {op: param, ref: sc.one}

  - id: sc.rrta
    printed: "(helper)"
    label: "This Schedule C's net profit is reported on Schedule SE, line 2"
    type: Bool
    expr: {op: test, eq: [sc.statutory, {const: false}]}
    note: "The IRS pages do not define a per-business RRTA fact. Schedule SE line 8a combines railroad retirement compensation with wages only when there is self-employment income, so this flag is read as 'this business contributes to Schedule SE' (not statutory-employee income). This is an interpretation, not a determination from the text."

  - id: sc.h_exp_pre179
    printed: "(helper)"
    label: "Total expenses (line 28) figured without the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: sum, of: [sc.line8, sc.line9, sc.line10, sc.line11, sc.line12, sc.h_dep_other, sc.line14, sc.line15, sc.line16a, sc.line16b, sc.line17, sc.line18, sc.line19, sc.line20a, sc.line20b, sc.line21, sc.line22, sc.line23, sc.line24a, sc.line24b, sc.line25, sc.line26, sc.line27a, sc.line27b]}

  - id: sc.h_line29_pre179
    printed: "(helper)"
    label: "Tentative profit figured without the section 179 expense deduction"
    type: Dollars
    expr: {op: subtract, from: sc.line7, take: sc.h_exp_pre179}

  - id: sc.h_ho_min_pre179
    printed: "(helper)"
    label: "Simplified-method home office amount limited by pre-section-179 income"
    type: Dollars
    expr: {op: smaller_of, of: [sc.h_line29_pre179, sc.ho_line4]}

  - id: sc.h_ho5_pre179
    printed: "(helper)"
    label: "If zero or less, zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.h_ho_min_pre179, take: {const: 0}}

  - id: sc.h_line30_pre179
    printed: "(helper)"
    label: "Business use of home figured without the section 179 expense deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sc.ho_uses, {const: true}]}
          then: sc.h_ho5_pre179
        - guard: {op: test, eq: [sc.ho_uses, {const: false}]}
          then: sc.h_zero

  - id: sc.line31_pre179
    printed: "(helper)"
    label: "Net profit or (loss) of this business figured without regard to the section 179 expense deduction"
    type: Dollars
    expr: {op: subtract, from: sc.h_line29_pre179, take: sc.h_line30_pre179}
    note: "Pub. 946 and i4562 line 11 say business taxable income is figured without regard to the section 179 deduction (and without the half SE tax deduction). The home office gross income limit is also refigured on this pre-179 income. That is a reading, chosen so the computation is not circular."

  - id: sc.result
    printed: "(helper)"
    label: "Net profit or (loss) entered on Schedule 1, line 3, and Schedule SE, line 2"
    type: Dollars
    expr: {op: copy, from: sc.line31}

  - id: sc.profit_pos
    printed: "(helper)"
    label: "Net profit from line 31 (not a net loss)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.line31, take: {const: 0}}

  - id: sc.f6
    printed: "(helper)"
    label: "Form 4562 line 6, column (c): elected section 179 cost of property other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.s179_2025
      where: {op: test, eq: [asset.listed, {const: false}]}

  - id: sc.f14
    printed: "(helper)"
    label: "Form 4562 line 14: special depreciation allowance (other than listed property)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.bonus
      where: {op: test, eq: [asset.listed, {const: false}]}

  - id: sc.f17
    printed: "(helper)"
    label: "Form 4562 line 17: MACRS deductions for assets placed in service before 2025"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs_prior
      where: {op: test, eq: [asset.listed, {const: false}]}

  - id: sc.f19_y3
    printed: "(helper)"
    label: "Form 4562 line 19a, column (g): 3-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y3"}]}

  - id: sc.f19_y5
    printed: "(helper)"
    label: "Form 4562 line 19b, column (g): 5-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y5"}]}

  - id: sc.f19_y7
    printed: "(helper)"
    label: "Form 4562 line 19c, column (g): 7-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y7"}]}

  - id: sc.f19_y10
    printed: "(helper)"
    label: "Form 4562 line 19d, column (g): 10-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y10"}]}

  - id: sc.f19_y15
    printed: "(helper)"
    label: "Form 4562 line 19e, column (g): 15-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y15"}]}

  - id: sc.f19_y20
    printed: "(helper)"
    label: "Form 4562 line 19f, column (g): 20-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y20"}]}

  - id: sc.f19_y15sl
    printed: "(helper)"
    label: "Form 4562 line 19, column (g): 15-year straight line property (qualified improvement property)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y15sl"}]}

  - id: sc.h_f25_asset
    printed: "(helper)"
    label: "Special depreciation allowance for qualified listed property other than vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.f25}

  - id: sc.h_f25_veh
    printed: "(helper)"
    label: "Special depreciation allowance for vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.bonus_allowed}

  - id: sc.f25
    printed: "(helper)"
    label: "Form 4562 line 25: special depreciation allowance for qualified listed property"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f25_asset, sc.h_f25_veh]}

  - id: sc.h_f26h_asset
    printed: "(helper)"
    label: "Depreciation deduction, column (h), listed property other than vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.dep_listed}

  - id: sc.h_f26h_veh
    printed: "(helper)"
    label: "Depreciation deduction, column (h), vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.macrs}
    note: "Reads the vehicle's regular MACRS depreciation (excluding the special allowance on line 25 and section 179 in column (i)) as its column (h) amount."

  - id: sc.f26h
    printed: "(helper)"
    label: "Form 4562 lines 26 and 27, column (h): depreciation deduction for listed property"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f26h_asset, sc.h_f26h_veh]}

  - id: sc.f28
    printed: "(helper)"
    label: "Form 4562 line 28: add amounts in column (h), lines 25 through 27"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f25, sc.f26h]}

  - id: sc.h_f29_asset
    printed: "(helper)"
    label: "Elected section 179 cost, column (i), listed property other than vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.f26i}

  - id: sc.h_f29_veh
    printed: "(helper)"
    label: "Elected section 179 cost, column (i), vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.s179_2025}

  - id: sc.f29
    printed: "(helper)"
    label: "Form 4562 line 29: add amounts in column (i), line 26"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f29_asset, sc.h_f29_veh]}

  - id: sc.h_mq_q4_asset
    printed: "(helper)"
    label: "Depreciable bases placed in service in the last 3 months (assets)"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_q4}

  - id: sc.h_mq_q4_veh
    printed: "(helper)"
    label: "Depreciable bases placed in service in the last 3 months (vehicles)"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.mq_q4}

  - id: sc.mq_q4
    printed: "(helper)"
    label: "Total depreciable bases of MACRS property placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_mq_q4_asset, sc.h_mq_q4_veh]}

  - id: sc.h_mq_total_asset
    printed: "(helper)"
    label: "Depreciable bases placed in service during the year (assets)"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_total}

  - id: sc.h_mq_total_veh
    printed: "(helper)"
    label: "Depreciable bases placed in service during the year (vehicles)"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.mq_total}

  - id: sc.mq_total
    printed: "(helper)"
    label: "Total depreciable bases of all MACRS property placed in service during the year"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_mq_total_asset, sc.h_mq_total_veh]}

  - id: sc.h_cost179_asset
    printed: "(helper)"
    label: "Cost of section 179 property placed in service (assets)"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.cost179}

  - id: sc.h_cost179_veh
    printed: "(helper)"
    label: "Cost of section 179 property placed in service (vehicles)"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.cost179}

  - id: sc.cost179
    printed: "(helper)"
    label: "Total cost of section 179 property placed in service in this business (Form 4562 line 2 contribution)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_cost179_asset, sc.h_cost179_veh]}
```
```
