# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | ffc8b2b0f2ee5db755f7cb620059f054ebfc470afa0ae9ec580c18babc0a6999 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Ruling: open

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

Ruling: open

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (g) | sales.bad_aggregate, sales.bad_code, sales.special | sales.bad_aggregate, sales.bad_code, sales.special |
| (h) | sales.bad_aggregate, sales.bad_code, sales.special | sales.bad_aggregate, sales.bad_code, sales.special |

## Raw second transcription

```yaml
lines:
  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: sales.covered
          then: sales.reported_basis
        - guard:
            op: test
            not: sales.covered
          then: sales.correct_basis
  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment"
    type: Dollars
    refuses: [sales.bad_code, sales.bad_aggregate, sales.special]
    expr:
      op: sum
      of: [sales.b, sales.w]
  - id: sales.h
    printed: "(h)"
    label: "Gain (or loss)"
    type: Dollars
    expr:
      op: sum
      of: [sales.before_adjustment, sales.g]
  - id: sales.one
    printed: "(helper)"
    label: "One"
    type: Count
    expr:
      op: param
      ref: sales.one
  - id: sales.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
  - id: sales.covered
    printed: "(helper)"
    label: "Basis was reported to the IRS"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [sales.box, {const: "A"}]
        - op: test
          eq: [sales.box, {const: "D"}]
        - op: test
          eq: [sales.box, {const: "G"}]
        - op: test
          eq: [sales.box, {const: "J"}]
  - id: sales.has_b
    printed: "(helper)"
    label: "Adjustment code includes B"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [sales.code, {const: "B"}]
        - op: test
          eq: [sales.code, {const: "BW"}]
  - id: sales.has_w
    printed: "(helper)"
    label: "Adjustment code includes W"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [sales.code, {const: "W"}]
        - op: test
          eq: [sales.code, {const: "BW"}]
  - id: sales.bad_code
    printed: "(helper)"
    label: "Adjustment code is other"
    type: Bool
    expr:
      op: test
      eq: [sales.code, {const: "other"}]
  - id: sales.bad_aggregate
    printed: "(helper)"
    label: "Aggregate route chosen without all aggregate conditions"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [sales.route, {const: "aggregate"}]
        - op: test
          not: sales.aggregate_eligible
  - id: sales.b_difference
    printed: "(helper)"
    label: "Reported basis minus correct basis"
    type: Dollars
    expr:
      op: subtract
      from: sales.reported_basis
      take: sales.correct_basis
  - id: sales.adjust_b
    printed: "(helper)"
    label: "Basis adjustment applies"
    type: Bool
    expr:
      op: test
      all:
        - sales.covered
        - sales.has_b
  - id: sales.b
    printed: "(helper)"
    label: "Basis adjustment amount"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: sales.adjust_b
          then: sales.b_difference
        - guard:
            op: test
            not: sales.adjust_b
          then: sales.zero
  - id: sales.w
    printed: "(helper)"
    label: "Wash sale adjustment amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: sales.has_w
          then: sales.wash_loss
        - guard:
            op: test
            not: sales.has_w
          then: sales.zero
  - id: sales.before_adjustment
    printed: "(helper)"
    label: "Proceeds minus basis"
    type: Dollars
    expr:
      op: subtract
      from: sales.proceeds
      take: sales.e
```
