# Transcription agreement — sc

Second transcription of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` by an isolated model (spec 6.5), compared line by line with `forms/2025/sc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 13f2cd73378cdede5138b8478776296f3340d3d91a1e6251e0eaef05ff4940ea |
| printed lines compared | 54 |
| agree / disagree / missing | 40 / 14 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
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

### sc.line31_pre179 — Line 31 without the section 179 expense deduction
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"line": "30"}}
```

Second:

```json
{"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}, {"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"param": "sc.fifty_cents"}, {"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}], "test": "lt"}}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(screen)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "(screen)"}], "test": "eq"}, "then": {"of": [{"line": "4 (sc.ho_line4)"}, {"from": {"from": {"line": "7 (sc.line7)"}, "op": "subtract", "take": {"of": [{"line": "10 (sc.line10)"}, {"line": "11"}, {"line": "12 (sc.line12)"}, {"line": "14 (sc.line14)"}, {"line": "15"}, {"line": "16a"}, {"line": "16b"}, {"line": "17"}, {"line": "18"}, {"line": "19"}, {"line": "20a"}, {"line": "20b"}, {"line": "21"}, {"line": "22"}, {"line": "23"}, {"line": "24a"}, {"line": "24b"}, {"line": "25"}, {"line": "26"}, {"line": "27a"}, {"line": "27b"}, {"line": "8 (sc.line8)"}, {"line": "9 (sc.line9)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}, {"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"param": "sc.fifty_cents"}, {"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}], "test": "lt"}}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}], "op": "choose"}}
```

Second transcription's note: Equals line 31 plus the section 179 deduction in every case not refused at line 30. Either no section 179 deduction is taken, or line 4 is not limited by line 29.

Ruling: representation; project retained. Both figure line 31 before the section 179 deduction for Pub. 946's two income limits (pp. 17–19, Steps 1 to 5); the project subtracts the home office deduction of line 30 as figured, the second refigures it inside this line from the worksheet. The line-30 value is the same; the difference also includes the more-than-50% filter on listed property (Listed property used 50% or less (Form 4562 line 27) is refused on both the asset and the vehicle (asset.yaml, scveh.yaml)).

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

Second transcription's note: A statutory employee's line 31 goes to Schedule 1 but not to Schedule SE, so one amount cannot serve both. That case is refused. A loss with box 32b is refused for Form 6198.

Ruling: equivalent; project retained. The project's choose has one alternative whose guard (line 31 at least zero, or less than zero) always holds; it is line 31 on both sides. The choose carries the refusals that reach this line (statutory employee income, box 32b, and the others on sc.result).

### sc.f6 — Section 179 elected on property other than listed property
Status: **AGREE**

### sc.f14 — Special allowance on property other than listed property
Status: **AGREE**

### sc.f17 — MACRS on earlier property other than listed property
Status: **AGREE**

### sc.f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

### sc.f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

### sc.f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

### sc.f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

### sc.f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

### sc.f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

### sc.f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

### sc.f25 — Line 25 for this business
Status: **AGREE**

### sc.f26h — Column (h), line 26, for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"param": "sc.fifty_cents"}, {"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}], "test": "lt"}}], "op": "sum"}
```

Ruling: equivalent within scope; project retained. Column (h) of line 26 summed over the business's listed assets and vehicles on both sides. Listed property used 50% or less (Form 4562 line 27) is refused on both the asset and the vehicle (asset.yaml, scveh.yaml), so the second's filter for more than 50% business use selects the same entries within scope.

### sc.f28 — Line 28 for this business
Status: **DISAGREE**

Project:

```json
{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": null}], "op": "sum"}], "op": "sum"}
```

Second:

```json
{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}, {"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"param": "sc.fifty_cents"}, {"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}], "test": "lt"}}], "op": "sum"}], "op": "sum"}
```

Ruling: equivalent within scope; project retained. Lines 25 and 26 column (h) on both sides; the difference is the second's more-than-50% filter on line 26. Listed property used 50% or less (Form 4562 line 27) is refused on both the asset and the vehicle (asset.yaml, scveh.yaml), so the second's filter for more than 50% business use selects the same entries within scope.

