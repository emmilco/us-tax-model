# Render comparison — s1a

The rendered English of every printed line of `Schedule 1-A (Form 1040) — Additional Deductions` (`rendered/2025/s1a.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 6d4affdfc3ec439de8a6509a7e935d1f725b38040cddd21d7eca344f5952b468 |
| lines judged | 43 |
| match / mismatch / unclear / missing | 43 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104, 105, 106, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104, 106, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **MATCH**

Model: The form says "Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b", and the restatement takes f1040 line 11b.

### 2a — Enter any income from Puerto Rico that you excluded
Status: **MATCH**

Model: The instructions say lines 2a–2e are needed only for excluded Puerto Rico income or Form 2555/4563. The refusal excludes exactly those cases, so $0 is right otherwise.

### 2b — Enter the amount from Form 2555, line 45
Status: **MATCH**

Model: Form 2555, line 45 applies only to Form 2555 filers. The sa.excluded_income refusal stated on line 2a excludes them, so $0 is correct within the supported cases.

### 2c — Enter the amount from Form 2555, line 50
Status: **MATCH**

Model: Form 2555, line 50 applies only to Form 2555 filers. The sa.excluded_income refusal on line 2a excludes them, so $0 is correct within the supported cases.

### 2d — Enter the amount from Form 4563, line 15
Status: **MATCH**

Model: Form 4563, line 15 applies only to Form 4563 filers. The sa.excluded_income refusal on line 2a excludes them, so $0 is correct within the supported cases.

### 2e — Add lines 2a, 2b, 2c, and 2d
Status: **MATCH**

Model: Matches "Add lines 2a, 2b, 2c, and 2d".

### 3 — Add lines 1 and 2e
Status: **MATCH**

Model: Matches "Add lines 1 and 2e".

### 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, bo
Status: **MATCH**

Model: With more than one employer it enters $0, as the form says ("enter -0- on lines 4a and 4b"). With one employer it enters the W-2 box 7 or Forms 4070 tips, which instructions methods 1–2 allow. Part II is gated on qualified tips, a joint return if married, and a valid SSN, per the caution.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **MATCH**

Model: Form 4137 tips are excluded by the s2.other refusal, which names Form 4137. Without Form 4137 the form says "If Form 4137 is not filed, enter -0-".

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **MATCH**

Model: With one employer it enters "the larger of line 4a or line 4b". With more than one employer it uses the worksheet, whose line 2 is "Add lines 1A through 1E, column (d), and enter this amount on Schedule 1-A, line 4c".

### 5 — Qualified tips received in the course of a trade or business
Status: **MATCH**

Model: Line 5 covers tips received "in the course of a trade or business" (Schedules C, E or F). The scope.schedule1 refusal excludes that income, so $0 is correct within the supported cases.

### 6 — Add lines 4c and 5
Status: **MATCH**

Model: Matches "Add lines 4c and 5".

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **MATCH**

Model: Matches "Enter the smaller of the amount on line 6 or $25,000".

### 8 — Enter the amount from line 3
Status: **MATCH**

Model: Matches "Enter the amount from line 3".

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: It enters $300,000 for married filing jointly and $150,000 otherwise, as the form says. Married filing separately is already excluded by the Part II gate.

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **MATCH**

Model: It subtracts line 9 from line 8. The "If zero or less, enter the amount from line 7 on line 13" instruction is carried out at line 13 through the line 8 > line 9 test.

### 12 — Multiply line 11 by $100
Status: **MATCH**

Model: Line 11 rounds line 10 down to whole thousands, as the form requires ("decrease the result to the next lower whole number"). Multiplying by 1/10 gives $100 per thousand, which matches "Multiply line 11 by $100".

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: It enters line 7 when line 10 is zero or less; otherwise line 7 minus line 12, floored at zero. It is $0 for married filing separately or without a valid SSN, matching the form and the Part II caution.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **MATCH**

Model: It sums qualified overtime per employer, matching the More Than One Employer Worksheet line 2: "Add the amounts from lines 1A through 1E, column (b), and enter this amount on Schedule 1-A, line 14a". With one employer the sum is just that employer's amount. Part III is gated as the caution requires.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **MATCH**

Model: Overtime reported on Form 1099-NEC or 1099-MISC (nonemployee compensation or other income) is excluded by the scope.schedule1 refusal, so $0 is correct within the supported cases.

### 14c — Add lines 14a and 14b
Status: **MATCH**

Model: Matches "Add lines 14a and 14b".

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **MATCH**

Model: Matches "Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)".

### 16 — Enter the amount from line 3
Status: **MATCH**

Model: Matches "Enter the amount from line 3".

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: Matches "Enter $150,000 ($300,000 if married filing jointly)". Married filing separately is excluded by the Part III gate.

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **MATCH**

Model: It subtracts line 17 from line 16. The zero-or-less rule ("enter the amount from line 15 on line 21") is carried out at line 21.

### 20 — Multiply line 19 by $100
Status: **MATCH**

Model: Line 19 rounds line 18 down to whole thousands, as the form requires. Multiplying by 1/10 gives $100 per thousand, which matches "Multiply line 19 by $100".

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **MATCH**

Model: It enters line 15 when line 18 is zero or less; otherwise line 15 minus line 20, floored at zero. It is $0 for married filing separately or without a valid SSN, matching the form and the Part III caution.

### 23 — Add lines 22a and 22b, column (iii)
Status: **MATCH**

Model: It sums column (iii) across all loans, matching "Add lines 22a and 22b, column (iii)". It includes loans on the attached statement, as the line 22 instructions allow for more than two VINs.

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **MATCH**

Model: Matches "Enter the smaller of the amount on line 23 or $10,000".

### 25 — Enter the amount from line 3
Status: **MATCH**

Model: Matches "Enter the amount from line 3".

### 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **MATCH**

Model: Matches "Enter $100,000 ($200,000 if married filing jointly)". The instructions also say "All other filing statuses—$100,000".

### 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
Status: **MATCH**

Model: It subtracts line 26 from line 25. The zero-or-less rule (enter line 24 on line 30) is carried out at line 30.

### 29 — Multiply line 28 by $200
Status: **MATCH**

Model: Line 28 rounds line 27 up to the next whole thousand ("increase the result to the next higher whole number"). Multiplying by 1/5 gives $200 per thousand, which matches "Multiply line 28 by $200".

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **MATCH**

Model: It enters line 24 when line 27 is zero or less; otherwise "Subtract line 29 from line 24. If zero or less, enter -0-". Part IV has no married-filing-separately or SSN restriction in the text.

### 31 — Enter the amount from line 3
Status: **MATCH**

Model: Matches "Enter the amount from line 3". Part V is gated on birth before January 2, 1961, not filing separately, and a valid SSN, per the caution.

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **MATCH**

Model: Matches "Enter $75,000 ($150,000 if married filing jointly)".

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **MATCH**

Model: It subtracts line 32 from line 31. The zero-or-less rule ("enter $6,000 on line 35") is carried out at line 35.

### 34 — Multiply line 33 by 6% (0.06)
Status: **MATCH**

Model: It multiplies line 33, floored at zero, by 6%. This matches "Multiply line 33 by 6% (0.06)"; the floor only matters when line 35 uses $6,000 anyway.

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **MATCH**

Model: It enters $6,000 when line 33 is zero or less; otherwise "Subtract line 34 from $6,000. If zero or less, enter -0-".

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **MATCH**

Model: It enters line 35 if the filer has a valid SSN, was born before January 2, 1961, and is not filing separately, matching the form and the requirement to file jointly. A refusal excludes a person who died in 2025 before reaching age 65, whom the instructions disqualify.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **MATCH**

Model: A joint-return spouse born before January 2, 1961 would check the spouse age box, so the sa.spouse_extra refusal excludes that case. Otherwise $0 is correct.

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **MATCH**

Model: Matches "Add lines 36a and 36b".

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **MATCH**

Model: Matches "Add lines 13, 21, 30, and 37".

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The form says \"Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b\", and the restatement takes f1040 line 11b."
  - key: "2a"
    status: MATCH
    reason: "The instructions say lines 2a–2e are needed only for excluded Puerto Rico income or Form 2555/4563. The refusal excludes exactly those cases, so $0 is right otherwise."
  - key: "2b"
    status: MATCH
    reason: "Form 2555, line 45 applies only to Form 2555 filers. The sa.excluded_income refusal stated on line 2a excludes them, so $0 is correct within the supported cases."
  - key: "2c"
    status: MATCH
    reason: "Form 2555, line 50 applies only to Form 2555 filers. The sa.excluded_income refusal on line 2a excludes them, so $0 is correct within the supported cases."
  - key: "2d"
    status: MATCH
    reason: "Form 4563, line 15 applies only to Form 4563 filers. The sa.excluded_income refusal on line 2a excludes them, so $0 is correct within the supported cases."
  - key: "2e"
    status: MATCH
    reason: "Matches \"Add lines 2a, 2b, 2c, and 2d\"."
  - key: "3"
    status: MATCH
    reason: "Matches \"Add lines 1 and 2e\"."
  - key: "4a"
    status: MATCH
    reason: "With more than one employer it enters $0, as the form says (\"enter -0- on lines 4a and 4b\"). With one employer it enters the W-2 box 7 or Forms 4070 tips, which instructions methods 1–2 allow. Part II is gated on qualified tips, a joint return if married, and a valid SSN, per the caution."
  - key: "4b"
    status: MATCH
    reason: "Form 4137 tips are excluded by the s2.other refusal, which names Form 4137. Without Form 4137 the form says \"If Form 4137 is not filed, enter -0-\"."
  - key: "4c"
    status: MATCH
    reason: "With one employer it enters \"the larger of line 4a or line 4b\". With more than one employer it uses the worksheet, whose line 2 is \"Add lines 1A through 1E, column (d), and enter this amount on Schedule 1-A, line 4c\"."
  - key: "5"
    status: MATCH
    reason: "Line 5 covers tips received \"in the course of a trade or business\" (Schedules C, E or F). The scope.schedule1 refusal excludes that income, so $0 is correct within the supported cases."
  - key: "6"
    status: MATCH
    reason: "Matches \"Add lines 4c and 5\"."
  - key: "7"
    status: MATCH
    reason: "Matches \"Enter the smaller of the amount on line 6 or $25,000\"."
  - key: "8"
    status: MATCH
    reason: "Matches \"Enter the amount from line 3\"."
  - key: "9"
    status: MATCH
    reason: "It enters $300,000 for married filing jointly and $150,000 otherwise, as the form says. Married filing separately is already excluded by the Part II gate."
  - key: "10"
    status: MATCH
    reason: "It subtracts line 9 from line 8. The \"If zero or less, enter the amount from line 7 on line 13\" instruction is carried out at line 13 through the line 8 > line 9 test."
  - key: "12"
    status: MATCH
    reason: "Line 11 rounds line 10 down to whole thousands, as the form requires (\"decrease the result to the next lower whole number\"). Multiplying by 1/10 gives $100 per thousand, which matches \"Multiply line 11 by $100\"."
  - key: "13"
    status: MATCH
    reason: "It enters line 7 when line 10 is zero or less; otherwise line 7 minus line 12, floored at zero. It is $0 for married filing separately or without a valid SSN, matching the form and the Part II caution."
  - key: "14a"
    status: MATCH
    reason: "It sums qualified overtime per employer, matching the More Than One Employer Worksheet line 2: \"Add the amounts from lines 1A through 1E, column (b), and enter this amount on Schedule 1-A, line 14a\". With one employer the sum is just that employer's amount. Part III is gated as the caution requires."
  - key: "14b"
    status: MATCH
    reason: "Overtime reported on Form 1099-NEC or 1099-MISC (nonemployee compensation or other income) is excluded by the scope.schedule1 refusal, so $0 is correct within the supported cases."
  - key: "14c"
    status: MATCH
    reason: "Matches \"Add lines 14a and 14b\"."
  - key: "15"
    status: MATCH
    reason: "Matches \"Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)\"."
  - key: "16"
    status: MATCH
    reason: "Matches \"Enter the amount from line 3\"."
  - key: "17"
    status: MATCH
    reason: "Matches \"Enter $150,000 ($300,000 if married filing jointly)\". Married filing separately is excluded by the Part III gate."
  - key: "18"
    status: MATCH
    reason: "It subtracts line 17 from line 16. The zero-or-less rule (\"enter the amount from line 15 on line 21\") is carried out at line 21."
  - key: "20"
    status: MATCH
    reason: "Line 19 rounds line 18 down to whole thousands, as the form requires. Multiplying by 1/10 gives $100 per thousand, which matches \"Multiply line 19 by $100\"."
  - key: "21"
    status: MATCH
    reason: "It enters line 15 when line 18 is zero or less; otherwise line 15 minus line 20, floored at zero. It is $0 for married filing separately or without a valid SSN, matching the form and the Part III caution."
  - key: "23"
    status: MATCH
    reason: "It sums column (iii) across all loans, matching \"Add lines 22a and 22b, column (iii)\". It includes loans on the attached statement, as the line 22 instructions allow for more than two VINs."
  - key: "24"
    status: MATCH
    reason: "Matches \"Enter the smaller of the amount on line 23 or $10,000\"."
  - key: "25"
    status: MATCH
    reason: "Matches \"Enter the amount from line 3\"."
  - key: "26"
    status: MATCH
    reason: "Matches \"Enter $100,000 ($200,000 if married filing jointly)\". The instructions also say \"All other filing statuses—$100,000\"."
  - key: "27"
    status: MATCH
    reason: "It subtracts line 26 from line 25. The zero-or-less rule (enter line 24 on line 30) is carried out at line 30."
  - key: "29"
    status: MATCH
    reason: "Line 28 rounds line 27 up to the next whole thousand (\"increase the result to the next higher whole number\"). Multiplying by 1/5 gives $200 per thousand, which matches \"Multiply line 28 by $200\"."
  - key: "30"
    status: MATCH
    reason: "It enters line 24 when line 27 is zero or less; otherwise \"Subtract line 29 from line 24. If zero or less, enter -0-\". Part IV has no married-filing-separately or SSN restriction in the text."
  - key: "31"
    status: MATCH
    reason: "Matches \"Enter the amount from line 3\". Part V is gated on birth before January 2, 1961, not filing separately, and a valid SSN, per the caution."
  - key: "32"
    status: MATCH
    reason: "Matches \"Enter $75,000 ($150,000 if married filing jointly)\"."
  - key: "33"
    status: MATCH
    reason: "It subtracts line 32 from line 31. The zero-or-less rule (\"enter $6,000 on line 35\") is carried out at line 35."
  - key: "34"
    status: MATCH
    reason: "It multiplies line 33, floored at zero, by 6%. This matches \"Multiply line 33 by 6% (0.06)\"; the floor only matters when line 35 uses $6,000 anyway."
  - key: "35"
    status: MATCH
    reason: "It enters $6,000 when line 33 is zero or less; otherwise \"Subtract line 34 from $6,000. If zero or less, enter -0-\"."
  - key: "36a"
    status: MATCH
    reason: "It enters line 35 if the filer has a valid SSN, was born before January 2, 1961, and is not filing separately, matching the form and the requirement to file jointly. A refusal excludes a person who died in 2025 before reaching age 65, whom the instructions disqualify."
  - key: "36b"
    status: MATCH
    reason: "A joint-return spouse born before January 2, 1961 would check the spouse age box, so the sa.spouse_extra refusal excludes that case. Otherwise $0 is correct."
  - key: "37"
    status: MATCH
    reason: "Matches \"Add lines 36a and 36b\"."
  - key: "38"
    status: MATCH
    reason: "Matches \"Add lines 13, 21, 30, and 37\"."
```
```
