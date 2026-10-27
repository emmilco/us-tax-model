# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | 364583fe6b62713491074b789f6e46022ff830821b46d6d3f25838a8986d674e |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | de2230e55acae1e3544d228f231a9d1f4e23e6bc23be1d46df0c4c2e2891211f |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 5a423f712d7f1e182d4571e370c26c68211a654977d387a8e97b0b39184a8c98 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 11546ec12851651ce0a50b94b569a90a2396846b7f07dd9626ff7f38baf714b3 |
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

Second transcription's note: Box A/D/G/J: enter the basis shown on Form 1099-B or 1099-DA, even if it is incorrect, and correct it in column (g). Box B/E/H/K: enter the correct basis. Box C/F/I/L: enter the basis from records. For box A/D/G/J without code B, the reported basis is taken to be correct; the mismatch check enforces this.

Ruling: scope; f8949 pp.1-2 explicitly extends the reported-basis treatment to digital-asset boxes G/J. Those boxes are outside the supported slice: sales.one refuses sales.digital before transaction aggregation (forms/2025/sales.yaml); other special digital paths stay refused. On supported A-F transactions the two basis/adjustment formulas agree. This does not certify the ungated intermediate quantities for refused digital transactions, and does not expand project scope.

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

Second transcription's note: When more than one code is entered, the net adjustment goes in column (g) (code BW: basis adjustment plus wash sale loss).

Ruling: scope; f8949 pp.1-2 explicitly extends the reported-basis treatment to digital-asset boxes G/J. Those boxes are outside the supported slice: sales.one refuses sales.digital before transaction aggregation (forms/2025/sales.yaml); other special digital paths stay refused. On supported A-F transactions the two basis/adjustment formulas agree. This does not certify the ungated intermediate quantities for refused digital transactions, and does not expand project scope.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (e) | sales.h_bad_aggregate, sales.h_bad_code, sales.h_basis_mismatch, sales.special | sales.h_bad_aggregate, sales.h_bad_code, sales.h_basis_mismatch, sales.special |
| (g) | sales.h_bad_aggregate, sales.h_bad_code, sales.special | sales.h_bad_aggregate, sales.h_bad_code, sales.special |
| (h) | sales.h_bad_aggregate, sales.h_bad_code, sales.h_basis_mismatch, sales.special | sales.h_bad_aggregate, sales.h_bad_code, sales.h_basis_mismatch, sales.special |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sales.one
    printed: "(helper)"
    label: "One (this transaction counted once)"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The IRS pages do not name this result. It is read as the per-entry count of one, used by other forms to count transactions with sum_over. It is taken from the year parameter sales.one."
  - id: sales.zero
    printed: "(helper)"
    label: "-0- (amount entered when no adjustment applies)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "The IRS pages do not name this result. It is read as the -0- amount the instructions enter in column (g) when no adjustment applies (for example, code B for box B/E/H/K, or no wash sale loss). It is taken from the year parameter sales.zero."
  - id: sales.h_covered
    printed: "(helper)"
    label: "Box A, D, G or J: transaction reported on Form 1099-B or 1099-DA showing basis was reported to the IRS"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}
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
    label: "A column (f) code other than B or W applies (not computed by this tool)"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}
  - id: sales.h_bad_aggregate
    printed: "(helper)"
    label: "Reported directly on Schedule D line 1a/8a (Exception 1) without meeting its conditions"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - op: test
          any:
            - {op: test, eq: [sales.aggregate_eligible, {const: false}]}
            - {op: test, ne: [sales.code, {const: "none"}]}
            - {op: test, eq: [sales.h_covered, {const: false}]}
    note: "Exception 1 applies only to transactions showing basis was reported to the IRS, with no adjustments or codes, other than sales of collectibles. A transaction routed to the aggregate totals is refused unless it is in box A/D/G/J, has no code, and the filer confirms the conditions."
  - id: sales.h_basis_mismatch
    printed: "(helper)"
    label: "Basis was reported to the IRS and differs from the correct basis, but code B is not entered"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_covered, {const: true}]}
        - {op: test, eq: [sales.h_has_b, {const: false}]}
        - {op: test, ne: [sales.reported_basis, sales.correct_basis]}
    note: "Consistency check inferred from the code B row: an incorrect reported basis requires code B and a column (g) adjustment."
  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_covered, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_covered, {const: false}]}
          then: sales.correct_basis
    refuses: [sales.special, sales.h_bad_code, sales.h_bad_aggregate, {when: sales.h_basis_mismatch, when_known: true}]
    note: "Box A/D/G/J: enter the basis shown on Form 1099-B or 1099-DA, even if it is incorrect, and correct it in column (g). Box B/E/H/K: enter the correct basis. Box C/F/I/L: enter the basis from records. For box A/D/G/J without code B, the reported basis is taken to be correct; the mismatch check enforces this."
  - id: sales.h_b_difference
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g), lines 3 and 4: line 1 (basis shown on Form 1099-B/1099-DA) minus line 2 (correct basis)"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
    note: "Line 4 (line 1 larger than line 2) is a positive adjustment. Line 3 (line 2 larger than line 1) is entered as a negative number. Both are expressed as the signed difference of line 1 minus line 2."
  - id: sales.h_adjust_b
    printed: "(helper)"
    label: "Code B on a box A, D, G or J transaction (basis adjustment in column (g) required)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_covered, {const: true}]}
        - {op: test, eq: [sales.h_has_b, {const: true}]}
  - id: sales.h_b
    printed: "(helper)"
    label: "Column (g) adjustment for code B"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_adjust_b, {const: true}]}
          then: sales.h_b_difference
        - guard: {op: test, eq: [sales.h_adjust_b, {const: false}]}
          then: sales.zero
    note: "For box B/E/H/K with code B, the correct basis goes in column (e) and -0- in column (g). For box C/F/I/L there is no reported basis, so no code B adjustment applies."
  - id: sales.h_w
    printed: "(helper)"
    label: "Column (g) adjustment for code W: nondeductible wash sale loss as a positive number"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_has_w, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_has_w, {const: false}]}
          then: sales.zero
  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment"
    type: Dollars
    expr: {op: sum, of: [sales.h_b, sales.h_w]}
    refuses: [sales.special, sales.h_bad_code, sales.h_bad_aggregate]
    note: "When more than one code is entered, the net adjustment goes in column (g) (code BW: basis adjustment plus wash sale loss)."
  - id: sales.h_before_adjustment
    printed: "(helper)"
    label: "Subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sales.proceeds, take: sales.e}
  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sales.h_before_adjustment, sales.g]}
    refuses: [sales.special, sales.h_bad_code, sales.h_bad_aggregate]
```
```
