# Class M hand-work — s1a

`Schedule 1-A (Form 1040) — Additional Deductions` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 8 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104, 105, 106, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104, 106, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.s1a.1 — prompt sha256 a110900d2d4fd8d3ffee8bd12a3a65ac009bde86a81ad9cb61dfb5ebc226a4b8; branches: s1a.tips:true, s1a.tip_multi:false, s1a.part2:true, s1a.line4a_calc#1, s1a.line4a#1, s1a.line4b#1, s1a.line4c_one:left, s1a.line4c_calc#1, s1a.line4c#1, s1a.line5#1, s1a.line6#1, s1a.line7_calc:left, s1a.line7#1, s1a.line8#1, s1a.line9_calc#0, s1a.line9#1, s1a.line10#1, s1a.line10_over:false, s1a.line10_pos:floor, s1a.line12#1, s1a.line13_figured:floor, s1a.line13_amount#0, s1a.line13_ssn#1, s1a.line13_claim#0, s1a.line13#1, s1a.overtime:false, s1a.part3:false, s1a.line14a#0, s1a.line14b#0, s1a.line14c#0, s1a.ot_max#0, s1a.line15_calc:left, s1a.line15#0, s1a.line16#0, s1a.line17_calc#0, s1a.line17#0, s1a.line18#0, s1a.line18_over:false, s1a.line18_pos:floor, s1a.line20#0, s1a.line21_figured:floor, s1a.line21_amount#0, s1a.line21_ssn#1, s1a.line21_claim#0, s1a.line21#0, s1a.carloan:false, s1a.line23#0, s1a.part4:false, s1a.line24_calc:left, s1a.line24#0, s1a.line25#0, s1a.line26_calc#0, s1a.line26#0, s1a.line27#0, s1a.line27_over:false, s1a.line27_pos:floor, s1a.line29#0, s1a.line30_figured:floor, s1a.line30_amount#0, s1a.line30#0, s1a.part5:false, s1a.line31#0, s1a.line32_calc#0, s1a.line32#0, s1a.line33#0, s1a.line33_over:false, s1a.line33_pos:floor, s1a.line34#0, s1a.line35_figured:positive, s1a.line35_calc#0, s1a.line35#0, s1a.died_before_65:false, s1a.senior_decedent:false, s1a.line36a_senior#1, s1a.line36a_claim#0, s1a.line36a#0

### classm.s1a.1 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $23,169.00

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

Value: $23,169.00

### classm.s1a.1 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $23,169.00

### classm.s1a.1 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $150,000.00

### classm.s1a.1 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $-126,831.00

### classm.s1a.1 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $0.00

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

Value: $0.00

### classm.s1a.1 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $0.00

### classm.s1a.1 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $0.00

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

Value: $0.00

### case classm.s1a.2 — prompt sha256 5496cc335147d444af5a512f321189f72b906bd414b8a0767a50d2432e8a2d2f; branches: s1a.tips:false, s1a.part2:false, s1a.line4a#0, s1a.line4b#0, s1a.line4c_one:left, s1a.line4c#0, s1a.line5#0, s1a.line6#0, s1a.line7_calc:left, s1a.line7#0, s1a.line8#0, s1a.line9_calc#3, s1a.line9#0, s1a.line10#0, s1a.line10_over:false, s1a.line10_pos:floor, s1a.line12#0, s1a.line13_figured:floor, s1a.line13_amount#0, s1a.line13_ssn#1, s1a.line13_claim#3, s1a.line13#0, s1a.overtime:false, s1a.part3:false, s1a.line14a#0, s1a.line14b#0, s1a.line14c#0, s1a.ot_max#3, s1a.line15_calc:left, s1a.line15#0, s1a.line16#0, s1a.line17_calc#3, s1a.line17#0, s1a.line18#0, s1a.line18_over:false, s1a.line18_pos:floor, s1a.line20#0, s1a.line21_figured:floor, s1a.line21_amount#0, s1a.line21_ssn#1, s1a.line21_claim#3, s1a.line21#0, s1a.carloan:true, s1a.line23#1, s1a.part4:true, s1a.line24_calc:right, s1a.line24#1, s1a.line25#1, s1a.line26_calc#3, s1a.line26#1, s1a.line27#1, s1a.line27_over:true, s1a.line27_pos:positive, s1a.line29#1, s1a.line30_figured:floor, s1a.line30_amount#1, s1a.line30#1, s1a.part5:true, s1a.line31#1, s1a.line32_calc#3, s1a.line32#1, s1a.line33#1, s1a.line33_over:true, s1a.line33_pos:positive, s1a.line34#1, s1a.line35_figured:floor, s1a.line35_calc#1, s1a.line35#1, s1a.died_before_65:false, s1a.senior_decedent:false, s1a.line36a_senior#1, s1a.line36a_claim#3, s1a.line36a#1

### classm.s1a.2 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $442,528.00

### classm.s1a.2 — 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 3 — Add lines 1 and 2e
Status: **AGREE**

Value: $442,528.00

### classm.s1a.2 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

Value: $14,334.00

### classm.s1a.2 — 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **AGREE**

Value: $10,000.00

### classm.s1a.2 — 25 — Enter the amount from line 3
Status: **AGREE**

Value: $442,528.00

### classm.s1a.2 — 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **AGREE**

Value: $100,000.00

### classm.s1a.2 — 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on
Status: **AGREE**

Value: $342,528.00

### classm.s1a.2 — 29 — Multiply line 28 by $200
Status: **AGREE**

Value: $68,600.00

### classm.s1a.2 — 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 31 — Enter the amount from line 3
Status: **AGREE**

Value: $442,528.00

### classm.s1a.2 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $75,000.00

### classm.s1a.2 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $367,528.00

### classm.s1a.2 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $22,051.68

### classm.s1a.2 — 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 36a — If you have a valid social security number (see instructions) and were born befo
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 36b — If you are married filing jointly, your spouse has a valid social security numbe
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

Value: $0.00

### classm.s1a.2 — 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, 
Status: **AGREE**

Value: $0.00

