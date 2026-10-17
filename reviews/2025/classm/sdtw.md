# Class M hand-work — sdtw

`Schedule D Tax Worksheet` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### case classm.sdtw.1 — prompt sha256 14a958c97eec5436032c9cfc1c0dc539a339bad911ee0c5571e7a8da6c853ce3; branches: sdtw.after22:true, sdtw.after32:true, sdtw.use1250:false, sdtw.use28:true, sdtw.line5:floor, sdtw.line6:floor, sdtw.line7:left, sdtw.line8:left, sdtw.line9:positive, sdtw.line12:right, sdtw.line14:positive, sdtw.line16:right, sdtw.line17:right, sdtw.line18:positive, sdtw.line19:right, sdtw.line20:right, sdtw.line21:left, sdtw.raw23:right, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:left, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:positive, sdtw.line29#0, sdtw.raw30:left, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#0, sdtw.line34#0, sdtw.raw35:right, sdtw.line35#1, sdtw.line36#1, sdtw.line37#1, sdtw.raw38:floor, sdtw.line38#1, sdtw.raw39:floor, sdtw.line39#1, sdtw.line40#1, sdtw.line41#0, sdtw.line42#0, sdtw.line43#0, sdtw.line47:left

### classm.sdtw.1 — 1 — Taxable income
Status: **AGREE**

Value: $339,977.00

### classm.sdtw.1 — 2 — Qualified dividends
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $334,207.00

### classm.sdtw.1 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $64,750.00

### classm.sdtw.1 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $64,750.00

### classm.sdtw.1 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $64,750.00

### classm.sdtw.1 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $334,207.00

### classm.sdtw.1 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.1 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.1 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $334,207.00

### classm.sdtw.1 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $566,700.00

### classm.sdtw.1 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $339,977.00

### classm.sdtw.1 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $334,207.00

### classm.sdtw.1 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $865.50

### classm.sdtw.1 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $5,770.00

### classm.sdtw.1 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 35 — Smaller of line 9 and Schedule D line 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 36 — Add lines 10 and 21
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 37 — Amount from line 1
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 38 — Subtract line 37 from line 36; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 40 — Multiply line 39 by 25 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **DISAGREE**

Project: $339,977.00
Model: $0.00
Work: Sch D line 18 is zero, so skip lines 41-43

Ruling: representation; project retained; model value dropped from the fixture. With Schedule D line 19 zero the worksheet says "skip lines 35 through 40 and go to line 41" (i1040sd p. 16); the instruction to skip lines 41 through 43 when Schedule D line 18 is zero follows line 40 and is only reached through lines 35–40. The project follows the printed flow and computes line 41 (the sum of lines 21, 22, 30, 33 and 39, here all of taxable income), so line 42 is zero and line 43 is zero; the model applied the line-40 instruction from line 34 and left lines 41–43 blank. Lines 42–45 agree either way, and the data-level property `sdtw_skip_rule` checks that a skipped line 42 is zero when computed. No change to the data. [dropped]

### classm.sdtw.1 — 42 — Subtract line 41 from line 1
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 43 — Multiply line 42 by 28 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $85,646.95

### classm.sdtw.1 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $85,646.95

### case classm.sdtw.2 — prompt sha256 5c5a5014eba8c6b065222c45e207f3e967cea5ba6ac5d0c5ff0c87800831405b; branches: sdtw.after22:false, sdtw.after32:false, sdtw.use1250:false, sdtw.use28:false, sdtw.line5:positive, sdtw.line6:positive, sdtw.line7:right, sdtw.line8:right, sdtw.line9:floor, sdtw.line12:left, sdtw.line14:floor, sdtw.line16:left, sdtw.line17:left, sdtw.line18:floor, sdtw.line19:left, sdtw.line20:left, sdtw.line21:left, sdtw.raw23:left, sdtw.line23#1, sdtw.line24#1, sdtw.raw25:floor, sdtw.line25#1, sdtw.line26#1, sdtw.raw27:right, sdtw.line27#1, sdtw.line28#1, sdtw.raw29:floor, sdtw.line29#1, sdtw.raw30:left, sdtw.line30#1, sdtw.line31#1, sdtw.line32#1, sdtw.line33#1, sdtw.line34#1, sdtw.raw35:left, sdtw.line35#1, sdtw.line36#1, sdtw.line37#1, sdtw.raw38:floor, sdtw.line38#1, sdtw.raw39:floor, sdtw.line39#1, sdtw.line40#1, sdtw.line41#1, sdtw.line42#1, sdtw.line43#1, sdtw.line47:left

