# Render comparison — qdcg

The rendered English of every printed line of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` (`rendered/2025/qdcg.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a99d5e2826bea59f347ef89ae1b8487ae4d6b5332184e93a5c8ec754c090f3ca |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 3e091415e4286dc3d5ff5b10d6e690d7b0e4e6fbd7bd377c50f4d9e1e5bc9b32 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 24 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 36, 38, 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31, 36 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sd | 2025; printed date 2025-12-11 | 8, 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| p550 | 2025 returns; printed date 2026-03-05 | 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The restatement always uses Form 1040 line 15 and has no refusal for Form 2555 filers. The IRS text adds: "However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet."

Ruling: scope; project retained. The Foreign Earned Income Tax Worksheet applies only to a filer who claims the foreign earned income or housing exclusion or the housing deduction on Form 2555 (i1040gi p. 36, Line 16), reported on Schedule 1 line 8d, which s1.line8_other refuses. Same reading as the earlier rounds.

### 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **MATCH**

Model: Both enter the amount from Form 1040 line 3a. The asterisk footnote only concerns Form 2555 filers.

### 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If
Status: **MATCH**

Model: Yes branch: the smaller of Schedule D lines 15 and 16, floored at zero, matches "If either line 15 or line 16 is blank or a loss, enter -0-." No branch: without Schedule D, Form 1040 line 7a holds only capital gain distributions (1099-DIV box 2a), so the value is the same.

### 4 — Add lines 2 and 3
Status: **MATCH**

Model: Both add lines 2 and 3.

### 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **MATCH**

Model: Both subtract line 4 from line 1 and enter -0- if the result is zero or less.

### 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly o
Status: **MATCH**

Model: The amounts match the IRS text: $48,350 for single or MFS, $96,700 for MFJ or QSS, and $64,750 for HOH.

### 7 — Enter the smaller of line 1 or line 6
Status: **MATCH**

Model: Both take the smaller of line 1 or line 6.

### 8 — Enter the smaller of line 5 or line 7
Status: **MATCH**

Model: Both take the smaller of line 5 or line 7.

### 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **MATCH**

Model: Both subtract line 8 from line 7.

### 10 — Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: Both take the smaller of line 1 or line 4.

### 11 — Enter the amount from line 9
Status: **MATCH**

Model: Both enter the amount from line 9.

### 12 — Subtract line 11 from line 10
Status: **MATCH**

Model: Both subtract line 11 from line 10.

### 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married fili
Status: **MATCH**

Model: The amounts match the IRS text: $533,400 single, $300,000 MFS, $600,050 MFJ or QSS, and $566,700 HOH.

### 14 — Enter the smaller of line 1 or line 13
Status: **MATCH**

Model: Both take the smaller of line 1 or line 13.

### 15 — Add lines 5 and 9
Status: **MATCH**

Model: Both add lines 5 and 9.

### 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **MATCH**

Model: Both subtract line 15 from line 14 and enter -0- if the result is zero or less.

### 17 — Enter the smaller of line 12 or line 16
Status: **MATCH**

Model: Both take the smaller of line 12 or line 16.

### 18 — Multiply line 17 by 15% (0.15)
Status: **MATCH**

Model: Both multiply line 17 by 15% (0.15).

### 19 — Add lines 9 and 17
Status: **MATCH**

Model: Both add lines 9 and 17.

### 20 — Subtract line 19 from line 10
Status: **MATCH**

Model: Both subtract line 19 from line 10.

### 21 — Multiply line 20 by 20% (0.20)
Status: **MATCH**

Model: Both multiply line 20 by 20% (0.20).

### 22 — Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use
Status: **MATCH**

Model: Both figure the tax on line 5: Tax Table below $100,000, Tax Computation Worksheet at $100,000 or more. The worksheet brackets, rates and subtraction amounts for every filing status match the 2025 Tax Computation Worksheet.

### 23 — Add lines 18, 21, and 22
Status: **MATCH**

Model: Both add lines 18, 21 and 22.

### 24 — Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use
Status: **MATCH**

Model: Both figure the tax on line 1 the same way: Tax Table below $100,000, Tax Computation Worksheet at $100,000 or more.

### 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amou
Status: **MATCH**

Model: Both enter the smaller of line 23 or line 24. The IRS's different destination for Form 2555 filers does not change the value.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always uses Form 1040 line 15 and has no refusal for Form 2555 filers. The IRS text adds: \"However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet.\""
  - key: "2"
    status: MATCH
    reason: "Both enter the amount from Form 1040 line 3a. The asterisk footnote only concerns Form 2555 filers."
  - key: "3"
    status: MATCH
    reason: "Yes branch: the smaller of Schedule D lines 15 and 16, floored at zero, matches \"If either line 15 or line 16 is blank or a loss, enter -0-.\" No branch: without Schedule D, Form 1040 line 7a holds only capital gain distributions (1099-DIV box 2a), so the value is the same."
  - key: "4"
    status: MATCH
    reason: "Both add lines 2 and 3."
  - key: "5"
    status: MATCH
    reason: "Both subtract line 4 from line 1 and enter -0- if the result is zero or less."
  - key: "6"
    status: MATCH
    reason: "The amounts match the IRS text: $48,350 for single or MFS, $96,700 for MFJ or QSS, and $64,750 for HOH."
  - key: "7"
    status: MATCH
    reason: "Both take the smaller of line 1 or line 6."
  - key: "8"
    status: MATCH
    reason: "Both take the smaller of line 5 or line 7."
  - key: "9"
    status: MATCH
    reason: "Both subtract line 8 from line 7."
  - key: "10"
    status: MATCH
    reason: "Both take the smaller of line 1 or line 4."
  - key: "11"
    status: MATCH
    reason: "Both enter the amount from line 9."
  - key: "12"
    status: MATCH
    reason: "Both subtract line 11 from line 10."
  - key: "13"
    status: MATCH
    reason: "The amounts match the IRS text: $533,400 single, $300,000 MFS, $600,050 MFJ or QSS, and $566,700 HOH."
  - key: "14"
    status: MATCH
    reason: "Both take the smaller of line 1 or line 13."
  - key: "15"
    status: MATCH
    reason: "Both add lines 5 and 9."
  - key: "16"
    status: MATCH
    reason: "Both subtract line 15 from line 14 and enter -0- if the result is zero or less."
  - key: "17"
    status: MATCH
    reason: "Both take the smaller of line 12 or line 16."
  - key: "18"
    status: MATCH
    reason: "Both multiply line 17 by 15% (0.15)."
  - key: "19"
    status: MATCH
    reason: "Both add lines 9 and 17."
  - key: "20"
    status: MATCH
    reason: "Both subtract line 19 from line 10."
  - key: "21"
    status: MATCH
    reason: "Both multiply line 20 by 20% (0.20)."
  - key: "22"
    status: MATCH
    reason: "Both figure the tax on line 5: Tax Table below $100,000, Tax Computation Worksheet at $100,000 or more. The worksheet brackets, rates and subtraction amounts for every filing status match the 2025 Tax Computation Worksheet."
  - key: "23"
    status: MATCH
    reason: "Both add lines 18, 21 and 22."
  - key: "24"
    status: MATCH
    reason: "Both figure the tax on line 1 the same way: Tax Table below $100,000, Tax Computation Worksheet at $100,000 or more."
  - key: "25"
    status: MATCH
    reason: "Both enter the smaller of line 23 or line 24. The IRS's different destination for Form 2555 filers does not change the value."
```
```
