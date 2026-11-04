# Class M hand-work — ssb

`Social Security Benefits Worksheet—Lines 6a and 6b` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 83c9e2ecf55d424847f47f84f524fb02eb52b8a67390436a142cfb1fd395b341 |
| cases | 5 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.ssb.1 — prompt sha256 fb4fb82c966fb579e5e75bf513b6eea7e233d6ae0c7b558bf9ebee64951179ef; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.has_benefits:false, ssb.line7:positive, ssb.lines8_to_15:true, ssb.line8#3, ssb.line9:positive, ssb.line10#3, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

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

### case classm.ssb.2 — prompt sha256 a73434e6d91a1c22a10ff68c265559c4a66675d99a60703053797aa6c14d0664; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.lived_apart:false, ssb.has_benefits:true, ssb.line7:positive, ssb.mfs_base#1, ssb.lines8_to_15:false, ssb.line8#2, ssb.line9:positive, ssb.mfs_adjust#1, ssb.line10#2, ssb.line11:positive, ssb.line12:right, ssb.line14:right, ssb.mfs_together:true, ssb.line16#0, ssb.line18_figured:right, ssb.line18#0

### classm.ssb.2 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $46,220.00

### classm.ssb.2 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $23,110.00

### classm.ssb.2 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $116,775.00

### classm.ssb.2 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $139,885.00

### classm.ssb.2 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.ssb.2 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **AGREE**

Value: $139,885.00

### classm.ssb.2 — 16 — Add lines 14 and 15
Status: **AGREE**

Value: $118,902.25

### classm.ssb.2 — 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

Value: $39,287.00

### classm.ssb.2 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $39,287.00

### case classm.ssb.3 — prompt sha256 665fcb8a6819197f23a8f1a9fb2bf5570b7261d15e49c3e6ad6cb4f2a4c6c8ad; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.has_benefits:false, ssb.line7:positive, ssb.lines8_to_15:true, ssb.line8#0, ssb.line9:floor, ssb.line10#0, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.3 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $14,269.00

### classm.ssb.3 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $14,269.00

### classm.ssb.3 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.ssb.3 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **AGREE**

Value: $14,269.00

### classm.ssb.3 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $25,000.00

### classm.ssb.3 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8
Status: **SKIPPED**

Model: blank
Work: Line 8 (25000.00) is not less than line 7 (14269.00), so no; STOP; none taxable; enter -0- on 1040 line 6b

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 12 — Enter the smaller of line 9 or line 10
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 13 — Enter one-half of line 12
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 14 — Enter the smaller of line 2 or line 13
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 16 — Add lines 14 and 15
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 17 — Multiply line 1 by 85% (0.85)
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.3 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **SKIPPED**

Model: blank
Work: Skipped; worksheet stopped at line 9 (1040 line 6b gets -0-)

No numeric assertion or class M credit: the model left this line blank.

### case classm.ssb.4 — prompt sha256 52faf555de1cf8de49ed429dc4b869e7f8e4ea403a5a2f8a66ceaa3c32fb7641; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.has_benefits:false, ssb.line7:floor, ssb.lines8_to_15:true, ssb.line8#4, ssb.line9:floor, ssb.line10#4, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.4 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $-144,709.34

### classm.ssb.4 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $-144,709.34

### classm.ssb.4 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.ssb.4 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **SKIPPED**

Model: blank
Work: Line 6 (0.00) is not less than line 5 (-144709.34), so the answer is No. STOP: none of the benefits are taxable.

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 12 — Enter the smaller of line 9 or line 10
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 13 — Enter one-half of line 12
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 14 — Enter the smaller of line 2 or line 13
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 16 — Add lines 14 and 15
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 17 — Multiply line 1 by 85% (0.85)
Status: **SKIPPED**

Model: blank
Work: Skipped because the worksheet stopped at line 7

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.4 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **AGREE**

Value: $0.00

