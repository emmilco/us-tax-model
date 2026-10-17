# Render comparison — sdtw

The rendered English of every printed line of `Schedule D Tax Worksheet` (`rendered/2025/sdtw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 245fe057b1916fa11b61730702923d60bc428af9c14cf535cf83ed1ba6c7e476 |
| lines judged | 47 |
| match / mismatch / unclear / missing | 45 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | - | ac7a0c9cbb9e635491b2505e7d04cea3381b892402408ddc97f8d49d80a6640b |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### 1 — Taxable income
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The restatement always uses Form 1040 line 15 and has no refusal for the Form 2555 case. The IRS text says "(However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet...)".

Ruling: scope; project retained. The Foreign Earned Income Tax Worksheet alternative applies only to a filer who claimed the exclusion or housing deduction on Form 2555 (i1040gi p. 36, line 16: "If you claimed the foreign earned income exclusion, housing exclusion, or housing deduction on Form 2555, you must use the Foreign Earned Income Tax Worksheet"). That filer reports the exclusion on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), and the return refuses any Schedule 1 income at Form 1040 line 8 (`scope.schedule1`, forms/2025/f1040.yaml) before line 16 is reached. The alternative is recorded as not encoded in the worksheet note. No change to the data.

### 2 — Qualified dividends
Status: **MATCH**

Model: Qualified dividends from Form 1040 line 3a, as the line says.

### 3 — Form 4952 line 4g election
Status: **MATCH**

Model: The helper chain leads to Form 4952 line 4g, as the line says. The refusals name the Form 4952 cases the program does not support.

### 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **MISMATCH**

Restated: Enter the amount from f4952 line 4e.

Model: The restatement always uses Form 4952 line 4e and does not cover the footnote: "* If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952." No refusal names this case.

Ruling: scope; project retained. The footnote's dotted-line amount arises only under the alternative allocation of Form 4952 line 4e, which is refused (`f4952.election` refuses when `f4952.alternative_allocation`: "Only the default capital-gain-first allocation is supported; alternative allocation and Form 1116 coordination are outside scope"). No change to the data.

### 5 — Subtract line 4 from line 3; floor at zero
Status: **MATCH**

Model: Subtract line 4 from line 3, with zero as the floor, as the line says.

### 6 — Subtract line 5 from line 2; floor at zero
Status: **MATCH**

Model: Subtract line 5 from line 2, with zero as the floor, as the line says. The ** Form 2555 footnote points to text not given here.

### 7 — Smaller of Schedule D lines 15 and 16
Status: **MATCH**

Model: The smaller of Schedule D line 15 or line 16, as the line says.

### 8 — Smaller of lines 3 and 4
Status: **MATCH**

Model: The smaller of line 3 or line 4, as the line says.

### 9 — Subtract line 8 from line 7; floor at zero
Status: **MATCH**

Model: Subtract line 8 from line 7, with zero as the floor, as the line says. The ** Form 2555 footnote points to text not given here.

### 10 — Add lines 6 and 9
Status: **MATCH**

Model: Add lines 6 and 9, as the line says.

### 11 — Add Schedule D lines 18 and 19
Status: **MATCH**

Model: Adds Schedule D lines 18 and 19, which the program supplies from the 28% Rate Gain and Unrecaptured Section 1250 Gain worksheet results. This matches "Add lines 18 and 19 of Schedule D".

### 12 — Smaller of lines 9 and 11
Status: **MATCH**

Model: The smaller of line 9 or line 11, as the line says.

### 13 — Subtract line 12 from line 10
Status: **MATCH**

Model: Subtract line 12 from line 10, as the line says.

### 14 — Subtract line 13 from line 1; floor at zero
Status: **MATCH**

Model: Subtract line 13 from line 1, with zero as the floor, as the line says.

### 15 — Zero-rate ceiling by filing status
Status: **MATCH**

Model: The amounts match the text: $48,350 for single or MFS, $96,700 for MFJ or QSS, and $64,750 for HOH.

### 16 — Smaller of lines 1 and 15
Status: **MATCH**

Model: The smaller of line 1 or line 15, as the line says.

### 17 — Smaller of lines 14 and 16
Status: **MATCH**

Model: The smaller of line 14 or line 16, as the line says.

### 18 — Subtract line 10 from line 1; floor at zero
Status: **MATCH**

Model: Subtract line 10 from line 1, with zero as the floor, as the line says.

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **MATCH**

Model: The smaller of line 1 or the filing-status amount. The amounts match the text: $197,300 for single, MFS and HOH, and $394,600 for MFJ and QSS.

### 20 — Smaller of lines 14 and 19
Status: **MATCH**

Model: The smaller of line 14 or line 19, as the line says.

### 21 — Larger of lines 18 and 20
Status: **MATCH**

Model: The larger of line 18 or line 20, as the line says.

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **MATCH**

Model: Subtract line 17 from line 16, as the line says.

### 23 — Smaller of lines 1 and 13
Status: **MATCH**

Model: The smaller of line 1 or line 13, and zero when lines 1 and 16 are the same. This follows "If lines 1 and 16 are the same, skip lines 23 through 43".

### 24 — Amount from line 22
Status: **MATCH**

Model: The amount from line 22, under the same skip rule. Line 22 is always computed, so the "blank" case gives the same result.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **MATCH**

Model: Subtract line 24 from line 23, with zero as the floor, under the line-22 skip rule.

### 26 — 15-percent ceiling by filing status
Status: **MATCH**

Model: The amounts match the text: $533,400 single, $300,000 MFS, $600,050 MFJ or QSS, and $566,700 HOH. The line-22 skip rule applies.

### 27 — Smaller of lines 1 and 26
Status: **MATCH**

Model: The smaller of line 1 or line 26, under the skip rule.

### 28 — Add lines 21 and 22
Status: **MATCH**

Model: Add lines 21 and 22, under the skip rule.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **MATCH**

Model: Subtract line 28 from line 27, with zero as the floor, under the skip rule.

### 30 — Smaller of lines 25 and 29
Status: **MATCH**

Model: The smaller of line 25 or line 29, under the skip rule.

### 31 — Multiply line 30 by 15 percent
Status: **MATCH**

Model: Line 30 times 15%, under the skip rule.

### 32 — Add lines 24 and 30
Status: **MATCH**

Model: Add lines 24 and 30, under the skip rule.

### 33 — Subtract line 32 from line 23
Status: **MATCH**

Model: Subtract line 32 from line 23. Lines 33 onward are skipped when lines 1 and 32 are the same or when the earlier skip applies, which follows the text.

### 34 — Multiply line 33 by 20 percent
Status: **MATCH**

Model: Line 33 times 20%, under the line-32 skip rule.

### 35 — Smaller of line 9 and Schedule D line 19
Status: **MATCH**

Model: The smaller of line 9 or Schedule D line 19. Lines 35–40 are computed only when Schedule D line 19 is above zero, which follows "If Schedule D, line 19, is zero or blank, skip lines 35 through 40".

### 36 — Add lines 10 and 21
Status: **MATCH**

Model: Add lines 10 and 21, under the line-19 skip rule.

### 37 — Amount from line 1
Status: **MATCH**

Model: The amount from line 1, under the skip rule.

### 38 — Subtract line 37 from line 36; floor at zero
Status: **MATCH**

Model: Subtract line 37 from line 36, with zero as the floor, under the skip rule.

### 39 — Subtract line 38 from line 35; floor at zero
Status: **MATCH**

Model: Subtract line 38 from line 35, with zero as the floor, under the skip rule.

### 40 — Multiply line 39 by 25 percent
Status: **MATCH**

Model: Line 39 times 25%, under the skip rule.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **MATCH**

Model: Add lines 21, 22, 30, 33 and 39. The gate follows the printed flow: the Schedule D line 18 skip check comes after line 40, and skipping lines 35–40 sends you straight to line 41.

### 42 — Subtract line 41 from line 1
Status: **MATCH**

Model: Subtract line 41 from line 1, under the same gate.

### 43 — Multiply line 42 by 28 percent
Status: **MATCH**

Model: Line 42 times 28%, under the same gate.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Tax on the line 21 amount using the Tax Table or the Tax Computation Worksheet for the filing status, as the line says.

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **MATCH**

Model: Add lines 31, 34, 40, 43 and 44, as the line says.

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Tax on the line 1 amount using the Tax Table or the Tax Computation Worksheet, as the line says.

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **MATCH**

Model: The smaller of line 45 or line 46, as the line says.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always uses Form 1040 line 15 and has no refusal for the Form 2555 case. The IRS text says \"(However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet...)\"."
  - key: "2"
    status: MATCH
    reason: "Qualified dividends from Form 1040 line 3a, as the line says."
  - key: "3"
    status: MATCH
    reason: "The helper chain leads to Form 4952 line 4g, as the line says. The refusals name the Form 4952 cases the program does not support."
  - key: "4"
    status: MISMATCH
    reason: "The restatement always uses Form 4952 line 4e and does not cover the footnote: \"* If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952.\" No refusal names this case."
  - key: "5"
    status: MATCH
    reason: "Subtract line 4 from line 3, with zero as the floor, as the line says."
  - key: "6"
    status: MATCH
    reason: "Subtract line 5 from line 2, with zero as the floor, as the line says. The ** Form 2555 footnote points to text not given here."
  - key: "7"
    status: MATCH
    reason: "The smaller of Schedule D line 15 or line 16, as the line says."
  - key: "8"
    status: MATCH
    reason: "The smaller of line 3 or line 4, as the line says."
  - key: "9"
    status: MATCH
    reason: "Subtract line 8 from line 7, with zero as the floor, as the line says. The ** Form 2555 footnote points to text not given here."
  - key: "10"
    status: MATCH
    reason: "Add lines 6 and 9, as the line says."
  - key: "11"
    status: MATCH
    reason: "Adds Schedule D lines 18 and 19, which the program supplies from the 28% Rate Gain and Unrecaptured Section 1250 Gain worksheet results. This matches \"Add lines 18 and 19 of Schedule D\"."
  - key: "12"
    status: MATCH
    reason: "The smaller of line 9 or line 11, as the line says."
  - key: "13"
    status: MATCH
    reason: "Subtract line 12 from line 10, as the line says."
  - key: "14"
    status: MATCH
    reason: "Subtract line 13 from line 1, with zero as the floor, as the line says."
  - key: "15"
    status: MATCH
    reason: "The amounts match the text: $48,350 for single or MFS, $96,700 for MFJ or QSS, and $64,750 for HOH."
  - key: "16"
    status: MATCH
    reason: "The smaller of line 1 or line 15, as the line says."
  - key: "17"
    status: MATCH
    reason: "The smaller of line 14 or line 16, as the line says."
  - key: "18"
    status: MATCH
    reason: "Subtract line 10 from line 1, with zero as the floor, as the line says."
  - key: "19"
    status: MATCH
    reason: "The smaller of line 1 or the filing-status amount. The amounts match the text: $197,300 for single, MFS and HOH, and $394,600 for MFJ and QSS."
  - key: "20"
    status: MATCH
    reason: "The smaller of line 14 or line 19, as the line says."
  - key: "21"
    status: MATCH
    reason: "The larger of line 18 or line 20, as the line says."
  - key: "22"
    status: MATCH
    reason: "Subtract line 17 from line 16, as the line says."
  - key: "23"
    status: MATCH
    reason: "The smaller of line 1 or line 13, and zero when lines 1 and 16 are the same. This follows \"If lines 1 and 16 are the same, skip lines 23 through 43\"."
  - key: "24"
    status: MATCH
    reason: "The amount from line 22, under the same skip rule. Line 22 is always computed, so the \"blank\" case gives the same result."
  - key: "25"
    status: MATCH
    reason: "Subtract line 24 from line 23, with zero as the floor, under the line-22 skip rule."
  - key: "26"
    status: MATCH
    reason: "The amounts match the text: $533,400 single, $300,000 MFS, $600,050 MFJ or QSS, and $566,700 HOH. The line-22 skip rule applies."
  - key: "27"
    status: MATCH
    reason: "The smaller of line 1 or line 26, under the skip rule."
  - key: "28"
    status: MATCH
    reason: "Add lines 21 and 22, under the skip rule."
  - key: "29"
    status: MATCH
    reason: "Subtract line 28 from line 27, with zero as the floor, under the skip rule."
  - key: "30"
    status: MATCH
    reason: "The smaller of line 25 or line 29, under the skip rule."
  - key: "31"
    status: MATCH
    reason: "Line 30 times 15%, under the skip rule."
  - key: "32"
    status: MATCH
    reason: "Add lines 24 and 30, under the skip rule."
  - key: "33"
    status: MATCH
    reason: "Subtract line 32 from line 23. Lines 33 onward are skipped when lines 1 and 32 are the same or when the earlier skip applies, which follows the text."
  - key: "34"
    status: MATCH
    reason: "Line 33 times 20%, under the line-32 skip rule."
  - key: "35"
    status: MATCH
    reason: "The smaller of line 9 or Schedule D line 19. Lines 35–40 are computed only when Schedule D line 19 is above zero, which follows \"If Schedule D, line 19, is zero or blank, skip lines 35 through 40\"."
  - key: "36"
    status: MATCH
    reason: "Add lines 10 and 21, under the line-19 skip rule."
  - key: "37"
    status: MATCH
    reason: "The amount from line 1, under the skip rule."
  - key: "38"
    status: MATCH
    reason: "Subtract line 37 from line 36, with zero as the floor, under the skip rule."
  - key: "39"
    status: MATCH
    reason: "Subtract line 38 from line 35, with zero as the floor, under the skip rule."
  - key: "40"
    status: MATCH
    reason: "Line 39 times 25%, under the skip rule."
  - key: "41"
    status: MATCH
    reason: "Add lines 21, 22, 30, 33 and 39. The gate follows the printed flow: the Schedule D line 18 skip check comes after line 40, and skipping lines 35–40 sends you straight to line 41."
  - key: "42"
    status: MATCH
    reason: "Subtract line 41 from line 1, under the same gate."
  - key: "43"
    status: MATCH
    reason: "Line 42 times 28%, under the same gate."
  - key: "44"
    status: MATCH
    reason: "Tax on the line 21 amount using the Tax Table or the Tax Computation Worksheet for the filing status, as the line says."
  - key: "45"
    status: MATCH
    reason: "Add lines 31, 34, 40, 43 and 44, as the line says."
  - key: "46"
    status: MATCH
    reason: "Tax on the line 1 amount using the Tax Table or the Tax Computation Worksheet, as the line says."
  - key: "47"
    status: MATCH
    reason: "The smaller of line 45 or line 46, as the line says."
```
```
