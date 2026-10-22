# Class M hand-work — ssb

`Social Security Benefits Worksheet—Lines 6a and 6b` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | b4d00c384b244b782ef4db32278e430d07b98994a5ea29bcd708d13a9a486522 |
| cases | 5 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.ssb.1 — prompt sha256 6f98a47b661082672020f8092b0c210c91011a69a0449d3e57f148688e65bbc2; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#1, ssb.line8#3, ssb.line9:positive, ssb.mfs_adjust#1, ssb.line10#3, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

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

### case classm.ssb.2 — prompt sha256 ee2d73257228dcfe19b3180ab3d5ad3d759a6520177ca8a1cc1e78ce083d7601; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:true, ssb.has_benefits:true, ssb.line7:positive, ssb.mfs_base#0, ssb.line8#0, ssb.line9:positive, ssb.mfs_adjust#0, ssb.line10#0, ssb.line11:positive, ssb.line12:right, ssb.line14:right, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:right, ssb.line18#0

### classm.ssb.2 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $17,949.00

### classm.ssb.2 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $8,974.50

### classm.ssb.2 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $156,121.00

### classm.ssb.2 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $165,095.50

### classm.ssb.2 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $165,095.50

### classm.ssb.2 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.2 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $140,095.50

### classm.ssb.2 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.2 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $131,095.50

### classm.ssb.2 — 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

Value: $9,000.00

### classm.ssb.2 — 13 — Enter one-half of line 12
Status: **AGREE**

Value: $4,500.00

### classm.ssb.2 — 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

Value: $4,500.00

### classm.ssb.2 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **AGREE**

Value: $111,431.18

### classm.ssb.2 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $115,931.18

### classm.ssb.2 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $15,256.65

### classm.ssb.2 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $15,256.65

### case classm.ssb.3 — prompt sha256 c01b1c2ba881f03d68db19e97b7347f86607defced2b67d608697d3141d6e241; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:floor, ssb.mfs_base#1, ssb.line8#2, ssb.line9:floor, ssb.mfs_adjust#1, ssb.line10#2, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:true, ssb.line16#0, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.3 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $-1,500.00

### classm.ssb.3 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $-1,500.00

### classm.ssb.3 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $0.00

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

### case classm.ssb.4 — prompt sha256 d3a458bab21fda1286793d851f72478afcdc163dce8536c27ef5db834d95b7c3; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#1, ssb.line8#1, ssb.line9:floor, ssb.mfs_adjust#1, ssb.line10#1, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.4 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $6,724.00

### classm.ssb.4 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $6,724.00

### classm.ssb.4 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $6,724.00

### classm.ssb.4 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $32,000.00

### classm.ssb.4 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **DISAGREE**

Project: $12,000.00
Model: $0.00
Work: Not reached; worksheet stopped at line 9

Ruling: representation; project retained; model value dropped from the fixture. Where line 9 says STOP (none of the benefits are taxable), the model leaves the later lines blank; the project figures every line and line 18 is $0 either way (lines 11 to 16 are zero once line 9 is zero), as the EIC worksheet ruling. [dropped]

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

### case classm.ssb.5 — prompt sha256 ef4f18cb9de1775923452609e40371222c5364f7c01a77d83c890bc07e451f75; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#1, ssb.line8#4, ssb.line9:positive, ssb.mfs_adjust#1, ssb.line10#4, ssb.line11:positive, ssb.line12:right, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:right, ssb.line18#1

### classm.ssb.5 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $272,822.00

### classm.ssb.5 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $272,822.00

### classm.ssb.5 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $272,822.00

### classm.ssb.5 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.5 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $247,822.00

### classm.ssb.5 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.5 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $238,822.00

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

Value: $202,998.70

### classm.ssb.5 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $202,998.70

### classm.ssb.5 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.ssb.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Total of box 5 of all Forms SSA-1099 and RRB-1099 = 0.00"
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
    work: "Schedule 1 lines 11, 13, 15, 16, 17 all 0; no other amounts given; total 0.00"
  - printed: "7"
    value: "32936.00"
    work: "0.00 < 32936.00, so yes: 32936.00 - 0.00 = 32936.00"
  - printed: "8"
    value: "25000.00"
    work: "Head of household enters 25000"
  - printed: "9"
    value: "7936.00"
    work: "25000 < 32936, so yes: 32936.00 - 25000.00 = 7936.00"
  - printed: "10"
    value: "9000.00"
    work: "Head of household enters 9000"
  - printed: "11"
    value: "0.00"
    work: "7936.00 - 9000.00 = -1064.00; zero or less, so 0"
  - printed: "12"
    value: "7936.00"
    work: "smaller of 7936.00 and 9000.00"
  - printed: "13"
    value: "3968.00"
    work: "7936.00 / 2 = 3968.00"
  - printed: "14"
    value: "0.00"
    work: "smaller of 0.00 and 3968.00"
  - printed: "15"
    value: "0.00"
    work: "line 11 is zero, so 0"
  - printed: "16"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "smaller of 0.00 and 0.00"
```
```

### classm.ssb.2

