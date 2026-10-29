# Stage 19 blind prediction B: notes

Sources used: f8863, i8863 (line 7 conditions p.6-7, Credit Limit Worksheet p.7, AQEE Worksheet p.9, Qualified Education Expenses p.4), p970 ch.2-3 (EIN requirement), i1040gi (standard deduction amounts in What's New: 15,750 / 31,500 / 23,625; Tax Table pp.68-79; Tax Computation Worksheet p.80), f1040s8812 and i1040s8812 Credit Limit Worksheet A.

General readings (apply to all returns):
- Cents are kept, not rounded to whole dollars. Line 6 and line 17 are rounded to 3 places.
- Tax Table values were read from the table. I checked the rows directly for E1 (68,800-68,850 single: 10,056), E3 (38,350-38,400 HOH: 4,265), E4 (13,500-13,550 MFJ: 1,353), E5, E7, E8 and E9. E6 (6,250-6,300: 628) and E10 (71,000-71,050 single: 10,540) come from the table's midpoint rule, which I confirmed on neighbouring rows.
- When Part I has no AOTC student (line 1 = 0), I still filled in lines 2-9 as the form reads (line 7 = 0, line 8 = 0, line 9 = 0), because the form gives no skip instruction for Part I. Another reading would leave Part I blank.
- When line 10 = 0, the form says to skip lines 11-17 (I report them as "blank") and enter 0 on line 18.
- When the line 7 box is checked, line 8 is "blank" and line 9 = line 7. Form 1040 line 29 is then reported as 0.
- Credit Limit Worksheet line 5 is 0 on every return (no Schedule 3 lines 1, 2, 6d or 6l). Line 18 = line 16 (no Schedule 2). Line 22 = line 18 - (line 19 + Schedule 3 line 8, which equals s3.3). Line 24 = line 22.
- Schedule 8812: a child aged 17 or over counts as an other dependent ($500). A child under 17 gets $2,200. There is no phaseout (line 10 = 0). Credit Limit Worksheet A line = line 18 - Schedule 3 line 3.
- Part III lines that the flow never reaches are reported as "blank".

## E1 (Single, AGI 84,567)
Filer AOTC: tuition 3,100 + books 450 = 3,550. Books bought elsewhere count for AOTC under i8863 Qualified Education Expenses. Line 27 = 3,550, line 28 = 1,550, line 29 = 387.50, line 30 = 2,387.50. Line 4 = 5,433, so line 6 = 0.5433, rounded to 0.543. Line 7 = 1,296.41, line 8 = 518.56, line 9 = 777.85. Taxable income 68,817 gives tax 10,056. CLW line 7 = 777.85. Line 22 = 9,278.15.

## E2 (MFJ, AGI 170,866)
- Son: 4,800 + 350 - 1,000 Pell = 4,150, capped at 4,000 on line 27. Line 30 = 2,500. I took the Pell grant as tax-free, as the facts state. Electing to include it in income would not change the result, because the son's expenses exceed 4,000 either way.
- Spouse: line 23 No (default: no prior AOTC), line 24 Yes (half-time in a master's degree program), line 25 Yes (bachelor's completed before 2025), so she goes to line 31 = 9,000 and line 26 is not reached.
- Part I: line 6 = 9,134/20,000 = 0.4567, rounded to 0.457. Line 7 = 1,142.50, line 8 = 457, line 9 = 685.50.
- Part II: line 12 = 1,800, line 18 = 822.60. CLW line 3 = 1,508.10.
- Taxable income 139,366, so the TCW Section B applies: 139,366 x 0.22 - 10,172 = 20,488.52 (kept with cents; a whole-dollar entry would be 20,489).
- Line 19: ODC 500. Line 22 = 18,480.42.

## E3 (HOH, AGI 62,000)
- Daughter: graduate student, bachelor's done in 2024. Line 23 No, 24 Yes, 25 Yes, so LLC 7,200.
- Filer: job-skills courses outside a degree program. Line 23 No, line 24 No, so LLC 5,000 (LLC allows courses to improve job skills).
- Line 10 = 12,200, line 11 = 10,000, line 12 = 2,000, line 17 = 1.0, line 18 = 2,000.
- Taxable income 38,375 gives tax 4,265. CLW line 7 = 2,000. ODC 500 (daughter is 22). Line 22 = 1,765.
- Part I is filled with zeros (general reading above).

## E4 (MFJ, AGI 45,000)
- Son AOTC 4,000, so line 30 = 2,500. Line 7 = 2,500, line 8 = 1,000, line 9 = 1,500. Line 10 = 0, so line 18 = 0.
- Taxable income 13,500 gives tax 1,353. CLW line 7 = 1,353, so tax goes to 0.
- Schedule 8812 line 12 = 2,700 (daughter 2,200 + son 500), but CLW A = 0, so line 19 = 0. The ACTC on line 28 was not asked for.

## E5 (Single, born 5/14/2008, age 17)
- Condition 1a (under 18) applies, a parent is alive, and the return is not joint, so the box is checked. The support test does not matter for condition 1a.
- AOTC 2,500, line 8 blank, line 9 = 2,500. Tax 1,475 is fully offset. Line 29 = 0.

## E6 (Single, born 3/10/2007, age 18)
- Condition 1b: earned income 22,000 is less than half of support (25,000). The support she paid herself from inheritance savings still counts as support; the test compares earned income with total support. So the box is checked.
- AQEE = 3,400, line 30 = 2,350. Tax 628 is fully offset.

## E7 (Single, born 8/22/2003, age 22)
- Condition 1c: full-time student (5+ months), and earned income 26,000 is less than 30,000 (half of 60,000). The box is checked. If the 1,500 scholarship were inside the 60,000 and excluded from support, half would be 29,250, so the result is the same.
- AQEE = 5,200 - 1,500 tax-free scholarship = 3,700. Line 28 = 1,700, line 29 = 425, line 30 = 2,425. Tax 1,028 is fully offset.

## E8 (Single, born 2/11/2004, age 21)
- Earned income 35,000 is less than 40,000, but both parents died in 2019, so condition 2 fails and the credit stays refundable. Box not checked.
- AQEE = 4,600, capped at 4,000, line 30 = 2,500. Line 8 = 1,000, line 9 = 1,500. Tax 2,075, line 22 = 575.

## E9 (HOH, AGI 58,000)
- Son: AOTC claimed for 4 prior years, so line 23 Yes and lines 24-30 are blank. LLC 8,000 (books not required are excluded for LLC).
- Filer: she meets lines 23-26 (No/Yes/No/No), but the institution's EIN is unavailable. The AOTC requires the EIN (i8863 requirement 7; p970), so she cannot claim the AOTC. The Tip says she may claim the LLC instead, so line 31 = 1,800 and lines 27-30 are blank.
  - Ambiguity: the form's literal flow after line 26 = No says to complete lines 27-30. I answered lines 23-26 truthfully and still routed her to line 31. An alternative reading would claim the AOTC (1,800 x 100% = 1,800) without the EIN, which would be improper.
- Line 10 = 9,800, line 12 = 1,960, line 18 = 1,960. Tax 3,785, CLW line 7 = 1,960.
- Schedule 8812 line 12 = 2,700, CLW A = 3,785 - 1,960 = 1,825, so line 19 = 1,825. Line 22 = 0.

## E10 (Single, AGI 86,782)
- Less than half-time, so line 23 No, line 24 No, and LLC applies. AQEE = 6,000 - 400 refund received in 2025 (AQEE worksheet line 2c) = 5,600. Books are excluded for LLC.
- Line 12 = 1,120, line 17 = 3,218/10,000, rounded to 0.322, line 18 = 360.64.
- Taxable income 71,032 gives tax 10,540. Line 22 = 10,179.36. Part I is zeros, with line 6 = 0.322.
