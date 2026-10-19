# Class M hand-work — s1a

`Schedule 1-A (Form 1040) — Additional Deductions` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 1 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104, 105, 106, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104, 106, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.s1a.1 — prompt sha256 e6d9f4578cd7f0d000559e79375ac0661d7906d4237c2e63384a2d3f95d1b7d7; branches: s1a.tips:true, s1a.tip_multi:true, s1a.tip_ssn:true, s1a.part2:true, s1a.line4a_calc#0, s1a.line4a#1, s1a.line4b#1, s1a.line4c_one:left, s1a.line4c_calc#0, s1a.line4c#1, s1a.line5#1, s1a.line6#1, s1a.line7_calc:right, s1a.line7#1, s1a.line8#1, s1a.line9_calc#1, s1a.line9#1, s1a.line10#1, s1a.line10_over:false, s1a.line10_pos:floor, s1a.line12#1, s1a.line13_figured:positive, s1a.line13_amount#0, s1a.line13_ssn#1, s1a.line13_claim#1, s1a.line13#1, s1a.overtime:true, s1a.ot_ssn:true, s1a.part3:true, s1a.line14a#1, s1a.line14b#1, s1a.line14c#1, s1a.ot_max#1, s1a.line15_calc:right, s1a.line15#1, s1a.line16#1, s1a.line17_calc#1, s1a.line17#1, s1a.line18#1, s1a.line18_over:false, s1a.line18_pos:floor, s1a.line20#1, s1a.line21_figured:positive, s1a.line21_amount#0, s1a.line21_ssn#1, s1a.line21_claim#1, s1a.line21#1, s1a.carloan:false, s1a.line23#0, s1a.part4:false, s1a.line24_calc:left, s1a.line24#0, s1a.line25#0, s1a.line26_calc#1, s1a.line26#0, s1a.line27#0, s1a.line27_over:false, s1a.line27_pos:floor, s1a.line29#0, s1a.line30_figured:floor, s1a.line30_amount#0, s1a.line30#0, s1a.senior_any:true, s1a.part5:true, s1a.line31#1, s1a.line32_calc#1, s1a.line32#1, s1a.line33#1, s1a.line33_over:true, s1a.line33_pos:positive, s1a.line34#1, s1a.line35_figured:floor, s1a.line35_calc#1, s1a.line35#1, s1a.died_before_65:false, s1a.senior_decedent:false, s1a.line36a_senior#1, s1a.line36a_claim#1, s1a.line36a#0, s1a.spouse_senior:true, s1a.spouse_died_before_65:false, s1a.spouse_senior_decedent:false, s1a.line36b#1

### classm.s1a.1 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $266,763.00

### classm.s1a.1 — 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 3 — Add lines 1 and 2e
Status: **AGREE**

Value: $266,763.00

### classm.s1a.1 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $29,071.00

### classm.s1a.1 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $29,071.00

### classm.s1a.1 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $25,000.00

### classm.s1a.1 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $266,763.00

### classm.s1a.1 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $300,000.00

### classm.s1a.1 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $-33,237.00

### classm.s1a.1 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $25,000.00

### classm.s1a.1 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $30,000.00

### classm.s1a.1 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $30,000.00

### classm.s1a.1 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $25,000.00

### classm.s1a.1 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $266,763.00

### classm.s1a.1 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $300,000.00

### classm.s1a.1 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $-33,237.00

### classm.s1a.1 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $25,000.00

### classm.s1a.1 — 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 25 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 29 — Multiply line 28 by $200
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 31 — Enter the amount from line 3
Status: **AGREE**

Value: $266,763.00

### classm.s1a.1 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $150,000.00

### classm.s1a.1 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $116,763.00

### classm.s1a.1 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $7,005.78

### classm.s1a.1 — 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 36a — If you have a valid social security number (see instructions) and were born befo
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 36b — If you are married filing jointly, your spouse has a valid social security numbe
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, 
Status: **AGREE**

Value: $50,000.00

## Raw responses

### classm.s1a.1

