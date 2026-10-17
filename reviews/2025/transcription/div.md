# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 27b496f69da3e176bae62d84f29e8b9979803cbeffdc2752e48cb1a69befb714 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 |

## Lines

### div.screen — Zero only after distribution scope checks
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "div.basis_reconciled"}], "test": "eq"}, {"args": [{"input": "div.box3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"input": "div.box10"}, {"const": 0}], "test": "le"}, {"args": [{"input": "div.box2c"}, {"const": 0}], "test": "le"}, {"args": [{"input": "div.box2e"}, {"const": 0}], "test": "le"}, {"args": [{"input": "div.box2f"}, {"const": 0}], "test": "le"}, {"args": [{"input": "div.box9"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": 0}, {"input": "div.box3"}], "test": "lt"}, {"args": [{"const": true}, {"input": "div.basis_reconciled"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"input": "div.box10"}], "test": "lt"}, {"args": [{"const": 0}, {"input": "div.box2c"}], "test": "lt"}, {"args": [{"const": 0}, {"input": "div.box2e"}], "test": "lt"}, {"args": [{"const": 0}, {"input": "div.box2f"}], "test": "lt"}, {"args": [{"const": 0}, {"input": "div.box9"}], "test": "lt"}], "test": "any"}, "then": {"of": [{"input": "div.box10"}, {"input": "div.box2c"}, {"input": "div.box2e"}, {"input": "div.box2f"}, {"input": "div.box3"}, {"input": "div.box9"}], "op": "sum"}}], "op": "choose"}
```

Second transcription's note: The request listed no printed lines to transcribe, so only helper lines are produced. The grammar has no error atom, so a failed screen is shown as a positive amount instead of an error. The guards are exhaustive and disjoint (h_pass is the negation of h_fail).

Ruling: refusal representation; project retained. `div.screen` is a zero-valued line whose `refuses` entries fire the Form 1099-DIV scope refusals (section 1202 gain, AMT interest, unreconciled basis, unsupported boxes); the grammar given to the second transcriber had no refusal construct, so it expressed a failed screen as a positive amount. The screening conditions it encoded are the same ones the project refuses on. The prompt now lacks `refuses`; recorded for the tool, not a data change.

## Raw second transcription

```yaml
```yaml
lines:
  - id: div.h_has2c
    printed: "(helper)"
    label: "Section 1202 gain reported (box 2c is more than zero)"
    type: Bool
    expr: {op: test, gt: [div.box2c, {const: 0}]}
    note: "Box 2c is section 1202 gain from certain small business stock that 'may be subject to an exclusion. See the Schedule D (Form 1040) instructions.' The text here does not explain how the exclusion works, so a positive box 2c fails the screen."
  - id: div.h_has2e
    printed: "(helper)"
    label: "Section 897 ordinary dividends reported (box 2e is more than zero)"
    type: Bool
    expr: {op: test, gt: [div.box2e, {const: 0}]}
    note: "'Boxes 2e and 2f apply only to foreign persons and entities ... It is generally treated as effectively connected to a trade or business within the United States. See the instructions for your tax return.' The text gives no computation, so a positive amount fails the screen."
  - id: div.h_has2f
    printed: "(helper)"
    label: "Section 897 capital gain reported (box 2f is more than zero)"
    type: Bool
    expr: {op: test, gt: [div.box2f, {const: 0}]}
    note: "Same reason as box 2e: the box applies only to foreign persons and entities, and the text gives no computation."
  - id: div.h_has9
    printed: "(helper)"
    label: "Cash liquidation distributions reported (box 9 is more than zero)"
    type: Bool
    expr: {op: test, gt: [div.box9, {const: 0}]}
    note: "The text only says 'Boxes 9 and 10. Show cash and noncash liquidation distributions' and gives no treatment, so I chose to fail the screen."
  - id: div.h_has10
    printed: "(helper)"
    label: "Noncash liquidation distributions reported (box 10 is more than zero)"
    type: Bool
    expr: {op: test, gt: [div.box10, {const: 0}]}
    note: "Same as box 9: the text gives no treatment, so I chose to fail the screen."
  - id: div.h_has3
    printed: "(helper)"
    label: "Nondividend distributions reported (box 3 is more than zero)"
    type: Bool
    expr: {op: test, gt: [div.box3, {const: 0}]}
  - id: div.h_basis_ok
    printed: "(helper)"
    label: "Basis reductions applied and no distribution exceeds basis"
    type: Bool
    expr: {op: test, eq: [div.basis_reconciled, {const: true}]}
  - id: div.h_box3_fail
    printed: "(helper)"
    label: "Box 3: 'To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable. Any amount received in excess of your basis is taxable to you as capital gain.' Fails when not reconciled"
    type: Bool
    expr: {op: test, all: [div.h_has3, {op: test, not: div.h_basis_ok}]}
    note: "Open point: the text does not say how to model the box 3 basis reduction. I chose this: box 3 passes only when the taxpayer confirms that basis has been reduced and no distribution exceeds basis. Any excess would be capital gain, and the text gives no computation for it."
  - id: div.h_fail
    printed: "(helper)"
    label: "Any distribution component outside scope"
    type: Bool
    expr: {op: test, any: [div.h_has2c, div.h_has2e, div.h_has2f, div.h_has9, div.h_has10, div.h_box3_fail]}
    note: "Not counted as failures: box 2b and box 2d (other worksheets use them), box 4 ('Include this amount on your income tax return as tax withheld'), box 6 ('This amount is included in box 1a'), box 12 (reported per the Form 1040 instructions), box 13 (its AMT effect is screened via Form 6251 / s2.amt) and FATCA box 11 ('You may also have a filing requirement. See the Instructions for Form 8938'; reviewed separately according to the div.fatca question). I chose to leave these out because the text gives no instruction that blocks the computation."
  - id: div.h_pass
    printed: "(helper)"
    label: "All distribution scope checks passed"
    type: Bool
    expr: {op: test, not: div.h_fail}
  - id: div.h_unsupported_total
    printed: "(helper)"
    label: "Total of out-of-scope distribution amounts (boxes 2c, 2e, 2f, 3, 9, 10)"
    type: NonNegDollars
    expr: {op: sum, of: [div.box2c, div.box2e, div.box2f, div.box3, div.box9, div.box10]}
    note: "When div.h_fail is true, at least one of these amounts is positive, so this total is more than zero. That makes div.screen nonzero whenever a check fails."
  - id: div.screen
    printed: "(helper)"
    label: "Zero only after distribution scope checks"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: div.h_pass, then: {const: 0}}
        - {guard: div.h_fail, then: div.h_unsupported_total}
    note: "The request listed no printed lines to transcribe, so only helper lines are produced. The grammar has no error atom, so a failed screen is shown as a positive amount instead of an error. The guards are exhaustive and disjoint (h_pass is the negation of h_fail)."
```
```
