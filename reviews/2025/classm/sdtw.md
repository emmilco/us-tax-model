# Class M hand-work — sdtw

`Schedule D Tax Worksheet` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-07 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 1312cadd960c541c16fb0f9501f7da73ddd5d3d479e5438ef32d43716d50cbbf |
| cases | 4 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | - | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.sdtw.1 — prompt sha256 2f3878d374961c81843e71c9f1471228fb2b5391967bf43f4c43ec8641684ea8; branches: sdtw.after22:false, sdtw.after32:false, sdtw.use1250:false, sdtw.use28:false, sdtw.line4#0, sdtw.line5:floor, sdtw.line6:floor, sdtw.line7:left, sdtw.line8:left, sdtw.line9:floor, sdtw.line12:left, sdtw.line14:floor, sdtw.line16:left, sdtw.line17:left, sdtw.line18:floor, sdtw.line19:left, sdtw.line20:left, sdtw.line21:left, sdtw.raw23:left, sdtw.line23#1, sdtw.line24#1, sdtw.raw25:floor, sdtw.line25#1, sdtw.line26#1, sdtw.raw27:left, sdtw.line27#1, sdtw.line28#1, sdtw.raw29:floor, sdtw.line29#1, sdtw.raw30:left, sdtw.line30#1, sdtw.line31#1, sdtw.line32#1, sdtw.line33#1, sdtw.line34#1, sdtw.raw35:left, sdtw.line35#1, sdtw.line36#1, sdtw.line37#1, sdtw.raw38:floor, sdtw.line38#1, sdtw.raw39:floor, sdtw.line39#1, sdtw.line40#1, sdtw.show41_43:false, sdtw.line41#1, sdtw.line42#1, sdtw.line43#1, sdtw.line47:left

### classm.sdtw.1 — 1 — Taxable income
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 2 — Qualified dividends
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $64,750.00

### classm.sdtw.1 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 23 — Smaller of lines 1 and 13
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 24 — Amount from line 22
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 25 — Subtract line 24 from line 23; floor at zero
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 26 — 15-percent ceiling by filing status
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 27 — Smaller of lines 1 and 26
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 28 — Add lines 21 and 22
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 29 — Subtract line 28 from line 27; floor at zero
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 30 — Smaller of lines 25 and 29
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 31 — Multiply line 30 by 15 percent
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 32 — Add lines 24 and 30
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 33 — Subtract line 32 from line 23
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 34 — Multiply line 33 by 20 percent
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 35 — Smaller of line 9 and Schedule D line 19
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 36 — Add lines 10 and 21
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 37 — Amount from line 1
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 38 — Subtract line 37 from line 36; floor at zero
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 39 — Subtract line 38 from line 35; floor at zero
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 40 — Multiply line 39 by 25 percent
Status: **SKIPPED**

Model: blank
Work: skipped (line 1 = line 16)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $0.00

### case classm.sdtw.2 — prompt sha256 f6b4ae546ce8e410cb5ba6616d403716ed8955de65dd908f6f0eabdc25873ae9; branches: sdtw.after22:true, sdtw.after32:true, sdtw.use1250:true, sdtw.use28:true, sdtw.line4#1, sdtw.line5:floor, sdtw.line6:positive, sdtw.line7:left, sdtw.line8:left, sdtw.line9:positive, sdtw.line12:right, sdtw.line14:positive, sdtw.line16:right, sdtw.line17:right, sdtw.line18:positive, sdtw.line19:right, sdtw.line20:right, sdtw.line21:left, sdtw.raw23:right, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:left, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:positive, sdtw.line29#0, sdtw.raw30:left, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#0, sdtw.line34#0, sdtw.raw35:right, sdtw.line35#0, sdtw.line36#0, sdtw.line37#0, sdtw.raw38:floor, sdtw.line38#0, sdtw.raw39:positive, sdtw.line39#0, sdtw.line40#0, sdtw.show41_43:true, sdtw.line41#0, sdtw.line42#0, sdtw.line43#0, sdtw.line47:left

### classm.sdtw.2 — 1 — Taxable income
Status: **AGREE**

Value: $389,726.20

### classm.sdtw.2 — 2 — Qualified dividends
Status: **AGREE**

Value: $962.00

### classm.sdtw.2 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $962.00

### classm.sdtw.2 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $4,127.00

### classm.sdtw.2 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $4,127.00