### case classm.s1a.3 — prompt sha256 3a72f185d0afe84cbcfde0ff4a1544cc46eabe5a76c537c7987dae19e5ea555f; branches: s1a.tips:true, s1a.tip_multi:true, s1a.part2:true, s1a.line4a_calc#0, s1a.line4a#1, s1a.line4b#1, s1a.line4c_one:left, s1a.line4c_calc#0, s1a.line4c#1, s1a.line5#1, s1a.line6#1, s1a.line7_calc:left, s1a.line7#1, s1a.line8#1, s1a.line9_calc#1, s1a.line9#1, s1a.line10#1, s1a.line10_over:false, s1a.line10_pos:floor, s1a.line12#1, s1a.line13_figured:positive, s1a.line13_amount#0, s1a.line13_ssn#1, s1a.line13_claim#1, s1a.line13#1, s1a.overtime:true, s1a.part3:true, s1a.line14a#1, s1a.line14b#1, s1a.line14c#1, s1a.ot_max#1, s1a.line15_calc:right, s1a.line15#1, s1a.line16#1, s1a.line17_calc#1, s1a.line17#1, s1a.line18#1, s1a.line18_over:false, s1a.line18_pos:floor, s1a.line20#1, s1a.line21_figured:positive, s1a.line21_amount#0, s1a.line21_ssn#1, s1a.line21_claim#1, s1a.line21#1, s1a.carloan:false, s1a.line23#0, s1a.part4:false, s1a.line24_calc:left, s1a.line24#0, s1a.line25#0, s1a.line26_calc#1, s1a.line26#0, s1a.line27#0, s1a.line27_over:false, s1a.line27_pos:floor, s1a.line29#0, s1a.line30_figured:floor, s1a.line30_amount#0, s1a.line30#0, s1a.part5:false, s1a.line31#0, s1a.line32_calc#1, s1a.line32#0, s1a.line33#0, s1a.line33_over:false, s1a.line33_pos:floor, s1a.line34#0, s1a.line35_figured:positive, s1a.line35_calc#0, s1a.line35#0, s1a.died_before_65:false, s1a.senior_decedent:false, s1a.line36a_senior#1, s1a.line36a_claim#1, s1a.line36a#0

### classm.s1a.3 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $72,064.00

### classm.s1a.3 — 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 3 — Add lines 1 and 2e
Status: **AGREE**

Value: $72,064.00

### classm.s1a.3 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $16,337.00

### classm.s1a.3 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $16,337.00

### classm.s1a.3 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $16,337.00

### classm.s1a.3 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $72,064.00

### classm.s1a.3 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $300,000.00

### classm.s1a.3 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $-227,936.00

### classm.s1a.3 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $16,337.00

### classm.s1a.3 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $31,045.00

### classm.s1a.3 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $31,045.00

### classm.s1a.3 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $25,000.00

### classm.s1a.3 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $72,064.00

### classm.s1a.3 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $300,000.00

### classm.s1a.3 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $-227,936.00

### classm.s1a.3 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $25,000.00

### classm.s1a.3 — 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 25 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 29 — Multiply line 28 by $200
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 31 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 36a — If you have a valid social security number (see instructions) and were born befo
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 36b — If you are married filing jointly, your spouse has a valid social security numbe
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

Value: $0.00

### classm.s1a.3 — 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, 
Status: **AGREE**

Value: $41,337.00

### case classm.s1a.4 — prompt sha256 a12d75cd0270cde4183f89af159a826173e6178beba03066e3cb83812882a151; branches: s1a.tips:true, s1a.tip_multi:true, s1a.part2:true, s1a.line4a_calc#0, s1a.line4a#1, s1a.line4b#1, s1a.line4c_one:left, s1a.line4c_calc#0, s1a.line4c#1, s1a.line5#1, s1a.line6#1, s1a.line7_calc:right, s1a.line7#1, s1a.line8#1, s1a.line9_calc#4, s1a.line9#1, s1a.line10#1, s1a.line10_over:true, s1a.line10_pos:positive, s1a.line12#1, s1a.line13_figured:floor, s1a.line13_amount#1, s1a.line13_ssn#1, s1a.line13_claim#4, s1a.line13#1, s1a.overtime:false, s1a.part3:false, s1a.line14a#0, s1a.line14b#0, s1a.line14c#0, s1a.ot_max#4, s1a.line15_calc:left, s1a.line15#0, s1a.line16#0, s1a.line17_calc#4, s1a.line17#0, s1a.line18#0, s1a.line18_over:false, s1a.line18_pos:floor, s1a.line20#0, s1a.line21_figured:floor, s1a.line21_amount#0, s1a.line21_ssn#1, s1a.line21_claim#4, s1a.line21#0, s1a.carloan:false, s1a.line23#0, s1a.part4:false, s1a.line24_calc:left, s1a.line24#0, s1a.line25#0, s1a.line26_calc#4, s1a.line26#0, s1a.line27#0, s1a.line27_over:false, s1a.line27_pos:floor, s1a.line29#0, s1a.line30_figured:floor, s1a.line30_amount#0, s1a.line30#0, s1a.part5:false, s1a.line31#0, s1a.line32_calc#4, s1a.line32#0, s1a.line33#0, s1a.line33_over:false, s1a.line33_pos:floor, s1a.line34#0, s1a.line35_figured:positive, s1a.line35_calc#0, s1a.line35#0, s1a.died_before_65:false, s1a.senior_decedent:false, s1a.line36a_senior#1, s1a.line36a_claim#4, s1a.line36a#0

### classm.s1a.4 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $575,169.80

### classm.s1a.4 — 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 3 — Add lines 1 and 2e
Status: **AGREE**

Value: $575,169.80

### classm.s1a.4 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $26,736.00

### classm.s1a.4 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $26,736.00

### classm.s1a.4 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $25,000.00

### classm.s1a.4 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $575,169.80

### classm.s1a.4 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $150,000.00

### classm.s1a.4 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $425,169.80

### classm.s1a.4 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $42,500.00

### classm.s1a.4 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 25 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 29 — Multiply line 28 by $200
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 31 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 36a — If you have a valid social security number (see instructions) and were born befo
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 36b — If you are married filing jointly, your spouse has a valid social security numbe
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

Value: $0.00

### classm.s1a.4 — 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, 
Status: **AGREE**

Value: $0.00

### case classm.s1a.5 — prompt sha256 d87d108c30234fe0f442f0198b0c514e9cd2038ac8996d177b6a113a8cb7786c; branches: s1a.tips:false, s1a.part2:false, s1a.line4a#0, s1a.line4b#0, s1a.line4c_one:left, s1a.line4c#0, s1a.line5#0, s1a.line6#0, s1a.line7_calc:left, s1a.line7#0, s1a.line8#0, s1a.line9_calc#2, s1a.line9#0, s1a.line10#0, s1a.line10_over:false, s1a.line10_pos:floor, s1a.line12#0, s1a.line13_figured:floor, s1a.line13_amount#0, s1a.line13_ssn#0, s1a.line13_claim#2, s1a.line13#0, s1a.overtime:false, s1a.part3:false, s1a.line14a#0, s1a.line14b#0, s1a.line14c#0, s1a.ot_max#2, s1a.line15_calc:left, s1a.line15#0, s1a.line16#0, s1a.line17_calc#2, s1a.line17#0, s1a.line18#0, s1a.line18_over:false, s1a.line18_pos:floor, s1a.line20#0, s1a.line21_figured:floor, s1a.line21_amount#0, s1a.line21_ssn#0, s1a.line21_claim#2, s1a.line21#0, s1a.carloan:false, s1a.line23#0, s1a.part4:false, s1a.line24_calc:left, s1a.line24#0, s1a.line25#0, s1a.line26_calc#2, s1a.line26#0, s1a.line27#0, s1a.line27_over:false, s1a.line27_pos:floor, s1a.line29#0, s1a.line30_figured:floor, s1a.line30_amount#0, s1a.line30#0, s1a.part5:false, s1a.line31#0, s1a.line32_calc#2, s1a.line32#0, s1a.line33#0, s1a.line33_over:false, s1a.line33_pos:floor, s1a.line34#0, s1a.line35_figured:positive, s1a.line35_calc#0, s1a.line35#0, s1a.died_before_65:false, s1a.senior_decedent:false, s1a.line36a_senior#0, s1a.line36a_claim#2, s1a.line36a#0

