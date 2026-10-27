# Class M hand-work — sdtw

`Schedule D Tax Worksheet` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 02fe0791ccd0e38d870efcef5e8ba34a34cb267aade4c89fe4becd1baf85da5d |
| cases | 5 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | - | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.sdtw.1 — prompt sha256 bf5b9751e93394c50fc420f86867d83060235bf4c93f0093c41bd52b89b5a7c1; branches: sdtw.after22:true, sdtw.after32:true, sdtw.use1250:false, sdtw.use28:true, sdtw.line4#0, sdtw.line5:floor, sdtw.line6:floor, sdtw.line7:left, sdtw.line8:left, sdtw.line9:floor, sdtw.line12:left, sdtw.line14:positive, sdtw.line16:right, sdtw.line17:right, sdtw.line18:positive, sdtw.line19:left, sdtw.line20:left, sdtw.line21:left, sdtw.raw23:right, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:floor, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:left, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:floor, sdtw.line29#0, sdtw.raw30:left, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#0, sdtw.line34#0, sdtw.raw35:left, sdtw.line35#1, sdtw.line36#1, sdtw.line37#1, sdtw.raw38:floor, sdtw.line38#1, sdtw.raw39:floor, sdtw.line39#1, sdtw.line40#1, sdtw.show41_43:false, sdtw.line41#0, sdtw.line42#0, sdtw.line43#0, sdtw.line47:left

### classm.sdtw.1 — 1 — Taxable income
Status: **AGREE**

Value: $89,629.10

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

Value: $89,629.10

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

Value: $89,629.10

### classm.sdtw.1 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $89,629.10

### classm.sdtw.1 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $89,629.10

### classm.sdtw.1 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $89,629.10

### classm.sdtw.1 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $566,700.00

### classm.sdtw.1 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $89,629.10

### classm.sdtw.1 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $89,629.10

### classm.sdtw.1 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.1 — 35 — Smaller of line 9 and Schedule D line 19
Status: **SKIPPED**

Model: blank
Work: Sch D line 19 is zero; skip lines 35-40

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 36 — Add lines 10 and 21
Status: **SKIPPED**

Model: blank
Work: skipped (Sch D line 19 zero)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 37 — Amount from line 1
Status: **SKIPPED**

Model: blank
Work: skipped (Sch D line 19 zero)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 38 — Subtract line 37 from line 36; floor at zero
Status: **SKIPPED**

Model: blank
Work: skipped (Sch D line 19 zero)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 39 — Subtract line 38 from line 35; floor at zero
Status: **SKIPPED**

Model: blank
Work: skipped (Sch D line 19 zero)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 40 — Multiply line 39 by 25 percent
Status: **SKIPPED**

Model: blank
Work: skipped (Sch D line 19 zero)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **SKIPPED**

Model: blank
Work: Sch D line 18 is zero; skip lines 41-43

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 42 — Subtract line 41 from line 1
Status: **SKIPPED**

Model: blank
Work: skipped (Sch D line 18 zero)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 43 — Multiply line 42 by 28 percent
Status: **SKIPPED**

Model: blank
Work: skipped (Sch D line 18 zero)

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.1 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $12,893.00

### classm.sdtw.1 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $12,893.00

### case classm.sdtw.2 — prompt sha256 f315c9f744f74c70e9accf8e901c1ff071aeb66ce25b674f936866ac42cf7c68; branches: sdtw.after22:false, sdtw.after32:false, sdtw.use1250:false, sdtw.use28:false, sdtw.line4#1, sdtw.line5:floor, sdtw.line6:positive, sdtw.line7:left, sdtw.line8:left, sdtw.line9:positive, sdtw.line12:right, sdtw.line14:floor, sdtw.line16:left, sdtw.line17:left, sdtw.line18:floor, sdtw.line19:left, sdtw.line20:left, sdtw.line21:left, sdtw.raw23:left, sdtw.line23#1, sdtw.line24#1, sdtw.raw25:floor, sdtw.line25#1, sdtw.line26#1, sdtw.raw27:right, sdtw.line27#1, sdtw.line28#1, sdtw.raw29:floor, sdtw.line29#1, sdtw.raw30:left, sdtw.line30#1, sdtw.line31#1, sdtw.line32#1, sdtw.line33#1, sdtw.line34#1, sdtw.raw35:right, sdtw.line35#1, sdtw.line36#1, sdtw.line37#1, sdtw.raw38:floor, sdtw.line38#1, sdtw.raw39:floor, sdtw.line39#1, sdtw.line40#1, sdtw.show41_43:true, sdtw.line41#1, sdtw.line42#1, sdtw.line43#1, sdtw.line47:left

