# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 04728b33493dd779d4177982aef3694b366296836745e6b2738683515d09962a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | f0dc1255712e282cb90d9cc4ff2ab072e67e24b3fdb2804e57adb1437395c129 |
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
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### 1a(d) — Line 1a, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box A transactions reported on the aggregate route, which matches line 1a's short-term transactions with basis reported to the IRS and no adjustments. The bad_aggregate refusal enforces the Exception 1 conditions, and the digital refusal excludes Form 1099-DA transactions.

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: For Box A, column (e) is the basis reported on the broker statement. Aggregate entries require no corrections, so that is the correct line 1a basis total.

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Aggregate entries must have code 'none', so neither the B nor the W adjustment applies and column (g) sums to zero. That is consistent with line 1a covering transactions 'for which you have no adjustments'.

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Column (h) per entry is proceeds less column (e) plus column (g), summed. This matches 'Subtract column (e) from column (d) and combine the result with column (g)'.

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box A transactions reported in detail on Form 8949. This matches 'Totals for all transactions reported on Form(s) 8949 with Box A'; Box G (digital assets) is refused.

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: For Box A, column (e) is the reported basis even if it is incorrect, as the IRS text directs: 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect.'

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Column (g) is reported basis minus correct basis under code B, plus a positive wash-sale adjustment under code W. This matches the Worksheet for Basis Adjustments and the code W instructions; other codes are refused.

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g) per entry, matching the column (h) instructions.

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box B detail transactions, matching line 2 'with Box B ... checked'; Box H is refused.

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: For Box B (basis not reported), column (e) is the correct basis, matching 'enter the correct basis in column (e)'.

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: No B adjustment applies to Box B because adjust_b requires basis reported to the IRS, matching 'enter -0- in column (g)'. A W adjustment is entered as a positive amount, per the code W instructions.

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g), matching the column (h) instructions.

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box C detail transactions, using net proceeds when there is no broker report. This matches line 3 and the column (d) instructions; Box I is refused.

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: Box C has no broker basis report, so column (e) is the correct basis from records.

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Code B is refused for Box C and W is entered as a positive amount, consistent with the column (g) instructions.

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g), matching the column (h) instructions.

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box D aggregate-route transactions, matching line 8a's long-term transactions with basis reported to the IRS and no adjustments. Exception 1 conditions are enforced by refusal.

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: Column (e) is the reported basis for Box D, which aggregate eligibility requires to be correct.

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Aggregate entries have no codes, so column (g) is zero, consistent with 'for which you have no adjustments'.

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g), matching the column (h) instructions.

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box D detail transactions, matching line 8b 'with Box D ... checked'; Box J is refused.

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: Column (e) is the reported basis for Box D, per 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect.'

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: The B adjustment (reported minus correct basis) and the positive W adjustment match the Worksheet for Basis Adjustments and the code W instructions.

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g), matching the column (h) instructions.

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box E detail transactions, matching line 9; Box K is refused.

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: For Box E, column (e) is the correct basis, matching 'enter the correct basis in column (e)'.

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: No B adjustment applies to Box E, matching 'enter -0- in column (g)'. A W adjustment is entered as a positive amount.

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g), matching the column (h) instructions.

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box F detail transactions, using net proceeds when there is no report, matching line 10; Box L is refused.

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: Box F has no broker report, so column (e) is the correct basis from records.

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Code B is refused for Box F and W is entered as a positive amount, consistent with the column (g) instructions.

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g), matching the column (h) instructions.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Zero is entered, and the refusal names Forms 6252, 4684, 6781 and 8824, which are the sources line 4 lists.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Zero is entered, and the refusal covers capital gains or losses on a Schedule K-1, which is line 5's source.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: When the 2024 line 21 showed a loss, the program enters Capital Loss Carryover Worksheet line 8 as a negative amount. This matches 'Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet' shown in parentheses; otherwise it enters no carryover.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Zero is entered, and the refusal covers Forms 4797, 2439, 6252, 4684, 6781 and 8824, which are line 11's sources.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Zero is entered, and the refusal covers Schedule K-1 capital gains or losses, which is line 12's source.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: When the 2024 line 21 showed a loss, the program enters Capital Loss Carryover Worksheet line 13 as a negative amount. This matches 'Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet' shown in parentheses.

### 13 — Capital gain distributions
Status: **MATCH**

