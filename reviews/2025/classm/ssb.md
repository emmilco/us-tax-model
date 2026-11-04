# Class M hand-work — ssb

`Social Security Benefits Worksheet—Lines 6a and 6b` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e9e7f70f0e4ab7856108d22e80b83291c698f2a909cb4efa742ac1b747ba8e3d |
| cases | 6 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.ssb.1 — prompt sha256 9a38708c0e982ca799aef67fa7aecf0765e9ea9c4a60fb97a8c2e08b9c22b31d; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#1, ssb.lines8_to_15:false, ssb.line8#2, ssb.line9:positive, ssb.past7:true, ssb.past9:true, ssb.show8_9:false, ssb.show10_15:false, ssb.show16_18:true, ssb.mfs_adjust#1, ssb.line10#2, ssb.line11:positive, ssb.line12:right, ssb.line14:left, ssb.mfs_together:true, ssb.line16#0, ssb.line18_figured:right, ssb.line18#1

### classm.ssb.1 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $51,731.00

### classm.ssb.1 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $51,731.00

### classm.ssb.1 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **AGREE**

Value: $51,731.00

### classm.ssb.1 — 16 — Add lines 14 and 15 (if married filing separately and you lived with your spouse
Status: **AGREE**

Value: $43,971.35

### classm.ssb.1 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.1 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

### case classm.ssb.2 — prompt sha256 e2c2975447a32c524b894481fc3ea2d496263268d1fbef66c814a826e9918dd1; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:true, ssb.has_benefits:true, ssb.line7:positive, ssb.mfs_base#0, ssb.lines8_to_15:true, ssb.line8#2, ssb.line9:floor, ssb.past7:true, ssb.past9:false, ssb.show8_9:true, ssb.show10_15:false, ssb.show16_18:false, ssb.mfs_adjust#0, ssb.line10#2, ssb.line11:floor, ssb.line12:left, ssb.line14:right, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#0

### classm.ssb.2 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $20,000.00

### classm.ssb.2 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $10,000.00

### classm.ssb.2 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $10,000.00

### classm.ssb.2 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $20,000.00

### classm.ssb.2 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **AGREE**

Value: $20,000.00

### classm.ssb.2 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.2 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8
Status: **SKIPPED**

Model: blank
Work: 25,000 is not less than 20,000, so no: STOP; none taxable, enter -0- on 1040 line 6b

No numeric assertion or class M credit: the model left this line blank.

### case classm.ssb.3 — prompt sha256 b5bcb474fbc1fcc9cdd77a7e3ebb5c551088335cd730d660691dfea1c64783b9; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.has_benefits:false, ssb.line7:floor, ssb.lines8_to_15:true, ssb.line8#1, ssb.line9:floor, ssb.past7:false, ssb.past9:false, ssb.show8_9:false, ssb.show10_15:false, ssb.show16_18:false, ssb.line10#1, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.3 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $-159,710.91

### classm.ssb.3 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $-159,710.91

### classm.ssb.3 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $712.50

### classm.ssb.3 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **SKIPPED**

Model: blank
Work: Line 6 (712.50) is not less than line 5 (-159710.91), so the answer is No: STOP, none taxable, 1040 line 6b = 0

No numeric assertion or class M credit: the model left this line blank.

### case classm.ssb.4 — prompt sha256 02a2510a202d05e2d6428ae4572a0405dd83f179b35a70fc0ddc3310d571333e; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.has_benefits:false, ssb.line7:positive, ssb.lines8_to_15:true, ssb.line8#3, ssb.line9:positive, ssb.past7:true, ssb.past9:true, ssb.show8_9:true, ssb.show10_15:true, ssb.show16_18:true, ssb.line10#3, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.4 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $32,936.00

### classm.ssb.4 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $32,936.00

### classm.ssb.4 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **AGREE**

Value: $32,936.00

### classm.ssb.4 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.4 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8
Status: **AGREE**

Value: $7,936.00

### classm.ssb.4 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.4 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

Value: $7,936.00

### classm.ssb.4 — 13 — Enter one-half of line 12
Status: **AGREE**

Value: $3,968.00

### classm.ssb.4 — 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 16 — Add lines 14 and 15 (if married filing separately and you lived with your spouse
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

