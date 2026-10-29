# Preparer B: 2025 Form 8962 derivations (20 returns)

Sources: f8962.cols.txt; i8962.txt pages 8-11 (Worksheets 1-1, 1-2, 2; Tables 1-1/1-2/1-3; Table 2), 14-18 (lines 10, 11, 12-23, 24-29, Table 5); i1040gi.cols.txt p.32 (Social Security Benefits Worksheet) and p.23 (round half up: "increase amounts from 50 to 99 cents"); rp-2024-40 sec. on 36B(f)(2)(B) (same $375/$750, $975/$1,950, $1,625/$3,250 limits as Table 5); usc-26-36b (f)(2)(B) (limit keyed to household income %); p974 (applicable-taxpayer flowchart).

Common rules used:
- Line 2a = Worksheet 1-1 (AGI + tax-exempt interest + nontaxable SS). Line 2b = Worksheet 1-2 (0 unless a dependent is required to file). Line 3 = 2a + 2b.
- Line 4: Table 1-1 (48 states: 15,060 / 20,440 / 25,820 / 31,200 ...; +5,380 above 8); Table 1-2 Alaska (1 = 18,810); Table 1-3 Hawaii (2 = 23,500).
- Line 5 = Worksheet 2: if line 3 > 4 x line 4, enter 401; else floor(line3/line4 x 100).
- Line 7 = Table 2 (p.11): <=150 -> 0.0000; >=400 -> 0.0850; table values otherwise (the 300-400 band is printed rounded to 4 places, e.g. 365 -> 0.0763; I used the printed value).
- 8a = round(line 3 x line 7); 8b = round(8a / 12); nearest dollar, half up.
- Line 10 "yes" when every policy covers all 12 months with constant A and B (p.14); else "no".
- Line 11: (a) sum of 33A, (b) 33B of one form (same-state) or sum (different states), (c) = 8a, (d) = max(0, b - c), (e) = min(a, d), (f) sum of 33C.
- Lines 12-23: (c) = 8b; months with (a) and (b) blank leave (c) blank (p.17); I also left (d)-(f) blank for those months.
- 26 = 24 - 25 if positive (also Schedule 3 line 9), else blank; 27 = 25 - 24; 28 = Table 5 (single vs. any other status; "400 or more" -> leave blank); 29 = min(27, 28) or 27 if 28 blank (also Schedule 2 line 1a). Lines 27-29 "skipped" when line 26 is filled.

| Ret | Fam | Line 3 | FPL | L5 | L7 | 8a | 8b | 24 | 25 | 26 | 27 | 28 | 29 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 1 | 40,000 | 15,060 | 265 | 0.0460 | 1,840 | 153 | 3,560 | 3,500 | 60 | - | - | - |
| P2 | 1 | 25,000 | 15,060 | 166 | 0.0064 | 160 | 13 | 4,800 (a < d) | 4,200 | 600 | - | - | - |
| P3 | 1 | 55,000 | 15,060 | 365 | 0.0763 | 4,197 (4,196.50 rounds up) | 350 | 2,403 | 6,000 | blank | 3,597 | 1,625 | 1,625 |
| P4 | 1 | 70,000 | 15,060 | 401 (>60,240) | 0.0850 | 5,950 | 496 | 1,850 | 3,000 | blank | 1,150 | blank (>=400) | 1,150 |
| P5 | 3 HOH | 50,000 | 25,820 | 193 | 0.0172 | 860 | 72 | 11,140 | 9,000 | 2,140 | - | - | - |
| P6 | 4 MFJ | 90,000 | 31,200 | 288 | 0.0552 | 4,968 | 414 | 11,832 | 15,000 | blank | 3,168 | 1,950 (other, 200-300) | 1,950 |
| P7 | 1 | 12,000 | 15,060 | 79 | 0.0000 | 0 | 0 | 5,160 | 5,000 | 160 | - | - | - |
| P8 | 1 | 12,000 | 15,060 | 79 | skipped | skipped | skipped | 0 | 5,000 | blank | 5,000 | 375 (<200 single) | 375 |
| P9 | 1 | 35,000 | 15,060 | 232 | 0.0328 | 1,148 | 96 | 3,276 (9 x 364) | 2,700 | 576 | - | - | - |
| P10 | 2 MFJ | 75,000 | 20,440 | 366 | 0.0765 | 5,738 (5,737.50 up) | 478 | 5,064 | 6,300 | blank | 1,236 | 3,250 | 1,236 |
| P11 | 1 | 38,000 | 15,060 | 252 | 0.0408 | 1,550 | 129 | 4,450 | 3,000 | 1,450 | - | - | - |
| P12 | 1 | 38,000 | 15,060 | 252 | 0.0408 | 1,550 | 129 | 4,422 | 3,740 | 682 | - | - | - |
| P13 | 1 AK | 30,000 | 18,810 | 159 | 0.0036 | 108 | 9 | 7,572 | 6,000 | 1,572 | - | - | - |
| P14 | 2 HI | 32,000 | 23,500 | 136 | 0.0000 | 0 | 0 | 9,120 | 7,800 | 1,320 | - | - | - |
| P15 | 2 HOH | 50,000 (42,000 + 8,000) | 20,440 | 244 | 0.0376 | 1,880 | 157 | 8,680 | 8,000 | 680 | - | - | - |
| P16 | 1 | 38,200 | 15,060 | 253 | 0.0412 | 1,574 | 131 | 4,426 | 4,000 | 426 | - | - | - |
| P17 | 1 | 30,000 | 15,060 | 199 | 0.0196 | 588 | 49 | 4,212 | 0 | 4,212 | - | - | - |
| P18 | 1 | 60,240 | 15,060 | 400 (=4x, not more) | 0.0850 | 5,120 | 427 | 1,840 | 1,000 | 840 | - | - | - |
| P19 | 1 | 60,347 | 15,060 | 401 | 0.0850 | 5,129 (5,129.495 down) | 427 | 4,231 | 2,000 | 2,231 | - | - | - |
| P20 | 9 MFJ | 100,000 | 58,100 (52,720 + 5,380) | 172 | 0.0088 | 880 | 73 | 24,320 | 20,000 | 4,320 | - | - | - |

