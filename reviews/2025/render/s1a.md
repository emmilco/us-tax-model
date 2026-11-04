# Render comparison — s1a

The rendered English of every printed line of `Schedule 1-A (Form 1040) — Additional Deductions` (`rendered/2025/s1a.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c16da5d11ef36fcb2385479ec03574e8add506c6f29163b41e390a3c9e16e69f |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | fc0dadcd31c9a578e0cd374ef530e9dcbf2ea506b5ea328176d08c401ac0127c |
| lines judged | 43 |
| match / mismatch / unclear / missing | 42 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 18, 23, 35, 43, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 18, 23, 43, 101, 102, 103, 104, 106, 107, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| f1040s2 | 2025; created 2025-05-08 | 1, 2 | whole document | 29e3a05ca4dca4b5316833984170cff8815045c2e3957d048cb713ad90cb728f | - | 129b2541cce9743c9bde3a48fdfcc2512767d88b7cbbbe562d7989b117232d62 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040sc | 2025 | 3, 6, 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 3, 6, 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22, 23 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22, 23 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| f1040s1 | 2025; created 2025-07-25 | 1, 2 | whole document | 30004f72691a7078d8720e432e83110aa2bc3852ce9b45867becdb8c28222956 | - | 2293cadd525c2df84256455db693bbd46b710c62d28a98d503b1a6f8d8aea444 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| i4562 | 2025 | 4 | pages named by another document's citation | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | - | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |

## Lines

### 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **MATCH**

Model: Line 1 enters the amount from Form 1040 line 11b, as the form says.

### 2a — Enter any income from Puerto Rico that you excluded
Status: **MATCH**

Model: The program enters $0 and refuses any filer with excluded Puerto Rico income or a Form 2555 or 4563. The instructions say lines 2a–2e are completed only in those cases, so $0 is right for everyone the program keeps.

### 2b — Enter the amount from Form 2555, line 45
Status: **MATCH**

Model: Form 2555 line 45 applies only to filers already excluded by the line 2a refusal, so $0 is right within scope.

### 2c — Enter the amount from Form 2555, line 50
Status: **MATCH**

Model: Form 2555 line 50 applies only to filers already excluded by the line 2a refusal, so $0 is right within scope.

### 2d — Enter the amount from Form 4563, line 15
Status: **MATCH**

Model: Form 4563 line 15 applies only to filers already excluded by the line 2a refusal, so $0 is right within scope.

### 2e — Add lines 2a, 2b, 2c, and 2d
Status: **MATCH**

Model: Adds lines 2a through 2d, as the form says.

### 3 — Add lines 1 and 2e
Status: **MATCH**

Model: Adds lines 1 and 2e, as the form says.

### 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, bo
Status: **MATCH**

Model: With more than one employer it enters $0, matching "enter -0- on lines 4a and 4b". With one employer it enters the reported tips (W-2 box 7, Forms 4070, or box 14), which the instructions allow.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **MATCH**

Model: It enters $0 and refuses any filer whose Schedule 2 shows tax on unreported tips (Form 4137). That matches "If Form 4137 is not filed, enter -0-" for the cases the program keeps.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **MATCH**

Model: With one employer it enters the larger of line 4a or 4b. With more than one it enters worksheet line 2 (the sum of column (d)), as the instructions direct.

### 5 — Qualified tips received in the course of a trade or business
Status: **MATCH**

Model: It enters $0 and refuses filers who received tips in a trade or business (Schedule C) or have other Schedule C, E or F income, so $0 is right within scope.

### 6 — Add lines 4c and 5
Status: **MATCH**

Model: Adds lines 4c and 5, as the form says.

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **MATCH**

Model: Enters the smaller of line 6 or $25,000, as the form says.

### 8 — Enter the amount from line 3
Status: **MATCH**

Model: Enters the amount from line 3, as the form says.

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: Enters $300,000 if married filing jointly and $150,000 otherwise. Married filing separately never reaches this line because the Part II gate excludes it.

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **MATCH**

Model: Subtracts line 9 from line 8 and keeps a negative result. The "if zero or less" rule is applied at line 13.

### 12 — Multiply line 11 by $100
Status: **MATCH**

Model: Line 11 is the positive part of line 10 rounded down to whole thousands, and multiplying by 1/10 gives $100 per thousand. That equals "Multiply line 11 by $100".

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: It is zero for married filing separately or without a valid SSN. If line 8 is not more than line 9 it enters line 7; otherwise it subtracts line 12 from line 7, floored at zero. Both results match the form and the line 10 instruction.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **MATCH**

Model: It adds qualified overtime for each person with a valid SSN, figured by the employer-reported amount or methods 1–4 (÷3, ×1/2, ×1/4). The total includes overtime not in W-2 box 1, as the instructions direct, and other methods are refused.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **MATCH**

Model: It enters $0 and refuses overtime reported on Form 1099-NEC or 1099-MISC, so $0 is right within scope.

### 14c — Add lines 14a and 14b
Status: **MATCH**

Model: Adds lines 14a and 14b, as the form says.

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **MATCH**

Model: Enters the smaller of line 14c or $12,500 ($25,000 if married filing jointly), as the form says.

### 16 — Enter the amount from line 3
Status: **MATCH**

Model: Enters the amount from line 3, as the form says.

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: Enters $300,000 if married filing jointly and $150,000 otherwise. Married filing separately never reaches this line because the Part III gate excludes it.

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **MATCH**

Model: Subtracts line 17 from line 16. The "if zero or less" rule is applied at line 21.

### 20 — Multiply line 19 by $100
Status: **MATCH**

Model: The positive part of line 18 rounded down to whole thousands, times 1/10, equals "Multiply line 19 by $100".

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **MATCH**

Model: It is zero for married filing separately or without a valid SSN. If line 16 is not more than line 17 it enters line 15; otherwise it subtracts line 20 from line 15, floored at zero. Both results match the form.

### 23 — Add lines 22a and 22b, column (iii)
Status: **MATCH**

Model: It adds column (iii) for every loan, each being the loan's qualified interest minus the amount deducted elsewhere, floored at zero. This matches "Add lines 22a and 22b, column (iii)" and the statement the instructions require for more than two VINs.

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **MATCH**

Model: Enters the smaller of line 23 or $10,000, as the form says.

### 25 — Enter the amount from line 3
Status: **MATCH**

Model: Enters the amount from line 3, as the form says.

### 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **MATCH**

Model: Enters $200,000 if married filing jointly and $100,000 for all other filing statuses, matching the instructions.

### 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
Status: **MATCH**

Model: Subtracts line 26 from line 25. The "if zero or less" rule is applied at line 30.

### 29 — Multiply line 28 by $200
Status: **MATCH**

Model: Line 28 rounds the positive part of line 27 up to whole thousands, as the form says, and multiplying by 1/5 gives $200 per thousand.

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **MATCH**

Model: If line 25 is not more than line 26 it enters line 24. Otherwise it subtracts line 29 from line 24, floored at zero, as the form says.

### 31 — Enter the amount from line 3
Status: **MATCH**

Model: Enters the amount from line 3, gated on Part V applying.

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **MATCH**

Model: Enters $150,000 if married filing jointly and $75,000 otherwise, matching the instructions.

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **MATCH**

Model: Subtracts line 32 from line 31. The "if zero or less" rule is applied at line 35.

### 34 — Multiply line 33 by 6% (0.06)
Status: **MATCH**

Model: Multiplies the positive part of line 33 by 6%, as the form says.

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **MATCH**

Model: It enters $6,000 when line 31 is not more than line 32. Otherwise it subtracts line 34 from $6,000, floored at zero, as the form says.

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **MATCH**

Model: It enters line 35 if you were born before January 2, 1961 and have a valid SSN, and zero for married filing separately. A person who died before reaching 65 is refused.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **MISMATCH**

Restated: Choose — [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = true → helper "Line 36b for a spouse born before January 2, 1961, with a valid SSN"]

Model: The form requires "If you are married filing jointly, your spouse has a valid social security number..., and your spouse was born before January 2, 1961". The restatement checks only the spouse's birth date and SSN, not the joint filing status, so a spouse entry on a non-joint return could pass line 35 through.

Ruling: scope; project retained. A spouse entry exists only on a joint return: any other roster is refused at Form 1040 line 1a (household.roster_bad; Form 1040 page 1, 'If joint return, spouse's first name'), so whenever the spouse's birth date and SSN are tested the return is filed jointly (Schedule 1-A line 36b; i1040gi p. 110). Same reading as the earlier rounds.

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **MATCH**

Model: Adds lines 36a and 36b, as the form says.

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **MATCH**

Model: Adds lines 13, 21, 30, and 37, as the form says.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Line 1 enters the amount from Form 1040 line 11b, as the form says."
  - key: "2a"
    status: MATCH
    reason: "The program enters $0 and refuses any filer with excluded Puerto Rico income or a Form 2555 or 4563. The instructions say lines 2a–2e are completed only in those cases, so $0 is right for everyone the program keeps."
  - key: "2b"
    status: MATCH
    reason: "Form 2555 line 45 applies only to filers already excluded by the line 2a refusal, so $0 is right within scope."
  - key: "2c"
    status: MATCH
    reason: "Form 2555 line 50 applies only to filers already excluded by the line 2a refusal, so $0 is right within scope."
  - key: "2d"
    status: MATCH
    reason: "Form 4563 line 15 applies only to filers already excluded by the line 2a refusal, so $0 is right within scope."
  - key: "2e"
    status: MATCH
    reason: "Adds lines 2a through 2d, as the form says."
  - key: "3"
    status: MATCH
    reason: "Adds lines 1 and 2e, as the form says."
  - key: "4a"
    status: MATCH
    reason: "With more than one employer it enters $0, matching \"enter -0- on lines 4a and 4b\". With one employer it enters the reported tips (W-2 box 7, Forms 4070, or box 14), which the instructions allow."
  - key: "4b"
    status: MATCH
    reason: "It enters $0 and refuses any filer whose Schedule 2 shows tax on unreported tips (Form 4137). That matches \"If Form 4137 is not filed, enter -0-\" for the cases the program keeps."
  - key: "4c"
    status: MATCH
    reason: "With one employer it enters the larger of line 4a or 4b. With more than one it enters worksheet line 2 (the sum of column (d)), as the instructions direct."
  - key: "5"
    status: MATCH
    reason: "It enters $0 and refuses filers who received tips in a trade or business (Schedule C) or have other Schedule C, E or F income, so $0 is right within scope."
  - key: "6"
    status: MATCH
    reason: "Adds lines 4c and 5, as the form says."
  - key: "7"
    status: MATCH
    reason: "Enters the smaller of line 6 or $25,000, as the form says."
  - key: "8"
    status: MATCH
    reason: "Enters the amount from line 3, as the form says."
  - key: "9"
    status: MATCH
    reason: "Enters $300,000 if married filing jointly and $150,000 otherwise. Married filing separately never reaches this line because the Part II gate excludes it."
  - key: "10"
    status: MATCH
    reason: "Subtracts line 9 from line 8 and keeps a negative result. The \"if zero or less\" rule is applied at line 13."
  - key: "12"
    status: MATCH
    reason: "Line 11 is the positive part of line 10 rounded down to whole thousands, and multiplying by 1/10 gives $100 per thousand. That equals \"Multiply line 11 by $100\"."
  - key: "13"
    status: MATCH
    reason: "It is zero for married filing separately or without a valid SSN. If line 8 is not more than line 9 it enters line 7; otherwise it subtracts line 12 from line 7, floored at zero. Both results match the form and the line 10 instruction."
  - key: "14a"
    status: MATCH
    reason: "It adds qualified overtime for each person with a valid SSN, figured by the employer-reported amount or methods 1–4 (÷3, ×1/2, ×1/4). The total includes overtime not in W-2 box 1, as the instructions direct, and other methods are refused."
  - key: "14b"
    status: MATCH
    reason: "It enters $0 and refuses overtime reported on Form 1099-NEC or 1099-MISC, so $0 is right within scope."
  - key: "14c"
    status: MATCH
    reason: "Adds lines 14a and 14b, as the form says."
  - key: "15"
    status: MATCH
    reason: "Enters the smaller of line 14c or $12,500 ($25,000 if married filing jointly), as the form says."
  - key: "16"
    status: MATCH
    reason: "Enters the amount from line 3, as the form says."
  - key: "17"
    status: MATCH
    reason: "Enters $300,000 if married filing jointly and $150,000 otherwise. Married filing separately never reaches this line because the Part III gate excludes it."
  - key: "18"
    status: MATCH
    reason: "Subtracts line 17 from line 16. The \"if zero or less\" rule is applied at line 21."
  - key: "20"
    status: MATCH
    reason: "The positive part of line 18 rounded down to whole thousands, times 1/10, equals \"Multiply line 19 by $100\"."
  - key: "21"
    status: MATCH
    reason: "It is zero for married filing separately or without a valid SSN. If line 16 is not more than line 17 it enters line 15; otherwise it subtracts line 20 from line 15, floored at zero. Both results match the form."
  - key: "23"
    status: MATCH
    reason: "It adds column (iii) for every loan, each being the loan's qualified interest minus the amount deducted elsewhere, floored at zero. This matches \"Add lines 22a and 22b, column (iii)\" and the statement the instructions require for more than two VINs."
  - key: "24"
    status: MATCH
    reason: "Enters the smaller of line 23 or $10,000, as the form says."
  - key: "25"
    status: MATCH
    reason: "Enters the amount from line 3, as the form says."
  - key: "26"
    status: MATCH
    reason: "Enters $200,000 if married filing jointly and $100,000 for all other filing statuses, matching the instructions."
  - key: "27"
    status: MATCH
    reason: "Subtracts line 26 from line 25. The \"if zero or less\" rule is applied at line 30."
  - key: "29"
    status: MATCH
    reason: "Line 28 rounds the positive part of line 27 up to whole thousands, as the form says, and multiplying by 1/5 gives $200 per thousand."
  - key: "30"
    status: MATCH
    reason: "If line 25 is not more than line 26 it enters line 24. Otherwise it subtracts line 29 from line 24, floored at zero, as the form says."
  - key: "31"
    status: MATCH
    reason: "Enters the amount from line 3, gated on Part V applying."
  - key: "32"
    status: MATCH
    reason: "Enters $150,000 if married filing jointly and $75,000 otherwise, matching the instructions."
  - key: "33"
    status: MATCH
    reason: "Subtracts line 32 from line 31. The \"if zero or less\" rule is applied at line 35."
  - key: "34"
    status: MATCH
    reason: "Multiplies the positive part of line 33 by 6%, as the form says."
  - key: "35"
    status: MATCH
    reason: "It enters $6,000 when line 31 is not more than line 32. Otherwise it subtracts line 34 from $6,000, floored at zero, as the form says."
  - key: "36a"
    status: MATCH
    reason: "It enters line 35 if you were born before January 2, 1961 and have a valid SSN, and zero for married filing separately. A person who died before reaching 65 is refused."
  - key: "36b"
    status: MISMATCH
    reason: "The form requires \"If you are married filing jointly, your spouse has a valid social security number..., and your spouse was born before January 2, 1961\". The restatement checks only the spouse's birth date and SSN, not the joint filing status, so a spouse entry on a non-joint return could pass line 35 through."
  - key: "37"
    status: MATCH
    reason: "Adds lines 36a and 36b, as the form says."
  - key: "38"
    status: MATCH
    reason: "Adds lines 13, 21, 30, and 37, as the form says."
```
```