### classm.sdtw.2 — 1 — Taxable income
Status: **AGREE**

Value: $10,429.58

### classm.sdtw.2 — 2 — Qualified dividends
Status: **AGREE**

Value: $44,516.00

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

Value: $44,516.00

### classm.sdtw.2 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $10,302.00

### classm.sdtw.2 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $10,302.00

### classm.sdtw.2 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $54,818.00

### classm.sdtw.2 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $927.00

### classm.sdtw.2 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $927.00

### classm.sdtw.2 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $53,891.00

### classm.sdtw.2 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $96,700.00

### classm.sdtw.2 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $10,429.58

### classm.sdtw.2 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $10,429.58

### classm.sdtw.2 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $10,429.58

### classm.sdtw.2 — 23 — Smaller of lines 1 and 13
Status: **SKIPPED**

Model: blank
Work: Lines 1 and 16 are the same, so skip lines 23-43

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 24 — Amount from line 22
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 25 — Subtract line 24 from line 23; floor at zero
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 26 — 15-percent ceiling by filing status
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 27 — Smaller of lines 1 and 26
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 28 — Add lines 21 and 22
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 29 — Subtract line 28 from line 27; floor at zero
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 30 — Smaller of lines 25 and 29
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 31 — Multiply line 30 by 15 percent
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 32 — Add lines 24 and 30
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 33 — Subtract line 32 from line 23
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 34 — Multiply line 33 by 20 percent
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 35 — Smaller of line 9 and Schedule D line 19
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 36 — Add lines 10 and 21
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 37 — Amount from line 1
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 38 — Subtract line 37 from line 36; floor at zero
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 39 — Subtract line 38 from line 35; floor at zero
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 40 — Multiply line 39 by 25 percent
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 42 — Subtract line 41 from line 1
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 43 — Multiply line 42 by 28 percent
Status: **SKIPPED**

Model: blank
Work: Skipped per line 22 instruction

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.2 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $0.00

### classm.sdtw.2 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $0.00

### case classm.sdtw.3 — prompt sha256 a222d33c9e47db352cf0a312cc010c98843b8c667fe80a4ac1dd6110a1fcf866; branches: sdtw.after22:true, sdtw.after32:true, sdtw.use1250:true, sdtw.use28:false, sdtw.line4#1, sdtw.line5:floor, sdtw.line6:positive, sdtw.line7:left, sdtw.line8:left, sdtw.line9:positive, sdtw.line12:right, sdtw.line14:positive, sdtw.line16:right, sdtw.line17:right, sdtw.line18:positive, sdtw.line19:right, sdtw.line20:right, sdtw.line21:left, sdtw.raw23:right, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:right, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:positive, sdtw.line29#0, sdtw.raw30:right, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#0, sdtw.line34#0, sdtw.raw35:right, sdtw.line35#0, sdtw.line36#0, sdtw.line37#0, sdtw.raw38:floor, sdtw.line38#0, sdtw.raw39:positive, sdtw.line39#0, sdtw.line40#0, sdtw.show41_43:false, sdtw.line41#1, sdtw.line42#1, sdtw.line43#1, sdtw.line47:left

### classm.sdtw.3 — 1 — Taxable income
Status: **AGREE**

Value: $317,901.55

### classm.sdtw.3 — 2 — Qualified dividends
Status: **AGREE**

Value: $31,832.00

### classm.sdtw.3 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $31,832.00

### classm.sdtw.3 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $3,303.00

### classm.sdtw.3 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $3,303.00

### classm.sdtw.3 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $35,135.00

### classm.sdtw.3 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $132.00

### classm.sdtw.3 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $132.00

### classm.sdtw.3 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $35,003.00

### classm.sdtw.3 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $282,898.55

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

Value: $282,766.55

### classm.sdtw.3 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.3 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $197,300.00

### classm.sdtw.3 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $282,766.55

### classm.sdtw.3 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $35,003.00

### classm.sdtw.3 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $35,003.00

