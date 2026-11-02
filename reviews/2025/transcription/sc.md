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
| required input context sha256 | 91ebadaa96db06f6a8d5611b353a501518e494a3193e131ab7d325bfce5a3504 |
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
{"args": [{"const": true}, {"ref": "person.rrta"}], "test": "eq"}
```

Second transcription's note: The IRS pages do not determine this interface. Schedule SE line 8a mentions railroad retirement (tier 1) compensation, and the catalog has person.sc_rrta_count and person.se_rrta. Chosen reading: this Schedule C belongs to a person who answered yes to person.rrta, read from the enclosing person's entry.

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.line31_pre179 — Line 31 without the section 179 expense deduction
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"line": "30"}}
```

Second:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}], "op": "sum"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs_prior", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "ne"}], "test": "all"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"from": {"of": [{"line": "4 (sc.ho_line4)"}, {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}], "op": "sum"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.macrs_prior", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "ne"}], "test": "all"}}], "op": "sum"}], "op": "sum"}}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}}
```

Second transcription's note: Form 4562 line 11 computes business income without regard to section 179. The home-use gross income limitation depends on line 29, which includes section 179, and the IRS text does not resolve that interdependence. Chosen reading: refigure the home-use limitation with line 29 before section 179.

Ruling: representation; the only differences are the project's cited refusals (sc.ho_both_limits, sc.ho_multi and the others on sc.result) on refused returns; no completed return differs. Triage executable-triage-v2 (triage/sc.json): 3824 of 3842 comparisons agree; on completed returns no difference.

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

Ruling: representation; the only differences are the project's cited refusals (sc.ho_both_limits, sc.ho_multi and the others on sc.result) on refused returns; no completed return differs. Triage executable-triage-v2 (triage/sc.json): 3830 of 3842 comparisons agree; on completed returns no difference.

### sc.f6 — Section 179 elected on property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f14 — Special allowance on property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "asset", "field": "asset.bonus", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f17 — MACRS on earlier property other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs_prior", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "ne"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **DISAGREE**

Project:

```json
{"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "asset", "field": "asset.macrs2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f25 — Line 25 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f26h — Column (h), line 26, for this business
Status: **AGREE**

### sc.f28 — Line 28 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}
```

Second:

```json
{"of": [{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.f25", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}
```

Second transcription's note: Line 27 (business use of 50% or less) is not added because the catalog's listed-property and vehicle gates (asset.listed_low, scveh.low_use) appear to refuse it. The supplied text does not state how those gates are computed.

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

### sc.f29 — Line 29 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"collection": "asset", "field": "asset.f26i", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: representation; triage found no difference: the line sums the same entries through helpers the comparison does not see through. Triage executable-triage-v2 (triage/sc.json): 3842 of 3842 comparisons agree; on completed returns no difference.

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

Ruling: representation; the only differences are the project's cited refusals (sc.ho_both_limits, sc.ho_multi and the others on sc.result) on refused returns; no completed return differs. Triage executable-triage-v2 (triage/sc.json): 3830 of 3842 comparisons agree; on completed returns no difference.

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

Ruling: representation; the only differences are the project's cited refusals (sc.ho_both_limits, sc.ho_multi and the others on sc.result) on refused returns; no completed return differs. Triage executable-triage-v2 (triage/sc.json): 3830 of 3842 comparisons agree; on completed returns no difference.

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

Second transcription's note: Worksheet line 2 is the smaller of the square feet used or 300. The model has no minimum over counts, so each count is multiplied by the rate and the smaller money amount is taken. Line 3b is 1.0 because daycare is screened by sc.ho_other, so line 3c equals line 3a.

Ruling: representation; $5 times the smaller of the square footage and 300 (i1040sc Simplified Method Worksheet) on both sides. representation; the only differences are the project's cited refusals (sc.ho_both_limits, sc.ho_multi and the others on sc.result) on refused returns; no completed return differs. Triage executable-triage-v2 (triage/sc.json): 3792 of 3842 comparisons agree; on completed returns no difference.

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

Ruling: representation; the smaller of worksheet lines 1 and 4 on both sides. The project refuses where the two income limits of p946 p. 19 interact (sc.ho_both_limits). The three completed-return witnesses have sc.ho_uses false, so the line is not read on those returns; the candidate's need for sc.ho_other there is unreachable for the same reason. Triage executable-triage-v2 (triage/sc.json): 2832 of 3842 comparisons agree; on completed returns {"candidate-unknown": 5, "project-refuses": 3}.

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
{"alternatives": [{"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "eq"}, "then": {"ref": "s179.line12"}}, {"guard": {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "ne"}, "then": {"of": [{"of": [{"collection": "asset", "field": "asset.f26i", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.s179_2025", "op": "sum_over", "where": null}], "op": "sum"}, {"collection": "asset", "field": "asset.s179_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y2025"}, {"ref": "asset.placed"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}], "op": "sum"}}], "op": "choose"}
```

Second transcription's note: Form 4562 instructions, line 12, let a taxpayer with several businesses allocate the deduction among them but fix no rule. Chosen reading: a single business takes the whole s179.line12. With several businesses, each takes its own elected cost. This assumes s179.multi refuses cases where the allowed total differs from the total elected; its computation is not supplied.

Ruling: ambiguity (amb.2025.s179_carryover_no_property, owner ruling T-043). representation; the only differences are the project's cited refusals (sc.ho_both_limits, sc.ho_multi and the others on sc.result) on refused returns; no completed return differs. Triage executable-triage-v2 (triage/sc.json): 3830 of 3842 comparisons agree; on completed returns no difference.

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

Ruling: scope; f7206 line 4, "any other earned income" (footnote: "gains from the sale, transfer, or licensing of property you created", not capital gain). The only such income the tool admits is on Schedule C; Form 4797 and outside income are refused. representation; the only differences are the project's cited refusals (sc.ho_both_limits, sc.ho_multi and the others on sc.result) on refused returns; no completed return differs. Triage executable-triage-v2 (triage/sc.json): 3830 of 3842 comparisons agree; on completed returns no difference.

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
{"alternatives": [{"guard": {"args": [{"line": "5 (sc.f7206_line5)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "5 (sc.f7206_line5)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 9, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Ruling: ambiguity (amb.2025.f7206_ratio_places); the project rounds the ratio to six places and the candidate to four; the one-cent value differences are on refused returns. Triage executable-triage-v2 (triage/sc.json): 3790 of 3842 comparisons agree; on completed returns no difference.

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
{"alternatives": [{"guard": {"args": [{"line": "5 (sc.f7206_line5)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "5 (sc.f7206_line5)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 9, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Ruling: ambiguity (amb.2025.f7206_plan_attribution, amb.2025.f7206_ratio_places). The candidate's refusals are person.plan_screened on returns the project also refuses or never reaches. Triage executable-triage-v2 (triage/sc.json): 3821 of 3842 comparisons agree; on completed returns no difference.

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
{"from": {"line": "31"}, "op": "subtract", "take": {"of": [{"line": "14 (sc.f7206_line14)"}, {"line": "7 (sc.f7206_line7)"}, {"line": "9 (sc.f7206_line9)"}], "op": "sum"}}
```

Second transcription's note: Form 8995 instructions require QBI to consider the deductible part of self-employment tax, the self-employed health insurance deduction and qualified retirement plan contributions, but give no allocation among businesses. Chosen reading: use the Form 7206 lines 7, 9 and 14 amounts for this business.

Ruling: ambiguity (amb.2025.qbi_attribution, amb.2025.f7206_ratio_places); i8995 p. 2. ambiguity (amb.2025.f7206_ratio_places); the project rounds the ratio to six places and the candidate to four; the one-cent value differences are on refused returns. Triage executable-triage-v2 (triage/sc.json): 3791 of 3842 comparisons agree; on completed returns no difference.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sc.line31_pre179 | sc.h_ho_area_bad, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| sc.result | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| sc.profit_pos | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 3 (sc.line3) | sc.h_not_material, sc.method_other, sc.spouse_owned, sc.statutory | sc.h_not_material, sc.method_other, sc.spouse_owned, sc.statutory |
| 4 (sc.line4) | sc.inventory_other | - |
| 5 (sc.line5) | sc.h_not_material, sc.inventory_other, sc.method_other, sc.spouse_owned, sc.statutory | sc.h_not_material, sc.method_other, sc.spouse_owned, sc.statutory |
| 7 (sc.line7) | sc.h_not_material, sc.inventory_other, sc.method_other, sc.spouse_owned, sc.statutory | sc.h_not_material, sc.method_other, sc.spouse_owned, sc.statutory |
| 12 (sc.line12) | sc.special | sc.special |
| 27a | sc.special | sc.special |
| 28 | sc.special | sc.special |
| 29 | sc.h_not_material, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_not_material, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 4 (sc.ho_line4) | sc.h_ho_area_bad | sc.h_ho_area_bad |
| 1 (sc.ho_line1) | sc.h_not_material, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_not_material, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 5 (sc.ho_line5) | sc.h_ho_area_bad, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 30 | sc.h_ho_area_bad, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 31 | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 42 | sc.inventory_other | - |
| 12 (sc.s179_allowed) | s179.multi | - |
| 4 (sc.f7206_line4) | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 7 (sc.f7206_line7) | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 8 (sc.f7206_line8) | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 9 (sc.f7206_line9) | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 10 (sc.f7206_line10) | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 13 (sc.f7206_line13) | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 14 (sc.f7206_line14) | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.hi_screen, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.hi_screen, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| 1(c) | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.hi_screen, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_area_bad, sc.h_loss_not_at_risk, sc.h_not_material, sc.hi_screen, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sc.h_not_material
    printed: "(helper)"
    label: "Line G answered No: you did not materially participate (and the oil and gas exception does not apply), or this is a rental activity"
    type: Bool
    expr: {op: test, eq: [sc.passive, {const: false}]}
  - id: sc.line3
    printed: "3 (sc.line3)"
    label: "Subtract line 2 from line 1"
    type: Dollars
    expr: {op: subtract, from: sc.line1, take: sc.line2}
    refuses: [sc.statutory, sc.spouse_owned, sc.method_other, sc.h_not_material]
    note: "Lines 3 to 7 feed every income result, so the business-level screens are listed here. sc.tips_ot is not listed: Schedule C arithmetic does not change for tips or overtime, and the deduction belongs to Schedule 1-A. The sc.one interface and the catalog's s1.sc_1a gate appear to handle it at return level, but the supplied text does not confirm this."
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
  - id: sc.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: sc.line12
    printed: "12 (sc.line12)"
    label: "Depletion"
    type: NonNegDollars
    expr: {op: copy, from: sc.h_zero}
    refuses: [sc.special]
  - id: sc.line13
    printed: "13 (sc.line13)"
    label: "Depreciation and section 179 expense deduction (not included in Part III)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f4562, field: f4562.line22}
  - id: sc.h_veh20a
    printed: "(helper)"
    label: "Business portion of vehicle lease payments"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.line20a}
  - id: sc.line20a
    printed: "20a"
    label: "Rent or lease: Vehicles, machinery, and equipment"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_veh20a, sc.rent_equipment]}
  - id: sc.h_meals50_amt
    printed: "(helper)"
    label: "Business meals subject to the 50% limit, at 50%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_50, rate: {param: sc.meals_rate}}
  - id: sc.h_meals80_amt
    printed: "(helper)"
    label: "Meals subject to the Department of Transportation hours of service limits, at 80%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_80, rate: {param: sc.meals_rate_dot}}
  - id: sc.line24b
    printed: "24b"
    label: "Deductible meals"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_meals50_amt, sc.h_meals80_amt, sc.meals_100]}
  - id: sc.line27a
    printed: "27a"
    label: "Energy efficient commercial bldgs deduction (attach Form 7205)"
    type: NonNegDollars
    expr: {op: copy, from: sc.h_zero}
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
    expr:
      op: sum
      of: [sc.line8, sc.line9, sc.line10, sc.line11, sc.line12, sc.line13, sc.line14, sc.line15, sc.line16a, sc.line16b, sc.line17, sc.line18, sc.line19, sc.line20a, sc.line20b, sc.line21, sc.line22, sc.line23, sc.line24a, sc.line24b, sc.line25, sc.line26, sc.line27a, sc.line27b]
  - id: sc.line29
    printed: "29"
    label: "Tentative profit or (loss). Subtract line 28 from line 7"
    type: Dollars
    expr: {op: subtract, from: sc.line7, take: sc.line28}
  - id: sc.ho_rate
    printed: "3a"
    label: "Simplified Method Worksheet: Maximum allowable amount"
    type: NonNegDollars
    expr: {op: param, ref: sc.ho_rate}
  - id: sc.h_ho_max
    printed: "(helper)"
    label: "Maximum allowable square footage for the simplified method"
    type: Count
    expr: {op: param, ref: sc.ho_max_sqft}
  - id: sc.h_ho_actual
    printed: "(helper)"
    label: "Rate per square foot times the square feet used"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sc.ho_rate, count: sc.ho_sqft}
  - id: sc.h_ho_cap
    printed: "(helper)"
    label: "Rate per square foot times 300 square feet"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sc.ho_rate, count: sc.h_ho_max}
  - id: sc.h_ho_area_bad
    printed: "(gate)"
    label: "The area used for business is larger than the total square footage of the home"
    type: Bool
    expr: {op: test, gt: [sc.ho_sqft, sc.ho_home_sqft]}
  - id: sc.ho_line4
    printed: "4 (sc.ho_line4)"
    label: "Simplified Method Worksheet: Multiply line 2 by line 3c"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.h_ho_actual, sc.h_ho_cap]}
    refuses:
      - {when: sc.h_ho_area_bad, when_known: true}
    note: "Worksheet line 2 is the smaller of the square feet used or 300. The model has no minimum over counts, so each count is multiplied by the rate and the smaller money amount is taken. Line 3b is 1.0 because daycare is screened by sc.ho_other, so line 3c equals line 3a."
  - id: sc.ho_line1
    printed: "1 (sc.ho_line1)"
    label: "Simplified Method Worksheet: Enter the amount of the gross income limitation"
    type: Dollars
    expr: {op: copy, from: sc.line29}
    note: "Instruction lines B and D (Form 8949, Schedule D and Form 4797 gains and losses) and income from another place of business are screened by sc.ho_other, so the limitation equals Schedule C line 29."
  - id: sc.h_ho_smaller
    printed: "(helper)"
    label: "The smaller of line 1 or line 4 of the Simplified Method Worksheet"
    type: Dollars
    expr: {op: smaller_of, of: [sc.ho_line1, sc.ho_line4]}
  - id: sc.ho_line5
    printed: "5 (sc.ho_line5)"
    label: "Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4 here and include that amount on Schedule C, line 30. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.h_ho_smaller, take: {const: 0}}
    refuses: [sc.ho_other]
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
  - id: sc.h_loss_not_at_risk
    printed: "(gate)"
    label: "There is a loss and some investment is not at risk (box 32b; Form 6198 is required)"
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
    refuses: [sc.h_loss_not_at_risk]
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
    refuses: [sc.inventory_other]
  - id: sc.f6
    printed: "(helper)"
    label: "Form 4562, line 6, column (c): elected cost of section 179 property other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.s179_2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
  - id: sc.f14
    printed: "(helper)"
    label: "Form 4562, line 14: special depreciation allowance for qualified property (other than listed property) placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.bonus
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
  - id: sc.f17
    printed: "(helper)"
    label: "Form 4562, line 17: MACRS deductions for assets placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs_prior
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: false}]}
          - {op: test, eq: [asset.listed, {const: false}]}
  - id: sc.f19_y3
    printed: "(helper)"
    label: "Form 4562, line 19a, column (g): 3-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y3"}]}
  - id: sc.f19_y5
    printed: "(helper)"
    label: "Form 4562, line 19b, column (g): 5-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y5"}]}
  - id: sc.f19_y7
    printed: "(helper)"
    label: "Form 4562, line 19c, column (g): 7-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y7"}]}
  - id: sc.f19_y10
    printed: "(helper)"
    label: "Form 4562, line 19d, column (g): 10-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y10"}]}
  - id: sc.f19_y15
    printed: "(helper)"
    label: "Form 4562, line 19e, column (g): 15-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y15"}]}
  - id: sc.f19_y20
    printed: "(helper)"
    label: "Form 4562, line 19f, column (g): 20-year property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y20"}]}
  - id: sc.f19_y15sl
    printed: "(helper)"
    label: "Form 4562, line 19e, column (g): 15-year straight line property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.macrs2025
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: false}]}
          - {op: test, eq: [asset.period, {const: "y15sl"}]}
  - id: sc.h_f25_asset
    printed: "(helper)"
    label: "Special depreciation allowance for listed property other than vehicles"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.f25
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: true}]}
  - id: sc.h_f25_veh
    printed: "(helper)"
    label: "Special depreciation allowance for vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.bonus}
  - id: sc.f25
    printed: "(helper)"
    label: "Form 4562, line 25: special depreciation allowance for qualified listed property"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f25_asset, sc.h_f25_veh]}
  - id: sc.h_f26h_asset
    printed: "(helper)"
    label: "Depreciation deduction for listed property other than vehicles"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_listed
      where: {op: test, eq: [asset.listed, {const: true}]}
  - id: sc.h_f26h_veh
    printed: "(helper)"
    label: "Depreciation deduction for vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.macrs}
  - id: sc.f26h
    printed: "(helper)"
    label: "Form 4562, line 26, column (h): depreciation deduction for property used more than 50% in a qualified business use"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f26h_asset, sc.h_f26h_veh]}
  - id: sc.f28
    printed: "(helper)"
    label: "Form 4562, line 28: Add amounts in column (h), lines 25 through 27"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f25, sc.f26h]}
    note: "Line 27 (business use of 50% or less) is not added because the catalog's listed-property and vehicle gates (asset.listed_low, scveh.low_use) appear to refuse it. The supplied text does not state how those gates are computed."
  - id: sc.h_f29_asset
    printed: "(helper)"
    label: "Elected section 179 cost of listed property other than vehicles"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.f26i
      where:
        op: test
        all:
          - {op: test, eq: [asset.is2025, {const: true}]}
          - {op: test, eq: [asset.listed, {const: true}]}
  - id: sc.h_f29_veh
    printed: "(helper)"
    label: "Elected section 179 cost of vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.s179_2025}
  - id: sc.f29
    printed: "(helper)"
    label: "Form 4562, line 29: Add amounts in column (i), line 26"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f29_asset, sc.h_f29_veh]}
  - id: sc.h_mq_q4_asset
    printed: "(helper)"
    label: "Depreciable bases of property other than vehicles placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_q4}
  - id: sc.h_mq_q4_veh
    printed: "(helper)"
    label: "Depreciable bases of vehicles placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.mq_q4}
  - id: sc.mq_q4
    printed: "(helper)"
    label: "Depreciable bases of MACRS property placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_mq_q4_asset, sc.h_mq_q4_veh]}
  - id: sc.h_mq_total_asset
    printed: "(helper)"
    label: "Depreciable bases of property other than vehicles placed in service during the year"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_total}
  - id: sc.h_mq_total_veh
    printed: "(helper)"
    label: "Depreciable bases of vehicles placed in service during the year"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.mq_total}
  - id: sc.mq_total
    printed: "(helper)"
    label: "Depreciable bases of all MACRS property placed in service during the entire year"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_mq_total_asset, sc.h_mq_total_veh]}
  - id: sc.h_cost179_asset
    printed: "(helper)"
    label: "Cost of section 179 property other than vehicles placed in service during the tax year"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.cost179}
  - id: sc.h_cost179_veh
    printed: "(helper)"
    label: "Cost of vehicles that are section 179 property placed in service during the tax year"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.cost179}
  - id: sc.cost179
    printed: "(helper)"
    label: "Total cost of section 179 property placed in service, for Form 4562, line 2"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_cost179_asset, sc.h_cost179_veh]}
  - id: sc.h_s179_elected
    printed: "(helper)"
    label: "Section 179 cost elected for this business (Form 4562, line 6, column (c), and line 29)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f6, sc.f29]}
  - id: sc.s179_allowed
    printed: "12 (sc.s179_allowed)"
    label: "Section 179 expense deduction. Add lines 9 and 10, but don't enter more than line 11"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s179.sc_count, {const: 1, type: Count}]}
          then: s179.line12
        - guard: {op: test, ne: [s179.sc_count, {const: 1, type: Count}]}
          then: sc.h_s179_elected
    refuses: [s179.multi]
    note: "Form 4562 instructions, line 12, let a taxpayer with several businesses allocate the deduction among them but fix no rule. Chosen reading: a single business takes the whole s179.line12. With several businesses, each takes its own elected cost. This assumes s179.multi refuses cases where the allowed total differs from the total elected; its computation is not supplied."
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
    label: "Enter the total of all net profits from Schedule C (Form 1040), line 31; Schedule F (Form 1040), line 34; or Schedule K-1 (Form 1065), box 14, code A, plus any other income allocable to the profitable businesses"
    type: NonNegDollars
    expr: {op: copy, from: person.positive_profits}
    note: "Read from the enclosing person's entry, on the reading that the total covers this person's own profitable businesses, because Schedule SE is figured per person. Schedule F and partnership earnings are outside the tool's scope."
  - id: sc.h_7206_line7_figured
    printed: "(helper)"
    label: "Multiply the deductible part of self-employment tax by line 4 divided by line 5"
    type: NonNegDollars
    expr: {op: prorate, amount: person.se_line13, part: sc.f7206_line4, whole: sc.f7206_line5, places: 9}
    note: "Form 7206 line 6 states no rounding for the ratio. Chosen reading: 9 places, the most the atom allows, as the closest available to no rounding. The amount is this person's Schedule SE line 13, the person's share of Schedule 1 line 15."
  - id: sc.f7206_line7
    printed: "7 (sc.f7206_line7)"
    label: "Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the percentage on line 6"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sc.f7206_line5, {const: 0}]}
          then: sc.h_7206_line7_figured
        - guard: {op: test, le: [sc.f7206_line5, {const: 0}]}
          then: sc.h_zero
  - id: sc.f7206_line8
    printed: "8 (sc.f7206_line8)"
    label: "Subtract line 7 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line4, take: sc.f7206_line7}
  - id: sc.h_7206_line9_figured
    printed: "(helper)"
    label: "This person's self-employed SEP and SIMPLE deduction, times this business's share of net profits"
    type: NonNegDollars
    expr: {op: prorate, amount: person.s16, part: sc.f7206_line4, whole: sc.f7206_line5, places: 9}
    note: "Form 7206 line 9 asks for the amount attributable to the same trade or business but gives no allocation rule. Chosen reading: share by net profit, the same ratio as line 6. With one profitable business, the whole amount is attributed to it."
  - id: sc.f7206_line9
    printed: "9 (sc.f7206_line9)"
    label: "Enter the amount, if any, from Schedule 1 (Form 1040), line 16, self-employed SEP, SIMPLE, and qualified plans, attributable to the same trade or business in which the insurance plan is established"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sc.f7206_line5, {const: 0}]}
          then: sc.h_7206_line9_figured
        - guard: {op: test, le: [sc.f7206_line5, {const: 0}]}
          then: sc.h_zero
  - id: sc.f7206_line10
    printed: "10 (sc.f7206_line10)"
    label: "Subtract line 9 from line 8"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line8, take: sc.f7206_line9}
    note: "The form prints no zero floor on lines 8 and 10, but the required type is NonNegDollars, so the subtraction floors at zero."
  - id: sc.f7206_line13
    printed: "13 (sc.f7206_line13)"
    label: "Subtract line 12 from line 10 or 11, whichever applies"
    type: NonNegDollars
    expr: {op: copy, from: sc.f7206_line10}
    note: "Line 11 (S corporation wages) and line 12 (Form 2555) are excluded by sc.hi_screen, so line 13 equals line 10."
  - id: sc.h_7206_smaller
    printed: "(helper)"
    label: "The smaller of line 3 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.f7206_line3, sc.f7206_line13]}
    refuses: [sc.hi_screen]
  - id: sc.f7206_line14
    printed: "14 (sc.f7206_line14)"
    label: "Self-employed health insurance deduction. Enter the smaller of line 3 or line 13 here and on Schedule 1 (Form 1040), line 17"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sc.hi_uses, {const: true}]}
          then: sc.h_7206_smaller
        - guard: {op: test, eq: [sc.hi_uses, {const: false}]}
          then: sc.h_zero
  - id: sc.h_qbi_deductions
    printed: "(helper)"
    label: "Deductible part of self-employment tax, contributions to qualified retirement plans and self-employed health insurance deduction attributable to this business"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f7206_line7, sc.f7206_line9, sc.f7206_line14]}
  - id: sc.qbi
    printed: "1(c)"
    label: "Qualified business income or (loss)"
    type: Dollars
    expr: {op: subtract, from: sc.line31, take: sc.h_qbi_deductions}
    note: "Form 8995 instructions require QBI to consider the deductible part of self-employment tax, the self-employed health insurance deduction and qualified retirement plan contributions, but give no allocation among businesses. Chosen reading: use the Form 7206 lines 7, 9 and 14 amounts for this business."
  - id: sc.one
    printed: "(helper)"
    label: "One, for counting Schedules C"
    type: Count
    expr: {op: param, ref: sc.one}
  - id: sc.rrta
    printed: "(helper)"
    label: "The person filing this Schedule C reports railroad retirement compensation or taxes"
    type: Bool
    expr: {op: test, eq: [person.rrta, {const: true}]}
    note: "The IRS pages do not determine this interface. Schedule SE line 8a mentions railroad retirement (tier 1) compensation, and the catalog has person.sc_rrta_count and person.se_rrta. Chosen reading: this Schedule C belongs to a person who answered yes to person.rrta, read from the enclosing person's entry."
  - id: sc.h_exp_no13
    printed: "(helper)"
    label: "Lines 8 through 27b other than line 13"
    type: NonNegDollars
    expr:
      op: sum
      of: [sc.line8, sc.line9, sc.line10, sc.line11, sc.line12, sc.line14, sc.line15, sc.line16a, sc.line16b, sc.line17, sc.line18, sc.line19, sc.line20a, sc.line20b, sc.line21, sc.line22, sc.line23, sc.line24a, sc.line24b, sc.line25, sc.line26, sc.line27a, sc.line27b]
  - id: sc.h_dep_no179
    printed: "(helper)"
    label: "Form 4562 line 22 amounts other than the section 179 expense deduction on line 12"
    type: NonNegDollars
    expr:
      op: sum
      of: [sc.f14, sc.f17, sc.f19_y3, sc.f19_y5, sc.f19_y7, sc.f19_y10, sc.f19_y15, sc.f19_y20, sc.f19_y15sl, sc.f28]
  - id: sc.h_exp_pre
    printed: "(helper)"
    label: "Total expenses before expenses for business use of home, without any section 179 expense deduction"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_exp_no13, sc.h_dep_no179]}
  - id: sc.h_line29_pre
    printed: "(helper)"
    label: "Tentative profit or (loss), without any section 179 expense deduction"
    type: Dollars
    expr: {op: subtract, from: sc.line7, take: sc.h_exp_pre}
  - id: sc.h_ho_smaller_pre
    printed: "(helper)"
    label: "The smaller of the tentative profit without section 179 or line 4 of the Simplified Method Worksheet"
    type: Dollars
    expr: {op: smaller_of, of: [sc.h_line29_pre, sc.ho_line4]}
  - id: sc.h_ho_line5_pre
    printed: "(helper)"
    label: "Simplified method amount, figured without any section 179 expense deduction. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.h_ho_smaller_pre, take: {const: 0}}
    refuses: [sc.ho_other]
  - id: sc.h_line30_pre
    printed: "(helper)"
    label: "Expenses for business use of your home, figured without any section 179 expense deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sc.ho_uses, {const: true}]}
          then: sc.h_ho_line5_pre
        - guard: {op: test, eq: [sc.ho_uses, {const: false}]}
          then: sc.h_zero
  - id: sc.line31_pre179
    printed: "(helper)"
    label: "Net profit or (loss) computed without regard to any section 179 expense deduction, for the Form 4562 line 11 business income limitation"
    type: Dollars
    expr: {op: subtract, from: sc.h_line29_pre, take: sc.h_line30_pre}
    note: "Form 4562 line 11 computes business income without regard to section 179. The home-use gross income limitation depends on line 29, which includes section 179, and the IRS text does not resolve that interdependence. Chosen reading: refigure the home-use limitation with line 29 before section 179."
  - id: sc.result
    printed: "(helper)"
    label: "Net profit or (loss) of this business, entered on Schedule 1 (Form 1040), line 3, and on Schedule SE, line 2"
    type: Dollars
    expr: {op: copy, from: sc.line31}
  - id: sc.profit_pos
    printed: "(helper)"
    label: "Net profit of this business; zero if a loss"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.line31, take: {const: 0}}
```
```
