# Class M hand-work — clcw26

`Capital loss carryover to 2026 (Capital Loss Carryover Worksheet applied to this return)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 24b33847a6a97a592abe2f1ba98b8a16535dac13d464c4283802abe8f7584582 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 10, 14 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 14 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 103 | cited pages | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | - | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### case classm.clcw26.1 — prompt sha256 01afbde329c269cdd7224778076a5503f764fd189b3792171d1292056c777c92; branches: clcw26.show:false, clcw26.show_st:false, clcw26.show_lt:false, clcw26.line2:floor, clcw26.line3:positive, clcw26.line4:left, clcw26.line5:floor, clcw26.line6:floor, clcw26.line8:floor, clcw26.line9:floor, clcw26.line10:floor, clcw26.line11:floor, clcw26.line13:floor, clcw26.decedent_notice:false

### classm.clcw26.1 — 1 — Form 1040 line 15 for 2025, negative if it would have been a loss (line 11b less
Status: **AGREE**

Value: $89,629.10

### classm.clcw26.1 — 2 — The loss on Schedule D line 21, as a positive amount
Status: **AGREE**

Value: $0.00

### classm.clcw26.1 — 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

Value: $89,629.10

### classm.clcw26.1 — 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

Value: $0.00

### classm.clcw26.1 — 5 — The loss on Schedule D line 7, as a positive amount (zero if line 7 is not a los
Status: **AGREE**

Value: $0.00

### classm.clcw26.1 — 6 — Any gain on Schedule D line 15. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped because line 7 is not a loss (go to line 9)

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.1 — 7 — Add lines 4 and 6
Status: **SKIPPED**

Model: blank
Work: Skipped because line 7 is not a loss (go to line 9)

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.1 — 8 — Short-term capital loss carryover to 2026. Subtract line 7 from line 5. If zero
Status: **SKIPPED**

Model: blank
Work: Skipped because line 7 is not a loss (go to line 9); no short-term carryover

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.1 — 9 — The loss on Schedule D line 15, as a positive amount
Status: **SKIPPED**

Model: blank
Work: Schedule D line 15 is 0.00, not a loss, so skip lines 9 through 13

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.1 — 10 — Any gain on Schedule D line 7. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped because line 15 is not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.1 — 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped because line 15 is not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.1 — 12 — Add lines 10 and 11
Status: **SKIPPED**

Model: blank
Work: Skipped because line 15 is not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.1 — 13 — Long-term capital loss carryover to 2026. Subtract line 12 from line 9. If zero
Status: **SKIPPED**

Model: blank
Work: Skipped because line 15 is not a loss; no long-term carryover

No numeric assertion or class M credit: the model left this line blank.

### case classm.clcw26.2 — prompt sha256 42d0600d38d48b0403a0189c60741161bc6432cb62a815c7135c7e511cb3441d; branches: clcw26.show:true, clcw26.show_st:true, clcw26.show_lt:true, clcw26.line2:positive, clcw26.line3:floor, clcw26.line4:right, clcw26.line5:positive, clcw26.line6:floor, clcw26.line8:positive, clcw26.line9:positive, clcw26.line10:floor, clcw26.line11:floor, clcw26.line13:positive, clcw26.decedent_notice:true

### classm.clcw26.2 — 1 — Form 1040 line 15 for 2025, negative if it would have been a loss (line 11b less
Status: **AGREE**

Value: $-75,840.35

### classm.clcw26.2 — 2 — The loss on Schedule D line 21, as a positive amount
Status: **AGREE**

Value: $3,000.00

### classm.clcw26.2 — 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.clcw26.2 — 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

Value: $0.00

### classm.clcw26.2 — 5 — The loss on Schedule D line 7, as a positive amount (zero if line 7 is not a los
Status: **AGREE**

Value: $10,701.00

### classm.clcw26.2 — 6 — Any gain on Schedule D line 15. If a loss, enter -0-
Status: **AGREE**

Value: $0.00

### classm.clcw26.2 — 7 — Add lines 4 and 6
Status: **AGREE**

Value: $0.00

### classm.clcw26.2 — 8 — Short-term capital loss carryover to 2026. Subtract line 7 from line 5. If zero
Status: **AGREE**

Value: $10,701.00

### classm.clcw26.2 — 9 — The loss on Schedule D line 15, as a positive amount
Status: **AGREE**

Value: $31,437.00

### classm.clcw26.2 — 10 — Any gain on Schedule D line 7. If a loss, enter -0-
Status: **AGREE**

Value: $0.00

### classm.clcw26.2 — 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.clcw26.2 — 12 — Add lines 10 and 11
Status: **AGREE**

Value: $0.00

### classm.clcw26.2 — 13 — Long-term capital loss carryover to 2026. Subtract line 12 from line 9. If zero
Status: **AGREE**

Value: $31,437.00

### case classm.clcw26.3 — prompt sha256 2a87ee3985a42e773d519817bd0b51b2dbc64b155a98337d968e1e1c052d7f95; branches: clcw26.show:false, clcw26.show_st:false, clcw26.show_lt:false, clcw26.line2:floor, clcw26.line3:positive, clcw26.line4:left, clcw26.line5:floor, clcw26.line6:positive, clcw26.line8:floor, clcw26.line9:floor, clcw26.line10:positive, clcw26.line11:floor, clcw26.line13:floor, clcw26.decedent_notice:false

### classm.clcw26.3 — 1 — Form 1040 line 15 for 2025, negative if it would have been a loss (line 11b less
Status: **AGREE**

Value: $29,527.00

### classm.clcw26.3 — 2 — The loss on Schedule D line 21, as a positive amount
Status: **AGREE**

Value: $0.00

### classm.clcw26.3 — 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

Value: $29,527.00

### classm.clcw26.3 — 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

Value: $0.00

### classm.clcw26.3 — 5 — The loss on Schedule D line 7, as a positive amount (zero if line 7 is not a los
Status: **AGREE**

Value: $0.00

### classm.clcw26.3 — 6 — Any gain on Schedule D line 15. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped: line 7 was not a loss, so go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.3 — 7 — Add lines 4 and 6
Status: **SKIPPED**

Model: blank
Work: Skipped: line 7 was not a loss, so go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.3 — 8 — Short-term capital loss carryover to 2026. Subtract line 7 from line 5. If zero
Status: **SKIPPED**

Model: blank
Work: Skipped: line 7 was not a loss, so go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.3 — 9 — The loss on Schedule D line 15, as a positive amount
Status: **SKIPPED**

Model: blank
Work: Schedule D line 15 is a gain of 17,081.00, not a loss; skip lines 9 through 13

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.3 — 10 — Any gain on Schedule D line 7. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped: line 15 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.3 — 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped: line 15 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.3 — 12 — Add lines 10 and 11
Status: **SKIPPED**

Model: blank
Work: Skipped: line 15 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.3 — 13 — Long-term capital loss carryover to 2026. Subtract line 12 from line 9. If zero
Status: **SKIPPED**

Model: blank
Work: Skipped: line 15 was not a loss

No numeric assertion or class M credit: the model left this line blank.

### case classm.clcw26.4 — prompt sha256 d21e1cf5d3cab04a8976da99fa12f98e29492b6578a40f26948dcdaf0e278529; branches: clcw26.show:true, clcw26.show_st:false, clcw26.show_lt:true, clcw26.line2:positive, clcw26.line3:positive, clcw26.line4:left, clcw26.line5:floor, clcw26.line6:floor, clcw26.line8:floor, clcw26.line9:positive, clcw26.line10:floor, clcw26.line11:positive, clcw26.line13:positive, clcw26.decedent_notice:false

### classm.clcw26.4 — 1 — Form 1040 line 15 for 2025, negative if it would have been a loss (line 11b less
Status: **AGREE**

Value: $146,038.00

### classm.clcw26.4 — 2 — The loss on Schedule D line 21, as a positive amount
Status: **AGREE**

Value: $3,000.00

### classm.clcw26.4 — 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

Value: $149,038.00

### classm.clcw26.4 — 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

Value: $3,000.00

### classm.clcw26.4 — 5 — The loss on Schedule D line 7, as a positive amount (zero if line 7 is not a los
Status: **AGREE**

Value: $0.00

### classm.clcw26.4 — 6 — Any gain on Schedule D line 15. If a loss, enter -0-
Status: **SKIPPED**

Model: blank
Work: Skipped: line 7 is not a loss, so go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.4 — 7 — Add lines 4 and 6
Status: **SKIPPED**

Model: blank
Work: Skipped: line 7 is not a loss, so go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.4 — 8 — Short-term capital loss carryover to 2026. Subtract line 7 from line 5. If zero
Status: **SKIPPED**

Model: blank
Work: Skipped: line 7 is not a loss, so go to line 9

No numeric assertion or class M credit: the model left this line blank.

### classm.clcw26.4 — 9 — The loss on Schedule D line 15, as a positive amount
Status: **AGREE**

Value: $7,280.00

### classm.clcw26.4 — 10 — Any gain on Schedule D line 7. If a loss, enter -0-
Status: **AGREE**

Value: $0.00

### classm.clcw26.4 — 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **AGREE**

Value: $3,000.00

### classm.clcw26.4 — 12 — Add lines 10 and 11
Status: **AGREE**

Value: $3,000.00

### classm.clcw26.4 — 13 — Long-term capital loss carryover to 2026. Subtract line 12 from line 9. If zero
Status: **AGREE**

Value: $4,280.00

## Raw responses

### classm.clcw26.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "89629.10"
    work: "Line 11b 168,227.38 − line 14 78,598.28 = 89,629.10"
  - printed: "2"
    value: "0.00"
    work: "Schedule D line 21 is 0.00, so there is no loss; enter 0"
  - printed: "3"
    value: "89629.10"
    work: "89,629.10 + 0.00 = 89,629.10"
  - printed: "4"
    value: "0.00"
    work: "Smaller of line 2 (0.00) or line 3 (89,629.10) = 0.00"
  - printed: "5"
    value: "0.00"
    work: "Schedule D line 7 is 0.00, not a loss, so enter -0- and go to line 9"
  - printed: "6"
    value: "blank"
    work: "Skipped because line 7 is not a loss (go to line 9)"
  - printed: "7"
    value: "blank"
    work: "Skipped because line 7 is not a loss (go to line 9)"
  - printed: "8"
    value: "blank"
    work: "Skipped because line 7 is not a loss (go to line 9); no short-term carryover"
  - printed: "9"
    value: "blank"
    work: "Schedule D line 15 is 0.00, not a loss, so skip lines 9 through 13"
  - printed: "10"
    value: "blank"
    work: "Skipped because line 15 is not a loss"
  - printed: "11"
    value: "blank"
    work: "Skipped because line 15 is not a loss"
  - printed: "12"
    value: "blank"
    work: "Skipped because line 15 is not a loss"
  - printed: "13"
    value: "blank"
    work: "Skipped because line 15 is not a loss; no long-term carryover"
```
```

### classm.clcw26.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "-75840.35"
    work: "1,302.00 - 77,142.35 = -75,840.35 (loss)"
  - printed: "2"
    value: "3000.00"
    work: "Schedule D line 21 loss -3,000.00 as positive"
  - printed: "3"
    value: "0.00"
    work: "-75,840.35 + 3,000.00 = -72,840.35; zero or less, enter -0-"
  - printed: "4"
    value: "0.00"
    work: "smaller of 3,000.00 or 0.00"
  - printed: "5"
    value: "10701.00"
    work: "Schedule D line 7 loss -10,701.00 as positive"
  - printed: "6"
    value: "0.00"
    work: "Schedule D line 15 is a loss (-31,437.00); enter -0-"
  - printed: "7"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "8"
    value: "10701.00"
    work: "10,701.00 - 0.00"
  - printed: "9"
    value: "31437.00"
    work: "Schedule D line 15 loss -31,437.00 as positive"
  - printed: "10"
    value: "0.00"
    work: "Schedule D line 7 is a loss; enter -0-"
  - printed: "11"
    value: "0.00"
    work: "0.00 - 10,701.00 = -10,701.00; zero or less, enter -0-"
  - printed: "12"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "13"
    value: "31437.00"
    work: "31,437.00 - 0.00"
```
```

### classm.clcw26.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "29527.00"
    work: "Line 11b 51,731.00 - line 14 22,204.00 = 29,527.00"
  - printed: "2"
    value: "0.00"
    work: "Schedule D line 21 is 0.00, so no loss to enter"
  - printed: "3"
    value: "29527.00"
    work: "29,527.00 + 0.00 = 29,527.00"
  - printed: "4"
    value: "0.00"
    work: "Smaller of line 2 (0.00) or line 3 (29,527.00) = 0.00"
  - printed: "5"
    value: "0.00"
    work: "Schedule D line 7 is a gain of 34,650.00, not a loss; enter -0- and go to line 9"
  - printed: "6"
    value: "blank"
    work: "Skipped: line 7 was not a loss, so go to line 9"
  - printed: "7"
    value: "blank"
    work: "Skipped: line 7 was not a loss, so go to line 9"
  - printed: "8"
    value: "blank"
    work: "Skipped: line 7 was not a loss, so go to line 9"
  - printed: "9"
    value: "blank"
    work: "Schedule D line 15 is a gain of 17,081.00, not a loss; skip lines 9 through 13"
  - printed: "10"
    value: "blank"
    work: "Skipped: line 15 was not a loss"
  - printed: "11"
    value: "blank"
    work: "Skipped: line 15 was not a loss"
  - printed: "12"
    value: "blank"
    work: "Skipped: line 15 was not a loss"
  - printed: "13"
    value: "blank"
    work: "Skipped: line 15 was not a loss"
```
```

### classm.clcw26.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "146038.00"
    work: "Line 11b 182,881.00 - line 14 36,843.00 = 146,038.00"
  - printed: "2"
    value: "3000.00"
    work: "Schedule D line 21 loss (3,000.00) entered as a positive amount"
  - printed: "3"
    value: "149038.00"
    work: "146,038.00 + 3,000.00 = 149,038.00"
  - printed: "4"
    value: "3000.00"
    work: "Smaller of line 2 (3,000.00) or line 3 (149,038.00)"
  - printed: "5"
    value: "0.00"
    work: "Schedule D line 7 is 0.00, not a loss; enter -0- on line 5 and go to line 9"
  - printed: "6"
    value: "blank"
    work: "Skipped: line 7 is not a loss, so go to line 9"
  - printed: "7"
    value: "blank"
    work: "Skipped: line 7 is not a loss, so go to line 9"
  - printed: "8"
    value: "blank"
    work: "Skipped: line 7 is not a loss, so go to line 9"
  - printed: "9"
    value: "7280.00"
    work: "Schedule D line 15 loss (7,280.00) entered as a positive amount"
  - printed: "10"
    value: "0.00"
    work: "Schedule D line 7 has no gain (0.00)"
  - printed: "11"
    value: "3000.00"
    work: "3,000.00 - 0.00 = 3,000.00"
  - printed: "12"
    value: "3000.00"
    work: "0.00 + 3,000.00 = 3,000.00"
  - printed: "13"
    value: "4280.00"
    work: "7,280.00 - 3,000.00 = 4,280.00"
```
```
