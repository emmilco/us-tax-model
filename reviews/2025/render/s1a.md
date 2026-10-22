# Render comparison — s1a

The rendered English of every printed line of `Schedule 1-A (Form 1040) — Additional Deductions` (`rendered/2025/s1a.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3c9f3cdae2200e783e78eb7d7875c7bebecc572ef32efdd4b4492eb9ad20fc0f |
| subject sha256 | e2c7e0e652b4b6d2c2c98723696702da3ed5cb5eb0c9669dce867a3158e0ef4b |
| lines judged | 43 |
| match / mismatch / unclear / missing | 42 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104, 105, 106, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104, 106, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **MATCH**

Model: Takes the amount from Form 1040, line 11b, as the form says.

### 2a — Enter any income from Puerto Rico that you excluded
Status: **MATCH**

Model: Entered as $0. The refusal excludes filers with Puerto Rico excluded income or Form 2555/4563, which are the only cases where lines 2a–2d would be filled in.

### 2b — Enter the amount from Form 2555, line 45
Status: **MATCH**

Model: $0 is correct because the line 2a refusal excludes Form 2555 filers.

### 2c — Enter the amount from Form 2555, line 50
Status: **MATCH**

Model: $0 is correct because the line 2a refusal excludes Form 2555 filers.

### 2d — Enter the amount from Form 4563, line 15
Status: **MATCH**

Model: $0 is correct because the line 2a refusal excludes Form 4563 filers.

### 2e — Add lines 2a, 2b, 2c, and 2d
Status: **MATCH**

Model: Adds lines 2a through 2d, as the form says.

### 3 — Add lines 1 and 2e
Status: **MATCH**

Model: Adds lines 1 and 2e, as the form says.

### 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, bo
Status: **MATCH**

Model: With more than one employer it enters $0, matching 'enter -0- on lines 4a and 4b'. Otherwise it uses the W-2 box 7 or Forms 4070 tip total, which the instructions allow as methods 1 and 2.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **MATCH**

Model: $0 is correct as 'If Form 4137 is not filed, enter -0-'. The refusal names Form 4137 as the excluded case.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **MATCH**

Model: With one employer it takes the larger of lines 4a and 4b. With more than one, it uses worksheet line 2 (sum of column (d)), as the line 4c instructions direct.

### 5 — Qualified tips received in the course of a trade or business
Status: **MATCH**

Model: Entered as $0. The refusals exclude qualified tips received in a trade or business (Schedule C, E or F).

### 6 — Add lines 4c and 5
Status: **MATCH**

Model: Adds lines 4c and 5.

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **MATCH**

Model: Takes the smaller of line 6 or $25,000.

### 8 — Enter the amount from line 3
Status: **MATCH**

Model: Takes the amount from line 3.

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: $300,000 for married filing jointly and $150,000 otherwise. Married filing separately is already gated out of Part II.

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **MATCH**

Model: Subtracts line 9 from line 8. The 'zero or less' case is handled at line 13 by entering line 7.

### 12 — Multiply line 11 by $100
Status: **MATCH**

Model: Line 11 is line 10 rounded down to whole thousands, and multiplying by 1/10 gives $100 per thousand, the same as 'Multiply line 11 by $100'.

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: Zero for married filing separately or without a valid SSN. Otherwise it is line 7 when line 8 does not exceed line 9, else line 7 minus line 12 floored at zero.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **MATCH**

Model: Adds the qualified overtime of the people who received it and have a valid SSN, consistent with line 14a and the more-than-one-employer worksheet.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **MATCH**

Model: Entered as $0. The refusals exclude overtime reported on Form 1099-NEC or 1099-MISC.

### 14c — Add lines 14a and 14b
Status: **MATCH**

Model: Adds lines 14a and 14b.

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **MATCH**

Model: Takes the smaller of line 14c or $12,500 ($25,000 if married filing jointly).

### 16 — Enter the amount from line 3
Status: **MATCH**

Model: Takes the amount from line 3.

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: $150,000, or $300,000 if married filing jointly.

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **MATCH**

Model: Subtracts line 17 from line 16. The 'zero or less' case is handled at line 21 by entering line 15.

### 20 — Multiply line 19 by $100
Status: **MATCH**

Model: Line 19 is line 18 rounded down to whole thousands, and 1/10 of that equals 'Multiply line 19 by $100'.

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **MATCH**

Model: Zero for married filing separately or without a valid SSN. Otherwise it is line 15 when line 16 does not exceed line 17, else line 15 minus line 20 floored at zero.

### 23 — Add lines 22a and 22b, column (iii)
Status: **MATCH**

Model: Adds column (iii) for every loan, including any listed on the attached statement for more than two VINs, as the line 22 instructions describe.

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **MATCH**

Model: Takes the smaller of line 23 or $10,000.

### 25 — Enter the amount from line 3
Status: **MATCH**

Model: Takes the amount from line 3.

### 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **MATCH**

Model: $100,000, or $200,000 if married filing jointly.

### 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
Status: **MATCH**

Model: Subtracts line 26 from line 25. The 'zero or less' case is handled at line 30 by entering line 24.

### 29 — Multiply line 28 by $200
Status: **MATCH**

Model: Line 28 is line 27 rounded up to whole thousands, which matches 'increase the result to the next higher whole number' if an exact multiple is left unchanged. 1/5 of that equals 'Multiply line 28 by $200'.

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **MATCH**

Model: Line 24 when line 25 does not exceed line 26, else line 24 minus line 29 floored at zero.

### 31 — Enter the amount from line 3
Status: **MATCH**

Model: Takes the amount from line 3.

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **MATCH**

Model: $75,000, or $150,000 if married filing jointly.

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **MATCH**

Model: Subtracts line 32 from line 31. The 'zero or less' case is handled at line 35 by entering $6,000.

### 34 — Multiply line 33 by 6% (0.06)
Status: **MATCH**

Model: Multiplies line 33, floored at zero, by 6%.

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **MATCH**

Model: $6,000 when line 31 does not exceed line 32; otherwise $6,000 minus line 34, floored at zero.

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **MATCH**

Model: Enters line 35 when the filer was born before January 2, 1961, and has a valid SSN; zero for married filing separately. The refusal covers a decedent who died before reaching age 65.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **MISMATCH**

Restated: Choose — [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = true → helper "Line 36b for a spouse born before January 2, 1961, with a valid SSN"]

Model: The IRS line requires 'If you are married filing jointly, your spouse has a valid social security number..., and your spouse was born before January 2, 1961'. The restatement checks only the spouse's birth date and SSN, not the joint filing status. Married filing separately happens to yield zero through line 35, but other filing statuses with a spouse entry are not excluded.

Ruling: scope; project retained. A spouse entry exists only on a joint return: any other roster is refused at Form 1040 line 1a (household.roster_bad; Form 1040 page 1, 'If joint return, spouse's first name'), so whenever the spouse's birth date and SSN can be tested the return is filed jointly (Schedule 1-A line 36b; i1040gi p. 110).

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **MATCH**

Model: Adds lines 36a and 36b.

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **MATCH**

Model: Adds lines 13, 21, 30 and 37.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Takes the amount from Form 1040, line 11b, as the form says."
  - key: "2a"
    status: MATCH
    reason: "Entered as $0. The refusal excludes filers with Puerto Rico excluded income or Form 2555/4563, which are the only cases where lines 2a–2d would be filled in."
  - key: "2b"
    status: MATCH
    reason: "$0 is correct because the line 2a refusal excludes Form 2555 filers."
  - key: "2c"
    status: MATCH
    reason: "$0 is correct because the line 2a refusal excludes Form 2555 filers."
  - key: "2d"
    status: MATCH
    reason: "$0 is correct because the line 2a refusal excludes Form 4563 filers."
  - key: "2e"
    status: MATCH
    reason: "Adds lines 2a through 2d, as the form says."
  - key: "3"
    status: MATCH
    reason: "Adds lines 1 and 2e, as the form says."
  - key: "4a"
    status: MATCH
    reason: "With more than one employer it enters $0, matching 'enter -0- on lines 4a and 4b'. Otherwise it uses the W-2 box 7 or Forms 4070 tip total, which the instructions allow as methods 1 and 2."
  - key: "4b"
    status: MATCH
    reason: "$0 is correct as 'If Form 4137 is not filed, enter -0-'. The refusal names Form 4137 as the excluded case."
  - key: "4c"
    status: MATCH
    reason: "With one employer it takes the larger of lines 4a and 4b. With more than one, it uses worksheet line 2 (sum of column (d)), as the line 4c instructions direct."
  - key: "5"
    status: MATCH
    reason: "Entered as $0. The refusals exclude qualified tips received in a trade or business (Schedule C, E or F)."
  - key: "6"
    status: MATCH
    reason: "Adds lines 4c and 5."
  - key: "7"
    status: MATCH
    reason: "Takes the smaller of line 6 or $25,000."
  - key: "8"
    status: MATCH
    reason: "Takes the amount from line 3."
  - key: "9"
    status: MATCH
    reason: "$300,000 for married filing jointly and $150,000 otherwise. Married filing separately is already gated out of Part II."
  - key: "10"
    status: MATCH
    reason: "Subtracts line 9 from line 8. The 'zero or less' case is handled at line 13 by entering line 7."
  - key: "12"
    status: MATCH
    reason: "Line 11 is line 10 rounded down to whole thousands, and multiplying by 1/10 gives $100 per thousand, the same as 'Multiply line 11 by $100'."
  - key: "13"
    status: MATCH
    reason: "Zero for married filing separately or without a valid SSN. Otherwise it is line 7 when line 8 does not exceed line 9, else line 7 minus line 12 floored at zero."
  - key: "14a"
    status: MATCH
    reason: "Adds the qualified overtime of the people who received it and have a valid SSN, consistent with line 14a and the more-than-one-employer worksheet."
  - key: "14b"
    status: MATCH
    reason: "Entered as $0. The refusals exclude overtime reported on Form 1099-NEC or 1099-MISC."
  - key: "14c"
    status: MATCH
    reason: "Adds lines 14a and 14b."
  - key: "15"
    status: MATCH
    reason: "Takes the smaller of line 14c or $12,500 ($25,000 if married filing jointly)."
  - key: "16"
    status: MATCH
    reason: "Takes the amount from line 3."
  - key: "17"
    status: MATCH
    reason: "$150,000, or $300,000 if married filing jointly."
  - key: "18"
    status: MATCH
    reason: "Subtracts line 17 from line 16. The 'zero or less' case is handled at line 21 by entering line 15."
  - key: "20"
    status: MATCH
    reason: "Line 19 is line 18 rounded down to whole thousands, and 1/10 of that equals 'Multiply line 19 by $100'."
  - key: "21"
    status: MATCH
    reason: "Zero for married filing separately or without a valid SSN. Otherwise it is line 15 when line 16 does not exceed line 17, else line 15 minus line 20 floored at zero."
  - key: "23"
    status: MATCH
    reason: "Adds column (iii) for every loan, including any listed on the attached statement for more than two VINs, as the line 22 instructions describe."
  - key: "24"
    status: MATCH
    reason: "Takes the smaller of line 23 or $10,000."
  - key: "25"
    status: MATCH
    reason: "Takes the amount from line 3."
  - key: "26"
    status: MATCH
    reason: "$100,000, or $200,000 if married filing jointly."
  - key: "27"
    status: MATCH
    reason: "Subtracts line 26 from line 25. The 'zero or less' case is handled at line 30 by entering line 24."
  - key: "29"
    status: MATCH
    reason: "Line 28 is line 27 rounded up to whole thousands, which matches 'increase the result to the next higher whole number' if an exact multiple is left unchanged. 1/5 of that equals 'Multiply line 28 by $200'."
  - key: "30"
    status: MATCH
    reason: "Line 24 when line 25 does not exceed line 26, else line 24 minus line 29 floored at zero."
  - key: "31"
    status: MATCH
    reason: "Takes the amount from line 3."
  - key: "32"
    status: MATCH
    reason: "$75,000, or $150,000 if married filing jointly."
  - key: "33"
    status: MATCH
    reason: "Subtracts line 32 from line 31. The 'zero or less' case is handled at line 35 by entering $6,000."
  - key: "34"
    status: MATCH
    reason: "Multiplies line 33, floored at zero, by 6%."
  - key: "35"
    status: MATCH
    reason: "$6,000 when line 31 does not exceed line 32; otherwise $6,000 minus line 34, floored at zero."
  - key: "36a"
    status: MATCH
    reason: "Enters line 35 when the filer was born before January 2, 1961, and has a valid SSN; zero for married filing separately. The refusal covers a decedent who died before reaching age 65."
  - key: "36b"
    status: MISMATCH
    reason: "The IRS line requires 'If you are married filing jointly, your spouse has a valid social security number..., and your spouse was born before January 2, 1961'. The restatement checks only the spouse's birth date and SSN, not the joint filing status. Married filing separately happens to yield zero through line 35, but other filing statuses with a spouse entry are not excluded."
  - key: "37"
    status: MATCH
    reason: "Adds lines 36a and 36b."
  - key: "38"
    status: MATCH
    reason: "Adds lines 13, 21, 30 and 37."
```
```
