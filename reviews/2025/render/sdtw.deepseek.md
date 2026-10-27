# Render comparison — sdtw

The rendered English of every printed line of `Schedule D Tax Worksheet` (`rendered/2025/sdtw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | ceca9bfe032cb8ebdb4a5e57d80a85dbe28d0ee11f980b5167ebfa0becab8411 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: IRS line 1 says to enter line 3 of the Foreign Earned Income Tax Worksheet instead when filing Form 2555; the restatement always uses Form 1040 line 15.

Ruling: scope; project retained. i1040sd p. 15, line 1: "Enter your taxable income from Form 1040, 1040-SR, or 1040-NR, line 15. (However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet in the instructions for Form 1040, line 16.)". The Form 2555 alternative is never reached on a return the tool computes: the exclusion is reported on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), refused by s1.line8_other (forms/2025/s1.yaml: "lines 8a, 8d, 8e, 8k to 8q and 8s to 8v are refused by s1.line8_other"); the housing deduction (Schedule 1, line 24j) is refused at Form 1040 line 10 ("lines 24b to 24z are outside this tool"); and a filer who answers that Form 2555 is filed is refused at Schedule 1-A line 2a (forms/2025/s1a.yaml, gate sa.excluded_income, i1040gi p. 101). The worksheet note records Form 2555 as outside scope. The restatement says what the page says for every return the tool computes; as round 2. No change.

### 2 — Qualified dividends
Status: **MATCH**

Model: Restatement matches IRS line 2.

### 3 — Form 4952 line 4g election
Status: **MATCH**

Model: Restatement matches IRS line 3.

### 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form 4952 is fi
Status: **MATCH**

Model: Restatement matches IRS line 4 within the supported non-alternative-allocation cases.

### 5 — Subtract line 4 from line 3; floor at zero
Status: **MATCH**

Model: Restatement matches IRS line 5.

### 6 — Subtract line 5 from line 2; floor at zero
Status: **MATCH**

Model: Restatement matches the main computation on IRS line 6.

### 7 — Smaller of Schedule D lines 15 and 16
Status: **MATCH**

Model: Restatement matches IRS line 7.

### 8 — Smaller of lines 3 and 4
Status: **MATCH**

Model: Restatement matches IRS line 8.

### 9 — Subtract line 8 from line 7; floor at zero
Status: **MATCH**

Model: Restatement matches IRS line 9.

### 10 — Add lines 6 and 9
Status: **MATCH**

Model: Restatement matches IRS line 10.

### 11 — Add Schedule D lines 18 and 19
Status: **MATCH**

Model: Restatement matches IRS line 11.

### 12 — Smaller of lines 9 and 11
Status: **MATCH**

Model: Restatement matches IRS line 12.

### 13 — Subtract line 12 from line 10
Status: **MATCH**

Model: Restatement matches IRS line 13.

### 14 — Subtract line 13 from line 1; floor at zero
Status: **MATCH**

Model: Restatement matches IRS line 14.

### 15 — Zero-rate ceiling by filing status
Status: **MATCH**

Model: Restatement matches IRS line 15 thresholds.

### 16 — Smaller of lines 1 and 15
Status: **MATCH**

Model: Restatement matches IRS line 16.

### 17 — Smaller of lines 14 and 16
Status: **MATCH**

Model: Restatement matches IRS line 17.

### 18 — Subtract line 10 from line 1; floor at zero
Status: **MATCH**

Model: Restatement matches IRS line 18.

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **MATCH**

Model: Restatement matches IRS line 19 thresholds.

### 20 — Smaller of lines 14 and 19
Status: **MATCH**

Model: Restatement matches IRS line 20.

### 21 — Larger of lines 18 and 20
Status: **MATCH**

Model: Restatement matches IRS line 21.

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **MATCH**

Model: Restatement matches IRS line 22.

### 23 — Smaller of lines 1 and 13
Status: **MATCH**

Model: Restatement matches IRS line 23 and its skip rule.

### 24 — Amount from line 22
Status: **MATCH**

Model: Restatement matches IRS line 24 and its skip rule.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **MATCH**

Model: Restatement matches IRS line 25.

### 26 — 15-percent ceiling by filing status
Status: **MATCH**

Model: Restatement matches IRS line 26 thresholds.

### 27 — Smaller of lines 1 and 26
Status: **MATCH**

Model: Restatement matches IRS line 27.

### 28 — Add lines 21 and 22
Status: **MATCH**

Model: Restatement matches IRS line 28.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **MATCH**

Model: Restatement matches IRS line 29.

### 30 — Smaller of lines 25 and 29
Status: **MATCH**

Model: Restatement matches IRS line 30.

### 31 — Multiply line 30 by 15 percent
Status: **MATCH**

Model: Restatement matches IRS line 31.

### 32 — Add lines 24 and 30
Status: **MATCH**

Model: Restatement matches IRS line 32.

### 33 — Subtract line 32 from line 23
Status: **MATCH**

Model: Restatement matches IRS line 33 and its skip rule.

### 34 — Multiply line 33 by 20 percent
Status: **MATCH**

Model: Restatement matches IRS line 34.

### 35 — Smaller of line 9 and Schedule D line 19
Status: **MATCH**

Model: Restatement matches IRS line 35 and its skip rule.

### 36 — Add lines 10 and 21
Status: **MATCH**

Model: Restatement matches IRS line 36.

### 37 — Amount from line 1
Status: **MATCH**

Model: Restatement matches IRS line 37.

### 38 — Subtract line 37 from line 36; floor at zero
Status: **MATCH**

Model: Restatement matches IRS line 38.

### 39 — Subtract line 38 from line 35; floor at zero
Status: **MATCH**

Model: Restatement matches IRS line 39.

### 40 — Multiply line 39 by 25 percent
Status: **MATCH**

Model: Restatement matches IRS line 40.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **MATCH**

Model: Restatement matches IRS line 41 and its Schedule D line 18 reporting gate.

### 42 — Subtract line 41 from line 1
Status: **MATCH**

Model: Restatement matches IRS line 42.

### 43 — Multiply line 42 by 28 percent
Status: **MATCH**

Model: Restatement matches IRS line 43.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Restatement matches IRS line 44.

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **MATCH**

Model: Restatement matches IRS line 45.

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Restatement matches IRS line 46.

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **MATCH**

Model: Restatement matches IRS line 47.

## Raw response

```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "IRS line 1 says to enter line 3 of the Foreign Earned Income Tax Worksheet instead when filing Form 2555; the restatement always uses Form 1040 line 15."
  - key: "2"
    status: MATCH
    reason: "Restatement matches IRS line 2."
  - key: "3"
    status: MATCH
    reason: "Restatement matches IRS line 3."
  - key: "4"
    status: MATCH
    reason: "Restatement matches IRS line 4 within the supported non-alternative-allocation cases."
  - key: "5"
    status: MATCH
    reason: "Restatement matches IRS line 5."
  - key: "6"
    status: MATCH
    reason: "Restatement matches the main computation on IRS line 6."
  - key: "7"
    status: MATCH
    reason: "Restatement matches IRS line 7."
  - key: "8"
    status: MATCH
    reason: "Restatement matches IRS line 8."
  - key: "9"
    status: MATCH
    reason: "Restatement matches IRS line 9."
  - key: "10"
    status: MATCH
    reason: "Restatement matches IRS line 10."
  - key: "11"
    status: MATCH
    reason: "Restatement matches IRS line 11."
  - key: "12"
    status: MATCH
    reason: "Restatement matches IRS line 12."
  - key: "13"
    status: MATCH
    reason: "Restatement matches IRS line 13."
  - key: "14"
    status: MATCH
    reason: "Restatement matches IRS line 14."
  - key: "15"
    status: MATCH
    reason: "Restatement matches IRS line 15 thresholds."
  - key: "16"
    status: MATCH
    reason: "Restatement matches IRS line 16."
  - key: "17"
    status: MATCH
    reason: "Restatement matches IRS line 17."
  - key: "18"
    status: MATCH
    reason: "Restatement matches IRS line 18."
  - key: "19"
    status: MATCH
    reason: "Restatement matches IRS line 19 thresholds."
  - key: "20"
    status: MATCH
    reason: "Restatement matches IRS line 20."
  - key: "21"
    status: MATCH
    reason: "Restatement matches IRS line 21."
  - key: "22"
    status: MATCH
    reason: "Restatement matches IRS line 22."
  - key: "23"
    status: MATCH
    reason: "Restatement matches IRS line 23 and its skip rule."
  - key: "24"
    status: MATCH
    reason: "Restatement matches IRS line 24 and its skip rule."
  - key: "25"
    status: MATCH
    reason: "Restatement matches IRS line 25."
  - key: "26"
    status: MATCH
    reason: "Restatement matches IRS line 26 thresholds."
  - key: "27"
    status: MATCH
    reason: "Restatement matches IRS line 27."
  - key: "28"
    status: MATCH
    reason: "Restatement matches IRS line 28."
  - key: "29"
    status: MATCH
    reason: "Restatement matches IRS line 29."
  - key: "30"
    status: MATCH
    reason: "Restatement matches IRS line 30."
  - key: "31"
    status: MATCH
    reason: "Restatement matches IRS line 31."
  - key: "32"
    status: MATCH
    reason: "Restatement matches IRS line 32."
  - key: "33"
    status: MATCH
    reason: "Restatement matches IRS line 33 and its skip rule."
  - key: "34"
    status: MATCH
    reason: "Restatement matches IRS line 34."
  - key: "35"
    status: MATCH
    reason: "Restatement matches IRS line 35 and its skip rule."
  - key: "36"
    status: MATCH
    reason: "Restatement matches IRS line 36."
  - key: "37"
    status: MATCH
    reason: "Restatement matches IRS line 37."
  - key: "38"
    status: MATCH
    reason: "Restatement matches IRS line 38."
  - key: "39"
    status: MATCH
    reason: "Restatement matches IRS line 39."
  - key: "40"
    status: MATCH
    reason: "Restatement matches IRS line 40."
  - key: "41"
    status: MATCH
    reason: "Restatement matches IRS line 41 and its Schedule D line 18 reporting gate."
  - key: "42"
    status: MATCH
    reason: "Restatement matches IRS line 42."
  - key: "43"
    status: MATCH
    reason: "Restatement matches IRS line 43."
  - key: "44"
    status: MATCH
    reason: "Restatement matches IRS line 44."
  - key: "45"
    status: MATCH
    reason: "Restatement matches IRS line 45."
  - key: "46"
    status: MATCH
    reason: "Restatement matches IRS line 46."
  - key: "47"
    status: MATCH
    reason: "Restatement matches IRS line 47."
```
