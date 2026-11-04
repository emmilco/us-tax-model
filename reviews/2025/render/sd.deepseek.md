# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a758b810b693e2608a599c15804503782b03af0cd1f05e3ac8227d715236ef1b |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: Schedule D line 1a aggregates short-term Box A transactions using column (d) proceeds when reported in aggregate; the refusal excludes screened or unsupported cases.

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: Column (e) uses the reported basis for Box A basis-reported transactions, as required for line 1a.

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Line 1a is limited to no-adjustment aggregate transactions, and the aggregate-route checks make column (g) zero in supported cases.

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Column (h) is proceeds less basis plus adjustments; sales.h computes that same column (h) amount.

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Schedule D line 1b totals Box A detail-reporting transactions, and column (d) is proceeds.

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: Column (e) uses the reported basis for Box A transactions, matching the Form 8949 column (e) requirement.

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Column (g) is the Form 8949 adjustment, and sales.g adds the supported basis and wash-sale adjustments.

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Column (h) subtracts column (e) from column (d) and combines column (g), matching sales.h.

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Line 2 totals Box B detail-reporting transactions; digital Box H is excluded by refusal, and column (d) is proceeds.

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: For Box B, basis was not reported, so column (e) uses the correct basis from records.

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: Column (g) is the Form 8949 adjustment for Box B detail transactions, using supported adjustments.

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Column (h) is proceeds less basis plus adjustments, matching sales.h.

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Line 3 totals Box C detail-reporting transactions; digital Box I is excluded by refusal, and column (d) is proceeds.

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: For Box C, no broker basis report applies, so column (e) uses the correct basis from records.

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Column (g) is the Form 8949 adjustment for Box C detail transactions, using supported adjustments.

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Column (h) is proceeds less basis plus adjustments, matching sales.h.

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Schedule D line 8a aggregates long-term Box D transactions using column (d) proceeds when reported in aggregate; the refusal excludes unsupported cases.

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: Column (e) uses the reported basis for Box D basis-reported transactions, as required for line 8a.

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Line 8a is limited to no-adjustment aggregate transactions, and the aggregate-route checks make column (g) zero in supported cases.

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Column (h) is proceeds less basis plus adjustments; sales.h computes that same column (h) amount.

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Schedule D line 8b totals Box D detail-reporting transactions, and column (d) is proceeds.

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: Column (e) uses the reported basis for Box D transactions, matching the Form 8949 column (e) requirement.

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Column (g) is the Form 8949 adjustment, and sales.g adds the supported basis and wash-sale adjustments.

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Column (h) subtracts column (e) from column (d) and combines column (g), matching sales.h.

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Line 9 totals Box E detail-reporting transactions; digital Box K is excluded by refusal, and column (d) is proceeds.

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: For Box E, basis was not reported, so column (e) uses the correct basis from records.

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: Column (g) is the Form 8949 adjustment for Box E detail transactions, using supported adjustments.

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Column (h) is proceeds less basis plus adjustments, matching sales.h.

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Line 10 totals Box F detail-reporting transactions; digital Box L is excluded by refusal, and column (d) is proceeds.

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: For Box F, no broker basis report applies, so column (e) uses the correct basis from records.

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Column (g) is the Form 8949 adjustment for Box F detail transactions, using supported adjustments.

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Column (h) is proceeds less basis plus adjustments, matching sales.h.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 4 is zero when no other source forms apply; the refusal excludes Forms 6252, 4684, 6781, and 8824.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 5 is zero when no Schedule K-1 partnership, S corporation, estate, or trust gains or losses apply; the refusal excludes them.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: Line 6 uses the Capital Loss Carryover Worksheet line 8 amount as a short-term loss when applicable, and otherwise zero.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 11 is zero when no other source forms apply; the refusal excludes Forms 4797, 2439, 6252, 4684, 6781, and 8824.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 12 is zero when no Schedule K-1 long-term gains or losses apply; the refusal excludes those sources.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: Line 14 uses the Capital Loss Carryover Worksheet line 13 amount as a long-term loss when applicable, and otherwise zero.

