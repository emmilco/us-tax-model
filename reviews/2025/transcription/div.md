# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d3202a30aad5a68b1d2dd2f9bc4a561b0476fe940bdabfafca2eed1074457a59 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

## Lines

### div.screen — Zero only after distribution scope checks
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "div.box10"}, {"const": 0}], "test": "le"}, {"args": [{"input": "div.box9"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"input": "div.box2e"}, {"const": 0}], "test": "le"}, {"args": [{"input": "div.box2f"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "div.basis_reconciled"}], "test": "eq"}, {"args": [{"input": "div.box3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"input": "div.box13"}, {"const": 0}], "test": "le"}, {"args": [{"input": "div.box2c"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": 0}, {"input": "div.box3"}], "test": "lt"}, {"args": [{"const": true}, {"input": "div.basis_reconciled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "div.box10"}], "test": "lt"}, {"args": [{"const": 0}, {"input": "div.box9"}], "test": "lt"}], "test": "any"}, {"args": [{"args": [{"const": 0}, {"input": "div.box2e"}], "test": "lt"}, {"args": [{"const": 0}, {"input": "div.box2f"}], "test": "lt"}], "test": "any"}, {"args": [{"const": 0}, {"input": "div.box13"}], "test": "lt"}, {"args": [{"const": 0}, {"input": "div.box2c"}], "test": "lt"}], "test": "any"}, "then": {"input": "div.h_unsupported_amount"}}], "op": "choose"}
```

Ruling: refusal representation; project retained. `div.screen` is a zero-valued line whose `refuses` entries fire the Form 1099-DIV scope refusals (section 1202 gain, AMT interest, unreconciled basis, unsupported boxes); the grammar given to the second transcriber had no refusal construct, so it expressed a failed screen as a positive amount. The screening conditions it encoded are the same ones the project refuses on. The prompt now lacks `refuses`; recorded for the tool, not a data change.

## Raw second transcription

```yaml
```yaml
lines:
  - id: div.h_box2c_present
    printed: "(helper)"
    label: "Box 2c shows section 1202 gain that may be eligible for the section 1202 exclusion"
    type: Bool
    expr: {op: test, gt: [div.box2c, {const: 0}]}
    note: "The text sends box 2c gain to Form 8949, Part II with code Q and a negative column (g) exclusion. It also changes the 28% Rate Gain Worksheet, line 2. Neither is modelled here, so any positive box 2c amount fails the screen."
  - id: div.h_box2ef_present
    printed: "(helper)"
    label: "Boxes 2e and 2f apply only to foreign persons and entities"
    type: Bool
    expr: {op: test, any: [{op: test, gt: [div.box2e, {const: 0}]}, {op: test, gt: [div.box2f, {const: 0}]}]}
    note: "The text says boxes 2e and 2f apply only to foreign persons and that the amounts are generally treated as effectively connected income. I read any positive amount as outside scope."
  - id: div.h_box3_unreconciled
    printed: "(helper)"
    label: "Box 3 return of capital: any amount received in excess of your basis is taxable to you as capital gain"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [div.box3, {const: 0}]}, {op: test, not: {op: test, eq: [div.basis_reconciled, {const: true}]}}]}
    note: "Box 3 reduces basis and is not taxable, up to the basis in the stock. Any excess is capital gain, and that gain is not modelled. A positive box 3 passes the screen only when the taxpayer confirms that basis was reduced and no distribution was more than basis."
  - id: div.h_liquidation_present
    printed: "(helper)"
    label: "Boxes 9 and 10. Show cash and noncash liquidation distributions"
    type: Bool
    expr: {op: test, any: [{op: test, gt: [div.box9, {const: 0}]}, {op: test, gt: [div.box10, {const: 0}]}]}
    note: "The text does not say how to report liquidation distributions. Any positive amount in either box fails the screen."
  - id: div.h_box13_present
    printed: "(helper)"
    label: "Box 13. Shows exempt-interest dividends subject to the alternative minimum tax. See the Instructions for Form 6251"
    type: Bool
    expr: {op: test, gt: [div.box13, {const: 0}]}
    note: "Open point: s2.amt may already cover this. I chose to fail the screen on any positive box 13 anyway, because Form 6251 is not modelled. Box 12 alone does not fail the screen, since the text gives it no computation here. Box 6 is already included in box 1a, and box 4 is ordinary withholding, so neither is screened. Box 11 (FATCA) only triggers a separate Form 8938 review and is not screened."
  - id: div.h_unsupported
    printed: "(helper)"
    label: "Any Form 1099-DIV distribution component outside the supported scope"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [div.h_box2c_present, {const: true}]}, {op: test, eq: [div.h_box2ef_present, {const: true}]}, {op: test, eq: [div.h_box3_unreconciled, {const: true}]}, {op: test, eq: [div.h_liquidation_present, {const: true}]}, {op: test, eq: [div.h_box13_present, {const: true}]}]}
  - id: div.h_unsupported_amount
    printed: "(helper)"
    label: "Amount for an unsupported distribution component, which must be figured outside this system"
    type: NonNegDollars
    expr: {op: input, source: "Interview: unsupported Form 1099-DIV component (box 2c, 2e, 2f, unreconciled box 3, box 9, box 10 or box 13); figure separately"}
    note: "The atom set has no 'fail' value. To keep a failed screen from passing as zero, this branch points to an input the interview never fills. The return then stays incomplete until the case is handled."
  - id: div.screen
    printed: "(helper)"
    label: "Zero only after distribution scope checks"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [div.h_unsupported, {const: false}]}, then: {const: 0}}, {guard: {op: test, eq: [div.h_unsupported, {const: true}]}, then: div.h_unsupported_amount}]}
```
```
