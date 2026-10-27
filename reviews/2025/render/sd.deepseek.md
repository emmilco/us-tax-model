# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | afc0704a53be3bdc9f34ee222cd9f088068dab73426fed6106b68396fdb86baf |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: Line 1a column (d) totals short-term reported transactions eligible for aggregation; the program sums proceeds for classification A aggregate entries, with refusals excluding unsupported/digital cases.

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: Line 1a column (e) is cost or other basis; for classification A the program uses the basis reported to the IRS, as required for line 1a.

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Line 1a is limited to transactions with no adjustments; the program's aggregate eligibility and refusals exclude adjustment cases, so summing sales.g yields the required zero adjustment total.

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Line 1a column (h) is gain or loss from proceeds less basis plus adjustments; for eligible aggregate transactions sales.h reduces to proceeds less basis.

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Line 1b column (d) totals Form 8949 box A/G transactions; the program sums proceeds for classification A entries reported in detail.

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: Line 1b column (e) is cost or other basis from Form 8949; for box A basis-reported entries the program uses reported basis.

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Line 1b column (g) is the Form 8949 adjustment total; the program sums supported basis and wash-sale adjustments for classification A detail entries.

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Line 1b column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation.

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Line 2 column (d) totals Form 8949 box B/H transactions; the program sums proceeds for classification B detail entries.

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: Line 2 column (e) is cost or other basis; for box B basis-not-reported entries the program uses correct adjusted basis from records.

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: Line 2 column (g) is the Form 8949 adjustment total; the program sums supported adjustments for classification B detail entries.

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Line 2 column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation.

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Line 3 column (d) totals Form 8949 box C/I transactions; the program sums proceeds for classification C detail entries.

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: Line 3 column (e) is cost or other basis; for box C entries not reported on a 1099-B/DA the program uses correct adjusted basis from records.

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Line 3 column (g) is the Form 8949 adjustment total; the program sums supported adjustments for classification C detail entries.

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Line 3 column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation.

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Line 8a column (d) totals long-term reported transactions eligible for aggregation; the program sums proceeds for classification D aggregate entries, refusing unsupported/digital cases.

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: Line 8a column (e) is cost or other basis; for classification D the program uses the basis reported to the IRS, as required for line 8a.

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Line 8a is limited to transactions with no adjustments; the program's aggregate eligibility and refusals exclude adjustment cases, so summing sales.g yields the required zero adjustment total.

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Line 8a column (h) is gain or loss from proceeds less basis plus adjustments; for eligible aggregate transactions sales.h reduces to proceeds less basis.

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Line 8b column (d) totals Form 8949 box D/J transactions; the program sums proceeds for classification D detail entries.

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: Line 8b column (e) is cost or other basis from Form 8949; for box D basis-reported entries the program uses reported basis.

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Line 8b column (g) is the Form 8949 adjustment total; the program sums supported basis and wash-sale adjustments for classification D detail entries.

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Line 8b column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation.

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Line 9 column (d) totals Form 8949 box E/K transactions; the program sums proceeds for classification E detail entries.

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: Line 9 column (e) is cost or other basis; for box E basis-not-reported entries the program uses correct adjusted basis from records.

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: Line 9 column (g) is the Form 8949 adjustment total; the program sums supported adjustments for classification E detail entries.

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Line 9 column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation.

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Line 10 column (d) totals Form 8949 box F/L transactions; the program sums proceeds for classification F detail entries.

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: Line 10 column (e) is cost or other basis; for box F entries not reported on a 1099-B/DA the program uses correct adjusted basis from records.

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Line 10 column (g) is the Form 8949 adjustment total; the program sums supported adjustments for classification F detail entries.

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Line 10 column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: The IRS line 4 is for Form 6252/4684/6781/8824 short-term amounts; the program uses zero when inapplicable and refuses when other source forms are present.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: The IRS line 5 is for Schedule K-1 short-term gains/losses; the program uses zero when inapplicable and refuses when other source forms are present.

### 6 — Line 6: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: The IRS line 6 is the short-term capital loss carryover; the program uses zero when inapplicable and refuses when a carryover or other source forms are present.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: The IRS line 11 is for Form 4797/2439/6252/4684/6781/8824 long-term amounts; the program uses zero when inapplicable and refuses when other source forms are present.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: The IRS line 12 is for Schedule K-1 long-term gains/losses; the program uses zero when inapplicable and refuses when other source forms are present.

### 14 — Line 14: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: The IRS line 14 is the long-term capital loss carryover; the program uses zero when inapplicable and refuses when a carryover or other source forms are present.

### 13 — Capital gain distributions
Status: **MATCH**