### classm.sdtw.2 — 1 — Taxable income
Status: **AGREE**

Value: $39,605.00

### classm.sdtw.2 — 2 — Qualified dividends
Status: **AGREE**

Value: $56,984.00

### classm.sdtw.2 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $3,853.00

### classm.sdtw.2 — 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $3,853.00

### classm.sdtw.2 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $53,131.00

### classm.sdtw.2 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $-31,444.00

### classm.sdtw.2 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $53,131.00

### classm.sdtw.2 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $53,131.00

### classm.sdtw.2 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $64,750.00

### classm.sdtw.2 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $39,605.00

### classm.sdtw.2 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $39,605.00

### classm.sdtw.2 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $39,605.00

### classm.sdtw.2 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 35 — Smaller of line 9 and Schedule D line 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 36 — Add lines 10 and 21
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 37 — Amount from line 1
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 38 — Subtract line 37 from line 36; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 40 — Multiply line 39 by 25 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 42 — Subtract line 41 from line 1
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 43 — Multiply line 42 by 28 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $0.00

### case classm.sdtw.3 — prompt sha256 1cbe148680b93aab659988792285258723d68f344d06bcbad732fc7ce2b779c1; branches: sdtw.after22:true, sdtw.after32:true, sdtw.use1250:true, sdtw.use28:true, sdtw.line5:floor, sdtw.line6:positive, sdtw.line7:left, sdtw.line8:left, sdtw.line9:positive, sdtw.line12:right, sdtw.line14:positive, sdtw.line16:right, sdtw.line17:right, sdtw.line18:positive, sdtw.line19:right, sdtw.line20:left, sdtw.line21:right, sdtw.raw23:right, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:right, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:positive, sdtw.line29#0, sdtw.raw30:right, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#0, sdtw.line34#0, sdtw.raw35:right, sdtw.line35#0, sdtw.line36#0, sdtw.line37#0, sdtw.raw38:positive, sdtw.line38#0, sdtw.raw39:floor, sdtw.line39#0, sdtw.line40#0, sdtw.line41#0, sdtw.line42#0, sdtw.line43#0, sdtw.line47:left

### classm.sdtw.3 — 1 — Taxable income
Status: **AGREE**

Value: $376,357.00

### classm.sdtw.3 — 2 — Qualified dividends
Status: **AGREE**

Value: $320,000.00

### classm.sdtw.3 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **AGREE**

Value: $19,848.00

### classm.sdtw.3 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $320,000.00

### classm.sdtw.3 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $19,848.00

### classm.sdtw.3 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $19,848.00

### classm.sdtw.3 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $339,848.00

### classm.sdtw.3 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $15,763.00

### classm.sdtw.3 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $15,763.00

### classm.sdtw.3 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $324,085.00

### classm.sdtw.3 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $52,272.00

### classm.sdtw.3 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.3 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.3 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.3 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $36,509.00

### classm.sdtw.3 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.3 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $52,272.00

### classm.sdtw.3 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $52,272.00

### classm.sdtw.3 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $324,085.00

### classm.sdtw.3 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $324,085.00

### classm.sdtw.3 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $300,000.00

### classm.sdtw.3 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $300,000.00

### classm.sdtw.3 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $52,272.00

### classm.sdtw.3 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $247,728.00

### classm.sdtw.3 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $247,728.00

### classm.sdtw.3 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $37,159.20

### classm.sdtw.3 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $247,728.00

### classm.sdtw.3 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $76,357.00

### classm.sdtw.3 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $15,271.40

### classm.sdtw.3 — 35 — Smaller of line 9 and Schedule D line 19
Status: **AGREE**