### classm.sdtw.3 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $300,000.00

### classm.sdtw.3 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $300,000.00

### classm.sdtw.3 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $282,766.55

### classm.sdtw.3 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $17,233.45

### classm.sdtw.3 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $17,233.45

### classm.sdtw.3 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $2,585.02

### classm.sdtw.3 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $17,233.45

### classm.sdtw.3 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $17,769.55

### classm.sdtw.3 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $3,553.91

### classm.sdtw.3 — 35 — Smaller of line 9 and Schedule D line 19
Status: **AGREE**

Value: $132.00

### classm.sdtw.3 — 36 — Add lines 10 and 21
Status: **AGREE**

Value: $317,901.55

### classm.sdtw.3 — 37 — Amount from line 1
Status: **AGREE**

Value: $317,901.55

### classm.sdtw.3 — 38 — Subtract line 37 from line 36; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.3 — 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

Value: $132.00

### classm.sdtw.3 — 40 — Multiply line 39 by 25 percent
Status: **AGREE**

Value: $33.00

### classm.sdtw.3 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **SKIPPED**

Model: blank
Work: Sch D line 18 is zero; skip lines 41-43

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.3 — 42 — Subtract line 41 from line 1
Status: **SKIPPED**

Model: blank
Work: Skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.3 — 43 — Multiply line 42 by 28 percent
Status: **SKIPPED**

Model: blank
Work: Skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.3 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $74,687.47

### classm.sdtw.3 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $74,687.47

### case classm.sdtw.4 — prompt sha256 f6aa2c5b1583f8731a012de7b6bd7239a1327c6b769525449e5089c07079fdf0; branches: sdtw.after22:true, sdtw.after32:false, sdtw.use1250:false, sdtw.use28:false, sdtw.line4#0, sdtw.line5:positive, sdtw.line6:positive, sdtw.line7:right, sdtw.line8:right, sdtw.line9:floor, sdtw.line12:left, sdtw.line14:floor, sdtw.line16:right, sdtw.line17:left, sdtw.line18:floor, sdtw.line19:left, sdtw.line20:left, sdtw.line21:left, sdtw.raw23:left, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:left, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:positive, sdtw.line29#0, sdtw.raw30:left, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#1, sdtw.line34#1, sdtw.raw35:left, sdtw.line35#1, sdtw.line36#1, sdtw.line37#1, sdtw.raw38:floor, sdtw.line38#1, sdtw.raw39:floor, sdtw.line39#1, sdtw.line40#1, sdtw.show41_43:false, sdtw.line41#1, sdtw.line42#1, sdtw.line43#1, sdtw.line47:left

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

### classm.sdtw.4 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 42 — Subtract line 41 from line 1
Status: **SKIPPED**

Model: blank
Work: skipped: lines 1 and 32 are the same

No numeric assertion or class M credit: the model left this line blank.

### classm.sdtw.4 — 43 — Multiply line 42 by 28 percent
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

### case classm.sdtw.5 — prompt sha256 a0c36285c73e198dc220be6def0bb6233d5d348a285a7f1ea037d5a7c4a59a55; branches: sdtw.after22:true, sdtw.after32:true, sdtw.use1250:true, sdtw.use28:true, sdtw.line4#1, sdtw.line5:floor, sdtw.line6:positive, sdtw.line7:left, sdtw.line8:left, sdtw.line9:positive, sdtw.line12:right, sdtw.line14:positive, sdtw.line16:right, sdtw.line17:right, sdtw.line18:positive, sdtw.line19:left, sdtw.line20:left, sdtw.line21:right, sdtw.raw23:right, sdtw.line23#0, sdtw.line24#0, sdtw.raw25:positive, sdtw.line25#0, sdtw.line26#0, sdtw.raw27:left, sdtw.line27#0, sdtw.line28#0, sdtw.raw29:positive, sdtw.line29#0, sdtw.raw30:left, sdtw.line30#0, sdtw.line31#0, sdtw.line32#0, sdtw.line33#0, sdtw.line34#0, sdtw.raw35:right, sdtw.line35#0, sdtw.line36#0, sdtw.line37#0, sdtw.raw38:positive, sdtw.line38#0, sdtw.raw39:floor, sdtw.line39#0, sdtw.line40#0, sdtw.show41_43:true, sdtw.line41#0, sdtw.line42#0, sdtw.line43#0, sdtw.line47:left