### sc.f29 — Line 29 for this business
Status: **AGREE**

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
{"of": [{"const": 0}, {"line": "31"}], "op": "larger_of"}
```

Ruling: equivalent; project retained. The project selects line 31 under a guard that holds for every value (line 31 at least zero, or less than zero) and floors it at zero; the second takes the larger of zero and line 31. Both are line 31 when it is positive and zero otherwise.

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
{"of": [{"line": "12 (sc.s179_allowed)"}, {"of": [{"of": [{"of": [{"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "scveh", "field": "scveh.bonus", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}, {"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}], "test": "le"}}], "op": "sum"}, {"of": [{"collection": "asset", "field": "asset.dep_listed", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "asset.listed"}], "test": "eq"}, {"args": [{"param": "sc.fifty_cents"}, {"amount": {"param": "sc.one_cent"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}}, {"collection": "scveh", "field": "scveh.macrs", "op": "sum_over", "where": {"args": [{"of": [{"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_commuting"}, "op": "multiply_count"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_other"}, "op": "multiply_count"}], "op": "sum"}, {"amount": {"param": "sc.one_cent"}, "count": {"ref": "scveh.miles_business"}, "op": "multiply_count"}], "test": "lt"}}], "op": "sum"}], "op": "sum"}, {"collection": "asset", "field": "asset.bonus_2025", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y10"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y15sl"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y20"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y3"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y5"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_2025", "op": "sum_over", "where": {"args": [{"args": [{"const": "y7"}, {"ref": "asset.period"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}], "test": "all"}}, {"collection": "asset", "field": "asset.dep_prior", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "asset.listed"}], "test": "eq"}}], "op": "sum"}], "op": "sum"}
```

Ruling: equivalent within scope; project retained. Form 4562 line 22 for the business (line 12, lines 14 to 17, line 19 column (g), line 21) on both sides; the difference is the second's more-than-50% filter inside line 21. Listed property used 50% or less (Form 4562 line 27) is refused on both the asset and the vehicle (asset.yaml, scveh.yaml), so the second's filter for more than 50% business use selects the same entries within scope.

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
{"amount": {"line": "3a"}, "count": {"of": [{"line": "30(b)"}, {"param": "sc.ho_max_sqft"}], "op": "smaller_of"}, "op": "multiply_count"}
```

Ruling: equivalent; project retained. $5 times the smaller of the square footage and 300 (i1040sc Simplified Method Worksheet); the project chooses by an interval on the footage, the second takes the smaller of the two counts.

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

Ruling: equivalent where computed; project retained. The smaller of worksheet lines 1 and 4 on both sides. The project tests whether line 4 can exceed line 1 under the most section 179 deduction the business could take (its 2025 elections plus the carryover, since BUG-0060) and refuses where the two limits of Pub. 946 (p. 19) interact (sc.ho_both); the second takes the smaller of the two lines directly. Equal on every return the project computes.

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
{"ref": "s179.line12"}
```

Second transcription's note: i4562 line 12 allows the taxpayer-level deduction to be allocated among businesses in any manner. I encode only the case with one business taking the whole deduction, and refuse when an allocation among more than one business is needed.

Ruling: owner's ruling; project retained. With one Schedule C both take the return's line 12. With more than one, the owner ruled that each business deducts its own 2025 elections when line 12 equals them (no allocation needed) and more than one Schedule C is refused otherwise; the second gives each business the whole line 12 and relies on s179.multi.

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