Value: $15,680.00

### classm.sdtw.3 — 36 — Add lines 10 and 21
Status: **AGREE**

Value: $392,120.00

### classm.sdtw.3 — 37 — Amount from line 1
Status: **AGREE**

Value: $376,357.00

### classm.sdtw.3 — 38 — Subtract line 37 from line 36; floor at zero
Status: **AGREE**

Value: $15,763.00

### classm.sdtw.3 — 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 40 — Multiply line 39 by 25 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **AGREE**

Value: $376,357.00

### classm.sdtw.3 — 42 — Subtract line 41 from line 1
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 43 — Multiply line 42 by 28 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $58,845.60

### classm.sdtw.3 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $58,845.60

### case classm.sdtw.4 — prompt sha256 a440919937e180975e193057c2ca2f5eb8c9c90d0cad88834c2184e9a251d99b; branches: sdtw.after22:true, sdtw.after32:true, sdtw.use1250:true, sdtw.use28:true, sdtw.line5:floor, sdtw.line6:floor, sdtw.line7:left, sdtw.line8:left, sdtw.line9:positive, sdtw.line12:right, sdtw.line14:positive, sdtw.line16:right, sdtw.line17:right, sdtw.line18:positive, sdtw.line19:right, sdtw.line20:right, sdtw.line21:left, sdtw.raw23:right, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:right, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:floor, sdtw.line29#0, sdtw.raw30:right, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#0, sdtw.line34#0, sdtw.raw35:right, sdtw.line35#0, sdtw.line36#0, sdtw.line37#0, sdtw.raw38:floor, sdtw.line38#0, sdtw.raw39:positive, sdtw.line39#0, sdtw.line40#0, sdtw.line41#0, sdtw.line42#0, sdtw.line43#0, sdtw.line47:left

### classm.sdtw.4 — 1 — Taxable income
Status: **AGREE**

Value: $365,573.00

### classm.sdtw.4 — 2 — Qualified dividends
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **AGREE**

Value: $45.00

### classm.sdtw.4 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $45.00

### classm.sdtw.4 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $45.00

### classm.sdtw.4 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $45.00

### classm.sdtw.4 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $31.00

### classm.sdtw.4 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $31.00

### classm.sdtw.4 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $14.00

### classm.sdtw.4 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $365,559.00

### classm.sdtw.4 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.4 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.4 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.4 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $365,528.00

### classm.sdtw.4 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.4 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.4 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $365,528.00

### classm.sdtw.4 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $14.00

### classm.sdtw.4 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $14.00

### classm.sdtw.4 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $300,000.00

### classm.sdtw.4 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $300,000.00

### classm.sdtw.4 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $365,528.00

### classm.sdtw.4 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $14.00

### classm.sdtw.4 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $2.80

### classm.sdtw.4 — 35 — Smaller of line 9 and Schedule D line 19
Status: **AGREE**

Value: $12.00

### classm.sdtw.4 — 36 — Add lines 10 and 21
Status: **AGREE**

Value: $365,573.00

### classm.sdtw.4 — 37 — Amount from line 1
Status: **AGREE**

Value: $365,573.00

### classm.sdtw.4 — 38 — Subtract line 37 from line 36; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

Value: $12.00

### classm.sdtw.4 — 40 — Multiply line 39 by 25 percent
Status: **AGREE**

Value: $3.00

### classm.sdtw.4 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **AGREE**

Value: $365,554.00

### classm.sdtw.4 — 42 — Subtract line 41 from line 1
Status: **AGREE**

Value: $19.00

### classm.sdtw.4 — 43 — Multiply line 42 by 28 percent
Status: **AGREE**

Value: $5.32

### classm.sdtw.4 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $97,493.17

### classm.sdtw.4 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $97,493.17

## Raw responses

### classm.sdtw.1