### classm.sdtw.5 — 1 — Taxable income
Status: **AGREE**

Value: $80,691.75

### classm.sdtw.5 — 2 — Qualified dividends
Status: **AGREE**

Value: $2,979.00

### classm.sdtw.5 — 3 — Form 4952 line 4g election
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

Value: $2,979.00

### classm.sdtw.5 — 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

Value: $20,000.00

### classm.sdtw.5 — 8 — Smaller of lines 3 and 4
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

Value: $20,000.00

### classm.sdtw.5 — 10 — Add lines 6 and 9
Status: **AGREE**

Value: $22,979.00

### classm.sdtw.5 — 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

Value: $19,800.00

### classm.sdtw.5 — 12 — Smaller of lines 9 and 11
Status: **AGREE**

Value: $19,800.00

### classm.sdtw.5 — 13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $3,179.00

### classm.sdtw.5 — 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

Value: $77,512.75

### classm.sdtw.5 — 15 — Zero-rate ceiling by filing status
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.5 — 16 — Smaller of lines 1 and 15
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.5 — 17 — Smaller of lines 14 and 16
Status: **AGREE**

Value: $48,350.00

### classm.sdtw.5 — 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

Value: $57,712.75

### classm.sdtw.5 — 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

Value: $80,691.75

### classm.sdtw.5 — 20 — Smaller of lines 14 and 19
Status: **AGREE**

Value: $77,512.75

### classm.sdtw.5 — 21 — Larger of lines 18 and 20
Status: **AGREE**

Value: $77,512.75

### classm.sdtw.5 — 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 23 — Smaller of lines 1 and 13
Status: **AGREE**

Value: $3,179.00

### classm.sdtw.5 — 24 — Amount from line 22
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 25 — Subtract line 24 from line 23; floor at zero
Status: **AGREE**

Value: $3,179.00

### classm.sdtw.5 — 26 — 15-percent ceiling by filing status
Status: **AGREE**

Value: $533,400.00

### classm.sdtw.5 — 27 — Smaller of lines 1 and 26
Status: **AGREE**

Value: $80,691.75

### classm.sdtw.5 — 28 — Add lines 21 and 22
Status: **AGREE**

Value: $77,512.75

### classm.sdtw.5 — 29 — Subtract line 28 from line 27; floor at zero
Status: **AGREE**

Value: $3,179.00

### classm.sdtw.5 — 30 — Smaller of lines 25 and 29
Status: **AGREE**

Value: $3,179.00

### classm.sdtw.5 — 31 — Multiply line 30 by 15 percent
Status: **AGREE**

Value: $476.85

### classm.sdtw.5 — 32 — Add lines 24 and 30
Status: **AGREE**

Value: $3,179.00

### classm.sdtw.5 — 33 — Subtract line 32 from line 23
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 34 — Multiply line 33 by 20 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 35 — Smaller of line 9 and Schedule D line 19
Status: **AGREE**

Value: $16,000.00

### classm.sdtw.5 — 36 — Add lines 10 and 21
Status: **AGREE**

Value: $100,491.75

### classm.sdtw.5 — 37 — Amount from line 1
Status: **AGREE**

Value: $80,691.75

### classm.sdtw.5 — 38 — Subtract line 37 from line 36; floor at zero
Status: **AGREE**

Value: $19,800.00

### classm.sdtw.5 — 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 40 — Multiply line 39 by 25 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 41 — Add lines 21, 22, 30, 33 and 39
Status: **AGREE**

Value: $80,691.75

### classm.sdtw.5 — 42 — Subtract line 41 from line 1
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 43 — Multiply line 42 by 28 percent
Status: **AGREE**

Value: $0.00

### classm.sdtw.5 — 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

Value: $12,446.85

### classm.sdtw.5 — 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

Value: $12,446.85

## Raw responses

