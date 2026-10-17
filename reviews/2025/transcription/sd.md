# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ceed9cca519c117a01642a8504c655dde61ea138b2eecdde72670ef24b13a010 |
| printed lines compared | 46 |
| agree / disagree / missing | 13 / 33 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 |
| i1040sd | 2025; printed date 2025-12-11 | 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

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

Second transcription's note: Open: the text does not name the Form 8949 box for line 1a transactions. Chosen: short-term, basis-reported, no-adjustment transactions are boxes A and G. Line 1a takes those reported by the aggregate route; line 1b takes the rest.

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

Second transcription's note: Open: line 1a covers only transactions with no adjustments, so column (g) should be zero. Chosen: sum sales.g over the same entries, so that any nonzero adjustment stays visible rather than being forced to zero.

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

Second transcription's note: Open: the line 2 filter could also require the detail route. Chosen: no route filter, because the aggregate route applies only to basis-reported transactions and sales.bad_aggregate screens any misuse. Without the route filter, no box B or H entry can drop out of the totals. The same reading applies to lines 3, 9 and 10.

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

Second transcription's note: Open: the box for line 8a is not named. Chosen: boxes D and J, using the aggregate route, mirroring line 1a.

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

Second transcription's note: Open: same as line 1a(g). Line 8a has no adjustments. Chosen: sum sales.g rather than forcing zero.

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

Ruling: equivalent representation; project retained. The project adds a zero term that carries the Form 1099-DIV screening gate (`div.screen`, zero when no refusal applies) to the supplied distributions total; the second transcription uses the total directly. Same value within scope.

### 7 — Combine the amounts for Schedule D line 7
Status: **AGREE**

### 15 — Combine the amounts for Schedule D line 15
Status: **AGREE**

### 16 — Combine the amounts for Schedule D line 16
Status: **AGREE**

### 17 — Are lines 15 and 16 both gains?
Status: **AGREE**

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **AGREE**

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
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments; column (d) Proceeds (sales price)"
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
    note: "Open: the text does not name the Form 8949 box for line 1a transactions. Chosen: short-term, basis-reported, no-adjustment transactions are boxes A and G. Line 1a takes those reported by the aggregate route; line 1b takes the rest."
  - id: sd.line1a(e)
    printed: "1a(e)"
    label: "Line 1a, column (e) Cost (or other basis)"
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
    label: "Line 1a, column (g) Adjustments to gain or loss"
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
    note: "Open: line 1a covers only transactions with no adjustments, so column (g) should be zero. Chosen: sum sales.g over the same entries, so that any nonzero adjustment stays visible rather than being forced to zero."
  - id: sd.line1a(h)
    printed: "1a(h)"
    label: "Line 1a, column (h) Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked; column (d)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked; column (e)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked; column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked; column (h)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked; column (d)"
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
    note: "Open: the line 2 filter could also require the detail route. Chosen: no route filter, because the aggregate route applies only to basis-reported transactions and sales.bad_aggregate screens any misuse. Without the route filter, no box B or H entry can drop out of the totals. The same reading applies to lines 3, 9 and 10."
  - id: sd.line2(e)
    printed: "2(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked; column (e)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked; column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked; column (h)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked; column (d)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked; column (e)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked; column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked; column (h)"
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
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments; column (d)"
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
    note: "Open: the box for line 8a is not named. Chosen: boxes D and J, using the aggregate route, mirroring line 1a."
  - id: sd.line8a(e)
    printed: "8a(e)"
    label: "Line 8a, column (e) Cost (or other basis)"
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
    label: "Line 8a, column (g) Adjustments to gain or loss"
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
    note: "Open: same as line 1a(g). Line 8a has no adjustments. Chosen: sum sales.g rather than forcing zero."
  - id: sd.line8a(h)
    printed: "8a(h)"
    label: "Line 8a, column (h) Gain or (loss)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked; column (d)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked; column (e)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked; column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked; column (h)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked; column (d)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked; column (e)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked; column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked; column (h)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked; column (d)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked; column (e)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked; column (g)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked; column (h)"
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
  - id: sd.h_zero
    printed: "(helper)"
    label: "Zero amount for lines not supported in scope"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sd.h_unsupported
    printed: "(helper)"
    label: "Gains/losses from other forms or Schedule K-1, or a capital loss carryover, are present (outside supported scope)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sd.other_forms, {const: true}]}
        - {op: test, eq: [sd.carryover, {const: true}]}
    note: "Open: these screening questions are not on the IRS form itself. Chosen: when this test is true, the return is out of scope and lines 4, 5, 6, 11, 12 and 14 are not valid as zero. Other forms reference sd.zero, while this transcription names the zero helper sd.h_zero as the instructions require; the two must be reconciled."
  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: copy, from: sd.h_zero}
  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: copy, from: sd.h_zero}
  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: copy, from: sd.h_zero}
    note: "Open: the form prints this line in parentheses. Chosen: store it as a signed amount (a loss is negative), so 'combine' on line 7 is a plain sum. The value is zero in scope."
  - id: sd.line11
    printed: "11"
    label: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: copy, from: sd.h_zero}
  - id: sd.line12
    printed: "12"
    label: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: copy, from: sd.h_zero}
  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: copy, from: sd.h_zero}
    note: "Open: same as line 6. Chosen: store it as a signed amount; the value is zero in scope."
  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions}
  - id: sd.line7
    printed: "7"
    label: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)"
    type: Dollars
    expr:
      op: sum
      of: [sd.line1a(h), sd.line1b(h), sd.line2(h), sd.line3(h), sd.line4, sd.line5, sd.line6]
  - id: sd.line15
    printed: "15"
    label: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)"
    type: Dollars
    expr:
      op: sum
      of: [sd.line8a(h), sd.line8b(h), sd.line9(h), sd.line10(h), sd.line11, sd.line12, sd.line13, sd.line14]
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
    note: "Open: whether 'gain' includes zero. Chosen: a gain means more than zero."
  - id: sd.line20
    printed: "20"
    label: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [g28.line7, {const: 0}]}
        - {op: test, eq: [u1250.line18, {const: 0}]}
        - op: test
          not: {op: test, eq: [f4952.required, {const: true}]}
    note: "Open: Schedule D lines 18 and 19 are not separate lines in this transcription. Chosen: read line 18 from 28% Rate Gain Worksheet line 7 (g28.line7) and line 19 from the Unrecaptured Section 1250 Gain Worksheet line 18 (u1250.line18). 'Not filing Form 4952' is read from f4952.required. The answer is meaningful only when line 17 is Yes."
  - id: sd.h_loss_limit
    printed: "(helper)"
    label: "($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr: {op: param, ref: sd.loss_limit}
  - id: sd.h_limited_loss
    printed: "(helper)"
    label: "Smaller of the loss on line 16 or the loss limit, treating both amounts as positive numbers"
    type: Dollars
    expr: {op: larger_of, of: [sd.line16, sd.h_loss_limit]}
    note: "Open: the form says to take the smaller loss when both are treated as positive. Chosen: with both amounts stored as negative signed values, the smaller loss is the larger signed value, so this line uses larger_of."
  - id: sd.line21
    printed: "21"
    label: "If line 16 is a loss, enter here and on Form 1040, line 7a, the smaller of: the loss on line 16; or ($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [sd.line16, {const: 0}]}
          then: sd.h_limited_loss
        - guard: {op: test, ge: [sd.line16, {const: 0}]}
          then: sd.h_zero
    note: "Open: the form reaches line 21 only when line 16 is a loss. Chosen: when line 16 is zero or a gain, the line is skipped and its value is zero."
  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}
```
```
