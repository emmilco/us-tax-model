# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f298fe0d3f01a04aa84e72718287578d98ae9e019c81fe9b289922a5e30cf6bc |
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

Second transcription's note: For covered securities enter the basis shown on Form 1099-B/1099-DA even if incorrect (box A/D/G/J). For noncovered (box B/E/H/K) or no statement (box C/F/I/L) enter the correct basis. The text does not separately address box C/F/I/L basis; read as the correct basis from records.

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

Second transcription's note: Code 'other' (any code beyond B/W) is outside what this transcription can compute; it contributes no adjustment here and should be screened out upstream. The aggregate route requires no adjustments; this line is not forced to zero for that route, so eligibility must be enforced elsewhere.

Ruling: scope; project retained. As for column (e): boxes G and J are refused, so the adjustment rule over A and D is the same within scope.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: sales.one
    printed: "(helper)"
    label: "Screen this transaction before any aggregation"
    type: Count
    expr: {op: param, ref: sales.one}

  - id: sales.zero
    printed: "(helper)"
    label: "No adjustment"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sales.h_covered
    printed: "(helper)"
    label: "Basis reported to the IRS (box A, D, G or J)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}
    note: "Boxes A/D/G/J are transactions reported on a statement showing basis was reported to the IRS; B/E/H/K show basis not reported; C/F/I/L have no broker statement. Only A/D/G/J are treated as covered for column (e)."

  - id: sales.line(e)
    printed: "(e)"
    label: "Cost or other basis. See the Note below and see Column (e) in the separate instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_covered, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_covered, {const: false}]}
          then: sales.correct_basis
    note: "For covered securities enter the basis shown on Form 1099-B/1099-DA even if incorrect (box A/D/G/J). For noncovered (box B/E/H/K) or no statement (box C/F/I/L) enter the correct basis. The text does not separately address box C/F/I/L basis; read as the correct basis from records."

  - id: sales.h_has_b
    printed: "(helper)"
    label: "Code B applies (basis shown on Form 1099-B or 1099-DA is incorrect)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_has_w
    printed: "(helper)"
    label: "Code W applies (nondeductible loss from a wash sale)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_adjust_b
    printed: "(helper)"
    label: "Basis was reported to the IRS and is incorrect; correct the error in column (g)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_covered, {const: true}]}
        - {op: test, eq: [sales.h_has_b, {const: true}]}
    note: "With code B on box B/E/H/K the correct basis goes in column (e) and -0- in column (g). Code B on box C/F/I/L is not addressed by the text; treated the same (no column (g) basis adjustment)."

  - id: sales.h_b_difference
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g): line 1 (basis shown on Form 1099-B or 1099-DA) less line 2 (correct basis)"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
    note: "Worksheet line 3 (line 2 larger: negative in column (g)) and line 4 (line 1 larger: positive in column (g)) together equal line 1 minus line 2, signed. If they are equal, the result is zero."

  - id: sales.h_b
    printed: "(helper)"
    label: "Basis adjustment in column (g)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_adjust_b, {const: true}]}
          then: sales.h_b_difference
        - guard: {op: test, eq: [sales.h_adjust_b, {const: false}]}
          then: sales.zero

  - id: sales.h_w
    printed: "(helper)"
    label: "Nondeductible wash sale loss as a positive number in column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_has_w, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_has_w, {const: false}]}
          then: sales.zero

  - id: sales.line(g)
    printed: "(g)"
    label: "Amount of adjustment. If more than one code is entered in column (f), enter the net adjustment"
    type: Dollars
    expr: {op: sum, of: [sales.h_b, sales.h_w]}
    note: "Code 'other' (any code beyond B/W) is outside what this transcription can compute; it contributes no adjustment here and should be screened out upstream. The aggregate route requires no adjustments; this line is not forced to zero for that route, so eligibility must be enforced elsewhere."

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
