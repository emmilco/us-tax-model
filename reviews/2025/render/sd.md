# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | afc0704a53be3bdc9f34ee222cd9f088068dab73426fed6106b68396fdb86baf |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | f619efc423f49555bc3e17271d712b89acae98dd68a232f99eded47d589fafac |
| lines judged | 46 |
| match / mismatch / unclear / missing | 46 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 8, 10, 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| f4952 | 2025; created 2025-05-28 | 1, 2, 3, 4 | whole document | efbeec4c44a1e43fb00231942c811a454d86b3632a2a662238893f8c4595bf81 | 3, 4 | c98eb27a83a89faecfdd0cd6597e8063fbd86a14ba1606f3e96c1c5f016d2b5c |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### 1a(d) — Line 1a, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box A transactions reported on line 1a: basis reported to the IRS and no adjustments. Line 1a is for short-term Form 1099-B/1099-DA transactions 'for which basis was reported to the IRS and for which you have no adjustments'. Digital assets and failed eligibility are refused.

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: For Box A, column (e) is the basis shown on the broker report. That matches 'enter the basis shown on Form 1099-B' for covered securities.

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Aggregate-route entries must have code 'none', so column (g) is zero. That matches line 1a's 'no adjustments' requirement.

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Sums (d) minus (e) plus (g) over the line 1a transactions. That matches 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)'.

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box A transactions reported on Form 8949 for line 1b ('Box A or Box G checked'). Box G digital assets are refused.

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: For Box A, column (e) is the reported basis even when it is incorrect. That matches 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect'.

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Column (g) is reported basis minus correct basis (the Worksheet for Basis Adjustments, lines 3/4) plus the positive wash-sale loss (code W). Other codes are refused.

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Sums (d) minus (e) combined with (g), as the column (h) instructions say.

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box B transactions for line 2 ('Box B or Box H checked'). Box H is refused as a digital asset.

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: For Box B, column (e) is the correct basis from records. That matches 'For noncovered securities, enter the correct basis of the property in column (e)', with -0- in column (g) for code B.

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: The basis correction applies only to covered boxes, so only the wash-sale adjustment remains for Box B. That matches 'enter the correct basis in column (e), and enter -0- in column (g)' for code B on Box B.

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Sums (d) minus (e) combined with (g), as the column (h) instructions say.

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Sums net proceeds of Box C transactions for line 3. That matches 'enter in column (d) the net proceeds' when no Form 1099-B was received. Box I is refused.

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: For Box C, column (e) is the correct basis from records. Code B on Box C is refused.

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Only the wash-sale adjustment applies, entered as a positive amount per code W. Other codes are refused.

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Sums (d) minus (e) combined with (g), as the column (h) instructions say.

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box D transactions reported on line 8a: long-term, basis reported to the IRS, no adjustments. That matches the line 8a text and Exception 1.

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: Column (e) is the reported basis for Box D. That matches the instructions for covered securities.

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Aggregate entries carry no codes, so column (g) is zero. That is consistent with 'no adjustments'.

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Sums (d) minus (e) plus (g). That matches the line 8a example, where column (h) is $6,000 minus $2,000.

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box D transactions on Form 8949 for line 8b ('Box D or Box J checked'). Box J is refused.

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: Column (e) is the reported basis for Box D, even when incorrect, with the correction made in column (g).

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Column (g) is reported basis minus correct basis plus the wash-sale loss. That matches the basis worksheet and the code W instructions.

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Sums (d) minus (e) combined with (g), as the column (h) instructions say.

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box E transactions for line 9 ('Box E or Box K checked'). Box K is refused.

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: Column (e) is the correct basis for noncovered Box E transactions, as the column (e) instructions say.

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: There is no basis correction in column (g) for Box E, so only the wash-sale adjustment remains. That matches the instructions for code B on Box E.

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Sums (d) minus (e) combined with (g), as the column (h) instructions say.

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Sums net proceeds of Box F transactions for line 10. Box L is refused.

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: Column (e) is the correct basis for Box F transactions. Code B on Box F is refused.

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Only the wash-sale adjustment applies. Other codes are refused.

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Sums (d) minus (e) combined with (g), as the column (h) instructions say.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 4 ('Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824') is zero. The other_forms refusal excludes those forms.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 5 (gain or loss from Schedule(s) K-1) is zero. The other_forms refusal excludes K-1 capital gains.

### 6 — Line 6: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 6 (short-term capital loss carryover) is zero. The carryover refusal excludes prior-year carryovers.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 11 (gain from Form 4797, Part I, and Forms 2439, 6252, 4684, 6781, 8824) is zero. The other_forms refusal excludes those forms.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 12 (K-1 long-term gain or loss) is zero. The other_forms refusal excludes it.

