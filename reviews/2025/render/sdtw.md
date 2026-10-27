# Render comparison — sdtw

The rendered English of every printed line of `Schedule D Tax Worksheet` (`rendered/2025/sdtw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ceca9bfe032cb8ebdb4a5e57d80a85dbe28d0ee11f980b5167ebfa0becab8411 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 9e3683249bf7cfc8d40fec622971518f1ba9ced67cdd534ab8613a5b19645d9b |
| lines judged | 47 |
| match / mismatch / unclear / missing | 46 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 8, 10, 11, 12, 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040gi | 2025; printed date 2026-02-25 | 38, 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f4952 | 2025; created 2025-05-28 | 1, 2, 3, 4 | whole document | efbeec4c44a1e43fb00231942c811a454d86b3632a2a662238893f8c4595bf81 | 3, 4 | c98eb27a83a89faecfdd0cd6597e8063fbd86a14ba1606f3e96c1c5f016d2b5c |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### 1 — Taxable income
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The restatement always takes Form 1040 line 15. The IRS text adds: "However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet". No refusal names Form 2555 as excluded.

Ruling: scope; project retained. i1040sd p. 15, line 1: "Enter your taxable income from Form 1040, 1040-SR, or 1040-NR, line 15. (However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet in the instructions for Form 1040, line 16.)". The Form 2555 alternative is never reached on a return the tool computes: the exclusion is reported on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), refused by s1.line8_other (forms/2025/s1.yaml: "lines 8a, 8d, 8e, 8k to 8q and 8s to 8v are refused by s1.line8_other"); the housing deduction (Schedule 1, line 24j) is refused at Form 1040 line 10 ("lines 24b to 24z are outside this tool"); and a filer who answers that Form 2555 is filed is refused at Schedule 1-A line 2a (forms/2025/s1a.yaml, gate sa.excluded_income, i1040gi p. 101). The worksheet note records Form 2555 as outside scope. The restatement says what the page says for every return the tool computes; as round 2. No change.

### 2 — Qualified dividends
Status: **MATCH**

Model: Qualified dividends from Form 1040 line 3a, as the line says.

### 3 — Form 4952 line 4g election
Status: **MATCH**

Model: This is the amount from Form 4952 line 4g. Refusals exclude carryovers, unsupported items, alternative allocation and invalid elections.

### 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form 4952 is fi
Status: **MATCH**

Model: This is Form 4952 line 4e, or zero when Form 4952 isn't filed. The footnote's dotted-line "Elec." amount is excluded by the alternative-allocation refusal on the line 4g helper.

### 5 — Subtract line 4 from line 3; floor at zero
Status: **MATCH**

Model: Subtract line 4 from line 3, floored at zero, as printed.

### 6 — Subtract line 5 from line 2; floor at zero
Status: **MATCH**

Model: Subtract line 5 from line 2, floored at zero, as printed.

### 7 — Smaller of Schedule D lines 15 and 16
Status: **MATCH**

Model: Smaller of Schedule D line 15 or line 16, as printed.

### 8 — Smaller of lines 3 and 4
Status: **MATCH**

Model: Smaller of line 3 or line 4, as printed.

### 9 — Subtract line 8 from line 7; floor at zero
Status: **MATCH**

Model: Subtract line 8 from line 7, floored at zero, as printed.

### 10 — Add lines 6 and 9
Status: **MATCH**

Model: Add lines 6 and 9, as printed.

### 11 — Add Schedule D lines 18 and 19
Status: **MATCH**

Model: Adds Schedule D lines 18 and 19. Those lines are zero when Schedule D line 17 is No, consistent with Schedule D's skip instruction.

### 12 — Smaller of lines 9 and 11
Status: **MATCH**

Model: Smaller of line 9 or line 11, as printed.

### 13 — Subtract line 12 from line 10
Status: **MATCH**

Model: Subtract line 12 from line 10, as printed.

### 14 — Subtract line 13 from line 1; floor at zero
Status: **MATCH**

Model: Subtract line 13 from line 1, floored at zero, as printed.

### 15 — Zero-rate ceiling by filing status
Status: **MATCH**

Model: Uses $48,350 for single and MFS, $96,700 for MFJ and QSS, and $64,750 for HOH. These match the printed amounts.

### 16 — Smaller of lines 1 and 15
Status: **MATCH**

Model: Smaller of line 1 or line 15, as printed.

### 17 — Smaller of lines 14 and 16
Status: **MATCH**

Model: Smaller of line 14 or line 16, as printed.

### 18 — Subtract line 10 from line 1; floor at zero
Status: **MATCH**

Model: Subtract line 10 from line 1, floored at zero, as printed.

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **MATCH**

Model: Smaller of line 1 or the ceiling: $197,300 for single, MFS and HOH, and $394,600 for MFJ and QSS. These match the printed amounts.

### 20 — Smaller of lines 14 and 19
Status: **MATCH**

Model: Smaller of line 14 or line 19, as printed.

### 21 — Larger of lines 18 and 20
Status: **MATCH**

Model: Larger of line 18 or line 20, as printed.

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **MATCH**

Model: Subtract line 17 from line 16, as printed.

### 23 — Smaller of lines 1 and 13
Status: **MATCH**

Model: Smaller of line 1 or line 13, zero when lines 1 and 16 are the same. This matches "If lines 1 and 16 are the same, skip lines 23 through 43".

### 24 — Amount from line 22
Status: **MATCH**

Model: Amount from line 22, zero when skipped, as printed.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **MATCH**

Model: Subtract line 24 from line 23, floored at zero, under the line 22 skip rule.

### 26 — 15-percent ceiling by filing status
Status: **MATCH**

Model: Uses $533,400 for single, $300,000 for MFS, $600,050 for MFJ and QSS, and $566,700 for HOH. These match the printed amounts.

### 27 — Smaller of lines 1 and 26
Status: **MATCH**

Model: Smaller of line 1 or line 26, under the skip rule.

### 28 — Add lines 21 and 22
Status: **MATCH**

Model: Add lines 21 and 22, under the skip rule.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **MATCH**

Model: Subtract line 28 from line 27, floored at zero, under the skip rule.

### 30 — Smaller of lines 25 and 29
Status: **MATCH**

Model: Smaller of line 25 or line 29, under the skip rule.

### 31 — Multiply line 30 by 15 percent
Status: **MATCH**

Model: Line 30 times 15%, as printed.

### 32 — Add lines 24 and 30
Status: **MATCH**

Model: Add lines 24 and 30, under the skip rule.

### 33 — Subtract line 32 from line 23
Status: **MATCH**

Model: Subtract line 32 from line 23. The line is zero when lines 1 and 32 are the same, or when the earlier skip applied.

### 34 — Multiply line 33 by 20 percent
Status: **MATCH**

Model: Line 33 times 20%, under the same skip rule.

### 35 — Smaller of line 9 and Schedule D line 19
Status: **MATCH**

Model: Smaller of line 9 or Schedule D line 19. Lines 35–40 are skipped when Schedule D line 19 is zero, as printed.

### 36 — Add lines 10 and 21
Status: **MATCH**

Model: Add lines 10 and 21, under the line 19 skip rule.

### 37 — Amount from line 1
Status: **MATCH**

Model: Amount from line 1, under the skip rule.

### 38 — Subtract line 37 from line 36; floor at zero
Status: **MATCH**

Model: Subtract line 37 from line 36, floored at zero, under the skip rule.

### 39 — Subtract line 38 from line 35; floor at zero
Status: **MATCH**

Model: Subtract line 38 from line 35, floored at zero, under the skip rule.

### 40 — Multiply line 39 by 25 percent
Status: **MATCH**

Model: Line 39 times 25%, under the skip rule.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **MATCH**

Model: Add lines 21, 22, 30, 33 and 39, reported only when Schedule D line 18 is more than zero. The gate also computes this line when line 19 is zero, but there line 42 works out to zero, so the result matches the printed skip rule.

### 42 — Subtract line 41 from line 1
Status: **MATCH**

Model: Subtract line 41 from line 1, under the line 18 skip rule.

### 43 — Multiply line 42 by 28 percent
Status: **MATCH**

Model: Line 42 times 28%, under the line 18 skip rule.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Tax on line 21: the Tax Table below $100,000, otherwise the Tax Computation Worksheet, as printed.

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **MATCH**

Model: Add lines 31, 34, 40, 43 and 44, as printed.

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Tax on line 1: the Tax Table below $100,000, otherwise the Tax Computation Worksheet, as printed.

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **MATCH**

Model: Smaller of line 45 or line 46, as printed.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always takes Form 1040 line 15. The IRS text adds: \"However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet\". No refusal names Form 2555 as excluded."
  - key: "2"
    status: MATCH
    reason: "Qualified dividends from Form 1040 line 3a, as the line says."
  - key: "3"
    status: MATCH
    reason: "This is the amount from Form 4952 line 4g. Refusals exclude carryovers, unsupported items, alternative allocation and invalid elections."
  - key: "4"
    status: MATCH
    reason: "This is Form 4952 line 4e, or zero when Form 4952 isn't filed. The footnote's dotted-line \"Elec.\" amount is excluded by the alternative-allocation refusal on the line 4g helper."
  - key: "5"
    status: MATCH
    reason: "Subtract line 4 from line 3, floored at zero, as printed."
  - key: "6"
    status: MATCH
    reason: "Subtract line 5 from line 2, floored at zero, as printed."
  - key: "7"
    status: MATCH
    reason: "Smaller of Schedule D line 15 or line 16, as printed."
  - key: "8"
    status: MATCH
    reason: "Smaller of line 3 or line 4, as printed."
  - key: "9"
    status: MATCH
    reason: "Subtract line 8 from line 7, floored at zero, as printed."
  - key: "10"
    status: MATCH
    reason: "Add lines 6 and 9, as printed."
  - key: "11"
    status: MATCH
    reason: "Adds Schedule D lines 18 and 19. Those lines are zero when Schedule D line 17 is No, consistent with Schedule D's skip instruction."
  - key: "12"
    status: MATCH
    reason: "Smaller of line 9 or line 11, as printed."
  - key: "13"
    status: MATCH
    reason: "Subtract line 12 from line 10, as printed."
  - key: "14"
    status: MATCH
    reason: "Subtract line 13 from line 1, floored at zero, as printed."
  - key: "15"
    status: MATCH
    reason: "Uses $48,350 for single and MFS, $96,700 for MFJ and QSS, and $64,750 for HOH. These match the printed amounts."
  - key: "16"
    status: MATCH
    reason: "Smaller of line 1 or line 15, as printed."
  - key: "17"
    status: MATCH
    reason: "Smaller of line 14 or line 16, as printed."
  - key: "18"
    status: MATCH
    reason: "Subtract line 10 from line 1, floored at zero, as printed."
  - key: "19"
    status: MATCH
    reason: "Smaller of line 1 or the ceiling: $197,300 for single, MFS and HOH, and $394,600 for MFJ and QSS. These match the printed amounts."
  - key: "20"
    status: MATCH
    reason: "Smaller of line 14 or line 19, as printed."
  - key: "21"
    status: MATCH
    reason: "Larger of line 18 or line 20, as printed."
  - key: "22"
    status: MATCH
    reason: "Subtract line 17 from line 16, as printed."
  - key: "23"
    status: MATCH
    reason: "Smaller of line 1 or line 13, zero when lines 1 and 16 are the same. This matches \"If lines 1 and 16 are the same, skip lines 23 through 43\"."
  - key: "24"
    status: MATCH
    reason: "Amount from line 22, zero when skipped, as printed."
  - key: "25"
    status: MATCH
    reason: "Subtract line 24 from line 23, floored at zero, under the line 22 skip rule."
  - key: "26"
    status: MATCH
    reason: "Uses $533,400 for single, $300,000 for MFS, $600,050 for MFJ and QSS, and $566,700 for HOH. These match the printed amounts."
  - key: "27"
    status: MATCH
    reason: "Smaller of line 1 or line 26, under the skip rule."
  - key: "28"
    status: MATCH
    reason: "Add lines 21 and 22, under the skip rule."
  - key: "29"
    status: MATCH
    reason: "Subtract line 28 from line 27, floored at zero, under the skip rule."
  - key: "30"
    status: MATCH
    reason: "Smaller of line 25 or line 29, under the skip rule."
  - key: "31"
    status: MATCH
    reason: "Line 30 times 15%, as printed."
  - key: "32"
    status: MATCH
    reason: "Add lines 24 and 30, under the skip rule."
  - key: "33"
    status: MATCH
    reason: "Subtract line 32 from line 23. The line is zero when lines 1 and 32 are the same, or when the earlier skip applied."
  - key: "34"
    status: MATCH
    reason: "Line 33 times 20%, under the same skip rule."
  - key: "35"
    status: MATCH
    reason: "Smaller of line 9 or Schedule D line 19. Lines 35–40 are skipped when Schedule D line 19 is zero, as printed."
  - key: "36"
    status: MATCH
    reason: "Add lines 10 and 21, under the line 19 skip rule."
  - key: "37"
    status: MATCH
    reason: "Amount from line 1, under the skip rule."
  - key: "38"
    status: MATCH
    reason: "Subtract line 37 from line 36, floored at zero, under the skip rule."
  - key: "39"
    status: MATCH
    reason: "Subtract line 38 from line 35, floored at zero, under the skip rule."
  - key: "40"
    status: MATCH
    reason: "Line 39 times 25%, under the skip rule."
  - key: "41"
    status: MATCH
    reason: "Add lines 21, 22, 30, 33 and 39, reported only when Schedule D line 18 is more than zero. The gate also computes this line when line 19 is zero, but there line 42 works out to zero, so the result matches the printed skip rule."
  - key: "42"
    status: MATCH
    reason: "Subtract line 41 from line 1, under the line 18 skip rule."
  - key: "43"
    status: MATCH
    reason: "Line 42 times 28%, under the line 18 skip rule."
  - key: "44"
    status: MATCH
    reason: "Tax on line 21: the Tax Table below $100,000, otherwise the Tax Computation Worksheet, as printed."
  - key: "45"
    status: MATCH
    reason: "Add lines 31, 34, 40, 43 and 44, as printed."
  - key: "46"
    status: MATCH
    reason: "Tax on line 1: the Tax Table below $100,000, otherwise the Tax Computation Worksheet, as printed."
  - key: "47"
    status: MATCH
    reason: "Smaller of line 45 or line 46, as printed."
```
```
