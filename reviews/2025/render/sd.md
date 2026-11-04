# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a758b810b693e2608a599c15804503782b03af0cd1f05e3ac8227d715236ef1b |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 8d3da910fc9bc545882f7f1186041dd9584fd5eeef0ac9633678e36aa1567a72 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 46 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 8, 10, 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 31, 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| f4952 | 2025; created 2025-05-28 | 1, 2, 3, 4 | whole document | efbeec4c44a1e43fb00231942c811a454d86b3632a2a662238893f8c4595bf81 | 3, 4 | c98eb27a83a89faecfdd0cd6597e8063fbd86a14ba1606f3e96c1c5f016d2b5c |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| p550 | 2025 returns; printed date 2026-03-05 | 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### 1a(d) — Line 1a, column (d) totals
Status: **MATCH**

Model: Line 1a takes proceeds for short-term transactions reported to the IRS with basis and no adjustments, chosen for the aggregate route. Box G is refused as a digital asset, and ineligible aggregate entries are refused, so only Box A qualifying entries are summed.

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: For Box A (covered) entries, column (e) is the basis shown on the broker report. That matches the aggregate totals described for line 1a.

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Aggregate entries with any adjustment code are refused, so column (g) sums to zero. This is consistent with line 1a being limited to transactions 'for which you have no adjustments.'

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Column (h) is column (d) less column (e), combined with column (g) (zero here). This matches 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d).'

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Line 1b totals Form 8949 transactions with Box A or G checked. Box G is refused, so summing proceeds of Box A entries on the detail route matches.

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: For Box A, column (e) is the basis shown on the Form 1099-B even if incorrect, as the code B instructions direct.

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Column (g) nets the code B correction (reported minus correct basis, positive or negative per the Worksheet for Basis Adjustments) and the code W wash-sale loss as a positive number. Other codes are refused.

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Column (h) is column (d) minus column (e), combined with column (g), as the line 1b/2/3/8b/9/10 column (h) instructions say.

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Line 2 totals Box B/H transactions on Form 8949. Box H is refused, and Box B cannot use the aggregate route, so summing Box B detail proceeds matches.

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: For Box B (basis not reported to the IRS), column (e) is the correct basis. This matches 'enter the correct basis in column (e), and enter -0- in column (g)' for an incorrect basis, and correct basis for noncovered securities.

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: No code B adjustment is made for uncovered entries, because the basis correction requires 'Basis reported to IRS'. Only the wash-sale W amount enters column (g), consistent with the code table.

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Column (d) less column (e), combined with column (g), as instructed.

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Line 3 totals Box C/I transactions. Box I is refused, so summing Box C detail proceeds (net proceeds if no report) matches.

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: For Box C, column (e) is the correct adjusted basis from records, as required when no Form 1099-B was received.

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Code B with Box C is refused, so column (g) holds only an applicable W wash-sale amount, consistent with the code instructions.

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Column (d) less column (e), combined with column (g), as instructed.

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: This is the long-term counterpart of line 1a: aggregate totals of Box D eligible transactions with basis reported and no adjustments. Box J is refused.

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: For Box D (covered) entries, column (e) is the reported basis, matching the line 8a examples.

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Aggregate entries with any adjustment code are refused, so column (g) is zero, consistent with 'no adjustments'.

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Column (d) minus column (e), matching the line 8a example '$4,000 ($6,000 − $2,000) in column (h).'

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Line 8b totals Form 8949 Box D/J transactions. Box J is refused, so summing Box D detail proceeds matches.

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: For Box D, column (e) is the basis as reported, even if incorrect, per the Form 8949 Part II note.

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Column (g) nets the code B correction and the code W positive wash-sale amount, per the code table and the basis-adjustment worksheet.

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Column (d) less column (e), combined with column (g), as instructed.

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Line 9 totals Box E/K transactions. Box K is refused, and Box E cannot use the aggregate route, so summing Box E detail proceeds matches.

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: For Box E, column (e) is the correct basis, per the code B instructions for Box E.

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: No code B adjustment applies to uncovered entries; only the W amount enters column (g), consistent with the instructions.

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Column (d) less column (e), combined with column (g), as instructed.

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Line 10 totals Box F/L transactions. Box L is refused, so summing Box F detail proceeds matches.

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: For Box F, column (e) is the correct adjusted basis from records.

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Code B with Box F is refused, so column (g) holds only an applicable W amount.

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Column (d) less column (e), combined with column (g), as instructed.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 4 covers 'Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824'. Those forms are refused via sd.other_forms, so zero is right within the supported cases.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 5 covers Schedule K-1 net short-term gain or loss. K-1 capital gains or losses are refused via sd.other_forms, so zero is right within the supported cases.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: Line 6 enters 'the amount, if any, from line 8 of your Capital Loss Carryover Worksheet' in parentheses. The program holds that amount as a negative when 2024 line 21 was a loss, and zero otherwise, consistent with 'Otherwise, you don't have any carryovers.'

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 11 covers Forms 4797, 2439, 6252, 4684, 6781 and 8824. These are all refused via sd.other_forms, so zero is right within the supported cases.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 12 covers Schedule K-1 net long-term gain or loss, which is refused via sd.other_forms.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: Line 14 enters the amount from line 13 of the Capital Loss Carryover Worksheet in parentheses. The program holds it as a negative when 2024 line 21 was a loss, and zero otherwise.

