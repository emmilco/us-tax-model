# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 52fcec313b912a306525806a211cdc13937f210340d190810eb19cf434ced46d |
| subject sha256 | 913d7bd7361f8781fad6e9e34c411bbe6bd93d16fba1df2a3150b2913c23e7f2 |
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

Model: The gate "Basis reported to IRS" is true only for boxes A and D, yet the classification enum includes digital-asset boxes G–L. For boxes G and J the program enters the correct basis instead of the reported basis. The IRS says "If this transaction is reported on Part I with box A or box G checked ... or on Part II with box D or box J checked ..., enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect."

Ruling: refusal located elsewhere; project retained. Boxes G to L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital ('Form 8949 digital asset boxes G-L'; f8949 Parts I and II), and the refusal reaches every Schedule D total and Form 1040 line 7a (checked: a box G sale gives sd.line15 and f1040.line16 refused on sales.digital). Within boxes A to F the gate reads as the instructions do. The row's own column (e) is still figured (box G gives the correct basis); it reaches no Schedule D line. The gate must widen to G and J when digital assets come into scope. No change to the data.

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The basis-correction adjustment is limited to boxes A and D, so a box G or J transaction with code B gets $0, where the IRS says to "Correct the error by entering an adjustment in column (g)" from the Worksheet for Basis Adjustments. The sign of the adjustment (reported minus correct) and the W amount ("enter the correct amount of the nondeductible loss as a positive number") match. However, a code entered as "other" adds no amount and no refusal is listed, although the IRS says to "enter the net adjustment in column (g)" for all codes.

Ruling: refusal located elsewhere; project retained. Boxes G and J are refused with every digital-asset box (see column (e)), so the basis correction's A/D condition is the whole supported case; a code entered as 'other' is refused by sales.bad_code at sales.one ('Only applicable B and W adjustments are supported'), and that refusal reaches every Schedule D total (checked: code other gives sd.line15 refused on sales.bad_code). The row's own column (g) is still figured and reaches no Schedule D line. No change to the data.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: Proceeds minus column (e), plus column (g), follows "Subtract column (e) from column (d) and combine the result with column (g)."

## Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The gate \"Basis reported to IRS\" is true only for boxes A and D, yet the classification enum includes digital-asset boxes G–L. For boxes G and J the program enters the correct basis instead of the reported basis. The IRS says \"If this transaction is reported on Part I with box A or box G checked ... or on Part II with box D or box J checked ..., enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect.\""
  - key: "(g)"
    status: MISMATCH
    reason: "The basis-correction adjustment is limited to boxes A and D, so a box G or J transaction with code B gets $0, where the IRS says to \"Correct the error by entering an adjustment in column (g)\" from the Worksheet for Basis Adjustments. The sign of the adjustment (reported minus correct) and the W amount (\"enter the correct amount of the nondeductible loss as a positive number\") match. However, a code entered as \"other\" adds no amount and no refusal is listed, although the IRS says to \"enter the net adjustment in column (g)\" for all codes."
  - key: "(h)"
    status: MATCH
    reason: "Proceeds minus column (e), plus column (g), follows \"Subtract column (e) from column (d) and combine the result with column (g).\""
```
```
