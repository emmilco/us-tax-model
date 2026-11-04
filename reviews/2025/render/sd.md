# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d8a1bade7e8895260afb189920619c7b281ba3f35ca05706a6924a7e0636eac5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | eeaf337d5fa7492478be5ffa58f4ffcda447017332dba311b038e96279119959 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 44 / 2 / 0 / 0 |
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
| p550 | 2025 returns; printed date 2026-03-05 | 82, 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 82, 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### 1a(d) — Line 1a, column (d) totals
Status: **MATCH**

Model: Sums column (d) proceeds for box A sales routed to aggregate, which is line 1a: short-term 1099-B transactions with basis reported and no adjustments. Ineligible aggregate entries and digital assets (1099-DA) are refused.

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: For box A, column (e) is the basis shown on the broker report, which is the reported basis line 1a requires.

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: The aggregate route requires code 'none', so column (g) sums to zero. This fits line 1a, which is limited to transactions 'for which you have no adjustments'.

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Column (h) is proceeds less basis plus column (g), summed. This follows 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d).'

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Sums proceeds for box A transactions reported in detail, which is line 1b ('Box A or Box G checked'). Box G digital assets are refused.

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: For box A, column (e) is the reported basis even if incorrect. This matches the 8949 instruction to 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect.'

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Column (g) combines the code B correction (reported minus correct basis, matching worksheet lines 3–4) with the code W nondeductible loss as a positive amount. Both follow the 8949 instructions.

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) minus (e) combined with (g), summed over box A detail entries, as the line 1b column (h) instructions say.

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Sums proceeds for box B detail entries; line 2 is 'Box B or Box H checked'. Box H is refused as a digital asset.

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: For box B (basis not reported), column (e) is the correct basis. This matches 'enter the correct basis in column (e), and enter -0- in column (g).'

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: The basis correction applies only when basis was reported to the IRS, so box B gets no code B adjustment in (g). Only a code W adjustment can apply, consistent with the instructions.

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: (d) minus (e) combined with (g), summed over box B entries.

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Sums proceeds for box C entries; line 3 is 'Box C or Box I checked'. Box I is refused, and box C entries use net proceeds when there is no report.

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: For box C, column (e) is the correct adjusted basis from records. Code B with box C is refused.

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Only a code W adjustment can apply to box C, and it is entered as a positive amount per the code W instructions.

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: (d) minus (e) combined with (g), summed over box C entries.

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Sums proceeds for box D aggregate-route sales, which is line 8a: long-term transactions with basis reported and no adjustments. Ineligible entries are refused.

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: For box D, column (e) is the reported basis, as line 8a requires.

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: The aggregate route requires no codes, so column (g) is zero, matching 'for which you have no adjustments'.

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Column (d) minus (e) plus (g), summed, consistent with the line 8a example.

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Sums proceeds for box D detail entries; line 8b is 'Box D or Box J checked'. Box J is refused.

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: For box D, column (e) is the reported basis even if incorrect, with the correction made in (g).

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Combines the code B correction (reported minus correct basis) with the code W positive adjustment, per the 8949 instructions.

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: (d) minus (e) combined with (g), summed over box D detail entries.

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Sums proceeds for box E entries; line 9 is 'Box E or Box K checked'. Box K is refused.

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: For box E (basis not reported), column (e) is the correct basis, as instructed.

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: No code B adjustment applies when basis was not reported; only code W can apply, consistent with the instructions.

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: (d) minus (e) combined with (g), summed over box E entries.

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Sums proceeds for box F entries; line 10 is 'Box F or Box L checked'. Box L is refused.

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: For box F, column (e) is the correct adjusted basis from records. Code B with box F is refused.

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Only a code W positive adjustment can apply to box F entries, per the instructions.

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: (d) minus (e) combined with (g), summed over box F entries.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 4 reports gains from Forms 6252, 4684, 6781 and 8824. It is zero, and the program refuses whenever such forms apply, so the line is correctly narrowed.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 5 reports net short-term gain or loss from Schedule K-1. It is zero, and the program refuses when K-1 capital gains or losses exist.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: When 2024 line 21 showed a loss, line 6 enters Capital Loss Carryover Worksheet line 8 as a negative amount, matching the parenthesized line 6 ('from line 8 of your Capital Loss Carryover Worksheet'). Otherwise it is zero.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 11 reports gains from Forms 4797, 2439, 6252, 4684, 6781 and 8824. It is zero, and the program refuses when any of these forms applies.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 12 reports net long-term K-1 gain or loss. It is zero, and the program refuses when K-1 capital items exist.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: When 2024 line 21 showed a loss, line 14 enters worksheet line 13 as a negative amount, matching 'Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet' shown in parentheses.

### 13 — Capital gain distributions
Status: **MATCH**