Ruling: equivalent; project retained. The project selects line 31 under a guard that holds for every value (line 31 at least zero, or less than zero) and floors it at zero; the second takes the larger of zero and line 31. Both are line 31 when it is positive and zero otherwise.

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
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 4, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Ruling: owner-review reading; project retained. Schedule 1 line 15 times line 4 over line 5 on both sides. The project rounds the ratio to six places (amb.2025.f7206_ratio_places, an agent reading for owner review in TASKS.md); the second to four.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **AGREE**

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 6, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "4 (sc.f7206_line4)"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4 (sc.f7206_line4)"}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}, "op": "prorate", "part": {"line": "4 (sc.f7206_line4)"}, "places": 4, "whole": {"line": "5 (sc.f7206_line5)"}}}], "op": "choose"}
```

Ruling: owner-review reading; project retained. Schedule 1 line 16 times line 4 over line 5 on both sides (amb.2025.f7206_plan_attribution); the project also enters zero for a person with no Schedule C, which cannot occur within this collection. The project rounds the ratio to six places (amb.2025.f7206_ratio_places, an agent reading for owner review in TASKS.md); the second to four.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **AGREE**

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **DISAGREE**

Project:

```json
{"line": "10 (sc.f7206_line10)"}
```

Second:

```json
{"from": {"line": "10 (sc.f7206_line10)"}, "op": "subtract", "take": {"const": 0}}
```

Second transcription's note: Line 12 (Form 2555, line 45) is computed only in the case with no Form 2555. Line 11 (S corporation wages) does not apply to a Schedule C business.

Ruling: equivalent; project retained. Line 12 (Form 2555) is refused and line 11 (S corporation) does not apply, so line 13 is line 10 on both sides.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **AGREE**

### 1(c) — Qualified business income or (loss) of this business
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract", "take": {"of": [{"line": "14 (sc.f7206_line14)"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "lt"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"ref": "person.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"ref": "person.wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}, "op": "prorate", "part": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "31"}], "test": "le"}, {"args": [{"line": "31"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"line": "31"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "places": 6, "whole": {"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}}}], "op": "choose"}], "op": "sum"}}
```

Second:

```json
{"from": {"line": "31"}, "op": "subtract", "take": {"of": [{"line": "14 (sc.f7206_line14)"}, {"line": "7 (sc.f7206_line7)"}, {"line": "9 (sc.f7206_line9)"}], "op": "sum"}}
```