Model: The IRS line 13 is capital gain distributions; the program uses Form 1099-DIV box 2a plus a zero scope check, with refusals excluding unsupported distribution cases.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: The IRS line 7 combines lines 1a through 6 in column (h); the program adds the column (h) amounts for 1a, 1b, 2, and 3 plus lines 4 through 6.

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: The IRS line 15 combines lines 8a through 14 in column (h); the program adds the column (h) amounts for 8a, 8b, 9, and 10 plus lines 11 through 14.

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: The IRS line 16 combines lines 7 and 15; the program adds line 7 and line 15.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: The IRS line 17 asks whether lines 15 and 16 are both gains; the program checks both amounts are greater than zero.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: The IRS line 20 asks whether lines 18 and 19 are zero or blank and Form 4952 is not being filed; the program checks the corresponding zero helpers and the Form 4952 filing helper.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: The IRS line 21 limits a line 16 loss to the annual capital loss limit; the program takes the larger signed amount, equivalent to the smaller positive loss when the note's positive-number rule is applied.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: The IRS line 22 asks whether there are qualified dividends on Form 1040 line 3a; the program checks f1040 line 3a greater than zero.

## Raw response

```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Line 1a column (d) totals short-term reported transactions eligible for aggregation; the program sums proceeds for classification A aggregate entries, with refusals excluding unsupported/digital cases."
  - key: "1a(e)"
    status: MATCH
    reason: "Line 1a column (e) is cost or other basis; for classification A the program uses the basis reported to the IRS, as required for line 1a."
  - key: "1a(g)"
    status: MATCH
    reason: "Line 1a is limited to transactions with no adjustments; the program's aggregate eligibility and refusals exclude adjustment cases, so summing sales.g yields the required zero adjustment total."
  - key: "1a(h)"
    status: MATCH
    reason: "Line 1a column (h) is gain or loss from proceeds less basis plus adjustments; for eligible aggregate transactions sales.h reduces to proceeds less basis."
  - key: "1b(d)"
    status: MATCH
    reason: "Line 1b column (d) totals Form 8949 box A/G transactions; the program sums proceeds for classification A entries reported in detail."
  - key: "1b(e)"
    status: MATCH
    reason: "Line 1b column (e) is cost or other basis from Form 8949; for box A basis-reported entries the program uses reported basis."
  - key: "1b(g)"
    status: MATCH
    reason: "Line 1b column (g) is the Form 8949 adjustment total; the program sums supported basis and wash-sale adjustments for classification A detail entries."
  - key: "1b(h)"
    status: MATCH
    reason: "Line 1b column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation."
  - key: "2(d)"
    status: MATCH
    reason: "Line 2 column (d) totals Form 8949 box B/H transactions; the program sums proceeds for classification B detail entries."
  - key: "2(e)"
    status: MATCH
    reason: "Line 2 column (e) is cost or other basis; for box B basis-not-reported entries the program uses correct adjusted basis from records."
  - key: "2(g)"
    status: MATCH
    reason: "Line 2 column (g) is the Form 8949 adjustment total; the program sums supported adjustments for classification B detail entries."
  - key: "2(h)"
    status: MATCH
    reason: "Line 2 column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation."
  - key: "3(d)"
    status: MATCH
    reason: "Line 3 column (d) totals Form 8949 box C/I transactions; the program sums proceeds for classification C detail entries."
  - key: "3(e)"
    status: MATCH
    reason: "Line 3 column (e) is cost or other basis; for box C entries not reported on a 1099-B/DA the program uses correct adjusted basis from records."
  - key: "3(g)"
    status: MATCH
    reason: "Line 3 column (g) is the Form 8949 adjustment total; the program sums supported adjustments for classification C detail entries."
  - key: "3(h)"
    status: MATCH
    reason: "Line 3 column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation."
  - key: "8a(d)"
    status: MATCH
    reason: "Line 8a column (d) totals long-term reported transactions eligible for aggregation; the program sums proceeds for classification D aggregate entries, refusing unsupported/digital cases."
  - key: "8a(e)"
    status: MATCH
    reason: "Line 8a column (e) is cost or other basis; for classification D the program uses the basis reported to the IRS, as required for line 8a."
  - key: "8a(g)"
    status: MATCH
    reason: "Line 8a is limited to transactions with no adjustments; the program's aggregate eligibility and refusals exclude adjustment cases, so summing sales.g yields the required zero adjustment total."
  - key: "8a(h)"
    status: MATCH
    reason: "Line 8a column (h) is gain or loss from proceeds less basis plus adjustments; for eligible aggregate transactions sales.h reduces to proceeds less basis."
  - key: "8b(d)"
    status: MATCH
    reason: "Line 8b column (d) totals Form 8949 box D/J transactions; the program sums proceeds for classification D detail entries."
  - key: "8b(e)"
    status: MATCH
    reason: "Line 8b column (e) is cost or other basis from Form 8949; for box D basis-reported entries the program uses reported basis."
  - key: "8b(g)"
    status: MATCH
    reason: "Line 8b column (g) is the Form 8949 adjustment total; the program sums supported basis and wash-sale adjustments for classification D detail entries."
  - key: "8b(h)"
    status: MATCH
    reason: "Line 8b column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation."
  - key: "9(d)"
    status: MATCH
    reason: "Line 9 column (d) totals Form 8949 box E/K transactions; the program sums proceeds for classification E detail entries."
  - key: "9(e)"
    status: MATCH
    reason: "Line 9 column (e) is cost or other basis; for box E basis-not-reported entries the program uses correct adjusted basis from records."
  - key: "9(g)"
    status: MATCH
    reason: "Line 9 column (g) is the Form 8949 adjustment total; the program sums supported adjustments for classification E detail entries."
  - key: "9(h)"
    status: MATCH
    reason: "Line 9 column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation."
  - key: "10(d)"
    status: MATCH
    reason: "Line 10 column (d) totals Form 8949 box F/L transactions; the program sums proceeds for classification F detail entries."
  - key: "10(e)"
    status: MATCH
    reason: "Line 10 column (e) is cost or other basis; for box F entries not reported on a 1099-B/DA the program uses correct adjusted basis from records."
  - key: "10(g)"
    status: MATCH
    reason: "Line 10 column (g) is the Form 8949 adjustment total; the program sums supported adjustments for classification F detail entries."
  - key: "10(h)"
    status: MATCH
    reason: "Line 10 column (h) subtracts column (e) from column (d) and combines column (g); sales.h follows that computation."
  - key: "4"
    status: MATCH
    reason: "The IRS line 4 is for Form 6252/4684/6781/8824 short-term amounts; the program uses zero when inapplicable and refuses when other source forms are present."
  - key: "5"
    status: MATCH
    reason: "The IRS line 5 is for Schedule K-1 short-term gains/losses; the program uses zero when inapplicable and refuses when other source forms are present."
  - key: "6"
    status: MATCH
    reason: "The IRS line 6 is the short-term capital loss carryover; the program uses zero when inapplicable and refuses when a carryover or other source forms are present."
  - key: "11"
    status: MATCH
    reason: "The IRS line 11 is for Form 4797/2439/6252/4684/6781/8824 long-term amounts; the program uses zero when inapplicable and refuses when other source forms are present."
  - key: "12"
    status: MATCH
    reason: "The IRS line 12 is for Schedule K-1 long-term gains/losses; the program uses zero when inapplicable and refuses when other source forms are present."
  - key: "14"
    status: MATCH
    reason: "The IRS line 14 is the long-term capital loss carryover; the program uses zero when inapplicable and refuses when a carryover or other source forms are present."
  - key: "13"
    status: MATCH
    reason: "The IRS line 13 is capital gain distributions; the program uses Form 1099-DIV box 2a plus a zero scope check, with refusals excluding unsupported distribution cases."
  - key: "7"
    status: MATCH
    reason: "The IRS line 7 combines lines 1a through 6 in column (h); the program adds the column (h) amounts for 1a, 1b, 2, and 3 plus lines 4 through 6."
  - key: "15"
    status: MATCH
    reason: "The IRS line 15 combines lines 8a through 14 in column (h); the program adds the column (h) amounts for 8a, 8b, 9, and 10 plus lines 11 through 14."
  - key: "16"
    status: MATCH
    reason: "The IRS line 16 combines lines 7 and 15; the program adds line 7 and line 15."
  - key: "17"
    status: MATCH
    reason: "The IRS line 17 asks whether lines 15 and 16 are both gains; the program checks both amounts are greater than zero."
  - key: "20"
    status: MATCH
    reason: "The IRS line 20 asks whether lines 18 and 19 are zero or blank and Form 4952 is not being filed; the program checks the corresponding zero helpers and the Form 4952 filing helper."
  - key: "21"
    status: MATCH
    reason: "The IRS line 21 limits a line 16 loss to the annual capital loss limit; the program takes the larger signed amount, equivalent to the smaller positive loss when the note's positive-number rule is applied."
  - key: "22"
    status: MATCH
    reason: "The IRS line 22 asks whether there are qualified dividends on Form 1040 line 3a; the program checks f1040 line 3a greater than zero."
```
