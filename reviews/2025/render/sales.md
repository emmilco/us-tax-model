# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 74e3ca5be95249eea928afb4f183ed167d4f45059f34856cfe7cbd82f0730630 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | a01b9dad55ae9373326a25daed5400919aad8e0b5f9d7e71b501603fb67ebb37 |
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

Model: The gate treats only boxes A and D as basis reported to the IRS, although the classification input includes G–L and no refusal excludes them, so boxes G and J get the correct basis. The IRS text says that for "box A or box G" or "box D or box J" you "enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect."

Ruling: scope; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 8, code B. Boxes G to L are refused at the transaction: sales.one refuses when sales.digital ("Form 8949 digital asset boxes G–L"), and the refusal reaches every Schedule D total and Form 1040 line 7a (checked: sales.refuse.digital.G gives sd.line15, f1040.line7a and f1040.line16 refused on sales.digital, while the row's own column (e) shows $2,000.00 and reaches no Schedule D line). Within boxes A to F the gate reads as the instructions do. The gate must widen to G and J if digital assets come into scope. Project stands on the English.

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The reported-minus-correct sign and netting with code W match the worksheet for boxes A and D, but code B gets $0 for boxes G and J, where the IRS says to "Correct the error by entering an adjustment in column (g)" (no refusal is shown). The "other" code also yields $0 with no refusal, although code O says "Enter the appropriate adjustment amount in column (g)."

Ruling: scope; i8949 p. 8, code B; i8949 pp. 7–11, columns (f) and (g). Boxes G and J are refused with every digital-asset box (see column (e)), so the A/D condition of the basis correction is the whole supported case. Codes other than B and W are refused: sales.one refuses when sales.bad_code ("Only applicable B and W adjustments are supported"), and the refusal reaches the Schedule D totals and Form 1040 (checked: sales.refuse.code gives sd.line15, f1040.line7a and f1040.line16 refused on sales.bad_code while the row's own column (g) shows $0.00). Project stands on the English.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: Column (d) minus column (e), plus column (g), follows the form's "Subtract column (e) from column (d) and combine the result with column (g)." The computation itself is correct, and the box G/J errors in (e) and (g) offset here, though an adjustment omitted from (g) under the "other" code would carry through.

## Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The gate treats only boxes A and D as basis reported to the IRS, although the classification input includes G–L and no refusal excludes them, so boxes G and J get the correct basis. The IRS text says that for \"box A or box G\" or \"box D or box J\" you \"enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect.\""
  - key: "(g)"
    status: MISMATCH
    reason: "The reported-minus-correct sign and netting with code W match the worksheet for boxes A and D, but code B gets $0 for boxes G and J, where the IRS says to \"Correct the error by entering an adjustment in column (g)\" (no refusal is shown). The \"other\" code also yields $0 with no refusal, although code O says \"Enter the appropriate adjustment amount in column (g).\""
  - key: "(h)"
    status: MATCH
    reason: "Column (d) minus column (e), plus column (g), follows the form's \"Subtract column (e) from column (d) and combine the result with column (g).\" The computation itself is correct, and the box G/J errors in (e) and (g) offset here, though an adjustment omitted from (g) under the \"other\" code would carry through."
```
```
