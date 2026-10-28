# Class M hand-work — clcw

`Capital Loss Carryover Worksheet—Lines 6 and 14` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | fe610ac4e461e2dec11059115dd080efe9cbcccf8541221b0a05879ec2520fad |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 3, 10 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 3 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 102, 103 | cited pages | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | - | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### case classm.clcw.1 — prompt sha256 f76393f6cdd691de4d65e587777624ca599a4de127756406f6f32e57da1f7d39; branches: clcw.spouse_screen:false, clcw.prior_loss:floor, clcw.prior_floor:left, clcw.bad:false, clcw.applies:false, clcw.show_st:false, clcw.show_lt:false, clcw.line3:floor, clcw.line4:left, clcw.st_loss:false, clcw.lt_loss:false, clcw.line5:floor, clcw.line6:floor, clcw.line8:floor, clcw.line9:floor, clcw.line10:floor, clcw.line11:floor, clcw.line13:floor, clcw.figures_notice:false

### classm.clcw.1 — 1 — Your 2024 taxable income (2024 Form 1040 line 15), negative if it would have bee
Status: **SKIPPED**

Model: blank
Work: 2024 Sch D line 21 was not a loss, so the worksheet is not used and there are no carryovers

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 2 — Enter the loss from your 2024 Schedule D, line 21, as a positive amount
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 4 — Enter the smaller of line 2 or line 3
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 5 — Enter the loss from your 2024 Schedule D, line 7, as a positive amount (zero if
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 6 — Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 7 — Add lines 4 and 6
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 8 — Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero
Status: **SKIPPED**

Model: blank
Work: No short-term carryover; nothing goes to 2025 Sch D line 6

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 9 — Enter the loss from your 2024 Schedule D, line 15, as a positive amount
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 10 — Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 12 — Add lines 10 and 11
Status: **SKIPPED**

Model: blank
Work: Worksheet not used: 2024 Sch D line 21 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.1 — 13 — Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero
Status: **SKIPPED**

Model: blank
Work: No long-term carryover; nothing goes to 2025 Sch D line 14

No numeric assertion or class M credit: the model left this line blank.

### case classm.clcw.2 — prompt sha256 e8b4709e5e2e5ee4f628ab970d5a6859df9c02aeeecc691c34c415c1e7f018a1; branches: clcw.spouse_screen:false, clcw.prior_loss:positive, clcw.prior_floor:right, clcw.bad:false, clcw.applies:true, clcw.show_st:true, clcw.show_lt:true, clcw.line3:positive, clcw.line4:right, clcw.st_loss:true, clcw.lt_loss:true, clcw.line5:positive, clcw.line6:floor, clcw.line8:positive, clcw.line9:positive, clcw.line10:floor, clcw.line11:floor, clcw.line13:positive, clcw.figures_notice:true

### classm.clcw.2 — 1 — Your 2024 taxable income (2024 Form 1040 line 15), negative if it would have bee
Status: **AGREE**

Value: $-1,004.00

### classm.clcw.2 — 2 — Enter the loss from your 2024 Schedule D, line 21, as a positive amount
Status: **AGREE**

Value: $3,000.00

### classm.clcw.2 — 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

Value: $1,996.00

### classm.clcw.2 — 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

Value: $1,996.00

### classm.clcw.2 — 5 — Enter the loss from your 2024 Schedule D, line 7, as a positive amount (zero if
Status: **AGREE**

Value: $26,622.00

### classm.clcw.2 — 6 — Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-
Status: **AGREE**

Value: $0.00

### classm.clcw.2 — 7 — Add lines 4 and 6
Status: **AGREE**

Value: $1,996.00

### classm.clcw.2 — 8 — Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero
Status: **AGREE**

Value: $24,626.00

### classm.clcw.2 — 9 — Enter the loss from your 2024 Schedule D, line 15, as a positive amount
Status: **AGREE**

Value: $9,376.00

### classm.clcw.2 — 10 — Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-
Status: **AGREE**

Value: $0.00

### classm.clcw.2 — 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.clcw.2 — 12 — Add lines 10 and 11
Status: **AGREE**

Value: $0.00

### classm.clcw.2 — 13 — Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero
Status: **AGREE**

Value: $9,376.00

### case classm.clcw.3 — prompt sha256 0494d8fd77d226c302b02ecdf98307abb09c38bbbe6d3dea1793b34b0e90032f; branches: clcw.spouse_screen:false, clcw.prior_loss:positive, clcw.prior_floor:right, clcw.bad:false, clcw.applies:true, clcw.show_st:false, clcw.show_lt:true, clcw.line3:positive, clcw.line4:left, clcw.st_loss:false, clcw.lt_loss:true, clcw.line5:floor, clcw.line6:floor, clcw.line8:floor, clcw.line9:positive, clcw.line10:positive, clcw.line11:positive, clcw.line13:positive, clcw.figures_notice:true

### classm.clcw.3 — 1 — Your 2024 taxable income (2024 Form 1040 line 15), negative if it would have bee
Status: **AGREE**

Value: $7,550.00

### classm.clcw.3 — 2 — Enter the loss from your 2024 Schedule D, line 21, as a positive amount
Status: **AGREE**

Value: $3,000.00

### classm.clcw.3 — 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

Value: $10,550.00

### classm.clcw.3 — 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

Value: $3,000.00

### classm.clcw.3 — 5 — Enter the loss from your 2024 Schedule D, line 7, as a positive amount (zero if
Status: **AGREE**

Value: $0.00

### classm.clcw.3 — 6 — Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: skipped: line 5 instruction says go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.3 — 7 — Add lines 4 and 6
Status: **SKIPPED**

Model: blank
Work: skipped: line 5 instruction says go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.3 — 8 — Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero
Status: **SKIPPED**

Model: blank
Work: skipped: line 5 instruction says go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.3 — 9 — Enter the loss from your 2024 Schedule D, line 15, as a positive amount
Status: **AGREE**

Value: $6,991.00

### classm.clcw.3 — 10 — Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-
Status: **AGREE**

Value: $1,775.00

### classm.clcw.3 — 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **AGREE**

Value: $3,000.00

### classm.clcw.3 — 12 — Add lines 10 and 11
Status: **AGREE**

Value: $4,775.00

### classm.clcw.3 — 13 — Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero
Status: **AGREE**

Value: $2,216.00

### case classm.clcw.4 — prompt sha256 eb546c275c264dac6f7a1218662c40d866da4efed399e5821da7ace301e53abf; branches: clcw.spouse_screen:false, clcw.prior_loss:positive, clcw.prior_floor:right, clcw.bad:false, clcw.applies:true, clcw.show_st:true, clcw.show_lt:false, clcw.line3:positive, clcw.line4:left, clcw.st_loss:true, clcw.lt_loss:false, clcw.line5:positive, clcw.line6:positive, clcw.line8:positive, clcw.line9:floor, clcw.line10:floor, clcw.line11:floor, clcw.line13:floor, clcw.figures_notice:true

### classm.clcw.4 — 1 — Your 2024 taxable income (2024 Form 1040 line 15), negative if it would have bee
Status: **AGREE**

Value: $34,346.00

### classm.clcw.4 — 2 — Enter the loss from your 2024 Schedule D, line 21, as a positive amount
Status: **AGREE**

Value: $3,000.00

### classm.clcw.4 — 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

Value: $37,346.00

### classm.clcw.4 — 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

Value: $3,000.00

### classm.clcw.4 — 5 — Enter the loss from your 2024 Schedule D, line 7, as a positive amount (zero if
Status: **AGREE**

Value: $13,209.00

### classm.clcw.4 — 6 — Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-
Status: **AGREE**

Value: $3,808.00

### classm.clcw.4 — 7 — Add lines 4 and 6
Status: **AGREE**

Value: $6,808.00

### classm.clcw.4 — 8 — Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero
Status: **AGREE**

Value: $6,401.00

### classm.clcw.4 — 9 — Enter the loss from your 2024 Schedule D, line 15, as a positive amount
Status: **SKIPPED**

Model: blank
Work: 2024 Schedule D line 15 is not a loss, so skip lines 9 through 13

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.4 — 10 — Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped because 2024 Schedule D line 15 is not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.4 — 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped because 2024 Schedule D line 15 is not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.4 — 12 — Add lines 10 and 11
Status: **SKIPPED**

Model: blank
Work: Skipped because 2024 Schedule D line 15 is not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw.4 — 13 — Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero
Status: **SKIPPED**

Model: blank
Work: Skipped because 2024 Schedule D line 15 is not a loss

No numeric assertion or class M credit: the model left this line blank.

## Raw responses

### classm.clcw.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "2024 Sch D line 21 was not a loss, so the worksheet is not used and there are no carryovers"
  - printed: "2"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "3"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "4"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "5"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "6"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "7"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "8"
    value: "blank"
    work: "No short-term carryover; nothing goes to 2025 Sch D line 6"
  - printed: "9"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "10"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "11"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "12"
    value: "blank"
    work: "Worksheet not used: 2024 Sch D line 21 was not a loss"
  - printed: "13"
    value: "blank"
    work: "No long-term carryover; nothing goes to 2025 Sch D line 14"
```
```

### classm.clcw.2

```yaml
lines:
  - printed: "1"
    value: "-1004.00"
    work: "2024 line 11 14,602.00 - line 14 15,606.00 = (1,004.00)"
  - printed: "2"
    value: "3000.00"
    work: "2024 Schedule D line 21 loss as positive = 3,000.00"
  - printed: "3"
    value: "1996.00"
    work: "-1,004.00 + 3,000.00 = 1,996.00"
  - printed: "4"
    value: "1996.00"
    work: "smaller of 3,000.00 or 1,996.00 = 1,996.00"
  - printed: "5"
    value: "26622.00"
    work: "2024 Schedule D line 7 is a loss; 26,622.00 as positive"
  - printed: "6"
    value: "0.00"
    work: "2024 Schedule D line 15 is a loss, so enter -0-"
  - printed: "7"
    value: "1996.00"
    work: "1,996.00 + 0.00 = 1,996.00"
  - printed: "8"
    value: "24626.00"
    work: "26,622.00 - 1,996.00 = 24,626.00"
  - printed: "9"
    value: "9376.00"
    work: "2024 Schedule D line 15 is a loss; 9,376.00 as positive"
  - printed: "10"
    value: "0.00"
    work: "2024 Schedule D line 7 is a loss, so enter -0-"
  - printed: "11"
    value: "0.00"
    work: "1,996.00 - 26,622.00 is less than zero, so enter -0-"
  - printed: "12"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "13"
    value: "9376.00"
    work: "9,376.00 - 0.00 = 9,376.00"
```

### classm.clcw.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "7550.00"
    work: "2024 taxable income = 2024 Form 1040 line 11 30,548.00 - line 14 22,998.00 = 7,550.00"
  - printed: "2"
    value: "3000.00"
    work: "Loss from 2024 Schedule D line 21 as a positive amount"
  - printed: "3"
    value: "10550.00"
    work: "7,550.00 + 3,000.00 = 10,550.00"
  - printed: "4"
    value: "3000.00"
    work: "smaller of line 2 (3,000.00) or line 3 (10,550.00)"
  - printed: "5"
    value: "0.00"
    work: "2024 Schedule D line 7 is a gain (1,775.00), not a loss: enter -0- and go to line 9"
  - printed: "6"
    value: "blank"
    work: "skipped: line 5 instruction says go to line 9"
  - printed: "7"
    value: "blank"
    work: "skipped: line 5 instruction says go to line 9"
  - printed: "8"
    value: "blank"
    work: "skipped: line 5 instruction says go to line 9"
  - printed: "9"
    value: "6991.00"
    work: "2024 Schedule D line 15 is a loss; enter it as a positive amount"
  - printed: "10"
    value: "1775.00"
    work: "gain on 2024 Schedule D line 7"
  - printed: "11"
    value: "3000.00"
    work: "3,000.00 - 0.00 = 3,000.00"
  - printed: "12"
    value: "4775.00"
    work: "1,775.00 + 3,000.00 = 4,775.00"
  - printed: "13"
    value: "2216.00"
    work: "6,991.00 - 4,775.00 = 2,216.00"
```
```

### classm.clcw.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "34346.00"
    work: "2024 Form 1040 line 11 minus line 14: 58,924.00 - 24,578.00 = 34,346.00"
  - printed: "2"
    value: "3000.00"
    work: "2024 Schedule D line 21 loss as a positive amount = 3,000.00"
  - printed: "3"
    value: "37346.00"
    work: "Line 1 + line 2: 34,346.00 + 3,000.00 = 37,346.00"
  - printed: "4"
    value: "3000.00"
    work: "Smaller of line 2 (3,000.00) or line 3 (37,346.00) = 3,000.00"
  - printed: "5"
    value: "13209.00"
    work: "2024 Schedule D line 7 is a loss; enter it as a positive amount = 13,209.00"
  - printed: "6"
    value: "3808.00"
    work: "2024 Schedule D line 15 is a gain of 3,808.00"
  - printed: "7"
    value: "6808.00"
    work: "Line 4 + line 6: 3,000.00 + 3,808.00 = 6,808.00"
  - printed: "8"
    value: "6401.00"
    work: "Line 5 - line 7: 13,209.00 - 6,808.00 = 6,401.00 (short-term carryover)"
  - printed: "9"
    value: "blank"
    work: "2024 Schedule D line 15 is not a loss, so skip lines 9 through 13"
  - printed: "10"
    value: "blank"
    work: "Skipped because 2024 Schedule D line 15 is not a loss"
  - printed: "11"
    value: "blank"
    work: "Skipped because 2024 Schedule D line 15 is not a loss"
  - printed: "12"
    value: "blank"
    work: "Skipped because 2024 Schedule D line 15 is not a loss"
  - printed: "13"
    value: "blank"
    work: "Skipped because 2024 Schedule D line 15 is not a loss"
```
```
