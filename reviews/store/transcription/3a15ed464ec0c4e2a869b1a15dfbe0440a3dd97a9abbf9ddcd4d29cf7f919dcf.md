# Review record 3a15ed464ec0 — transcription div

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "div",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "complete-input-context-v1",
  "prompt policy": "source-only-computation-v2",
  "type validation policy": "project-expression-types-v1"
 },
 "prompt_sha256": "4bd9b6b65b1a70f6d88bba25152777efc8b49b7cc665c961da2cf3016f850865",
 "response_sha256": "fff3f6b434ea863ad8e6caf43f1fc1558e4b337830613cdfa4134a8e8afaa261",
 "scope": "whole",
 "subjects": {
  "(document)": "42b78e5376ee4a1dfb47c58ddb1d582b614f006924582ead17ed6327920c53fa"
 }
}
```

<!-- part head -->
# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4bd9b6b65b1a70f6d88bba25152777efc8b49b7cc665c961da2cf3016f850865 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 42b78e5376ee4a1dfb47c58ddb1d582b614f006924582ead17ed6327920c53fa |
| printed lines compared | 5 |
| agree / disagree / missing | 4 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

<!-- part raw -->

## Raw second transcription

```yaml
```yaml
lines:
  - id: div.h_zero
    printed: "(helper)"
    label: "Zero (no unsupported nondividend distribution)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: div.h_box3_unhandled
    printed: "(helper)"
    label: "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable. Any amount received in excess of your basis is taxable to you as capital gain. See Pub. 550."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [div.basis_reconciled, {const: true}]}
          then: div.h_zero
        - guard: {op: test, eq: [div.basis_reconciled, {const: false}]}
          then: div.box3
    note: "Box 3 is not taxable up to basis; any excess is capital gain (Pub. 550). The tool handles box 3 only when the filer confirms the basis reductions have been made and no distribution is more than basis. Otherwise the box 3 amount counts in the screen."
  - id: div.screen
    printed: "(helper)"
    label: "Form 1099-DIV amounts outside the computed scope (boxes 2c, 2e, 2f, 9, 10, and box 3 not reconciled to basis)"
    type: NonNegDollars
    expr:
      op: sum
      of: [div.box2c, div.box2e, div.box2f, div.box9, div.box10, div.h_box3_unhandled]
    note: "The IRS pages do not define this result. I read it as the total of the 1099-DIV amounts the tool does not compute; any amount above zero should send the filer elsewhere. The amounts included are: box 2c (the section 1202 exclusion needs a Form 8949 'Q' entry, i1040sd p.8); boxes 2e and 2f (for foreign persons, effectively connected income); boxes 9 and 10 (liquidation distributions, for which no reporting is given); and box 3 not reconciled to basis. Left out: boxes 2b and 2d, because the Unrecaptured Section 1250 Gain and 28% Rate Gain Worksheets (u1250, g28) exist in the catalog; and boxes 12 and 13, because exempt-interest dividends go on line 2a and AMT is screened separately by s2.amt. Box 13 is part of box 12. These choices are open."
```
```

<!-- end -->
