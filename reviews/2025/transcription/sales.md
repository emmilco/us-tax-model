# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f945808b07423f54f78a0bfad82f7aa566ea62946a1faf4b6cafc90c34a6c027 |
| printed lines compared | 5 |
| agree / disagree / missing | 3 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | 7fca69da50288287e68c08bd90231a46194bd409c9f01f797573fd41f1ce0d2e |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 12 | ac7a0c9cbb9e635491b2505e7d04cea3381b892402408ddc97f8d49d80a6640b |
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

Second transcription's note: Boxes B, E, H and K: the basis shown was not reported to the IRS, so the correct basis goes in column (e) with -0- in column (g). Boxes C, F, I and L: there is no statement, so the correct basis is used.

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
    note: "The IRS text ties 'basis was reported to the IRS' to boxes A, D, G and J. Boxes B, E, H and K (basis not reported) and C, F, I and L (no Form 1099-B or 1099-DA) are treated as not covered."

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
    label: "Code B in column (f): basis shown on Form 1099-B or 1099-DA is incorrect"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_has_w
    printed: "(helper)"
    label: "Code W in column (f): nondeductible loss from a wash sale"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_bad_code
    printed: "(helper)"
    label: "Unsupported adjustment code, or code B with no Form 1099-B or 1099-DA basis to correct"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "other"}]}
        - {op: test, all: [sales.h_has_b, sales.h_no_statement]}
    note: "Code B presupposes a basis shown on a broker statement. Boxes C, F, I and L have no such statement, so I flagged code B with those boxes as unsupported. All other codes (C, D, E, H, L, M, N, O, P, Q, R, S, T, X, Y, Z) fall under 'other' and are unsupported."

  - id: sales.h_bad_aggregate
    printed: "(helper)"
    label: "Exception 1 (direct entry on Schedule D line 1a or 8a) chosen but its conditions are not met"
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
            - sales.special
    note: "Exception 1 requires all of the following: basis reported to the IRS, no adjustments, no Ordinary box, no QOF election or termination, and not a sale of collectibles. The 'special' flag covers collectibles together with section 1202 and section 1250 property. I conservatively excluded all three from the aggregate route."

  - id: sales.h_unsupported
    printed: "(helper)"
    label: "Transaction fails screening (unsupported code, invalid aggregate route, or special property)"
    type: Bool
    expr:
      op: test
      any:
        - sales.h_bad_code
        - sales.h_bad_aggregate
        - sales.special
    note: "Collectibles require code C. Section 1202 and 1250 items involve worksheets outside this transcription. All are treated as out of scope."

  - id: sales.one
    printed: "(helper)"
    label: "Screen this transaction before any aggregation"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The atom set has no failure atom, so this line cannot block the return itself. Screening is expressed in sales.h_unsupported, and the host is expected to reject any entry where that line is true. The line still counts one per transaction."

  - id: sales.zero
    printed: "(helper)"
    label: "No adjustment"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sales.line(e)
    printed: "(e)"
    label: "Cost or other basis. For covered securities, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement), even if incorrect; for noncovered securities, enter the correct basis"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: sales.h_covered, then: sales.reported_basis}
        - {guard: {op: test, not: sales.h_covered}, then: sales.correct_basis}
    note: "Boxes B, E, H and K: the basis shown was not reported to the IRS, so the correct basis goes in column (e) with -0- in column (g). Boxes C, F, I and L: there is no statement, so the correct basis is used."

  - id: sales.h_b_difference
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g), lines 3–4: basis shown on Form 1099-B or 1099-DA (line 1) minus correct basis (line 2); positive if line 1 is larger, negative if line 2 is larger"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
    note: "Worksheet lines 3 and 4 are combined into one signed difference. If line 1 equals line 2, neither line applies and the result is zero."

  - id: sales.h_adjust_b
    printed: "(helper)"
    label: "Code B with box A, D, G or J: correct reported basis by an adjustment in column (g)"
    type: Bool
    expr:
      op: test
      all:
        - sales.h_has_b
        - sales.h_covered

  - id: sales.h_b
    printed: "(helper)"
    label: "Basis correction included in column (g)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: sales.h_adjust_b, then: sales.h_b_difference}
        - {guard: {op: test, not: sales.h_adjust_b}, then: sales.zero}

  - id: sales.h_w
    printed: "(helper)"
    label: "Code W: correct nondeductible wash-sale loss as a positive number in column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: sales.h_has_w, then: sales.wash_loss}
        - {guard: {op: test, not: sales.h_has_w}, then: sales.zero}

  - id: sales.line(g)
    printed: "(g)"
    label: "Amount of adjustment. If more than one code is entered in column (f), enter the net adjustment"
    type: Dollars
    expr: {op: sum, of: [sales.h_b, sales.h_w]}

  - id: sales.h_before_adjustment
    printed: "(helper)"
    label: "Subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sales.proceeds, take: sales.line(e)}

  - id: sales.line(h)
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sales.h_before_adjustment, sales.line(g)]}
```
```
