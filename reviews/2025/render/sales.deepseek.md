# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 74e3ca5be95249eea928afb4f183ed167d4f45059f34856cfe7cbd82f0730630 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: The restatement's 'Basis reported to IRS' gate is true only for classifications A or D, but the IRS form also treats boxes G and J as 'reported on Form(s) 1099-DA showing basis was reported to the IRS'; for those rows column (e) must use the reported basis, not the records basis.

Ruling: scope; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 8, code B. Boxes G to L are refused at the transaction: sales.one refuses when sales.digital ("Form 8949 digital asset boxes G–L"), and the refusal reaches every Schedule D total and Form 1040 line 7a (checked: sales.refuse.digital.G gives sd.line15, f1040.line7a and f1040.line16 refused on sales.digital, while the row's own column (e) shows $2,000.00 and reaches no Schedule D line). Within boxes A to F the gate reads as the instructions do. The gate must widen to G and J if digital assets come into scope. Project stands on the English.

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: IRS column (g) says 'Enter in this column any necessary adjustments to gain (or loss)' and, for multiple codes, 'enter the net adjustment in column (g)'; the restatement only adds B basis correction and W wash-sale adjustment, omitting other required adjustment codes.

Ruling: scope; i8949 p. 8, code B; i8949 pp. 7–11, columns (f) and (g). Boxes G and J are refused with every digital-asset box (see column (e)), so the A/D condition of the basis correction is the whole supported case. Codes other than B and W are refused: sales.one refuses when sales.bad_code ("Only applicable B and W adjustments are supported"), and the refusal reaches the Schedule D totals and Form 1040 (checked: sales.refuse.code gives sd.line15, f1040.line7a and f1040.line16 refused on sales.bad_code while the row's own column (g) shows $0.00). Project stands on the English.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: Form 8949 column (h) says to subtract column (e) from column (d) and combine the result with column (g); the restatement's proceeds-less-(e) plus column (g) does exactly that.

## Raw response

```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The restatement's 'Basis reported to IRS' gate is true only for classifications A or D, but the IRS form also treats boxes G and J as 'reported on Form(s) 1099-DA showing basis was reported to the IRS'; for those rows column (e) must use the reported basis, not the records basis."
  - key: "(g)"
    status: MISMATCH
    reason: "IRS column (g) says 'Enter in this column any necessary adjustments to gain (or loss)' and, for multiple codes, 'enter the net adjustment in column (g)'; the restatement only adds B basis correction and W wash-sale adjustment, omitting other required adjustment codes."
  - key: "(h)"
    status: MATCH
    reason: "Form 8949 column (h) says to subtract column (e) from column (d) and combine the result with column (g); the restatement's proceeds-less-(e) plus column (g) does exactly that."
```