### case classm.ssb.5 — prompt sha256 9cf2f905a17e3cfb8b38d26baf0211dc71c2a879191043234dc5be7e9f4e956a; branches: ssb.pub915:false, ssb.lump_sum:false, ssb.terror_disability:false, ssb.has_benefits:false, ssb.line7:positive, ssb.lines8_to_15:true, ssb.line8#1, ssb.line9:floor, ssb.line10#1, ssb.line11:floor, ssb.line12:left, ssb.line14:left, ssb.mfs_together:false, ssb.line16#1, ssb.line18_figured:left, ssb.line18#1

### classm.ssb.5 — 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and
Status: **AGREE**

Value: $6,574.00

### classm.ssb.5 — 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

Value: $0.00

### classm.ssb.5 — 5 — Combine lines 2, 3, and 4
Status: **AGREE**

Value: $6,574.00

### classm.ssb.5 — 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $712.50

### classm.ssb.5 — 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6
Status: **AGREE**

Value: $5,861.50

### classm.ssb.5 — 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualify
Status: **AGREE**

Value: $32,000.00

### classm.ssb.5 — 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8
Status: **SKIPPED**

Model: blank
Work: 32000.00 not less than 5861.50: STOP, none taxable; enter -0- on 1040 line 6b

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qu
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 12 — Enter the smaller of line 9 or line 10
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 13 — Enter one-half of line 12
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 14 — Enter the smaller of line 2 or line 13
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 16 — Add lines 14 and 15
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 17 — Multiply line 1 by 85% (0.85)
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.ssb.5 — 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **SKIPPED**

Model: blank
Work: Skipped, STOP at line 9; Form 1040 line 6b gets -0-

No numeric assertion or class M credit: the model left this line blank.

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
    work: "1z 32936.00 + 2b 0 + 3b 0 + 4b 0 + 5b 0 + 7a 0 + 8 0 = 32936.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "32936.00"
    work: "0.00 + 32936.00 + 0.00 = 32936.00"
  - printed: "6"
    value: "0.00"
    work: "Sch 1 lines 11-20, 23, 25 all 0 (IRA deduction 0) = 0.00"
  - printed: "7"
    value: "32936.00"
    work: "Line 6 (0) is less than line 5, so 32936.00 - 0.00 = 32936.00"
  - printed: "8"
    value: "25000.00"
    work: "Head of household, so enter $25,000"
  - printed: "9"
    value: "7936.00"
    work: "Line 8 (25000) is less than line 7, so 32936.00 - 25000.00 = 7936.00"
  - printed: "10"
    value: "9000.00"
    work: "Head of household, so enter $9,000"
  - printed: "11"
    value: "0.00"
    work: "7936.00 - 9000.00 < 0, so enter -0-"
  - printed: "12"
    value: "7936.00"
    work: "smaller of 7936.00 or 9000.00"
  - printed: "13"
    value: "3968.00"
    work: "7936.00 / 2 = 3968.00"
  - printed: "14"
    value: "0.00"
    work: "smaller of line 2 (0.00) or line 13 (3968.00)"
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
    work: "smaller of line 16 (0.00) or line 17 (0.00)"
```
```

