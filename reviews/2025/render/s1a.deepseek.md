# Render comparison — s1a

The rendered English of every printed line of `Schedule 1-A (Form 1040) — Additional Deductions` (`rendered/2025/s1a.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a4f7e3432b9fe9f40e75c4de5258187671cdb19eadd30a7b1468a88ecf8e4a28 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | fc0dadcd31c9a578e0cd374ef530e9dcbf2ea506b5ea328176d08c401ac0127c |
| lines judged | 43 |
| match / mismatch / unclear / missing | 41 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 18, 95, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 18, 95, 101, 102, 103, 104, 106, 107, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| f1040s2 | 2025; created 2025-05-08 | 1, 2 | whole document | 29e3a05ca4dca4b5316833984170cff8815045c2e3957d048cb713ad90cb728f | - | 129b2541cce9743c9bde3a48fdfcc2512767d88b7cbbbe562d7989b117232d62 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040sc | 2025 | 3, 6, 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 3, 6, 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p560 | For use in preparing 2025 returns | 11, 16, 38 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 11, 16, 38 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| iw2w3 | 2025; printed date 2025-02-19 | 20 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 20 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| p590a | 2025 | 30, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |
| f1040s1 | 2025; created 2025-07-25 | 1, 2 | whole document | 30004f72691a7078d8720e432e83110aa2bc3852ce9b45867becdb8c28222956 | - | 2293cadd525c2df84256455db693bbd46b710c62d28a98d503b1a6f8d8aea444 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| i4562 | 2025 | 4 | pages named by another document's citation | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | - | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |

## Lines

### 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **MATCH**

Model: Restatement uses Form 1040 line 11b, as the IRS line directs.

### 2a — Enter any income from Puerto Rico that you excluded
Status: **MATCH**

Model: With no excluded Puerto Rico income, Form 2555, or Form 4563 amounts, line 2a is zero; the refusal covers those excluded cases for lines 2a-2d.

### 2b — Enter the amount from Form 2555, line 45
Status: **MATCH**

Model: With no Form 2555, line 2b is zero; the line 2a refusal covers Forms 2555 and 4563 for lines 2a-2d.

### 2c — Enter the amount from Form 2555, line 50
Status: **MATCH**

Model: With no Form 2555, line 2c is zero; the line 2a refusal covers Forms 2555 and 4563 for lines 2a-2d.

### 2d — Enter the amount from Form 4563, line 15
Status: **MATCH**

Model: With no Form 4563, line 2d is zero; the line 2a refusal covers Forms 2555 and 4563 for lines 2a-2d.

### 2e — Add lines 2a, 2b, 2c, and 2d
Status: **MATCH**

Model: Adds lines 2a through 2d, as the IRS line directs.

### 3 — Add lines 1 and 2e
Status: **MATCH**

Model: Adds lines 1 and 2e, as the IRS line directs.

### 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, bo
Status: **MATCH**

Model: Uses Form W-2 box 7 qualified tips with the box 5 caveat and zeroes when there is more than one employer, as the IRS line and instructions direct.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **MATCH**

Model: With no supported Form 4137 amount, line 4b is zero; Form 4137 cases are refused.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **MATCH**

Model: Uses the larger of 4a or 4b for one employer and the multiple-employer worksheet otherwise, as the IRS line directs.

### 5 — Qualified tips received in the course of a trade or business
Status: **MATCH**

Model: Zero is correct when no trade-or-business tips are supported; the program refuses Schedule C trade-or-business tip cases.

### 6 — Add lines 4c and 5
Status: **MATCH**

Model: Adds lines 4c and 5, as the IRS line directs.

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **MATCH**

Model: Enters the smaller of line 6 or $25,000, as the IRS line directs.

### 8 — Enter the amount from line 3
Status: **MATCH**

Model: Enters the amount from line 3, as the IRS line directs.

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: Uses $150,000, or $300,000 for married filing jointly, as the IRS line directs.

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **MATCH**

Model: Subtracts line 9 from line 8 and implements the zero-or-less direction to use line 7 on line 13.

### 12 — Multiply line 11 by $100
Status: **MATCH**

Model: Multiplies the line 11 thousands figure by $100, as the IRS lines 11 and 12 direct.

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: Computes line 7 less line 12, floored at zero, with line 7 used when MAGI is not above the threshold; MFS, SSN, and business-tip refusals apply.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **MATCH**

Model: Sums qualified overtime compensation includible on line 14a, including the Form W-2 box 1 amount and supported exceptions, as the IRS line and instructions direct.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **MATCH**

Model: Zero is correct when no 1099-NEC or 1099-MISC overtime is supported; nonemployee overtime cases are refused.

### 14c — Add lines 14a and 14b
Status: **MATCH**

Model: Adds lines 14a and 14b, as the IRS line directs.

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **MATCH**

Model: Enters the smaller of line 14c or $12,500, or $25,000 if married filing jointly, as the IRS line directs.

### 16 — Enter the amount from line 3
Status: **MATCH**

Model: Enters the amount from line 3, as the IRS line directs.

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: Uses $150,000, or $300,000 for married filing jointly, as the IRS line directs.

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **MATCH**

Model: Subtracts line 17 from line 16 and implements the zero-or-less direction to use line 15 on line 21.

### 20 — Multiply line 19 by $100
Status: **MATCH**

Model: Multiplies the line 19 thousands figure by $100, as the IRS lines 19 and 20 direct.

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **MATCH**

Model: Computes line 15 less line 20, floored at zero, with line 15 used when MAGI is not above the threshold; MFS, SSN, and business-overtime refusals apply.

### 23 — Add lines 22a and 22b, column (iii)
Status: **MISMATCH**

Restated: Choose — [helper "Did you pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = true → helper "Add lines 22a and 22b, column (iii), and any further loans on the attached statement"]

Model: Line 23 adds column (iii), but the program's column (iii) subtracts only Schedule C interest; IRS column (ii) is 'Deducted on Schedule C, Schedule E, or Schedule F.'

Ruling: scope; i1040gi p. 110, Part IV, before Line 22: "if you deducted some or all of the interest that you paid or accrued on your loan as interest on Schedule C, Schedule E, or Schedule F, then you can’t deduct that same interest as QPVLI on Schedule 1-A." Column (ii) asks only for interest deducted on Schedule C (carloan.col_ii_input, zero without a Schedule C) because Schedule E and Schedule F are outside the tool: the Schedule 1 screen scope.schedule1 refuses rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1) and farm income (Schedule F) (forms/2025/scope.yaml). No return in scope can have the interest deducted on Schedule E or F, so line 23 is not overstated on any computed return.

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **MATCH**

Model: Enters the smaller of line 23 or $10,000, as the IRS line directs.

### 25 — Enter the amount from line 3
Status: **MATCH**

Model: Enters the amount from line 3, as the IRS line directs.

### 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **MATCH**

Model: Uses $100,000, or $200,000 for married filing jointly, as the IRS line directs.

### 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
Status: **MATCH**

Model: Subtracts line 26 from line 25 and implements the zero-or-less direction to use line 24 on line 30.

### 29 — Multiply line 28 by $200
Status: **MATCH**

Model: Multiplies the line 28 thousands figure, rounded up as required, by $200.

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **MATCH**

Model: Computes line 24 less line 29, floored at zero, and uses line 24 when line 27 is zero or less.

### 31 — Enter the amount from line 3
Status: **MATCH**

Model: Enters the amount from line 3 when the Part V senior conditions are met.

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **MATCH**

Model: Uses $75,000, or $150,000 for married filing jointly, as the IRS line directs.

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **MATCH**

Model: Subtracts line 32 from line 31 and implements the zero-or-less direction to enter $6,000 on line 35.

### 34 — Multiply line 33 by 6% (0.06)
Status: **MATCH**

Model: Multiplies line 33 by 6% (0.06); the zero floor implements the line 33 zero-or-less rule.

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **MATCH**

Model: Subtracts line 34 from $6,000, floored at zero, and enters $6,000 when line 33 is zero or less.

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **MATCH**

Model: Enters line 35 for a filer born before January 2, 1961 with a valid SSN, subject to the MFS and decedent refusals.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **MISMATCH**

Restated: Choose — [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = true → helper "Line 36b for a spouse born before January 2, 1961, with a valid SSN"]

Model: IRS line 36b applies only 'If you are married filing jointly'; the restatement checks only that the spouse was born before January 2, 1961 and has a valid SSN.

Ruling: scope; project retained. Schedule 1-A line 36b: "If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35"; i1040gi p. 110: "If you are married, you must file a joint return with your spouse to claim this deduction." The English gates line 36b on the spouse entry, and a spouse entry exists only on a joint return: household.roster_ok requires one entry for the spouse exactly when filing jointly and any other roster is refused at household.roster_bad (Form 1040 page 1, "If joint return, spouse’s first name"; fixtures stage13.refuse.single_with_spouse and stage13.refuse.joint_without_spouse, both refused at household.roster_bad, witnesses in triage/s179.json). A head of household or other non-joint return with a spouse entry is therefore refused, never given line 35; married filing separately is refused for the whole return at s3.mfs. The model read the line 36b English without the roster refusal located elsewhere.

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **MATCH**

Model: Adds lines 36a and 36b, as the IRS line directs.

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **MATCH**

Model: Adds lines 13, 21, 30, and 37, as the IRS line directs.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Restatement uses Form 1040 line 11b, as the IRS line directs."
  - key: "2a"
    status: MATCH
    reason: "With no excluded Puerto Rico income, Form 2555, or Form 4563 amounts, line 2a is zero; the refusal covers those excluded cases for lines 2a-2d."
  - key: "2b"
    status: MATCH
    reason: "With no Form 2555, line 2b is zero; the line 2a refusal covers Forms 2555 and 4563 for lines 2a-2d."
  - key: "2c"
    status: MATCH
    reason: "With no Form 2555, line 2c is zero; the line 2a refusal covers Forms 2555 and 4563 for lines 2a-2d."
  - key: "2d"
    status: MATCH
    reason: "With no Form 4563, line 2d is zero; the line 2a refusal covers Forms 2555 and 4563 for lines 2a-2d."
  - key: "2e"
    status: MATCH
    reason: "Adds lines 2a through 2d, as the IRS line directs."
  - key: "3"
    status: MATCH
    reason: "Adds lines 1 and 2e, as the IRS line directs."
  - key: "4a"
    status: MATCH
    reason: "Uses Form W-2 box 7 qualified tips with the box 5 caveat and zeroes when there is more than one employer, as the IRS line and instructions direct."
  - key: "4b"
    status: MATCH
    reason: "With no supported Form 4137 amount, line 4b is zero; Form 4137 cases are refused."
  - key: "4c"
    status: MATCH
    reason: "Uses the larger of 4a or 4b for one employer and the multiple-employer worksheet otherwise, as the IRS line directs."
  - key: "5"
    status: MATCH
    reason: "Zero is correct when no trade-or-business tips are supported; the program refuses Schedule C trade-or-business tip cases."
  - key: "6"
    status: MATCH
    reason: "Adds lines 4c and 5, as the IRS line directs."
  - key: "7"
    status: MATCH
    reason: "Enters the smaller of line 6 or $25,000, as the IRS line directs."
  - key: "8"
    status: MATCH
    reason: "Enters the amount from line 3, as the IRS line directs."
  - key: "9"
    status: MATCH
    reason: "Uses $150,000, or $300,000 for married filing jointly, as the IRS line directs."
  - key: "10"
    status: MATCH
    reason: "Subtracts line 9 from line 8 and implements the zero-or-less direction to use line 7 on line 13."
  - key: "12"
    status: MATCH
    reason: "Multiplies the line 11 thousands figure by $100, as the IRS lines 11 and 12 direct."
  - key: "13"
    status: MATCH
    reason: "Computes line 7 less line 12, floored at zero, with line 7 used when MAGI is not above the threshold; MFS, SSN, and business-tip refusals apply."
  - key: "14a"
    status: MATCH
    reason: "Sums qualified overtime compensation includible on line 14a, including the Form W-2 box 1 amount and supported exceptions, as the IRS line and instructions direct."
  - key: "14b"
    status: MATCH
    reason: "Zero is correct when no 1099-NEC or 1099-MISC overtime is supported; nonemployee overtime cases are refused."
  - key: "14c"
    status: MATCH
    reason: "Adds lines 14a and 14b, as the IRS line directs."
  - key: "15"
    status: MATCH
    reason: "Enters the smaller of line 14c or $12,500, or $25,000 if married filing jointly, as the IRS line directs."
  - key: "16"
    status: MATCH
    reason: "Enters the amount from line 3, as the IRS line directs."
  - key: "17"
    status: MATCH
    reason: "Uses $150,000, or $300,000 for married filing jointly, as the IRS line directs."
  - key: "18"
    status: MATCH
    reason: "Subtracts line 17 from line 16 and implements the zero-or-less direction to use line 15 on line 21."
  - key: "20"
    status: MATCH
    reason: "Multiplies the line 19 thousands figure by $100, as the IRS lines 19 and 20 direct."
  - key: "21"
    status: MATCH
    reason: "Computes line 15 less line 20, floored at zero, with line 15 used when MAGI is not above the threshold; MFS, SSN, and business-overtime refusals apply."
  - key: "23"
    status: MISMATCH
    reason: "Line 23 adds column (iii), but the program's column (iii) subtracts only Schedule C interest; IRS column (ii) is 'Deducted on Schedule C, Schedule E, or Schedule F.'"
  - key: "24"
    status: MATCH
    reason: "Enters the smaller of line 23 or $10,000, as the IRS line directs."
  - key: "25"
    status: MATCH
    reason: "Enters the amount from line 3, as the IRS line directs."
  - key: "26"
    status: MATCH
    reason: "Uses $100,000, or $200,000 for married filing jointly, as the IRS line directs."
  - key: "27"
    status: MATCH
    reason: "Subtracts line 26 from line 25 and implements the zero-or-less direction to use line 24 on line 30."
  - key: "29"
    status: MATCH
    reason: "Multiplies the line 28 thousands figure, rounded up as required, by $200."
  - key: "30"
    status: MATCH
    reason: "Computes line 24 less line 29, floored at zero, and uses line 24 when line 27 is zero or less."
  - key: "31"
    status: MATCH
    reason: "Enters the amount from line 3 when the Part V senior conditions are met."
  - key: "32"
    status: MATCH
    reason: "Uses $75,000, or $150,000 for married filing jointly, as the IRS line directs."
  - key: "33"
    status: MATCH
    reason: "Subtracts line 32 from line 31 and implements the zero-or-less direction to enter $6,000 on line 35."
  - key: "34"
    status: MATCH
    reason: "Multiplies line 33 by 6% (0.06); the zero floor implements the line 33 zero-or-less rule."
  - key: "35"
    status: MATCH
    reason: "Subtracts line 34 from $6,000, floored at zero, and enters $6,000 when line 33 is zero or less."
  - key: "36a"
    status: MATCH
    reason: "Enters line 35 for a filer born before January 2, 1961 with a valid SSN, subject to the MFS and decedent refusals."
  - key: "36b"
    status: MISMATCH
    reason: "IRS line 36b applies only 'If you are married filing jointly'; the restatement checks only that the spouse was born before January 2, 1961 and has a valid SSN."
  - key: "37"
    status: MATCH
    reason: "Adds lines 36a and 36b, as the IRS line directs."
  - key: "38"
    status: MATCH
    reason: "Adds lines 13, 21, 30, and 37, as the IRS line directs."
```