### classm.sdtw.2 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $5,089.00

### classm.sdtw.2 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $4,041.00

### classm.sdtw.2 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $4,041.00

### classm.sdtw.2 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $1,048.00

### classm.sdtw.2 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $388,678.20

### classm.sdtw.2 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.2 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.2 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.2 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $384,637.20

### classm.sdtw.2 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.2 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.2 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $384,637.20

### classm.sdtw.2 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $1,048.00

### classm.sdtw.2 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $1,048.00

### classm.sdtw.2 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $533,400.00

### classm.sdtw.2 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $389,726.20

### classm.sdtw.2 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $384,637.20

### classm.sdtw.2 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $5,089.00

### classm.sdtw.2 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $1,048.00

### classm.sdtw.2 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $157.20

### classm.sdtw.2 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $1,048.00

### classm.sdtw.2 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 35 — Smaller of line 9 and Schedule D line 19
Status: **AGREE**

Value: $3,054.00

### classm.sdtw.2 — 36 — Add lines 10 and 21
Status: **AGREE**

Value: $389,726.20

### classm.sdtw.2 — 37 — Amount from line 1
Status: **AGREE**

Value: $389,726.20

### classm.sdtw.2 — 38 — Subtract line 37 from line 36; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

Value: $3,054.00

### classm.sdtw.2 — 40 — Multiply line 39 by 25 percent
Status: **AGREE**

Value: $763.50

### classm.sdtw.2 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **AGREE**

Value: $388,739.20

### classm.sdtw.2 — 42 — Subtract line 41 from line 1
Status: **AGREE**

Value: $987.00

### classm.sdtw.2 — 43 — Multiply line 42 by 28 percent
Status: **AGREE**

Value: $276.36

### classm.sdtw.2 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $105,367.33

### classm.sdtw.2 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $105,367.33

### case classm.sdtw.3 — prompt sha256 7a168507b0a5b7087bc0702fb8cf3a03bf5653d6405fea7b2d523c9772c2e89e; branches: sdtw.after22:true, sdtw.after32:true, sdtw.use1250:true, sdtw.use28:false, sdtw.line4#0, sdtw.line5:floor, sdtw.line6:positive, sdtw.line7:left, sdtw.line8:left, sdtw.line9:positive, sdtw.line12:right, sdtw.line14:positive, sdtw.line16:right, sdtw.line17:right, sdtw.line18:positive, sdtw.line19:right, sdtw.line20:left, sdtw.line21:right, sdtw.raw23:right, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:right, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:positive, sdtw.line29#0, sdtw.raw30:right, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#0, sdtw.line34#0, sdtw.raw35:right, sdtw.line35#0, sdtw.line36#0, sdtw.line37#0, sdtw.raw38:positive, sdtw.line38#0, sdtw.raw39:floor, sdtw.line39#0, sdtw.line40#0, sdtw.show41_43:false, sdtw.line41#1, sdtw.line42#1, sdtw.line43#1, sdtw.line47:left

### classm.sdtw.3 — 1 — Taxable income
Status: **AGREE**

Value: $303,525.00

### classm.sdtw.3 — 2 — Qualified dividends
Status: **AGREE**

Value: $200,000.00

### classm.sdtw.3 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form
Status: **AGREE**

Value: $52,198.00

### classm.sdtw.3 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $200,000.00

### classm.sdtw.3 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $52,198.00

### classm.sdtw.3 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $52,198.00

### classm.sdtw.3 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $252,198.00

### classm.sdtw.3 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $10,700.00

### classm.sdtw.3 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $10,700.00

### classm.sdtw.3 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $241,498.00

### classm.sdtw.3 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $62,027.00

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

Value: $51,327.00

### classm.sdtw.3 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.3 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $62,027.00

### classm.sdtw.3 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $62,027.00

### classm.sdtw.3 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $241,498.00

### classm.sdtw.3 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $241,498.00

### classm.sdtw.3 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $300,000.00

### classm.sdtw.3 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $300,000.00

### classm.sdtw.3 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $62,027.00

### classm.sdtw.3 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $237,973.00

### classm.sdtw.3 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $237,973.00

### classm.sdtw.3 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $35,695.95

### classm.sdtw.3 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $237,973.00

### classm.sdtw.3 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $3,525.00

### classm.sdtw.3 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $705.00

### classm.sdtw.3 — 35 — Smaller of line 9 and Schedule D line 19
Status: **AGREE**

