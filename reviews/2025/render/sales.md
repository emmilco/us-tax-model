# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 234f69a9411e95708df66521082b22cb5fa48aed5bf75242a1487fe9f9b1775b |
| lines judged | 3 |
| match / mismatch / unclear / missing | 1 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d |

## Lines

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **MISMATCH**

Restated: Choose — [helper "Basis reported to IRS" = true → helper "Basis shown on broker report"] [helper "Basis reported to IRS" = false → helper "Correct adjusted basis from records"]

Model: The program treats basis as reported to the IRS only for boxes A and D, so boxes G and J (digital assets with basis reported) get the correct basis instead of the broker's figure. The IRS says 'If this transaction is reported on Part I with box A or box G checked ... or ... Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA ... in column (e), even though that basis is incorrect.'

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The sign of the basis correction (reported minus correct) and the positive wash-sale amount, netted, agree with the worksheet and 'enter the net adjustment in column (g)'. But because the basis correction is gated on boxes A and D only, boxes G and J get no correction, although the IRS says for box A or G and D or J to 'Correct the error by entering an adjustment in column (g)'. The 'other' code also yields $0 with no refusal naming the excluded case.

Ruling: scope; project retained. Boxes G and J are refused with every digital-asset box (see column (e)), so the basis correction's A/D condition is the whole supported case. Adjustment codes other than B and W are refused: `sales.one` refuses when `sales.bad_code` ("Only applicable B and W adjustments are supported"), and the refusal reaches the Schedule D totals through `sd.count`. No change to the data.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: This matches 'Subtract column (e) from column (d) and combine the result with column (g).'

## Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The program treats basis as reported to the IRS only for boxes A and D, so boxes G and J (digital assets with basis reported) get the correct basis instead of the broker's figure. The IRS says 'If this transaction is reported on Part I with box A or box G checked ... or ... Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA ... in column (e), even though that basis is incorrect.'"
  - key: "(g)"
    status: MISMATCH
    reason: "The sign of the basis correction (reported minus correct) and the positive wash-sale amount, netted, agree with the worksheet and 'enter the net adjustment in column (g)'. But because the basis correction is gated on boxes A and D only, boxes G and J get no correction, although the IRS says for box A or G and D or J to 'Correct the error by entering an adjustment in column (g)'. The 'other' code also yields $0 with no refusal naming the excluded case."
  - key: "(h)"
    status: MATCH
    reason: "This matches 'Subtract column (e) from column (d) and combine the result with column (g).'"
```
```
