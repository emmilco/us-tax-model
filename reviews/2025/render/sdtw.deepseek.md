# Render comparison — sdtw

The rendered English of every printed line of `Schedule D Tax Worksheet` (`rendered/2025/sdtw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 6da767a03fe77d301804d09a439c14fde61f644fb0fd75be8d1cf1504cace513 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | ad5dbe41f9378e5dbc65094fa635d34acd196f617c0b876328f6fc9e6d4fa2ae |
| lines judged | 47 |
| match / mismatch / unclear / missing | 42 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | - | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Taxable income
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The IRS line adds a Form 2555 alternative: 'if you are filing Form 2555 ... enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet'; the restatement always uses Form 1040 line 15.

Ruling: open

### 2 — Qualified dividends
Status: **MATCH**

Model: Matches the IRS line: qualified dividends from Form 1040 line 3a.

### 3 — Form 4952 line 4g election
Status: **MATCH**

Model: Matches Form 4952 line 4g through the supplied helper, with Form 4952 refusals narrowing unsupported cases.

### 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **MISMATCH**

Restated: Enter the amount from f4952 line 4e.

Model: The IRS footnote says 'If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952'; the restatement always uses line 4e.

Ruling: open

### 5 — Subtract line 4 from line 3; floor at zero
Status: **MATCH**

Model: Matches the IRS subtraction and zero floor.

### 6 — Subtract line 5 from line 2; floor at zero
Status: **MATCH**

Model: Matches the IRS subtraction and zero floor.

### 7 — Smaller of Schedule D lines 15 and 16
Status: **MATCH**

Model: Matches the smaller of Schedule D line 15 or line 16.

### 8 — Smaller of lines 3 and 4
Status: **MATCH**

Model: Matches the smaller of line 3 or line 4.

### 9 — Subtract line 8 from line 7; floor at zero
Status: **MATCH**

Model: Matches the IRS subtraction and zero floor.

### 10 — Add lines 6 and 9
Status: **MATCH**

Model: Matches adding lines 6 and 9.

### 11 — Add Schedule D lines 18 and 19
Status: **MATCH**

Model: Matches adding Schedule D lines 18 and 19, represented by the 28% rate gain and unrecaptured section 1250 gain worksheet results.

### 12 — Smaller of lines 9 and 11
Status: **MATCH**

Model: Matches the smaller of line 9 or line 11.

### 13 — Subtract line 12 from line 10
Status: **MATCH**

Model: Matches subtracting line 12 from line 10.

### 14 — Subtract line 13 from line 1; floor at zero
Status: **MATCH**

Model: Matches subtracting line 13 from line 1 with a zero floor.

### 15 — Zero-rate ceiling by filing status
Status: **MATCH**

Model: Matches the IRS zero-rate ceiling amounts for all filing statuses.

### 16 — Smaller of lines 1 and 15
Status: **MATCH**

Model: Matches the smaller of line 1 or line 15.

### 17 — Smaller of lines 14 and 16
Status: **MATCH**

Model: Matches the smaller of line 14 or line 16.

### 18 — Subtract line 10 from line 1; floor at zero
Status: **MATCH**

Model: Matches subtracting line 10 from line 1 with a zero floor.

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **MATCH**

Model: Matches the IRS ordinary-income ceiling amounts for all filing statuses.

### 20 — Smaller of lines 14 and 19
Status: **MATCH**

Model: Matches the smaller of line 14 or line 19.

### 21 — Larger of lines 18 and 20
Status: **MATCH**

Model: Matches the larger of line 18 or line 20.

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **MATCH**

Model: Matches subtracting line 17 from line 16.

### 23 — Smaller of lines 1 and 13
Status: **MATCH**

Model: Matches the smaller of line 1 or line 13 when the worksheet continues.

### 24 — Amount from line 22
Status: **MATCH**

Model: Matches entering the amount from line 22.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **MATCH**

Model: Matches subtracting line 24 from line 23 with a zero floor.

### 26 — 15-percent ceiling by filing status
Status: **MATCH**

Model: Matches the IRS 15-percent ceiling amounts for all filing statuses.

### 27 — Smaller of lines 1 and 26
Status: **MATCH**

Model: Matches the smaller of line 1 or line 26.

### 28 — Add lines 21 and 22
Status: **MATCH**

Model: Matches adding lines 21 and 22.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **MATCH**

Model: Matches subtracting line 28 from line 27 with a zero floor.

### 30 — Smaller of lines 25 and 29
Status: **MATCH**

Model: Matches the smaller of line 25 or line 29.

### 31 — Multiply line 30 by 15 percent
Status: **MATCH**

Model: Matches multiplying line 30 by 15%.

### 32 — Add lines 24 and 30
Status: **MATCH**

Model: Matches adding lines 24 and 30.

### 33 — Subtract line 32 from line 23
Status: **MATCH**

Model: Matches subtracting line 32 from line 23 when the worksheet continues.

### 34 — Multiply line 33 by 20 percent
Status: **MATCH**

Model: Matches multiplying line 33 by 20%.

### 35 — Smaller of line 9 and Schedule D line 19
Status: **MATCH**

Model: Matches the smaller of line 9 and Schedule D line 19, represented by the unrecaptured section 1250 gain helper.

### 36 — Add lines 10 and 21
Status: **MATCH**

Model: Matches adding lines 10 and 21.

### 37 — Amount from line 1
Status: **MATCH**

Model: Matches entering the amount from line 1.

### 38 — Subtract line 37 from line 36; floor at zero
Status: **MATCH**

Model: Matches subtracting line 37 from line 36 with a zero floor.

### 39 — Subtract line 38 from line 35; floor at zero
Status: **MATCH**

Model: Matches subtracting line 38 from line 35 with a zero floor.

### 40 — Multiply line 39 by 25 percent
Status: **MATCH**

Model: Matches multiplying line 39 by 25%.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **MISMATCH**

Restated: Choose — [helper "Follow printed flow to lines 41–43" = true → helper "Add lines 21, 22, 30, 33 and 39 before skip rule"] [helper "Follow printed flow to lines 41–43" = false → helper "Zero for skipped worksheet lines"]

Model: The IRS says 'If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44.' The gate also computes lines 41-43 when line 19 is zero even if line 18 is zero.

Ruling: open

### 42 — Subtract line 41 from line 1
Status: **MISMATCH**

Restated: Choose — [helper "Follow printed flow to lines 41–43" = true → helper "Subtract line 41 from line 1 before skip rule"] [helper "Follow printed flow to lines 41–43" = false → helper "Zero for skipped worksheet lines"]

Model: Same gate error as line 41: the IRS skips lines 41 through 43 when Schedule D line 18 is zero or blank, but the restatement computes when line 19 is zero even if line 18 is zero.

Ruling: open

### 43 — Multiply line 42 by 28 percent
Status: **MISMATCH**

Restated: Choose — [helper "Follow printed flow to lines 41–43" = true → helper "Multiply line 42 by 28 percent before skip rule"] [helper "Follow printed flow to lines 41–43" = false → helper "Zero for skipped worksheet lines"]

Model: Same gate error as line 41: the IRS skips lines 41 through 43 when Schedule D line 18 is zero or blank, but the restatement computes when line 19 is zero even if line 18 is zero.

Ruling: open

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Matches the IRS instruction to use the Tax Table below $100,000 and the Tax Computation Worksheet at $100,000 or more for line 21.

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **MATCH**

Model: Matches adding lines 31, 34, 40, 43, and 44.

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Matches the IRS instruction to use the Tax Table below $100,000 and the Tax Computation Worksheet at $100,000 or more for line 1.

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **MATCH**

Model: Matches entering the smaller of line 45 or line 46.

## Raw response

```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The IRS line adds a Form 2555 alternative: 'if you are filing Form 2555 ... enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet'; the restatement always uses Form 1040 line 15."
  - key: "2"
    status: MATCH
    reason: "Matches the IRS line: qualified dividends from Form 1040 line 3a."
  - key: "3"
    status: MATCH
    reason: "Matches Form 4952 line 4g through the supplied helper, with Form 4952 refusals narrowing unsupported cases."
  - key: "4"
    status: MISMATCH
    reason: "The IRS footnote says 'If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952'; the restatement always uses line 4e."
  - key: "5"
    status: MATCH
    reason: "Matches the IRS subtraction and zero floor."
  - key: "6"
    status: MATCH
    reason: "Matches the IRS subtraction and zero floor."
  - key: "7"
    status: MATCH
    reason: "Matches the smaller of Schedule D line 15 or line 16."
  - key: "8"
    status: MATCH
    reason: "Matches the smaller of line 3 or line 4."
  - key: "9"
    status: MATCH
    reason: "Matches the IRS subtraction and zero floor."
  - key: "10"
    status: MATCH
    reason: "Matches adding lines 6 and 9."
  - key: "11"
    status: MATCH
    reason: "Matches adding Schedule D lines 18 and 19, represented by the 28% rate gain and unrecaptured section 1250 gain worksheet results."
  - key: "12"
    status: MATCH
    reason: "Matches the smaller of line 9 or line 11."
  - key: "13"
    status: MATCH
    reason: "Matches subtracting line 12 from line 10."
  - key: "14"
    status: MATCH
    reason: "Matches subtracting line 13 from line 1 with a zero floor."
  - key: "15"
    status: MATCH
    reason: "Matches the IRS zero-rate ceiling amounts for all filing statuses."
  - key: "16"
    status: MATCH
    reason: "Matches the smaller of line 1 or line 15."
  - key: "17"
    status: MATCH
    reason: "Matches the smaller of line 14 or line 16."
  - key: "18"
    status: MATCH
    reason: "Matches subtracting line 10 from line 1 with a zero floor."
  - key: "19"
    status: MATCH
    reason: "Matches the IRS ordinary-income ceiling amounts for all filing statuses."
  - key: "20"
    status: MATCH
    reason: "Matches the smaller of line 14 or line 19."
  - key: "21"
    status: MATCH
    reason: "Matches the larger of line 18 or line 20."
  - key: "22"
    status: MATCH
    reason: "Matches subtracting line 17 from line 16."
  - key: "23"
    status: MATCH
    reason: "Matches the smaller of line 1 or line 13 when the worksheet continues."
  - key: "24"
    status: MATCH
    reason: "Matches entering the amount from line 22."
  - key: "25"
    status: MATCH
    reason: "Matches subtracting line 24 from line 23 with a zero floor."
  - key: "26"
    status: MATCH
    reason: "Matches the IRS 15-percent ceiling amounts for all filing statuses."
  - key: "27"
    status: MATCH
    reason: "Matches the smaller of line 1 or line 26."
  - key: "28"
    status: MATCH
    reason: "Matches adding lines 21 and 22."
  - key: "29"
    status: MATCH
    reason: "Matches subtracting line 28 from line 27 with a zero floor."
  - key: "30"
    status: MATCH
    reason: "Matches the smaller of line 25 or line 29."
  - key: "31"
    status: MATCH
    reason: "Matches multiplying line 30 by 15%."
  - key: "32"
    status: MATCH
    reason: "Matches adding lines 24 and 30."
  - key: "33"
    status: MATCH
    reason: "Matches subtracting line 32 from line 23 when the worksheet continues."
  - key: "34"
    status: MATCH
    reason: "Matches multiplying line 33 by 20%."
  - key: "35"
    status: MATCH
    reason: "Matches the smaller of line 9 and Schedule D line 19, represented by the unrecaptured section 1250 gain helper."
  - key: "36"
    status: MATCH
    reason: "Matches adding lines 10 and 21."
  - key: "37"
    status: MATCH
    reason: "Matches entering the amount from line 1."
  - key: "38"
    status: MATCH
    reason: "Matches subtracting line 37 from line 36 with a zero floor."
  - key: "39"
    status: MATCH
    reason: "Matches subtracting line 38 from line 35 with a zero floor."
  - key: "40"
    status: MATCH
    reason: "Matches multiplying line 39 by 25%."
  - key: "41"
    status: MISMATCH
    reason: "The IRS says 'If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44.' The gate also computes lines 41-43 when line 19 is zero even if line 18 is zero."
  - key: "42"
    status: MISMATCH
    reason: "Same gate error as line 41: the IRS skips lines 41 through 43 when Schedule D line 18 is zero or blank, but the restatement computes when line 19 is zero even if line 18 is zero."
  - key: "43"
    status: MISMATCH
    reason: "Same gate error as line 41: the IRS skips lines 41 through 43 when Schedule D line 18 is zero or blank, but the restatement computes when line 19 is zero even if line 18 is zero."
  - key: "44"
    status: MATCH
    reason: "Matches the IRS instruction to use the Tax Table below $100,000 and the Tax Computation Worksheet at $100,000 or more for line 21."
  - key: "45"
    status: MATCH
    reason: "Matches adding lines 31, 34, 40, 43, and 44."
  - key: "46"
    status: MATCH
    reason: "Matches the IRS instruction to use the Tax Table below $100,000 and the Tax Computation Worksheet at $100,000 or more for line 1."
  - key: "47"
    status: MATCH
    reason: "Matches entering the smaller of line 45 or line 46."
```