### case classm.ssb.5 — prompt sha256 bdf8ac396d59e3b379c739434a52b6d61277edd62d4be2ddb8e41960e3aad055; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.has_benefits:false, ssb.line7:positive, ssb.lines8_to_15:true, ssb.line8#0, ssb.line9:positive, ssb.past7:true, ssb.past9:true, ssb.show8_9:true, ssb.show10_15:true, ssb.show16_18:true, ssb.line10#0, ssb.line11:positive, ssb.line12:right, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:right, ssb.line18#1

### classm.ssb.5 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $50,121.00

### classm.ssb.5 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $50,121.00

### classm.ssb.5 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **AGREE**

Value: $50,121.00

### classm.ssb.5 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.5 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8
Status: **AGREE**

Value: $25,121.00

### classm.ssb.5 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.5 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $16,121.00

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

Value: $13,702.85

### classm.ssb.5 — 16 — Add lines 14 and 15 (if married filing separately and you lived with your spouse
Status: **AGREE**

Value: $13,702.85

### classm.ssb.5 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

### case classm.ssb.6 — prompt sha256 3feb214fce41ff2e0523eda11f46da3a3b006ca3a4357a4d4edf0e253164d9a3; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.has_benefits:false, ssb.line7:positive, ssb.lines8_to_15:true, ssb.line8#4, ssb.line9:positive, ssb.past7:true, ssb.past9:true, ssb.show8_9:true, ssb.show10_15:true, ssb.show16_18:true, ssb.line10#4, ssb.line11:positive, ssb.line12:right, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:right, ssb.line18#1

### classm.ssb.6 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.6 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.6 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $515,291.00

### classm.ssb.6 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.6 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $515,291.00

### classm.ssb.6 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.ssb.6 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **AGREE**

Value: $515,291.00

### classm.ssb.6 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.6 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8
Status: **AGREE**

Value: $490,291.00

### classm.ssb.6 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.6 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $481,291.00

### classm.ssb.6 — 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

Value: $9,000.00

### classm.ssb.6 — 13 — Enter one-half of line 12
Status: **AGREE**

Value: $4,500.00

### classm.ssb.6 — 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

Value: $0.00

### classm.ssb.6 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **AGREE**

Value: $409,097.35

### classm.ssb.6 — 16 — Add lines 14 and 15 (if married filing separately and you lived with your spouse
Status: **AGREE**

Value: $409,097.35

### classm.ssb.6 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.6 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.ssb.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total of box 5 of SSA-1099/RRB-1099 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 x 0.50 = 0.00"
  - printed: "3"
    value: "51731.00"
    work: "0 + 0 + 0 + 0 + 0 + 51,731.00 + 0 = 51,731.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "51731.00"
    work: "0.00 + 51,731.00 + 0.00 = 51,731.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25 total = 0.00"
  - printed: "7"
    value: "51731.00"
    work: "Line 6 (0.00) < line 5, so yes: 51,731.00 - 0.00 = 51,731.00"
  - printed: "16"
    value: "43971.35"
    work: "MFS and lived with spouse, so skip lines 8-15: 51,731.00 x 0.85 = 43,971.35"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "Smaller of line 16 (43,971.35) or line 17 (0.00) = 0.00"
```
```

### classm.ssb.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "20000.00"
    work: "Total box 5 of SSA-1099/RRB-1099 = 20,000.00"
  - printed: "2"
    value: "10000.00"
    work: "20,000.00 x 0.50 = 10,000.00"
  - printed: "3"
    value: "10000.00"
    work: "1z 10,000 + 2b 0 + 3b 0 + 4b 0 + 5b 0 + 7a 0 + 8 0 = 10,000.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "20000.00"
    work: "10,000 + 10,000 + 0 = 20,000.00"
  - printed: "6"
    value: "0.00"
    work: "Sch 1 lines 11-20 (IRA deduction 0), 23, 25 all 0 = 0.00"
  - printed: "7"
    value: "20000.00"
    work: "0 < 20,000, so yes: 20,000 - 0 = 20,000.00"
  - printed: "8"
    value: "25000.00"
    work: "MFS and lived apart from spouse all of 2025, so enter $25,000"
  - printed: "9"
    value: "blank"
    work: "25,000 is not less than 20,000, so no: STOP; none taxable, enter -0- on 1040 line 6b"
```
```