```yaml
lines:
  - printed: "1"
    value: "17949.00"
    work: "Total of box 5 of all SSA-1099/RRB-1099 = 17,949.00"
  - printed: "2"
    value: "8974.50"
    work: "17,949.00 x 0.50 = 8,974.50"
  - printed: "3"
    value: "156121.00"
    work: "43,023 + 0 + 80,000 + 20,068 + 0 + 13,030 + 0 = 156,121.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "165095.50"
    work: "8,974.50 + 156,121.00 + 0.00 = 165,095.50"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25 given amounts total 0.00"
  - printed: "7"
    value: "165095.50"
    work: "Line 6 (0.00) < line 5, so 165,095.50 - 0.00 = 165,095.50"
  - printed: "8"
    value: "25000.00"
    work: "Single: enter 25,000"
  - printed: "9"
    value: "140095.50"
    work: "Line 8 < line 7, so 165,095.50 - 25,000 = 140,095.50"
  - printed: "10"
    value: "9000.00"
    work: "Single: enter 9,000"
  - printed: "11"
    value: "131095.50"
    work: "140,095.50 - 9,000 = 131,095.50"
  - printed: "12"
    value: "9000.00"
    work: "Smaller of 140,095.50 or 9,000 = 9,000.00"
  - printed: "13"
    value: "4500.00"
    work: "9,000 / 2 = 4,500.00"
  - printed: "14"
    value: "4500.00"
    work: "Smaller of 8,974.50 or 4,500 = 4,500.00"
  - printed: "15"
    value: "111431.18"
    work: "131,095.50 x 0.85 = 111,431.175, rounded to 111,431.18"
  - printed: "16"
    value: "115931.18"
    work: "4,500.00 + 111,431.18 = 115,931.18"
  - printed: "17"
    value: "15256.65"
    work: "17,949.00 x 0.85 = 15,256.65"
  - printed: "18"
    value: "15256.65"
    work: "Smaller of 115,931.18 or 15,256.65 = 15,256.65"
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
    value: "-1500.00"
    work: "1z 0 + 2b 0 + 3b 0 + 4b 0 + 5b 0 + 7a -1,500 + 8 0 = -1,500.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "-1500.00"
    work: "0.00 + -1,500.00 + 0.00 = -1,500.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11, 13, 15, 16, 17 all 0; no other amounts given = 0.00"
  - printed: "7"
    value: "0.00"
    work: "Line 6 (0.00) is not less than line 5 (-1,500.00); No -> STOP, none of the benefits are taxable"
  - printed: "8"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "9"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "10"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "11"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "12"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "13"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "14"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "15"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "16"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "17"
    value: ""
    work: "Skipped: STOP at line 7"
  - printed: "18"
    value: "0.00"
    work: "Line 7 STOP: none of the benefits are taxable; enter -0- on Form 1040 line 6b"
```
```

### classm.ssb.4

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
    value: "6724.00"
    work: "6574.00 + 150.00 + 0 + 0 + 0 + 0 + 0 = 6724.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "6724.00"
    work: "0.00 + 6724.00 + 0.00 = 6724.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11, 13, 15, 16, 17 are all 0.00; no other amounts given; total = 0.00"
  - printed: "7"
    value: "6724.00"
    work: "Line 6 (0.00) < line 5 (6724.00), so yes; 6724.00 - 0.00 = 6724.00"
  - printed: "8"
    value: "32000.00"
    work: "Married filing jointly: enter 32,000"
  - printed: "9"
    value: "blank"
    work: "Line 8 (32000.00) is not less than line 7 (6724.00); STOP, none of the benefits are taxable"
  - printed: "10"
    value: "blank"
    work: "Not reached; worksheet stopped at line 9"
  - printed: "11"
    value: "blank"
    work: "Not reached; worksheet stopped at line 9"
  - printed: "12"
    value: "blank"
    work: "Not reached; worksheet stopped at line 9"
  - printed: "13"
    value: "blank"
    work: "Not reached; worksheet stopped at line 9"
  - printed: "14"
    value: "blank"
    work: "Not reached; worksheet stopped at line 9"
  - printed: "15"
    value: "blank"
    work: "Not reached; worksheet stopped at line 9"
  - printed: "16"
    value: "blank"
    work: "Not reached; worksheet stopped at line 9"
  - printed: "17"
    value: "blank"
    work: "Not reached; worksheet stopped at line 9"
  - printed: "18"
    value: "0.00"
    work: "Line 9 STOP rule: none of the benefits are taxable; enter -0- on Form 1040 line 6b"
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
    value: "272822.00"
    work: "95263 + 30279 + 0 + 46977 + 2591 + 97712 + 0 = 272822.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "272822.00"
    work: "0.00 + 272822.00 + 0.00 = 272822.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11, 13, 15, 16, 17 (others not given) = 0.00"
  - printed: "7"
    value: "272822.00"
    work: "Line 6 (0) is less than line 5, so yes: 272822.00 - 0.00 = 272822.00"
  - printed: "8"
    value: "25000.00"
    work: "Qualifying surviving spouse, so enter $25,000"
  - printed: "9"
    value: "247822.00"
    work: "Line 8 is less than line 7, so yes: 272822.00 - 25000.00 = 247822.00"
  - printed: "10"
    value: "9000.00"
    work: "Qualifying surviving spouse, so enter $9,000"
  - printed: "11"
    value: "238822.00"
    work: "247822.00 - 9000.00 = 238822.00"
  - printed: "12"
    value: "9000.00"
    work: "smaller of 247822.00 or 9000.00"
  - printed: "13"
    value: "4500.00"
    work: "9000.00 / 2 = 4500.00"
  - printed: "14"
    value: "0.00"
    work: "smaller of line 2 (0.00) or line 13 (4500.00)"
  - printed: "15"
    value: "202998.70"
    work: "238822.00 x 0.85 = 202998.70"
  - printed: "16"
    value: "202998.70"
    work: "0.00 + 202998.70 = 202998.70"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "smaller of line 16 (202998.70) or line 17 (0.00)"
```
```