```yaml
lines:
  - printed: "1"
    value: "339977.00"
    work: "Form 1040 line 15 = 339,977.00"
  - printed: "2"
    value: "0.00"
    work: "Form 1040 line 3a = 0.00"
  - printed: "3"
    value: "0.00"
    work: "Form 4952 line 4g = 0.00"
  - printed: "4"
    value: "5770.00"
    work: "Form 4952 line 4e = 5,770.00"
  - printed: "5"
    value: "0.00"
    work: "0.00 - 5,770.00 < 0, so enter -0-"
  - printed: "6"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "7"
    value: "5770.00"
    work: "smaller of Sch D line 15 (5,770.00) and line 16 (5,770.00)"
  - printed: "8"
    value: "0.00"
    work: "smaller of line 3 (0.00) and line 4 (5,770.00)"
  - printed: "9"
    value: "5770.00"
    work: "5,770.00 - 0.00"
  - printed: "10"
    value: "5770.00"
    work: "0.00 + 5,770.00"
  - printed: "11"
    value: "0.00"
    work: "Sch D line 18 (0.00) + line 19 (0.00)"
  - printed: "12"
    value: "0.00"
    work: "smaller of 5,770.00 and 0.00"
  - printed: "13"
    value: "5770.00"
    work: "5,770.00 - 0.00"
  - printed: "14"
    value: "334207.00"
    work: "339,977.00 - 5,770.00"
  - printed: "15"
    value: "64750.00"
    work: "Head of household amount"
  - printed: "16"
    value: "64750.00"
    work: "smaller of 339,977.00 and 64,750.00"
  - printed: "17"
    value: "64750.00"
    work: "smaller of 334,207.00 and 64,750.00"
  - printed: "18"
    value: "334207.00"
    work: "339,977.00 - 5,770.00"
  - printed: "19"
    value: "197300.00"
    work: "smaller of 339,977.00 and 197,300.00 (head of household)"
  - printed: "20"
    value: "197300.00"
    work: "smaller of 334,207.00 and 197,300.00"
  - printed: "21"
    value: "334207.00"
    work: "larger of 334,207.00 and 197,300.00"
  - printed: "22"
    value: "0.00"
    work: "64,750.00 - 64,750.00; line 1 is not equal to line 16, so continue to line 23"
  - printed: "23"
    value: "5770.00"
    work: "smaller of 339,977.00 and 5,770.00"
  - printed: "24"
    value: "0.00"
    work: "amount from line 22"
  - printed: "25"
    value: "5770.00"
    work: "5,770.00 - 0.00"
  - printed: "26"
    value: "566700.00"
    work: "Head of household amount"
  - printed: "27"
    value: "339977.00"
    work: "smaller of 339,977.00 and 566,700.00"
  - printed: "28"
    value: "334207.00"
    work: "334,207.00 + 0.00"
  - printed: "29"
    value: "5770.00"
    work: "339,977.00 - 334,207.00"
  - printed: "30"
    value: "5770.00"
    work: "smaller of 5,770.00 and 5,770.00"
  - printed: "31"
    value: "865.50"
    work: "5,770.00 x 0.15"
  - printed: "32"
    value: "5770.00"
    work: "0.00 + 5,770.00; line 1 is not equal to line 32, so continue to line 33"
  - printed: "33"
    value: "0.00"
    work: "5,770.00 - 5,770.00"
  - printed: "34"
    value: "0.00"
    work: "0.00 x 0.20"
  - printed: "35"
    value: "blank"
    work: "Sch D line 19 is zero, so skip lines 35-40"
  - printed: "36"
    value: "blank"
    work: "skipped (Sch D line 19 is zero)"
  - printed: "37"
    value: "blank"
    work: "skipped (Sch D line 19 is zero)"
  - printed: "38"
    value: "blank"
    work: "skipped (Sch D line 19 is zero)"
  - printed: "39"
    value: "blank"
    work: "skipped (Sch D line 19 is zero)"
  - printed: "40"
    value: "blank"
    work: "skipped (Sch D line 19 is zero)"
  - printed: "41"
    value: "blank"
    work: "Sch D line 18 is zero, so skip lines 41-43"
  - printed: "42"
    value: "blank"
    work: "skipped (Sch D line 18 is zero)"
  - printed: "43"
    value: "blank"
    work: "skipped (Sch D line 18 is zero)"
  - printed: "45"
    value: "85646.95"
    work: "865.50 + 0.00 + 0 + 0 + 84,781.45 (given line 44)"
  - printed: "47"
    value: "85646.95"
    work: "smaller of line 45 (85,646.95) and line 46 (86,800.95)"
```

