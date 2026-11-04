# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f060738f207fba5a8b02602760fd1393eceab283f4c36c09f35ddf1997ab97bf |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 0b9ec9f65641ab9ee08de46c173cbf25107f1f889dcf640bfe9e63ae434562ff |
| lines judged | 3 |
| match / mismatch / unclear / missing | 1 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 82, 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 82, 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **MISMATCH**

Restated: Choose — [helper "Basis reported to IRS" = true → helper "Basis shown on broker report"] [helper "Basis reported to IRS" = false → helper "Correct adjusted basis from records (for inherited property shown on a Schedule A (Form 8971) as increasing the estate tax, starting from no more than its final estate tax value)"]

Model: The program uses the broker-reported basis only for boxes A and D. For digital-asset boxes G and J it enters the correct basis instead, but the IRS says "If this transaction is reported on Part I with box A or box G checked ... or on Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA ... in column (e), even though that basis is incorrect."

Ruling: scope; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 8, code B. The model is right that the instructions treat boxes G and J like A and D, but boxes G to L are refused at the transaction: sales.one refuses when sales.digital ("Form 8949 digital asset boxes G–L"), and the refusal reaches every Schedule D total and Form 1040 (checked this round: sales.refuse.digital.G refuses Form 1040 lines 7a and 16 on sales[a].digital). Same point as the bklg ruling. The restatement's new Form 8971 wording (BUG-0395) matches i8949 p. 6: "first use an amount that is equal to or less than the final estate tax value listed in Part II, column (h)". Project stands on the English.

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The code B adjustment applies only to boxes A and D, so a box G or J transaction with an incorrect basis gets no column (g) correction, although the IRS says for box A, G, D or J to "Correct the error by entering an adjustment in column (g)." Also, choosing "other" for an additional code gives $0 with no refusal, although the IRS requires the adjustment for codes such as E, H, L and Q (for example "enter the amount of the nondeductible loss as a positive number in column (g)").

Ruling: scope; i8949 p. 8, code B; i8949 pp. 7–11, columns (f) and (g). Boxes G and J are refused with every digital-asset box (see column (e)), so the A/D condition of the basis correction is the whole supported case; codes other than B and W are refused at sales.one on sales.bad_code ("Only applicable B and W adjustments are supported"; checked this round: sales.refuse.code refuses Form 1040 lines 7a and 16 on sales[a].bad_code), so "other" never gives a printed $0 on a completed return. Same point as the bklg ruling. Project stands on the English.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: The program takes column (d) minus column (e), plus column (g). This matches the IRS: "subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d). Then take into account any adjustments in column (g)."

## Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The program uses the broker-reported basis only for boxes A and D. For digital-asset boxes G and J it enters the correct basis instead, but the IRS says \"If this transaction is reported on Part I with box A or box G checked ... or on Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA ... in column (e), even though that basis is incorrect.\""
  - key: "(g)"
    status: MISMATCH
    reason: "The code B adjustment applies only to boxes A and D, so a box G or J transaction with an incorrect basis gets no column (g) correction, although the IRS says for box A, G, D or J to \"Correct the error by entering an adjustment in column (g).\" Also, choosing \"other\" for an additional code gives $0 with no refusal, although the IRS requires the adjustment for codes such as E, H, L and Q (for example \"enter the amount of the nondeductible loss as a positive number in column (g)\")."
  - key: "(h)"
    status: MATCH
    reason: "The program takes column (d) minus column (e), plus column (g). This matches the IRS: \"subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d). Then take into account any adjustments in column (g).\""
```
```