Model: Line 13 enters total capital gain distributions (Form 1099-DIV box 2a), matching 'Report the total gain (box 2a) on Schedule D, line 13'. Unsupported distribution cases are refused.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: Matches 'Combine lines 1a through 6 in column (h)'. Line 6 is carried as a negative amount.

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: Matches 'Combine lines 8a through 14 in column (h)'. Line 14 is carried as a negative amount.

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: Matches 'Combine lines 7 and 15'.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: Matches 'Are lines 15 and 16 both gains?' as both amounts being greater than zero.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MISMATCH**

Restated: helper "Line 18. 28% Rate Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 skipped)" = $0 and helper "Line 19. Unrecaptured Section 1250 Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 skipped)" = $0 and helper "Are you filing Form 4952?" = false

Model: The restatement answers line 20 in every case. The IRS says 'If line 16 is a loss, skip lines 17 through 20' and, on line 17 No, 'Skip lines 18 through 21, and go to line 22'. On those paths the program answers Yes (QDCGT, don't complete lines 21 and 22) where the line should be skipped.

Ruling: representation; f1040sd p. 2, line 17: "No. Skip lines 18 through 21, and go to line 22". Line 20 (and line 22) are Boolean flow predicates, evaluated on every path by the documented convention (forms/2025/sd.yaml form note); the path the filer follows, and which lines show, is decided by line 17 and line 16 upstream, so the answer on a skipped path is never read. Same reading as the earlier rounds.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: When line 16 is a loss, line 21 takes the larger signed amount of line 16 and -$3,000 (-$1,500 MFS). This equals 'the smaller of: The loss on line 16; or ($3,000), or if married filing separately, ($1,500)' treated as positive numbers.

### 22 — Do you have qualified dividends?
Status: **MISMATCH**

Restated: f1040 line 3a > $0

Model: The restatement answers line 22 unconditionally. The IRS line 20 says 'Don't complete lines 21 and 22 below', so line 22 should be completed only when line 16 is a loss or zero or line 17 is No.

Ruling: representation; f1040sd p. 2, line 17: "No. Skip lines 18 through 21, and go to line 22". Line 20 (and line 22) are Boolean flow predicates, evaluated on every path by the documented convention (forms/2025/sd.yaml form note); the path the filer follows, and which lines show, is decided by line 17 and line 16 upstream, so the answer on a skipped path is never read. Same reading as the earlier rounds.

## Raw response

```yaml
```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Sums column (d) proceeds for box A sales routed to aggregate, which is line 1a: short-term 1099-B transactions with basis reported and no adjustments. Ineligible aggregate entries and digital assets (1099-DA) are refused."
  - key: "1a(e)"
    status: MATCH
    reason: "For box A, column (e) is the basis shown on the broker report, which is the reported basis line 1a requires."
  - key: "1a(g)"
    status: MATCH
    reason: "The aggregate route requires code 'none', so column (g) sums to zero. This fits line 1a, which is limited to transactions 'for which you have no adjustments'."
  - key: "1a(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus column (g), summed. This follows 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d).'"
  - key: "1b(d)"
    status: MATCH
    reason: "Sums proceeds for box A transactions reported in detail, which is line 1b ('Box A or Box G checked'). Box G digital assets are refused."
  - key: "1b(e)"
    status: MATCH
    reason: "For box A, column (e) is the reported basis even if incorrect. This matches the 8949 instruction to 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect.'"
  - key: "1b(g)"
    status: MATCH
    reason: "Column (g) combines the code B correction (reported minus correct basis, matching worksheet lines 3–4) with the code W nondeductible loss as a positive amount. Both follow the 8949 instructions."
  - key: "1b(h)"
    status: MATCH
    reason: "Column (h) is (d) minus (e) combined with (g), summed over box A detail entries, as the line 1b column (h) instructions say."
  - key: "2(d)"
    status: MATCH
    reason: "Sums proceeds for box B detail entries; line 2 is 'Box B or Box H checked'. Box H is refused as a digital asset."
  - key: "2(e)"
    status: MATCH
    reason: "For box B (basis not reported), column (e) is the correct basis. This matches 'enter the correct basis in column (e), and enter -0- in column (g).'"
  - key: "2(g)"
    status: MATCH
    reason: "The basis correction applies only when basis was reported to the IRS, so box B gets no code B adjustment in (g). Only a code W adjustment can apply, consistent with the instructions."
  - key: "2(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box B entries."
  - key: "3(d)"
    status: MATCH
    reason: "Sums proceeds for box C entries; line 3 is 'Box C or Box I checked'. Box I is refused, and box C entries use net proceeds when there is no report."
  - key: "3(e)"
    status: MATCH
    reason: "For box C, column (e) is the correct adjusted basis from records. Code B with box C is refused."
  - key: "3(g)"
    status: MATCH
    reason: "Only a code W adjustment can apply to box C, and it is entered as a positive amount per the code W instructions."
  - key: "3(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box C entries."
  - key: "8a(d)"
    status: MATCH
    reason: "Sums proceeds for box D aggregate-route sales, which is line 8a: long-term transactions with basis reported and no adjustments. Ineligible entries are refused."
  - key: "8a(e)"
    status: MATCH
    reason: "For box D, column (e) is the reported basis, as line 8a requires."
  - key: "8a(g)"
    status: MATCH
    reason: "The aggregate route requires no codes, so column (g) is zero, matching 'for which you have no adjustments'."
  - key: "8a(h)"
    status: MATCH
    reason: "Column (d) minus (e) plus (g), summed, consistent with the line 8a example."
  - key: "8b(d)"
    status: MATCH
    reason: "Sums proceeds for box D detail entries; line 8b is 'Box D or Box J checked'. Box J is refused."
  - key: "8b(e)"
    status: MATCH
    reason: "For box D, column (e) is the reported basis even if incorrect, with the correction made in (g)."
  - key: "8b(g)"
    status: MATCH
    reason: "Combines the code B correction (reported minus correct basis) with the code W positive adjustment, per the 8949 instructions."
  - key: "8b(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box D detail entries."
  - key: "9(d)"
    status: MATCH
    reason: "Sums proceeds for box E entries; line 9 is 'Box E or Box K checked'. Box K is refused."
  - key: "9(e)"
    status: MATCH
    reason: "For box E (basis not reported), column (e) is the correct basis, as instructed."
  - key: "9(g)"
    status: MATCH
    reason: "No code B adjustment applies when basis was not reported; only code W can apply, consistent with the instructions."
  - key: "9(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box E entries."
  - key: "10(d)"
    status: MATCH
    reason: "Sums proceeds for box F entries; line 10 is 'Box F or Box L checked'. Box L is refused."
  - key: "10(e)"
    status: MATCH
    reason: "For box F, column (e) is the correct adjusted basis from records. Code B with box F is refused."
  - key: "10(g)"
    status: MATCH
    reason: "Only a code W positive adjustment can apply to box F entries, per the instructions."
  - key: "10(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box F entries."
  - key: "4"
    status: MATCH
    reason: "Line 4 reports gains from Forms 6252, 4684, 6781 and 8824. It is zero, and the program refuses whenever such forms apply, so the line is correctly narrowed."
  - key: "5"
    status: MATCH
    reason: "Line 5 reports net short-term gain or loss from Schedule K-1. It is zero, and the program refuses when K-1 capital gains or losses exist."
  - key: "6"
    status: MATCH
    reason: "When 2024 line 21 showed a loss, line 6 enters Capital Loss Carryover Worksheet line 8 as a negative amount, matching the parenthesized line 6 ('from line 8 of your Capital Loss Carryover Worksheet'). Otherwise it is zero."
  - key: "11"
    status: MATCH
    reason: "Line 11 reports gains from Forms 4797, 2439, 6252, 4684, 6781 and 8824. It is zero, and the program refuses when any of these forms applies."
  - key: "12"
    status: MATCH
    reason: "Line 12 reports net long-term K-1 gain or loss. It is zero, and the program refuses when K-1 capital items exist."
  - key: "14"
    status: MATCH
    reason: "When 2024 line 21 showed a loss, line 14 enters worksheet line 13 as a negative amount, matching 'Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet' shown in parentheses."
  - key: "13"
    status: MATCH
    reason: "Line 13 enters total capital gain distributions (Form 1099-DIV box 2a), matching 'Report the total gain (box 2a) on Schedule D, line 13'. Unsupported distribution cases are refused."
  - key: "7"
    status: MATCH
    reason: "Matches 'Combine lines 1a through 6 in column (h)'. Line 6 is carried as a negative amount."
  - key: "15"
    status: MATCH
    reason: "Matches 'Combine lines 8a through 14 in column (h)'. Line 14 is carried as a negative amount."
  - key: "16"
    status: MATCH
    reason: "Matches 'Combine lines 7 and 15'."
  - key: "17"
    status: MATCH
    reason: "Matches 'Are lines 15 and 16 both gains?' as both amounts being greater than zero."
  - key: "20"
    status: MISMATCH
    reason: "The restatement answers line 20 in every case. The IRS says 'If line 16 is a loss, skip lines 17 through 20' and, on line 17 No, 'Skip lines 18 through 21, and go to line 22'. On those paths the program answers Yes (QDCGT, don't complete lines 21 and 22) where the line should be skipped."
  - key: "21"
    status: MATCH
    reason: "When line 16 is a loss, line 21 takes the larger signed amount of line 16 and -$3,000 (-$1,500 MFS). This equals 'the smaller of: The loss on line 16; or ($3,000), or if married filing separately, ($1,500)' treated as positive numbers."
  - key: "22"
    status: MISMATCH
    reason: "The restatement answers line 22 unconditionally. The IRS line 20 says 'Don't complete lines 21 and 22 below', so line 22 should be completed only when line 16 is a loss or zero or line 17 is No."
```
```