### classm.s1a.5 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $448,712.55

### classm.s1a.5 — 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 3 — Add lines 1 and 2e
Status: **AGREE**

Value: $448,712.55

### classm.s1a.5 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 25 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 29 — Multiply line 28 by $200
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 31 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 36a — If you have a valid social security number (see instructions) and were born befo
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 36b — If you are married filing jointly, your spouse has a valid social security numbe
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

Value: $0.00

### classm.s1a.5 — 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, 
Status: **AGREE**

Value: $0.00

### case classm.s1a.6 — prompt sha256 bcc51d9ac698f85107e3ab174661e0f15557a594d77b292ec748105420eceafa; branches: s1a.tips:false, s1a.part2:false, s1a.line4a#0, s1a.line4b#0, s1a.line4c_one:left, s1a.line4c#0, s1a.line5#0, s1a.line6#0, s1a.line7_calc:left, s1a.line7#0, s1a.line8#0, s1a.line9_calc#0, s1a.line9#0, s1a.line10#0, s1a.line10_over:false, s1a.line10_pos:floor, s1a.line12#0, s1a.line13_figured:floor, s1a.line13_amount#0, s1a.line13_ssn#1, s1a.line13_claim#0, s1a.line13#0, s1a.overtime:true, s1a.part3:true, s1a.line14a#1, s1a.line14b#1, s1a.line14c#1, s1a.ot_max#0, s1a.line15_calc:right, s1a.line15#1, s1a.line16#1, s1a.line17_calc#0, s1a.line17#1, s1a.line18#1, s1a.line18_over:true, s1a.line18_pos:positive, s1a.line20#1, s1a.line21_figured:floor, s1a.line21_amount#1, s1a.line21_ssn#1, s1a.line21_claim#0, s1a.line21#1, s1a.carloan:false, s1a.line23#0, s1a.part4:false, s1a.line24_calc:left, s1a.line24#0, s1a.line25#0, s1a.line26_calc#0, s1a.line26#0, s1a.line27#0, s1a.line27_over:false, s1a.line27_pos:floor, s1a.line29#0, s1a.line30_figured:floor, s1a.line30_amount#0, s1a.line30#0, s1a.part5:true, s1a.line31#1, s1a.line32_calc#0, s1a.line32#1, s1a.line33#1, s1a.line33_over:true, s1a.line33_pos:positive, s1a.line34#1, s1a.line35_figured:floor, s1a.line35_calc#1, s1a.line35#1, s1a.died_before_65:false, s1a.senior_decedent:false, s1a.line36a_senior#1, s1a.line36a_claim#0, s1a.line36a#1

### classm.s1a.6 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $322,001.25

### classm.s1a.6 — 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 3 — Add lines 1 and 2e
Status: **AGREE**

Value: $322,001.25

### classm.s1a.6 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $14,733.00

### classm.s1a.6 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $14,733.00

### classm.s1a.6 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $12,500.00

### classm.s1a.6 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $322,001.25

### classm.s1a.6 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $150,000.00

### classm.s1a.6 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $172,001.25

### classm.s1a.6 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $17,200.00

### classm.s1a.6 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 25 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 29 — Multiply line 28 by $200
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 31 — Enter the amount from line 3
Status: **AGREE**

Value: $322,001.25

### classm.s1a.6 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $75,000.00

### classm.s1a.6 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $247,001.25

### classm.s1a.6 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $14,820.08

### classm.s1a.6 — 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 36a — If you have a valid social security number (see instructions) and were born befo
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 36b — If you are married filing jointly, your spouse has a valid social security numbe
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

Value: $0.00

### classm.s1a.6 — 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, 
Status: **AGREE**

Value: $0.00

### case classm.s1a.7 — prompt sha256 64daff29277ee275fb24b1334cde0299bde838db2cf03c2335697fa445e6e37a; branches: s1a.tips:false, s1a.part2:false, s1a.line4a#0, s1a.line4b#0, s1a.line4c_one:left, s1a.line4c#0, s1a.line5#0, s1a.line6#0, s1a.line7_calc:left, s1a.line7#0, s1a.line8#0, s1a.line9_calc#0, s1a.line9#0, s1a.line10#0, s1a.line10_over:false, s1a.line10_pos:floor, s1a.line12#0, s1a.line13_figured:floor, s1a.line13_amount#0, s1a.line13_ssn#1, s1a.line13_claim#0, s1a.line13#0, s1a.overtime:false, s1a.part3:false, s1a.line14a#0, s1a.line14b#0, s1a.line14c#0, s1a.ot_max#0, s1a.line15_calc:left, s1a.line15#0, s1a.line16#0, s1a.line17_calc#0, s1a.line17#0, s1a.line18#0, s1a.line18_over:false, s1a.line18_pos:floor, s1a.line20#0, s1a.line21_figured:floor, s1a.line21_amount#0, s1a.line21_ssn#1, s1a.line21_claim#0, s1a.line21#0, s1a.carloan:false, s1a.line23#0, s1a.part4:false, s1a.line24_calc:left, s1a.line24#0, s1a.line25#0, s1a.line26_calc#0, s1a.line26#0, s1a.line27#0, s1a.line27_over:false, s1a.line27_pos:floor, s1a.line29#0, s1a.line30_figured:floor, s1a.line30_amount#0, s1a.line30#0, s1a.part5:false, s1a.line31#0, s1a.line32_calc#0, s1a.line32#0, s1a.line33#0, s1a.line33_over:false, s1a.line33_pos:floor, s1a.line34#0, s1a.line35_figured:positive, s1a.line35_calc#0, s1a.line35#0, s1a.died_before_65:true, s1a.senior_decedent:true, s1a.line36a_claim#0, s1a.line36a#0

### classm.s1a.7 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $71,974.00

### classm.s1a.7 — 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 3 — Add lines 1 and 2e
Status: **AGREE**

Value: $71,974.00

### classm.s1a.7 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 25 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 29 — Multiply line 28 by $200
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 31 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 36a — If you have a valid social security number (see instructions) and were born befo
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 36b — If you are married filing jointly, your spouse has a valid social security numbe
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

Value: $0.00

