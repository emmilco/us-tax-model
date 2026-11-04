# Transcription agreement — asset

Second transcription of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` by an isolated model (spec 6.5), compared line by line with `forms/2025/asset.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 3bd958c1cda7b95c1eefe8deed517d8b2b0fa71fac8a0a039a084661fd161b3f |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 77448d9efd60568e88aa320de925a9afc86c212f00c2169ecf0b3b8c7ae5ce82 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 6ff28f69c232cb157b95a0aa2bfb0fc389f458f23dadbb47104466a281c7c6d4 |
| printed lines compared | 16 |
| agree / disagree / missing | 1 / 15 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 32, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, f1040, f4952, household, refund, s1, sa, scope |
| named line | f5329 |
| shared page | f4562, mq, person, s179, sc, scveh |

## Lines

### asset.dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "17"}, {"line": "19(g)"}, {"line": "26(h)"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Ruling: model error; The candidate takes the 2025 convention from asset.prior_conv, the answer for the year a prior-year asset was placed in service, instead of the mid-quarter test (p946 p. 34, "the mid-quarter convention applies if the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year are more than 40%"): stage14.asset.mq_7yr sofa project $357.00, candidate $1,429.00 (half-year rate where the mid-quarter test applies), classm.eic.3.deepseek item_1 a Q2 asset figured at the Q4 rate; and it is unknown where prior_conv is not asked (classm.f8962.4.deepseek item_1, classm.asset.1 biz_b items 1 and 2). The candidate also adds lines 17, 6(c) and 14 to the 2025 amount: the values are an interface gap on the values: the published interface gives only the name (labels are withheld by design) and the pages do not fix whether it includes the special allowance; the candidate said so in its note. The project's helper is MACRS (line 19(g)) on 2025 property, the special allowance being the separate asset.bonus_2025; the section 179 amount has its own interface asset.s179_2025. Completed value differences include classm.f8960.1.deepseek, classm.g28.1.deepseek, classm.sd.1.deepseek, classm.u1250.1.deepseek, classm.clcw26.1.deepseek item_1 project $0.00, candidate $46,128.00, and classm.f8880.2.deepseek spouse item_2 $0.00 against $39,115.00; the candidate asks asset.not179 of 2025 property used 50% or less in the business or of qualified improvement property with no election (classm.f8962.4 and .deepseek item_2, classm.f8995.3 biz_b item_1, stage14.asset.low_use_nonlisted), an answer the source needs only for Form 4562 line 2 and the election (p946 p. 17; i4562 p. 3, "used predominantly (more than 50%) in your trade or business"); same as the backlog-round ruling. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 396 of 1,364 agree; on completed returns 122 value, 52 candidate-unknown.

### asset.bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "14"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Where the property was acquired before January 20, 2025, the full choice is read as the applicable 40% allowance under the instructions.

Ruling: model error; the candidate asks asset.not179 of 2025 property used 50% or less in the business or of qualified improvement property with no election (classm.f8962.4 and .deepseek item_2, classm.f8995.3 biz_b item_1, stage14.asset.low_use_nonlisted), an answer the source needs only for Form 4562 line 2 and the election (p946 p. 17; i4562 p. 3, "used predominantly (more than 50%) in your trade or business"); same as the backlog-round ruling. No value differs. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,245 of 1,364 agree; on completed returns 3 candidate-unknown. Every other difference is a record withholding an answer the interview asks of the asset (placed, class, screen, pct, listed, cost) or a cited refusal (asset.screened, asset.outside, asset.qip_early, asset.listed_low; fixtures stage14.asset.refuse_*), on refused or incomplete returns.

### asset.s179_2025 — Section 179 elected on 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: This is the elected section 179 amount for this property for 2025; the business-income limitation is applied at the Form 4562 summary level.

Ruling: model error; same as the backlog-round ruling. i4562 p. 5, Line 6, Column (c), Elected cost; the candidate asks asset.not179 of 2025 property used 50% or less in the business or of qualified improvement property with no election (classm.f8962.4 and .deepseek item_2, classm.f8995.3 biz_b item_1, stage14.asset.low_use_nonlisted), an answer the source needs only for Form 4562 line 2 and the election (p946 p. 17; i4562 p. 3, "used predominantly (more than 50%) in your trade or business"); same as the backlog-round ruling. No completed value differs. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,225 of 1,364 agree; on completed returns 9 candidate-unknown.

