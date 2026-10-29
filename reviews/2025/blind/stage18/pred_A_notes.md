# Preparer A: notes on the twenty 2025 Form 8962 returns

Sources: i8962.cols.txt (Instructions for Form 8962, 2025), f8962.cols.txt, i1040gi.cols.txt (Social Security Benefits Worksheet), rp-2024-40.cols.txt section 4.07 (repayment limits; it agrees with Table 5).

## Rules used for every return
- Line 1 (i8962 p.7-8): you, plus your spouse on a joint return, plus your dependents.
- Line 2a, Worksheet 1-1 (p.8): AGI + tax-exempt interest + (Form 1040 line 6a minus 6b). Line 2b, Worksheet 1-2: only for dependents who are required to file. Where no dependent must file, line 2b is "blank" ("Complete line 2b only if...", p.22) and line 3 equals line 2a.
- Line 4, Tables 1-1/1-2/1-3 (p.8-9). Above 8 people, add $5,380 per person in the 48 states.
- Line 5, Worksheet 2 (p.9): if line 3 > 4 x line 4, enter 401. Otherwise floor(line 3 / line 4 x 100).
- Line 7, Table 2 (p.11): "150 or less" gives 0.0000; "400 or more" gives 0.0850. Values between come straight from the table.
- Line 8a = line 3 x line 7, rounded to the nearest dollar. Line 8b = 8a / 12, rounded (p.12).
- Line 10 (p.14): "yes" only if every plan covers all 12 months with the same column A and column B each month.
- Line 11 and lines 12-23 (p.15-17). With two forms from the same state, column (b) comes from one form only; with different states, column B amounts are added. Months with no coverage are left blank in all columns, (c) included (p.17).
- Lines 26-29 (p.17-18). If 24 > 25, line 26 = 24 - 25 and also goes on Schedule 3 line 9, and lines 27-29 are skipped. If 25 > 24, line 26 is blank. Line 28 comes from Table 5: Single gets $375/$975/$1,625; every other status gets $750/$1,950/$3,250, for line 5 below 200, 200-299 and 300-399. If line 5 is 400 or more, line 28 is blank and line 29 = line 27. Line 29 also goes on Schedule 2 line 1a.