### classm.s1a.7 — 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, 
Status: **AGREE**

Value: $0.00

### case classm.s1a.8 — prompt sha256 2db7b46834d8a53064a08be31998129987c6a13836a4c13c400b173abccd1ab7; branches: s1a.tips:false, s1a.part2:false, s1a.line4a#0, s1a.line4b#0, s1a.line4c_one:left, s1a.line4c#0, s1a.line5#0, s1a.line6#0, s1a.line7_calc:left, s1a.line7#0, s1a.line8#0, s1a.line9_calc#1, s1a.line9#0, s1a.line10#0, s1a.line10_over:false, s1a.line10_pos:floor, s1a.line12#0, s1a.line13_figured:floor, s1a.line13_amount#0, s1a.line13_ssn#1, s1a.line13_claim#1, s1a.line13#0, s1a.overtime:true, s1a.part3:true, s1a.line14a#1, s1a.line14b#1, s1a.line14c#1, s1a.ot_max#1, s1a.line15_calc:left, s1a.line15#1, s1a.line16#1, s1a.line17_calc#1, s1a.line17#1, s1a.line18#1, s1a.line18_over:false, s1a.line18_pos:floor, s1a.line20#1, s1a.line21_figured:floor, s1a.line21_amount#0, s1a.line21_ssn#1, s1a.line21_claim#1, s1a.line21#1, s1a.carloan:true, s1a.line23#1, s1a.part4:true, s1a.line24_calc:left, s1a.line24#1, s1a.line25#1, s1a.line26_calc#1, s1a.line26#1, s1a.line27#1, s1a.line27_over:false, s1a.line27_pos:floor, s1a.line29#1, s1a.line30_figured:positive, s1a.line30_amount#0, s1a.line30#1, s1a.part5:false, s1a.line31#0, s1a.line32_calc#1, s1a.line32#0, s1a.line33#0, s1a.line33_over:false, s1a.line33_pos:floor, s1a.line34#0, s1a.line35_figured:positive, s1a.line35_calc#0, s1a.line35#0, s1a.died_before_65:false, s1a.senior_decedent:false, s1a.line36a_senior#1, s1a.line36a_claim#1, s1a.line36a#0

### classm.s1a.8 — 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

Value: $110,760.00

### classm.s1a.8 — 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 3 — Add lines 1 and 2e
Status: **AGREE**

Value: $110,760.00

### classm.s1a.8 — 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Fo
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 4c — If you only received qualified tips as an employee with respect to employment wi
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 5 — Qualified tips received in the course of a trade or business
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 6 — Add lines 4c and 5
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 8 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on li
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 12 — Multiply line 11 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qua
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-M
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 14c — Add lines 14a and 14b
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filin
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 16 — Enter the amount from line 3
Status: **AGREE**

Value: $110,760.00

### classm.s1a.8 — 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **AGREE**

Value: $300,000.00

### classm.s1a.8 — 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on
Status: **AGREE**

Value: $-189,240.00

### classm.s1a.8 — 20 — Multiply line 19 by $100
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zer
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

Value: $4,060.00

### classm.s1a.8 — 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **AGREE**

Value: $4,060.00

### classm.s1a.8 — 25 — Enter the amount from line 3
Status: **AGREE**

Value: $110,760.00

### classm.s1a.8 — 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **AGREE**

Value: $200,000.00

### classm.s1a.8 — 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on
Status: **AGREE**

Value: $-89,240.00

### classm.s1a.8 — 29 — Multiply line 28 by $200
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 
Status: **AGREE**

Value: $4,060.00

### classm.s1a.8 — 31 — Enter the amount from line 3
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 34 — Multiply line 33 by 6% (0.06)
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 36a — If you have a valid social security number (see instructions) and were born befo
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 36b — If you are married filing jointly, your spouse has a valid social security numbe
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

Value: $0.00

### classm.s1a.8 — 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, 
Status: **AGREE**

Value: $4,060.00

## Raw responses

### classm.s1a.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "23169.00"
    work: "Form 1040, line 11b = 23,169.00"
  - printed: "2a"
    value: ""
    work: "No excluded Puerto Rico income given; instructions say skip 2a-2e"
  - printed: "2b"
    value: ""
    work: "No Form 2555 filed; left blank"
  - printed: "2c"
    value: ""
    work: "No Form 2555 filed; left blank"
  - printed: "2d"
    value: ""
    work: "No Form 4563 filed; left blank"
  - printed: "2e"
    value: ""
    work: "Lines 2a-2d not required; line 11b goes directly to line 3"
  - printed: "3"
    value: "23169.00"
    work: "23,169.00 + 0 = 23,169.00 (MAGI)"
  - printed: "4a"
    value: "0.00"
    work: "Filer said yes to qualified employee tips, but no W-2 box 7 amount was supplied; 0 entered"
  - printed: "4b"
    value: "0.00"
    work: "No Form 4137 filed; enter -0-"
  - printed: "4c"
    value: "0.00"
    work: "One employer assumed; larger of 4a (0) or 4b (0) = 0"
  - printed: "5"
    value: "0.00"
    work: "No trade or business tips supplied"
  - printed: "6"
    value: "0.00"
    work: "0 + 0 = 0"
  - printed: "7"
    value: "0.00"
    work: "smaller of 0 or 25,000 = 0"
  - printed: "8"
    value: "23169.00"
    work: "From line 3"
  - printed: "9"
    value: "150000.00"
    work: "Filing status is Single, so 150,000"
  - printed: "10"
    value: "-126831.00"
    work: "23,169 - 150,000 = -126,831; zero or less, so line 7 goes to line 13"
  - printed: "12"
    value: ""
    work: "Skipped because line 10 is zero or less"
  - printed: "13"
    value: "0.00"
    work: "Amount from line 7 = 0"
  - printed: "14a"
    value: ""
    work: "No qualified overtime received; Part III not filled out"
  - printed: "14b"
    value: ""
    work: "Part III not filled out"
  - printed: "14c"
    value: ""
    work: "Part III not filled out"
  - printed: "15"
    value: ""
    work: "Part III not filled out"
  - printed: "16"
    value: ""
    work: "Part III not filled out"
  - printed: "17"
    value: ""
    work: "Part III not filled out"
  - printed: "18"
    value: ""
    work: "Part III not filled out"
  - printed: "20"
    value: ""
    work: "Part III not filled out"
  - printed: "21"
    value: ""
    work: "Part III not filled out; treated as 0"
  - printed: "23"
    value: ""
    work: "No qualified car loan interest; Part IV not filled out"
  - printed: "24"
    value: ""
    work: "Part IV not filled out"
  - printed: "25"
    value: ""
    work: "Part IV not filled out"
  - printed: "26"
    value: ""
    work: "Part IV not filled out"
  - printed: "27"
    value: ""
    work: "Part IV not filled out"
  - printed: "29"
    value: ""
    work: "Part IV not filled out"
  - printed: "30"
    value: ""
    work: "Part IV not filled out; treated as 0"
  - printed: "31"
    value: ""
    work: "Not born before 1/2/1961; Part V not filled out"
  - printed: "32"
    value: ""
    work: "Part V not filled out"
  - printed: "33"
    value: ""
    work: "Part V not filled out"
  - printed: "34"
    value: ""
    work: "Part V not filled out"
  - printed: "35"
    value: ""
    work: "Part V not filled out"
  - printed: "36a"
    value: ""
    work: "Part V not filled out; filer not born before 1/2/1961"
  - printed: "36b"
    value: ""
    work: "Part V not filled out; not married filing jointly"
  - printed: "37"
    value: ""
    work: "Part V not filled out; treated as 0"
  - printed: "38"
    value: "0.00"
    work: "13 (0) + 21 (0) + 30 (0) + 37 (0) = 0"