### classm.sdtw.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "89629.10"
    work: "Form 1040 line 15 taxable income"
  - printed: "2"
    value: "0.00"
    work: "Form 1040 line 3a qualified dividends"
  - printed: "3"
    value: "0.00"
    work: "Form 4952 line 4g"
  - printed: "4"
    value: "0.00"
    work: "Form 4952 line 4e"
  - printed: "5"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "6"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "7"
    value: "0.00"
    work: "smaller of Sch D line 15 (0.00) or line 16 (0.00)"
  - printed: "8"
    value: "0.00"
    work: "smaller of line 3 (0.00) or line 4 (0.00)"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "10"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "11"
    value: "0.00"
    work: "Sch D line 18 (0.00) + line 19 (0.00)"
  - printed: "12"
    value: "0.00"
    work: "smaller of line 9 (0.00) or line 11 (0.00)"
  - printed: "13"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "14"
    value: "89629.10"
    work: "89,629.10 - 0.00"
  - printed: "15"
    value: "64750.00"
    work: "head of household amount"
  - printed: "16"
    value: "64750.00"
    work: "smaller of 89,629.10 or 64,750.00"
  - printed: "17"
    value: "64750.00"
    work: "smaller of 89,629.10 or 64,750.00"
  - printed: "18"
    value: "89629.10"
    work: "89,629.10 - 0.00"
  - printed: "19"
    value: "89629.10"
    work: "smaller of 89,629.10 or 197,300.00 (head of household)"
  - printed: "20"
    value: "89629.10"
    work: "smaller of 89,629.10 or 89,629.10"
  - printed: "21"
    value: "89629.10"
    work: "larger of 89,629.10 or 89,629.10"
  - printed: "22"
    value: "0.00"
    work: "64,750.00 - 64,750.00; lines 1 and 16 differ, so go to line 23"
  - printed: "23"
    value: "0.00"
    work: "smaller of 89,629.10 or 0.00"
  - printed: "24"
    value: "0.00"
    work: "amount from line 22"
  - printed: "25"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "26"
    value: "566700.00"
    work: "head of household amount"
  - printed: "27"
    value: "89629.10"
    work: "smaller of 89,629.10 or 566,700.00"
  - printed: "28"
    value: "89629.10"
    work: "89,629.10 + 0.00"
  - printed: "29"
    value: "0.00"
    work: "89,629.10 - 89,629.10 = 0.00"
  - printed: "30"
    value: "0.00"
    work: "smaller of 0.00 or 0.00"
  - printed: "31"
    value: "0.00"
    work: "0.00 x 0.15"
  - printed: "32"
    value: "0.00"
    work: "0.00 + 0.00; lines 1 and 32 differ, so go to line 33"
  - printed: "33"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "34"
    value: "0.00"
    work: "0.00 x 0.20"
  - printed: "35"
    value: "blank"
    work: "Sch D line 19 is zero; skip lines 35-40"
  - printed: "36"
    value: "blank"
    work: "skipped (Sch D line 19 zero)"
  - printed: "37"
    value: "blank"
    work: "skipped (Sch D line 19 zero)"
  - printed: "38"
    value: "blank"
    work: "skipped (Sch D line 19 zero)"
  - printed: "39"
    value: "blank"
    work: "skipped (Sch D line 19 zero)"
  - printed: "40"
    value: "blank"
    work: "skipped (Sch D line 19 zero)"
  - printed: "41"
    value: "blank"
    work: "Sch D line 18 is zero; skip lines 41-43"
  - printed: "42"
    value: "blank"
    work: "skipped (Sch D line 18 zero)"
  - printed: "43"
    value: "blank"
    work: "skipped (Sch D line 18 zero)"
  - printed: "45"
    value: "12893.00"
    work: "0.00 + 0.00 + 0 + 0 + 12,893.00"
  - printed: "47"
    value: "12893.00"
    work: "smaller of line 45 (12,893.00) or line 46 (12,893.00)"
```
```