Value: $10,700.00

### classm.sdtw.3 — 36 — Add lines 10 and 21
Status: **AGREE**

Value: $314,225.00

### classm.sdtw.3 — 37 — Amount from line 1
Status: **AGREE**

Value: $303,525.00

### classm.sdtw.3 — 38 — Subtract line 37 from line 36; floor at zero
Status: **AGREE**

Value: $10,700.00

### classm.sdtw.3 — 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 40 — Multiply line 39 by 25 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $44,960.95

### classm.sdtw.3 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $44,960.95

### case classm.sdtw.4 — prompt sha256 d5c3b2007e7485589e815d6fc4aeeece13d939f9555aaa76227c7e966dd28232; branches: sdtw.after22:true, sdtw.after32:false, sdtw.use1250:false, sdtw.use28:false, sdtw.line4#0, sdtw.line5:positive, sdtw.line6:positive, sdtw.line7:right, sdtw.line8:right, sdtw.line9:floor, sdtw.line12:left, sdtw.line14:floor, sdtw.line16:right, sdtw.line17:left, sdtw.line18:floor, sdtw.line19:left, sdtw.line20:left, sdtw.line21:left, sdtw.raw23:left, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:left, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:positive, sdtw.line29#0, sdtw.raw30:left, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#1, sdtw.line34#1, sdtw.raw35:left, sdtw.line35#1, sdtw.line36#1, sdtw.line37#1, sdtw.raw38:floor, sdtw.line38#1, sdtw.raw39:floor, sdtw.line39#1, sdtw.line40#1, sdtw.show41_43:false, sdtw.line41#1, sdtw.line42#1, sdtw.line43#1, sdtw.line47:left

### classm.sdtw.4 — 1 — Taxable income
Status: **AGREE**

Value: $91,213.55

### classm.sdtw.4 — 2 — Qualified dividends
Status: **AGREE**

Value: $143,278.00

### classm.sdtw.4 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $6,530.00

### classm.sdtw.4 — 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form
Status: **AGREE**

Value: $516.00

### classm.sdtw.4 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $6,014.00

### classm.sdtw.4 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $137,264.00

### classm.sdtw.4 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $516.00

### classm.sdtw.4 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $516.00

### classm.sdtw.4 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $137,264.00

### classm.sdtw.4 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $137,264.00

### classm.sdtw.4 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.4 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.4 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $91,213.55

### classm.sdtw.4 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $0.00

### classm.sdtw.4 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.4 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $91,213.55

### classm.sdtw.4 — 24 — Amount from line 22
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.4 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $42,863.55

### classm.sdtw.4 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $533,400.00

### classm.sdtw.4 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $91,213.55

### classm.sdtw.4 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.4 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $42,863.55

### classm.sdtw.4 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $42,863.55

### classm.sdtw.4 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $6,429.53

### classm.sdtw.4 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $91,213.55

### classm.sdtw.4 — 33 — Subtract line 32 from line 23
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 34 — Multiply line 33 by 20 percent
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 35 — Smaller of line 9 and Schedule D line 19
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 36 — Add lines 10 and 21
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 37 — Amount from line 1
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 38 — Subtract line 37 from line 36; floor at zero
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 39 — Subtract line 38 from line 35; floor at zero
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 40 — Multiply line 39 by 25 percent
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $6,429.53

### classm.sdtw.4 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $6,429.53

## Raw responses

