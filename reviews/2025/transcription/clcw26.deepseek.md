# Transcription agreement — clcw26

Second transcription of `Capital loss carryover to 2026 (Capital Loss Carryover Worksheet applied to this return)` by an isolated model (spec 6.5), compared line by line with `forms/2025/clcw26.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4196c7c5b11a8bffdc25a57d9f4bcecc64ddcdefa400c513a1de7faa51640811 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 6db1c5e7dc5c317ea9d86a08e98716888f3726df957fe4631f9780e5ea7d8c76 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | cd1860b673af88976841ed370a4905ad7cb46e9ceb0e582596ba2e6c7b6a92f7 |
| printed lines compared | 13 |
| agree / disagree / missing | 12 / 1 / 0 |
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
Status: **DISAGREE**

Project:

```json
{"from": {"of": [{"line": "1"}, {"line": "2"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"from": {"line": "2"}, "op": "subtract_floor0", "take": {"from": {"const": 0}, "op": "subtract", "take": {"line": "1"}}}
```

Ruling: model error; ruled on each difference kind. Value: representation. The candidate is line 2 less the negative of line 1, floored at zero (clcw26.h_neg_line1 = 0 - line 1), which is algebraically line 1 plus line 2 floored at zero, the project's line. i1040sd p. 10, line 3: "Combine lines 1 and 2. If zero or less, enter -0-". Triage executable-triage-v2 (`../triage/clcw26.deepseek.json`, 1,168 fixtures, 500 generated, 1,668 comparisons) finds no value difference (308 agree). The other differences are defects of the candidate. 127 candidate-shows-skipped (82 on completed returns): the reply hides nothing, so it shows line 3 where the source has no carryover to figure. Witness 7 (classm.f4952.1.deepseek, completed) shows $89,629.10 and witness 8 (classm.f4952.2.deepseek) $8,234.16, where the project hides the line under clcw26.show. That condition is i1040sd p. 14, Line 21: "You have a capital loss carryover from 2025 to 2026 if you have a loss on line 16 and either: That loss is more than the loss on line 21; or ... line 15, would be less than zero" (the BUG-0187 condition, checked and right). 1,010 candidate-unknown: the reply's line 1 declares refuses: [clcw.spouse_screen], the 2024-returns screen of the 2024-to-2025 worksheet, which is asked only behind sd.carryover. The 2026 worksheet does not need it (witnesses 0-2, classm.f2441.1-3.deepseek, completed). 203 candidate-refuses: upstream Form 1040 screens the candidate reaches on refused returns where the project hides the line (witnesses 9, 10, 14). 20 project-refuses: upstream screens on refused returns (scope.schedule1, sb.unsupported, f4952.unsupported; witnesses 6, 16, 17).

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

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | clcw.spouse_screen | - |
| 3 | clcw.spouse_screen | - |
| 4 | clcw.spouse_screen | - |
| 7 | clcw.spouse_screen | - |
| 8 | clcw.spouse_screen | - |
| 11 | clcw.spouse_screen | - |
| 12 | clcw.spouse_screen | - |
| 13 | clcw.spouse_screen | - |

## Raw second transcription

```yaml
lines:
  - id: clcw26.line1
    printed: "1"
    label: "Enter the amount from your 2025 Form 1040, 1040-SR, or 1040-NR, line 15. If the amount would have been a loss if you could enter a negative number on that line, enclose the amount in parentheses."
    type: Dollars
    expr: {op: subtract, from: f1040.line11b, take: f1040.line14}
    refuses: [clcw.spouse_screen]
    note: "The archived worksheet says to enter Form 1040 line 15, but also directs a negative amount when line 15 would be a loss. Because the line 15 interface is nonnegative, line 1 is computed as line 11b minus line 14 to preserve that negative hypothetical."
  - id: clcw26.line2
    printed: "2"
    label: "Enter the loss from your 2025 Schedule D, line 21, as a positive amount."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.zero, take: sd.line21}
  - id: clcw26.line3
    printed: "3"
    label: "Combine lines 1 and 2. If zero or less, enter -0-."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.line2, take: clcw26.h_neg_line1}
  - id: clcw26.line4
    printed: "4"
    label: "Enter the smaller of line 2 or line 3."
    type: NonNegDollars
    expr: {op: smaller_of, of: [clcw26.line2, clcw26.line3]}
  - id: clcw26.line5
    printed: "5"
    label: "Enter the loss from your 2025 Schedule D, line 7, as a positive amount."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.zero, take: sd.line7}
  - id: clcw26.line6
    printed: "6"
    label: "Enter any gain from your 2025 Schedule D, line 15. If a loss, enter -0-."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line15, take: clcw.zero}
  - id: clcw26.line7
    printed: "7"
    label: "Add lines 4 and 6."
    type: NonNegDollars
    expr: {op: sum, of: [clcw26.line4, clcw26.line6]}
  - id: clcw26.line8
    printed: "8"
    label: "Short-term capital loss carryover for 2026. Subtract line 7 from line 5. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 6."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.line5, take: clcw26.line7}
  - id: clcw26.line9
    printed: "9"
    label: "Enter the loss from your 2025 Schedule D, line 15, as a positive amount."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw.zero, take: sd.line15}
  - id: clcw26.line10
    printed: "10"
    label: "Enter any gain from your 2025 Schedule D, line 7. If a loss, enter -0-."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line7, take: clcw.zero}
  - id: clcw26.line11
    printed: "11"
    label: "Subtract line 5 from line 4. If zero or less, enter -0-."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.line4, take: clcw26.line5}
  - id: clcw26.line12
    printed: "12"
    label: "Add lines 10 and 11."
    type: NonNegDollars
    expr: {op: sum, of: [clcw26.line10, clcw26.line11]}
  - id: clcw26.line13
    printed: "13"
    label: "Long-term capital loss carryover for 2026. Subtract line 12 from line 9. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 14."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: clcw26.line9, take: clcw26.line12}
  - id: clcw26.h_neg_line1
    printed: "(helper)"
    label: "Negative of line 1, used to combine line 1 with line 2 and apply the zero floor."
    type: Dollars
    expr: {op: subtract, from: clcw.zero, take: clcw26.line1}
```
