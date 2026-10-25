# Render comparison — s1a

The rendered English of every printed line of `Schedule 1-A (Form 1040) — Additional Deductions` (`rendered/2025/s1a.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 95a14d953d8ae73409b711073737d95e3855f25a5ba082a43f82b0dd0ac1a8dd |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: IRS line 1 is the same entry from Form 1040 line 11b.

### 2a — Enter any income from Puerto Rico that you excluded
Status: **MATCH**

Model: IRS line 2a is excluded Puerto Rico income; the program enters zero when not excluded and refuses the excluded-income cases for lines 2a through 2d.

### 2b — Enter the amount from Form 2555, line 45
Status: **MATCH**

Model: IRS line 2b is Form 2555 line 45; with no excluded income it is zero, and the Part I refusal covers the cases where Form 2555 applies.

### 2c — Enter the amount from Form 2555, line 50
Status: **MATCH**

Model: IRS line 2c is Form 2555 line 50; with no excluded income it is zero, and the Part I refusal covers the cases where Form 2555 applies.

### 2d — Enter the amount from Form 4563, line 15
Status: **MATCH**

Model: IRS line 2d is Form 4563 line 15; with no excluded income it is zero, and the Part I refusal covers the cases where Form 4563 applies.

### 2e — Add lines 2a, 2b, 2c, and 2d
Status: **MATCH**

Model: IRS line 2e adds lines 2a through 2d, as the restatement does.

### 3 — Add lines 1 and 2e
Status: **MATCH**

Model: IRS line 3 adds lines 1 and 2e, as the restatement does.

### 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, bo
Status: **MATCH**

Model: IRS line 4a is qualified tips from Form W-2 box 7, with the stated box 5 and non-social-security-tip caveats; the helper also zeros multi-employer cases as line 4a directs.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **MATCH**

Model: IRS line 4b is Form 4137 line 1 row A column (c), or zero if no Form 4137; the refusal excludes Form 4137 cases.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **MATCH**

Model: IRS line 4c uses the larger of lines 4a and 4b for one employer and the worksheet for more than one employer; the helper does the same.

### 5 — Qualified tips received in the course of a trade or business
Status: **MATCH**

Model: IRS line 5 is trade-or-business qualified tips; the program refuses those business-tip cases and otherwise enters zero.

### 6 — Add lines 4c and 5
Status: **MATCH**

Model: IRS line 6 adds lines 4c and 5, as the restatement does.

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **MATCH**

Model: IRS line 7 is the smaller of line 6 or $25,000, as the restatement does.

### 8 — Enter the amount from line 3
Status: **MATCH**

Model: IRS line 8 is the amount from line 3, as the restatement does.

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: IRS line 9 is $150,000, or $300,000 if married filing jointly; the Part II gate excludes married filing separately.

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **MATCH**

Model: IRS line 10 subtracts line 9 from line 8 and notes the zero-or-less consequence for line 13.

### 12 — Multiply line 11 by $100
Status: **MATCH**

Model: IRS line 12 multiplies line 11 by $100; the helper represents line 11 in thousands and multiplies by 1/10, which gives the same result.

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: IRS line 13 subtracts line 12 from line 7, floors at zero, and line 10 sends line 7 when line 10 is zero or less; the helper adds the MFS and valid-SSN limits.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **MATCH**

Model: IRS line 14a is qualified overtime compensation from Form W-2, including the instruction for amounts not reported in box 1; the helper totals the W-2 worksheet column.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **MATCH**

Model: IRS line 14b is qualified overtime on Form 1099-NEC box 1 or Form 1099-MISC box 3; the program refuses those nonemployee cases and otherwise enters zero.

### 14c — Add lines 14a and 14b
Status: **MATCH**

Model: IRS line 14c adds lines 14a and 14b, as the restatement does.

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **MATCH**

Model: IRS line 15 is the smaller of line 14c or $12,500 ($25,000 if married filing jointly); the Part III gate excludes married filing separately.

### 16 — Enter the amount from line 3
Status: **MATCH**

Model: IRS line 16 is the amount from line 3, as the restatement does.

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **MATCH**

Model: IRS line 17 is $150,000, or $300,000 if married filing jointly; the Part III gate excludes married filing separately.

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **MATCH**

Model: IRS line 18 subtracts line 17 from line 16 and notes the zero-or-less consequence for line 21.

### 20 — Multiply line 19 by $100
Status: **MATCH**

Model: IRS line 20 multiplies line 19 by $100; the helper represents line 19 in thousands and multiplies by 1/10, which gives the same result.

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **MATCH**

Model: IRS line 21 subtracts line 20 from line 15 and floors at zero, while line 18 sends line 15 when line 18 is zero or less; the helper adds the MFS and valid-SSN limits.

### 23 — Add lines 22a and 22b, column (iii)
Status: **MATCH**

Model: IRS line 23 adds the column (iii) QPVLI amounts; including further loans on the attached statement follows the line 22 instruction for more than two VINs.

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **MATCH**

Model: IRS line 24 is the smaller of line 23 or $10,000, as the restatement does.

### 25 — Enter the amount from line 3
Status: **MATCH**

Model: IRS line 25 is the amount from line 3, as the restatement does.

### 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **MATCH**

Model: IRS line 26 is $100,000, or $200,000 if married filing jointly, as the helper applies.

### 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
Status: **MATCH**

Model: IRS line 27 subtracts line 26 from line 25 and notes the zero-or-less consequence for line 30.

### 29 — Multiply line 28 by $200
Status: **MATCH**

Model: IRS line 29 multiplies line 28 by $200; the helper represents line 28 in thousands and multiplies by 1/5, which gives the same result.

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **MATCH**

Model: IRS line 30 subtracts line 29 from line 24 and floors at zero, and line 27 sends line 24 when line 27 is zero or less.

### 31 — Enter the amount from line 3
Status: **MATCH**

Model: IRS line 31 is the amount from line 3; the Part V gate excludes nonqualifying statuses and the helper handles the joint filing and valid-SSN limits.

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **MATCH**

Model: IRS line 32 is $75,000, or $150,000 if married filing jointly; the Part V gate excludes married filing separately.

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **MATCH**

Model: IRS line 33 subtracts line 32 from line 31 and notes the zero-or-less consequence for line 35.

### 34 — Multiply line 33 by 6% (0.06)
Status: **MATCH**

Model: IRS line 34 multiplies line 33 by 6%; using zero when line 33 is zero or less is consistent with the line 33 and line 35 instructions.

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **MATCH**

Model: IRS line 35 subtracts line 34 from $6,000 and floors at zero; when line 33 is zero or less, the line 33 instruction sends $6,000 to line 35.

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **MATCH**

Model: IRS line 36a requires a valid SSN and birth before January 2, 1961, and Part V is joint-only; the helper adds the MFS zero and the SSN and decedent limits.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **MISMATCH**

Restated: Choose — [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = true → helper "Line 36b for a spouse born before January 2, 1961, with a valid SSN"]

Model: IRS line 36b applies only "If you are married filing jointly," with spouse valid SSN and birth before January 2, 1961; the restatement triggers on the spouse SSN and birth date alone, so it could compute line 36b for a non-MFJ filer such as married filing separately.

Ruling: open

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **MATCH**

Model: IRS line 37 adds lines 36a and 36b, as the restatement does.

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **MATCH**

Model: IRS line 38 adds lines 13, 21, 30, and 37, as the restatement does.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "IRS line 1 is the same entry from Form 1040 line 11b."
  - key: "2a"
    status: MATCH
    reason: "IRS line 2a is excluded Puerto Rico income; the program enters zero when not excluded and refuses the excluded-income cases for lines 2a through 2d."
  - key: "2b"
    status: MATCH
    reason: "IRS line 2b is Form 2555 line 45; with no excluded income it is zero, and the Part I refusal covers the cases where Form 2555 applies."
  - key: "2c"
    status: MATCH
    reason: "IRS line 2c is Form 2555 line 50; with no excluded income it is zero, and the Part I refusal covers the cases where Form 2555 applies."
  - key: "2d"
    status: MATCH
    reason: "IRS line 2d is Form 4563 line 15; with no excluded income it is zero, and the Part I refusal covers the cases where Form 4563 applies."
  - key: "2e"
    status: MATCH
    reason: "IRS line 2e adds lines 2a through 2d, as the restatement does."
  - key: "3"
    status: MATCH
    reason: "IRS line 3 adds lines 1 and 2e, as the restatement does."
  - key: "4a"
    status: MATCH
    reason: "IRS line 4a is qualified tips from Form W-2 box 7, with the stated box 5 and non-social-security-tip caveats; the helper also zeros multi-employer cases as line 4a directs."
  - key: "4b"
    status: MATCH
    reason: "IRS line 4b is Form 4137 line 1 row A column (c), or zero if no Form 4137; the refusal excludes Form 4137 cases."
  - key: "4c"
    status: MATCH
    reason: "IRS line 4c uses the larger of lines 4a and 4b for one employer and the worksheet for more than one employer; the helper does the same."
  - key: "5"
    status: MATCH
    reason: "IRS line 5 is trade-or-business qualified tips; the program refuses those business-tip cases and otherwise enters zero."
  - key: "6"
    status: MATCH
    reason: "IRS line 6 adds lines 4c and 5, as the restatement does."
  - key: "7"
    status: MATCH
    reason: "IRS line 7 is the smaller of line 6 or $25,000, as the restatement does."
  - key: "8"
    status: MATCH
    reason: "IRS line 8 is the amount from line 3, as the restatement does."
  - key: "9"
    status: MATCH
    reason: "IRS line 9 is $150,000, or $300,000 if married filing jointly; the Part II gate excludes married filing separately."
  - key: "10"
    status: MATCH
    reason: "IRS line 10 subtracts line 9 from line 8 and notes the zero-or-less consequence for line 13."
  - key: "12"
    status: MATCH
    reason: "IRS line 12 multiplies line 11 by $100; the helper represents line 11 in thousands and multiplies by 1/10, which gives the same result."
  - key: "13"
    status: MATCH
    reason: "IRS line 13 subtracts line 12 from line 7, floors at zero, and line 10 sends line 7 when line 10 is zero or less; the helper adds the MFS and valid-SSN limits."
  - key: "14a"
    status: MATCH
    reason: "IRS line 14a is qualified overtime compensation from Form W-2, including the instruction for amounts not reported in box 1; the helper totals the W-2 worksheet column."
  - key: "14b"
    status: MATCH
    reason: "IRS line 14b is qualified overtime on Form 1099-NEC box 1 or Form 1099-MISC box 3; the program refuses those nonemployee cases and otherwise enters zero."
  - key: "14c"
    status: MATCH
    reason: "IRS line 14c adds lines 14a and 14b, as the restatement does."
  - key: "15"
    status: MATCH
    reason: "IRS line 15 is the smaller of line 14c or $12,500 ($25,000 if married filing jointly); the Part III gate excludes married filing separately."
  - key: "16"
    status: MATCH
    reason: "IRS line 16 is the amount from line 3, as the restatement does."
  - key: "17"
    status: MATCH
    reason: "IRS line 17 is $150,000, or $300,000 if married filing jointly; the Part III gate excludes married filing separately."
  - key: "18"
    status: MATCH
    reason: "IRS line 18 subtracts line 17 from line 16 and notes the zero-or-less consequence for line 21."
  - key: "20"
    status: MATCH
    reason: "IRS line 20 multiplies line 19 by $100; the helper represents line 19 in thousands and multiplies by 1/10, which gives the same result."
  - key: "21"
    status: MATCH
    reason: "IRS line 21 subtracts line 20 from line 15 and floors at zero, while line 18 sends line 15 when line 18 is zero or less; the helper adds the MFS and valid-SSN limits."
  - key: "23"
    status: MATCH
    reason: "IRS line 23 adds the column (iii) QPVLI amounts; including further loans on the attached statement follows the line 22 instruction for more than two VINs."
  - key: "24"
    status: MATCH
    reason: "IRS line 24 is the smaller of line 23 or $10,000, as the restatement does."
  - key: "25"
    status: MATCH
    reason: "IRS line 25 is the amount from line 3, as the restatement does."
  - key: "26"
    status: MATCH
    reason: "IRS line 26 is $100,000, or $200,000 if married filing jointly, as the helper applies."
  - key: "27"
    status: MATCH
    reason: "IRS line 27 subtracts line 26 from line 25 and notes the zero-or-less consequence for line 30."
  - key: "29"
    status: MATCH
    reason: "IRS line 29 multiplies line 28 by $200; the helper represents line 28 in thousands and multiplies by 1/5, which gives the same result."
  - key: "30"
    status: MATCH
    reason: "IRS line 30 subtracts line 29 from line 24 and floors at zero, and line 27 sends line 24 when line 27 is zero or less."
  - key: "31"
    status: MATCH
    reason: "IRS line 31 is the amount from line 3; the Part V gate excludes nonqualifying statuses and the helper handles the joint filing and valid-SSN limits."
  - key: "32"
    status: MATCH
    reason: "IRS line 32 is $75,000, or $150,000 if married filing jointly; the Part V gate excludes married filing separately."
  - key: "33"
    status: MATCH
    reason: "IRS line 33 subtracts line 32 from line 31 and notes the zero-or-less consequence for line 35."
  - key: "34"
    status: MATCH
    reason: "IRS line 34 multiplies line 33 by 6%; using zero when line 33 is zero or less is consistent with the line 33 and line 35 instructions."
  - key: "35"
    status: MATCH
    reason: "IRS line 35 subtracts line 34 from $6,000 and floors at zero; when line 33 is zero or less, the line 33 instruction sends $6,000 to line 35."
  - key: "36a"
    status: MATCH
    reason: "IRS line 36a requires a valid SSN and birth before January 2, 1961, and Part V is joint-only; the helper adds the MFS zero and the SSN and decedent limits."
  - key: "36b"
    status: MISMATCH
    reason: 'IRS line 36b applies only "If you are married filing jointly," with spouse valid SSN and birth before January 2, 1961; the restatement triggers on the spouse SSN and birth date alone, so it could compute line 36b for a non-MFJ filer such as married filing separately.'
  - key: "37"
    status: MATCH
    reason: "IRS line 37 adds lines 36a and 36b, as the restatement does."
  - key: "38"
    status: MATCH
    reason: "IRS line 38 adds lines 13, 21, 30, and 37, as the restatement does."
```
