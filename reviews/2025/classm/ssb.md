# Class M hand-work — ssb

`Social Security Benefits Worksheet—Lines 6a and 6b` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 76343b958fae5bd72b0706831047544a4469ee252cbb389fb430cdfffe568769 |
| cases | 5 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.ssb.1 — prompt sha256 3bf924239dbd8fdbab5fb8d4595f94c1f0da91bdff968f770da99195588a0be7; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#1, ssb.line8#3, ssb.line9:positive, ssb.mfs_adjust#1, ssb.line10#3, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.1 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $32,936.00

### classm.ssb.1 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $32,936.00

### classm.ssb.1 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $32,936.00

### classm.ssb.1 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.1 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $7,936.00

### classm.ssb.1 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.1 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

Value: $7,936.00

### classm.ssb.1 — 13 — Enter one-half of line 12
Status: **AGREE**

Value: $3,968.00

### classm.ssb.1 — 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

### case classm.ssb.2 — prompt sha256 86874609f532e9d688b180df9e4573370d56ba2db5dce08c24d3ef248ffb9bb4; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:true, ssb.line7:positive, ssb.mfs_base#1, ssb.line8#2, ssb.line9:positive, ssb.mfs_adjust#1, ssb.line10#2, ssb.line11:positive, ssb.line12:right, ssb.line14:right, ssb.mfs_together:true, ssb.line16#0, ssb.line18_figured:right, ssb.line18#0

### classm.ssb.2 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $46,220.00

### classm.ssb.2 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $23,110.00

### classm.ssb.2 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $176,699.00

### classm.ssb.2 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $199,809.00

### classm.ssb.2 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $199,809.00

### classm.ssb.2 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **DISAGREE**

Project: $199,809.00
Model: $0.00
Work: Skipped (MFS, lived with spouse)

Ruling: representation; project retained; model value dropped from the fixture. The filer is married filing separately and lived with the spouse in 2025 (i1040gi p. 32, Social Security Benefits Worksheet, line 8, "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17"); the model left lines 8 to 15 blank, and the project figures every line (line 9 is line 7 less a $0.00 line 8, $199,809.00) but takes line 16 as line 7 x 85% for such a filer (ssb.mfs_together), $169,837.65, on which the model agrees, as on lines 17 ($39,287.00) and 18 ($39,287.00). A blank is not the number zero. No change to the data. [dropped]

### classm.ssb.2 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **DISAGREE**

Project: $199,809.00
Model: $0.00
Work: Skipped (MFS, lived with spouse)

Ruling: representation; project retained; model value dropped from the fixture. The filer is married filing separately and lived with the spouse in 2025 (i1040gi p. 32, Social Security Benefits Worksheet, line 8, "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17"); the model left lines 8 to 15 blank, and the project figures every line (line 11 is line 9 less a $0.00 line 10, $199,809.00) but takes line 16 as line 7 x 85% for such a filer (ssb.mfs_together), $169,837.65, on which the model agrees, as on lines 17 ($39,287.00) and 18 ($39,287.00). A blank is not the number zero. No change to the data. [dropped]

### classm.ssb.2 — 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 13 — Enter one-half of line 12
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **DISAGREE**

Project: $169,837.65
Model: $0.00
Work: Skipped (MFS, lived with spouse)

Ruling: representation; project retained; model value dropped from the fixture. The filer is married filing separately and lived with the spouse in 2025 (i1040gi p. 32, Social Security Benefits Worksheet, line 8, "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17"); the model left lines 8 to 15 blank, and the project figures every line (line 15 is line 11 x 85%, $169,837.65) but takes line 16 as line 7 x 85% for such a filer (ssb.mfs_together), $169,837.65, on which the model agrees, as on lines 17 ($39,287.00) and 18 ($39,287.00). A blank is not the number zero. No change to the data. [dropped]

### classm.ssb.2 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $169,837.65

### classm.ssb.2 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $39,287.00

### classm.ssb.2 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $39,287.00

