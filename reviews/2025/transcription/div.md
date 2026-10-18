# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 06b73cb455a5fe1ce8e40ca79ebd7a6725e968a8d1eafdc6451850bd0be626c7 |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

## Lines

### div.screen — Zero only after distribution scope checks
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| div.screen | div.h_2b_exceeds, div.h_2d_exceeds, div.h_box3_unreconciled, div.h_has10, div.h_has13, div.h_has2c, div.h_has2e, div.h_has2f, div.h_has9 | div.h_2b_exceeds, div.h_2d_exceeds, div.h_box3_unreconciled, div.h_has10, div.h_has13, div.h_has2c, div.h_has2e, div.h_has2f, div.h_has9 |

## Raw second transcription

```yaml
```yaml
lines:
  - id: div.h_has2c
    printed: "(helper)"
    label: "Box 2c section 1202 gain is reported (portion of box 2a that may be eligible for the section 1202 exclusion)"
    type: Bool
    expr: {op: test, gt: [div.box2c, {const: 0}]}
    note: "Open: the 1099-DIV text and the Schedule D instructions say a box 2c gain may need the section 1202 exclusion, entered on Form 8949 with code Q and on line 2 of the 28% Rate Gain Worksheet. Chosen reading: any amount in box 2c stops the tool, which does not figure the exclusion."

  - id: div.h_has2e
    printed: "(helper)"
    label: "Box 2e section 897 ordinary dividends are reported (applies only to foreign persons and entities)"
    type: Bool
    expr: {op: test, gt: [div.box2e, {const: 0}]}

  - id: div.h_has2f
    printed: "(helper)"
    label: "Box 2f section 897 capital gain is reported (applies only to foreign persons and entities)"
    type: Bool
    expr: {op: test, gt: [div.box2f, {const: 0}]}

  - id: div.h_has3
    printed: "(helper)"
    label: "Box 3 nondividend distributions (return of capital) are reported"
    type: Bool
    expr: {op: test, gt: [div.box3, {const: 0}]}

  - id: div.h_not_reconciled
    printed: "(helper)"
    label: "Basis reductions for box 3 have not been applied, or a distribution exceeds basis"
    type: Bool
    expr: {op: test, not: div.basis_reconciled}

  - id: div.h_box3_unreconciled
    printed: "(helper)"
    label: "Box 3: to the extent of your basis the distribution reduces basis and is not taxable; any amount in excess of basis is taxable as capital gain"
    type: Bool
    expr: {op: test, all: [div.h_has3, div.h_not_reconciled]}
    note: "Open: the text makes a box 3 amount taxable only where it exceeds basis, and the tool does not track basis. Chosen reading: a box 3 amount is accepted as nontaxable only when the filer confirms that the basis reductions have been applied and no distribution exceeds basis. Otherwise the tool stops."

  - id: div.h_has9
    printed: "(helper)"
    label: "Box 9 cash liquidation distributions are reported"
    type: Bool
    expr: {op: test, gt: [div.box9, {const: 0}]}

  - id: div.h_has10
    printed: "(helper)"
    label: "Box 10 noncash liquidation distributions are reported"
    type: Bool
    expr: {op: test, gt: [div.box10, {const: 0}]}

  - id: div.h_has13
    printed: "(helper)"
    label: "Box 13 exempt-interest dividends subject to the alternative minimum tax are reported (see the Instructions for Form 6251)"
    type: Bool
    expr: {op: test, gt: [div.box13, {const: 0}]}
    note: "Open: box 13 points the filer to the Form 6251 instructions but does not say whether Form 6251 is required. Chosen reading: any amount in box 13 stops the tool, since it does not review AMT preference items. The separate s2.amt screen covers whether Form 6251 is required."

  - id: div.h_2b_exceeds
    printed: "(helper)"
    label: "Box 2b (portion of the amount in box 2a that is unrecaptured section 1250 gain) exceeds box 2a"
    type: Bool
    expr: {op: test, gt: [div.box2b, sd.distributions]}
    note: "Open: the 1099-DIV text says box 2b is a portion of box 2a. Chosen reading: compare the box 2b total with the box 2a total (sd.distributions) as a consistency check."

  - id: div.h_2d_exceeds
    printed: "(helper)"
    label: "Box 2d (portion of the amount in box 2a that is 28% rate gain from collectibles) exceeds box 2a"
    type: Bool
    expr: {op: test, gt: [div.box2d, sd.distributions]}
    note: "Open: the 1099-DIV text says box 2d is a portion of box 2a. Chosen reading: compare the box 2d total with the box 2a total (sd.distributions) as a consistency check."

  - id: div.screen
    printed: "(helper)"
    label: "Zero only after distribution scope checks"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    refuses: [div.h_has2c, div.h_has2e, div.h_has2f, div.h_box3_unreconciled, div.h_has9, div.h_has10, div.h_has13, div.h_2b_exceeds, div.h_2d_exceeds]
    note: "Open: the 1099-DIV recipient instructions only describe the boxes; they do not list a scope test. Chosen reading: the zero that downstream worksheets copy from this line is produced only when no unsupported distribution component is present. Those components are boxes 2c, 2e, 2f, 9, 10 and 13, and a box 3 amount without confirmed basis reconciliation. Boxes 2b and 2d are used directly elsewhere and are only checked against box 2a."
```
```
