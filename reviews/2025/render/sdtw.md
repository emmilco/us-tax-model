# Render comparison — sdtw

The rendered English of every printed line of `Schedule D Tax Worksheet` (`rendered/2025/sdtw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | cde45a52d381dc7c230ffdde0c5484ee56d7d650f4f07fac90148b7aff9ef362 |
| lines judged | 47 |
| match / mismatch / unclear / missing | 45 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### 1 — Taxable income
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The restatement always uses f1040 line 15 and has no refusal for Form 2555 filers. The IRS line says "if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet."

Ruling: scope; project retained. The Foreign Earned Income Tax Worksheet alternative applies only to a filer who claimed the exclusion or housing deduction on Form 2555 (i1040gi p. 36, line 16: "If you claimed the foreign earned income exclusion, housing exclusion, or housing deduction on Form 2555, you must use the Foreign Earned Income Tax Worksheet"). That filer reports the exclusion on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), and the return refuses any Schedule 1 income at Form 1040 line 8 (`scope.schedule1`, forms/2025/f1040.yaml) before line 16 is reached. The alternative is recorded as not encoded in the worksheet note. No change to the data.

### 2 — Qualified dividends
Status: **MATCH**

Model: Qualified dividends from Form 1040 line 3a, as the IRS line says.

### 3 — Form 4952 line 4g election
Status: **MATCH**

Model: Form 4952 line 4g passes through the validated election helper. The refusals name the Form 4952 cases the program excludes.

### 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **MISMATCH**

Restated: Enter the amount from f4952 line 4e.

Model: The restatement always uses f4952 line 4e and omits the footnote: "* If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952." No refusal covers that case.

Ruling: scope; project retained. The footnote's dotted-line amount arises only under the alternative allocation of Form 4952 line 4e, which is refused (`f4952.election` refuses when `f4952.alternative_allocation`: "Only the default capital-gain-first allocation is supported; alternative allocation and Form 1116 coordination are outside scope"). No change to the data.

### 5 — Subtract line 4 from line 3; floor at zero
Status: **MATCH**

Model: Subtract line 4 from line 3, floored at zero, as printed.

### 6 — Subtract line 5 from line 2; floor at zero
Status: **MATCH**

Model: Subtract line 5 from line 2, floored at zero, as printed. The ** footnote applies only to Form 2555 filers, which is flagged at line 1.

### 7 — Smaller of Schedule D lines 15 and 16
Status: **MATCH**

Model: Smaller of Schedule D line 15 or line 16, as printed.

### 8 — Smaller of lines 3 and 4
Status: **MATCH**

Model: Smaller of line 3 or line 4.

### 9 — Subtract line 8 from line 7; floor at zero
Status: **MATCH**

Model: Subtract line 8 from line 7, floored at zero.

### 10 — Add lines 6 and 9
Status: **MATCH**

Model: Add lines 6 and 9.

### 11 — Add Schedule D lines 18 and 19
Status: **MATCH**

Model: Adds the supplied Schedule D line 18 and line 19 amounts (the 28% Rate Gain and Unrecaptured Section 1250 Gain worksheet results), matching "Add lines 18 and 19 of Schedule D."

### 12 — Smaller of lines 9 and 11
Status: **MATCH**

Model: Smaller of line 9 or line 11.

### 13 — Subtract line 12 from line 10
Status: **MATCH**

Model: Subtract line 12 from line 10.

### 14 — Subtract line 13 from line 1; floor at zero
Status: **MATCH**

Model: Subtract line 13 from line 1, floored at zero.

### 15 — Zero-rate ceiling by filing status
Status: **MATCH**

Model: Amounts match the IRS text: $48,350 for single or MFS, $96,700 for MFJ or QSS, $64,750 for HOH.

### 16 — Smaller of lines 1 and 15
Status: **MATCH**

Model: Smaller of line 1 or line 15.

### 17 — Smaller of lines 14 and 16
Status: **MATCH**

Model: Smaller of line 14 or line 16.

### 18 — Subtract line 10 from line 1; floor at zero
Status: **MATCH**

Model: Subtract line 10 from line 1, floored at zero.

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **MATCH**

Model: Smaller of line 1 or the ceiling helper. The ceilings match the IRS text: $197,300 for single, MFS and HOH; $394,600 for MFJ and QSS.

### 20 — Smaller of lines 14 and 19
Status: **MATCH**

Model: Smaller of line 14 or line 19.

### 21 — Larger of lines 18 and 20
Status: **MATCH**

Model: Larger of line 18 or line 20.

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **MATCH**

Model: Subtract line 17 from line 16.

### 23 — Smaller of lines 1 and 13
Status: **MATCH**

Model: Computed only when line 1 ≠ line 16, matching "If lines 1 and 16 are the same, skip lines 23 through 43". The value is the smaller of line 1 or line 13.

### 24 — Amount from line 22
Status: **MATCH**

Model: Amount from line 22, under the same skip gate as line 23.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **MATCH**

Model: Subtract line 24 from line 23, floored at zero, under the skip gate.

### 26 — 15-percent ceiling by filing status
Status: **MATCH**

Model: Amounts match the IRS text: $533,400 single, $300,000 MFS, $600,050 MFJ and QSS, $566,700 HOH. The skip gate is correct.

### 27 — Smaller of lines 1 and 26
Status: **MATCH**

Model: Smaller of line 1 or line 26, under the skip gate.

### 28 — Add lines 21 and 22
Status: **MATCH**

Model: Add lines 21 and 22, under the skip gate.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **MATCH**

Model: Subtract line 28 from line 27, floored at zero, under the skip gate.

### 30 — Smaller of lines 25 and 29
Status: **MATCH**

Model: Smaller of line 25 or line 29, under the skip gate.

### 31 — Multiply line 30 by 15 percent
Status: **MATCH**

Model: Line 30 times 15%, under the skip gate.

### 32 — Add lines 24 and 30
Status: **MATCH**

Model: Add lines 24 and 30, under the skip gate.

### 33 — Subtract line 32 from line 23
Status: **MATCH**

Model: Computed only if the line 23 gate passed and line 1 ≠ line 32, matching "If lines 1 and 32 are the same, skip lines 33 through 43". The value is line 23 minus line 32.

### 34 — Multiply line 33 by 20 percent
Status: **MATCH**

Model: Line 33 times 20%, under the line 32 gate.

### 35 — Smaller of line 9 and Schedule D line 19
Status: **MATCH**

Model: Computed only when Schedule D line 19 is positive, matching "If Schedule D, line 19, is zero or blank, skip lines 35 through 40". The value is the smaller of line 9 or Schedule D line 19.

### 36 — Add lines 10 and 21
Status: **MATCH**

Model: Add lines 10 and 21, under the line 19 gate.

### 37 — Amount from line 1
Status: **MATCH**

Model: Amount from line 1, under the line 19 gate.

### 38 — Subtract line 37 from line 36; floor at zero
Status: **MATCH**

Model: Subtract line 37 from line 36, floored at zero.

### 39 — Subtract line 38 from line 35; floor at zero
Status: **MATCH**

Model: Subtract line 38 from line 35, floored at zero.

### 40 — Multiply line 39 by 25 percent
Status: **MATCH**

Model: Line 39 times 25%.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **MATCH**

Model: The gate follows the printed flow literally. When Schedule D line 19 is zero, the IRS says "go to line 41", which bypasses the line 18 check. Otherwise lines 41–43 are skipped when "Schedule D, line 18, is zero or blank." The sum of lines 21, 22, 30, 33 and 39 is correct.

### 42 — Subtract line 41 from line 1
Status: **MATCH**

Model: Subtract line 41 from line 1, under the same gate.

### 43 — Multiply line 42 by 28 percent
Status: **MATCH**

Model: Line 42 times 28%, under the same gate.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Tax on line 21 by filing status, using the Tax Table or the Tax Computation Worksheet as the IRS line directs.

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **MATCH**

Model: Add lines 31, 34, 40, 43 and 44.

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Tax on line 1, using the Tax Table or the Tax Computation Worksheet.

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **MATCH**

Model: Smaller of line 45 or line 46. The Form 2555 note only changes where the amount is entered, not its value.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always uses f1040 line 15 and has no refusal for Form 2555 filers. The IRS line says \"if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet.\""
  - key: "2"
    status: MATCH
    reason: "Qualified dividends from Form 1040 line 3a, as the IRS line says."
  - key: "3"
    status: MATCH
    reason: "Form 4952 line 4g passes through the validated election helper. The refusals name the Form 4952 cases the program excludes."
  - key: "4"
    status: MISMATCH
    reason: "The restatement always uses f4952 line 4e and omits the footnote: \"* If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952.\" No refusal covers that case."
  - key: "5"
    status: MATCH
    reason: "Subtract line 4 from line 3, floored at zero, as printed."
  - key: "6"
    status: MATCH
    reason: "Subtract line 5 from line 2, floored at zero, as printed. The ** footnote applies only to Form 2555 filers, which is flagged at line 1."
  - key: "7"
    status: MATCH
    reason: "Smaller of Schedule D line 15 or line 16, as printed."
  - key: "8"
    status: MATCH
    reason: "Smaller of line 3 or line 4."
  - key: "9"
    status: MATCH
    reason: "Subtract line 8 from line 7, floored at zero."
  - key: "10"
    status: MATCH
    reason: "Add lines 6 and 9."
  - key: "11"
    status: MATCH
    reason: "Adds the supplied Schedule D line 18 and line 19 amounts (the 28% Rate Gain and Unrecaptured Section 1250 Gain worksheet results), matching \"Add lines 18 and 19 of Schedule D.\""
  - key: "12"
    status: MATCH
    reason: "Smaller of line 9 or line 11."
  - key: "13"
    status: MATCH
    reason: "Subtract line 12 from line 10."
  - key: "14"
    status: MATCH
    reason: "Subtract line 13 from line 1, floored at zero."
  - key: "15"
    status: MATCH
    reason: "Amounts match the IRS text: $48,350 for single or MFS, $96,700 for MFJ or QSS, $64,750 for HOH."
  - key: "16"
    status: MATCH
    reason: "Smaller of line 1 or line 15."
  - key: "17"
    status: MATCH
    reason: "Smaller of line 14 or line 16."
  - key: "18"
    status: MATCH
    reason: "Subtract line 10 from line 1, floored at zero."
  - key: "19"
    status: MATCH
    reason: "Smaller of line 1 or the ceiling helper. The ceilings match the IRS text: $197,300 for single, MFS and HOH; $394,600 for MFJ and QSS."
  - key: "20"
    status: MATCH
    reason: "Smaller of line 14 or line 19."
  - key: "21"
    status: MATCH
    reason: "Larger of line 18 or line 20."
  - key: "22"
    status: MATCH
    reason: "Subtract line 17 from line 16."
  - key: "23"
    status: MATCH
    reason: "Computed only when line 1 ≠ line 16, matching \"If lines 1 and 16 are the same, skip lines 23 through 43\". The value is the smaller of line 1 or line 13."
  - key: "24"
    status: MATCH
    reason: "Amount from line 22, under the same skip gate as line 23."
  - key: "25"
    status: MATCH
    reason: "Subtract line 24 from line 23, floored at zero, under the skip gate."
  - key: "26"
    status: MATCH
    reason: "Amounts match the IRS text: $533,400 single, $300,000 MFS, $600,050 MFJ and QSS, $566,700 HOH. The skip gate is correct."
  - key: "27"
    status: MATCH
    reason: "Smaller of line 1 or line 26, under the skip gate."
  - key: "28"
    status: MATCH
    reason: "Add lines 21 and 22, under the skip gate."
  - key: "29"
    status: MATCH
    reason: "Subtract line 28 from line 27, floored at zero, under the skip gate."
  - key: "30"
    status: MATCH
    reason: "Smaller of line 25 or line 29, under the skip gate."
  - key: "31"
    status: MATCH
    reason: "Line 30 times 15%, under the skip gate."
  - key: "32"
    status: MATCH
    reason: "Add lines 24 and 30, under the skip gate."
  - key: "33"
    status: MATCH
    reason: "Computed only if the line 23 gate passed and line 1 ≠ line 32, matching \"If lines 1 and 32 are the same, skip lines 33 through 43\". The value is line 23 minus line 32."
  - key: "34"
    status: MATCH
    reason: "Line 33 times 20%, under the line 32 gate."
  - key: "35"
    status: MATCH
    reason: "Computed only when Schedule D line 19 is positive, matching \"If Schedule D, line 19, is zero or blank, skip lines 35 through 40\". The value is the smaller of line 9 or Schedule D line 19."
  - key: "36"
    status: MATCH
    reason: "Add lines 10 and 21, under the line 19 gate."
  - key: "37"
    status: MATCH
    reason: "Amount from line 1, under the line 19 gate."
  - key: "38"
    status: MATCH
    reason: "Subtract line 37 from line 36, floored at zero."
  - key: "39"
    status: MATCH
    reason: "Subtract line 38 from line 35, floored at zero."
  - key: "40"
    status: MATCH
    reason: "Line 39 times 25%."
  - key: "41"
    status: MATCH
    reason: "The gate follows the printed flow literally. When Schedule D line 19 is zero, the IRS says \"go to line 41\", which bypasses the line 18 check. Otherwise lines 41–43 are skipped when \"Schedule D, line 18, is zero or blank.\" The sum of lines 21, 22, 30, 33 and 39 is correct."
  - key: "42"
    status: MATCH
    reason: "Subtract line 41 from line 1, under the same gate."
  - key: "43"
    status: MATCH
    reason: "Line 42 times 28%, under the same gate."
  - key: "44"
    status: MATCH
    reason: "Tax on line 21 by filing status, using the Tax Table or the Tax Computation Worksheet as the IRS line directs."
  - key: "45"
    status: MATCH
    reason: "Add lines 31, 34, 40, 43 and 44."
  - key: "46"
    status: MATCH
    reason: "Tax on line 1, using the Tax Table or the Tax Computation Worksheet."
  - key: "47"
    status: MATCH
    reason: "Smaller of line 45 or line 46. The Form 2555 note only changes where the amount is entered, not its value."
```
```
