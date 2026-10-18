# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5af084543fbe96e13bea5f4b81a8c545d4001fcf1d3c0cdd792330088007609d |
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
| div.screen | div.h_box13_exceeds_box12, div.h_box2c_present, div.h_box2ef_present, div.h_box3_unreconciled, div.h_liquidation_present | div.h_box13_exceeds_box12, div.h_box2c_present, div.h_box2ef_present, div.h_box3_unreconciled, div.h_liquidation_present |

## Raw second transcription

```yaml
lines:
  - id: div.h_box2c_present
    printed: "(helper)"
    label: "Box 2c. Shows the portion of the amount in box 2a that is section 1202 gain from certain small business stock that may be subject to an exclusion."
    type: Bool
    expr: {op: test, gt: [div.box2c, {const: 0}]}
    note: "Open: the text says box 2c gain 'may be eligible' for the section 1202 exclusion. Claiming it means a Form 8949 Part II entry with code Q and the excluded gain in column (g), plus an entry on line 2 of the 28% Rate Gain Worksheet. The sales adjustment codes have no Q. Chosen reading: any positive box 2c amount is out of scope, and div.screen refuses it. The tool does not assume no exclusion."
  - id: div.h_box2ef_present
    printed: "(helper)"
    label: "Boxes 2e and 2f apply only to foreign persons and entities whose income maintains its character when passed through or distributed to its direct or indirect foreign owners or beneficiaries."
    type: Bool
    expr: {op: test, any: [{op: test, gt: [div.box2e, {const: 0}]}, {op: test, gt: [div.box2f, {const: 0}]}]}
    note: "The text says boxes 2e and 2f apply only to foreign persons and refers to the instructions for that return. Chosen reading: any positive amount in either box is out of scope."
  - id: div.h_liquidation_present
    printed: "(helper)"
    label: "Boxes 9 and 10. Show cash and noncash liquidation distributions."
    type: Bool
    expr: {op: test, any: [{op: test, gt: [div.box9, {const: 0}]}, {op: test, gt: [div.box10, {const: 0}]}]}
    note: "The text gives no reporting rule for liquidation distributions. Chosen reading: any positive amount in box 9 or box 10 is out of scope. The tool does not treat it as zero."
  - id: div.h_box3_unreconciled
    printed: "(helper)"
    label: "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable. Any amount received in excess of your basis is taxable to you as capital gain."
    type: Bool
    expr: {op: test, all: [{op: test, gt: [div.box3, {const: 0}]}, {op: test, eq: [div.basis_reconciled, {const: false}]}]}
    note: "A box 3 amount is supported only when the filer confirms that the basis reductions have been applied and no distribution exceeded basis. That makes the distribution wholly nontaxable. Gain above basis is out of scope."
  - id: div.h_box13_exceeds_box12
    printed: "(helper)"
    label: "Box 13. Shows exempt-interest dividends subject to the alternative minimum tax. This amount is included in box 12."
    type: Bool
    expr: {op: test, gt: [div.box13, div.box12]}
    note: "Consistency check: the text says box 13 is included in box 12, so box 13 cannot be more than box 12. The text sends box 13 to the Form 6251 instructions; that is left to the s2.amt screen. A box 13 amount alone does not refuse here."
  - id: div.screen
    printed: "(helper)"
    label: "Zero only after distribution scope checks"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    refuses: [div.h_box2c_present, div.h_box2ef_present, div.h_liquidation_present, div.h_box3_unreconciled, div.h_box13_exceeds_box12]
    note: "No printed lines were listed for this form, so this is the only required line. It is zero once none of the refusing conditions holds. Boxes 2b and 2d need no refusal here because they feed the Unrecaptured Section 1250 Gain Worksheet and the 28% Rate Gain Worksheet."
```