### 14 — Line 14: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 14 (long-term capital loss carryover) is zero. The carryover refusal excludes it.

### 13 — Capital gain distributions
Status: **MATCH**

Model: Line 13 'Capital gain distributions' is the Form 1099-DIV box 2a total, plus a zero helper whose refusals screen out unsupported distribution cases. The text says 'Report the total gain (box 2a) on Schedule D, line 13'.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: Adds the column (h) amounts on lines 1a through 6. That matches 'Combine lines 1a through 6 in column (h)'.

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: Adds lines 8a through 14 in column (h). That matches 'Combine lines 8a through 14 in column (h)'. Line 14 is zero in scope.

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: Matches 'Combine lines 7 and 15'.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: Tests whether lines 15 and 16 are both positive. That matches 'Are lines 15 and 16 both gains?'.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: Tests whether lines 18 and 19 are zero and Form 4952 is not being filed. That matches 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?'. The Form 4952 filing test follows the 'Who Must File' exception.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: When line 16 is a loss, takes the larger of the signed loss and -$3,000 (-$1,500 for MFS). That matches 'the smaller of ... treat both amounts as positive numbers'. Zero otherwise, since the line does not apply.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: Tests whether Form 1040 line 3a is above $0. That matches 'Do you have qualified dividends on Form 1040 ... line 3a?'.

## Raw response