### classm.sdtw.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "39605.00"
    work: "Form 1040 line 15 taxable income = 39,605.00"
  - printed: "2"
    value: "56984.00"
    work: "Form 1040 line 3a qualified dividends = 56,984.00"
  - printed: "3"
    value: "3853.00"
    work: "Form 4952 line 4g = 3,853.00"
  - printed: "4"
    value: "0.00"
    work: "Form 4952 line 4e = 0.00"
  - printed: "5"
    value: "3853.00"
    work: "3,853.00 - 0.00 = 3,853.00"
  - printed: "6"
    value: "53131.00"
    work: "56,984.00 - 3,853.00 = 53,131.00"
  - printed: "7"
    value: "-31444.00"
    work: "smaller of 57,837.00 and -31,444.00 = -31,444.00"
  - printed: "8"
    value: "0.00"
    work: "smaller of 3,853.00 and 0.00 = 0.00"
  - printed: "9"
    value: "0.00"
    work: "-31,444.00 - 0.00 = -31,444.00; zero or less, so -0-"
  - printed: "10"
    value: "53131.00"
    work: "53,131.00 + 0.00 = 53,131.00"
  - printed: "11"
    value: "0.00"
    work: "Sch D line 18 (0.00) + line 19 (0.00) = 0.00"
  - printed: "12"
    value: "0.00"
    work: "smaller of 0.00 and 0.00 = 0.00"
  - printed: "13"
    value: "53131.00"
    work: "53,131.00 - 0.00 = 53,131.00"
  - printed: "14"
    value: "0.00"
    work: "39,605.00 - 53,131.00 < 0, so -0-"
  - printed: "15"
    value: "64750.00"
    work: "head of household = 64,750.00"
  - printed: "16"
    value: "39605.00"
    work: "smaller of 39,605.00 and 64,750.00 = 39,605.00"
  - printed: "17"
    value: "0.00"
    work: "smaller of 0.00 and 39,605.00 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "39,605.00 - 53,131.00 < 0, so -0-"
  - printed: "19"
    value: "39605.00"
    work: "smaller of 39,605.00 and 197,300.00 (HOH) = 39,605.00"
  - printed: "20"
    value: "0.00"
    work: "smaller of 0.00 and 39,605.00 = 0.00"
  - printed: "21"
    value: "0.00"
    work: "larger of 0.00 and 0.00 = 0.00"
  - printed: "22"
    value: "39605.00"
    work: "39,605.00 - 0.00 = 39,605.00, taxed at 0%"
  - printed: "23"
    value: "blank"
    work: "lines 1 and 16 are the same; skip lines 23-43"
  - printed: "24"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "25"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "26"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "27"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "28"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "29"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "30"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "31"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "32"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "33"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "34"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "35"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "36"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "37"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "38"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "39"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "40"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "41"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "42"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "43"
    value: "blank"
    work: "skipped (lines 1 and 16 are the same)"
  - printed: "45"
    value: "0.00"
    work: "lines 31, 34, 40, 43 blank + line 44 (0.00) = 0.00"
  - printed: "47"
    value: "0.00"
    work: "smaller of line 45 (0.00) and line 46 (4,415.00) = 0.00"
```
```

### classm.sdtw.3