### classm.sdtw.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "10429.58"
    work: "Form 1040 line 15 taxable income"
  - printed: "2"
    value: "44516.00"
    work: "Form 1040 line 3a qualified dividends"
  - printed: "3"
    value: "0.00"
    work: "No Form 4952 filed; line 4g = 0"
  - printed: "4"
    value: "0.00"
    work: "No Form 4952 filed, so enter zero"
  - printed: "5"
    value: "0.00"
    work: "0 - 0 = 0"
  - printed: "6"
    value: "44516.00"
    work: "44516.00 - 0 = 44516.00"
  - printed: "7"
    value: "10302.00"
    work: "smaller of 10302.00 and 10302.00"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0 and 0"
  - printed: "9"
    value: "10302.00"
    work: "10302.00 - 0 = 10302.00"
  - printed: "10"
    value: "54818.00"
    work: "44516.00 + 10302.00"
  - printed: "11"
    value: "927.00"
    work: "927.00 + 0.00"
  - printed: "12"
    value: "927.00"
    work: "smaller of 10302.00 and 927.00"
  - printed: "13"
    value: "53891.00"
    work: "54818.00 - 927.00"
  - printed: "14"
    value: "0.00"
    work: "10429.58 - 53891.00 is less than zero, so enter 0"
  - printed: "15"
    value: "96700.00"
    work: "Qualifying surviving spouse amount"
  - printed: "16"
    value: "10429.58"
    work: "smaller of 10429.58 and 96700.00"
  - printed: "17"
    value: "0.00"
    work: "smaller of 0 and 10429.58"
  - printed: "18"
    value: "0.00"
    work: "10429.58 - 54818.00 is less than zero, so enter 0"
  - printed: "19"
    value: "10429.58"
    work: "smaller of 10429.58 and 394600.00"
  - printed: "20"
    value: "0.00"
    work: "smaller of 0 and 10429.58"
  - printed: "21"
    value: "0.00"
    work: "larger of 0 and 0"
  - printed: "22"
    value: "10429.58"
    work: "10429.58 - 0 = 10429.58, taxed at 0%"
  - printed: "23"
    value: "blank"
    work: "Lines 1 and 16 are the same, so skip lines 23-43"
  - printed: "24"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "25"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "26"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "27"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "28"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "29"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "30"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "31"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "32"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "33"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "34"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "35"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "36"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "37"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "38"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "39"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "40"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "41"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "42"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "43"
    value: "blank"
    work: "Skipped per line 22 instruction"
  - printed: "45"
    value: "0.00"
    work: "Lines 31, 34, 40 and 43 are blank; 0 + 0.00 (line 44) = 0.00"
  - printed: "47"
    value: "0.00"
    work: "smaller of 0.00 (line 45) and 1043.00 (line 46)"
```
```

