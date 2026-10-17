# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 52fcec313b912a306525806a211cdc13937f210340d190810eb19cf434ced46d |
| lines judged | 3 |
| match / mismatch / unclear / missing | 1 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |

## Lines

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **MISMATCH**

Restated: Choose — [helper "Basis reported to IRS" = true → helper "Basis shown on broker report"] [helper "Basis reported to IRS" = false → helper "Correct adjusted basis from records"]

Model: The gate "Basis reported to IRS" is true only for boxes A and D, but the box input also accepts G–L, and no refusal excludes them. For boxes G and J the program enters the correct basis from records, while the IRS says "If this transaction is reported on Part I with box A or box G checked ... or ... Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect."

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: Within boxes A and D the basis correction (reported minus correct) matches the worksheet, and the wash-sale amount matches 'enter the correct amount of the nondeductible loss as a positive number in column (g)'. But for boxes G and J with code B the program enters no basis correction, while the IRS says 'Correct the error by entering an adjustment in column (g)' using the Worksheet for Basis Adjustments. Also, code 'other' yields no adjustment and no refusal, though the IRS requires adjustments for other codes (e.g., E, L).

Ruling: scope; project retained. Boxes G and J are refused with every digital-asset box (see column (e)), so the basis correction's A/D condition is the whole supported case. Adjustment codes other than B and W are refused: `sales.one` refuses when `sales.bad_code` ("Only applicable B and W adjustments are supported"), and the refusal reaches the Schedule D totals through `sd.count`. No change to the data.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: The IRS says 'Subtract column (e) from column (d) and combine the result with column (g)'. The restatement computes (d) − (e) plus (g); any errors come from columns (e) and (g), not from this line's formula.

## Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The gate \"Basis reported to IRS\" is true only for boxes A and D, but the box input also accepts G–L, and no refusal excludes them. For boxes G and J the program enters the correct basis from records, while the IRS says \"If this transaction is reported on Part I with box A or box G checked ... or ... Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect.\""
  - key: "(g)"
    status: MISMATCH
    reason: "Within boxes A and D the basis correction (reported minus correct) matches the worksheet, and the wash-sale amount matches 'enter the correct amount of the nondeductible loss as a positive number in column (g)'. But for boxes G and J with code B the program enters no basis correction, while the IRS says 'Correct the error by entering an adjustment in column (g)' using the Worksheet for Basis Adjustments. Also, code 'other' yields no adjustment and no refusal, though the IRS requires adjustments for other codes (e.g., E, L)."
  - key: "(h)"
    status: MATCH
    reason: "The IRS says 'Subtract column (e) from column (d) and combine the result with column (g)'. The restatement computes (d) − (e) plus (g); any errors come from columns (e) and (g), not from this line's formula."
```
```