```yaml
lines:
  - printed: "1"
    value: "376357.00"
    work: "Form 1040 line 15 taxable income"
  - printed: "2"
    value: "320000.00"
    work: "Form 1040 line 3a qualified dividends"
  - printed: "3"
    value: "0.00"
    work: "Form 4952 line 4g = 0"
  - printed: "4"
    value: "19848.00"
    work: "Form 4952 line 4e = 19,848"
  - printed: "5"
    value: "0.00"
    work: "0 - 19,848 < 0, so -0-"
  - printed: "6"
    value: "320000.00"
    work: "320,000 - 0"
  - printed: "7"
    value: "19848.00"
    work: "smaller of 19,848 (Sch D line 15) and 74,667 (Sch D line 16)"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0 and 19,848"
  - printed: "9"
    value: "19848.00"
    work: "19,848 - 0"
  - printed: "10"
    value: "339848.00"
    work: "320,000 + 19,848"
  - printed: "11"
    value: "15763.00"
    work: "Sch D line 18 (83) + line 19 (15,680)"
  - printed: "12"
    value: "15763.00"
    work: "smaller of 19,848 and 15,763"
  - printed: "13"
    value: "324085.00"
    work: "339,848 - 15,763"
  - printed: "14"
    value: "52272.00"
    work: "376,357 - 324,085"
  - printed: "15"
    value: "48350.00"
    work: "MFS 0% threshold"
  - printed: "16"
    value: "48350.00"
    work: "smaller of 376,357 and 48,350"
  - printed: "17"
    value: "48350.00"
    work: "smaller of 52,272 and 48,350"
  - printed: "18"
    value: "36509.00"
    work: "376,357 - 339,848"
  - printed: "19"
    value: "197300.00"
    work: "smaller of 376,357 and 197,300 (MFS)"
  - printed: "20"
    value: "52272.00"
    work: "smaller of 52,272 and 197,300"
  - printed: "21"
    value: "52272.00"
    work: "larger of 36,509 and 52,272"
  - printed: "22"
    value: "0.00"
    work: "48,350 - 48,350; line 1 differs from line 16, so continue to line 23"
  - printed: "23"
    value: "324085.00"
    work: "smaller of 376,357 and 324,085"
  - printed: "24"
    value: "0.00"
    work: "amount from line 22"
  - printed: "25"
    value: "324085.00"
    work: "324,085 - 0"
  - printed: "26"
    value: "300000.00"
    work: "MFS 15% threshold"
  - printed: "27"
    value: "300000.00"
    work: "smaller of 376,357 and 300,000"
  - printed: "28"
    value: "52272.00"
    work: "52,272 + 0"
  - printed: "29"
    value: "247728.00"
    work: "300,000 - 52,272"
  - printed: "30"
    value: "247728.00"
    work: "smaller of 324,085 and 247,728"
  - printed: "31"
    value: "37159.20"
    work: "247,728 x 0.15"
  - printed: "32"
    value: "247728.00"
    work: "0 + 247,728; not equal to line 1, so continue to line 33"
  - printed: "33"
    value: "76357.00"
    work: "324,085 - 247,728"
  - printed: "34"
    value: "15271.40"
    work: "76,357 x 0.20"
  - printed: "35"
    value: "15680.00"
    work: "Sch D line 19 > 0; smaller of 19,848 and 15,680"
  - printed: "36"
    value: "392120.00"
    work: "339,848 + 52,272"
  - printed: "37"
    value: "376357.00"
    work: "amount from line 1"
  - printed: "38"
    value: "15763.00"
    work: "392,120 - 376,357"
  - printed: "39"
    value: "0.00"
    work: "15,680 - 15,763 < 0, so -0-"
  - printed: "40"
    value: "0.00"
    work: "0 x 0.25"
  - printed: "41"
    value: "376357.00"
    work: "Sch D line 18 > 0; 52,272 + 0 + 247,728 + 76,357 + 0"
  - printed: "42"
    value: "0.00"
    work: "376,357 - 376,357"
  - printed: "43"
    value: "0.00"
    work: "0 x 0.28"
  - printed: "45"
    value: "58845.60"
    work: "37,159.20 + 15,271.40 + 0 + 0 + 6,415.00"
  - printed: "47"
    value: "58845.60"
    work: "smaller of 58,845.60 and 101,283.34"
```

