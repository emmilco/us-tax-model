# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 37b06bb871d19523b31c4ae12b5ca9ddeba0042d87a75971e7e17ad967f313db |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | bfaac0e73b8640fe9cb209f96905d33fc22bf29f3aec472330d0132cda9cc329 |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | ac7a0c9cbb9e635491b2505e7d04cea3381b892402408ddc97f8d49d80a6640b |

## Lines

### div.screen — Zero only after distribution scope checks
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"input": "div.basis_reconciled"}, {"args": [{"const": 0}, {"input": "div.box3"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 0}, {"input": "div.box10"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "div.box2c"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "div.box2e"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "div.box2f"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "div.box9"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": 0}, {"input": "div.box3"}], "test": "ne"}, {"args": [{"input": "div.basis_reconciled"}], "test": "not"}], "test": "all"}, {"args": [{"const": 0}, {"input": "div.box10"}], "test": "ne"}, {"args": [{"const": 0}, {"input": "div.box2c"}], "test": "ne"}, {"args": [{"const": 0}, {"input": "div.box2e"}], "test": "ne"}, {"args": [{"const": 0}, {"input": "div.box2f"}], "test": "ne"}, {"args": [{"const": 0}, {"input": "div.box9"}], "test": "ne"}], "test": "any"}, "then": {"input": "div.h_unsupported"}}], "op": "choose"}
```

Ruling: refusal representation; project retained. `div.screen` is a zero-valued line whose `refuses` entries fire the Form 1099-DIV scope refusals (section 1202 gain, AMT interest, unreconciled basis, unsupported boxes); the grammar given to the second transcriber had no refusal construct, so it expressed a failed screen as a positive amount. The screening conditions it encoded are the same ones the project refuses on. The prompt now lacks `refuses`; recorded for the tool, not a data change.

## Raw second transcription

```yaml
```yaml
lines:
  - id: div.h_box2c_zero
    printed: "(helper)"
    label: "No section 1202 gain in box 2c (box 2c: portion of box 2a that is section 1202 gain from certain small business stock that may be subject to an exclusion)"
    type: Bool
    expr: {op: test, eq: [div.box2c, {const: 0}]}
    note: "Open: the text sends a box 2c gain to a Form 8949 Part II entry with code Q and a negative exclusion in column (g), and possibly to 28% Rate Gain Worksheet line 2. That treatment is not modelled here. Chose: any positive box 2c amount fails the scope screen."
  - id: div.h_box2e_zero
    printed: "(helper)"
    label: "No section 897 ordinary dividends in box 2e (applies only to foreign persons and entities)"
    type: Bool
    expr: {op: test, eq: [div.box2e, {const: 0}]}
  - id: div.h_box2f_zero
    printed: "(helper)"
    label: "No section 897 capital gain in box 2f (applies only to foreign persons and entities)"
    type: Bool
    expr: {op: test, eq: [div.box2f, {const: 0}]}
  - id: div.h_box3_zero
    printed: "(helper)"
    label: "No nondividend distributions (return of capital) in box 3"
    type: Bool
    expr: {op: test, eq: [div.box3, {const: 0}]}
  - id: div.h_box3_ok
    printed: "(helper)"
    label: "Box 3 is zero, or basis reductions have been applied and no distribution exceeds basis (any excess over basis is taxable as capital gain)"
    type: Bool
    expr: {op: test, any: [div.h_box3_zero, div.basis_reconciled]}
  - id: div.h_box9_zero
    printed: "(helper)"
    label: "No cash liquidation distributions in box 9"
    type: Bool
    expr: {op: test, eq: [div.box9, {const: 0}]}
    note: "Open: the text says only that boxes 9 and 10 show liquidation distributions and gives no reporting rule. Chose: treat any positive amount as outside scope."
  - id: div.h_box10_zero
    printed: "(helper)"
    label: "No noncash liquidation distributions in box 10"
    type: Bool
    expr: {op: test, eq: [div.box10, {const: 0}]}
    note: "Open: the text gives no reporting rule for box 10. Chose: treat any positive amount as outside scope."
  - id: div.h_in_scope
    printed: "(helper)"
    label: "All distribution scope checks passed"
    type: Bool
    expr: {op: test, all: [div.h_box2c_zero, div.h_box2e_zero, div.h_box2f_zero, div.h_box3_ok, div.h_box9_zero, div.h_box10_zero]}
    note: "Not screened here: boxes 4, 6 and 12, and the FATCA box. Box 4 is reported as withholding. Box 6 is already included in box 1a. Box 12 is reported per the Form 1040 instructions. The FATCA box only says to review Form 8938 separately. Box 13 (AMT, Form 6251) is also not screened; the AMT question is left to the Schedule 2 screen (s2.amt)."
  - id: div.h_out_of_scope
    printed: "(helper)"
    label: "A distribution scope check failed"
    type: Bool
    expr: {op: test, not: {op: test, eq: [div.h_in_scope, {const: true}]}}
  - id: div.h_unsupported
    printed: "(helper)"
    label: "Distribution outside supported scope; no supported value"
    type: NonNegDollars
    expr: {op: input, source: "Not supported: box 2c, 2e, 2f, 9 or 10 amount, or unreconciled box 3 basis; this line is never supplied, so the return cannot be completed"}
    note: "The grammar has no error atom. Chose: an input that is never supplied, so this line stays unknown and blocks the return."
  - id: div.screen
    printed: "(helper)"
    label: "Zero only after distribution scope checks"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [div.h_in_scope, {const: true}]}
          then: {const: 0}
        - guard: {op: test, eq: [div.h_out_of_scope, {const: true}]}
          then: div.h_unsupported
```
```