### case classm.ssb.3 — prompt sha256 47072ae1b66c43a8682229b638b022908191f2af4f48bdcb9ddc863b9b105ec1; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:true, ssb.has_benefits:false, ssb.line7:floor, ssb.mfs_base#0, ssb.line8#0, ssb.line9:floor, ssb.mfs_adjust#0, ssb.line10#0, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.3 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **DISAGREE**

Project: $25,000.00
Model: $0.00
Work: Not reached; the worksheet stopped at line 7

Ruling: representation; project retained; model value dropped from the fixture. Line 6 is not less than line 5 here (no benefits; line 1 $0.00), so the worksheet stops at line 7 (i1040gi p. 32, Social Security Benefits Worksheet, line 7, "Is the amount on line 6 less than the amount on line 5? No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. STOP") and the model left the later lines blank; the project figures every line, line 8 being the $25,000 base amount for a filer not married filing jointly (p. 32, line 8), and line 7 is $0.00, so lines 9, 11 and 15 to 18 are $0.00 in both, line 18 (Form 1040 line 6b) included. A blank is not the number zero; both blind predictors likewise leave the lines after a STOP blank (scenario I10, which stops at line 9). As the earlier ruling on classm.ssb.4 line 10. No change to the data. [dropped]

### classm.ssb.3 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **DISAGREE**

Project: $9,000.00
Model: $0.00
Work: Not reached; the worksheet stopped at line 7

Ruling: representation; project retained; model value dropped from the fixture. Line 6 is not less than line 5 here (no benefits; line 1 $0.00), so the worksheet stops at line 7 (i1040gi p. 32, Social Security Benefits Worksheet, line 7, "Is the amount on line 6 less than the amount on line 5? No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. STOP") and the model left the later lines blank; the project figures every line, line 10 being the $9,000 amount for a filer not married filing jointly (p. 32, line 10), and line 7 is $0.00, so lines 9, 11 and 15 to 18 are $0.00 in both, line 18 (Form 1040 line 6b) included. A blank is not the number zero; both blind predictors likewise leave the lines after a STOP blank (scenario I10, which stops at line 9). As the earlier ruling on classm.ssb.4 line 10. No change to the data. [dropped]

### classm.ssb.3 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 13 — Enter one-half of line 12
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

### case classm.ssb.4 — prompt sha256 c7043c79e2a96ac39d87adc31a387d6e5e7c0ced6829795415eefe7de57ca6dc; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:floor, ssb.mfs_base#1, ssb.line8#1, ssb.line9:floor, ssb.mfs_adjust#1, ssb.line10#1, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.4 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $-103,568.92

### classm.ssb.4 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $-103,568.92

### classm.ssb.4 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **DISAGREE**

Project: $32,000.00
Model: $0.00
Work: Skipped: worksheet stopped at line 7

Ruling: representation; project retained; model value dropped from the fixture. Line 6 is not less than line 5 here (no benefits; line 1 $0.00), so the worksheet stops at line 7 (i1040gi p. 32, Social Security Benefits Worksheet, line 7, "Is the amount on line 6 less than the amount on line 5? No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. STOP") and the model left the later lines blank; the project figures every line, line 8 being the $32,000 base amount for married filing jointly (p. 32, line 8), and line 7 is $0.00, so lines 9, 11 and 15 to 18 are $0.00 in both, line 18 (Form 1040 line 6b) included. A blank is not the number zero; both blind predictors likewise leave the lines after a STOP blank (scenario I10, which stops at line 9). As the earlier ruling on classm.ssb.4 line 10. No change to the data. [dropped]

### classm.ssb.4 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **DISAGREE**

Project: $12,000.00
Model: $0.00
Work: Skipped: worksheet stopped at line 7

Ruling: representation; project retained; model value dropped from the fixture. Line 6 is not less than line 5 here, so the worksheet stops at line 7 (i1040gi p. 32, Social Security Benefits Worksheet, line 7, "None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. STOP") and the model leaves the later lines blank; the project figures every line (line 10 is the $12,000 amount for married filing jointly) and line 18 is $0 either way, as the EIC worksheet ruling. [dropped]

