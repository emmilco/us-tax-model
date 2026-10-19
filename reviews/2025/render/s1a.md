# Render comparison — s1a

The rendered English of every printed line of `Schedule 1-A (Form 1040) — Additional Deductions` (`rendered/2025/s1a.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3769f8941598415b9e3ea877475d1778bc8f1f279824e8556b5227916707c779 |
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

Model: The form says to enter the amount from Form 1040, line 11b. The restatement does exactly that.

### 2a — Enter any income from Puerto Rico that you excluded
Status: **MATCH**

Model: The program enters $0 and refuses whenever there is excluded Puerto Rico income or a Form 2555 or 4563. The instructions say lines 2a–2e are completed only in those cases.

### 2b — Enter the amount from Form 2555, line 45
Status: **MATCH**

Model: The program enters $0. The Form 2555 case is covered by the line 2a refusal, so $0 is right for the cases it supports.

### 2c — Enter the amount from Form 2555, line 50
Status: **MATCH**

Model: The program enters $0. The Form 2555 case is covered by the line 2a refusal.

### 2d — Enter the amount from Form 4563, line 15
Status: **MATCH**

Model: The program enters $0. The Form 4563 case is covered by the line 2a refusal.

### 2e — Add lines 2a, 2b, 2c, and 2d
Status: **MATCH**

Model: The form says to add lines 2a, 2b, 2c and 2d. The restatement does the same.

### 3 — Add lines 1 and 2e
Status: **MATCH**

Model: The form says to add lines 1 and 2e. The restatement does the same.

### 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, bo
Status: **MATCH**

Model: With more than one employer the program enters $0, as the form says ('enter -0- on lines 4a and 4b'). Otherwise it uses tips from Form W-2 box 7 or from Forms 4070, which the instructions list as allowed methods. Part II is gated on qualified tips, a valid SSN and not married filing separately, as the caution requires.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **MATCH**

Model: The program enters $0 and refuses any return with Form 4137 tips, which falls under its Schedule 2 refusal. The form says 'If Form 4137 is not filed, enter -0-', so $0 is right in the supported cases.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **MATCH**

Model: With one employer the program enters the larger of line 4a or 4b, as the form says. With more than one employer it uses worksheet line 2 (the sum of column (d)), as the instructions say.

### 5 — Qualified tips received in the course of a trade or business
Status: **MATCH**

Model: The program enters $0 and refuses trade-or-business income through its Schedule 1 refusal, which covers the Schedule C, E and F cases this line needs.

### 6 — Add lines 4c and 5
Status: **MATCH**

Model: The form says to add lines 4c and 5. The restatement does the same.

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **MATCH**

Model: The form says to enter the smaller of line 6 or $25,000. The restatement does the same.

### 8 — Enter the amount from line 3
Status: **MATCH**

Model: The form says to enter the amount from line 3. The restatement does the same.

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: The program uses $300,000 for married filing jointly and $150,000 otherwise, as the form says.

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **MATCH**

Model: The form says to subtract line 9 from line 8. When the result is zero or less, line 13 takes line 7, which the line 13 logic handles.

### 12 — Multiply line 11 by $100
Status: **MATCH**

Model: Line 11 drops any part of line 10 below a whole $1,000, and line 12 multiplies by $100 per $1,000. This matches 'decrease the result to the next lower whole number' and 'Multiply line 11 by $100'.

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: The program enters $0 for married filing separately or with no valid SSN. It enters line 7 when line 10 is zero or less, and otherwise line 7 minus line 12, but not below zero. This matches the form and the line 10 instruction.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **MATCH**

Model: The program adds the qualified overtime of each person with a valid SSN. This matches the line and its multi-employer worksheet.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **MATCH**

Model: The program enters $0 and refuses overtime reported on Form 1099-NEC or 1099-MISC (nonemployee compensation, which means filing Schedule C).

### 14c — Add lines 14a and 14b
Status: **MATCH**

Model: The form says to add lines 14a and 14b. The restatement does the same.

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **MATCH**

Model: The program enters the smaller of line 14c or $12,500 ($25,000 if married filing jointly), as the form says.

### 16 — Enter the amount from line 3
Status: **MATCH**

Model: The form says to enter the amount from line 3. The restatement does the same.

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: The program uses $300,000 for married filing jointly and $150,000 otherwise, as the form says.

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **MATCH**

Model: The form says to subtract line 17 from line 16. When the result is zero or less, line 21 takes line 15.

### 20 — Multiply line 19 by $100
Status: **MATCH**

Model: Line 19 drops any part of line 18 below a whole $1,000, and line 20 multiplies by $100 per $1,000, as the form says.

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **MATCH**

Model: The program enters $0 for married filing separately or with no valid SSN. It enters line 15 when line 18 is zero or less, and otherwise line 15 minus line 20, but not below zero.

### 23 — Add lines 22a and 22b, column (iii)
Status: **MATCH**

Model: The program adds column (iii) for every loan, including loans on an attached statement. The instructions allow such a statement when there are more than two VINs.

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **MATCH**

Model: The form says to enter the smaller of line 23 or $10,000. The restatement does the same.

### 25 — Enter the amount from line 3
Status: **MATCH**

Model: The form says to enter the amount from line 3. The restatement does the same.

### 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **MATCH**

Model: The program uses $200,000 for married filing jointly and $100,000 otherwise, as the form and instructions say.

### 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
Status: **MATCH**

Model: The form says to subtract line 26 from line 25. When the result is zero or less, line 30 takes line 24.

### 29 — Multiply line 28 by $200
Status: **MATCH**

Model: Line 28 rounds line 27 up to the next whole $1,000, and line 29 multiplies by $200 per $1,000. This matches 'increase the result to the next higher whole number' and 'Multiply line 28 by $200'.

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **MATCH**

Model: The program enters line 24 when line 27 is zero or less, and otherwise line 24 minus line 29, but not below zero, as the form and instructions say.

### 31 — Enter the amount from line 3
Status: **MATCH**

Model: The form says to enter the amount from line 3. Part V is gated on birth before January 2, 1961, a valid SSN and not married filing separately, as the caution requires.

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **MATCH**

Model: The program uses $150,000 for married filing jointly and $75,000 otherwise, as the form says.

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **MATCH**

Model: The form says to subtract line 32 from line 31. When the result is zero or less, line 35 takes $6,000.

### 34 — Multiply line 33 by 6% (0.06)
Status: **MATCH**

Model: The program multiplies line 33 (zero if negative) by 6%, as the form says.

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **MATCH**

Model: The program enters $6,000 when line 33 is zero or less, and otherwise $6,000 minus line 34, but not below zero.

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **MATCH**

Model: The program enters line 35 when the filer was born before January 2, 1961 and has a valid SSN, and $0 for married filing separately. It refuses a filer who died in 2025 before reaching 65, as the instructions require.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **MISMATCH**

Restated: Choose — [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = true → helper "Line 36b for a spouse born before January 2, 1961, with a valid SSN"]

Model: The form says 'If you are married filing jointly, your spouse has a valid social security number..., and your spouse was born before January 2, 1961'. The restatement checks only the spouse's birth date and SSN, not that the return is filed jointly. A spouse entry on a head of household or qualifying surviving spouse return could therefore get line 35.

Ruling: scope; project retained. A spouse entry exists only on a joint return: any other roster is refused at Form 1040 line 1a (household.roster_bad; Form 1040 page 1, 'If joint return, spouse's first name'), so whenever the spouse's birth date and SSN can be tested the return is filed jointly (Schedule 1-A line 36b; i1040gi p. 110).

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **MATCH**

Model: The form says to add lines 36a and 36b. The restatement does the same.

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **MATCH**

Model: The form says to add lines 13, 21, 30 and 37. The restatement does the same.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The form says to enter the amount from Form 1040, line 11b. The restatement does exactly that."
  - key: "2a"
    status: MATCH
    reason: "The program enters $0 and refuses whenever there is excluded Puerto Rico income or a Form 2555 or 4563. The instructions say lines 2a–2e are completed only in those cases."
  - key: "2b"
    status: MATCH
    reason: "The program enters $0. The Form 2555 case is covered by the line 2a refusal, so $0 is right for the cases it supports."
  - key: "2c"
    status: MATCH
    reason: "The program enters $0. The Form 2555 case is covered by the line 2a refusal."
  - key: "2d"
    status: MATCH
    reason: "The program enters $0. The Form 4563 case is covered by the line 2a refusal."
  - key: "2e"
    status: MATCH
    reason: "The form says to add lines 2a, 2b, 2c and 2d. The restatement does the same."
  - key: "3"
    status: MATCH
    reason: "The form says to add lines 1 and 2e. The restatement does the same."
  - key: "4a"
    status: MATCH
    reason: "With more than one employer the program enters $0, as the form says ('enter -0- on lines 4a and 4b'). Otherwise it uses tips from Form W-2 box 7 or from Forms 4070, which the instructions list as allowed methods. Part II is gated on qualified tips, a valid SSN and not married filing separately, as the caution requires."
  - key: "4b"
    status: MATCH
    reason: "The program enters $0 and refuses any return with Form 4137 tips, which falls under its Schedule 2 refusal. The form says 'If Form 4137 is not filed, enter -0-', so $0 is right in the supported cases."
  - key: "4c"
    status: MATCH
    reason: "With one employer the program enters the larger of line 4a or 4b, as the form says. With more than one employer it uses worksheet line 2 (the sum of column (d)), as the instructions say."
  - key: "5"
    status: MATCH
    reason: "The program enters $0 and refuses trade-or-business income through its Schedule 1 refusal, which covers the Schedule C, E and F cases this line needs."
  - key: "6"
    status: MATCH
    reason: "The form says to add lines 4c and 5. The restatement does the same."
  - key: "7"
    status: MATCH
    reason: "The form says to enter the smaller of line 6 or $25,000. The restatement does the same."
  - key: "8"
    status: MATCH
    reason: "The form says to enter the amount from line 3. The restatement does the same."
  - key: "9"
    status: MATCH
    reason: "The program uses $300,000 for married filing jointly and $150,000 otherwise, as the form says."
  - key: "10"
    status: MATCH
    reason: "The form says to subtract line 9 from line 8. When the result is zero or less, line 13 takes line 7, which the line 13 logic handles."
  - key: "12"
    status: MATCH
    reason: "Line 11 drops any part of line 10 below a whole $1,000, and line 12 multiplies by $100 per $1,000. This matches 'decrease the result to the next lower whole number' and 'Multiply line 11 by $100'."
  - key: "13"
    status: MATCH
    reason: "The program enters $0 for married filing separately or with no valid SSN. It enters line 7 when line 10 is zero or less, and otherwise line 7 minus line 12, but not below zero. This matches the form and the line 10 instruction."
  - key: "14a"
    status: MATCH
    reason: "The program adds the qualified overtime of each person with a valid SSN. This matches the line and its multi-employer worksheet."
  - key: "14b"
    status: MATCH
    reason: "The program enters $0 and refuses overtime reported on Form 1099-NEC or 1099-MISC (nonemployee compensation, which means filing Schedule C)."
  - key: "14c"
    status: MATCH
    reason: "The form says to add lines 14a and 14b. The restatement does the same."
  - key: "15"
    status: MATCH
    reason: "The program enters the smaller of line 14c or $12,500 ($25,000 if married filing jointly), as the form says."
  - key: "16"
    status: MATCH
    reason: "The form says to enter the amount from line 3. The restatement does the same."
  - key: "17"
    status: MATCH
    reason: "The program uses $300,000 for married filing jointly and $150,000 otherwise, as the form says."
  - key: "18"
    status: MATCH
    reason: "The form says to subtract line 17 from line 16. When the result is zero or less, line 21 takes line 15."
  - key: "20"
    status: MATCH
    reason: "Line 19 drops any part of line 18 below a whole $1,000, and line 20 multiplies by $100 per $1,000, as the form says."
  - key: "21"
    status: MATCH
    reason: "The program enters $0 for married filing separately or with no valid SSN. It enters line 15 when line 18 is zero or less, and otherwise line 15 minus line 20, but not below zero."
  - key: "23"
    status: MATCH
    reason: "The program adds column (iii) for every loan, including loans on an attached statement. The instructions allow such a statement when there are more than two VINs."
  - key: "24"
    status: MATCH
    reason: "The form says to enter the smaller of line 23 or $10,000. The restatement does the same."
  - key: "25"
    status: MATCH
    reason: "The form says to enter the amount from line 3. The restatement does the same."
  - key: "26"
    status: MATCH
    reason: "The program uses $200,000 for married filing jointly and $100,000 otherwise, as the form and instructions say."
  - key: "27"
    status: MATCH
    reason: "The form says to subtract line 26 from line 25. When the result is zero or less, line 30 takes line 24."
  - key: "29"
    status: MATCH
    reason: "Line 28 rounds line 27 up to the next whole $1,000, and line 29 multiplies by $200 per $1,000. This matches 'increase the result to the next higher whole number' and 'Multiply line 28 by $200'."
  - key: "30"
    status: MATCH
    reason: "The program enters line 24 when line 27 is zero or less, and otherwise line 24 minus line 29, but not below zero, as the form and instructions say."
  - key: "31"
    status: MATCH
    reason: "The form says to enter the amount from line 3. Part V is gated on birth before January 2, 1961, a valid SSN and not married filing separately, as the caution requires."
  - key: "32"
    status: MATCH
    reason: "The program uses $150,000 for married filing jointly and $75,000 otherwise, as the form says."
  - key: "33"
    status: MATCH
    reason: "The form says to subtract line 32 from line 31. When the result is zero or less, line 35 takes $6,000."
  - key: "34"
    status: MATCH
    reason: "The program multiplies line 33 (zero if negative) by 6%, as the form says."
  - key: "35"
    status: MATCH
    reason: "The program enters $6,000 when line 33 is zero or less, and otherwise $6,000 minus line 34, but not below zero."
  - key: "36a"
    status: MATCH
    reason: "The program enters line 35 when the filer was born before January 2, 1961 and has a valid SSN, and $0 for married filing separately. It refuses a filer who died in 2025 before reaching 65, as the instructions require."
  - key: "36b"
    status: MISMATCH
    reason: "The form says 'If you are married filing jointly, your spouse has a valid social security number..., and your spouse was born before January 2, 1961'. The restatement checks only the spouse's birth date and SSN, not that the return is filed jointly. A spouse entry on a head of household or qualifying surviving spouse return could therefore get line 35."
  - key: "37"
    status: MATCH
    reason: "The form says to add lines 36a and 36b. The restatement does the same."
  - key: "38"
    status: MATCH
    reason: "The form says to add lines 13, 21, 30 and 37. The restatement does the same."
```
```
