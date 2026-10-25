# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | db325fe40900394a7a7dc28391803ab0dc4558755b927a9cc47449aaf1524e2b |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 705b144100978501b6560fdba21b14526cf0ad2157399772a690a11397bde7b7 |
| printed lines compared | 54 |
| agree / disagree / missing | 15 / 39 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### sd.line18 — 28% Rate Gain Worksheet result (supplied subtotal; worksheet deferred to Stage 4)
Status: **DISAGREE**

Project:

```json
{"ref": "g28.line7"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"of": [{"const": 0}, {"of": [{"of": [{"const": 0}, {"line": "7"}], "op": "smaller_of"}, {"ref": "div.box2d"}], "op": "sum"}], "op": "larger_of"}}], "op": "choose"}
```

Second transcription's note: The 28% Rate Gain Worksheet's section 1202 exclusion and other-form amounts are outside this slice; line 18 is computed only from Form 1099-DIV box 2d reduced by a Schedule D line 7 loss, and refuses the listed screening inputs otherwise.

Ruling: open

### sd.line19 — Unrecaptured Section 1250 Gain Worksheet result (supplied subtotal; worksheet deferred to 
Status: **DISAGREE**

Project:

```json
{"ref": "u1250.line18"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "div.box2b"}}], "op": "choose"}
```

Second transcription's note: The Unrecaptured Section 1250 Gain Worksheet is not fully reproduced in the archived text; chosen reading: with no other-form or special-sale source, line 19 is Form 1099-DIV box 2b.

Ruling: open

### sd.filing4952 — Are you filing Form 4952?
Status: **AGREE**

### sd.investment_election — Form 4952 line 4g (supplied subtotal; Form 4952 deferred to Stage 4)
Status: **AGREE**

### sd.filed — Schedule D required for entered sales or special distribution gains
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "g28.line7"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sd.other_forms"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "13"}], "test": "lt"}, {"args": [{"const": 0}, {"line": "15"}], "test": "ne"}, {"args": [{"const": 0}, {"line": "16"}], "test": "ne"}, {"args": [{"const": 0}, {"line": "7"}], "test": "ne"}], "test": "any"}
```

Second transcription's note: The archived pages do not define a separate filed flag; chosen reading: true when any Schedule D amount or carryover/other-form input is present. A return with transactions that net to zero in every total is not distinguished.

Ruling: open

### sd.zero — No amount on an inapplicable line
Status: **AGREE**

### sd.to1040 — Capital gain or limited capital loss for Form 1040 line 7a
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"line": "16"}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"line": "21"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "lt"}, "then": {"line": "16"}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"line": "21"}}], "op": "choose"}
```

Ruling: open

### sd.net_gain — Nonnegative net capital gain for QDCGT
Status: **DISAGREE**

Project:

```json
{"from": {"of": [{"line": "15"}, {"line": "16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "15"}], "test": "lt"}, {"args": [{"const": 0}, {"line": "16"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"line": "15"}, {"line": "16"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"line": "15"}, {"const": 0}], "test": "le"}, {"args": [{"line": "16"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Chosen reading: the smaller of Schedule D lines 15 and 16 when both are gains, otherwise zero, as in the Qualified Dividends and Capital Gain Tax Worksheet line 3.

Ruling: open

### 1a(d) — Line 1a, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sales.aggregate_eligible"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 1a(e) — Line 1a, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sales.aggregate_eligible"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 1a(g) — Line 1a, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sales.aggregate_eligible"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 1a(h) — Line 1a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sales.aggregate_eligible"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 1b(d) — Line 1b, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 1b(e) — Line 1b, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 1b(g) — Line 1b, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 1b(h) — Line 1b, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 2(d) — Line 2, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 2(e) — Line 2, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 2(g) — Line 2, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 2(h) — Line 2, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 3(d) — Line 3, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 3(e) — Line 3, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 3(g) — Line 3, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 3(h) — Line 3, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 8a(d) — Line 8a, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sales.aggregate_eligible"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 8a(e) — Line 8a, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sales.aggregate_eligible"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 8a(g) — Line 8a, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sales.aggregate_eligible"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 8a(h) — Line 8a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sales.aggregate_eligible"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 8b(d) — Line 8b, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 8b(e) — Line 8b, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 8b(g) — Line 8b, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 8b(h) — Line 8b, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 9(d) — Line 9, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 9(e) — Line 9, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 9(g) — Line 9, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 9(h) — Line 9, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 10(d) — Line 10, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 10(e) — Line 10, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 10(g) — Line 10, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 10(h) — Line 10, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **AGREE**

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **AGREE**

### 6 — Line 6: zero only after unsupported source/carryover screening
Status: **AGREE**

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **AGREE**

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **AGREE**

### 14 — Line 14: zero only after unsupported source/carryover screening
Status: **AGREE**

### 13 — Capital gain distributions
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "sd.distributions"}, {"param": "sales.zero"}], "op": "sum"}
```