### classm.ssb.4 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 13 — Enter one-half of line 12
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

### case classm.ssb.5 — prompt sha256 8ccccc835d139a5df5bb6c1facf461f62937668101d3c7db0f46625614cd33f9; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:true, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#0, ssb.line8#4, ssb.line9:positive, ssb.mfs_adjust#0, ssb.line10#4, ssb.line11:positive, ssb.line12:right, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:right, ssb.line18#1

### classm.ssb.5 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $244,885.00

### classm.ssb.5 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $244,885.00

### classm.ssb.5 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $244,885.00

### classm.ssb.5 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.5 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $219,885.00

### classm.ssb.5 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.5 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $210,885.00

### classm.ssb.5 — 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

Value: $9,000.00

### classm.ssb.5 — 13 — Enter one-half of line 12
Status: **AGREE**

Value: $4,500.00

### classm.ssb.5 — 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **AGREE**

Value: $179,252.25

### classm.ssb.5 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $179,252.25

### classm.ssb.5 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.ssb.1

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total of box 5 on all Forms SSA-1099 and RRB-1099 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 x 0.50 = 0.00"
  - printed: "3"
    value: "32936.00"
    work: "32936.00 + 0 + 0 + 0 + 0 + 0 + 0 = 32936.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "32936.00"
    work: "0.00 + 32936.00 + 0.00 = 32936.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11 through 20, 23 and 25 add up to 0.00"
  - printed: "7"
    value: "32936.00"
    work: "0.00 < 32936.00, so yes: 32936.00 - 0.00 = 32936.00"
  - printed: "8"
    value: "25000.00"
    work: "Head of household: enter 25,000"
  - printed: "9"
    value: "7936.00"
    work: "25000.00 < 32936.00, so yes: 32936.00 - 25000.00 = 7936.00"
  - printed: "10"
    value: "9000.00"
    work: "Head of household: enter 9,000"
  - printed: "11"
    value: "0.00"
    work: "7936.00 - 9000.00 is less than zero, so enter -0-"
  - printed: "12"
    value: "7936.00"
    work: "Smaller of 7936.00 or 9000.00 = 7936.00"
  - printed: "13"
    value: "3968.00"
    work: "7936.00 / 2 = 3968.00"
  - printed: "14"
    value: "0.00"
    work: "Smaller of 0.00 or 3968.00 = 0.00"
  - printed: "15"
    value: "0.00"
    work: "Line 11 is zero, so enter -0-"
  - printed: "16"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "Smaller of 0.00 or 0.00 = 0.00"
```

### classm.ssb.2

```yaml
lines:
  - printed: "1"
    value: "46220.00"
    work: "Total of box 5 on all Forms SSA-1099 and RRB-1099 = 46,220.00"
  - printed: "2"
    value: "23110.00"
    work: "46,220.00 x 0.50 = 23,110.00"
  - printed: "3"
    value: "176699.00"
    work: "14,441 + 44,289 + 31,263 + 26,782 + 59,924 + 0 + 0 = 176,699.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "199809.00"
    work: "23,110.00 + 176,699.00 + 0.00 = 199,809.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23 and 25 total 0.00"
  - printed: "7"
    value: "199809.00"
    work: "Line 6 (0) is less than line 5, so 199,809.00 - 0.00 = 199,809.00"
  - printed: "8"
    value: "blank"
    work: "Married filing separately and lived with spouse during 2025: skip lines 8-15"
  - printed: "9"
    value: "blank"
    work: "Skipped (MFS, lived with spouse)"
  - printed: "10"
    value: "blank"
    work: "Skipped (MFS, lived with spouse)"
  - printed: "11"
    value: "blank"
    work: "Skipped (MFS, lived with spouse)"
  - printed: "12"
    value: "blank"
    work: "Skipped (MFS, lived with spouse)"
  - printed: "13"
    value: "blank"
    work: "Skipped (MFS, lived with spouse)"
  - printed: "14"
    value: "blank"
    work: "Skipped (MFS, lived with spouse)"
  - printed: "15"
    value: "blank"
    work: "Skipped (MFS, lived with spouse)"
  - printed: "16"
    value: "169837.65"
    work: "MFS and lived with spouse: line 7 x 0.85 = 199,809.00 x 0.85 = 169,837.65"
  - printed: "17"
    value: "39287.00"
    work: "46,220.00 x 0.85 = 39,287.00"
  - printed: "18"
    value: "39287.00"
    work: "Smaller of line 16 (169,837.65) or line 17 (39,287.00) = 39,287.00"