### 13 — Capital gain distributions
Status: **MATCH**

Model: Line 13 is 'Capital gain distributions'. The instructions say to report the total gain (box 2a) on line 13. Special components (section 1202, section 897, etc.) are refused through the div gates.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: This matches 'Combine lines 1a through 6 in column (h)'. Line 6 is held as a negative, so adding the lines combines them correctly.

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: This matches 'Combine lines 8a through 14 in column (h)', with line 14 held as a negative.

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: This matches 'Combine lines 7 and 15 and enter the result.'

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: This matches 'Are lines 15 and 16 both gains?' A gain is an amount greater than zero.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: This matches 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?' Lines 18 and 19 are zero when line 17 is No, consistent with skipping them.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: Line 21 enters the smaller of the line 16 loss or ($3,000)/($1,500 MFS), 'treat both amounts as positive numbers'. The larger signed value of line 16 and the negative limit gives the same result.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: This matches 'Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?'

## Raw response

```yaml
```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Line 1a takes proceeds for short-term transactions reported to the IRS with basis and no adjustments, chosen for the aggregate route. Box G is refused as a digital asset, and ineligible aggregate entries are refused, so only Box A qualifying entries are summed."
  - key: "1a(e)"
    status: MATCH
    reason: "For Box A (covered) entries, column (e) is the basis shown on the broker report. That matches the aggregate totals described for line 1a."
  - key: "1a(g)"
    status: MATCH
    reason: "Aggregate entries with any adjustment code are refused, so column (g) sums to zero. This is consistent with line 1a being limited to transactions 'for which you have no adjustments.'"
  - key: "1a(h)"
    status: MATCH
    reason: "Column (h) is column (d) less column (e), combined with column (g) (zero here). This matches 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d).'"
  - key: "1b(d)"
    status: MATCH
    reason: "Line 1b totals Form 8949 transactions with Box A or G checked. Box G is refused, so summing proceeds of Box A entries on the detail route matches."
  - key: "1b(e)"
    status: MATCH
    reason: "For Box A, column (e) is the basis shown on the Form 1099-B even if incorrect, as the code B instructions direct."
  - key: "1b(g)"
    status: MATCH
    reason: "Column (g) nets the code B correction (reported minus correct basis, positive or negative per the Worksheet for Basis Adjustments) and the code W wash-sale loss as a positive number. Other codes are refused."
  - key: "1b(h)"
    status: MATCH
    reason: "Column (h) is column (d) minus column (e), combined with column (g), as the line 1b/2/3/8b/9/10 column (h) instructions say."
  - key: "2(d)"
    status: MATCH
    reason: "Line 2 totals Box B/H transactions on Form 8949. Box H is refused, and Box B cannot use the aggregate route, so summing Box B detail proceeds matches."
  - key: "2(e)"
    status: MATCH
    reason: "For Box B (basis not reported to the IRS), column (e) is the correct basis. This matches 'enter the correct basis in column (e), and enter -0- in column (g)' for an incorrect basis, and correct basis for noncovered securities."
  - key: "2(g)"
    status: MATCH
    reason: "No code B adjustment is made for uncovered entries, because the basis correction requires 'Basis reported to IRS'. Only the wash-sale W amount enters column (g), consistent with the code table."
  - key: "2(h)"
    status: MATCH
    reason: "Column (d) less column (e), combined with column (g), as instructed."
  - key: "3(d)"
    status: MATCH
    reason: "Line 3 totals Box C/I transactions. Box I is refused, so summing Box C detail proceeds (net proceeds if no report) matches."
  - key: "3(e)"
    status: MATCH
    reason: "For Box C, column (e) is the correct adjusted basis from records, as required when no Form 1099-B was received."
  - key: "3(g)"
    status: MATCH
    reason: "Code B with Box C is refused, so column (g) holds only an applicable W wash-sale amount, consistent with the code instructions."
  - key: "3(h)"
    status: MATCH
    reason: "Column (d) less column (e), combined with column (g), as instructed."
  - key: "8a(d)"
    status: MATCH
    reason: "This is the long-term counterpart of line 1a: aggregate totals of Box D eligible transactions with basis reported and no adjustments. Box J is refused."
  - key: "8a(e)"
    status: MATCH
    reason: "For Box D (covered) entries, column (e) is the reported basis, matching the line 8a examples."
  - key: "8a(g)"
    status: MATCH
    reason: "Aggregate entries with any adjustment code are refused, so column (g) is zero, consistent with 'no adjustments'."
  - key: "8a(h)"
    status: MATCH
    reason: "Column (d) minus column (e), matching the line 8a example '$4,000 ($6,000 − $2,000) in column (h).'"
  - key: "8b(d)"
    status: MATCH
    reason: "Line 8b totals Form 8949 Box D/J transactions. Box J is refused, so summing Box D detail proceeds matches."
  - key: "8b(e)"
    status: MATCH
    reason: "For Box D, column (e) is the basis as reported, even if incorrect, per the Form 8949 Part II note."
  - key: "8b(g)"
    status: MATCH
    reason: "Column (g) nets the code B correction and the code W positive wash-sale amount, per the code table and the basis-adjustment worksheet."
  - key: "8b(h)"
    status: MATCH
    reason: "Column (d) less column (e), combined with column (g), as instructed."
  - key: "9(d)"
    status: MATCH
    reason: "Line 9 totals Box E/K transactions. Box K is refused, and Box E cannot use the aggregate route, so summing Box E detail proceeds matches."
  - key: "9(e)"
    status: MATCH
    reason: "For Box E, column (e) is the correct basis, per the code B instructions for Box E."
  - key: "9(g)"
    status: MATCH
    reason: "No code B adjustment applies to uncovered entries; only the W amount enters column (g), consistent with the instructions."
  - key: "9(h)"
    status: MATCH
    reason: "Column (d) less column (e), combined with column (g), as instructed."
  - key: "10(d)"
    status: MATCH
    reason: "Line 10 totals Box F/L transactions. Box L is refused, so summing Box F detail proceeds matches."
  - key: "10(e)"
    status: MATCH
    reason: "For Box F, column (e) is the correct adjusted basis from records."
  - key: "10(g)"
    status: MATCH
    reason: "Code B with Box F is refused, so column (g) holds only an applicable W amount."
  - key: "10(h)"
    status: MATCH
    reason: "Column (d) less column (e), combined with column (g), as instructed."
  - key: "4"
    status: MATCH
    reason: "Line 4 covers 'Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824'. Those forms are refused via sd.other_forms, so zero is right within the supported cases."
  - key: "5"
    status: MATCH
    reason: "Line 5 covers Schedule K-1 net short-term gain or loss. K-1 capital gains or losses are refused via sd.other_forms, so zero is right within the supported cases."
  - key: "6"
    status: MATCH
    reason: "Line 6 enters 'the amount, if any, from line 8 of your Capital Loss Carryover Worksheet' in parentheses. The program holds that amount as a negative when 2024 line 21 was a loss, and zero otherwise, consistent with 'Otherwise, you don't have any carryovers.'"
  - key: "11"
    status: MATCH
    reason: "Line 11 covers Forms 4797, 2439, 6252, 4684, 6781 and 8824. These are all refused via sd.other_forms, so zero is right within the supported cases."
  - key: "12"
    status: MATCH
    reason: "Line 12 covers Schedule K-1 net long-term gain or loss, which is refused via sd.other_forms."
  - key: "14"
    status: MATCH
    reason: "Line 14 enters the amount from line 13 of the Capital Loss Carryover Worksheet in parentheses. The program holds it as a negative when 2024 line 21 was a loss, and zero otherwise."
  - key: "13"
    status: MATCH
    reason: "Line 13 is 'Capital gain distributions'. The instructions say to report the total gain (box 2a) on line 13. Special components (section 1202, section 897, etc.) are refused through the div gates."
  - key: "7"
    status: MATCH
    reason: "This matches 'Combine lines 1a through 6 in column (h)'. Line 6 is held as a negative, so adding the lines combines them correctly."
  - key: "15"
    status: MATCH
    reason: "This matches 'Combine lines 8a through 14 in column (h)', with line 14 held as a negative."
  - key: "16"
    status: MATCH
    reason: "This matches 'Combine lines 7 and 15 and enter the result.'"
  - key: "17"
    status: MATCH
    reason: "This matches 'Are lines 15 and 16 both gains?' A gain is an amount greater than zero."
  - key: "20"
    status: MATCH
    reason: "This matches 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?' Lines 18 and 19 are zero when line 17 is No, consistent with skipping them."
  - key: "21"
    status: MATCH
    reason: "Line 21 enters the smaller of the line 16 loss or ($3,000)/($1,500 MFS), 'treat both amounts as positive numbers'. The larger signed value of line 16 and the negative limit gives the same result."
  - key: "22"
    status: MATCH
    reason: "This matches 'Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?'"
```
```
