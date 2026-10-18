# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 346fc0a4d564f586c4e878248b517abb0751fae3790f53717c1699f2a0c9eaf0 |
| printed lines compared | 5 |
| agree / disagree / missing | 3 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |

## Lines

### sales.one — Screen this transaction before any aggregation
Status: **AGREE**

### sales.zero — No adjustment
Status: **AGREE**

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, "then": {"input": "sales.correct_basis"}}, {"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.reported_basis"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, "then": {"input": "sales.correct_basis"}}, {"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.reported_basis"}}], "op": "choose"}
```

Second transcription's note: Box A/D/G/J (basis reported to the IRS) uses the reported basis, even if it is wrong, and code B fixes it in (g). Box B/E/H/K and C/F/I/L use the correct basis, and any code B adjustment in (g) is -0-.

Ruling: scope; project retained. The second transcription treats boxes G and J (digital assets, basis reported) like A and D; digital-asset transactions are refused (`sales.digital`, spec 2.2), so within scope the basis rule is the same.

### (g) — Column (g): net adjustments
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}], "op": "sum"}
```

Ruling: scope; project retained. As for column (e): boxes G and J are refused, so the adjustment rule over A and D is the same within scope.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sales.one | sales.h_bad_aggregate, sales.h_bad_code, sales.special | sales.h_bad_aggregate, sales.h_bad_code |
| (h) | sales.h_bad_aggregate, sales.h_bad_code, sales.special | sales.h_bad_aggregate, sales.h_bad_code, sales.special |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sales.h_covered
    printed: "(helper)"
    label: "Basis reported to the IRS (box A, D, G or J checked)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}

  - id: sales.h_no_statement
    printed: "(helper)"
    label: "No Form 1099-B or Form 1099-DA received (box C, F, I or L checked)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "C"}]}
        - {op: test, eq: [sales.box, {const: "F"}]}
        - {op: test, eq: [sales.box, {const: "I"}]}
        - {op: test, eq: [sales.box, {const: "L"}]}

  - id: sales.h_has_b
    printed: "(helper)"
    label: "Code B: the basis shown in box 1e on Form 1099-B or box 1g on Form 1099-DA is incorrect"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_has_w
    printed: "(helper)"
    label: "Code W: you have a nondeductible loss from a wash sale"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_bad_code
    printed: "(helper)"
    label: "Adjustment code not supported, code B with no broker statement, or a wash-sale loss with no code W"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "other"}]}
        - op: test
          all:
            - sales.h_has_b
            - sales.h_no_statement
        - op: test
          all:
            - {op: test, not: sales.h_has_w}
            - {op: test, gt: [sales.wash_loss, {const: 0}]}
    note: >-
      The code B row says it applies when "You received a Form 1099-B or Form 1099-DA ... and the basis
      shown ... is incorrect", so code B with box C/F/I/L (no statement) is refused. For box B/E/H/K, code B
      is supported: the correct basis goes in (e) and -0- in (g). A positive wash-sale loss entered without
      code W is refused as inconsistent, because code W is what puts that loss in (g).

  - id: sales.h_bad_aggregate
    printed: "(helper)"
    label: "Reported directly on Schedule D line 1a/8a but Exception 1 conditions not met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - op: test
          any:
            - {op: test, not: sales.aggregate_eligible}
            - {op: test, not: sales.h_covered}
            - {op: test, ne: [sales.code, {const: "none"}]}
    note: >-
      Exception 1 applies only to transactions where the statement shows basis was reported to the IRS
      (box A/D/G/J) and no adjustments or codes are needed. Any code other than "none" therefore makes the
      aggregate route invalid.

  - id: sales.one
    printed: "(helper)"
    label: "Screen this transaction before any aggregation"
    type: Count
    expr: {op: param, ref: sales.one}
    refuses: [sales.special, sales.h_bad_code, sales.h_bad_aggregate]

  - id: sales.zero
    printed: "(helper)"
    label: "No adjustment"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sales.line(e)
    printed: "(e)"
    label: "Cost or other basis. For covered securities, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e); for noncovered securities, enter the correct basis of the property"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: sales.h_covered
          then: sales.reported_basis
        - guard: {op: test, not: sales.h_covered}
          then: sales.correct_basis
    note: >-
      Box A/D/G/J (basis reported to the IRS) uses the reported basis, even if it is wrong, and code B fixes
      it in (g). Box B/E/H/K and C/F/I/L use the correct basis, and any code B adjustment in (g) is -0-.

  - id: sales.h_b_difference
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g): line 1 (basis shown on Form 1099-B or 1099-DA) minus line 2 (correct cost or other basis)"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
    note: >-
      Worksheet line 4 (positive when line 1 is larger) and line 3 (negative when line 2 is larger) together
      equal line 1 minus line 2, as a signed amount.

  - id: sales.h_adjust_b
    printed: "(helper)"
    label: "Basis was reported to the IRS and is incorrect: correct it by entering an adjustment in column (g)"
    type: Bool
    expr:
      op: test
      all:
        - sales.h_covered
        - sales.h_has_b

  - id: sales.h_b
    printed: "(helper)"
    label: "Code B adjustment in column (g)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: sales.h_adjust_b
          then: sales.h_b_difference
        - guard: {op: test, not: sales.h_adjust_b}
          then: sales.zero

  - id: sales.h_w
    printed: "(helper)"
    label: "Code W: enter the amount of the nondeductible wash-sale loss as a positive number in column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: sales.h_has_w
          then: sales.wash_loss
        - guard: {op: test, not: sales.h_has_w}
          then: sales.zero

  - id: sales.line(g)
    printed: "(g)"
    label: "Amount of adjustment. If you entered more than one code in column (f) on the same row, enter the net adjustment in column (g)"
    type: Dollars
    expr: {op: sum, of: [sales.h_b, sales.h_w]}

  - id: sales.h_before_adjustment
    printed: "(helper)"
    label: "Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)"
    type: Dollars
    expr: {op: subtract, from: sales.proceeds, take: sales.line(e)}

  - id: sales.line(h)
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sales.h_before_adjustment, sales.line(g)]}
    refuses: [sales.special, sales.h_bad_code, sales.h_bad_aggregate]
```
```
