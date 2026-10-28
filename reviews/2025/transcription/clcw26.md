# Transcription agreement — clcw26

Second transcription of `Capital loss carryover to 2026 (Capital Loss Carryover Worksheet applied to this return)` by an isolated model (spec 6.5), compared line by line with `forms/2025/clcw26.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4196c7c5b11a8bffdc25a57d9f4bcecc64ddcdefa400c513a1de7faa51640811 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 67033a9373d134076149077bfad5efc30e7b438aeda428422eb0b583cd6bd7f4 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | cd1860b673af88976841ed370a4905ad7cb46e9ceb0e582596ba2e6c7b6a92f7 |
| printed lines compared | 13 |
| agree / disagree / missing | 13 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 10, 14 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 14 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 103 | cited pages | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | - | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### 1 — Form 1040 line 15 for 2025, negative if it would have been a loss (line 11b less line 14)
Status: **AGREE**

### 2 — The loss on Schedule D line 21, as a positive amount
Status: **AGREE**

### 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **AGREE**

### 4 — Enter the smaller of line 2 or line 3
Status: **AGREE**

### 5 — The loss on Schedule D line 7, as a positive amount (zero if line 7 is not a loss)
Status: **AGREE**

### 6 — Any gain on Schedule D line 15. If a loss, enter -0-
Status: **AGREE**

### 7 — Add lines 4 and 6
Status: **AGREE**

### 8 — Short-term capital loss carryover to 2026. Subtract line 7 from line 5. If zero or less, e
Status: **AGREE**

### 9 — The loss on Schedule D line 15, as a positive amount
Status: **AGREE**

### 10 — Any gain on Schedule D line 7. If a loss, enter -0-
Status: **AGREE**

### 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **AGREE**

### 12 — Add lines 10 and 11
Status: **AGREE**

### 13 — Long-term capital loss carryover to 2026. Subtract line 12 from line 9. If zero or less, e
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: clcw26.h_zero
    printed: "(helper)"
    label: "Zero (used for 'enter -0-' and for entering a loss as a positive amount)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: clcw26.line1
    printed: "1"
    label: "Enter the amount from your 2025 Form 1040, 1040-SR, or 1040-NR, line 15. If the amount would have been a loss if you could enter a negative number on that line, enclose the amount in parentheses"
    type: Dollars
    expr: {op: subtract, from: f1040.line11b, take: f1040.line14}
    note: "The printed line 15 is floored at zero, so f1040.line15 cannot carry the negative amount this line asks for. Line 15 is the subtraction of line 14 from line 11b, so that subtraction is recomputed here without the floor to keep the would-be loss. Line 11b was chosen as the operand because it is the AGI carried to page 2 that line 15 subtracts from."
  - id: clcw26.line2
    printed: "2"
    label: "Enter the loss from your 2025 Schedule D, line 21, as a positive amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.h_zero, take: sd.line21}
    note: "sd.line21 is assumed to be negative for a loss. Subtracting it from zero gives the loss as a positive amount, and 0 when line 21 is not a loss."
  - id: clcw26.h_combined
    printed: "(helper)"
    label: "Combine lines 1 and 2"
    type: Dollars
    expr: {op: sum, of: [clcw26.line1, clcw26.line2]}
  - id: clcw26.line3
    printed: "3"
    label: "Combine lines 1 and 2. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.h_combined, take: clcw26.h_zero}
  - id: clcw26.line4
    printed: "4"
    label: "Enter the smaller of line 2 or line 3"
    type: NonNegDollars
    expr: {op: smaller_of, of: [clcw26.line2, clcw26.line3]}
  - id: clcw26.line5
    printed: "5"
    label: "Enter the loss from your 2025 Schedule D, line 7, as a positive amount (if line 7 is not a loss, enter -0- and go to line 9)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.h_zero, take: sd.line7}
    note: "When line 7 is not a loss this line is 0. Lines 6 to 8 are still computed in that case; line 8 then comes out 0, which is what the instruction 'go to line 9' produces."
  - id: clcw26.line6
    printed: "6"
    label: "Enter any gain from your 2025 Schedule D, line 15. If a loss, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line15, take: clcw26.h_zero}
  - id: clcw26.line7
    printed: "7"
    label: "Add lines 4 and 6"
    type: NonNegDollars
    expr: {op: sum, of: [clcw26.line4, clcw26.line6]}
  - id: clcw26.line8
    printed: "8"
    label: "Short-term capital loss carryover for 2026. Subtract line 7 from line 5. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 6"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.line5, take: clcw26.line7}
  - id: clcw26.line9
    printed: "9"
    label: "Enter the loss from your 2025 Schedule D, line 15, as a positive amount (if line 15 is not a loss, skip lines 9 through 13)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.h_zero, take: sd.line15}
    note: "When line 15 is not a loss this line is 0. Lines 10 to 13 are still computed in that case; line 13 then comes out 0, which matches skipping those lines (no long-term carryover)."
  - id: clcw26.line10
    printed: "10"
    label: "Enter any gain from your 2025 Schedule D, line 7. If a loss, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line7, take: clcw26.h_zero}
  - id: clcw26.line11
    printed: "11"
    label: "Subtract line 5 from line 4. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.line4, take: clcw26.line5}
  - id: clcw26.line12
    printed: "12"
    label: "Add lines 10 and 11"
    type: NonNegDollars
    expr: {op: sum, of: [clcw26.line10, clcw26.line11]}
  - id: clcw26.line13
    printed: "13"
    label: "Long-term capital loss carryover for 2026. Subtract line 12 from line 9. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 14"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.line9, take: clcw26.line12}
    note: "The worksheet's entry condition (a line 21 loss that is smaller than the line 16 loss, or a would-be negative line 15) is not encoded as a separate gate. When that condition fails, the arithmetic already gives 0 on lines 8 and 13. The rule that a joint-return carryover goes only to the spouse who had the loss concerns 2026 filing and is not encoded. The Pub. 4681 canceled-debt adjustment is also not encoded, because no input or screen for it was provided."
```
```