### classm.sdtw.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Form 1040 line 15 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "Form 1040 line 3a = 0.00"
  - printed: "3"
    value: "0.00"
    work: "Form 4952 line 4g = 0.00"
  - printed: "4"
    value: "0.00"
    work: "Form 4952 line 4e = 0.00 (Form 4952 filed)"
  - printed: "5"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "6"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "7"
    value: "0.00"
    work: "smaller of Sch D line 15 (0.00) or line 16 (0.00) = 0.00"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0.00 or 0.00 = 0.00"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "10"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "11"
    value: "0.00"
    work: "Sch D line 18 (0.00) + line 19 (0.00) = 0.00"
  - printed: "12"
    value: "0.00"
    work: "smaller of 0.00 or 0.00 = 0.00"
  - printed: "13"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "14"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "15"
    value: "64750.00"
    work: "head of household = 64,750"
  - printed: "16"
    value: "0.00"
    work: "smaller of 0.00 or 64,750 = 0.00"
  - printed: "17"
    value: "0.00"
    work: "smaller of 0.00 or 0.00 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "19"
    value: "0.00"
    work: "smaller of 0.00 or 197,300 (HOH) = 0.00"
  - printed: "20"
    value: "0.00"
    work: "smaller of 0.00 or 0.00 = 0.00"
  - printed: "21"
    value: "0.00"
    work: "larger of 0.00 or 0.00 = 0.00"
  - printed: "22"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00; lines 1 and 16 are the same, so skip lines 23-43"
  - printed: "23"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "24"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "25"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "26"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "27"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "28"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "29"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "30"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "31"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "32"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "33"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "34"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "35"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "36"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "37"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "38"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "39"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "40"
    value: "blank"
    work: "skipped (line 1 = line 16)"
  - printed: "45"
    value: "0.00"
    work: "lines 31, 34, 40, 43 blank + line 44 (0.00) = 0.00"
  - printed: "47"
    value: "0.00"
    work: "smaller of line 45 (0.00) or line 46 (0.00) = 0.00"
```
```

### classm.sdtw.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "389726.20"
    work: "Form 1040 line 15 taxable income"
  - printed: "2"
    value: "962.00"
    work: "Form 1040 line 3a qualified dividends"
  - printed: "3"
    value: "0.00"
    work: "Form 4952 line 4g supplied as 0.00 (no Form 4952 filed)"
  - printed: "4"
    value: "0.00"
    work: "No Form 4952 filed, so 0"
  - printed: "5"
    value: "0.00"
    work: "0.00 - 0.00 = 0, floor 0"
  - printed: "6"
    value: "962.00"
    work: "962.00 - 0.00 = 962.00"
  - printed: "7"
    value: "4127.00"
    work: "smaller of 4,127.00 and 56,589.00"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0.00 and 0.00"
  - printed: "9"
    value: "4127.00"
    work: "4,127.00 - 0.00"
  - printed: "10"
    value: "5089.00"
    work: "962.00 + 4,127.00"
  - printed: "11"
    value: "4041.00"
    work: "987.00 + 3,054.00"
  - printed: "12"
    value: "4041.00"
    work: "smaller of 4,127.00 and 4,041.00"
  - printed: "13"
    value: "1048.00"
    work: "5,089.00 - 4,041.00"
  - printed: "14"
    value: "388678.20"
    work: "389,726.20 - 1,048.00"
  - printed: "15"
    value: "48350.00"
    work: "Single: $48,350"
  - printed: "16"
    value: "48350.00"
    work: "smaller of 389,726.20 and 48,350.00"
  - printed: "17"
    value: "48350.00"
    work: "smaller of 388,678.20 and 48,350.00"
  - printed: "18"
    value: "384637.20"
    work: "389,726.20 - 5,089.00"
  - printed: "19"
    value: "197300.00"
    work: "smaller of 389,726.20 and 197,300 (single)"
  - printed: "20"
    value: "197300.00"
    work: "smaller of 388,678.20 and 197,300.00"
  - printed: "21"
    value: "384637.20"
    work: "larger of 384,637.20 and 197,300.00"
  - printed: "22"
    value: "0.00"
    work: "48,350.00 - 48,350.00; lines 1 and 16 differ, so go to line 23"
  - printed: "23"
    value: "1048.00"
    work: "smaller of 389,726.20 and 1,048.00"
  - printed: "24"
    value: "0.00"
    work: "amount from line 22"
  - printed: "25"
    value: "1048.00"
    work: "1,048.00 - 0.00"
  - printed: "26"
    value: "533400.00"
    work: "Single: $533,400"
  - printed: "27"
    value: "389726.20"
    work: "smaller of 389,726.20 and 533,400.00"
  - printed: "28"
    value: "384637.20"
    work: "384,637.20 + 0.00"
  - printed: "29"
    value: "5089.00"
    work: "389,726.20 - 384,637.20"
  - printed: "30"
    value: "1048.00"
    work: "smaller of 1,048.00 and 5,089.00"
  - printed: "31"
    value: "157.20"
    work: "1,048.00 x 0.15"
  - printed: "32"
    value: "1048.00"
    work: "0.00 + 1,048.00; not equal to line 1, so go to line 33"
  - printed: "33"
    value: "0.00"
    work: "1,048.00 - 1,048.00"
  - printed: "34"
    value: "0.00"
    work: "0.00 x 0.20"
  - printed: "35"
    value: "3054.00"
    work: "Sch D line 19 is nonzero; smaller of 4,127.00 and 3,054.00"
  - printed: "36"
    value: "389726.20"
    work: "5,089.00 + 384,637.20"
  - printed: "37"
    value: "389726.20"
    work: "amount from line 1"
  - printed: "38"
    value: "0.00"
    work: "389,726.20 - 389,726.20 = 0, floor 0"
  - printed: "39"
    value: "3054.00"
    work: "3,054.00 - 0.00"
  - printed: "40"
    value: "763.50"
    work: "3,054.00 x 0.25"
  - printed: "41"
    value: "388739.20"
    work: "Sch D line 18 is nonzero; 384,637.20 + 0.00 + 1,048.00 + 0.00 + 3,054.00"
  - printed: "42"
    value: "987.00"
    work: "389,726.20 - 388,739.20"
  - printed: "43"
    value: "276.36"
    work: "987.00 x 0.28"
  - printed: "45"
    value: "105367.33"
    work: "157.20 + 0.00 + 763.50 + 276.36 + 104,170.27"
  - printed: "47"
    value: "105367.33"
    work: "smaller of 105,367.33 and 105,951.42"