```
```

### classm.s1a.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "442528.00"
    work: "Form 1040 line 11b = 442,528.00"
  - printed: "2a"
    value: "0.00"
    work: "No excluded Puerto Rico income given"
  - printed: "2b"
    value: "0.00"
    work: "No Form 2555 given"
  - printed: "2c"
    value: "0.00"
    work: "No Form 2555 given"
  - printed: "2d"
    value: "0.00"
    work: "No Form 4563 given"
  - printed: "2e"
    value: "0.00"
    work: "0 + 0 + 0 + 0 = 0"
  - printed: "3"
    value: "442528.00"
    work: "442,528.00 + 0 = 442,528.00"
  - printed: "4a"
    value: ""
    work: "No qualified tips; fill out Part II only if qualified tips were received"
  - printed: "4b"
    value: ""
    work: "Part II not filled out"
  - printed: "4c"
    value: ""
    work: "Part II not filled out"
  - printed: "5"
    value: ""
    work: "Part II not filled out"
  - printed: "6"
    value: ""
    work: "Part II not filled out"
  - printed: "7"
    value: ""
    work: "Part II not filled out"
  - printed: "8"
    value: ""
    work: "Part II not filled out"
  - printed: "9"
    value: ""
    work: "Part II not filled out"
  - printed: "10"
    value: ""
    work: "Part II not filled out"
  - printed: "12"
    value: ""
    work: "Part II not filled out"
  - printed: "13"
    value: ""
    work: "Part II not filled out; treated as 0 on line 38"
  - printed: "14a"
    value: ""
    work: "No qualified overtime; fill out Part III only if qualified overtime was received"
  - printed: "14b"
    value: ""
    work: "Part III not filled out"
  - printed: "14c"
    value: ""
    work: "Part III not filled out"
  - printed: "15"
    value: ""
    work: "Part III not filled out"
  - printed: "16"
    value: ""
    work: "Part III not filled out"
  - printed: "17"
    value: ""
    work: "Part III not filled out"
  - printed: "18"
    value: ""
    work: "Part III not filled out"
  - printed: "20"
    value: ""
    work: "Part III not filled out"
  - printed: "21"
    value: ""
    work: "Part III not filled out; treated as 0 on line 38"
  - printed: "23"
    value: "14334.00"
    work: "Line 22a column (iii) = 14,334.00; no line 22b"
  - printed: "24"
    value: "10000.00"
    work: "Smaller of 14,334.00 or 10,000 = 10,000.00"
  - printed: "25"
    value: "442528.00"
    work: "Line 3 = 442,528.00"
  - printed: "26"
    value: "100000.00"
    work: "Head of household (not MFJ) = 100,000"
  - printed: "27"
    value: "342528.00"
    work: "442,528.00 - 100,000 = 342,528.00"
  - printed: "29"
    value: "68600.00"
    work: "Line 28 = 342,528 / 1,000 = 342.528, rounded up to 343; 343 x 200 = 68,600.00"
  - printed: "30"
    value: "0.00"
    work: "10,000.00 - 68,600.00 < 0, so enter -0-"
  - printed: "31"
    value: "442528.00"
    work: "Line 3 = 442,528.00"
  - printed: "32"
    value: "75000.00"
    work: "Head of household (not MFJ) = 75,000"
  - printed: "33"
    value: "367528.00"
    work: "442,528.00 - 75,000 = 367,528.00"
  - printed: "34"
    value: "22051.68"
    work: "367,528.00 x 0.06 = 22,051.68"
  - printed: "35"
    value: "0.00"
    work: "6,000 - 22,051.68 < 0, so enter -0-"
  - printed: "36a"
    value: "0.00"
    work: "Valid SSN and born before 1/2/1961, so enter line 35 = 0.00"
  - printed: "36b"
    value: ""
    work: "Not married filing jointly"
  - printed: "37"
    value: "0.00"
    work: "0.00 + 0 = 0.00"
  - printed: "38"
    value: "0.00"
    work: "Line 13 (0) + line 21 (0) + line 30 (0.00) + line 37 (0.00) = 0.00"
```
```