```yaml
lines:
  - printed: "1"
    value: "266763.00"
    work: "Form 1040, line 11b = 266,763.00"
  - printed: "2a"
    value: "0.00"
    work: "No excluded Puerto Rico income was given"
  - printed: "2b"
    value: "0.00"
    work: "No Form 2555 was given"
  - printed: "2c"
    value: "0.00"
    work: "No Form 2555 was given"
  - printed: "2d"
    value: "0.00"
    work: "No Form 4563 was given"
  - printed: "2e"
    value: "0.00"
    work: "0 + 0 + 0 + 0 = 0"
  - printed: "3"
    value: "266763.00"
    work: "266,763.00 + 0 = 266,763.00"
  - printed: "4a"
    value: "0.00"
    work: "Spouse had more than one employer, so enter -0-"
  - printed: "4b"
    value: "0.00"
    work: "Spouse had more than one employer, so enter -0-"
  - printed: "4c"
    value: "29071.00"
    work: "More-than-one-employer worksheet, column (d): spouse 29,071 + taxpayer 0"
  - printed: "5"
    value: "0.00"
    work: "No qualified tips from a trade or business"
  - printed: "6"
    value: "29071.00"
    work: "29,071 + 0"
  - printed: "7"
    value: "25000.00"
    work: "Smaller of 29,071 or 25,000"
  - printed: "8"
    value: "266763.00"
    work: "Line 3"
  - printed: "9"
    value: "300000.00"
    work: "Married filing jointly"
  - printed: "10"
    value: "-33237.00"
    work: "266,763 - 300,000 = -33,237; zero or less, so line 7 goes to line 13"
  - printed: "12"
    value: "blank"
    work: "Skipped because line 10 is zero or less"
  - printed: "13"
    value: "25000.00"
    work: "Line 10 is zero or less, so enter line 7"
  - printed: "14a"
    value: "30000.00"
    work: "Overtime worksheet column (b): spouse 30,000 + taxpayer 0"
  - printed: "14b"
    value: "0.00"
    work: "No 1099 overtime"
  - printed: "14c"
    value: "30000.00"
    work: "30,000 + 0"
  - printed: "15"
    value: "25000.00"
    work: "Smaller of 30,000 or 25,000 (married filing jointly)"
  - printed: "16"
    value: "266763.00"
    work: "Line 3"
  - printed: "17"
    value: "300000.00"
    work: "Married filing jointly"
  - printed: "18"
    value: "-33237.00"
    work: "266,763 - 300,000 = -33,237; zero or less, so line 15 goes to line 21"
  - printed: "20"
    value: "blank"
    work: "Skipped because line 18 is zero or less"
  - printed: "21"
    value: "25000.00"
    work: "Line 18 is zero or less, so enter line 15"
  - printed: "23"
    value: "blank"
    work: "No qualified car loan interest, so Part IV is not filled out"
  - printed: "24"
    value: "blank"
    work: "Part IV is not filled out"
  - printed: "25"
    value: "blank"
    work: "Part IV is not filled out"
  - printed: "26"
    value: "blank"
    work: "Part IV is not filled out"
  - printed: "27"
    value: "blank"
    work: "Part IV is not filled out"
  - printed: "29"
    value: "blank"
    work: "Part IV is not filled out"
  - printed: "30"
    value: "blank"
    work: "Part IV is not filled out"
  - printed: "31"
    value: "266763.00"
    work: "Line 3"
  - printed: "32"
    value: "150000.00"
    work: "Married filing jointly"
  - printed: "33"
    value: "116763.00"
    work: "266,763 - 150,000"
  - printed: "34"
    value: "7005.78"
    work: "116,763 x 0.06"
  - printed: "35"
    value: "0.00"
    work: "6,000 - 7,005.78 is less than zero, so enter -0-"
  - printed: "36a"
    value: "blank"
    work: "Taxpayer was not born before January 2, 1961"
  - printed: "36b"
    value: "0.00"
    work: "Spouse has a valid SSN and was born before January 2, 1961, so enter line 35 (0)"
  - printed: "37"
    value: "0.00"
    work: "0 + 0"
  - printed: "38"
    value: "50000.00"
    work: "25,000 + 25,000 + 0 + 0"
```
