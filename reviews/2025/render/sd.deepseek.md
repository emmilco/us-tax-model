# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 04728b33493dd779d4177982aef3694b366296836745e6b2738683515d09962a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | f0dc1255712e282cb90d9cc4ff2ab072e67e24b3fdb2804e57adb1437395c129 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 45 / 1 / 0 / 0 |
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

Model: IRS line 1a totals short-term basis-reported, no-adjustment transactions; the restatement sums proceeds for the A/aggregate subset, with unsupported cases refused.

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: IRS line 1a column (e) is cost or other basis for those short-term basis-reported, no-adjustment transactions; the restatement uses the basis helper for the A/aggregate subset.

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: IRS line 1a has no adjustments; the restatement sums the adjustment helper over A/aggregate entries, and ineligible aggregate adjustments are refused.

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: IRS line 1a column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for A/aggregate entries.

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: IRS line 1b totals Form 8949 Box A (and Box G, excluded as digital) transactions; the restatement sums proceeds for A/detail entries.

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: IRS line 1b column (e) is cost or other basis for Box A transactions; the restatement uses the basis helper for A/detail entries.

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: IRS line 1b column (g) is adjustments for Box A transactions; the restatement sums the supported adjustment helper for A/detail entries.

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: IRS line 1b column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for A/detail entries.

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: IRS line 2 totals Form 8949 Box B (and Box H, excluded as digital) transactions; the restatement sums proceeds for B/detail entries.

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: IRS line 2 column (e) is cost or other basis for Box B transactions; the restatement uses the basis helper for B/detail entries.

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: IRS line 2 column (g) is adjustments for Box B transactions; the restatement sums the supported adjustment helper for B/detail entries.

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: IRS line 2 column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for B/detail entries.

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: IRS line 3 totals Form 8949 Box C (and Box I, excluded as digital) transactions; the restatement sums proceeds for C/detail entries.

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: IRS line 3 column (e) is cost or other basis for Box C transactions; the restatement uses the basis helper for C/detail entries.

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: IRS line 3 column (g) is adjustments for Box C transactions; the restatement sums the supported adjustment helper for C/detail entries.

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: IRS line 3 column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for C/detail entries.

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: IRS line 8a totals long-term basis-reported, no-adjustment transactions; the restatement sums proceeds for the D/aggregate subset, with unsupported cases refused.

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: IRS line 8a column (e) is cost or other basis for those long-term basis-reported, no-adjustment transactions; the restatement uses the basis helper for D/aggregate entries.

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: IRS line 8a has no adjustments; the restatement sums the adjustment helper over D/aggregate entries, and ineligible aggregate adjustments are refused.

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: IRS line 8a column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for D/aggregate entries.

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: IRS line 8b totals Form 8949 Box D (and Box J, excluded as digital) transactions; the restatement sums proceeds for D/detail entries.

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: IRS line 8b column (e) is cost or other basis for Box D transactions; the restatement uses the basis helper for D/detail entries.

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: IRS line 8b column (g) is adjustments for Box D transactions; the restatement sums the supported adjustment helper for D/detail entries.

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: IRS line 8b column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for D/detail entries.

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: IRS line 9 totals Form 8949 Box E (and Box K, excluded as digital) transactions; the restatement sums proceeds for E/detail entries.

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: IRS line 9 column (e) is cost or other basis for Box E transactions; the restatement uses the basis helper for E/detail entries.

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: IRS line 9 column (g) is adjustments for Box E transactions; the restatement sums the supported adjustment helper for E/detail entries.

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: IRS line 9 column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for E/detail entries.

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: IRS line 10 totals Form 8949 Box F (and Box L, excluded as digital) transactions; the restatement sums proceeds for F/detail entries.

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: IRS line 10 column (e) is cost or other basis for Box F transactions; the restatement uses the basis helper for F/detail entries.

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: IRS line 10 column (g) is adjustments for Box F transactions; the restatement sums the supported adjustment helper for F/detail entries.

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: IRS line 10 column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for F/detail entries.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: With no other-form items, the Form 6252/4684/6781/8824 short-term items described on line 4 are absent, so $0 is correct; the refusal names those excluded forms.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: With no other-form or K-1 items, the line 5 short-term partnership/S corporation/estate/trust amount is absent, so $0 is correct; the refusal names that exclusion.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: IRS line 6 takes the short-term capital loss carryover from line 8 of the Capital Loss Carryover Worksheet; the restatement enters it as a negative loss when the 2024 line 21 loss gate applies, else no amount.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: With no other-form items, the Forms 4797/2439/6252/4684/6781/8824 long-term amounts described on line 11 are absent, so $0 is correct; the refusal names those excluded forms.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: With no K-1 items, the line 12 long-term partnership/S corporation/estate/trust amount is absent, so $0 is correct; the refusal names that exclusion.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: IRS line 14 takes the long-term capital loss carryover from line 13 of the Capital Loss Carryover Worksheet; the restatement enters it as a negative loss when the 2024 line 21 loss gate applies, else no amount.