### 13 — Capital gain distributions
Status: **MATCH**

Model: Line 13 is the Form 1099-DIV box 2a capital gain distribution; unsupported distribution cases are refused.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: Line 7 combines the Part I column (h) amounts and lines 4 through 6, matching the form instruction to combine lines 1a through 6 in column (h).

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: Line 15 combines the Part II column (h) amounts and lines 11 through 14, matching the form instruction to combine lines 8a through 14 in column (h).

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: Line 16 combines lines 7 and 15, as the form directs.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: Line 17 is true only when both lines 15 and 16 are gains, matching 'Are lines 15 and 16 both gains?'

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: Line 20 checks that lines 18 and 19 are zero or blank and that Form 4952 is not being filed.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: Line 21 limits a line 16 loss to the annual capital loss limit, using the signed larger-of computation that matches the smaller positive loss.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: Line 22 is true when qualified dividends on Form 1040 line 3a are greater than zero.

## Raw response

```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Schedule D line 1a aggregates short-term Box A transactions using column (d) proceeds when reported in aggregate; the refusal excludes screened or unsupported cases."
  - key: "1a(e)"
    status: MATCH
    reason: "Column (e) uses the reported basis for Box A basis-reported transactions, as required for line 1a."
  - key: "1a(g)"
    status: MATCH
    reason: "Line 1a is limited to no-adjustment aggregate transactions, and the aggregate-route checks make column (g) zero in supported cases."
  - key: "1a(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus adjustments; sales.h computes that same column (h) amount."
  - key: "1b(d)"
    status: MATCH
    reason: "Schedule D line 1b totals Box A detail-reporting transactions, and column (d) is proceeds."
  - key: "1b(e)"
    status: MATCH
    reason: "Column (e) uses the reported basis for Box A transactions, matching the Form 8949 column (e) requirement."
  - key: "1b(g)"
    status: MATCH
    reason: "Column (g) is the Form 8949 adjustment, and sales.g adds the supported basis and wash-sale adjustments."
  - key: "1b(h)"
    status: MATCH
    reason: "Column (h) subtracts column (e) from column (d) and combines column (g), matching sales.h."
  - key: "2(d)"
    status: MATCH
    reason: "Line 2 totals Box B detail-reporting transactions; digital Box H is excluded by refusal, and column (d) is proceeds."
  - key: "2(e)"
    status: MATCH
    reason: "For Box B, basis was not reported, so column (e) uses the correct basis from records."
  - key: "2(g)"
    status: MATCH
    reason: "Column (g) is the Form 8949 adjustment for Box B detail transactions, using supported adjustments."
  - key: "2(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus adjustments, matching sales.h."
  - key: "3(d)"
    status: MATCH
    reason: "Line 3 totals Box C detail-reporting transactions; digital Box I is excluded by refusal, and column (d) is proceeds."
  - key: "3(e)"
    status: MATCH
    reason: "For Box C, no broker basis report applies, so column (e) uses the correct basis from records."
  - key: "3(g)"
    status: MATCH
    reason: "Column (g) is the Form 8949 adjustment for Box C detail transactions, using supported adjustments."
  - key: "3(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus adjustments, matching sales.h."
  - key: "8a(d)"
    status: MATCH
    reason: "Schedule D line 8a aggregates long-term Box D transactions using column (d) proceeds when reported in aggregate; the refusal excludes unsupported cases."
  - key: "8a(e)"
    status: MATCH
    reason: "Column (e) uses the reported basis for Box D basis-reported transactions, as required for line 8a."
  - key: "8a(g)"
    status: MATCH
    reason: "Line 8a is limited to no-adjustment aggregate transactions, and the aggregate-route checks make column (g) zero in supported cases."
  - key: "8a(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus adjustments; sales.h computes that same column (h) amount."
  - key: "8b(d)"
    status: MATCH
    reason: "Schedule D line 8b totals Box D detail-reporting transactions, and column (d) is proceeds."
  - key: "8b(e)"
    status: MATCH
    reason: "Column (e) uses the reported basis for Box D transactions, matching the Form 8949 column (e) requirement."
  - key: "8b(g)"
    status: MATCH
    reason: "Column (g) is the Form 8949 adjustment, and sales.g adds the supported basis and wash-sale adjustments."
  - key: "8b(h)"
    status: MATCH
    reason: "Column (h) subtracts column (e) from column (d) and combines column (g), matching sales.h."
  - key: "9(d)"
    status: MATCH
    reason: "Line 9 totals Box E detail-reporting transactions; digital Box K is excluded by refusal, and column (d) is proceeds."
  - key: "9(e)"
    status: MATCH
    reason: "For Box E, basis was not reported, so column (e) uses the correct basis from records."
  - key: "9(g)"
    status: MATCH
    reason: "Column (g) is the Form 8949 adjustment for Box E detail transactions, using supported adjustments."
  - key: "9(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus adjustments, matching sales.h."
  - key: "10(d)"
    status: MATCH
    reason: "Line 10 totals Box F detail-reporting transactions; digital Box L is excluded by refusal, and column (d) is proceeds."
  - key: "10(e)"
    status: MATCH
    reason: "For Box F, no broker basis report applies, so column (e) uses the correct basis from records."
  - key: "10(g)"
    status: MATCH
    reason: "Column (g) is the Form 8949 adjustment for Box F detail transactions, using supported adjustments."
  - key: "10(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus adjustments, matching sales.h."
  - key: "4"
    status: MATCH
    reason: "Line 4 is zero when no other source forms apply; the refusal excludes Forms 6252, 4684, 6781, and 8824."
  - key: "5"
    status: MATCH
    reason: "Line 5 is zero when no Schedule K-1 partnership, S corporation, estate, or trust gains or losses apply; the refusal excludes them."
  - key: "6"
    status: MATCH
    reason: "Line 6 uses the Capital Loss Carryover Worksheet line 8 amount as a short-term loss when applicable, and otherwise zero."
  - key: "11"
    status: MATCH
    reason: "Line 11 is zero when no other source forms apply; the refusal excludes Forms 4797, 2439, 6252, 4684, 6781, and 8824."
  - key: "12"
    status: MATCH
    reason: "Line 12 is zero when no Schedule K-1 long-term gains or losses apply; the refusal excludes those sources."
  - key: "14"
    status: MATCH
    reason: "Line 14 uses the Capital Loss Carryover Worksheet line 13 amount as a long-term loss when applicable, and otherwise zero."
  - key: "13"
    status: MATCH
    reason: "Line 13 is the Form 1099-DIV box 2a capital gain distribution; unsupported distribution cases are refused."
  - key: "7"
    status: MATCH
    reason: "Line 7 combines the Part I column (h) amounts and lines 4 through 6, matching the form instruction to combine lines 1a through 6 in column (h)."
  - key: "15"
    status: MATCH
    reason: "Line 15 combines the Part II column (h) amounts and lines 11 through 14, matching the form instruction to combine lines 8a through 14 in column (h)."
  - key: "16"
    status: MATCH
    reason: "Line 16 combines lines 7 and 15, as the form directs."
  - key: "17"
    status: MATCH
    reason: "Line 17 is true only when both lines 15 and 16 are gains, matching 'Are lines 15 and 16 both gains?'"
  - key: "20"
    status: MATCH
    reason: "Line 20 checks that lines 18 and 19 are zero or blank and that Form 4952 is not being filed."
  - key: "21"
    status: MATCH
    reason: "Line 21 limits a line 16 loss to the annual capital loss limit, using the signed larger-of computation that matches the smaller positive loss."
  - key: "22"
    status: MATCH
    reason: "Line 22 is true when qualified dividends on Form 1040 line 3a are greater than zero."
```
