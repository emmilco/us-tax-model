# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 84459d5bd38762813b75a5cb37fb671946183027822b0de5bd0e601b379e20be |
| printed lines compared | 5 |
| agree / disagree / missing | 3 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d |

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

Second transcription's note: Box A/D/G/J (basis reported) uses the basis shown on the broker form, even if it is incorrect, with code B correcting it in column (g). Boxes B/E/H/K and C/F/I/L use the correct basis.

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
    label: "Basis reported to IRS (box A, D, G or J)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sales.h_unreported
    printed: "(helper)"
    label: "Not reported on Form 1099-B or Form 1099-DA (box C, F, I or L)"
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
    label: "Code B (incorrect basis shown on Form 1099-B or 1099-DA) applies"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}
  - id: sales.h_has_w
    printed: "(helper)"
    label: "Code W (nondeductible loss from a wash sale) applies"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}
  - id: sales.h_bad_code
    printed: "(helper)"
    label: "Unsupported adjustment code, or code B with no broker statement"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "other"}]}
        - op: test
          all:
            - {op: test, eq: [sales.h_has_b, {const: true}]}
            - {op: test, eq: [sales.h_unreported, {const: true}]}
    note: "Code B covers a basis shown on Form 1099-B or 1099-DA that is incorrect. With box C/F/I/L there is no such form, so I treat code B there as an input error to screen out."
  - id: sales.h_bad_aggregate
    printed: "(helper)"
    label: "Aggregate route fails Exception 1 conditions"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - op: test
          not:
            op: test
            all:
              - {op: test, eq: [sales.h_covered, {const: true}]}
              - {op: test, eq: [sales.code, {const: "none"}]}
              - {op: test, eq: [sales.aggregate_eligible, {const: true}]}
    note: "Exception 1 / Lines 1a and 8a: basis reported to IRS, no adjustments or codes, Ordinary box not checked, no QOF deferral or termination, no collectibles. Only the collectibles exclusion appears in the text, so I rely on sales.aggregate_eligible to cover it. sales.special also includes section 1202 and 1250 property, which the text does not bar from aggregation, so I left sales.special out of this test."
  - id: sales.one
    printed: "(helper)"
    label: "Screen this transaction before any aggregation"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "These atoms have no way to reject a transaction: choose guards must be exhaustive, and there is no error value. So this is the constant 1. The screen is the pair sales.h_bad_code and sales.h_bad_aggregate, which the aggregating form must check."
  - id: sales.zero
    printed: "(helper)"
    label: "No adjustment"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sales.line(e)
    printed: "(e)"
    label: "Cost or other basis. For covered securities, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement); for noncovered securities, enter the correct basis"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_covered, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_covered, {const: false}]}
          then: sales.correct_basis
    note: "Box A/D/G/J (basis reported) uses the basis shown on the broker form, even if it is incorrect, with code B correcting it in column (g). Boxes B/E/H/K and C/F/I/L use the correct basis."
  - id: sales.h_b_difference
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments: line 1 (basis shown on form) minus line 2 (correct basis); positive is line 4, negative is line 3 in parentheses"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
  - id: sales.h_adjust_b
    printed: "(helper)"
    label: "Code B with basis reported to IRS: correct the basis in column (g)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_has_b, {const: true}]}
        - {op: test, eq: [sales.h_covered, {const: true}]}
  - id: sales.h_b
    printed: "(helper)"
    label: "Basis adjustment in column (g); -0- if basis wasn't reported to the IRS"
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
    label: "Code W: amount of the nondeductible wash-sale loss as a positive number in column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_has_w, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_has_w, {const: false}]}
          then: sales.zero
    note: "Uses the correct nondeductible loss (sales.wash_loss), not the broker's box 1g/1i figure, as the code W instruction requires. Any statement explaining a smaller amount is outside this model."
  - id: sales.line(g)
    printed: "(g)"
    label: "Amount of adjustment. If you entered more than one code in column (f), enter the net adjustment in column (g)"
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
```
```
