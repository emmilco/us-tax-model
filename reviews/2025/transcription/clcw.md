# Transcription agreement — clcw

Second transcription of `Capital Loss Carryover Worksheet—Lines 6 and 14` by an isolated model (spec 6.5), compared line by line with `forms/2025/clcw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 21b913c61430d59439cc02ee9070592abf76f30ff88327cb51aa6e5ef47b7d3c |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 7708eae399f8e1c9831a179110f7e5f8c2de8801de7fd32df6c303d59126b568 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | ec566d96a73721f08704e370ce5253fb97b65362cfc30d2da46151178af4cb47 |
| printed lines compared | 13 |
| agree / disagree / missing | 13 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 3, 10 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 3 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 102, 103 | cited pages | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | - | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### 1 — Your 2024 taxable income (2024 Form 1040 line 15), negative if it would have been a loss
Status: **AGREE**

### 2 — Enter the loss from your 2024 Schedule D, line 21, as a positive amount
Status: **AGREE**

### 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

### 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

### 5 — Enter the loss from your 2024 Schedule D, line 7, as a positive amount (zero if line 7 is
Status: **AGREE**

### 6 — Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-
Status: **AGREE**

### 7 — Add lines 4 and 6
Status: **AGREE**

### 8 — Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero or less,
Status: **AGREE**

### 9 — Enter the loss from your 2024 Schedule D, line 15, as a positive amount
Status: **AGREE**

### 10 — Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-
Status: **AGREE**

### 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **AGREE**

### 12 — Add lines 10 and 11
Status: **AGREE**

### 13 — Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero or less,
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | clcw.spouse_screen | - |
| 2 | clcw.spouse_screen | clcw.spouse_screen |
| 3 | clcw.spouse_screen | - |
| 4 | clcw.spouse_screen | - |
| 7 | clcw.spouse_screen | - |
| 8 | clcw.spouse_screen | - |
| 11 | clcw.spouse_screen | - |
| 12 | clcw.spouse_screen | - |
| 13 | clcw.spouse_screen | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: clcw.h_zero
    printed: "(helper)"
    label: "Zero (used to express a loss entered as a positive amount)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: clcw.line1
    printed: "1"
    label: "Enter the amount from your 2024 Form 1040, 1040-SR, or 1040-NR, line 15. If the amount would have been a loss if you could enter a negative number on that line, enclose the amount in parentheses"
    type: Dollars
    expr: {op: subtract, from: clcw.prior_11, take: clcw.prior_14}
    refuses: [clcw.spouse_screen]
    note: "The interface supplies 2024 Form 1040 lines 11 and 14 rather than line 15. Line 15 is figured as line 11 minus line 14, with no zero floor, so a negative result is kept as the 'amount in parentheses' the worksheet asks for."
  - id: clcw.line2
    printed: "2"
    label: "Enter the loss from your 2024 Schedule D, line 21, as a positive amount"
    type: NonNegDollars
    expr: {op: copy, from: clcw.prior_sd21}
    refuses: [clcw.spouse_screen]
  - id: clcw.h_line1_plus_2
    printed: "(helper)"
    label: "Combine lines 1 and 2"
    type: Dollars
    expr: {op: sum, of: [clcw.line1, clcw.line2]}
  - id: clcw.line3
    printed: "3"
    label: "Combine lines 1 and 2. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.h_line1_plus_2, take: {const: 0}}
  - id: clcw.line4
    printed: "4"
    label: "Enter the smaller of line 2 or line 3"
    type: NonNegDollars
    expr: {op: smaller_of, of: [clcw.line2, clcw.line3]}
  - id: clcw.line5
    printed: "5"
    label: "Enter the loss from your 2024 Schedule D, line 7, as a positive amount (if line 7 of your 2024 Schedule D is not a loss, enter -0- on line 5 and go to line 9)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.h_zero, take: clcw.prior_sd7}
    note: "Zero minus line 7, floored at zero, gives the loss as a positive amount, or -0- when line 7 is not a loss, as the instruction above line 5 says."
  - id: clcw.line6
    printed: "6"
    label: "Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.prior_sd15, take: {const: 0}}
    note: "When 2024 Schedule D line 7 is not a loss, the worksheet skips lines 6 to 8. Lines 6 and 7 are still computed here, but line 8 is then zero because line 5 is zero."
  - id: clcw.line7
    printed: "7"
    label: "Add lines 4 and 6"
    type: NonNegDollars
    expr: {op: sum, of: [clcw.line4, clcw.line6]}
  - id: clcw.line8
    printed: "8"
    label: "Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 6"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.line5, take: clcw.line7}
    refuses: [clcw.spouse_screen]
    note: "The applicability test in the heading is not encoded separately: line 21 must be a loss, and either it is smaller than the line 16 loss or 2024 line 15 is below zero. When the test fails, the arithmetic already gives zero carryovers (line 4 then absorbs the whole loss). If line 21 is not a loss, line 2 is zero."
  - id: clcw.line9
    printed: "9"
    label: "Enter the loss from your 2024 Schedule D, line 15, as a positive amount (if line 15 of your 2024 Schedule D is not a loss, skip lines 9 through 13)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.h_zero, take: clcw.prior_sd15}
    note: "When 2024 Schedule D line 15 is not a loss, lines 9 to 13 are skipped. Line 9 is then zero, which makes line 13 (the carryover) zero."
  - id: clcw.line10
    printed: "10"
    label: "Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.prior_sd7, take: {const: 0}}
  - id: clcw.line11
    printed: "11"
    label: "Subtract line 5 from line 4. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.line4, take: clcw.line5}
  - id: clcw.line12
    printed: "12"
    label: "Add lines 10 and 11"
    type: NonNegDollars
    expr: {op: sum, of: [clcw.line10, clcw.line11]}
  - id: clcw.line13
    printed: "13"
    label: "Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 14"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.line9, take: clcw.line12}
    refuses: [clcw.spouse_screen]
```
```