### asset.mq_q4 — Mid-quarter test basis, fourth quarter
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "asset.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "outside"}, {"line": "(d)"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "outside"}, {"line": "(d)"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; p946 p. 34, "the total depreciable bases of MACRS property you placed in service during the last 3 months". The candidate asks asset.quarter of property not placed in service in 2025 (classm.asset.1 biz_a item_1, classm.s8812.3 item_1: project $0.00, candidate unknown), an answer the interview does not ask and the source does not need. No value differs. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,201 of 1,364 agree; on completed returns 6 candidate-unknown.

### asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": "outside"}, {"line": "(d)"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "outside"}, {"line": "(d)"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; same as the backlog-round ruling. p946 p. 34; the candidate asks asset.not179 of 2025 property used 50% or less in the business or of qualified improvement property with no election (classm.f8962.4 and .deepseek item_2, classm.f8995.3 biz_b item_1, stage14.asset.low_use_nonlisted), an answer the source needs only for Form 4562 line 2 and the election (p946 p. 17; i4562 p. 3, "used predominantly (more than 50%) in your trade or business"); same as the backlog-round ruling. No value differs. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,266 of 1,364 agree; on completed returns 9 candidate-unknown.

### asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; same as the backlog-round ruling. i4562 p. 4, Line 2, "(including the total cost of qualified real property that you elect to treat as section 179 property)". The candidate counts qualified improvement property with no election (stage14.asset.qip fitout, project $0.00, candidate $30,000.00); the candidate asks asset.not179 of 2025 property used 50% or less in the business or of qualified improvement property with no election (classm.f8962.4 and .deepseek item_2, classm.f8995.3 biz_b item_1, stage14.asset.low_use_nonlisted), an answer the source needs only for Form 4562 line 2 and the election (p946 p. 17; i4562 p. 3, "used predominantly (more than 50%) in your trade or business"); same as the backlog-round ruling. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,251 of 1,364 agree; on completed returns 1 value, 9 candidate-unknown.

### asset.dep_prior — MACRS on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"line": "26(h)"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: Uses line 17 for nonlisted prior-year property and line 26(h) for listed prior-year property.