```yaml
```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Sums proceeds of Box A transactions reported on line 1a: basis reported to the IRS and no adjustments. Line 1a is for short-term Form 1099-B/1099-DA transactions 'for which basis was reported to the IRS and for which you have no adjustments'. Digital assets and failed eligibility are refused."
  - key: "1a(e)"
    status: MATCH
    reason: "For Box A, column (e) is the basis shown on the broker report. That matches 'enter the basis shown on Form 1099-B' for covered securities."
  - key: "1a(g)"
    status: MATCH
    reason: "Aggregate-route entries must have code 'none', so column (g) is zero. That matches line 1a's 'no adjustments' requirement."
  - key: "1a(h)"
    status: MATCH
    reason: "Sums (d) minus (e) plus (g) over the line 1a transactions. That matches 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)'."
  - key: "1b(d)"
    status: MATCH
    reason: "Sums proceeds of Box A transactions reported on Form 8949 for line 1b ('Box A or Box G checked'). Box G digital assets are refused."
  - key: "1b(e)"
    status: MATCH
    reason: "For Box A, column (e) is the reported basis even when it is incorrect. That matches 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect'."
  - key: "1b(g)"
    status: MATCH
    reason: "Column (g) is reported basis minus correct basis (the Worksheet for Basis Adjustments, lines 3/4) plus the positive wash-sale loss (code W). Other codes are refused."
  - key: "1b(h)"
    status: MATCH
    reason: "Sums (d) minus (e) combined with (g), as the column (h) instructions say."
  - key: "2(d)"
    status: MATCH
    reason: "Sums proceeds of Box B transactions for line 2 ('Box B or Box H checked'). Box H is refused as a digital asset."
  - key: "2(e)"
    status: MATCH
    reason: "For Box B, column (e) is the correct basis from records. That matches 'For noncovered securities, enter the correct basis of the property in column (e)', with -0- in column (g) for code B."
  - key: "2(g)"
    status: MATCH
    reason: "The basis correction applies only to covered boxes, so only the wash-sale adjustment remains for Box B. That matches 'enter the correct basis in column (e), and enter -0- in column (g)' for code B on Box B."
  - key: "2(h)"
    status: MATCH
    reason: "Sums (d) minus (e) combined with (g), as the column (h) instructions say."
  - key: "3(d)"
    status: MATCH
    reason: "Sums net proceeds of Box C transactions for line 3. That matches 'enter in column (d) the net proceeds' when no Form 1099-B was received. Box I is refused."
  - key: "3(e)"
    status: MATCH
    reason: "For Box C, column (e) is the correct basis from records. Code B on Box C is refused."
  - key: "3(g)"
    status: MATCH
    reason: "Only the wash-sale adjustment applies, entered as a positive amount per code W. Other codes are refused."
  - key: "3(h)"
    status: MATCH
    reason: "Sums (d) minus (e) combined with (g), as the column (h) instructions say."
  - key: "8a(d)"
    status: MATCH
    reason: "Sums proceeds of Box D transactions reported on line 8a: long-term, basis reported to the IRS, no adjustments. That matches the line 8a text and Exception 1."
  - key: "8a(e)"
    status: MATCH
    reason: "Column (e) is the reported basis for Box D. That matches the instructions for covered securities."
  - key: "8a(g)"
    status: MATCH
    reason: "Aggregate entries carry no codes, so column (g) is zero. That is consistent with 'no adjustments'."
  - key: "8a(h)"
    status: MATCH
    reason: "Sums (d) minus (e) plus (g). That matches the line 8a example, where column (h) is $6,000 minus $2,000."
  - key: "8b(d)"
    status: MATCH
    reason: "Sums proceeds of Box D transactions on Form 8949 for line 8b ('Box D or Box J checked'). Box J is refused."
  - key: "8b(e)"
    status: MATCH
    reason: "Column (e) is the reported basis for Box D, even when incorrect, with the correction made in column (g)."
  - key: "8b(g)"
    status: MATCH
    reason: "Column (g) is reported basis minus correct basis plus the wash-sale loss. That matches the basis worksheet and the code W instructions."
  - key: "8b(h)"
    status: MATCH
    reason: "Sums (d) minus (e) combined with (g), as the column (h) instructions say."
  - key: "9(d)"
    status: MATCH
    reason: "Sums proceeds of Box E transactions for line 9 ('Box E or Box K checked'). Box K is refused."
  - key: "9(e)"
    status: MATCH
    reason: "Column (e) is the correct basis for noncovered Box E transactions, as the column (e) instructions say."
  - key: "9(g)"
    status: MATCH
    reason: "There is no basis correction in column (g) for Box E, so only the wash-sale adjustment remains. That matches the instructions for code B on Box E."
  - key: "9(h)"
    status: MATCH
    reason: "Sums (d) minus (e) combined with (g), as the column (h) instructions say."
  - key: "10(d)"
    status: MATCH
    reason: "Sums net proceeds of Box F transactions for line 10. Box L is refused."
  - key: "10(e)"
    status: MATCH
    reason: "Column (e) is the correct basis for Box F transactions. Code B on Box F is refused."
  - key: "10(g)"
    status: MATCH
    reason: "Only the wash-sale adjustment applies. Other codes are refused."
  - key: "10(h)"
    status: MATCH
    reason: "Sums (d) minus (e) combined with (g), as the column (h) instructions say."
  - key: "4"
    status: MATCH
    reason: "Line 4 ('Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824') is zero. The other_forms refusal excludes those forms."
  - key: "5"
    status: MATCH
    reason: "Line 5 (gain or loss from Schedule(s) K-1) is zero. The other_forms refusal excludes K-1 capital gains."
  - key: "6"
    status: MATCH
    reason: "Line 6 (short-term capital loss carryover) is zero. The carryover refusal excludes prior-year carryovers."
  - key: "11"
    status: MATCH
    reason: "Line 11 (gain from Form 4797, Part I, and Forms 2439, 6252, 4684, 6781, 8824) is zero. The other_forms refusal excludes those forms."
  - key: "12"
    status: MATCH
    reason: "Line 12 (K-1 long-term gain or loss) is zero. The other_forms refusal excludes it."
  - key: "14"
    status: MATCH
    reason: "Line 14 (long-term capital loss carryover) is zero. The carryover refusal excludes it."
  - key: "13"
    status: MATCH
    reason: "Line 13 'Capital gain distributions' is the Form 1099-DIV box 2a total, plus a zero helper whose refusals screen out unsupported distribution cases. The text says 'Report the total gain (box 2a) on Schedule D, line 13'."
  - key: "7"
    status: MATCH
    reason: "Adds the column (h) amounts on lines 1a through 6. That matches 'Combine lines 1a through 6 in column (h)'."
  - key: "15"
    status: MATCH
    reason: "Adds lines 8a through 14 in column (h). That matches 'Combine lines 8a through 14 in column (h)'. Line 14 is zero in scope."
  - key: "16"
    status: MATCH
    reason: "Matches 'Combine lines 7 and 15'."
  - key: "17"
    status: MATCH
    reason: "Tests whether lines 15 and 16 are both positive. That matches 'Are lines 15 and 16 both gains?'."
  - key: "20"
    status: MATCH
    reason: "Tests whether lines 18 and 19 are zero and Form 4952 is not being filed. That matches 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?'. The Form 4952 filing test follows the 'Who Must File' exception."
  - key: "21"
    status: MATCH
    reason: "When line 16 is a loss, takes the larger of the signed loss and -$3,000 (-$1,500 for MFS). That matches 'the smaller of ... treat both amounts as positive numbers'. Zero otherwise, since the line does not apply."
  - key: "22"
    status: MATCH
    reason: "Tests whether Form 1040 line 3a is above $0. That matches 'Do you have qualified dividends on Form 1040 ... line 3a?'."
```
```