## Per return (HI = household income, FPL = poverty line)
- P1: family 1. HI 40,000 / 15,060 = 2.656, so line 5 = 265 and line 7 = 0.0460. 8a 1,840, 8b 153. Line 11: a 6,000, b 5,400, c 1,840, d 3,560, e 3,560, f 3,500. Net PTC 60.
- P2: 25,000 gives 166 and 0.0064. 8a 160, 8b 13. d 4,880, so e = a = 4,800. f 4,200. Net 600.
- P3: 55,000 gives 365 and 0.0763. 8a = 4,196.50, rounded **up** to 4,197 (half dollar, see ambiguities). 8b 349.75, rounded to 350. d 2,403, e 2,403, f 6,000. Excess 3,597; Single limit for 300-399 is 1,625, so line 29 = 1,625.
- P4: 70,000 > 60,240 (4 x FPL), so line 5 = 401 and line 7 = 0.0850. 8a 5,950, 8b 496. d = e = 1,850, f 3,000. Excess 1,150. Line 28 blank, line 29 = 1,150.
- P5: HOH, family 3, FPL 25,820. 50,000 gives 193 and 0.0172. 8a 860, 8b 72. d 11,140, e 11,140, f 9,000. Net 2,140.
- P6: MFJ, family 4, FPL 31,200. 90,000 gives 288 and 0.0552. 8a 4,968, 8b 414. d = e = 11,832, f 15,000. Excess 3,168; the limit for other statuses at 200-299 is 1,950. Line 29 = 1,950.
- P7: 12,000 / 15,060 gives 79 (below 100). The Marketplace estimated at least 100% and APTC was paid, so the filer still qualifies (p.9-10) and continues to line 7. Line 5 = 79 is "150 or less", so line 7 = 0.0000. 8a 0, 8b 0. d = b = 5,160, e 5,160, f 5,000. Net 160.
- P8: line 5 = 79, and the Marketplace estimate was below 100%. So P8 is not an applicable taxpayer. APTC was paid, so per p.10 lines 7, 8a and 8b are skipped and the return goes on to line 9. Line 10 = yes. 11a 5,400, 11b 5,160, 11c and 11d blank (line 8a was skipped), 11e 0 (no PTC allowed), 11f 5,000. Line 24 0, line 25 5,000, line 27 5,000. Line 28 = 375 (Single, below 200). Line 29 = 375. See ambiguities.
- P9: coverage April-December only, so line 10 = no. 35,000 gives 232 and 0.0328. 8a 1,148, 8b 96. Lines 12-14 are blank. April-December each month: a 480, b 460, c 96, d 364, e 364, f 300. Line 24 3,276, line 25 2,700, net 576.
- P10: MFJ, family 2, FPL 20,440. Column B changes in July, so line 10 = no. 75,000 gives 366 and 0.0765. 8a = 5,737.50, rounded **up** to 5,738. 8b 478. Jan-Jun: d = e = 372, f 500. Jul-Dec: d = e = 472, f 550. Line 24 5,064, line 25 6,300, excess 1,236. The limit is 3,250, so line 29 = 1,236.
- P11: two forms from the same state, both full year with level amounts, so line 10 = yes. 11a = 4,200 + 1,800 = 6,000. 11b comes from one form only: 6,000. 38,000 gives 252 and 0.0408. 8a 1,550, 8b 129. d = e = 4,450. 11f = 2,400 + 600 = 3,000. Net 1,450.
- P12: each form covers fewer than 12 months, so line 10 = no. Both states are treated as contiguous 48, since the facts give no Alaska or Hawaii. 252 and 0.0408, 8b 129. Jan-May: a 500, b 480, d = e = 351, f 300. Jun-Dec: a 520, b 510, d = e = 381, f 320. Line 24 4,422, line 25 3,740, net 682.
- P13: Alaska, Table 1-2, FPL 18,810. 30,000 gives 159 and 0.0036. 8a 108, 8b 9. d = e = 7,572, f 6,000. Net 1,572.
- P14: Hawaii, Table 1-3, family 2, FPL 23,500. 32,000 gives 136, which is "150 or less", so 0.0000. 8a 0, 8b 0. e = b = 9,120, f 7,800. Net 1,320.
- P15: the child must file, so line 2b = 8,000 (Worksheet 1-2) and line 3 = 50,000. Family 2, FPL 20,440. Line 5 = 244, line 7 = 0.0376. 8a 1,880, 8b 157. d = e = 8,680, f 8,000. Net 680.
- P16: Social Security Benefits Worksheet: L1 9,000; L2 4,500; L3 28,000; L4 1,200; L5 33,700; L6 0; L7 33,700; L8 25,000; L9 8,700; L10 9,000; L11 0; L12 8,700; L13 4,350; L14 4,350; L15 0; L16 4,350; L17 7,650; L18 4,350. So taxable SS = 4,350 and AGI = 32,350. Worksheet 1-1: 32,350 + 1,200 + (9,000 - 4,350) = 38,200. That gives line 5 = 253 and line 7 = 0.0412. 8a = 1,573.84, rounded to 1,574; 8b 131. d = e = 4,426, f 4,000. Net 426.
- P17: no APTC; facts say column B is correct, so line 10 = yes. 30,000 gives 199 and 0.0196. 8a 588, 8b 49. d 4,212, which is less than a = 4,560. e 4,212, f 0. Net 4,212.
- P18: 60,240 = exactly 4 x 15,060. Worksheet 2 line 4 asks whether line 1 is *more than* line 3; it is not, so divide: 4.00, giving line 5 = 400. Line 7 = 0.0850 ("400 or more"). 8a = 5,120.40, rounded to 5,120. 8b = 426.67, rounded to 427. d = e = 1,840, f 1,000. Net 840.
- P19: 60,347 > 60,240, so line 5 = 401 and line 7 = 0.0850. 8a = 5,129.495, rounded to 5,129. 8b 427. d = 4,231, e 4,231 (a = 9,600), f 2,000. Net 2,231.
- P20: family 9. FPL = 52,720 + 5,380 = 58,100. 100,000 gives 172 and 0.0088. 8a 880, 8b 73. d = e = 24,320, f 20,000. Net 4,320.

## Ambiguities and readings used
1. **Exact half dollars on line 8a (P3 4,196.50; P10 5,737.50).** "Round to nearest whole dollar" does not say how to round a half. I used round-half-up, giving 4,197 and 5,738. Round-half-even would give 4,196 and 5,738, so only P3 changes: P3 line 11c/d/e would be 4,196 / 2,404 / 2,404, with line 27 3,596. Line 29 stays at the 1,625 limit.
2. **P8 (below 100% FPL, not an applicable taxpayer).** The instructions say only "skip lines 7 and 8, and go to line 9". They do not say what goes in line 11 columns (a)-(e). That contrasts with the married-filing-separately case, which says to complete only column (f). My reading: (a) and (b) are copied from Form 1095-A, as their column rules are unconditional; (c) and (d) are blank because 8a was skipped; (e) is 0 because no PTC is allowed; line 24 is 0. An alternative is to leave 11a-11e all blank, by analogy to MFS. Either way lines 24-29 are the same. I also applied Table 5 ("less than 200" gives $375) to this non-applicable taxpayer. The text gives no exception for this case.
3. **Line 2b** is reported as "blank", not 0.00, when no dependent must file (p.22 "Complete line 2b only if...").
4. **Line 5 = 400 exactly (P18).** The worksheet's "more than" test means 400, not 401. Table 2 and Table 5 both treat "400 or more" the same as 401, so the outcome does not change.
5. **P11:** one column B was used, not two added together, per the same-state rule. The facts give the same $500 on both forms.
6. Table 2's first column header reads "less than 150 | 150 | 151 ..." with values "0.0000 0.0000 0.0004 ...". So 151 = 0.0004, which agrees with the tip "150 or less is 0.0000".