```
```

### classm.sdtw.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "303525.00"
    work: "Form 1040 line 15 = 303,525.00"
  - printed: "2"
    value: "200000.00"
    work: "Form 1040 line 3a qualified dividends = 200,000.00"
  - printed: "3"
    value: "0.00"
    work: "Form 4952 line 4g = 0.00"
  - printed: "4"
    value: "52198.00"
    work: "Form 4952 line 4e = 52,198.00"
  - printed: "5"
    value: "0.00"
    work: "0 - 52,198 < 0, enter -0-"
  - printed: "6"
    value: "200000.00"
    work: "200,000 - 0 = 200,000"
  - printed: "7"
    value: "52198.00"
    work: "smaller of 52,198 (Sch D 15) or 155,295 (Sch D 16)"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0 or 52,198"
  - printed: "9"
    value: "52198.00"
    work: "52,198 - 0 = 52,198"
  - printed: "10"
    value: "252198.00"
    work: "200,000 + 52,198"
  - printed: "11"
    value: "10700.00"
    work: "0 + 10,700"
  - printed: "12"
    value: "10700.00"
    work: "smaller of 52,198 or 10,700"
  - printed: "13"
    value: "241498.00"
    work: "252,198 - 10,700"
  - printed: "14"
    value: "62027.00"
    work: "303,525 - 241,498"
  - printed: "15"
    value: "48350.00"
    work: "married filing separately: 48,350"
  - printed: "16"
    value: "48350.00"
    work: "smaller of 303,525 or 48,350"
  - printed: "17"
    value: "48350.00"
    work: "smaller of 62,027 or 48,350"
  - printed: "18"
    value: "51327.00"
    work: "303,525 - 252,198"
  - printed: "19"
    value: "197300.00"
    work: "smaller of 303,525 or 197,300 (MFS)"
  - printed: "20"
    value: "62027.00"
    work: "smaller of 62,027 or 197,300"
  - printed: "21"
    value: "62027.00"
    work: "larger of 51,327 or 62,027"
  - printed: "22"
    value: "0.00"
    work: "48,350 - 48,350 = 0; lines 1 and 16 differ, continue to line 23"
  - printed: "23"
    value: "241498.00"
    work: "smaller of 303,525 or 241,498"
  - printed: "24"
    value: "0.00"
    work: "line 22 = 0"
  - printed: "25"
    value: "241498.00"
    work: "241,498 - 0"
  - printed: "26"
    value: "300000.00"
    work: "married filing separately: 300,000"
  - printed: "27"
    value: "300000.00"
    work: "smaller of 303,525 or 300,000"
  - printed: "28"
    value: "62027.00"
    work: "62,027 + 0"
  - printed: "29"
    value: "237973.00"
    work: "300,000 - 62,027"
  - printed: "30"
    value: "237973.00"
    work: "smaller of 241,498 or 237,973"
  - printed: "31"
    value: "35695.95"
    work: "237,973 x 0.15"
  - printed: "32"
    value: "237973.00"
    work: "0 + 237,973; lines 1 and 32 differ, continue to line 33"
  - printed: "33"
    value: "3525.00"
    work: "241,498 - 237,973"
  - printed: "34"
    value: "705.00"
    work: "3,525 x 0.20; Sch D line 19 > 0, continue to line 35"
  - printed: "35"
    value: "10700.00"
    work: "smaller of 52,198 or 10,700"
  - printed: "36"
    value: "314225.00"
    work: "252,198 + 62,027"
  - printed: "37"
    value: "303525.00"
    work: "line 1"
  - printed: "38"
    value: "10700.00"
    work: "314,225 - 303,525"
  - printed: "39"
    value: "0.00"
    work: "10,700 - 10,700 = 0"
  - printed: "40"
    value: "0.00"
    work: "0 x 0.25; Sch D line 18 = 0, skip lines 41-43"
  - printed: "45"
    value: "44960.95"
    work: "35,695.95 + 705 + 0 + 0 (line 43 skipped) + 8,560"
  - printed: "47"
    value: "44960.95"
    work: "smaller of 44,960.95 or 75,781"