Ruling: equivalent; project retained. Both subtract from line 31 the deductible part of self-employment tax, the SEP or SIMPLE deduction and the health insurance deduction attributable to the business (i8995 p. 2; amb.2025.qbi_attribution). The second uses Form 7206 lines 7, 9 and 14 for the first two; the project's sc.qbi_se and sc.qbi_plan prorate the same amounts by the same ratio (net profit over person.positive_profits, which is Form 7206 line 5), so the comparison sees references on one side and their expansion on the other.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sc.line31_pre179 | sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.method_other, sc.special, sc.spouse_owned |
| sc.result | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.h_not_at_risk, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sc.h_ho_interact, sc.h_ho_multi, sc.h_not_at_risk, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |
| sc.profit_pos | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 3 (sc.line3) | sc.method_other, sc.spouse_owned | sc.method_other, sc.spouse_owned |
| 4 (sc.line4) | sc.inventory_other | - |
| 5 (sc.line5) | sc.inventory_other, sc.method_other, sc.spouse_owned | sc.method_other, sc.spouse_owned |
| 7 (sc.line7) | sc.inventory_other, sc.method_other, sc.spouse_owned | sc.method_other, sc.spouse_owned |
| 12 (sc.line12) | sc.special | sc.special |
| 13 (sc.line13) | s179.multi | - |
| 27a | sc.special | sc.special |
| 28 | s179.multi, sc.special | sc.special |
| 29 | s179.multi, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.method_other, sc.special, sc.spouse_owned |
| 1 (sc.ho_line1) | s179.multi, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.method_other, sc.special, sc.spouse_owned |
| 5 (sc.ho_line5) | s179.multi, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | s179.multi, sc.method_other, sc.special, sc.spouse_owned |
| 30 | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 31 | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 42 | sc.inventory_other | - |
| 12 (sc.s179_allowed) | s179.multi | - |
| 4 (sc.f7206_line4) | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 7 (sc.f7206_line7) | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 8 (sc.f7206_line8) | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 9 (sc.f7206_line9) | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 10 (sc.f7206_line10) | s179.multi, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 13 (sc.f7206_line13) | s179.multi, sa.excluded_income, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sa.excluded_income, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 14 (sc.f7206_line14) | s179.multi, sa.excluded_income, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.hi_screen, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned | sa.excluded_income, sc.h_ho_interact, sc.h_ho_multi, sc.h_passive_activity, sc.hi_screen, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned |
| 1(c) | s179.multi, sa.excluded_income, sc.h_ho_interact, sc.h_ho_multi, sc.h_not_at_risk, sc.h_passive_activity, sc.hi_screen, sc.ho_other, sc.inventory_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory | sa.excluded_income, sc.h_ho_interact, sc.h_ho_multi, sc.h_not_at_risk, sc.h_passive_activity, sc.hi_screen, sc.ho_other, sc.method_other, sc.special, sc.spouse_owned, sc.statutory |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sc.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sc.one
    printed: "(helper)"
    label: "One business"
    type: Count
    expr: {op: param, ref: sc.one}

  - id: sc.line3
    printed: "3 (sc.line3)"
    label: "Subtract line 2 from line 1"
    type: Dollars
    expr: {op: subtract, from: sc.line1, take: sc.line2}
    refuses: [sc.method_other, sc.spouse_owned]
    note: "The screens for accounting method (line F) and spouse ownership do not belong to any one printed amount line. I attached them to line 3, the first computed line of Part I."

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
    expr: {op: copy, from: sc.h_zero}
    refuses: [sc.special]

  # ---- Form 4562 amounts for this business ----
  - id: sc.f6
    printed: "(helper)"
    label: "Section 179 elected on property other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.s179_2025
      where: {op: test, eq: [asset.listed, {const: false}]}

  - id: sc.f14
    printed: "(helper)"
    label: "Special allowance on property other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.bonus_2025
      where: {op: test, eq: [asset.listed, {const: false}]}

  - id: sc.f17
    printed: "(helper)"
    label: "MACRS on earlier property other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_prior
      where: {op: test, eq: [asset.listed, {const: false}]}

  - id: sc.f19_y3
    printed: "(helper)"
    label: "MACRS on 2025 property of period y3 other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_2025
      where: {op: test, all: [{op: test, eq: [asset.period, {const: "y3"}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: sc.f19_y5
    printed: "(helper)"
    label: "MACRS on 2025 property of period y5 other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_2025
      where: {op: test, all: [{op: test, eq: [asset.period, {const: "y5"}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: sc.f19_y7
    printed: "(helper)"
    label: "MACRS on 2025 property of period y7 other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_2025
      where: {op: test, all: [{op: test, eq: [asset.period, {const: "y7"}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: sc.f19_y10
    printed: "(helper)"
    label: "MACRS on 2025 property of period y10 other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_2025
      where: {op: test, all: [{op: test, eq: [asset.period, {const: "y10"}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: sc.f19_y15
    printed: "(helper)"
    label: "MACRS on 2025 property of period y15 other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_2025
      where: {op: test, all: [{op: test, eq: [asset.period, {const: "y15"}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: sc.f19_y20
    printed: "(helper)"
    label: "MACRS on 2025 property of period y20 other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_2025
      where: {op: test, all: [{op: test, eq: [asset.period, {const: "y20"}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: sc.f19_y15sl
    printed: "(helper)"
    label: "MACRS on 2025 property of period y15sl other than listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_2025
      where: {op: test, all: [{op: test, eq: [asset.period, {const: "y15sl"}]}, {op: test, eq: [asset.listed, {const: false}]}]}

  - id: sc.h_f25_assets
    printed: "(helper)"
    label: "Special allowance on listed property other than vehicles"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.bonus_2025
      where: {op: test, eq: [asset.listed, {const: true}]}

  - id: sc.h_f25_veh
    printed: "(helper)"
    label: "Special allowance on vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.bonus}

  - id: sc.f25
    printed: "(helper)"
    label: "Line 25 for this business"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f25_assets, sc.h_f25_veh]}

  - id: sc.h_f26_assets
    printed: "(helper)"
    label: "Column (h) of listed property other than vehicles used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_listed
      where: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.over_half, {const: true}]}]}

  - id: sc.h_f26_veh
    printed: "(helper)"
    label: "Column (h) of vehicles used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: scveh
      field: scveh.macrs
      where: {op: test, eq: [scveh.low_use, {const: false}]}

  - id: sc.f26h
    printed: "(helper)"
    label: "Column (h), line 26, for this business"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f26_assets, sc.h_f26_veh]}

  - id: sc.h_f27_assets
    printed: "(helper)"
    label: "Column (h) of listed property other than vehicles used 50% or less in a qualified business use"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.dep_listed
      where: {op: test, all: [{op: test, eq: [asset.listed, {const: true}]}, {op: test, eq: [asset.over_half, {const: false}]}]}

  - id: sc.h_f27_veh
    printed: "(helper)"
    label: "Column (h) of vehicles used 50% or less in a qualified business use"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: scveh
      field: scveh.macrs
      where: {op: test, eq: [scveh.low_use, {const: true}]}

  - id: sc.h_f27
    printed: "(helper)"
    label: "Column (h), line 27, for this business"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f27_assets, sc.h_f27_veh]}

  - id: sc.f28
    printed: "(helper)"
    label: "Line 28 for this business: add amounts in column (h), lines 25 through 27"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f25, sc.f26h, sc.h_f27]}

  - id: sc.h_f29_assets
    printed: "(helper)"
    label: "Section 179 elected on listed property other than vehicles"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: asset
      field: asset.s179_2025
      where: {op: test, eq: [asset.listed, {const: true}]}

  - id: sc.h_f29_veh
    printed: "(helper)"
    label: "Section 179 elected on vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.s179_2025}

  - id: sc.f29
    printed: "(helper)"
    label: "Line 29 for this business: add amounts in column (i), line 26"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_f29_assets, sc.h_f29_veh]}

  - id: sc.h_mq_q4_a
    printed: "(helper)"
    label: "mq_q4 of this business's property"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_q4}

  - id: sc.h_mq_q4_v
    printed: "(helper)"
    label: "mq_q4 of this business's vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.mq_q4}

  - id: sc.mq_q4
    printed: "(helper)"
    label: "mq_q4 of this business"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_mq_q4_a, sc.h_mq_q4_v]}

  - id: sc.h_mq_total_a
    printed: "(helper)"
    label: "mq_total of this business's property"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.mq_total}

  - id: sc.h_mq_total_v
    printed: "(helper)"
    label: "mq_total of this business's vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.mq_total}

  - id: sc.mq_total
    printed: "(helper)"
    label: "mq_total of this business"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_mq_total_a, sc.h_mq_total_v]}

  - id: sc.h_cost179_a
    printed: "(helper)"
    label: "cost179 of this business's property"
    type: NonNegDollars
    expr: {op: sum_over, collection: asset, field: asset.cost179}

  - id: sc.h_cost179_v
    printed: "(helper)"
    label: "cost179 of this business's vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.cost179}

  - id: sc.cost179
    printed: "(helper)"
    label: "cost179 of this business"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_cost179_a, sc.h_cost179_v]}

  - id: sc.h_dep_other
    printed: "(helper)"
    label: "Depreciation other than the section 179 expense deduction (Form 4562, line 22 without line 12)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f14, sc.f17, sc.f19_y3, sc.f19_y5, sc.f19_y7, sc.f19_y10, sc.f19_y15, sc.f19_y20, sc.f19_y15sl, sc.f28]}
    note: "Form 4562, line 22 adds line 12, lines 14 through 17, lines 19 and 20, and line 21 (= line 28). Lines 15, 16 and 20 are outside the computed scope, so they are not included here. Line 12 is added on Schedule C line 13 as sc.s179_allowed."

  - id: sc.s179_allowed
    printed: "12 (sc.s179_allowed)"
    label: "Section 179 expense deduction for this business"
    type: NonNegDollars
    expr: {op: copy, from: s179.line12}
    refuses: [s179.multi]
    note: "i4562 line 12 allows the taxpayer-level deduction to be allocated among businesses in any manner. I encode only the case with one business taking the whole deduction, and refuse when an allocation among more than one business is needed."

  - id: sc.line13
    printed: "13 (sc.line13)"
    label: "Depreciation and section 179 expense deduction (not included in Part III)"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_dep_other, sc.s179_allowed]}

  - id: sc.h_veh_lease
    printed: "(helper)"
    label: "Business part of vehicle lease payments"
    type: NonNegDollars
    expr: {op: sum_over, collection: scveh, field: scveh.line20a}

  - id: sc.line20a
    printed: "20a"
    label: "Rent or lease: vehicles, machinery, and equipment"
    type: NonNegDollars
    expr: {op: sum, of: [sc.rent_equipment, sc.h_veh_lease]}

  - id: sc.h_meals_50_ded
    printed: "(helper)"
    label: "50% of the meals subject to the 50% limit"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_50, rate: {param: sc.meals_rate}}

  - id: sc.h_meals_80_ded
    printed: "(helper)"
    label: "80% of the meals under the DOT hours of service limits"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sc.meals_80, rate: {param: sc.meals_rate_dot}}

  - id: sc.line24b
    printed: "24b"
    label: "Deductible meals"
    type: NonNegDollars
    expr: {op: sum, of: [sc.h_meals_50_ded, sc.h_meals_80_ded, sc.meals_100]}

  - id: sc.line27a
    printed: "27a"
    label: "Energy efficient commercial buildings deduction (attach Form 7205)"
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
    expr: {op: sum, of: [sc.line8, sc.line9, sc.line10, sc.line11, sc.line12, sc.line13, sc.line14, sc.line15, sc.line16a, sc.line16b, sc.line17, sc.line18, sc.line19, sc.line20a, sc.line20b, sc.line21, sc.line22, sc.line23, sc.line24a, sc.line24b, sc.line25, sc.line26, sc.line27a, sc.line27b]}

  - id: sc.line29
    printed: "29"
    label: "Tentative profit or (loss). Subtract line 28 from line 7"
    type: Dollars
    expr: {op: subtract, from: sc.line7, take: sc.line28}

  - id: sc.h_line28_pre179
    printed: "(helper)"
    label: "Line 28 without the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: sum, of: [sc.line8, sc.line9, sc.line10, sc.line11, sc.line12, sc.h_dep_other, sc.line14, sc.line15, sc.line16a, sc.line16b, sc.line17, sc.line18, sc.line19, sc.line20a, sc.line20b, sc.line21, sc.line22, sc.line23, sc.line24a, sc.line24b, sc.line25, sc.line26, sc.line27a, sc.line27b]}

  - id: sc.h_line29_pre179
    printed: "(helper)"
    label: "Line 29 without the section 179 expense deduction"
    type: Dollars
    expr: {op: subtract, from: sc.line7, take: sc.h_line28_pre179}

  # ---- Simplified Method Worksheet ----
  - id: sc.line3a
    printed: "3a"
    label: "Maximum allowable amount (per square foot)"
    type: NonNegDollars
    expr: {op: param, ref: sc.ho_rate}

  - id: sc.h_ho_cap
    printed: "(helper)"
    label: "300 square feet"
    type: Count
    expr: {op: param, ref: sc.ho_max_sqft}

  - id: sc.h_ho_line2
    printed: "(helper)"
    label: "Allowable square footage for the qualified business use. Don't enter more than 300 square feet (worksheet line 2)"
    type: Count
    expr: {op: smaller_of, of: [sc.ho_sqft, sc.h_ho_cap]}
    note: "Line 2 is the smaller of the square feet actually used or 300 when the same area was used all year. Part-year use, shared space and daycare (line 3b other than 1.0) are taken as covered by the sc.ho_other screen. Line 3c is therefore line 3a times 1.0, which is line 3a."

  - id: sc.ho_line4
    printed: "4 (sc.ho_line4)"
    label: "Multiply line 2 by line 3c"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sc.line3a, count: sc.h_ho_line2}

  - id: sc.ho_line1
    printed: "1 (sc.ho_line1)"
    label: "Gross income limitation (Schedule C, line 29)"
    type: Dollars
    expr: {op: copy, from: sc.line29}
    note: "Lines A to E of the instructions also add home-use gains (Form 8949, Form 4797) and subtract unrelated losses. They also require an allocation when part of the income comes from elsewhere. Those cases are taken as covered by the sc.ho_other screen, so line E equals line A (Schedule C, line 29)."

  - id: sc.h_ho_min
    printed: "(helper)"
    label: "The smaller of line 1 or line 4"
    type: Dollars
    expr: {op: smaller_of, of: [sc.ho_line1, sc.ho_line4]}

  - id: sc.ho_line5
    printed: "5 (sc.ho_line5)"
    label: "Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.h_ho_min, take: {const: 0}}

  - id: sc.h_ho_multi
    printed: "(helper)"
    label: "This person claims the business use of the home for more than one Schedule C (300 square feet shared among businesses)"
    type: Bool
    expr: {op: test, gt: [person.ho_count, {param: sc.one}]}

  - id: sc.h_ho_interact
    printed: "(helper)"
    label: "The gross income limitation reduces the home deduction while a section 179 deduction is taken (Pub. 946, two different taxable income limits)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, lt: [sc.line29, sc.ho_line4]}
        - {op: test, gt: [sc.s179_allowed, {const: 0}]}

  - id: sc.line30
    printed: "30"
    label: "Expenses for business use of your home"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sc.ho_uses, {const: true}]}, then: sc.ho_line5}
        - {guard: {op: test, eq: [sc.ho_uses, {const: false}]}, then: sc.h_zero}
    refuses: [sc.ho_other, sc.h_ho_multi, sc.h_ho_interact]
    note: "The home-office gross income limit depends on line 29, which includes the section 179 deduction. The section 179 business income limit depends on net profit after the home-office deduction. Pub. 946 resolves this with an eight-step procedure. I compute only the cases where the two limits cannot interact, and refuse otherwise (sc.h_ho_interact)."

  - id: sc.line31
    printed: "31"
    label: "Net profit or (loss). Subtract line 30 from line 29"
    type: Dollars
    expr: {op: subtract, from: sc.line29, take: sc.line30}
    refuses: [sc.h_passive_activity]

  - id: sc.h_passive_activity
    printed: "(helper)"
    label: "Line G answered No (did not materially participate); the passive activity rules (Form 8582) apply"
    type: Bool
    expr: {op: test, eq: [sc.passive, {const: false}]}
    note: "It is open whether sc.passive holds the answer to line G. I read it as true = Yes, materially participated. A No answer sends the filer to Form 8582 even with a profit, so it is refused."

  - id: sc.h_ho_pre_floor
    printed: "(helper)"
    label: "Line 29 without the section 179 deduction; if zero or less, zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.h_line29_pre179, take: {const: 0}}

  - id: sc.h_ho_pre_min
    printed: "(helper)"
    label: "Simplified method amount figured with line 29 without the section 179 deduction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.ho_line4, sc.h_ho_pre_floor]}

  - id: sc.h_ho_pre
    printed: "(helper)"
    label: "Line 30 figured without the section 179 deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sc.ho_uses, {const: true}]}, then: sc.h_ho_pre_min}
        - {guard: {op: test, eq: [sc.ho_uses, {const: false}]}, then: sc.h_zero}

  - id: sc.line31_pre179
    printed: "(helper)"
    label: "Line 31 without the section 179 expense deduction"
    type: Dollars
    expr: {op: subtract, from: sc.h_line29_pre179, take: sc.h_ho_pre}
    note: "Equals line 31 plus the section 179 deduction in every case not refused at line 30. Either no section 179 deduction is taken, or line 4 is not limited by line 29."

  - id: sc.h_loss
    printed: "(helper)"
    label: "Line 31 is a loss"
    type: Bool
    expr: {op: test, lt: [sc.line31, {const: 0}]}

  - id: sc.h_not_at_risk
    printed: "(helper)"
    label: "A loss and some investment is not at risk (box 32b); Form 6198 required"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sc.h_loss, {const: true}]}
        - {op: test, eq: [sc.at_risk, {const: false}]}

  - id: sc.result
    printed: "(helper)"
    label: "The amount for Schedule 1, line 3 and Schedule SE, line 2"
    type: Dollars
    expr: {op: copy, from: sc.line31}
    refuses: [sc.statutory, sc.h_not_at_risk]
    note: "A statutory employee's line 31 goes to Schedule 1 but not to Schedule SE, so one amount cannot serve both. That case is refused. A loss with box 32b is refused for Form 6198."

  - id: sc.profit_pos
    printed: "(helper)"
    label: "Net profit of this business (zero for a loss)"
    type: NonNegDollars
    expr: {op: larger_of, of: [sc.line31, sc.h_zero]}

  # ---- Part III ----
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

  # ---- Form 7206 ----
  - id: sc.f7206_line2
    printed: "2 (sc.f7206_line2)"
    label: "Qualified long-term care insurance (the smaller of payments or the age limit, for each person covered)"
    type: NonNegDollars
    expr: {op: sum_over, collection: ltc, field: ltc.amount}

  - id: sc.f7206_line3
    printed: "3 (sc.f7206_line3)"
    label: "Add lines 1 and 2"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f7206_line1, sc.f7206_line2]}

  - id: sc.f7206_line4
    printed: "4 (sc.f7206_line4)"
    label: "Net profit from the trade or business under which the insurance plan is established"
    type: NonNegDollars
    expr: {op: copy, from: sc.profit_pos}

  - id: sc.f7206_line5
    printed: "5 (sc.f7206_line5)"
    label: "Total of all net profits from Schedule C, line 31"
    type: NonNegDollars
    expr: {op: copy, from: person.positive_profits}

  - id: sc.h_f7206_has
    printed: "(helper)"
    label: "Line 4 is more than zero"
    type: Bool
    expr: {op: test, gt: [sc.f7206_line4, {const: 0}]}

  - id: sc.h_f7206_line7_pos
    printed: "(helper)"
    label: "Schedule 1, line 15, times line 6 (line 4 divided by line 5)"
    type: NonNegDollars
    expr: {op: prorate, amount: person.se_line13, part: sc.f7206_line4, whole: sc.f7206_line5, places: 4}
    note: "Line 6 (divide line 4 by line 5) states no rounding; I chose four decimal places. Schedule 1, line 15 is read as this person's deduction (Schedule SE, line 13), since the form is one person's."

  - id: sc.f7206_line7
    printed: "7 (sc.f7206_line7)"
    label: "Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the percentage on line 6"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sc.h_f7206_has, {const: true}]}, then: sc.h_f7206_line7_pos}
        - {guard: {op: test, eq: [sc.h_f7206_has, {const: false}]}, then: sc.h_zero}

  - id: sc.f7206_line8
    printed: "8 (sc.f7206_line8)"
    label: "Subtract line 7 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line4, take: sc.f7206_line7}
    note: "The form gives no zero floor, but line 7 is a fraction of the self-employment tax deduction and cannot exceed line 4. The floor only keeps the type non-negative."

  - id: sc.h_f7206_line9_pos
    printed: "(helper)"
    label: "This person's SEP or SIMPLE deduction times line 4 divided by line 5"
    type: NonNegDollars
    expr: {op: prorate, amount: person.plan_deduction, part: sc.f7206_line4, whole: sc.f7206_line5, places: 4}
    note: "The form does not say how to find the part of Schedule 1, line 16 attributable to this business. I allocate this person's plan deduction in proportion to net profit, as line 7 does."

  - id: sc.f7206_line9
    printed: "9 (sc.f7206_line9)"
    label: "Schedule 1, line 16, attributable to the same trade or business"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sc.h_f7206_has, {const: true}]}, then: sc.h_f7206_line9_pos}
        - {guard: {op: test, eq: [sc.h_f7206_has, {const: false}]}, then: sc.h_zero}

  - id: sc.f7206_line10
    printed: "10 (sc.f7206_line10)"
    label: "Subtract line 9 from line 8"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sc.f7206_line8, take: sc.f7206_line9}
    note: "The form gives no zero floor. I floor at zero so the line stays non-negative; the deduction on line 14 cannot be less than zero."

  - id: sc.f7206_line13
    printed: "13 (sc.f7206_line13)"
    label: "Subtract line 12 from line 10"
    type: NonNegDollars
    expr: {op: subtract, from: sc.f7206_line10, take: {const: 0}}
    refuses: [sa.excluded_income]
    note: "Line 12 (Form 2555, line 45) is computed only in the case with no Form 2555. Line 11 (S corporation wages) does not apply to a Schedule C business."

  - id: sc.h_f7206_min
    printed: "(helper)"
    label: "The smaller of line 3 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sc.f7206_line3, sc.f7206_line13]}

  - id: sc.f7206_line14
    printed: "14 (sc.f7206_line14)"
    label: "Self-employed health insurance deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sc.hi_uses, {const: true}]}, then: sc.h_f7206_min}
        - {guard: {op: test, eq: [sc.hi_uses, {const: false}]}, then: sc.h_zero}
    refuses: [sc.hi_screen]

  # ---- Form 8995 line 1(c) ----
  - id: sc.h_qbi_ded
    printed: "(helper)"
    label: "Deductions attributable to this business: deductible part of self-employment tax, self-employed retirement plan contributions and self-employed health insurance deduction"
    type: NonNegDollars
    expr: {op: sum, of: [sc.f7206_line7, sc.f7206_line9, sc.f7206_line14]}
    note: "i8995 says QBI accounts for the deductible part of self-employment tax, self-employed health insurance and retirement contributions attributable to the business, but gives no allocation rule. I use the profit-share allocations of Form 7206, lines 7 and 9, which give zero for a business with a loss."

  - id: sc.line1(c)
    printed: "1(c)"
    label: "Qualified business income or (loss) of this business"
    type: Dollars
    expr: {op: subtract, from: sc.result, take: sc.h_qbi_ded}
```
```