### classm.sdtw.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "365573.00"
    work: "Form 1040 line 15"
  - printed: "2"
    value: "0.00"
    work: "Form 1040 line 3a"
  - printed: "3"
    value: "0.00"
    work: "Form 4952 line 4g"
  - printed: "4"
    value: "45.00"
    work: "Form 4952 line 4e"
  - printed: "5"
    value: "0.00"
    work: "0 - 45 = -45; zero or less, enter 0"
  - printed: "6"
    value: "0.00"
    work: "0 - 0 = 0"
  - printed: "7"
    value: "45.00"
    work: "smaller of 45 (Sch D line 15) or 45 (Sch D line 16)"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0 (line 3) or 45 (line 4)"
  - printed: "9"
    value: "45.00"
    work: "45 - 0"
  - printed: "10"
    value: "45.00"
    work: "0 + 45"
  - printed: "11"
    value: "31.00"
    work: "19 (Sch D line 18) + 12 (Sch D line 19)"
  - printed: "12"
    value: "31.00"
    work: "smaller of 45 (line 9) or 31 (line 11)"
  - printed: "13"
    value: "14.00"
    work: "45 - 31"
  - printed: "14"
    value: "365559.00"
    work: "365573 - 14"
  - printed: "15"
    value: "48350.00"
    work: "married filing separately"
  - printed: "16"
    value: "48350.00"
    work: "smaller of 365573 (line 1) or 48350 (line 15)"
  - printed: "17"
    value: "48350.00"
    work: "smaller of 365559 (line 14) or 48350 (line 16)"
  - printed: "18"
    value: "365528.00"
    work: "365573 - 45"
  - printed: "19"
    value: "197300.00"
    work: "smaller of 365573 or 197300 (MFS)"
  - printed: "20"
    value: "197300.00"
    work: "smaller of 365559 (line 14) or 197300 (line 19)"
  - printed: "21"
    value: "365528.00"
    work: "larger of 365528 (line 18) or 197300 (line 20)"
  - printed: "22"
    value: "0.00"
    work: "48350 - 48350; lines 1 and 16 differ, so continue to line 23"
  - printed: "23"
    value: "14.00"
    work: "smaller of 365573 (line 1) or 14 (line 13)"
  - printed: "24"
    value: "0.00"
    work: "from line 22"
  - printed: "25"
    value: "14.00"
    work: "14 - 0"
  - printed: "26"
    value: "300000.00"
    work: "married filing separately"
  - printed: "27"
    value: "300000.00"
    work: "smaller of 365573 (line 1) or 300000 (line 26)"
  - printed: "28"
    value: "365528.00"
    work: "365528 + 0"
  - printed: "29"
    value: "0.00"
    work: "300000 - 365528 is negative; enter 0"
  - printed: "30"
    value: "0.00"
    work: "smaller of 14 (line 25) or 0 (line 29)"
  - printed: "31"
    value: "0.00"
    work: "0 x 0.15"
  - printed: "32"
    value: "0.00"
    work: "0 + 0; lines 1 and 32 differ, so continue to line 33"
  - printed: "33"
    value: "14.00"
    work: "14 - 0"
  - printed: "34"
    value: "2.80"
    work: "14 x 0.20"
  - printed: "35"
    value: "12.00"
    work: "Sch D line 19 is not zero; smaller of 45 (line 9) or 12 (Sch D line 19)"
  - printed: "36"
    value: "365573.00"
    work: "45 + 365528"
  - printed: "37"
    value: "365573.00"
    work: "from line 1"
  - printed: "38"
    value: "0.00"
    work: "365573 - 365573 = 0"
  - printed: "39"
    value: "12.00"
    work: "12 - 0"
  - printed: "40"
    value: "3.00"
    work: "12 x 0.25"
  - printed: "41"
    value: "365554.00"
    work: "Sch D line 18 is not zero; 365528 + 0 + 0 + 14 + 12"
  - printed: "42"
    value: "19.00"
    work: "365573 - 365554"
  - printed: "43"
    value: "5.32"
    work: "19 x 0.28"
  - printed: "45"
    value: "97493.17"
    work: "0 + 2.80 + 3.00 + 5.32 + 97482.05"
  - printed: "47"
    value: "97493.17"
    work: "smaller of 97493.17 (line 45) or 97497.80 (line 46)"
```
```