### classm.s1a.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "72064.00"
    work: "Form 1040 line 11b"
  - printed: "2a"
    value: ""
    work: "No excluded Puerto Rico income; instructions say enter line 11b directly on line 3"
  - printed: "2b"
    value: ""
    work: "No Form 2555 filed"
  - printed: "2c"
    value: ""
    work: "No Form 2555 filed"
  - printed: "2d"
    value: ""
    work: "No Form 4563 filed"
  - printed: "2e"
    value: ""
    work: "Lines 2a-2d not used"
  - printed: "3"
    value: "72064.00"
    work: "72064.00 + 0 = 72064.00 (MAGI)"
  - printed: "4a"
    value: "0.00"
    work: "More than one employer, so enter -0-"
  - printed: "4b"
    value: "0.00"
    work: "More than one employer, so enter -0-"
  - printed: "4c"
    value: "16337.00"
    work: "Multiple-employer worksheet col (d): 13784 + 2553 + 0 = 16337"
  - printed: "5"
    value: "0.00"
    work: "No qualified tips from a trade or business"
  - printed: "6"
    value: "16337.00"
    work: "16337 + 0"
  - printed: "7"
    value: "16337.00"
    work: "smaller of 16337 or 25000"
  - printed: "8"
    value: "72064.00"
    work: "line 3"
  - printed: "9"
    value: "300000.00"
    work: "MFJ threshold"
  - printed: "10"
    value: "-227936.00"
    work: "72064 - 300000 = -227936; zero or less, so line 7 goes to line 13"
  - printed: "12"
    value: ""
    work: "Skipped because line 10 is zero or less"
  - printed: "13"
    value: "16337.00"
    work: "line 7 amount (no reduction)"
  - printed: "14a"
    value: "31045.00"
    work: "Multiple-employer worksheet: 0 + 31045 = 31045"
  - printed: "14b"
    value: "0.00"
    work: "No 1099 overtime"
  - printed: "14c"
    value: "31045.00"
    work: "31045 + 0"
  - printed: "15"
    value: "25000.00"
    work: "smaller of 31045 or 25000 (MFJ)"
  - printed: "16"
    value: "72064.00"
    work: "line 3"
  - printed: "17"
    value: "300000.00"
    work: "MFJ threshold"
  - printed: "18"
    value: "-227936.00"
    work: "72064 - 300000 = -227936; zero or less, so line 15 goes to line 21"
  - printed: "20"
    value: ""
    work: "Skipped because line 18 is zero or less"
  - printed: "21"
    value: "25000.00"
    work: "line 15 amount (no reduction)"
  - printed: "23"
    value: ""
    work: "No QPVLI, so Part IV is not filled out"
  - printed: "24"
    value: ""
    work: "Part IV not filled out"
  - printed: "25"
    value: ""
    work: "Part IV not filled out"
  - printed: "26"
    value: ""
    work: "Part IV not filled out"
  - printed: "27"
    value: ""
    work: "Part IV not filled out"
  - printed: "29"
    value: ""
    work: "Part IV not filled out"
  - printed: "30"
    value: ""
    work: "Part IV not filled out"
  - printed: "31"
    value: ""
    work: "Not born before 1/2/1961, so Part V is not filled out"
  - printed: "32"
    value: ""
    work: "Part V not filled out"
  - printed: "33"
    value: ""
    work: "Part V not filled out"
  - printed: "34"
    value: ""
    work: "Part V not filled out"
  - printed: "35"
    value: ""
    work: "Part V not filled out"
  - printed: "36a"
    value: ""
    work: "Taxpayer not born before 1/2/1961"
  - printed: "36b"
    value: ""
    work: "No spouse born before 1/2/1961 indicated"
  - printed: "37"
    value: ""
    work: "Part V not filled out"
  - printed: "38"
    value: "41337.00"
    work: "16337 + 25000 + 0 + 0 = 41337"
```
```

### classm.s1a.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "575169.80"
    work: "Form 1040 line 11b = 575,169.80"
  - printed: "2a"
    value: "0.00"
    work: "No excluded Puerto Rico income given"
  - printed: "2b"
    value: "0.00"
    work: "No Form 2555 given"
  - printed: "2c"
    value: "0.00"
    work: "No Form 2555 given"
  - printed: "2d"
    value: "0.00"
    work: "No Form 4563 given"
  - printed: "2e"
    value: "0.00"
    work: "0 + 0 + 0 + 0 = 0"
  - printed: "3"
    value: "575169.80"
    work: "575,169.80 + 0 = 575,169.80"
  - printed: "4a"
    value: "0.00"
    work: "More than one employer, so enter -0-"
  - printed: "4b"
    value: "0.00"
    work: "More than one employer, so enter -0-"
  - printed: "4c"
    value: "26736.00"
    work: "More Than One Employer Worksheet line 2: 23,637 + 3,099 = 26,736"
  - printed: "5"
    value: "0.00"
    work: "No trade or business tips"
  - printed: "6"
    value: "26736.00"
    work: "26,736 + 0 = 26,736"
  - printed: "7"
    value: "25000.00"
    work: "Smaller of 26,736 or 25,000 = 25,000"
  - printed: "8"
    value: "575169.80"
    work: "Line 3 = 575,169.80"
  - printed: "9"
    value: "150000.00"
    work: "Qualifying surviving spouse, not MFJ: 150,000"
  - printed: "10"
    value: "425169.80"
    work: "575,169.80 - 150,000 = 425,169.80"
  - printed: "12"
    value: "42500.00"
    work: "Line 11 = floor(425,169.80 / 1,000) = 425; 425 x 100 = 42,500"
  - printed: "13"
    value: "0.00"
    work: "25,000 - 42,500 is less than zero, so enter -0-"
  - printed: "14a"
    value: ""
    work: "No qualified overtime, so Part III is not filled out"
  - printed: "14b"
    value: ""
    work: "Part III is not filled out"
  - printed: "14c"
    value: ""
    work: "Part III is not filled out"
  - printed: "15"
    value: ""
    work: "Part III is not filled out"
  - printed: "16"
    value: ""
    work: "Part III is not filled out"
  - printed: "17"
    value: ""
    work: "Part III is not filled out"
  - printed: "18"
    value: ""
    work: "Part III is not filled out"
  - printed: "20"
    value: ""
    work: "Part III is not filled out"
  - printed: "21"
    value: ""
    work: "Part III is not filled out"
  - printed: "23"
    value: ""
    work: "No qualified passenger vehicle loan interest, so Part IV is not filled out"
  - printed: "24"
    value: ""
    work: "Part IV is not filled out"
  - printed: "25"
    value: ""
    work: "Part IV is not filled out"
  - printed: "26"
    value: ""
    work: "Part IV is not filled out"
  - printed: "27"
    value: ""
    work: "Part IV is not filled out"
  - printed: "29"
    value: ""
    work: "Part IV is not filled out"
  - printed: "30"
    value: ""
    work: "Part IV is not filled out"
  - printed: "31"
    value: ""
    work: "Not born before 1/2/1961, so Part V is not filled out"
  - printed: "32"
    value: ""
    work: "Part V is not filled out"
  - printed: "33"
    value: ""
    work: "Part V is not filled out"
  - printed: "34"
    value: ""
    work: "Part V is not filled out"
  - printed: "35"
    value: ""
    work: "Part V is not filled out"
  - printed: "36a"
    value: ""
    work: "Part V is not filled out; not born before 1/2/1961"
  - printed: "36b"
    value: ""
    work: "Part V is not filled out; not MFJ"
  - printed: "37"
    value: ""
    work: "Part V is not filled out"
  - printed: "38"
    value: "0.00"
    work: "Line 13 (0) + line 21 (blank) + line 30 (blank) + line 37 (blank) = 0"
```
```

### classm.s1a.5

