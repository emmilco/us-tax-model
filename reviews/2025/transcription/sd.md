# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e57f6fec642de0049e5d24bdf9d2ad03cbf65016f0e260acf62158ccf73dbb17 |
| printed lines compared | 54 |
| agree / disagree / missing | 14 / 40 / 0 |
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
{"alternatives": [{"guard": {"line": "17"}, "then": {"ref": "g28.line7"}}, {"guard": {"args": [{"line": "17"}], "test": "not"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The text says to complete the 28% Rate Gain Worksheet only after 'Yes' on line 17, and line 17 'No' skips lines 18 through 21. Chose g28.line7 when line 17 is true and zero otherwise. The worksheet itself returns zero when it is not required.

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

Second transcription's note: The text says to complete the Unrecaptured Section 1250 Gain Worksheet only after 'Yes' on line 17. Chose u1250.line18 when line 17 is true and zero otherwise.

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

Second transcription's note: Open: the supplied text does not state when Schedule D is required. Chose to require it when any sale is entered or when the special capital-gain distribution components (div.special_total) are positive.

Ruling: equivalent within scope; project retained. The instruction (i1040gi p. 33, line 7a, Exception 1) requires Schedule D when any Form 1099-DIV has an amount in box 2b, 2c or 2d, which the second transcription tests on the raw boxes. The project tests the worksheet results instead; with no sales entered the worksheets have nothing to net against, so a nonzero box 2b or 2d gives a nonzero result, and box 2c is refused (`div.section1202`). When sales are entered Schedule D is required on that ground alone. If carryovers come into scope the netting could zero a worksheet result while a box amount remains, and the test must then move to the raw boxes; this ruling records that.

### sd.zero — No amount on an inapplicable line
Status: **AGREE**

### sd.to1040 — Capital gain or limited capital loss for Form 1040 line 7a
Status: **AGREE**

### sd.net_gain — Nonnegative net capital gain for QDCGT
Status: **DISAGREE**

Project:

```json
{"from": {"of": [{"line": "15"}, {"line": "16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"of": [{"const": 0}, {"of": [{"line": "15"}, {"line": "16"}], "op": "smaller_of"}], "op": "larger_of"}
```

Second transcription's note: If either line is zero or a loss, the smaller of the two is zero or less, so a floor at zero gives the QDCGT line 3 rule.

Ruling: equivalent representation; project retained. The smaller of lines 15 and 16 floored at zero equals the larger of zero and that smaller amount.

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

Second transcription's note: Open: which entries feed line 1a. Chose sales with route 'aggregate' in box A (Form 1099-B) or box G (Form 1099-DA), because the text limits line 1a to short-term transactions with basis reported and no adjustments. sales.bad_aggregate screens whether an entry is eligible.

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

Second transcription's note: Line 1a covers only transactions with no adjustments, so this total should be zero. Chose to sum sales.g anyway so that an unscreened adjustment is not silently dropped.

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

Second transcription's note: Open: whether to filter on route. Only lines 1a and 8a offer an aggregate route, so chose to include every box B/H entry whatever its route; sales.bad_aggregate flags any entry wrongly marked aggregate. Lines 3, 9 and 10 make the same choice.

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

Second transcription's note: Open: which entries feed line 8a. Chose sales with route 'aggregate' in box D (Form 1099-B) or box J (Form 1099-DA), because the text limits line 8a to long-term transactions with basis reported and no adjustments.

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

Second transcription's note: Line 8a covers only transactions with no adjustments, so this total should be zero. Chose to sum sales.g anyway so that an unscreened adjustment is not silently dropped.

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
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "1a(h)"}, {"line": "1b(h)"}, {"line": "2(h)"}, {"line": "3(h)"}, {"line": "4"}, {"line": "5"}, {"line": "6"}], "op": "sum"}
```

Second:

```json
{"from": {"of": [{"line": "1a(h)"}, {"line": "1b(h)"}, {"line": "2(h)"}, {"line": "3(h)"}, {"line": "4"}, {"line": "5"}], "op": "sum"}, "op": "subtract", "take": {"line": "6"}}
```

Ruling: scope; project retained. Line 6 is the short-term capital loss carryover, entered in parentheses; carryovers are refused (`sd.other_forms`), so line 6 is zero and adding or subtracting it agree. The sign convention is open as T-004 for when carryovers come into scope.

### 15 — Combine the amounts for Schedule D line 15
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "10(h)"}, {"line": "11"}, {"line": "12"}, {"line": "13"}, {"line": "14"}, {"line": "8a(h)"}, {"line": "8b(h)"}, {"line": "9(h)"}], "op": "sum"}
```

Second:

```json
{"from": {"of": [{"line": "10(h)"}, {"line": "11"}, {"line": "12"}, {"line": "13"}, {"line": "8a(h)"}, {"line": "8b(h)"}, {"line": "9(h)"}], "op": "sum"}, "op": "subtract", "take": {"line": "14"}}
```

Ruling: scope; project retained. Line 14 is the long-term capital loss carryover, entered in parentheses; carryovers are refused (`sd.other_forms`), so line 14 is zero and adding or subtracting it agree. The sign convention is open as T-004.

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

Second transcription's note: On the form, line 20 is reached only when line 17 is 'Yes'. Chose to compute it in every case; anything that uses it must also check line 17.

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
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — (d) Proceeds (sales price)"
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
    note: "Open: which entries feed line 1a. Chose sales with route 'aggregate' in box A (Form 1099-B) or box G (Form 1099-DA), because the text limits line 1a to short-term transactions with basis reported and no adjustments. sales.bad_aggregate screens whether an entry is eligible."
  - id: sd.line1a(e)
    printed: "1a(e)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — (e) Cost (or other basis)"
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
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — (g) Adjustments to gain or loss"
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
    note: "Line 1a covers only transactions with no adjustments, so this total should be zero. Chose to sum sales.g anyway so that an unscreened adjustment is not silently dropped."
  - id: sd.line1a(h)
    printed: "1a(h)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — (h) Gain or (loss)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — (d) Proceeds (sales price)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — (e) Cost (or other basis)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — (g) Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — (h) Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — (d) Proceeds (sales price)"
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
    note: "Open: whether to filter on route. Only lines 1a and 8a offer an aggregate route, so chose to include every box B/H entry whatever its route; sales.bad_aggregate flags any entry wrongly marked aggregate. Lines 3, 9 and 10 make the same choice."
  - id: sd.line2(e)
    printed: "2(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — (e) Cost (or other basis)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — (g) Adjustments to gain or loss"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — (h) Gain or (loss)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — (d) Proceeds (sales price)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — (e) Cost (or other basis)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — (g) Adjustments to gain or loss"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — (h) Gain or (loss)"
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
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — (d) Proceeds (sales price)"
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
    note: "Open: which entries feed line 8a. Chose sales with route 'aggregate' in box D (Form 1099-B) or box J (Form 1099-DA), because the text limits line 8a to long-term transactions with basis reported and no adjustments."
  - id: sd.line8a(e)
    printed: "8a(e)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — (e) Cost (or other basis)"
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
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — (g) Adjustments to gain or loss"
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
    note: "Line 8a covers only transactions with no adjustments, so this total should be zero. Chose to sum sales.g anyway so that an unscreened adjustment is not silently dropped."
  - id: sd.line8a(h)
    printed: "8a(h)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — (h) Gain or (loss)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — (d) Proceeds (sales price)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — (e) Cost (or other basis)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — (g) Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — (h) Gain or (loss)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — (d) Proceeds (sales price)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — (e) Cost (or other basis)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — (g) Adjustments to gain or loss"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — (h) Gain or (loss)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — (d) Proceeds (sales price)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — (e) Cost (or other basis)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — (g) Adjustments to gain or loss"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — (h) Gain or (loss)"
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
  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero by scope. Returns where sd.other_forms is true are screened out elsewhere; this line does not test for them."
  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero by scope. Returns where sd.other_forms is true (Schedule K-1) are screened out elsewhere."
  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: NonNegDollars
    expr: {op: copy, from: sd.zero}
    note: "The form prints this line in parentheses. Chose to store it as a positive amount that line 7 subtracts. Zero by scope; returns where sd.carryover is true are screened out elsewhere."
  - id: sd.line11
    printed: "11"
    label: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero by scope. Returns where sd.other_forms is true are screened out elsewhere."
  - id: sd.line12
    printed: "12"
    label: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: copy, from: sd.zero}
    note: "Zero by scope. Returns where sd.other_forms is true (Schedule K-1) are screened out elsewhere."
  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: NonNegDollars
    expr: {op: copy, from: sd.zero}
    note: "The form prints this line in parentheses. Chose to store it as a positive amount that line 15 subtracts. Zero by scope; returns where sd.carryover is true are screened out elsewhere."
  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions. See the instructions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions}
  - id: sd.h_short_combined
    printed: "(helper)"
    label: "Lines 1a through 5 in column (h), before the line 6 carryover"
    type: Dollars
    expr: {op: sum, of: [sd.line1a(h), sd.line1b(h), sd.line2(h), sd.line3(h), sd.line4, sd.line5]}
  - id: sd.line7
    printed: "7"
    label: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)"
    type: Dollars
    expr: {op: subtract, from: sd.h_short_combined, take: sd.line6}
  - id: sd.h_long_combined
    printed: "(helper)"
    label: "Lines 8a through 13 in column (h), before the line 14 carryover"
    type: Dollars
    expr: {op: sum, of: [sd.line8a(h), sd.line8b(h), sd.line9(h), sd.line10(h), sd.line11, sd.line12, sd.line13]}
  - id: sd.line15
    printed: "15"
    label: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)"
    type: Dollars
    expr: {op: subtract, from: sd.h_long_combined, take: sd.line14}
  - id: sd.line16
    printed: "16"
    label: "Combine lines 7 and 15 and enter the result"
    type: Dollars
    expr: {op: sum, of: [sd.line7, sd.line15]}
  - id: sd.line17
    printed: "17"
    label: "Are lines 15 and 16 both gains?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [sd.line15, {const: 0}]}
        - {op: test, gt: [sd.line16, {const: 0}]}
  - id: sd.line18
    printed: "(helper)"
    label: "If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: sd.line17, then: g28.line7}
        - {guard: {op: test, not: sd.line17}, then: sd.zero}
    note: "The text says to complete the 28% Rate Gain Worksheet only after 'Yes' on line 17, and line 17 'No' skips lines 18 through 21. Chose g28.line7 when line 17 is true and zero otherwise. The worksheet itself returns zero when it is not required."
  - id: sd.line19
    printed: "(helper)"
    label: "If you are required to complete the Unrecaptured Section 1250 Gain Worksheet (see instructions), enter the amount, if any, from line 18 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: sd.line17, then: u1250.line18}
        - {guard: {op: test, not: sd.line17}, then: sd.zero}
    note: "The text says to complete the Unrecaptured Section 1250 Gain Worksheet only after 'Yes' on line 17. Chose u1250.line18 when line 17 is true and zero otherwise."
  - id: sd.filing4952
    printed: "(helper)"
    label: "Are you filing Form 4952?"
    type: Bool
    expr: {op: copy, from: f4952.required}
    note: "Open: where this answer comes from. Chose Form 4952's own filing-requirement determination (f4952.required) rather than a separate interview question."
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
    note: "On the form, line 20 is reached only when line 17 is 'Yes'. Chose to compute it in every case; anything that uses it must also check line 17."
  - id: sd.h_loss_limit
    printed: "(helper)"
    label: "($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr: {op: param, ref: sd.loss_limit}
  - id: sd.h_limited_loss
    printed: "(helper)"
    label: "Smaller of the loss on line 16 or the loss limit, both treated as positive numbers"
    type: Dollars
    expr: {op: larger_of, of: [sd.line16, sd.h_loss_limit]}
    note: "Both amounts are negative here. Taking the smaller magnitude, as the form's note directs, is the same as taking the larger of the two signed values."
  - id: sd.line21
    printed: "21"
    label: "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of: the loss on line 16; or ($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, lt: [sd.line16, {const: 0}]}, then: sd.h_limited_loss}
        - {guard: {op: test, ge: [sd.line16, {const: 0}]}, then: sd.zero}
    note: "Stored as a signed (negative) amount; zero when line 16 is not a loss and line 21 is skipped."
  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}
  - id: sd.zero
    printed: "(helper)"
    label: "No amount on an inapplicable line"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sd.h_sale_count
    printed: "(helper)"
    label: "Number of entered sales"
    type: Count
    expr: {op: sum_over, collection: sales, field: sales.one}
  - id: sd.filed
    printed: "(helper)"
    label: "Schedule D required for entered sales or special distribution gains"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sd.h_sale_count, {const: 0}]}
        - {op: test, gt: [div.special_total, {const: 0}]}
    note: "Open: the supplied text does not state when Schedule D is required. Chose to require it when any sale is entered or when the special capital-gain distribution components (div.special_total) are positive."
  - id: sd.to1040
    printed: "(helper)"
    label: "Capital gain or limited capital loss for Form 1040 line 7a"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, ge: [sd.line16, {const: 0}]}, then: sd.line16}
        - {guard: {op: test, lt: [sd.line16, {const: 0}]}, then: sd.line21}
    note: "Gain: line 16. Zero: line 16, which equals the -0- the form says to enter. Loss: line 21."
  - id: sd.h_smaller_15_16
    printed: "(helper)"
    label: "Smaller of Schedule D line 15 or line 16"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}
  - id: sd.net_gain
    printed: "(helper)"
    label: "Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-"
    type: NonNegDollars
    expr: {op: larger_of, of: [sd.h_smaller_15_16, sd.zero]}
    note: "If either line is zero or a loss, the smaller of the two is zero or less, so a floor at zero gives the QDCGT line 3 rule."
```
```