Second:

```json
{"input": "sd.distributions"}
```

Ruling: open

### 7 — Combine the amounts for Schedule D line 7
Status: **AGREE**

### 15 — Combine the amounts for Schedule D line 15
Status: **AGREE**

### 16 — Combine the amounts for Schedule D line 16
Status: **AGREE**

### 17 — Are lines 15 and 16 both gains?
Status: **AGREE**

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"ref": "g28.line7"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"of": [{"const": 0}, {"of": [{"of": [{"const": 0}, {"line": "7"}], "op": "smaller_of"}, {"ref": "div.box2d"}], "op": "sum"}], "op": "larger_of"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "div.box2b"}}], "op": "choose"}], "test": "eq"}], "test": "all"}
```

Ruling: open

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **AGREE**

### 22 — Do you have qualified dividends?
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sd.line18 | div.section1202, sales.special, sd.carryover, sd.other_forms | sales.special |
| sd.line19 | sales.special, sd.carryover, sd.other_forms | sales.special |
| sd.filed | sd.carryover, sd.other_forms | - |
| sd.to1040 | sd.carryover, sd.other_forms | - |
| sd.net_gain | sd.carryover, sd.other_forms | - |
| 4 | sd.other_forms | - |
| 5 | sd.other_forms | - |
| 6 | sd.carryover | - |
| 11 | sd.other_forms | - |
| 12 | sd.other_forms | - |
| 14 | sd.carryover | - |
| 7 | sd.carryover, sd.other_forms | - |
| 15 | sd.carryover, sd.other_forms | - |
| 16 | sd.carryover, sd.other_forms | - |
| 17 | sd.carryover, sd.other_forms | - |
| 20 | div.section1202, sales.special, sd.carryover, sd.other_forms | sales.special |
| 21 | sd.carryover, sd.other_forms | - |

## Raw second transcription

```yaml
lines:
  - id: sd.line1a.d
    printed: "1a(d)"
    label: "Line 1a, column (d) — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "aggregate"}]
          - op: test
            eq: [sales.aggregate_eligible, {const: true}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
  - id: sd.line1a.e
    printed: "1a(e)"
    label: "Line 1a, column (e) — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "aggregate"}]
          - op: test
            eq: [sales.aggregate_eligible, {const: true}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
  - id: sd.line1a.g
    printed: "1a(g)"
    label: "Line 1a, column (g) — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "aggregate"}]
          - op: test
            eq: [sales.aggregate_eligible, {const: true}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
  - id: sd.line1a.h
    printed: "1a(h)"
    label: "Line 1a, column (h) — Gain or (loss): subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "aggregate"}]
          - op: test
            eq: [sales.aggregate_eligible, {const: true}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
  - id: sd.line1b.d
    printed: "1b(d)"
    label: "Line 1b, column (d) — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
  - id: sd.line1b.e
    printed: "1b(e)"
    label: "Line 1b, column (e) — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
  - id: sd.line1b.g
    printed: "1b(g)"
    label: "Line 1b, column (g) — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
  - id: sd.line1b.h
    printed: "1b(h)"
    label: "Line 1b, column (h) — Gain or (loss): subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
  - id: sd.line2.d
    printed: "2(d)"
    label: "Line 2, column (d) — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "B"}]
              - op: test
                eq: [sales.box, {const: "H"}]
  - id: sd.line2.e
    printed: "2(e)"
    label: "Line 2, column (e) — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "B"}]
              - op: test
                eq: [sales.box, {const: "H"}]
  - id: sd.line2.g
    printed: "2(g)"
    label: "Line 2, column (g) — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "B"}]
              - op: test
                eq: [sales.box, {const: "H"}]
  - id: sd.line2.h
    printed: "2(h)"
    label: "Line 2, column (h) — Gain or (loss): subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "B"}]
              - op: test
                eq: [sales.box, {const: "H"}]
  - id: sd.line3.d
    printed: "3(d)"
    label: "Line 3, column (d) — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "C"}]
              - op: test
                eq: [sales.box, {const: "I"}]
  - id: sd.line3.e
    printed: "3(e)"
    label: "Line 3, column (e) — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "C"}]
              - op: test
                eq: [sales.box, {const: "I"}]
  - id: sd.line3.g
    printed: "3(g)"
    label: "Line 3, column (g) — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "C"}]
              - op: test
                eq: [sales.box, {const: "I"}]
  - id: sd.line3.h
    printed: "3(h)"
    label: "Line 3, column (h) — Gain or (loss): subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "C"}]
              - op: test
                eq: [sales.box, {const: "I"}]
  - id: sd.line8a.d
    printed: "8a(d)"
    label: "Line 8a, column (d) — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "aggregate"}]
          - op: test
            eq: [sales.aggregate_eligible, {const: true}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
  - id: sd.line8a.e
    printed: "8a(e)"
    label: "Line 8a, column (e) — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "aggregate"}]
          - op: test
            eq: [sales.aggregate_eligible, {const: true}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
  - id: sd.line8a.g
    printed: "8a(g)"
    label: "Line 8a, column (g) — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "aggregate"}]
          - op: test
            eq: [sales.aggregate_eligible, {const: true}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
  - id: sd.line8a.h
    printed: "8a(h)"
    label: "Line 8a, column (h) — Gain or (loss): subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "aggregate"}]
          - op: test
            eq: [sales.aggregate_eligible, {const: true}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
  - id: sd.line8b.d
    printed: "8b(d)"
    label: "Line 8b, column (d) — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
  - id: sd.line8b.e
    printed: "8b(e)"
    label: "Line 8b, column (e) — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
  - id: sd.line8b.g
    printed: "8b(g)"
    label: "Line 8b, column (g) — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
  - id: sd.line8b.h
    printed: "8b(h)"
    label: "Line 8b, column (h) — Gain or (loss): subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
  - id: sd.line9.d
    printed: "9(d)"
    label: "Line 9, column (d) — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "E"}]
              - op: test
                eq: [sales.box, {const: "K"}]
  - id: sd.line9.e
    printed: "9(e)"
    label: "Line 9, column (e) — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "E"}]
              - op: test
                eq: [sales.box, {const: "K"}]
  - id: sd.line9.g
    printed: "9(g)"
    label: "Line 9, column (g) — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "E"}]
              - op: test
                eq: [sales.box, {const: "K"}]
  - id: sd.line9.h
    printed: "9(h)"
    label: "Line 9, column (h) — Gain or (loss): subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "E"}]
              - op: test
                eq: [sales.box, {const: "K"}]
  - id: sd.line10.d
    printed: "10(d)"
    label: "Line 10, column (d) — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "F"}]
              - op: test
                eq: [sales.box, {const: "L"}]
  - id: sd.line10.e
    printed: "10(e)"
    label: "Line 10, column (e) — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "F"}]
              - op: test
                eq: [sales.box, {const: "L"}]
  - id: sd.line10.g
    printed: "10(g)"
    label: "Line 10, column (g) — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "F"}]
              - op: test
                eq: [sales.box, {const: "L"}]
  - id: sd.line10.h
    printed: "10(h)"
    label: "Line 10, column (h) — Gain or (loss): subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            eq: [sales.route, {const: "detail"}]
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "F"}]
              - op: test
                eq: [sales.box, {const: "L"}]
  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.carryover]
  - id: sd.line11
    printed: "11"
    label: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
  - id: sd.line12
    printed: "12"
    label: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.carryover]
  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions. See the instructions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions}
  - id: sd.line7
    printed: "7"
    label: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)"
    type: Dollars
    expr:
      op: sum
      of:
        - sd.line1a.h
        - sd.line1b.h
        - sd.line2.h
        - sd.line3.h
        - sd.line4
        - sd.line5
        - sd.line6
  - id: sd.line15
    printed: "15"
    label: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)"
    type: Dollars
    expr:
      op: sum
      of:
        - sd.line8a.h
        - sd.line8b.h
        - sd.line9.h
        - sd.line10.h
        - sd.line11
        - sd.line12
        - sd.line13
        - sd.line14
  - id: sd.line16
    printed: "16"
    label: "Combine lines 7 and 15 and enter the result"
    type: Dollars
    expr:
      op: sum
      of:
        - sd.line7
        - sd.line15
  - id: sd.line17
    printed: "17"
    label: "Are lines 15 and 16 both gains?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [sd.line15, {const: 0}]}
        - {op: test, gt: [sd.line16, {const: 0}]}
  - id: sd.line20
    printed: "20"
    label: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sd.line18, {const: 0}]}
        - {op: test, eq: [sd.line19, {const: 0}]}
        - {op: test, eq: [sd.filing4952, {const: false}]}
  - id: sd.line21
    printed: "21"
    label: "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of: The loss on line 16; or ($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [sd.line16, {const: 0}]}
          then: sd.h_line21_loss
        - guard: {op: test, ge: [sd.line16, {const: 0}]}
          then: sd.zero
  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}
  - id: sd.line18
    printed: "(helper)"
    label: "If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.line17, {const: true}]}
          then: sd.h_line18_floor
        - guard: {op: test, eq: [sd.line17, {const: false}]}
          then: sd.zero
    refuses: [sd.other_forms, sd.carryover, sales.special, div.section1202]
    note: "The 28% Rate Gain Worksheet's section 1202 exclusion and other-form amounts are outside this slice; line 18 is computed only from Form 1099-DIV box 2d reduced by a Schedule D line 7 loss, and refuses the listed screening inputs otherwise."
  - id: sd.line19
    printed: "(helper)"
    label: "If you are required to complete the Unrecaptured Section 1250 Gain Worksheet (see instructions), enter the amount, if any, from line 18 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.line17, {const: true}]}
          then: div.box2b
        - guard: {op: test, eq: [sd.line17, {const: false}]}
          then: sd.zero
    refuses: [sd.other_forms, sales.special]
    note: "The Unrecaptured Section 1250 Gain Worksheet is not fully reproduced in the archived text; chosen reading: with no other-form or special-sale source, line 19 is Form 1099-DIV box 2b."
  - id: sd.filing4952
    printed: "(helper)"
    label: "Are you filing Form 4952?"
    type: Bool
    expr: {op: copy, from: f4952.required}
    note: "Taken from the required Form 4952 line used by Schedule D line 20."
  - id: sd.investment_election
    printed: "(helper)"
    label: "Form 4952 line 4g amount of qualified dividends and net capital gain elected into investment income"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line4g}
    note: "The Schedule D Tax Worksheet uses Form 4952 line 4g; this interface copies that line and is zero when there is no election."
  - id: sd.filed
    printed: "(helper)"
    label: "Is Schedule D filed?"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, ne: [sd.line16, {const: 0}]}
        - {op: test, ne: [sd.line7, {const: 0}]}
        - {op: test, ne: [sd.line15, {const: 0}]}
        - {op: test, gt: [sd.line13, {const: 0}]}
        - {op: test, eq: [sd.carryover, {const: true}]}
        - {op: test, eq: [sd.other_forms, {const: true}]}
    note: "The archived pages do not define a separate filed flag; chosen reading: true when any Schedule D amount or carryover/other-form input is present. A return with transactions that net to zero in every total is not distinguished."
  - id: sd.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sd.to1040
    printed: "(helper)"
    label: "Amount to enter on Form 1040, 1040-SR, or 1040-NR, line 7a"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sd.line16, {const: 0}]}
          then: sd.line16
        - guard: {op: test, lt: [sd.line16, {const: 0}]}
          then: sd.line21
        - guard: {op: test, eq: [sd.line16, {const: 0}]}
          then: sd.zero
  - id: sd.net_gain
    printed: "(helper)"
    label: "Net capital gain for the Qualified Dividends and Capital Gain Tax Worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.h_net_gain_both, {const: true}]}
          then: sd.h_net_gain_amount
        - guard: {op: test, eq: [sd.h_net_gain_both, {const: false}]}
          then: sd.zero
    note: "Chosen reading: the smaller of Schedule D lines 15 and 16 when both are gains, otherwise zero, as in the Qualified Dividends and Capital Gain Tax Worksheet line 3."
  - id: sd.h_line7_loss
    printed: "(helper)"
    label: "Schedule D line 7 if a loss, otherwise zero"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line7, sd.zero]}
  - id: sd.h_line18_raw
    printed: "(helper)"
    label: "28% Rate Gain Worksheet raw amount from Form 1099-DIV box 2d and a Schedule D line 7 loss"
    type: Dollars
    expr:
      op: sum
      of:
        - div.box2d
        - sd.h_line7_loss
  - id: sd.h_line18_floor
    printed: "(helper)"
    label: "28% Rate Gain Worksheet amount floored at zero"
    type: NonNegDollars
    expr: {op: larger_of, of: [sd.h_line18_raw, sd.zero]}
  - id: sd.h_loss_limit
    printed: "(helper)"
    label: "Capital loss limit for the filing status"
    type: Dollars
    expr: {op: param, ref: sd.loss_limit}
  - id: sd.h_line21_loss
    printed: "(helper)"
    label: "Smaller capital loss allowed on line 21, treated as a negative amount"
    type: Dollars
    expr: {op: larger_of, of: [sd.line16, sd.h_loss_limit]}
  - id: sd.h_net_gain_both
    printed: "(helper)"
    label: "Are Schedule D lines 15 and 16 both gains?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [sd.line15, {const: 0}]}
        - {op: test, gt: [sd.line16, {const: 0}]}
  - id: sd.h_net_gain_amount
    printed: "(helper)"
    label: "Smaller of Schedule D lines 15 and 16"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}
```