Model: Enters Form 1099-DIV box 2a capital gain distributions, matching 'Report the total gain (box 2a) on Schedule D, line 13'. Section 1202, section 897, liquidation and unreconciled return-of-capital cases are refused.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: Adds column (h) of lines 1a through 6, matching 'Combine lines 1a through 6 in column (h)'.

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: Adds column (h) of lines 8a through 14, matching 'Combine lines 8a through 14 in column (h)'.

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: Matches 'Combine lines 7 and 15'.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: Tests whether both line 15 and line 16 are positive, matching 'Are lines 15 and 16 both gains?'

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: Tests whether lines 18 and 19 are zero and Form 4952 is not being filed. This matches 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?'; the helpers treat skipped lines as zero.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: When line 16 is a loss, the program takes the larger of the signed line 16 and −$3,000 (−$1,500 for married filing separately). That is the smaller loss in absolute terms, matching 'treat both amounts as positive numbers'.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: Tests whether Form 1040 line 3a is greater than zero, matching 'Do you have qualified dividends on Form 1040 ... line 3a?'

## Raw response

```yaml
```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Sums proceeds of Box A transactions reported on the aggregate route, which matches line 1a's short-term transactions with basis reported to the IRS and no adjustments. The bad_aggregate refusal enforces the Exception 1 conditions, and the digital refusal excludes Form 1099-DA transactions."
  - key: "1a(e)"
    status: MATCH
    reason: "For Box A, column (e) is the basis reported on the broker statement. Aggregate entries require no corrections, so that is the correct line 1a basis total."
  - key: "1a(g)"
    status: MATCH
    reason: "Aggregate entries must have code 'none', so neither the B nor the W adjustment applies and column (g) sums to zero. That is consistent with line 1a covering transactions 'for which you have no adjustments'."
  - key: "1a(h)"
    status: MATCH
    reason: "Column (h) per entry is proceeds less column (e) plus column (g), summed. This matches 'Subtract column (e) from column (d) and combine the result with column (g)'."
  - key: "1b(d)"
    status: MATCH
    reason: "Sums proceeds of Box A transactions reported in detail on Form 8949. This matches 'Totals for all transactions reported on Form(s) 8949 with Box A'; Box G (digital assets) is refused."
  - key: "1b(e)"
    status: MATCH
    reason: "For Box A, column (e) is the reported basis even if it is incorrect, as the IRS text directs: 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect.'"
  - key: "1b(g)"
    status: MATCH
    reason: "Column (g) is reported basis minus correct basis under code B, plus a positive wash-sale adjustment under code W. This matches the Worksheet for Basis Adjustments and the code W instructions; other codes are refused."
  - key: "1b(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g) per entry, matching the column (h) instructions."
  - key: "2(d)"
    status: MATCH
    reason: "Sums proceeds of Box B detail transactions, matching line 2 'with Box B ... checked'; Box H is refused."
  - key: "2(e)"
    status: MATCH
    reason: "For Box B (basis not reported), column (e) is the correct basis, matching 'enter the correct basis in column (e)'."
  - key: "2(g)"
    status: MATCH
    reason: "No B adjustment applies to Box B because adjust_b requires basis reported to the IRS, matching 'enter -0- in column (g)'. A W adjustment is entered as a positive amount, per the code W instructions."
  - key: "2(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g), matching the column (h) instructions."
  - key: "3(d)"
    status: MATCH
    reason: "Sums proceeds of Box C detail transactions, using net proceeds when there is no broker report. This matches line 3 and the column (d) instructions; Box I is refused."
  - key: "3(e)"
    status: MATCH
    reason: "Box C has no broker basis report, so column (e) is the correct basis from records."
  - key: "3(g)"
    status: MATCH
    reason: "Code B is refused for Box C and W is entered as a positive amount, consistent with the column (g) instructions."
  - key: "3(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g), matching the column (h) instructions."
  - key: "8a(d)"
    status: MATCH
    reason: "Sums proceeds of Box D aggregate-route transactions, matching line 8a's long-term transactions with basis reported to the IRS and no adjustments. Exception 1 conditions are enforced by refusal."
  - key: "8a(e)"
    status: MATCH
    reason: "Column (e) is the reported basis for Box D, which aggregate eligibility requires to be correct."
  - key: "8a(g)"
    status: MATCH
    reason: "Aggregate entries have no codes, so column (g) is zero, consistent with 'for which you have no adjustments'."
  - key: "8a(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g), matching the column (h) instructions."
  - key: "8b(d)"
    status: MATCH
    reason: "Sums proceeds of Box D detail transactions, matching line 8b 'with Box D ... checked'; Box J is refused."
  - key: "8b(e)"
    status: MATCH
    reason: "Column (e) is the reported basis for Box D, per 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect.'"
  - key: "8b(g)"
    status: MATCH
    reason: "The B adjustment (reported minus correct basis) and the positive W adjustment match the Worksheet for Basis Adjustments and the code W instructions."
  - key: "8b(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g), matching the column (h) instructions."
  - key: "9(d)"
    status: MATCH
    reason: "Sums proceeds of Box E detail transactions, matching line 9; Box K is refused."
  - key: "9(e)"
    status: MATCH
    reason: "For Box E, column (e) is the correct basis, matching 'enter the correct basis in column (e)'."
  - key: "9(g)"
    status: MATCH
    reason: "No B adjustment applies to Box E, matching 'enter -0- in column (g)'. A W adjustment is entered as a positive amount."
  - key: "9(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g), matching the column (h) instructions."
  - key: "10(d)"
    status: MATCH
    reason: "Sums proceeds of Box F detail transactions, using net proceeds when there is no report, matching line 10; Box L is refused."
  - key: "10(e)"
    status: MATCH
    reason: "Box F has no broker report, so column (e) is the correct basis from records."
  - key: "10(g)"
    status: MATCH
    reason: "Code B is refused for Box F and W is entered as a positive amount, consistent with the column (g) instructions."
  - key: "10(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g), matching the column (h) instructions."
  - key: "4"
    status: MATCH
    reason: "Zero is entered, and the refusal names Forms 6252, 4684, 6781 and 8824, which are the sources line 4 lists."
  - key: "5"
    status: MATCH
    reason: "Zero is entered, and the refusal covers capital gains or losses on a Schedule K-1, which is line 5's source."
  - key: "6"
    status: MATCH
    reason: "When the 2024 line 21 showed a loss, the program enters Capital Loss Carryover Worksheet line 8 as a negative amount. This matches 'Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet' shown in parentheses; otherwise it enters no carryover."
  - key: "11"
    status: MATCH
    reason: "Zero is entered, and the refusal covers Forms 4797, 2439, 6252, 4684, 6781 and 8824, which are line 11's sources."
  - key: "12"
    status: MATCH
    reason: "Zero is entered, and the refusal covers Schedule K-1 capital gains or losses, which is line 12's source."
  - key: "14"
    status: MATCH
    reason: "When the 2024 line 21 showed a loss, the program enters Capital Loss Carryover Worksheet line 13 as a negative amount. This matches 'Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet' shown in parentheses."
  - key: "13"
    status: MATCH
    reason: "Enters Form 1099-DIV box 2a capital gain distributions, matching 'Report the total gain (box 2a) on Schedule D, line 13'. Section 1202, section 897, liquidation and unreconciled return-of-capital cases are refused."
  - key: "7"
    status: MATCH
    reason: "Adds column (h) of lines 1a through 6, matching 'Combine lines 1a through 6 in column (h)'."
  - key: "15"
    status: MATCH
    reason: "Adds column (h) of lines 8a through 14, matching 'Combine lines 8a through 14 in column (h)'."
  - key: "16"
    status: MATCH
    reason: "Matches 'Combine lines 7 and 15'."
  - key: "17"
    status: MATCH
    reason: "Tests whether both line 15 and line 16 are positive, matching 'Are lines 15 and 16 both gains?'"
  - key: "20"
    status: MATCH
    reason: "Tests whether lines 18 and 19 are zero and Form 4952 is not being filed. This matches 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?'; the helpers treat skipped lines as zero."
  - key: "21"
    status: MATCH
    reason: "When line 16 is a loss, the program takes the larger of the signed line 16 and −$3,000 (−$1,500 for married filing separately). That is the smaller loss in absolute terms, matching 'treat both amounts as positive numbers'."
  - key: "22"
    status: MATCH
    reason: "Tests whether Form 1040 line 3a is greater than zero, matching 'Do you have qualified dividends on Form 1040 ... line 3a?'"
```
```