```
```

### classm.sdtw.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "91213.55"
    work: "Form 1040 line 15"
  - printed: "2"
    value: "143278.00"
    work: "Form 1040 line 3a qualified dividends"
  - printed: "3"
    value: "6530.00"
    work: "Form 4952 line 4g"
  - printed: "4"
    value: "516.00"
    work: "Form 4952 line 4e"
  - printed: "5"
    value: "6014.00"
    work: "6530.00 - 516.00 = 6014.00"
  - printed: "6"
    value: "137264.00"
    work: "143278.00 - 6014.00 = 137264.00"
  - printed: "7"
    value: "516.00"
    work: "smaller of 16368.00 or 516.00"
  - printed: "8"
    value: "516.00"
    work: "smaller of 6530.00 or 516.00"
  - printed: "9"
    value: "0.00"
    work: "516.00 - 516.00 = 0"
  - printed: "10"
    value: "137264.00"
    work: "137264.00 + 0.00"
  - printed: "11"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "12"
    value: "0.00"
    work: "smaller of 0.00 or 0.00"
  - printed: "13"
    value: "137264.00"
    work: "137264.00 - 0.00"
  - printed: "14"
    value: "0.00"
    work: "91213.55 - 137264.00 < 0, enter -0-"
  - printed: "15"
    value: "48350.00"
    work: "Single"
  - printed: "16"
    value: "48350.00"
    work: "smaller of 91213.55 or 48350.00"
  - printed: "17"
    value: "0.00"
    work: "smaller of 0.00 or 48350.00"
  - printed: "18"
    value: "0.00"
    work: "91213.55 - 137264.00 < 0, enter -0-"
  - printed: "19"
    value: "91213.55"
    work: "smaller of 91213.55 or 197300.00"
  - printed: "20"
    value: "0.00"
    work: "smaller of 0.00 or 91213.55"
  - printed: "21"
    value: "0.00"
    work: "larger of 0.00 or 0.00"
  - printed: "22"
    value: "48350.00"
    work: "48350.00 - 0.00; lines 1 and 16 differ, go to line 23"
  - printed: "23"
    value: "91213.55"
    work: "smaller of 91213.55 or 137264.00"
  - printed: "24"
    value: "48350.00"
    work: "line 22"
  - printed: "25"
    value: "42863.55"
    work: "91213.55 - 48350.00"
  - printed: "26"
    value: "533400.00"
    work: "Single"
  - printed: "27"
    value: "91213.55"
    work: "smaller of 91213.55 or 533400.00"
  - printed: "28"
    value: "48350.00"
    work: "0.00 + 48350.00"
  - printed: "29"
    value: "42863.55"
    work: "91213.55 - 48350.00"
  - printed: "30"
    value: "42863.55"
    work: "smaller of 42863.55 or 42863.55"
  - printed: "31"
    value: "6429.53"
    work: "42863.55 x 0.15 = 6429.5325"
  - printed: "32"
    value: "91213.55"
    work: "48350.00 + 42863.55; equals line 1, skip lines 33-43"
  - printed: "33"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "34"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "35"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "36"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "37"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "38"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "39"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "40"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "45"
    value: "6429.53"
    work: "6429.53 + 0 + 0 + 0 + 0.00"
  - printed: "47"
    value: "6429.53"
    work: "smaller of 6429.53 or 14984.00"
```
```
