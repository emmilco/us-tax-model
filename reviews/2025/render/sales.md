# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9cddefa4504e6e807aa0421144d999d007d2902fdf09f0f147b1a3385d5f2d12 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | b246a3f7ec08ce50632d0b6ab41e022307103c415f53ec1e4eda4f37cf2fb1aa |
| lines judged | 3 |
| match / mismatch / unclear / missing | 1 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **MISMATCH**

Restated: Choose — [helper "Basis reported to IRS" = true → helper "Basis shown on broker report"] [helper "Basis reported to IRS" = false → helper "Correct adjusted basis from records"]

Model: The gate "Basis reported to IRS" is true only for box A or D, so a box G or J transaction gets the filer's correct basis instead of the broker-reported basis. The IRS says "If this transaction is reported on Part I with box A or box G checked ... or on Part II with box D or box J checked ..., enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect."

Ruling: scope; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 8, code B. The model is right that the instructions treat boxes G and J like A and D, but boxes G to L are refused at the transaction: sales.one refuses when sales.digital ("Form 8949 digital asset boxes G–L"), and the refusal reaches every Schedule D total and Form 1040 line 7a (fixture sales.refuse.digital.G passes on the current tree: sd.line15, f1040.line7a and f1040.line16 refused on sales.digital; the DeepSeek transcription triage's 7 column (e) value differences are all box G or J entries on refused returns, generated 8, 21, 92, 160, 256, 357 and 470). Within boxes A to F the gate reads as the instructions do. The gate must widen to G and J if digital assets come into scope. Unchanged by the income package. Project stands on the English.

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The code B part (reported basis minus correct basis, net with the positive W loss) matches Worksheet lines 3–4 and the W instructions, but it applies only to boxes A and D. For box G or J the IRS says to "Correct the error by entering an adjustment in column (g)", while the program enters $0 for those boxes.

Ruling: scope; i8949 p. 8, code B; i8949 pp. 7–11, columns (f) and (g). Boxes G and J are refused with every digital-asset box (see column (e)), so the A/D condition of the basis correction is the whole supported case; codes other than B and W are refused at sales.one on sales.bad_code (fixture sales.refuse.code passes). The income package's new entry-error gate sales.wash_bad refuses at sales.w, inside column (g), when a code W loss is larger than the loss after the code B correction (i8949 p. 10, code W, "enter the amount of the nondeductible loss as a positive number in column (g)"); the restatement does not show it, but it can only refuse (fixtures sales.refuse.wash_over_loss, sales.adjust.A.W.equal_loss and sales.adjust.D.BW.wash_within_corrected_loss pass). Project stands on the English.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: This computes column (d) minus column (e), plus column (g), as the form says: "Subtract column (e) from column (d) and combine the result with column (g)."

## Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The gate \"Basis reported to IRS\" is true only for box A or D, so a box G or J transaction gets the filer's correct basis instead of the broker-reported basis. The IRS says \"If this transaction is reported on Part I with box A or box G checked ... or on Part II with box D or box J checked ..., enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect.\""
  - key: "(g)"
    status: MISMATCH
    reason: "The code B part (reported basis minus correct basis, net with the positive W loss) matches Worksheet lines 3–4 and the W instructions, but it applies only to boxes A and D. For box G or J the IRS says to \"Correct the error by entering an adjustment in column (g)\", while the program enters $0 for those boxes."
  - key: "(h)"
    status: MATCH
    reason: "This computes column (d) minus column (e), plus column (g), as the form says: \"Subtract column (e) from column (d) and combine the result with column (g).\""
```
```