### classm.sdtw.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "317901.55"
    work: "Form 1040 line 15"
  - printed: "2"
    value: "31832.00"
    work: "Form 1040 line 3a"
  - printed: "3"
    value: "0.00"
    work: "Not filing Form 4952; line 4g = 0"
  - printed: "4"
    value: "0.00"
    work: "No Form 4952 filed, so enter 0"
  - printed: "5"
    value: "0.00"
    work: "0 - 0 = 0"
  - printed: "6"
    value: "31832.00"
    work: "31832.00 - 0 = 31832.00"
  - printed: "7"
    value: "3303.00"
    work: "smaller of 3303.00, 3303.00"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0, 0"
  - printed: "9"
    value: "3303.00"
    work: "3303.00 - 0 = 3303.00"
  - printed: "10"
    value: "35135.00"
    work: "31832.00 + 3303.00"
  - printed: "11"
    value: "132.00"
    work: "0 + 132.00"
  - printed: "12"
    value: "132.00"
    work: "smaller of 3303.00, 132.00"
  - printed: "13"
    value: "35003.00"
    work: "35135.00 - 132.00"
  - printed: "14"
    value: "282898.55"
    work: "317901.55 - 35003.00"
  - printed: "15"
    value: "48350.00"
    work: "Married filing separately"
  - printed: "16"
    value: "48350.00"
    work: "smaller of 317901.55, 48350"
  - printed: "17"
    value: "48350.00"
    work: "smaller of 282898.55, 48350.00"
  - printed: "18"
    value: "282766.55"
    work: "317901.55 - 35135.00"
  - printed: "19"
    value: "197300.00"
    work: "smaller of 317901.55, 197300 (MFS)"
  - printed: "20"
    value: "197300.00"
    work: "smaller of 282898.55, 197300.00"
  - printed: "21"
    value: "282766.55"
    work: "larger of 282766.55, 197300.00"
  - printed: "22"
    value: "0.00"
    work: "48350.00 - 48350.00"
  - printed: "23"
    value: "35003.00"
    work: "Lines 1 and 16 differ; smaller of 317901.55, 35003.00"
  - printed: "24"
    value: "0.00"
    work: "line 22"
  - printed: "25"
    value: "35003.00"
    work: "35003.00 - 0"
  - printed: "26"
    value: "300000.00"
    work: "Married filing separately"
  - printed: "27"
    value: "300000.00"
    work: "smaller of 317901.55, 300000"
  - printed: "28"
    value: "282766.55"
    work: "282766.55 + 0"
  - printed: "29"
    value: "17233.45"
    work: "300000.00 - 282766.55"
  - printed: "30"
    value: "17233.45"
    work: "smaller of 35003.00, 17233.45"
  - printed: "31"
    value: "2585.02"
    work: "17233.45 x 0.15 = 2585.0175"
  - printed: "32"
    value: "17233.45"
    work: "0 + 17233.45; differs from line 1, continue"
  - printed: "33"
    value: "17769.55"
    work: "35003.00 - 17233.45"
  - printed: "34"
    value: "3553.91"
    work: "17769.55 x 0.20"
  - printed: "35"
    value: "132.00"
    work: "Sch D line 19 > 0; smaller of 3303.00, 132.00"
  - printed: "36"
    value: "317901.55"
    work: "35135.00 + 282766.55"
  - printed: "37"
    value: "317901.55"
    work: "line 1"
  - printed: "38"
    value: "0.00"
    work: "317901.55 - 317901.55 = 0"
  - printed: "39"
    value: "132.00"
    work: "132.00 - 0"
  - printed: "40"
    value: "33.00"
    work: "132.00 x 0.25"
  - printed: "41"
    value: "blank"
    work: "Sch D line 18 is zero; skip lines 41-43"
  - printed: "42"
    value: "blank"
    work: "Skipped"
  - printed: "43"
    value: "blank"
    work: "Skipped"
  - printed: "45"
    value: "74687.47"
    work: "2585.02 + 3553.91 + 33.00 + 0 + 68515.54"
  - printed: "47"
    value: "74687.47"
    work: "smaller of 74687.47, 80812.79"
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
    work: "Form 1040 line 3a"
  - printed: "3"
    value: "6530.00"
    work: "Form 4952 line 4g"
  - printed: "4"
    value: "516.00"
    work: "Form 4952 line 4e (Form 4952 filed)"
  - printed: "5"
    value: "6014.00"
    work: "6530.00 - 516.00"
  - printed: "6"
    value: "137264.00"
    work: "143278.00 - 6014.00"
  - printed: "7"
    value: "516.00"
    work: "smaller of 16368.00 and 516.00"
  - printed: "8"
    value: "516.00"
    work: "smaller of 6530.00 and 516.00"
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
    work: "smaller of 0.00 and 0.00"
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
    work: "smaller of 91213.55 and 48350.00"
  - printed: "17"
    value: "0.00"
    work: "smaller of 0.00 and 48350.00"
  - printed: "18"
    value: "0.00"
    work: "91213.55 - 137264.00 < 0, enter -0-"
  - printed: "19"
    value: "91213.55"
    work: "smaller of 91213.55 and 197300.00"
  - printed: "20"
    value: "0.00"
    work: "smaller of 0.00 and 91213.55"
  - printed: "21"
    value: "0.00"
    work: "larger of 0.00 and 0.00"
  - printed: "22"
    value: "48350.00"
    work: "48350.00 - 0.00; lines 1 and 16 differ, continue"
  - printed: "23"
    value: "91213.55"
    work: "smaller of 91213.55 and 137264.00"
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
    work: "smaller of 91213.55 and 533400.00"
  - printed: "28"
    value: "48350.00"
    work: "0.00 + 48350.00"
  - printed: "29"
    value: "42863.55"
    work: "91213.55 - 48350.00"
  - printed: "30"
    value: "42863.55"
    work: "smaller of 42863.55 and 42863.55"
  - printed: "31"
    value: "6429.53"
    work: "42863.55 x 0.15 = 6429.5325"
  - printed: "32"
    value: "91213.55"
    work: "48350.00 + 42863.55; equals line 1, skip 33-43"
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
  - printed: "41"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "42"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "43"
    value: "blank"
    work: "skipped: lines 1 and 32 are the same"
  - printed: "45"
    value: "6429.53"
    work: "6429.53 + 0 + 0 + 0 + 0.00 (line 44)"
  - printed: "47"
    value: "6429.53"
    work: "smaller of 6429.53 and 14984.00"
```
```

### classm.sdtw.5

