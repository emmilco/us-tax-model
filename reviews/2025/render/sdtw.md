# Render comparison — sdtw

The rendered English of every printed line of `Schedule D Tax Worksheet` (`rendered/2025/sdtw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 245fe057b1916fa11b61730702923d60bc428af9c14cf535cf83ed1ba6c7e476 |
| subject sha256 | ad5dbe41f9378e5dbc65094fa635d34acd196f617c0b876328f6fc9e6d4fa2ae |
| lines judged | 47 |
| match / mismatch / unclear / missing | 45 / 2 / 0 / 0 |
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

Model: The restatement always uses f1040 line 15 and names no refusal for the Form 2555 case. The IRS text says "if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet."

Ruling: scope; project retained. The Foreign Earned Income Tax Worksheet alternative applies only to a filer who claimed the exclusion or housing deduction on Form 2555 (i1040gi p. 36, line 16: "If you claimed the foreign earned income exclusion, housing exclusion, or housing deduction on Form 2555, you must use the Foreign Earned Income Tax Worksheet"). That filer reports the exclusion on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), and the return refuses any Schedule 1 income at Form 1040 line 8 (`scope.schedule1`, forms/2025/f1040.yaml) before line 16 is reached. The alternative is recorded as not encoded in the worksheet note. No change to the data.

### 2 — Qualified dividends
Status: **MATCH**

Model: The IRS line enters qualified dividends from Form 1040 line 3a, as restated.

### 3 — Form 4952 line 4g election
Status: **MATCH**

Model: The helper enters Form 4952 line 4g, matching "Enter the amount from Form 4952 ... line 4g". The refusals name the excluded Form 4952 cases.

### 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **MISMATCH**

Restated: Enter the amount from f4952 line 4e.

Model: The restatement always uses f4952 line 4e and has no refusal for the footnote case. The IRS footnote says "If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952."

Ruling: scope; project retained. The footnote's dotted-line amount arises only under the alternative allocation of Form 4952 line 4e, which is refused (`f4952.election` refuses when `f4952.alternative_allocation`: "Only the default capital-gain-first allocation is supported; alternative allocation and Form 1116 coordination are outside scope"). No change to the data.

### 5 — Subtract line 4 from line 3; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 4 from line 3, with a floor at zero, as restated.

### 6 — Subtract line 5 from line 2; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 5 from line 2, with a floor at zero, as restated. The ** footnote only refers to Form 2555 text that is not given here.

### 7 — Smaller of Schedule D lines 15 and 16
Status: **MATCH**

Model: The IRS line enters the smaller of Schedule D line 15 or line 16, as restated.

### 8 — Smaller of lines 3 and 4
Status: **MATCH**

Model: The IRS line enters the smaller of line 3 or line 4, as restated.

### 9 — Subtract line 8 from line 7; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 8 from line 7, with a floor at zero, as restated.

### 10 — Add lines 6 and 9
Status: **MATCH**

Model: The IRS line adds lines 6 and 9, as restated.

### 11 — Add Schedule D lines 18 and 19
Status: **MATCH**

Model: The IRS line adds Schedule D lines 18 and 19. The helpers supply those two amounts from the 28% Rate Gain and Unrecaptured Section 1250 Gain worksheet results.

### 12 — Smaller of lines 9 and 11
Status: **MATCH**

Model: The IRS line enters the smaller of line 9 or line 11, as restated.

### 13 — Subtract line 12 from line 10
Status: **MATCH**

Model: The IRS line says subtract line 12 from line 10, as restated.

### 14 — Subtract line 13 from line 1; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 13 from line 1, with a floor at zero, as restated.

### 15 — Zero-rate ceiling by filing status
Status: **MATCH**

Model: The amounts match the IRS text: $48,350 single/MFS, $96,700 MFJ/QSS, $64,750 HOH.

### 16 — Smaller of lines 1 and 15
Status: **MATCH**

Model: The IRS line enters the smaller of line 1 or line 15, as restated.

### 17 — Smaller of lines 14 and 16
Status: **MATCH**

Model: The IRS line enters the smaller of line 14 or line 16, as restated.

### 18 — Subtract line 10 from line 1; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 10 from line 1, with a floor at zero, as restated.

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **MATCH**

Model: The IRS line enters the smaller of line 1 or the ceiling. The ceiling amounts match: $197,300 single/MFS/HOH, $394,600 MFJ/QSS.

### 20 — Smaller of lines 14 and 19
Status: **MATCH**

Model: The IRS line enters the smaller of line 14 or line 19, as restated.

### 21 — Larger of lines 18 and 20
Status: **MATCH**

Model: The IRS line enters the larger of line 18 or line 20, as restated.

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **MATCH**

Model: The IRS line says subtract line 17 from line 16, as restated.

### 23 — Smaller of lines 1 and 13
Status: **MATCH**

Model: The line is computed only when lines 1 and 16 differ, per "If lines 1 and 16 are the same, skip lines 23 through 43". It then takes the smaller of line 1 or line 13.

### 24 — Amount from line 22
Status: **MATCH**

Model: The line enters the line 22 amount under the same skip rule. Line 22 is always computed, so the blank case does not arise.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 24 from line 23, with a floor at zero, under the skip rule.

### 26 — 15-percent ceiling by filing status
Status: **MATCH**

Model: The amounts match the IRS text: $533,400 single, $300,000 MFS, $600,050 MFJ/QSS, $566,700 HOH.

### 27 — Smaller of lines 1 and 26
Status: **MATCH**

Model: The IRS line enters the smaller of line 1 or line 26, as restated.

### 28 — Add lines 21 and 22
Status: **MATCH**

Model: The IRS line adds lines 21 and 22, as restated.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 28 from line 27, with a floor at zero, as restated.

### 30 — Smaller of lines 25 and 29
Status: **MATCH**

Model: The IRS line enters the smaller of line 25 or line 29, as restated.

### 31 — Multiply line 30 by 15 percent
Status: **MATCH**

Model: The IRS line multiplies line 30 by 15%, as restated.

### 32 — Add lines 24 and 30
Status: **MATCH**

Model: The IRS line adds lines 24 and 30, as restated.

### 33 — Subtract line 32 from line 23
Status: **MATCH**

Model: The line is computed only when lines 1 and 32 differ (and line 23 was reached), per "If lines 1 and 32 are the same, skip lines 33 through 43". It then subtracts line 32 from line 23.

### 34 — Multiply line 33 by 20 percent
Status: **MATCH**

Model: The IRS line multiplies line 33 by 20% under the same skip rule.

### 35 — Smaller of line 9 and Schedule D line 19
Status: **MATCH**

Model: The line is computed only when Schedule D line 19 is positive, per "If Schedule D, line 19, is zero or blank, skip lines 35 through 40". It then takes the smaller of line 9 or Schedule D line 19.

### 36 — Add lines 10 and 21
Status: **MATCH**

Model: The IRS line adds lines 10 and 21 under the skip rule.

### 37 — Amount from line 1
Status: **MATCH**

Model: The IRS line enters the amount from line 1 under the skip rule.

### 38 — Subtract line 37 from line 36; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 37 from line 36, with a floor at zero, as restated.

### 39 — Subtract line 38 from line 35; floor at zero
Status: **MATCH**

Model: The IRS line says subtract line 38 from line 35, with a floor at zero, as restated.

### 40 — Multiply line 39 by 25 percent
Status: **MATCH**

Model: The IRS line multiplies line 39 by 25%, as restated.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **MATCH**

Model: The gate follows the printed flow: skipping lines 35–40 goes directly "to line 41", and otherwise line 41 is reached only if Schedule D line 18 is nonzero. The line then adds lines 21, 22, 30, 33 and 39.

### 42 — Subtract line 41 from line 1
Status: **MATCH**

Model: The IRS line says subtract line 41 from line 1, under the same gate.

### 43 — Multiply line 42 by 28 percent
Status: **MATCH**

Model: The IRS line multiplies line 42 by 28%, under the same gate.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: The IRS line figures the tax on line 21 using the Tax Table or the Tax Computation Worksheet, as restated.

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **MATCH**

Model: The IRS line adds lines 31, 34, 40, 43, and 44, as restated.

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: The IRS line figures the tax on line 1 using the Tax Table or the Tax Computation Worksheet, as restated.

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **MATCH**

Model: The IRS line enters the smaller of line 45 or line 46, as restated.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always uses f1040 line 15 and names no refusal for the Form 2555 case. The IRS text says \"if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet.\""
  - key: "2"
    status: MATCH
    reason: "The IRS line enters qualified dividends from Form 1040 line 3a, as restated."
  - key: "3"
    status: MATCH
    reason: "The helper enters Form 4952 line 4g, matching \"Enter the amount from Form 4952 ... line 4g\". The refusals name the excluded Form 4952 cases."
  - key: "4"
    status: MISMATCH
    reason: "The restatement always uses f4952 line 4e and has no refusal for the footnote case. The IRS footnote says \"If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952.\""
  - key: "5"
    status: MATCH
    reason: "The IRS line says subtract line 4 from line 3, with a floor at zero, as restated."
  - key: "6"
    status: MATCH
    reason: "The IRS line says subtract line 5 from line 2, with a floor at zero, as restated. The ** footnote only refers to Form 2555 text that is not given here."
  - key: "7"
    status: MATCH
    reason: "The IRS line enters the smaller of Schedule D line 15 or line 16, as restated."
  - key: "8"
    status: MATCH
    reason: "The IRS line enters the smaller of line 3 or line 4, as restated."
  - key: "9"
    status: MATCH
    reason: "The IRS line says subtract line 8 from line 7, with a floor at zero, as restated."
  - key: "10"
    status: MATCH
    reason: "The IRS line adds lines 6 and 9, as restated."
  - key: "11"
    status: MATCH
    reason: "The IRS line adds Schedule D lines 18 and 19. The helpers supply those two amounts from the 28% Rate Gain and Unrecaptured Section 1250 Gain worksheet results."
  - key: "12"
    status: MATCH
    reason: "The IRS line enters the smaller of line 9 or line 11, as restated."
  - key: "13"
    status: MATCH
    reason: "The IRS line says subtract line 12 from line 10, as restated."
  - key: "14"
    status: MATCH
    reason: "The IRS line says subtract line 13 from line 1, with a floor at zero, as restated."
  - key: "15"
    status: MATCH
    reason: "The amounts match the IRS text: $48,350 single/MFS, $96,700 MFJ/QSS, $64,750 HOH."
  - key: "16"
    status: MATCH
    reason: "The IRS line enters the smaller of line 1 or line 15, as restated."
  - key: "17"
    status: MATCH
    reason: "The IRS line enters the smaller of line 14 or line 16, as restated."
  - key: "18"
    status: MATCH
    reason: "The IRS line says subtract line 10 from line 1, with a floor at zero, as restated."
  - key: "19"
    status: MATCH
    reason: "The IRS line enters the smaller of line 1 or the ceiling. The ceiling amounts match: $197,300 single/MFS/HOH, $394,600 MFJ/QSS."
  - key: "20"
    status: MATCH
    reason: "The IRS line enters the smaller of line 14 or line 19, as restated."
  - key: "21"
    status: MATCH
    reason: "The IRS line enters the larger of line 18 or line 20, as restated."
  - key: "22"
    status: MATCH
    reason: "The IRS line says subtract line 17 from line 16, as restated."
  - key: "23"
    status: MATCH
    reason: "The line is computed only when lines 1 and 16 differ, per \"If lines 1 and 16 are the same, skip lines 23 through 43\". It then takes the smaller of line 1 or line 13."
  - key: "24"
    status: MATCH
    reason: "The line enters the line 22 amount under the same skip rule. Line 22 is always computed, so the blank case does not arise."
  - key: "25"
    status: MATCH
    reason: "The IRS line says subtract line 24 from line 23, with a floor at zero, under the skip rule."
  - key: "26"
    status: MATCH
    reason: "The amounts match the IRS text: $533,400 single, $300,000 MFS, $600,050 MFJ/QSS, $566,700 HOH."
  - key: "27"
    status: MATCH
    reason: "The IRS line enters the smaller of line 1 or line 26, as restated."
  - key: "28"
    status: MATCH
    reason: "The IRS line adds lines 21 and 22, as restated."
  - key: "29"
    status: MATCH
    reason: "The IRS line says subtract line 28 from line 27, with a floor at zero, as restated."
  - key: "30"
    status: MATCH
    reason: "The IRS line enters the smaller of line 25 or line 29, as restated."
  - key: "31"
    status: MATCH
    reason: "The IRS line multiplies line 30 by 15%, as restated."
  - key: "32"
    status: MATCH
    reason: "The IRS line adds lines 24 and 30, as restated."
  - key: "33"
    status: MATCH
    reason: "The line is computed only when lines 1 and 32 differ (and line 23 was reached), per \"If lines 1 and 32 are the same, skip lines 33 through 43\". It then subtracts line 32 from line 23."
  - key: "34"
    status: MATCH
    reason: "The IRS line multiplies line 33 by 20% under the same skip rule."
  - key: "35"
    status: MATCH
    reason: "The line is computed only when Schedule D line 19 is positive, per \"If Schedule D, line 19, is zero or blank, skip lines 35 through 40\". It then takes the smaller of line 9 or Schedule D line 19."
  - key: "36"
    status: MATCH
    reason: "The IRS line adds lines 10 and 21 under the skip rule."
  - key: "37"
    status: MATCH
    reason: "The IRS line enters the amount from line 1 under the skip rule."
  - key: "38"
    status: MATCH
    reason: "The IRS line says subtract line 37 from line 36, with a floor at zero, as restated."
  - key: "39"
    status: MATCH
    reason: "The IRS line says subtract line 38 from line 35, with a floor at zero, as restated."
  - key: "40"
    status: MATCH
    reason: "The IRS line multiplies line 39 by 25%, as restated."
  - key: "41"
    status: MATCH
    reason: "The gate follows the printed flow: skipping lines 35–40 goes directly \"to line 41\", and otherwise line 41 is reached only if Schedule D line 18 is nonzero. The line then adds lines 21, 22, 30, 33 and 39."
  - key: "42"
    status: MATCH
    reason: "The IRS line says subtract line 41 from line 1, under the same gate."
  - key: "43"
    status: MATCH
    reason: "The IRS line multiplies line 42 by 28%, under the same gate."
  - key: "44"
    status: MATCH
    reason: "The IRS line figures the tax on line 21 using the Tax Table or the Tax Computation Worksheet, as restated."
  - key: "45"
    status: MATCH
    reason: "The IRS line adds lines 31, 34, 40, 43, and 44, as restated."
  - key: "46"
    status: MATCH
    reason: "The IRS line figures the tax on line 1 using the Tax Table or the Tax Computation Worksheet, as restated."
  - key: "47"
    status: MATCH
    reason: "The IRS line enters the smaller of line 45 or line 46, as restated."
```
```
