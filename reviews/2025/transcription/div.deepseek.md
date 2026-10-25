# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 2a3735fb20954c22b57c2de1a518f4cc5accce904a25ba8aada58facb4f0d01e |
| prompt policy | source-only-computation-v2 |
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
{"of": [{"input": "div.box10"}, {"input": "div.box12"}, {"input": "div.box13"}, {"input": "div.box2b"}, {"input": "div.box2c"}, {"input": "div.box2d"}, {"input": "div.box2e"}, {"input": "div.box2f"}, {"input": "div.box3"}, {"input": "div.box9"}], "op": "sum"}
```

Second transcription's note: The IRS Form 1099-DIV pages do not define a 'screen' line. I read the project interface as the total of the supplied distribution components that require scope screening; box 3 is accepted only when div.basis_reconciled is true.

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| div.screen | div.h_basis_bad | div.h_basis_bad |

## Raw second transcription

```yaml
lines:
  - id: div.screen
    printed: "(helper)"
    label: "Total of Form 1099-DIV distribution components in boxes 2b, 2c, 2d, 2e, 2f, 3, 9, 10, 12 and 13"
    type: NonNegDollars
    expr:
      op: sum
      of:
        - div.box2b
        - div.box2c
        - div.box2d
        - div.box2e
        - div.box2f
        - div.box3
        - div.box9
        - div.box10
        - div.box12
        - div.box13
    refuses:
      - div.h_basis_bad
    note: "The IRS Form 1099-DIV pages do not define a 'screen' line. I read the project interface as the total of the supplied distribution components that require scope screening; box 3 is accepted only when div.basis_reconciled is true."
  - id: div.h_basis_bad
    printed: "(helper)"
    label: "Box 3 basis has not been reconciled with no distribution exceeding basis"
    type: Bool
    expr: {op: test, eq: [div.basis_reconciled, {const: false}]}
```