Ruling: representation; i4562 p. 9, Line 17. The candidate now has a recovery-year branch (the backlog-round error is gone). Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,272 of 1,364 agree; no completed return differs. Every other difference is a record withholding an answer the interview asks of the asset (placed, class, screen, pct, listed, cost) or a cited refusal (asset.screened, asset.outside, asset.qip_early, asset.listed_low; fixtures stage14.asset.refuse_*), on refused or incomplete returns.

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
{"amount": {"amount": {"input": "asset.cost"}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "op": "prorate", "part": {"const": 1}, "places": 2, "whole": {"const": 100}}
```

Second transcription's note: The source prints only column (c); read here as the business/investment-use basis before the current-year section 179 and special allowance reductions, with line 19(c) applying those reductions.

Ruling: representation; i4562 p. 11, Column (c). The candidate shows the business basis before section 179 and the special allowance, the project's amount. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,268 of 1,364 agree; the only differences are project refusals on cited screens and project-unknown on records withholding answers the interview asks; no completed return differs.

### 14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; same as the backlog-round ruling. i4562 p. 5, Line 14; the candidate asks asset.not179 of 2025 property used 50% or less in the business or of qualified improvement property with no election (classm.f8962.4 and .deepseek item_2, classm.f8995.3 biz_b item_1, stage14.asset.low_use_nonlisted), an answer the source needs only for Form 4562 line 2 and the election (p946 p. 17; i4562 p. 3, "used predominantly (more than 50%) in your trade or business"); same as the backlog-round ruling. No value differs. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,252 of 1,364 agree; on completed returns 3 candidate-unknown.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **DISAGREE**

Project:

```json
{"line": "14"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; same as the backlog-round ruling. i4562 p. 14, Line 25. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,290 of 1,364 agree; no completed return differs; the differences are records withholding answers the interview asks or screen refusals.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; same as the backlog-round ruling. i4562 p. 5, Line 6. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,292 of 1,364 agree; no completed return differs.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "outside"}, {"line": "(d)"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "outside"}, {"line": "(d)"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; same as the backlog-round ruling. i4562 p. 9, Lines 19a Through 19j; the candidate asks asset.not179 of 2025 property used 50% or less in the business or of qualified improvement property with no election (classm.f8962.4 and .deepseek item_2, classm.f8995.3 biz_b item_1, stage14.asset.low_use_nonlisted), an answer the source needs only for Form 4562 line 2 and the election (p946 p. 17; i4562 p. 3, "used predominantly (more than 50%) in your trade or business"); same as the backlog-round ruling. No value differs. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,250 of 1,364 agree; on completed returns 9 candidate-unknown.

### 19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}
```

Ruling: model error; i4562 p. 9, Lines 19a Through 19j. The candidate takes the 2025 convention from asset.prior_conv, the answer for the year a prior-year asset was placed in service, instead of the mid-quarter test (p946 p. 34, "the mid-quarter convention applies if the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year are more than 40%"): stage14.asset.mq_7yr sofa project $357.00, candidate $1,429.00 (half-year rate where the mid-quarter test applies), classm.eic.3.deepseek item_1 a Q2 asset figured at the Q4 rate; and it is unknown where prior_conv is not asked (classm.f8962.4.deepseek item_1, classm.asset.1 biz_b items 1 and 2); also classm.f1040.6.deepseek spouse item_1 $432.42 against $1,296.79, classm.f8863.2 item_1 $345.06 against $1,380.25, classm.eic.3.deepseek item_2 $563.03 against $2,252.10. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 806 of 1,364 agree; on completed returns 19 value, 52 candidate-unknown.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "outside"}, {"line": "(d)"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "outside"}, {"line": "(d)"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i4562 p. 9, Line 17. The candidate now has the recovery-year branch (the backlog-round error is gone). Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,293 of 1,364 agree; no completed return differs; the differences are cited project refusals, records withholding asked answers, and candidate refusals and unknowns on refused or incomplete returns.

### 26(h) — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"line": "17"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"line": "19(g)"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_179"}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "ne"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_bonus"}}], "op": "choose"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i4562 p. 15, Column (h). The candidate takes the 2025 convention from asset.prior_conv, the answer for the year a prior-year asset was placed in service, instead of the mid-quarter test (p946 p. 34, "the mid-quarter convention applies if the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year are more than 40%"): stage14.asset.mq_7yr sofa project $357.00, candidate $1,429.00 (half-year rate where the mid-quarter test applies), classm.eic.3.deepseek item_1 a Q2 asset figured at the Q4 rate; and it is unknown where prior_conv is not asked (classm.f8962.4.deepseek item_1, classm.asset.1 biz_b items 1 and 2): classm.eic.3.deepseek item_1 (listed, Q2, mid-quarter applies) project $1,560.09, candidate $312.02, the 4th-quarter rate taken from prior_conv; classm.asset.1 biz_b item_2 unknown on prior_conv. Triage executable-triage-v2 (`../triage/asset.deepseek.json`, refresh round; 1,565 fixtures, 500 generated returns seed 20261026, 713 partial records): 1,229 of 1,364 agree; on completed returns 1 value, 1 candidate-unknown.

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
    expr: {op: prorate, amount: asset.h_cost_times_pct, part: asset.h_one_cent, whole: {const: 100}, places: 2}
    refuses: [asset.screen]
    note: "The source prints only column (c); read here as the business/investment-use basis before the current-year section 179 and special allowance reductions, with line 19(c) applying those reductions."
  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_line14_applies, {const: true}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.h_line14_applies, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    shown_when: asset.h_line14_applies
  - id: asset.f25
    printed: "25"
    label: "Special depreciation allowance for qualified listed property placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_line25_applies, {const: true}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.h_line25_applies, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    shown_when: asset.h_line25_applies
  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost of listed property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_line25_applies, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.h_line25_applies, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    shown_when: asset.h_line25_applies
  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_line19_applies, {const: true}]}
          then: asset.h_col19c_calc
        - guard: {op: test, eq: [asset.h_line19_applies, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    shown_when: asset.h_line19_applies
  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_macrs_rate}
    refuses: [asset.screen]
    shown_when: asset.h_line19_applies
  - id: asset.macrs_prior
    printed: "17"
    label: "Depreciation for tangible property placed in service in tax years beginning before 2025 and depreciated under MACRS"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_line17_applies, {const: true}]}
          then: asset.h_macrs_prior_within
        - guard: {op: test, eq: [asset.h_line17_applies, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    shown_when: asset.h_line17_applies
  - id: asset.dep_listed
    printed: "26(h)"
    label: "Depreciation deduction for listed property used more than 50% in a qualified business use"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_listed, {const: true}]}
          then: asset.h_dep_listed_within
        - guard: {op: test, eq: [asset.h_listed, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    shown_when: asset.listed
  - id: asset.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
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
  - id: asset.h_is2025
    printed: "(helper)"
    label: "Property placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}
  - id: asset.h_is_prior
    printed: "(helper)"
    label: "Property not placed in service in 2025"
    type: Bool
    expr: {op: test, eq: [asset.h_is2025, {const: false}]}
  - id: asset.h_listed
    printed: "(helper)"
    label: "Listed property"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: true}]}
  - id: asset.h_not_listed
    printed: "(helper)"
    label: "Not listed property"
    type: Bool
    expr: {op: test, eq: [asset.listed, {const: false}]}
  - id: asset.h_not179_false
    printed: "(helper)"
    label: "Property qualifies for section 179"
    type: Bool
    expr: {op: test, eq: [asset.not179, {const: false}]}
  - id: asset.h_period_not_outside
    printed: "(helper)"
    label: "Recovery period is within the MACRS GDS tables"
    type: Bool
    expr: {op: test, ne: [asset.period, {const: "outside"}]}
  - id: asset.h_after_jan19
    printed: "(helper)"
    label: "Property acquired after January 19, 2025"
    type: Bool
    expr: {op: test, eq: [asset.after_jan19, {const: true}]}
  - id: asset.h_line14_applies
    printed: "(helper)"
    label: "Line 14 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.h_not_listed, {const: true}]}
  - id: asset.h_line25_applies
    printed: "(helper)"
    label: "Line 25 or line 26(i) applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.h_listed, {const: true}]}
  - id: asset.h_line19_applies
    printed: "(helper)"
    label: "Line 19 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.h_not_listed, {const: true}]}
        - {op: test, eq: [asset.h_period_not_outside, {const: true}]}
  - id: asset.h_line17_applies
    printed: "(helper)"
    label: "Line 17 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is_prior, {const: true}]}
        - {op: test, eq: [asset.h_not_listed, {const: true}]}
        - {op: test, eq: [asset.h_period_not_outside, {const: true}]}
  - id: asset.h_q4
    printed: "(helper)"
    label: "Placed in service in the fourth quarter"
    type: Bool
    expr: {op: test, eq: [asset.quarter, {const: "q4"}]}
  - id: asset.h_mq_include
    printed: "(helper)"
    label: "Included in the mid-quarter test"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.h_period_not_outside, {const: true}]}
  - id: asset.h_recovery_year
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}
  - id: asset.h_last_year
    printed: "(helper)"
    label: "Last year of recovery"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}
  - id: asset.h_within_recovery
    printed: "(helper)"
    label: "2025 is within the recovery period"
    type: Bool
    expr: {op: test, le: [asset.h_recovery_year, asset.h_last_year]}
  - id: asset.h_macrs_rate
    printed: "(helper)"
    label: "MACRS GDS rate"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_recovery_year]}
  - id: asset.h_s179_eligible
    printed: "(helper)"
    label: "Section 179 property placed in service in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.h_not179_false, {const: true}]}
  - id: asset.h_bonus_base
    printed: "(helper)"
    label: "Basis for special depreciation allowance after section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.s179_2025}
  - id: asset.h_bonus_forty
    printed: "(helper)"
    label: "Special depreciation allowance at 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_bonus_base, rate: {param: sc.bonus_rate_40}}
  - id: asset.h_bonus_full_case
    printed: "(helper)"
    label: "Special depreciation allowance when full is chosen"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_after_jan19, {const: true}]}
          then: asset.h_bonus_base
        - guard: {op: test, eq: [asset.h_after_jan19, {const: false}]}
          then: asset.h_bonus_forty
  - id: asset.h_bonus_choice_amount
    printed: "(helper)"
    label: "Special depreciation allowance amount by choice"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.bonus_choice, {const: "full"}]}
          then: asset.h_bonus_full_case
        - guard: {op: test, eq: [asset.bonus_choice, {const: "forty"}]}
          then: asset.h_bonus_forty
        - guard: {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.zero
  - id: asset.h_col19c_after_s179
    printed: "(helper)"
    label: "Line 19(c) basis after section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.s179_2025}
  - id: asset.h_col19c_calc
    printed: "(helper)"
    label: "Line 19(c) basis after section 179 and special allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_col19c_after_s179, take: asset.bonus_2025}
  - id: asset.h_prior_basis_after_179
    printed: "(helper)"
    label: "Prior-year property basis after section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.prior_179}
  - id: asset.h_prior_basis
    printed: "(helper)"
    label: "Prior-year property basis after section 179 and special allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_prior_basis_after_179, take: asset.prior_bonus}
  - id: asset.h_macrs_prior_calc
    printed: "(helper)"
    label: "Prior-year property MACRS depreciation before recovery-period test"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_prior_basis, rate: asset.h_macrs_rate}
  - id: asset.h_macrs_prior_within
    printed: "(helper)"
    label: "Prior-year property MACRS depreciation within recovery period"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_within_recovery, {const: true}]}
          then: asset.h_macrs_prior_calc
        - guard: {op: test, eq: [asset.h_within_recovery, {const: false}]}
          then: asset.zero
  - id: asset.h_listed_s179
    printed: "(helper)"
    label: "Listed property section 179 reduction for the current year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.s179_2025
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.prior_179
  - id: asset.h_listed_bonus
    printed: "(helper)"
    label: "Listed property special allowance reduction for the current year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.bonus_2025
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.prior_bonus
  - id: asset.h_listed_basis_after_s179
    printed: "(helper)"
    label: "Listed property basis after section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.h_listed_s179}
  - id: asset.h_listed_basis
    printed: "(helper)"
    label: "Listed property basis after section 179 and special allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_listed_basis_after_s179, take: asset.h_listed_bonus}
  - id: asset.h_listed_macrs_calc
    printed: "(helper)"
    label: "Listed property MACRS depreciation before recovery-period test"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_listed_basis, rate: asset.h_macrs_rate}
  - id: asset.h_dep_listed_within
    printed: "(helper)"
    label: "Listed property MACRS depreciation within recovery period"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_within_recovery, {const: true}]}
          then: asset.h_listed_macrs_calc
        - guard: {op: test, eq: [asset.h_within_recovery, {const: false}]}
          then: asset.zero
  - id: asset.h_prior_any
    printed: "(helper)"
    label: "Current-year depreciation for prior-year property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_listed, {const: true}]}
          then: asset.dep_listed
        - guard: {op: test, eq: [asset.h_listed, {const: false}]}
          then: asset.macrs_prior
  - id: asset.h_mq_basis_after_s179
    printed: "(helper)"
    label: "Mid-quarter-test basis after section 179"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.basis, take: asset.s179_2025}
  - id: asset.s179_2025
    printed: "(helper)"
    label: "Section 179 amount for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_s179_eligible, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.h_s179_eligible, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    note: "This is the elected section 179 amount for this property for 2025; the business-income limitation is applied at the Form 4562 summary level."
  - id: asset.bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_bonus_choice_amount
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    note: "Where the property was acquired before January 20, 2025, the full choice is read as the applicable 40% allowance under the instructions."
  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service in 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_s179_eligible, {const: true}]}
          then: asset.basis
        - guard: {op: test, eq: [asset.h_s179_eligible, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
  - id: asset.mq_total
    printed: "(helper)"
    label: "Basis for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_mq_include, {const: true}]}
          then: asset.h_mq_basis_after_s179
        - guard: {op: test, eq: [asset.h_mq_include, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
  - id: asset.mq_q4
    printed: "(helper)"
    label: "Basis placed in service in the fourth quarter for the mid-quarter test"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_q4, {const: true}]}
          then: asset.mq_total
        - guard: {op: test, eq: [asset.h_q4, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
  - id: asset.dep_prior
    printed: "(helper)"
    label: "Current-year depreciation for property placed before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is_prior, {const: true}]}
          then: asset.h_prior_any
        - guard: {op: test, eq: [asset.h_is_prior, {const: false}]}
          then: asset.zero
    refuses: [asset.screen]
    note: "Uses line 17 for nonlisted prior-year property and line 26(h) for listed prior-year property."
  - id: asset.dep_2025
    printed: "(helper)"
    label: "Total 2025 depreciation and section 179 deduction for this property"
    type: NonNegDollars
    expr: {op: sum, of: [asset.s179_2025, asset.bonus_2025, asset.macrs2025, asset.macrs_prior, asset.dep_listed]}
    refuses: [asset.screen]
```