Per-return notes:
- P1-P6, P11, P13-P20: full year, constant A and B -> line 10 yes, line 11 as above (11a = 12 x A, 11b = 12 x B, 11f = 33C).
- P2: 11e = 11a 4,800 because enrollment premium is less than 11d 4,880.
- P7: line 5 = 79 (< 100), but the "Estimated household income at least 100%" exception applies (Marketplace estimate >= 100%, APTC paid, otherwise applicable) -> continue to line 7; Table 2 "less than 150" -> 0.0000. 11: 5,400 / 5,160 / 0 / 5,160 / 5,160 / 5,000.
- P8: line 5 = 79, exception not met -> not an applicable taxpayer; i8962 p.10: "If APTC was paid ... skip lines 7 and 8, and go to line 9." See ambiguity 1 for line 11. PTC 0; 27 = 5,000; Table 5 still applies (statute 36B(f)(2)(B) keys the limit to household income %, not applicable-taxpayer status) -> 375.
- P9: line 10 no (fewer than 12 months, TIP p.14). Jan-Mar blank. Apr-Dec: 480 / 460 / 96 / 364 / 364 / 300.
- P10: SLCSP changes in July -> line 10 no. Jan-Jun: 900 / 850 / 478 / 372 / 372 / 500. Jul-Dec: 900 / 950 / 478 / 472 / 472 / 550. Family 2.
- P11: two same-state policies: 11a = 4,200 + 1,800 = 6,000; 11b = column B of only one form = 6,000 (p.15 "do not add"); 11f = 2,400 + 600 = 3,000.
- P12: moved; neither policy is 12 months -> line 10 no. Jan-May 500 / 480 / 129 / 351 / 351 / 300; Jun-Dec 520 / 510 / 129 / 381 / 381 / 320. In each month only one state's form shows coverage, so the "add column B from each state" rule adds nothing. FPL Table 1-1 (both states contiguous).
- P13: Table 1-2 Alaska, family 1. 11: 7,800 / 7,680 / 108 / 7,572 / 7,572 / 6,000.
- P14: Table 1-3 Hawaii, family 2. 11: 9,600 / 9,120 / 0 / 9,120 / 9,120 / 7,800.
- P15: 2b = 8,000 (Worksheet 1-2: dependent required to file; given MAGI used directly). 11: 10,800 / 10,560 / 1,880 / 8,680 / 8,680 / 8,000.
- P16: SS Benefits Worksheet (i1040gi p.32): L1 9,000; L2 4,500; L3 28,000; L4 1,200; L5 33,700; L6 0; L7 33,700; L8 25,000; L9 8,700; L10 9,000; L11 0; L12 8,700; L13 4,350; L14 4,350; L15 0; L16 4,350; L17 7,650; L18 4,350 taxable. AGI = 32,350. Worksheet 1-1: 32,350 + 1,200 + (9,000 - 4,350 = 4,650) = 38,200. 11: 6,240 / 6,000 / 1,574 / 4,426 / 4,426 / 4,000.
- P17: no APTC; the Form 1095-A column B "may be wrong" warning (p.14) does not change anything since the facts say B is correct and constant -> line 10 yes. 25 = 0, 26 = 4,212.
- P18: line 3 equals exactly 4 x 15,060 = 60,240; Worksheet 2 line 4 asks "more than", so divide: 400 -> Table 2 "400 or more" 0.0850. No repayment, so the "400 or more, leave 28 blank" question does not arise.
- P19: 60,347 > 60,240 -> 401 -> 0.0850; 8a = 5,129.495 -> 5,129.
- P20: family 9 -> 52,720 + 5,380 = 58,100.

Ambiguities and readings used:
1. P8 (not an applicable taxpayer below 100% FPL, APTC paid). The instructions say to skip lines 7-8 and go to line 9 but give no explicit line 11 / lines 12-23 direction for this case (the "complete only column (f)" and "enter -0- on line 24" directions are written for MFS filers without Exception 2). I applied that treatment by analogy: line 10 yes (full year, constant), 11a-11e skipped, 11f 5,000, line 24 0, 25 = 27 = 5,000, 28 = 375, 29 = 375. Another reading would fill 11a/11b from the 1095-A and enter 11e = 0; lines 24-29 come out the same either way. A reading that no repayment limit applies (29 = 5,000) is not supported: Table 5 and 36B(f)(2)(B) depend only on line 5 and filing status.
2. Table 2 300-400 band: values printed to 4 decimals (e.g. 365 -> 0.0763, not 0.07625). I used the printed table.
3. Line 5 at exactly 400% (P18): "more than" means 60,240 gives 400, not 401. The figure is 0.0850 either way.
4. Lines 12-23 for uncovered months (P9 Jan-Mar): the instructions only say to leave (c) blank; I reported (a)-(f) all blank.
5. Line 2b with no filing dependents: reported 0.00 (Worksheet 1-2 total) rather than blank.
6. Lines 27-29 when line 26 is filled: "skipped" (p.18 "Skip lines 27 through 29"); Schedule 2 line 1a "blank"; Schedule 3 line 9 "blank" when line 26 is blank.