### classm.ssb.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total of box 5 of all SSA-1099/RRB-1099 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 x 0.50 = 0.00"
  - printed: "3"
    value: "-159710.91"
    work: "6574.00 + 0 + 0 + 0 + 0 + 0 + (-166284.91) = -159710.91"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "-159710.91"
    work: "0.00 + (-159710.91) + 0.00 = -159710.91"
  - printed: "6"
    value: "712.50"
    work: "Sch 1 lines 11-20, 23, 25: 0 + 712.50 + 0 + 0 + 0 + 0 + 0 + 0 = 712.50"
  - printed: "7"
    value: "blank"
    work: "Line 6 (712.50) is not less than line 5 (-159710.91), so the answer is No: STOP, none taxable, 1040 line 6b = 0"
```
```

### classm.ssb.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total of box 5 of all Forms SSA-1099/RRB-1099 = 0.00"
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
    work: "Schedule 1 lines 11-20, 23, 25 total = 0.00"
  - printed: "7"
    value: "32936.00"
    work: "Line 6 (0.00) is less than line 5, so yes: 32936.00 - 0.00 = 32936.00"
  - printed: "8"
    value: "25000.00"
    work: "Head of household: 25000.00"
  - printed: "9"
    value: "7936.00"
    work: "Line 8 is less than line 7, so yes: 32936.00 - 25000.00 = 7936.00"
  - printed: "10"
    value: "9000.00"
    work: "Head of household: 9000.00"
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
```

### classm.ssb.5

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total box 5 of SSA-1099/RRB-1099 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 x 0.50 = 0.00"
  - printed: "3"
    value: "50121.00"
    work: "50,000 + 121 + 0 + 0 + 0 + 0 + 0 = 50,121.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "50121.00"
    work: "0 + 50,121 + 0 = 50,121.00"
  - printed: "6"
    value: "0.00"
    work: "Sch 1 lines 11-20, 23, 25 total = 0.00"
  - printed: "7"
    value: "50121.00"
    work: "0 < 50,121 yes; 50,121 - 0 = 50,121.00"
  - printed: "8"
    value: "25000.00"
    work: "Single = 25,000"
  - printed: "9"
    value: "25121.00"
    work: "25,000 < 50,121 yes; 50,121 - 25,000 = 25,121.00"
  - printed: "10"
    value: "9000.00"
    work: "Single = 9,000"
  - printed: "11"
    value: "16121.00"
    work: "25,121 - 9,000 = 16,121.00"
  - printed: "12"
    value: "9000.00"
    work: "smaller of 25,121 or 9,000 = 9,000.00"
  - printed: "13"
    value: "4500.00"
    work: "9,000 / 2 = 4,500.00"
  - printed: "14"
    value: "0.00"
    work: "smaller of line 2 (0) or line 13 (4,500) = 0.00"
  - printed: "15"
    value: "13702.85"
    work: "16,121 x 0.85 = 13,702.85"
  - printed: "16"
    value: "13702.85"
    work: "0 + 13,702.85 = 13,702.85"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "smaller of 13,702.85 or 0.00 = 0.00"
```
```

### classm.ssb.6

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total of box 5 of all SSA-1099/RRB-1099 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 x 0.50 = 0.00"
  - printed: "3"
    value: "515291.00"
    work: "474286 + 0 + 27786 + 0 + 0 + 5182 + 8037 = 515291.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "515291.00"
    work: "0 + 515291 + 0 = 515291.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25 (all given amounts 0, IRA deduction 0) = 0.00"
  - printed: "7"
    value: "515291.00"
    work: "Line 6 (0) is less than line 5, so yes: 515291 - 0 = 515291.00"
  - printed: "8"
    value: "25000.00"
    work: "Qualifying surviving spouse = 25000.00"
  - printed: "9"
    value: "490291.00"
    work: "Line 8 is less than line 7, so yes: 515291 - 25000 = 490291.00"
  - printed: "10"
    value: "9000.00"
    work: "Qualifying surviving spouse = 9000.00"
  - printed: "11"
    value: "481291.00"
    work: "490291 - 9000 = 481291.00"
  - printed: "12"
    value: "9000.00"
    work: "smaller of 490291 or 9000 = 9000.00"
  - printed: "13"
    value: "4500.00"
    work: "9000 / 2 = 4500.00"
  - printed: "14"
    value: "0.00"
    work: "smaller of line 2 (0) or line 13 (4500) = 0.00"
  - printed: "15"
    value: "409097.35"
    work: "481291 x 0.85 = 409097.35"
  - printed: "16"
    value: "409097.35"
    work: "0 + 409097.35 = 409097.35"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "smaller of line 16 (409097.35) or line 17 (0) = 0.00"
```
```
