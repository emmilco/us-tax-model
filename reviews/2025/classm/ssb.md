# Class M hand-work — ssb

`Social Security Benefits Worksheet—Lines 6a and 6b` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 5 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.ssb.1 — prompt sha256 2504a94bf9f1ab5c1abe18fc81d08b56e88919dcb689a86aa72586377bae6a9e; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#1, ssb.line8#3, ssb.line9:positive, ssb.mfs_adjust#1, ssb.line10#3, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

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

### case classm.ssb.2 — prompt sha256 9d63ce8727d3ab4ef17ddc8391c7420343ddbfa974210fb0d09160d07c8974a6; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:true, ssb.has_benefits:true, ssb.line7:positive, ssb.mfs_base#0, ssb.line8#0, ssb.line9:positive, ssb.mfs_adjust#0, ssb.line10#0, ssb.line11:positive, ssb.line12:right, ssb.line14:right, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:right, ssb.line18#0

### classm.ssb.2 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $42,441.00

### classm.ssb.2 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $21,220.50

### classm.ssb.2 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $120,076.00

### classm.ssb.2 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $141,296.50

### classm.ssb.2 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $6,212.00

### classm.ssb.2 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $135,084.50

### classm.ssb.2 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.2 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $110,084.50

### classm.ssb.2 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.2 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $101,084.50

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

Value: $85,921.83

### classm.ssb.2 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $90,421.83

### classm.ssb.2 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $36,074.85

### classm.ssb.2 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $36,074.85

### case classm.ssb.3 — prompt sha256 2cda0b48bbca11452e00c0e41289dd43a55dc232c51ed5d8e1b65ce02a8b4bb8; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:floor, ssb.mfs_base#1, ssb.line8#2, ssb.line9:floor, ssb.mfs_adjust#1, ssb.line10#2, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:true, ssb.line16#0, ssb.line18_figured:left, ssb.line18#1

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

### case classm.ssb.4 — prompt sha256 033e8eee950bc90b98e6e9952a74005a67450c89c519b109580ac9f1810a62da; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#1, ssb.line8#1, ssb.line9:floor, ssb.mfs_adjust#1, ssb.line10#1, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

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
Work: Skipped; STOP at line 9

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

### case classm.ssb.5 — prompt sha256 b3ea4af6c143b256de2ee615556aff4c4d5a16ac710a6e7d3bce56395f16e587; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:false, ssb.line7:positive, ssb.mfs_base#1, ssb.line8#4, ssb.line9:positive, ssb.mfs_adjust#1, ssb.line10#4, ssb.line11:positive, ssb.line12:right, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:right, ssb.line18#1

### classm.ssb.5 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $296,744.00

### classm.ssb.5 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $296,744.00

### classm.ssb.5 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 
Status: **AGREE**

Value: $296,744.00

### classm.ssb.5 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.5 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 
Status: **AGREE**

Value: $271,744.00

### classm.ssb.5 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **AGREE**

Value: $9,000.00

### classm.ssb.5 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

Value: $262,744.00

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

Value: $223,332.40

### classm.ssb.5 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $223,332.40

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
    work: "Total of box 5 from all Forms SSA-1099 and RRB-1099 = 0.00"
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
    work: "Schedule 1 lines 11 and 13 = 0 + 0; no other lines given = 0.00"
  - printed: "7"
    value: "32936.00"
    work: "0.00 < 32936.00, so yes: 32936.00 - 0.00 = 32936.00"
  - printed: "8"
    value: "25000.00"
    work: "Head of household = 25000.00"
  - printed: "9"
    value: "7936.00"
    work: "25000.00 < 32936.00, so yes: 32936.00 - 25000.00 = 7936.00"
  - printed: "10"
    value: "9000.00"
    work: "Head of household = 9000.00"
  - printed: "11"
    value: "0.00"
    work: "7936.00 - 9000.00 is less than zero, so enter 0"
  - printed: "12"
    value: "7936.00"
    work: "smaller of 7936.00 and 9000.00 = 7936.00"
  - printed: "13"
    value: "3968.00"
    work: "7936.00 / 2 = 3968.00"
  - printed: "14"
    value: "0.00"
    work: "smaller of 0.00 and 3968.00 = 0.00"
  - printed: "15"
    value: "0.00"
    work: "Line 11 is zero, so enter 0"
  - printed: "16"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "smaller of 0.00 and 0.00 = 0.00"