```yaml
```yaml
lines:
  - printed: "1"
    value: "448712.55"
    work: "Form 1040 line 11b = 448,712.55"
  - printed: "2a"
    value: ""
    work: "No excluded Puerto Rico income; instructions put line 11b straight on line 3"
  - printed: "2b"
    value: ""
    work: "No Form 2555 filed; skipped"
  - printed: "2c"
    value: ""
    work: "No Form 2555 filed; skipped"
  - printed: "2d"
    value: ""
    work: "No Form 4563 filed; skipped"
  - printed: "2e"
    value: ""
    work: "Lines 2a-2d not used; skipped"
  - printed: "3"
    value: "448712.55"
    work: "Line 1 + 0 = 448,712.55 (MAGI)"
  - printed: "4a"
    value: ""
    work: "No qualified tips (and the filer is MFS); Part II not filled"
  - printed: "4b"
    value: ""
    work: "Part II not filled"
  - printed: "4c"
    value: ""
    work: "Part II not filled"
  - printed: "5"
    value: ""
    work: "Part II not filled"
  - printed: "6"
    value: ""
    work: "Part II not filled"
  - printed: "7"
    value: ""
    work: "Part II not filled"
  - printed: "8"
    value: ""
    work: "Part II not filled"
  - printed: "9"
    value: ""
    work: "Part II not filled"
  - printed: "10"
    value: ""
    work: "Part II not filled"
  - printed: "12"
    value: ""
    work: "Part II not filled"
  - printed: "13"
    value: ""
    work: "Part II not filled; no tips deduction"
  - printed: "14a"
    value: ""
    work: "No qualified overtime (and the filer is MFS); Part III not filled"
  - printed: "14b"
    value: ""
    work: "Part III not filled"
  - printed: "14c"
    value: ""
    work: "Part III not filled"
  - printed: "15"
    value: ""
    work: "Part III not filled"
  - printed: "16"
    value: ""
    work: "Part III not filled"
  - printed: "17"
    value: ""
    work: "Part III not filled"
  - printed: "18"
    value: ""
    work: "Part III not filled"
  - printed: "20"
    value: ""
    work: "Part III not filled"
  - printed: "21"
    value: ""
    work: "Part III not filled; no overtime deduction"
  - printed: "23"
    value: ""
    work: "No qualified car loan interest paid; Part IV not filled"
  - printed: "24"
    value: ""
    work: "Part IV not filled"
  - printed: "25"
    value: ""
    work: "Part IV not filled"
  - printed: "26"
    value: ""
    work: "Part IV not filled"
  - printed: "27"
    value: ""
    work: "Part IV not filled"
  - printed: "29"
    value: ""
    work: "Part IV not filled"
  - printed: "30"
    value: ""
    work: "Part IV not filled; no car loan interest deduction"
  - printed: "31"
    value: ""
    work: "Not born before 1/2/1961, no valid SSN, filer is MFS; Part V not filled"
  - printed: "32"
    value: ""
    work: "Part V not filled"
  - printed: "33"
    value: ""
    work: "Part V not filled"
  - printed: "34"
    value: ""
    work: "Part V not filled"
  - printed: "35"
    value: ""
    work: "Part V not filled"
  - printed: "36a"
    value: ""
    work: "Part V not filled"
  - printed: "36b"
    value: ""
    work: "Part V not filled; filer is not MFJ"
  - printed: "37"
    value: ""
    work: "Part V not filled; no senior deduction"
  - printed: "38"
    value: "0.00"
    work: "Lines 13 + 21 + 30 + 37 = 0 + 0 + 0 + 0 = 0.00"
```
```

### classm.s1a.6

```yaml
```yaml
lines:
  - printed: "1"
    value: "322001.25"
    work: "Form 1040 line 11b = 322,001.25"
  - printed: "2a"
    value: "0.00"
    work: "No excluded Puerto Rico income given"
  - printed: "2b"
    value: "0.00"
    work: "No Form 2555 given"
  - printed: "2c"
    value: "0.00"
    work: "No Form 2555 given"
  - printed: "2d"
    value: "0.00"
    work: "No Form 4563 given"
  - printed: "2e"
    value: "0.00"
    work: "0 + 0 + 0 + 0 = 0"
  - printed: "3"
    value: "322001.25"
    work: "322,001.25 + 0 = 322,001.25"
  - printed: "4a"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "4b"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "4c"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "5"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "6"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "7"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "8"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "9"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "10"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "12"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "13"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "14a"
    value: "14733.00"
    work: "One W-2 job, qualified overtime in box 1 = 14,733.00"
  - printed: "14b"
    value: "0.00"
    work: "No 1099 overtime"
  - printed: "14c"
    value: "14733.00"
    work: "14,733 + 0 = 14,733"
  - printed: "15"
    value: "12500.00"
    work: "Smaller of 14,733 or 12,500 (Single)"
  - printed: "16"
    value: "322001.25"
    work: "Line 3"
  - printed: "17"
    value: "150000.00"
    work: "Single: $150,000"
  - printed: "18"
    value: "172001.25"
    work: "322,001.25 - 150,000 = 172,001.25"
  - printed: "20"
    value: "17200.00"
    work: "Line 19 = 172,001.25 / 1,000 = 172.00125, rounded down to 172; 172 x 100 = 17,200"
  - printed: "21"
    value: "0.00"
    work: "12,500 - 17,200 is less than zero, so enter -0-"
  - printed: "23"
    value: ""
    work: "No qualified car loan interest; Part IV not filled out"
  - printed: "24"
    value: ""
    work: "No qualified car loan interest; Part IV not filled out"
  - printed: "25"
    value: ""
    work: "No qualified car loan interest; Part IV not filled out"
  - printed: "26"
    value: ""
    work: "No qualified car loan interest; Part IV not filled out"
  - printed: "27"
    value: ""
    work: "No qualified car loan interest; Part IV not filled out"
  - printed: "29"
    value: ""
    work: "No qualified car loan interest; Part IV not filled out"
  - printed: "30"
    value: ""
    work: "No qualified car loan interest; Part IV not filled out"
  - printed: "31"
    value: "322001.25"
    work: "Line 3"
  - printed: "32"
    value: "75000.00"
    work: "Single: $75,000"
  - printed: "33"
    value: "247001.25"
    work: "322,001.25 - 75,000 = 247,001.25"
  - printed: "34"
    value: "14820.08"
    work: "247,001.25 x 0.06 = 14,820.075, rounded to 14,820.08"
  - printed: "35"
    value: "0.00"
    work: "6,000 - 14,820.08 is less than zero, so enter -0-"
  - printed: "36a"
    value: "0.00"
    work: "Valid SSN and born before 1/2/1961, so enter line 35 = 0"
  - printed: "36b"
    value: "0.00"
    work: "Filing status is Single, not married filing jointly, so enter 0"
  - printed: "37"
    value: "0.00"
    work: "0 + 0 = 0"
  - printed: "38"
    value: "0.00"
    work: "Line 13 (blank, 0) + 0 + line 30 (blank, 0) + 0 = 0"
```
```

### classm.s1a.7

