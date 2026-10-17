# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4b39da5402e2a0736202f501b123602b3c1aae3f21031c6a8bc5d447c3b73225 |
| printed lines compared | 54 |
| agree / disagree / missing | 16 / 38 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | f265dc3989a82f04fbea0f04cf8495b9b5ff8f18335d395176aa06773cc8072f |
| i1040sd | 2025; printed date 2025-12-11 | 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 12 | ac7a0c9cbb9e635491b2505e7d04cea3381b892402408ddc97f8d49d80a6640b |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### sd.line18 — 28% Rate Gain Worksheet result (supplied subtotal; worksheet deferred to Stage 4)
Status: **DISAGREE**

Project:

```json
{"ref": "g28.line7"}
```

Second:

```json
{"alternatives": [{"guard": {"line": "17"}, "then": {"ref": "g28.line7"}}, {"guard": {"args": [{"line": "17"}], "test": "not"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open point: whether you are 'required to complete' the worksheet depends on conditions (section 1202 exclusions, collectibles) that the stub worksheet does not yet test. I take worksheet line 7 when line 17 is Yes and zero when line 17 is No. A worksheet that does not apply gives zero.

Ruling: equivalent in effect; project retained. The second transcription zeroes line 18 unless line 17 is Yes, as the form skips it; the project copies the 28% Rate Gain Worksheet result unconditionally and uses line 17 in the gate that selects the Schedule D Tax Worksheet (`f1040.gate.sdtw` requires line 17), so the value is read only when line 17 is true. No change to the data.

### sd.line19 — Unrecaptured Section 1250 Gain Worksheet result (supplied subtotal; worksheet deferred to 
Status: **DISAGREE**

Project:

```json
{"ref": "u1250.line18"}
```

Second:

```json
{"alternatives": [{"guard": {"line": "17"}, "then": {"ref": "u1250.line18"}}, {"guard": {"args": [{"line": "17"}], "test": "not"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open point: the 'required to complete' conditions are not modeled yet. I take worksheet line 18 when line 17 is Yes and zero when it is No.

Ruling: equivalent in effect; project retained. As for line 18, with the Unrecaptured Section 1250 Gain Worksheet result.

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
{"args": [{"args": [{"const": 0}, {"of": [{"input": "div.box2b"}, {"input": "div.box2c"}, {"input": "div.box2d"}], "op": "sum"}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "any"}
```

Second transcription's note: The text given does not state when Schedule D is required. The QDCG worksheet suggests that box 2a distributions alone may not require it. I chose: required if any sale is entered or any special distribution component is positive.

Ruling: equivalent within scope; project retained. The instruction (i1040gi p. 33, line 7a, Exception 1) requires Schedule D when any Form 1099-DIV has an amount in box 2b, 2c or 2d, which the second transcription tests on the raw boxes. The project tests the worksheet results instead; with no sales entered the worksheets have nothing to net against, so a nonzero box 2b or 2d gives a nonzero result, and box 2c is refused (`div.section1202`). When sales are entered Schedule D is required on that ground alone. If carryovers come into scope the netting could zero a worksheet result while a box amount remains, and the test must then move to the raw boxes; this ruling records that.

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

Second transcription's note: From the Part III flow: a gain gives line 16, zero gives -0-, and a loss gives line 21.

Ruling: equivalent representation; project retained. The second transcription separates the zero case (enter zero) from the gain case (line 16) and the loss case (line 21); the project's two cases, line 16 when zero or more and line 21 otherwise, give the same value since line 16 is zero in the zero case.

### sd.net_gain — Nonnegative net capital gain for QDCGT
Status: **AGREE**

### 1a(d) — Line 1a, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second transcription's note: The text does not say which box classes go on line 1a. It describes 1a as short-term sales with basis reported and no adjustments, which matches Box A (securities) or Box G (digital assets) entries reported in aggregate. I filtered on route = aggregate and box A or G.

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 1a(e) — Line 1a, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 1a(g) — Line 1a, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second transcription's note: Line 1a covers only sales with no adjustments, so this total should be zero. Aggregate entries with adjustments are caught by sales.bad_aggregate. I summed sales.g anyway rather than hard-coding zero.

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 1a(h) — Line 1a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 2(d) — Line 2, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Second transcription's note: The aggregate route applies only to lines 1a and 8a, so I filtered lines 2, 3, 9 and 10 on box alone. An aggregate entry in one of these boxes is caught by sales.bad_aggregate.

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 2(e) — Line 2, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 2(g) — Line 2, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 2(h) — Line 2, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 3(d) — Line 3, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 3(e) — Line 3, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 3(g) — Line 3, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 3(h) — Line 3, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 8a(d) — Line 8a, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second transcription's note: The long-term basis-reported classes are Box D (securities) and Box J (digital assets). I filtered on route = aggregate and box D or J.

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 8a(e) — Line 8a, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 8a(g) — Line 8a, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second transcription's note: Line 8a covers only sales with no adjustments, so this total should be zero. I summed sales.g anyway rather than hard-coding zero.

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 8a(h) — Line 8a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 9(d) — Line 9, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 9(e) — Line 9, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 9(g) — Line 9, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 9(h) — Line 9, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 10(d) — Line 10, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 10(e) — Line 10, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 10(g) — Line 10, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

### 10(h) — Line 10, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope and a redundant conjunct; project retained. Schedule D (2025) lines 1b, 2, 3, 8b, 9 and 10 read “Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked” and so on through Box F or Box L; lines 1a and 8a take the aggregate route for basis-reported transactions without adjustments. The second transcription includes the digital-asset boxes G–L as printed. The project filters on boxes A–F only because digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the two sums are over the same entries. On lines 2, 3, 9 and 10 the project also requires the detail route; the second transcription omits that conjunct because the aggregate route is permitted only for boxes A and D and any other use is refused by `sales.bad_aggregate`, which makes the project's conjunct redundant rather than wrong. No change to the data; a future stage bringing digital assets into scope must widen these filters, and this ruling records that.

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

Ruling: equivalent representation; project retained. The project adds a zero term that carries the Form 1099-DIV screening gate (`div.screen`) to the supplied distributions total; the second transcription uses the total directly.

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
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"line": "17"}, "then": {"ref": "g28.line7"}}, {"guard": {"args": [{"line": "17"}], "test": "not"}, "then": {"const": 0}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"line": "17"}, "then": {"ref": "u1250.line18"}}, {"guard": {"args": [{"line": "17"}], "test": "not"}, "then": {"const": 0}}], "op": "choose"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: This is reached only when line 17 is Yes. Elsewhere it is evaluated but only means something together with sd.line17.

Ruling: equivalent in effect; project retained. The second transcription tests its line 18, which it zeroes unless line 17 is Yes; the project tests the 28% Rate Gain Worksheet result directly. Line 20 is read only on the Yes path of line 17 (the worksheet selection gate requires line 17), so the tests agree where the line is used. The same reasoning as for sd.line18.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **AGREE**

### 22 — Do you have qualified dividends?
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: sd.line1a(d)
    printed: "1a(d)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments. Column (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
    note: "The text does not say which box classes go on line 1a. It describes 1a as short-term sales with basis reported and no adjustments, which matches Box A (securities) or Box G (digital assets) entries reported in aggregate. I filtered on route = aggregate and box A or G."
  - id: sd.line1a(e)
    printed: "1a(e)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments. Column (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
  - id: sd.line1a(g)
    printed: "1a(g)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments. Column (g) Adjustments"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
    note: "Line 1a covers only sales with no adjustments, so this total should be zero. Aggregate entries with adjustments are caught by sales.bad_aggregate. I summed sales.g anyway rather than hard-coding zero."
  - id: sd.line1a(h)
    printed: "1a(h)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments. Column (h) Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
  - id: sd.line1b(d)
    printed: "1b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked. Column (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
  - id: sd.line1b(e)
    printed: "1b(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked. Column (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
  - id: sd.line1b(g)
    printed: "1b(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked. Column (g) Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
  - id: sd.line1b(h)
    printed: "1b(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked. Column (h) Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
  - id: sd.line2(d)
    printed: "2(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked. Column (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "B"}]}
          - {op: test, eq: [sales.box, {const: "H"}]}
    note: "The aggregate route applies only to lines 1a and 8a, so I filtered lines 2, 3, 9 and 10 on box alone. An aggregate entry in one of these boxes is caught by sales.bad_aggregate."
  - id: sd.line2(e)
    printed: "2(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked. Column (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "B"}]}
          - {op: test, eq: [sales.box, {const: "H"}]}
  - id: sd.line2(g)
    printed: "2(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked. Column (g) Adjustments"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "B"}]}
          - {op: test, eq: [sales.box, {const: "H"}]}
  - id: sd.line2(h)
    printed: "2(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked. Column (h) Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "B"}]}
          - {op: test, eq: [sales.box, {const: "H"}]}
  - id: sd.line3(d)
    printed: "3(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked. Column (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "C"}]}
          - {op: test, eq: [sales.box, {const: "I"}]}
  - id: sd.line3(e)
    printed: "3(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked. Column (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "C"}]}
          - {op: test, eq: [sales.box, {const: "I"}]}
  - id: sd.line3(g)
    printed: "3(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked. Column (g) Adjustments"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "C"}]}
          - {op: test, eq: [sales.box, {const: "I"}]}
  - id: sd.line3(h)
    printed: "3(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked. Column (h) Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "C"}]}
          - {op: test, eq: [sales.box, {const: "I"}]}
  - id: sd.line8a(d)
    printed: "8a(d)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments. Column (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
    note: "The long-term basis-reported classes are Box D (securities) and Box J (digital assets). I filtered on route = aggregate and box D or J."
  - id: sd.line8a(e)
    printed: "8a(e)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments. Column (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sd.line8a(g)
    printed: "8a(g)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments. Column (g) Adjustments"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
    note: "Line 8a covers only sales with no adjustments, so this total should be zero. I summed sales.g anyway rather than hard-coding zero."
  - id: sd.line8a(h)
    printed: "8a(h)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments. Column (h) Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sd.line8b(d)
    printed: "8b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked. Column (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sd.line8b(e)
    printed: "8b(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked. Column (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sd.line8b(g)
    printed: "8b(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked. Column (g) Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sd.line8b(h)
    printed: "8b(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked. Column (h) Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sd.line9(d)
    printed: "9(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked. Column (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "E"}]}
          - {op: test, eq: [sales.box, {const: "K"}]}
  - id: sd.line9(e)
    printed: "9(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked. Column (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "E"}]}
          - {op: test, eq: [sales.box, {const: "K"}]}
  - id: sd.line9(g)
    printed: "9(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked. Column (g) Adjustments"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "E"}]}
          - {op: test, eq: [sales.box, {const: "K"}]}
  - id: sd.line9(h)
    printed: "9(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked. Column (h) Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "E"}]}
          - {op: test, eq: [sales.box, {const: "K"}]}
  - id: sd.line10(d)
    printed: "10(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked. Column (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "F"}]}
          - {op: test, eq: [sales.box, {const: "L"}]}
  - id: sd.line10(e)
    printed: "10(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked. Column (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "F"}]}
          - {op: test, eq: [sales.box, {const: "L"}]}
  - id: sd.line10(g)
    printed: "10(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked. Column (g) Adjustments"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "F"}]}
          - {op: test, eq: [sales.box, {const: "L"}]}
  - id: sd.line10(h)
    printed: "10(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked. Column (h) Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "F"}]}
          - {op: test, eq: [sales.box, {const: "L"}]}
  - id: sd.zero
    printed: "(helper)"
    label: "No amount on an inapplicable line"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "This line is zero only because those sources are out of scope. Returns with sd.other_forms true are screened out elsewhere. One atom cannot both screen and copy, so I copied zero."
  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero because Schedule K-1 amounts are out of scope. Returns with sd.other_forms true are screened out elsewhere."
  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero because carryovers are out of scope. Returns with sd.carryover true are screened out elsewhere. The form shows this amount in parentheses, so I treat it as a signed value (a loss is negative) wherever it is combined."
  - id: sd.line11
    printed: "11"
    label: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero because those sources are out of scope. Returns with sd.other_forms true are screened out elsewhere."
  - id: sd.line12
    printed: "12"
    label: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero because Schedule K-1 amounts are out of scope. Returns with sd.other_forms true are screened out elsewhere."
  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero because carryovers are out of scope. Returns with sd.carryover true are screened out elsewhere. I treat the amount as signed, with a loss negative."
  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions. See the instructions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions}
  - id: sd.line7
    printed: "7"
    label: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)"
    type: Dollars
    expr: {op: sum, of: [sd.line1a(h), sd.line1b(h), sd.line2(h), sd.line3(h), sd.line4, sd.line5, sd.line6]}
    note: "'Combine' could mean add or subtract line 6, which is shown in parentheses. I add it, with line 6 already carried as a negative number."
  - id: sd.line15
    printed: "15"
    label: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)"
    type: Dollars
    expr: {op: sum, of: [sd.line8a(h), sd.line8b(h), sd.line9(h), sd.line10(h), sd.line11, sd.line12, sd.line13, sd.line14]}
    note: "Line 14 is shown in parentheses. I add it, with the amount already carried as a negative number."
  - id: sd.line16
    printed: "16"
    label: "Combine lines 7 and 15 and enter the result"
    type: Dollars
    expr: {op: sum, of: [sd.line7, sd.line15]}
  - id: sd.h_line16_gain
    printed: "(helper)"
    label: "Line 16 is a gain"
    type: Bool
    expr: {op: test, gt: [sd.line16, {const: 0}]}
  - id: sd.h_line16_zero
    printed: "(helper)"
    label: "Line 16 is zero"
    type: Bool
    expr: {op: test, eq: [sd.line16, {const: 0}]}
  - id: sd.h_line16_loss
    printed: "(helper)"
    label: "Line 16 is a loss"
    type: Bool
    expr: {op: test, lt: [sd.line16, {const: 0}]}
  - id: sd.line17
    printed: "17"
    label: "Are lines 15 and 16 both gains?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [sd.line15, {const: 0}]}
        - {op: test, gt: [sd.line16, {const: 0}]}
    note: "Per the printed flow, this question applies only when line 16 is a gain. If line 16 is not a gain, the test is false anyway, so lines 18 through 20 come out zero or false."
  - id: sd.h_not17
    printed: "(helper)"
    label: "Line 17 answered No (lines 18 through 21 skipped)"
    type: Bool
    expr: {op: test, not: sd.line17}
  - id: sd.line18
    printed: "(helper)"
    label: "If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: sd.line17, then: g28.line7}
        - {guard: sd.h_not17, then: sd.zero}
    note: "Open point: whether you are 'required to complete' the worksheet depends on conditions (section 1202 exclusions, collectibles) that the stub worksheet does not yet test. I take worksheet line 7 when line 17 is Yes and zero when line 17 is No. A worksheet that does not apply gives zero."
  - id: sd.line19
    printed: "(helper)"
    label: "If you are required to complete the Unrecaptured Section 1250 Gain Worksheet (see instructions), enter the amount, if any, from line 18 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: sd.line17, then: u1250.line18}
        - {guard: sd.h_not17, then: sd.zero}
    note: "Open point: the 'required to complete' conditions are not modeled yet. I take worksheet line 18 when line 17 is Yes and zero when it is No."
  - id: sd.filing4952
    printed: "(helper)"
    label: "Are you filing Form 4952?"
    type: Bool
    expr: {op: copy, from: f4952.required}
    note: "Schedule D does not say how to answer this. I chose the Form 4952 filing-requirement line over a separate interview question, so the two forms cannot disagree."
  - id: sd.investment_election
    printed: "(helper)"
    label: "Form 4952 line 4g"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line4g}
  - id: sd.line20
    printed: "20"
    label: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sd.line18, {const: 0}]}
        - {op: test, eq: [sd.line19, {const: 0}]}
        - {op: test, not: sd.filing4952}
    note: "This is reached only when line 17 is Yes. Elsewhere it is evaluated but only means something together with sd.line17."
  - id: sd.h_loss_limit
    printed: "(helper)"
    label: "($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr: {op: param, ref: sd.loss_limit}
    note: "The parameter is keyed by filing status, taken from f1040.status. It is stored as a negative amount."
  - id: sd.h_limited_loss
    printed: "(helper)"
    label: "Smaller of the loss on line 16 or the loss limit, treating both amounts as positive numbers"
    type: Dollars
    expr: {op: larger_of, of: [sd.line16, sd.h_loss_limit]}
    note: "'Smaller, treating both as positive numbers' on two negative amounts is the larger signed value."
  - id: sd.h_not_loss
    printed: "(helper)"
    label: "Line 16 is not a loss (line 21 skipped)"
    type: Bool
    expr: {op: test, ge: [sd.line16, {const: 0}]}
  - id: sd.line21
    printed: "21"
    label: "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of: The loss on line 16; or ($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: sd.h_line16_loss, then: sd.h_limited_loss}
        - {guard: sd.h_not_loss, then: sd.zero}
  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}
    note: "Line 22 matters only when lines 17 through 21 are skipped or line 16 is a loss. Line 20 says not to complete it otherwise. I evaluate it every time."
  - id: sd.h_sales_count
    printed: "(helper)"
    label: "Number of securities sales entered"
    type: Count
    expr: {op: sum_over, collection: sales, field: sales.one}
  - id: sd.h_has_sales
    printed: "(helper)"
    label: "Any sales entered"
    type: Bool
    expr: {op: test, gt: [sd.h_sales_count, {const: 0}]}
  - id: sd.h_has_special
    printed: "(helper)"
    label: "Any special capital gain distribution components (boxes 2b, 2c, 2d, 2f)"
    type: Bool
    expr: {op: test, gt: [div.special_total, {const: 0}]}
  - id: sd.filed
    printed: "(helper)"
    label: "Schedule D required for entered sales or special distribution gains"
    type: Bool
    expr:
      op: test
      any: [sd.h_has_sales, sd.h_has_special]
    note: "The text given does not state when Schedule D is required. The QDCG worksheet suggests that box 2a distributions alone may not require it. I chose: required if any sale is entered or any special distribution component is positive."
  - id: sd.h_zero_or_gain
    printed: "(helper)"
    label: "Line 16 is zero"
    type: Bool
    expr: {op: copy, from: sd.h_line16_zero}
  - id: sd.to1040
    printed: "(helper)"
    label: "Capital gain or limited capital loss for Form 1040 line 7a"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: sd.h_line16_gain, then: sd.line16}
        - {guard: sd.h_zero_or_gain, then: sd.zero}
        - {guard: sd.h_line16_loss, then: sd.line21}
    note: "From the Part III flow: a gain gives line 16, zero gives -0-, and a loss gives line 21."
  - id: sd.h_min_15_16
    printed: "(helper)"
    label: "Smaller of Schedule D line 15 or line 16"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}
  - id: sd.net_gain
    printed: "(helper)"
    label: "Nonnegative net capital gain for QDCGT: smaller of line 15 or line 16; if either is blank or a loss, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.h_min_15_16, take: {const: 0}}
    note: "If either line is a loss, the smaller of the two is zero or less, so a floor at zero matches the QDCG line 3 'enter -0-' rule."
```
```
