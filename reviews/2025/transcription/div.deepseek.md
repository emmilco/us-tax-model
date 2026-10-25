# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4bd9b6b65b1a70f6d88bba25152777efc8b49b7cc665c961da2cf3016f850865 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 42b78e5376ee4a1dfb47c58ddb1d582b614f006924582ead17ed6327920c53fa |
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
{"of": [{"input": "div.box10"}, {"input": "div.box2b"}, {"input": "div.box2c"}, {"input": "div.box2d"}, {"input": "div.box2e"}, {"input": "div.box2f"}, {"input": "div.box9"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "div.basis_reconciled"}], "test": "eq"}, "then": {"input": "div.box3"}}, {"guard": {"args": [{"const": true}, {"input": "div.basis_reconciled"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"of": [{"input": "div.box12"}, {"input": "div.box13"}], "op": "larger_of"}], "op": "sum"}
```

Second transcription's note: The IRS pages do not define a 'screen' line. I read div.screen as the total of the special distribution components that require treatment outside ordinary dividends and capital gain distributions. Box 3 is included only when the basis-reconciliation input says it has not been established that no distribution exceeds basis, because the instructions say a return of capital is not taxable to the extent of basis. Box 12 is used for exempt-interest dividends and box 13 is not added separately because box 12 already includes it; taking the larger of the two avoids double counting while still flagging box 13.

Ruling: interface gap; f1099div (2025) Instructions for Recipient describes the dividend boxes, but defines no quantity named div.screen. The reply explicitly invents a total of special amounts because the required export has no supplied semantic contract. The project uses this internal adapter as zero after scope checks, including when unsupported Form4797/K-1 amounts are absent; that behavior was not independently inferable from the id/type alone. No whole-tree equivalence or clean model-only error is claimed. BUG-0135/T-064 keeps this source-interface review pending until adapter and source-defined quantities are separated.

## Raw second transcription

```yaml
lines:
  - id: div.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: div.h_box3_screened
    printed: "(helper)"
    label: "Box 3 amount included in the scope screen (zero if basis is reconciled)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [div.basis_reconciled, {const: true}]}
          then: div.h_zero
        - guard: {op: test, eq: [div.basis_reconciled, {const: false}]}
          then: div.box3
  - id: div.h_exempt_screen
    printed: "(helper)"
    label: "Exempt-interest screen amount (box 12, which includes box 13)"
    type: NonNegDollars
    expr: {op: larger_of, of: [div.box12, div.box13]}
  - id: div.screen
    printed: "(helper)"
    label: "Scope screening total of special distribution components"
    type: NonNegDollars
    expr:
      op: sum
      of:
        - div.box2b
        - div.box2c
        - div.box2d
        - div.box2e
        - div.box2f
        - div.h_box3_screened
        - div.box9
        - div.box10
        - div.h_exempt_screen
    note: "The IRS pages do not define a 'screen' line. I read div.screen as the total of the special distribution components that require treatment outside ordinary dividends and capital gain distributions. Box 3 is included only when the basis-reconciliation input says it has not been established that no distribution exceeds basis, because the instructions say a return of capital is not taxable to the extent of basis. Box 12 is used for exempt-interest dividends and box 13 is not added separately because box 12 already includes it; taking the larger of the two avoids double counting while still flagging box 13."
```