```yaml
```yaml
lines:
  - printed: "1"
    value: "80691.75"
    work: "Form 1040 line 15 taxable income"
  - printed: "2"
    value: "2979.00"
    work: "Form 1040 line 3a qualified dividends"
  - printed: "3"
    value: "0.00"
    work: "Not filing Form 4952; line 4g = 0"
  - printed: "4"
    value: "0.00"
    work: "No Form 4952 filed, so zero"
  - printed: "5"
    value: "0.00"
    work: "0 - 0 = 0"
  - printed: "6"
    value: "2979.00"
    work: "2,979.00 - 0 = 2,979.00"
  - printed: "7"
    value: "20000.00"
    work: "smaller of 20,000 (Sch D line 15) and 20,000 (Sch D line 16)"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0 and 0"
  - printed: "9"
    value: "20000.00"
    work: "20,000 - 0 = 20,000"
  - printed: "10"
    value: "22979.00"
    work: "2,979 + 20,000"
  - printed: "11"
    value: "19800.00"
    work: "3,800 + 16,000"
  - printed: "12"
    value: "19800.00"
    work: "smaller of 20,000 and 19,800"
  - printed: "13"
    value: "3179.00"
    work: "22,979 - 19,800"
  - printed: "14"
    value: "77512.75"
    work: "80,691.75 - 3,179"
  - printed: "15"
    value: "48350.00"
    work: "Single: $48,350"
  - printed: "16"
    value: "48350.00"
    work: "smaller of 80,691.75 and 48,350"
  - printed: "17"
    value: "48350.00"
    work: "smaller of 77,512.75 and 48,350"
  - printed: "18"
    value: "57712.75"
    work: "80,691.75 - 22,979"
  - printed: "19"
    value: "80691.75"
    work: "smaller of 80,691.75 and 197,300"
  - printed: "20"
    value: "77512.75"
    work: "smaller of 77,512.75 and 80,691.75"
  - printed: "21"
    value: "77512.75"
    work: "larger of 57,712.75 and 77,512.75"
  - printed: "22"
    value: "0.00"
    work: "48,350 - 48,350 = 0; line 1 differs from line 16, so continue to line 23"
  - printed: "23"
    value: "3179.00"
    work: "smaller of 80,691.75 and 3,179"
  - printed: "24"
    value: "0.00"
    work: "line 22"
  - printed: "25"
    value: "3179.00"
    work: "3,179 - 0"
  - printed: "26"
    value: "533400.00"
    work: "Single: $533,400"
  - printed: "27"
    value: "80691.75"
    work: "smaller of 80,691.75 and 533,400"
  - printed: "28"
    value: "77512.75"
    work: "77,512.75 + 0"
  - printed: "29"
    value: "3179.00"
    work: "80,691.75 - 77,512.75"
  - printed: "30"
    value: "3179.00"
    work: "smaller of 3,179 and 3,179"
  - printed: "31"
    value: "476.85"
    work: "3,179 x 0.15"
  - printed: "32"
    value: "3179.00"
    work: "0 + 3,179; differs from line 1, so continue to line 33"
  - printed: "33"
    value: "0.00"
    work: "3,179 - 3,179"
  - printed: "34"
    value: "0.00"
    work: "0 x 0.20"
  - printed: "35"
    value: "16000.00"
    work: "Sch D line 19 is nonzero; smaller of 20,000 and 16,000"
  - printed: "36"
    value: "100491.75"
    work: "22,979 + 77,512.75"
  - printed: "37"
    value: "80691.75"
    work: "line 1"
  - printed: "38"
    value: "19800.00"
    work: "100,491.75 - 80,691.75"
  - printed: "39"
    value: "0.00"
    work: "16,000 - 19,800 < 0, so 0"
  - printed: "40"
    value: "0.00"
    work: "0 x 0.25"
  - printed: "41"
    value: "80691.75"
    work: "Sch D line 18 is nonzero; 77,512.75 + 0 + 3,179 + 0 + 0"
  - printed: "42"
    value: "0.00"
    work: "80,691.75 - 80,691.75"
  - printed: "43"
    value: "0.00"
    work: "0 x 0.28"
  - printed: "45"
    value: "12446.85"
    work: "476.85 + 0 + 0 + 0 + 11,970"
  - printed: "47"
    value: "12446.85"
    work: "smaller of 12,446.85 and 12,663"
```
```