```

### classm.ssb.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "42441.00"
    work: "Total of box 5 of Forms SSA-1099/RRB-1099 = 42,441.00"
  - printed: "2"
    value: "21220.50"
    work: "42,441.00 x 0.50 = 21,220.50"
  - printed: "3"
    value: "120076.00"
    work: "0 + 32,491 + 34,074 + 0 + 33,511 + 20,000 + 0 = 120,076.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "141296.50"
    work: "21,220.50 + 120,076.00 + 0.00 = 141,296.50"
  - printed: "6"
    value: "6212.00"
    work: "Sch 1 line 11 (0) + line 13 HSA (6,212); no other amounts given = 6,212.00"
  - printed: "7"
    value: "135084.50"
    work: "6,212.00 < 141,296.50, yes; 141,296.50 - 6,212.00 = 135,084.50"
  - printed: "8"
    value: "25000.00"
    work: "Single filer, enter $25,000"
  - printed: "9"
    value: "110084.50"
    work: "25,000 < 135,084.50, yes; 135,084.50 - 25,000.00 = 110,084.50"
  - printed: "10"
    value: "9000.00"
    work: "Single filer, enter $9,000"
  - printed: "11"
    value: "101084.50"
    work: "110,084.50 - 9,000.00 = 101,084.50"
  - printed: "12"
    value: "9000.00"
    work: "smaller of 110,084.50 or 9,000.00 = 9,000.00"
  - printed: "13"
    value: "4500.00"
    work: "9,000.00 / 2 = 4,500.00"
  - printed: "14"
    value: "4500.00"
    work: "smaller of 21,220.50 or 4,500.00 = 4,500.00"
  - printed: "15"
    value: "85921.83"
    work: "101,084.50 x 0.85 = 85,921.825, rounded to 85,921.83"
  - printed: "16"
    value: "90421.83"
    work: "4,500.00 + 85,921.83 = 90,421.83"
  - printed: "17"
    value: "36074.85"
    work: "42,441.00 x 0.85 = 36,074.85"
  - printed: "18"
    value: "36074.85"
    work: "smaller of 90,421.83 or 36,074.85 = 36,074.85"
```
```

### classm.ssb.3

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
    value: "-1500.00"
    work: "0 + 0 + 0 + 0 + 0 + (-1500.00) + 0 = -1500.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "-1500.00"
    work: "0.00 + (-1500.00) + 0.00 = -1500.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11 (0) + 13 (0); no other adjustments given = 0.00"
  - printed: "7"
    value: "blank"
    work: "Is 0.00 less than -1500.00? No. STOP: none of the benefits are taxable, so enter -0- on Form 1040 line 6b."
  - printed: "8"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "9"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "10"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "11"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "12"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "13"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "14"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "15"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "16"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "17"
    value: "blank"
    work: "Not reached; the worksheet stopped at line 7."
  - printed: "18"
    value: "blank"
    work: "Not reached; the line 7 STOP puts -0- on Form 1040 line 6b."
```
```

### classm.ssb.4

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
    work: "Schedule 1 line 11 (0) + line 13 (0); no other lines 11-20, 23 or 25 given = 0.00"
  - printed: "7"
    value: "6724.00"
    work: "Line 6 (0) is less than line 5, so Yes: 6724.00 - 0.00 = 6724.00"
  - printed: "8"
    value: "32000.00"
    work: "Married filing jointly = $32,000"
  - printed: "9"
    value: "blank"
    work: "Line 8 (32000) is not less than line 7 (6724), so No: STOP; none taxable; enter -0- on Form 1040 line 6b"
  - printed: "10"
    value: "blank"
    work: "Skipped; STOP at line 9"
  - printed: "11"
    value: "blank"
    work: "Skipped; STOP at line 9"
  - printed: "12"
    value: "blank"
    work: "Skipped; STOP at line 9"
  - printed: "13"
    value: "blank"
    work: "Skipped; STOP at line 9"
  - printed: "14"
    value: "blank"
    work: "Skipped; STOP at line 9"
  - printed: "15"
    value: "blank"
    work: "Skipped; STOP at line 9"
  - printed: "16"
    value: "blank"
    work: "Skipped; STOP at line 9"
  - printed: "17"
    value: "blank"
    work: "Skipped; STOP at line 9"
  - printed: "18"
    value: "blank"
    work: "Skipped; STOP at line 9 (Form 1040 line 6b = -0-)"
```
```

### classm.ssb.5

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
    value: "296744.00"
    work: "95263 + 30279 + 0 + 30819 + 42671 + 97712 + 0 = 296744.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "296744.00"
    work: "0.00 + 296744.00 + 0.00 = 296744.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11 (0) + 13 (0); no other amounts given = 0.00"
  - printed: "7"
    value: "296744.00"
    work: "Line 6 (0) < line 5, so yes: 296744.00 - 0.00 = 296744.00"
  - printed: "8"
    value: "25000.00"
    work: "Qualifying surviving spouse enters 25000.00"
  - printed: "9"
    value: "271744.00"
    work: "Line 8 < line 7, so yes: 296744.00 - 25000.00 = 271744.00"
  - printed: "10"
    value: "9000.00"
    work: "Qualifying surviving spouse enters 9000.00"
  - printed: "11"
    value: "262744.00"
    work: "271744.00 - 9000.00 = 262744.00"
  - printed: "12"
    value: "9000.00"
    work: "smaller of 271744.00 or 9000.00 = 9000.00"
  - printed: "13"
    value: "4500.00"
    work: "9000.00 / 2 = 4500.00"
  - printed: "14"
    value: "0.00"
    work: "smaller of line 2 (0.00) or line 13 (4500.00) = 0.00"
  - printed: "15"
    value: "223332.40"
    work: "262744.00 x 0.85 = 223332.40"
  - printed: "16"
    value: "223332.40"
    work: "0.00 + 223332.40 = 223332.40"
  - printed: "17"
    value: "0.00"
    work: "0.00 x 0.85 = 0.00"
  - printed: "18"
    value: "0.00"
    work: "smaller of 223332.40 or 0.00 = 0.00"
```
```