### 13 — Capital gain distributions
Status: **MATCH**

Model: IRS line 13 is capital gain distributions; the restatement adds the 1099-DIV box 2a distribution input and a zero scope-check, refusing unsupported distribution cases.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: IRS line 7 combines lines 1a through 6 in column (h); the restatement adds the corresponding line 1a, 1b, 2, 3, 4, 5, and 6 amounts.

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: IRS line 15 combines lines 8a through 14 in column (h); the restatement adds the corresponding line 8a, 8b, 9, 10, 11, 12, 13, and 14 amounts.

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: IRS line 16 combines lines 7 and 15; the restatement adds line 7 and line 15.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: IRS line 17 asks whether lines 15 and 16 are both gains; the restatement is true exactly when both amounts are greater than zero.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MISMATCH**

Restated: helper "Line 18. 28% Rate Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 skipped)" = $0 and helper "Line 19. Unrecaptured Section 1250 Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 skipped)" = $0 and helper "Are you filing Form 4952?" = false

Model: IRS line 17 says: 'No. Skip lines 18 through 21, and go to line 22.' The restatement computes line 20 even when line 17 is No; it should be skipped.

Ruling: representation; f1040sd p. 2, line 17: "Are lines 15 and 16 both gains? Yes. Go to line 18. No. Skip lines 18 through 21, and go to line 22." The model reads the restated line 20 as computed when line 17 is No. Line 20 is a Boolean flow predicate: the documented convention (forms/2025/sd.yaml form note, "Boolean flow predicates are shown even when their printed line is skipped"; adjudication README, owner's decision of 2026-10-26, "Boolean flow predicates are shown ... so the rule does not apply to them") exempts it from the skipped-line rule, and on the line-17-No path no amount reads it (the tax worksheet choice goes by line 22, which the project computes). The English states the printed question ("Are lines 18 and 19 both zero or blank and you are not filing Form 4952?") over lines 18 and 19, which are $0 when line 17 is No, and the Form 4952 helper. Project stands.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: IRS line 21 applies only if line 16 is a loss and uses the smaller positive loss or annual limit; the signed helper chooses the larger signed amount, equivalent to that smaller positive amount, and otherwise no amount.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: IRS line 22 asks whether there are qualified dividends on Form 1040 line 3a; the restatement is true exactly when f1040 line 3a is greater than zero.

## Raw response

```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "IRS line 1a totals short-term basis-reported, no-adjustment transactions; the restatement sums proceeds for the A/aggregate subset, with unsupported cases refused."
  - key: "1a(e)"
    status: MATCH
    reason: "IRS line 1a column (e) is cost or other basis for those short-term basis-reported, no-adjustment transactions; the restatement uses the basis helper for the A/aggregate subset."
  - key: "1a(g)"
    status: MATCH
    reason: "IRS line 1a has no adjustments; the restatement sums the adjustment helper over A/aggregate entries, and ineligible aggregate adjustments are refused."
  - key: "1a(h)"
    status: MATCH
    reason: "IRS line 1a column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for A/aggregate entries."
  - key: "1b(d)"
    status: MATCH
    reason: "IRS line 1b totals Form 8949 Box A (and Box G, excluded as digital) transactions; the restatement sums proceeds for A/detail entries."
  - key: "1b(e)"
    status: MATCH
    reason: "IRS line 1b column (e) is cost or other basis for Box A transactions; the restatement uses the basis helper for A/detail entries."
  - key: "1b(g)"
    status: MATCH
    reason: "IRS line 1b column (g) is adjustments for Box A transactions; the restatement sums the supported adjustment helper for A/detail entries."
  - key: "1b(h)"
    status: MATCH
    reason: "IRS line 1b column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for A/detail entries."
  - key: "2(d)"
    status: MATCH
    reason: "IRS line 2 totals Form 8949 Box B (and Box H, excluded as digital) transactions; the restatement sums proceeds for B/detail entries."
  - key: "2(e)"
    status: MATCH
    reason: "IRS line 2 column (e) is cost or other basis for Box B transactions; the restatement uses the basis helper for B/detail entries."
  - key: "2(g)"
    status: MATCH
    reason: "IRS line 2 column (g) is adjustments for Box B transactions; the restatement sums the supported adjustment helper for B/detail entries."
  - key: "2(h)"
    status: MATCH
    reason: "IRS line 2 column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for B/detail entries."
  - key: "3(d)"
    status: MATCH
    reason: "IRS line 3 totals Form 8949 Box C (and Box I, excluded as digital) transactions; the restatement sums proceeds for C/detail entries."
  - key: "3(e)"
    status: MATCH
    reason: "IRS line 3 column (e) is cost or other basis for Box C transactions; the restatement uses the basis helper for C/detail entries."
  - key: "3(g)"
    status: MATCH
    reason: "IRS line 3 column (g) is adjustments for Box C transactions; the restatement sums the supported adjustment helper for C/detail entries."
  - key: "3(h)"
    status: MATCH
    reason: "IRS line 3 column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for C/detail entries."
  - key: "8a(d)"
    status: MATCH
    reason: "IRS line 8a totals long-term basis-reported, no-adjustment transactions; the restatement sums proceeds for the D/aggregate subset, with unsupported cases refused."
  - key: "8a(e)"
    status: MATCH
    reason: "IRS line 8a column (e) is cost or other basis for those long-term basis-reported, no-adjustment transactions; the restatement uses the basis helper for D/aggregate entries."
  - key: "8a(g)"
    status: MATCH
    reason: "IRS line 8a has no adjustments; the restatement sums the adjustment helper over D/aggregate entries, and ineligible aggregate adjustments are refused."
  - key: "8a(h)"
    status: MATCH
    reason: "IRS line 8a column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for D/aggregate entries."
  - key: "8b(d)"
    status: MATCH
    reason: "IRS line 8b totals Form 8949 Box D (and Box J, excluded as digital) transactions; the restatement sums proceeds for D/detail entries."
  - key: "8b(e)"
    status: MATCH
    reason: "IRS line 8b column (e) is cost or other basis for Box D transactions; the restatement uses the basis helper for D/detail entries."
  - key: "8b(g)"
    status: MATCH
    reason: "IRS line 8b column (g) is adjustments for Box D transactions; the restatement sums the supported adjustment helper for D/detail entries."
  - key: "8b(h)"
    status: MATCH
    reason: "IRS line 8b column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for D/detail entries."
  - key: "9(d)"
    status: MATCH
    reason: "IRS line 9 totals Form 8949 Box E (and Box K, excluded as digital) transactions; the restatement sums proceeds for E/detail entries."
  - key: "9(e)"
    status: MATCH
    reason: "IRS line 9 column (e) is cost or other basis for Box E transactions; the restatement uses the basis helper for E/detail entries."
  - key: "9(g)"
    status: MATCH
    reason: "IRS line 9 column (g) is adjustments for Box E transactions; the restatement sums the supported adjustment helper for E/detail entries."
  - key: "9(h)"
    status: MATCH
    reason: "IRS line 9 column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for E/detail entries."
  - key: "10(d)"
    status: MATCH
    reason: "IRS line 10 totals Form 8949 Box F (and Box L, excluded as digital) transactions; the restatement sums proceeds for F/detail entries."
  - key: "10(e)"
    status: MATCH
    reason: "IRS line 10 column (e) is cost or other basis for Box F transactions; the restatement uses the basis helper for F/detail entries."
  - key: "10(g)"
    status: MATCH
    reason: "IRS line 10 column (g) is adjustments for Box F transactions; the restatement sums the supported adjustment helper for F/detail entries."
  - key: "10(h)"
    status: MATCH
    reason: "IRS line 10 column (h) is proceeds less basis plus adjustments; the restatement uses the column (h) helper for F/detail entries."
  - key: "4"
    status: MATCH
    reason: "With no other-form items, the Form 6252/4684/6781/8824 short-term items described on line 4 are absent, so $0 is correct; the refusal names those excluded forms."
  - key: "5"
    status: MATCH
    reason: "With no other-form or K-1 items, the line 5 short-term partnership/S corporation/estate/trust amount is absent, so $0 is correct; the refusal names that exclusion."
  - key: "6"
    status: MATCH
    reason: "IRS line 6 takes the short-term capital loss carryover from line 8 of the Capital Loss Carryover Worksheet; the restatement enters it as a negative loss when the 2024 line 21 loss gate applies, else no amount."
  - key: "11"
    status: MATCH
    reason: "With no other-form items, the Forms 4797/2439/6252/4684/6781/8824 long-term amounts described on line 11 are absent, so $0 is correct; the refusal names those excluded forms."
  - key: "12"
    status: MATCH
    reason: "With no K-1 items, the line 12 long-term partnership/S corporation/estate/trust amount is absent, so $0 is correct; the refusal names that exclusion."
  - key: "14"
    status: MATCH
    reason: "IRS line 14 takes the long-term capital loss carryover from line 13 of the Capital Loss Carryover Worksheet; the restatement enters it as a negative loss when the 2024 line 21 loss gate applies, else no amount."
  - key: "13"
    status: MATCH
    reason: "IRS line 13 is capital gain distributions; the restatement adds the 1099-DIV box 2a distribution input and a zero scope-check, refusing unsupported distribution cases."
  - key: "7"
    status: MATCH
    reason: "IRS line 7 combines lines 1a through 6 in column (h); the restatement adds the corresponding line 1a, 1b, 2, 3, 4, 5, and 6 amounts."
  - key: "15"
    status: MATCH
    reason: "IRS line 15 combines lines 8a through 14 in column (h); the restatement adds the corresponding line 8a, 8b, 9, 10, 11, 12, 13, and 14 amounts."
  - key: "16"
    status: MATCH
    reason: "IRS line 16 combines lines 7 and 15; the restatement adds line 7 and line 15."
  - key: "17"
    status: MATCH
    reason: "IRS line 17 asks whether lines 15 and 16 are both gains; the restatement is true exactly when both amounts are greater than zero."
  - key: "20"
    status: MISMATCH
    reason: "IRS line 17 says: 'No. Skip lines 18 through 21, and go to line 22.' The restatement computes line 20 even when line 17 is No; it should be skipped."
  - key: "21"
    status: MATCH
    reason: "IRS line 21 applies only if line 16 is a loss and uses the smaller positive loss or annual limit; the signed helper chooses the larger signed amount, equivalent to that smaller positive amount, and otherwise no amount."
  - key: "22"
    status: MATCH
    reason: "IRS line 22 asks whether there are qualified dividends on Form 1040 line 3a; the restatement is true exactly when f1040 line 3a is greater than zero."
```