```

### classm.ssb.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total of box 5 on all SSA-1099/RRB-1099 forms = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 x 0.50 = 0.00"
  - printed: "3"
    value: "0.00"
    work: "1z 0 + 2b 0 + 3b 0 + 4b 0 + 5b 0 + 7a 0 + 8 0 = 0.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25 total = 0.00"
  - printed: "7"
    value: "blank"
    work: "Line 6 (0.00) is not less than line 5 (0.00): No, so STOP. No benefits are taxable; enter -0- on 1040 line 6b"
  - printed: "8"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "9"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "10"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "11"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "12"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "13"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "14"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "15"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "16"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "17"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7"
  - printed: "18"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7 (1040 line 6b = -0-)"
```
```

### classm.ssb.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total box 5 of Forms SSA-1099/RRB-1099 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 x 0.50 = 0.00"
  - printed: "3"
    value: "-103568.92"
    work: "6574.00 + 0 + 0 + 0 + 0 + 0 + (-110142.92) = -103568.92"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "-103568.92"
    work: "0.00 + (-103568.92) + 0.00 = -103568.92"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25 (IRA deductions 0) total = 0.00"
  - printed: "7"
    value: "blank"
    work: "Line 6 (0.00) is not less than line 5 (-103568.92); answer No, STOP; enter 0 on Form 1040 line 6b"
  - printed: "8"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "9"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "10"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "11"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "12"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "13"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "14"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "15"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "16"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "17"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7"
  - printed: "18"
    value: "blank"
    work: "Skipped: worksheet stopped at line 7; no benefits taxable, Form 1040 line 6b = 0"
```
```

### classm.ssb.5

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total of box 5 from all Forms SSA-1099 and RRB-1099 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 x 0.50 = 0.00"
  - printed: "3"
    value: "244885.00"
    work: "0 + 0 + 237588.00 + 0 + 0 + 7297.00 + 0 = 244885.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "244885.00"
    work: "0.00 + 244885.00 + 0.00 = 244885.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25 total = 0.00"
  - printed: "7"
    value: "244885.00"
    work: "Line 6 (0) < line 5, so yes: 244885.00 - 0.00 = 244885.00"
  - printed: "8"
    value: "25000.00"
    work: "Qualifying surviving spouse = 25000.00"
  - printed: "9"
    value: "219885.00"
    work: "Line 8 < line 7, so yes: 244885.00 - 25000.00 = 219885.00"
  - printed: "10"
    value: "9000.00"
    work: "Qualifying surviving spouse = 9000.00"
  - printed: "11"
    value: "210885.00"
    work: "219885.00 - 9000.00 = 210885.00"
  - printed: "12"
    value: "9000.00"
    work: "Smaller of 219885.00 or 9000.00 = 9000.00"
  - printed: "13"
    value: "4500.00"
    work: "9000.00 / 2 = 4500.00"
  - printed: "14"
    value: "0.00"
    work: "Smaller of line 2 (0.00) or line 13 (4500.00) = 0.00"
  - printed: "15"
    value: "179252.25"
    work: "210885.00 x 0.85 = 179252.25"
  - printed: "16"
    value: "179252.25"
    work: "0.00 + 179252.25 = 179252.25"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "Smaller of 179252.25 or 0.00 = 0.00"
```
