# Render comparison — clcw

The rendered English of every printed line of `Capital Loss Carryover Worksheet—Lines 6 and 14` (`rendered/2025/clcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d25fd14f39ed065fe1e89ae203b64d39fb2d6298534400a99100dd2480651f12 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | ee542d2249ed46670d176c89ce2496b0a4068c3e91aeb7be89421d1ccb132ea6 |
| lines judged | 13 |
| match / mismatch / unclear / missing | 13 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 3, 10 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 3 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 102, 103 | cited pages | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | - | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### 1 — Your 2024 taxable income (2024 Form 1040 line 15), negative if it would have been a loss
Status: **MATCH**

Model: Computes 2024 Form 1040 line 15 as AGI minus deductions, matching the worksheet instruction to enter line 15 and treat a would-be loss as negative.

### 2 — Enter the loss from your 2024 Schedule D, line 21, as a positive amount
Status: **MATCH**

Model: Enters the 2024 Schedule D line 21 loss as a positive amount, as the worksheet directs.

### 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **MATCH**

Model: Combines lines 1 and 2 and enters -0- if zero or less, matching the IRS line.

### 4 — Enter the smaller of line 2 or line 3
Status: **MATCH**

Model: Enters the smaller of line 2 or line 3, as the IRS line says.

### 5 — Enter the loss from your 2024 Schedule D, line 7, as a positive amount (zero if line 7 is
Status: **MATCH**

Model: Computes the line 7 loss as a positive amount, with -0- if line 7 is not a loss, matching the worksheet.

### 6 — Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-
Status: **MATCH**

Model: Enters any gain from 2024 Schedule D line 15 and enters -0- if line 15 is a loss, as directed.

### 7 — Add lines 4 and 6
Status: **MATCH**

Model: Adds lines 4 and 6, matching the IRS line.

### 8 — Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero or less,
Status: **MATCH**

Model: Subtracts line 7 from line 5 and enters -0- if zero or less, as the worksheet says.

### 9 — Enter the loss from your 2024 Schedule D, line 15, as a positive amount
Status: **MATCH**

Model: Computes the line 15 loss as a positive amount and is used only when line 15 is a loss, matching the worksheet.

### 10 — Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-
Status: **MATCH**

Model: Enters any gain from 2024 Schedule D line 7 and enters -0- if line 7 is a loss, as directed.

### 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **MATCH**

Model: Subtracts line 5 from line 4 and enters -0- if zero or less, matching the IRS line.

### 12 — Add lines 10 and 11
Status: **MATCH**

Model: Adds lines 10 and 11, matching the IRS line.

### 13 — Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero or less,
Status: **MATCH**

Model: Subtracts line 12 from line 9 and enters -0- if zero or less, matching the IRS line.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Computes 2024 Form 1040 line 15 as AGI minus deductions, matching the worksheet instruction to enter line 15 and treat a would-be loss as negative."
  - key: "2"
    status: MATCH
    reason: "Enters the 2024 Schedule D line 21 loss as a positive amount, as the worksheet directs."
  - key: "3"
    status: MATCH
    reason: "Combines lines 1 and 2 and enters -0- if zero or less, matching the IRS line."
  - key: "4"
    status: MATCH
    reason: "Enters the smaller of line 2 or line 3, as the IRS line says."
  - key: "5"
    status: MATCH
    reason: "Computes the line 7 loss as a positive amount, with -0- if line 7 is not a loss, matching the worksheet."
  - key: "6"
    status: MATCH
    reason: "Enters any gain from 2024 Schedule D line 15 and enters -0- if line 15 is a loss, as directed."
  - key: "7"
    status: MATCH
    reason: "Adds lines 4 and 6, matching the IRS line."
  - key: "8"
    status: MATCH
    reason: "Subtracts line 7 from line 5 and enters -0- if zero or less, as the worksheet says."
  - key: "9"
    status: MATCH
    reason: "Computes the line 15 loss as a positive amount and is used only when line 15 is a loss, matching the worksheet."
  - key: "10"
    status: MATCH
    reason: "Enters any gain from 2024 Schedule D line 7 and enters -0- if line 7 is a loss, as directed."
  - key: "11"
    status: MATCH
    reason: "Subtracts line 5 from line 4 and enters -0- if zero or less, matching the IRS line."
  - key: "12"
    status: MATCH
    reason: "Adds lines 10 and 11, matching the IRS line."
  - key: "13"
    status: MATCH
    reason: "Subtracts line 12 from line 9 and enters -0- if zero or less, matching the IRS line."
```