```yaml
```yaml
lines:
  - printed: "1"
    value: "71974.00"
    work: "Form 1040 line 11b = 71,974.00"
  - printed: "2a"
    value: ""
    work: "No excluded Puerto Rico income or Form 2555/4563; per instructions skip 2a-2e"
  - printed: "2b"
    value: ""
    work: "No Form 2555; skipped"
  - printed: "2c"
    value: ""
    work: "No Form 2555; skipped"
  - printed: "2d"
    value: ""
    work: "No Form 4563; skipped"
  - printed: "2e"
    value: ""
    work: "Skipped; enter line 11b directly on line 3"
  - printed: "3"
    value: "71974.00"
    work: "MAGI = line 1 = 71,974.00"
  - printed: "4a"
    value: ""
    work: "No qualified tips; Part II not filled out"
  - printed: "4b"
    value: ""
    work: "Part II not filled out"
  - printed: "4c"
    value: ""
    work: "Part II not filled out"
  - printed: "5"
    value: ""
    work: "Part II not filled out"
  - printed: "6"
    value: ""
    work: "Part II not filled out"
  - printed: "7"
    value: ""
    work: "Part II not filled out"
  - printed: "8"
    value: ""
    work: "Part II not filled out"
  - printed: "9"
    value: ""
    work: "Part II not filled out"
  - printed: "10"
    value: ""
    work: "Part II not filled out"
  - printed: "12"
    value: ""
    work: "Part II not filled out"
  - printed: "13"
    value: ""
    work: "Part II not filled out; no tips deduction"
  - printed: "14a"
    value: ""
    work: "No qualified overtime; Part III not filled out"
  - printed: "14b"
    value: ""
    work: "Part III not filled out"
  - printed: "14c"
    value: ""
    work: "Part III not filled out"
  - printed: "15"
    value: ""
    work: "Part III not filled out"
  - printed: "16"
    value: ""
    work: "Part III not filled out"
  - printed: "17"
    value: ""
    work: "Part III not filled out"
  - printed: "18"
    value: ""
    work: "Part III not filled out"
  - printed: "20"
    value: ""
    work: "Part III not filled out"
  - printed: "21"
    value: ""
    work: "Part III not filled out; no overtime deduction"
  - printed: "23"
    value: ""
    work: "No QPVLI; Part IV not filled out"
  - printed: "24"
    value: ""
    work: "Part IV not filled out"
  - printed: "25"
    value: ""
    work: "Part IV not filled out"
  - printed: "26"
    value: ""
    work: "Part IV not filled out"
  - printed: "27"
    value: ""
    work: "Part IV not filled out"
  - printed: "29"
    value: ""
    work: "Part IV not filled out"
  - printed: "30"
    value: ""
    work: "Part IV not filled out; no car loan interest deduction"
  - printed: "31"
    value: ""
    work: "Not born before Jan 2, 1961 (and died before reaching 65); Part V not filled out"
  - printed: "32"
    value: ""
    work: "Part V not filled out"
  - printed: "33"
    value: ""
    work: "Part V not filled out"
  - printed: "34"
    value: ""
    work: "Part V not filled out"
  - printed: "35"
    value: ""
    work: "Part V not filled out"
  - printed: "36a"
    value: ""
    work: "Taxpayer not born before Jan 2, 1961 / died before age 65; does not qualify"
  - printed: "36b"
    value: ""
    work: "Filing status Single; not applicable"
  - printed: "37"
    value: ""
    work: "Part V not filled out"
  - printed: "38"
    value: "0.00"
    work: "Lines 13 + 21 + 30 + 37 = 0 + 0 + 0 + 0 = 0.00"
```
```

### classm.s1a.8

```yaml
```yaml
lines:
  - printed: "1"
    value: "110760.00"
    work: "Form 1040 line 11b = 110,760.00"
  - printed: "2a"
    value: "0.00"
    work: "No excluded Puerto Rico income given"
  - printed: "2b"
    value: "0.00"
    work: "No Form 2555 given"
  - printed: "2c"
    value: "0.00"
    work: "No Form 2555 given"
  - printed: "2d"
    value: "0.00"
    work: "No Form 4563 given"
  - printed: "2e"
    value: "0.00"
    work: "0 + 0 + 0 + 0 = 0"
  - printed: "3"
    value: "110760.00"
    work: "110,760.00 + 0 = 110,760.00"
  - printed: "4a"
    value: ""
    work: "No qualified tips; Part II is filled out only if qualified tips were received"
  - printed: "4b"
    value: ""
    work: "Part II not filled out"
  - printed: "4c"
    value: ""
    work: "Part II not filled out"
  - printed: "5"
    value: ""
    work: "Part II not filled out"
  - printed: "6"
    value: ""
    work: "Part II not filled out"
  - printed: "7"
    value: ""
    work: "Part II not filled out"
  - printed: "8"
    value: ""
    work: "Part II not filled out"
  - printed: "9"
    value: ""
    work: "Part II not filled out"
  - printed: "10"
    value: ""
    work: "Part II not filled out"
  - printed: "12"
    value: ""
    work: "Part II not filled out"
  - printed: "13"
    value: ""
    work: "Part II not filled out; no tips deduction"
  - printed: "14a"
    value: "0.00"
    work: "Filer said yes to overtime, but no qualified overtime amount was given"
  - printed: "14b"
    value: "0.00"
    work: "No 1099-NEC or 1099-MISC overtime given"
  - printed: "14c"
    value: "0.00"
    work: "0 + 0 = 0"
  - printed: "15"
    value: "0.00"
    work: "Smaller of 0 or 25,000 (MFJ) = 0"
  - printed: "16"
    value: "110760.00"
    work: "Line 3"
  - printed: "17"
    value: "300000.00"
    work: "MFJ amount"
  - printed: "18"
    value: "-189240.00"
    work: "110,760 - 300,000 = -189,240; zero or less, so line 15 goes to line 21"
  - printed: "20"
    value: ""
    work: "Skipped because line 18 is zero or less"
  - printed: "21"
    value: "0.00"
    work: "Amount from line 15 = 0"
  - printed: "23"
    value: "4060.00"
    work: "Line 22a column (iii) 4,060.00; line 22b none"
  - printed: "24"
    value: "4060.00"
    work: "Smaller of 4,060 or 10,000"
  - printed: "25"
    value: "110760.00"
    work: "Line 3"
  - printed: "26"
    value: "200000.00"
    work: "MFJ amount"
  - printed: "27"
    value: "-89240.00"
    work: "110,760 - 200,000 = -89,240; zero or less, so line 24 goes to line 30"
  - printed: "29"
    value: ""
    work: "Skipped because line 27 is zero or less"
  - printed: "30"
    value: "4060.00"
    work: "Amount from line 24"
  - printed: "31"
    value: ""
    work: "Not born before 1/2/1961 (no spouse qualification given); Part V not filled out"
  - printed: "32"
    value: ""
    work: "Part V not filled out"
  - printed: "33"
    value: ""
    work: "Part V not filled out"
  - printed: "34"
    value: ""
    work: "Part V not filled out"
  - printed: "35"
    value: ""
    work: "Part V not filled out"
  - printed: "36a"
    value: ""
    work: "Taxpayer not born before 1/2/1961"
  - printed: "36b"
    value: ""
    work: "No spouse born before 1/2/1961 given"
  - printed: "37"
    value: ""
    work: "No enhanced senior deduction"
  - printed: "38"
    value: "4060.00"
    work: "0 + 0 + 4,060 + 0 = 4,060.00"
```
```