### classm.ssb.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "46220.00"
    work: "Total of box 5 of all Forms SSA-1099/RRB-1099 = 46,220.00"
  - printed: "2"
    value: "23110.00"
    work: "46,220.00 × 0.50 = 23,110.00"
  - printed: "3"
    value: "116775.00"
    work: "14,441 + 44,289 + 31,263 + 26,782 + 0 + 0 + 0 = 116,775.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "139885.00"
    work: "23,110 + 116,775 + 0 = 139,885.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11–20, 23, 25 all 0 = 0.00"
  - printed: "7"
    value: "139885.00"
    work: "Line 6 (0) is less than line 5, so yes: 139,885 − 0 = 139,885.00"
  - printed: "16"
    value: "118902.25"
    work: "Married filing separately and lived with spouse during 2025, so skip lines 8–15: 139,885 × 0.85 = 118,902.25"
  - printed: "17"
    value: "39287.00"
    work: "46,220 × 0.85 = 39,287.00"
  - printed: "18"
    value: "39287.00"
    work: "Smaller of line 16 (118,902.25) or line 17 (39,287.00) = 39,287.00"
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
    value: "14269.00"
    work: "13937.00 + 332.00 + 0 + 0 + 0 + 0 + 0 = 14269.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "14269.00"
    work: "0.00 + 14269.00 + 0.00 = 14269.00"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25 all 0.00"
  - printed: "7"
    value: "14269.00"
    work: "Line 6 (0.00) < line 5 (14269.00), so yes; 14269.00 - 0.00 = 14269.00"
  - printed: "8"
    value: "25000.00"
    work: "Single, so enter $25,000"
  - printed: "9"
    value: ""
    work: "Line 8 (25000.00) is not less than line 7 (14269.00), so no; STOP; none taxable; enter -0- on 1040 line 6b"
  - printed: "10"
    value: ""
    work: "Skipped; worksheet stopped at line 9"
  - printed: "11"
    value: ""
    work: "Skipped; worksheet stopped at line 9"
  - printed: "12"
    value: ""
    work: "Skipped; worksheet stopped at line 9"
  - printed: "13"
    value: ""
    work: "Skipped; worksheet stopped at line 9"
  - printed: "14"
    value: ""
    work: "Skipped; worksheet stopped at line 9"
  - printed: "15"
    value: ""
    work: "Skipped; worksheet stopped at line 9"
  - printed: "16"
    value: ""
    work: "Skipped; worksheet stopped at line 9"
  - printed: "17"
    value: ""
    work: "Skipped; worksheet stopped at line 9"
  - printed: "18"
    value: ""
    work: "Skipped; worksheet stopped at line 9 (1040 line 6b gets -0-)"
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
    value: "-144709.34"
    work: "0 + 0 + 50000.00 + 0 + 0 + 0 + (-194709.34) = -144709.34"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "-144709.34"
    work: "0.00 + (-144709.34) + 0.00 = -144709.34"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25 total 0.00"
  - printed: "7"
    value: "blank"
    work: "Line 6 (0.00) is not less than line 5 (-144709.34), so the answer is No. STOP: none of the benefits are taxable."
  - printed: "8"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "9"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "10"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "11"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "12"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "13"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "14"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "15"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "16"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "17"
    value: "blank"
    work: "Skipped because the worksheet stopped at line 7"
  - printed: "18"
    value: "0.00"
    work: "The line 7 STOP says to enter -0- on Form 1040 line 6b, so taxable benefits = 0.00"
```
```

### classm.ssb.5

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
    value: "6574.00"
    work: "6574.00 + 0 + 0 + 0 + 0 + 0 + 0 = 6574.00"
  - printed: "4"
    value: "0.00"
    work: "Form 1040 line 2a = 0.00"
  - printed: "5"
    value: "6574.00"
    work: "0.00 + 6574.00 + 0.00 = 6574.00"
  - printed: "6"
    value: "712.50"
    work: "Sch 1 lines 11-20, 23, 25: 0 + 712.50 (line 13) + 0s, IRA deduction 0 = 712.50"
  - printed: "7"
    value: "5861.50"
    work: "712.50 < 6574.00, yes: 6574.00 - 712.50 = 5861.50"
  - printed: "8"
    value: "32000.00"
    work: "Married filing jointly = 32000.00"
  - printed: "9"
    value: "blank"
    work: "32000.00 not less than 5861.50: STOP, none taxable; enter -0- on 1040 line 6b"
  - printed: "10"
    value: "blank"
    work: "Skipped, STOP at line 9"
  - printed: "11"
    value: "blank"
    work: "Skipped, STOP at line 9"
  - printed: "12"
    value: "blank"
    work: "Skipped, STOP at line 9"
  - printed: "13"
    value: "blank"
    work: "Skipped, STOP at line 9"
  - printed: "14"
    value: "blank"
    work: "Skipped, STOP at line 9"
  - printed: "15"
    value: "blank"
    work: "Skipped, STOP at line 9"
  - printed: "16"
    value: "blank"
    work: "Skipped, STOP at line 9"
  - printed: "17"
    value: "blank"
    work: "Skipped, STOP at line 9"
  - printed: "18"
    value: "blank"
    work: "Skipped, STOP at line 9; Form 1040 line 6b gets -0-"
```
```
