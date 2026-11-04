# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 9cddefa4504e6e807aa0421144d999d007d2902fdf09f0f147b1a3385d5f2d12 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | b246a3f7ec08ce50632d0b6ab41e022307103c415f53ec1e4eda4f37cf2fb1aa |
| lines judged | 3 |
| match / mismatch / unclear / missing | 3 / 0 / 0 / 0 |
| verdicts for lines not in the form | sales.adjust_b, sales.b, sales.b_difference, sales.before_adjustment, sales.box, sales.code, sales.correct_basis, sales.covered, sales.has_b, sales.has_w, sales.proceeds, sales.reported_basis, sales.w, sales.wash_bad, sales.wash_loss, sales.wash_over, sales.zero |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **MATCH**

Model: IRS column (e) uses the basis reported to the IRS for reported-basis cases and the correct basis from records when basis was not reported; the restatement chooses between those two.

### (g) — Column (g): net adjustments
Status: **MATCH**

Model: IRS column (g) is the adjustment amount, and with multiple codes the net adjustment is entered; adding the basis and wash-sale adjustments matches that.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: IRS column (h) says to subtract column (e) from column (d) and combine the result with column (g), which is what the restatement does.

## Raw response

```yaml
lines:
  - key: "(e)"
    status: MATCH
    reason: "IRS column (e) uses the basis reported to the IRS for reported-basis cases and the correct basis from records when basis was not reported; the restatement chooses between those two."
  - key: "(g)"
    status: MATCH
    reason: "IRS column (g) is the adjustment amount, and with multiple codes the net adjustment is entered; adding the basis and wash-sale adjustments matches that."
  - key: "(h)"
    status: MATCH
    reason: "IRS column (h) says to subtract column (e) from column (d) and combine the result with column (g), which is what the restatement does."
  - key: "sales.covered"
    status: MISMATCH
    reason: "The IRS treats basis as reported to the IRS for boxes A and G (short-term) and D and J (long-term); the restatement returns true only for A or D and omits G and J."
  - key: "sales.reported_basis"
    status: MATCH
    reason: "This is an input for the basis shown on the broker report, consistent with column (e) for reported basis."
  - key: "sales.correct_basis"
    status: MATCH
    reason: "This is an input for the correct cost or other basis from the filer's records, as used in column (e) when basis was not reported or must be corrected."
  - key: "sales.b"
    status: MATCH
    reason: "For reported basis with code B, the IRS worksheet adjustment is reported basis minus correct basis; otherwise no adjustment is entered."
  - key: "sales.w"
    status: MATCH
    reason: "For code W the IRS requires entering the correct nondeductible wash-sale loss as a positive amount, and -0- if none; the restatement and refusal for an amount exceeding the loss are consistent."
  - key: "sales.before_adjustment"
    status: MATCH
    reason: "This is column (d) proceeds less column (e), which the IRS uses as the first step in column (h)."
  - key: "sales.box"
    status: MATCH
    reason: "The input records the Form 8949 box/classification from the filer's records; the listed short-term, long-term, and digital-asset boxes correspond to the form's categories."
  - key: "sales.adjust_b"
    status: MATCH
    reason: "A code B basis correction in column (g) applies only when basis was reported to the IRS and code B applies, which the restatement states."
  - key: "sales.b_difference"
    status: MATCH
    reason: "The basis-adjustment worksheet computes reported basis minus correct basis, entering a positive or negative column (g) adjustment as appropriate."
  - key: "sales.zero"
    status: MATCH
    reason: "The IRS uses -0-/zero when no adjustment or no nondeductible wash-sale loss applies."
  - key: "sales.has_w"
    status: MATCH
    reason: "Code W applies for code W and also for the combined code BW."
  - key: "sales.wash_loss"
    status: MATCH
    reason: "The input describes the correct nondeductible wash-sale loss as a positive amount, with no more than the loss on the sale."
  - key: "sales.wash_bad"
    status: MATCH
    reason: "Adding the pre-wash gain or loss (including the code B correction) to the entered wash-sale loss and testing whether the result is positive is equivalent to testing whether the entered wash-sale loss exceeds the loss on the sale."
  - key: "sales.proceeds"
    status: MATCH
    reason: "Column (d) is the proceeds shown on the broker report, or net proceeds when there is no report."
  - key: "sales.has_b"
    status: MATCH
    reason: "Code B applies for code B and also for the combined code BW."
  - key: "sales.code"
    status: MATCH
    reason: "The supported choices none, B, W, and BW correspond to no adjustment, basis correction, wash sale, and both; other codes are left to manual/other treatment."
  - key: "sales.wash_over"
    status: MATCH
    reason: "This adds the pre-wash gain or loss (including the code B basis correction) and the entered wash-sale loss, as described."
```
