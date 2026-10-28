# Render comparison — clcw26

The rendered English of every printed line of `Capital loss carryover to 2026 (Capital Loss Carryover Worksheet applied to this return)` (`rendered/2025/clcw26.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 14cc7b7f9fb5d460bd6381a4b9ee80671f838cfdb2ddbe8ce4ac0a115f0a3f1e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | ec31b327d7815597f047931f9ef880444410d2c7e017bf072ec03703a5d22d8b |
| lines judged | 13 |
| match / mismatch / unclear / missing | 13 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 10, 14 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 14 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 103 | cited pages | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | - | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### 1 — Form 1040 line 15 for 2025, negative if it would have been a loss (line 11b less line 14)
Status: **MATCH**

Model: Subtracting f1040 line 14 from line 11b gives the Form 1040 line 15 amount the worksheet asks for, and the gate mirrors the carryover condition.

### 2 — The loss on Schedule D line 21, as a positive amount
Status: **MATCH**

Model: Zero minus signed Schedule D line 21 converts a loss to a positive amount and floors nonlosses at zero, matching 'Enter the loss ... as a positive amount.'

### 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **MATCH**

Model: Adds lines 1 and 2 and floors at zero, matching 'Combine lines 1 and 2. If zero or less, enter -0-.'

### 4 — Enter the smaller of line 2 or line 3
Status: **MATCH**

Model: Enters the smaller of line 2 or line 3, exactly as IRS line 4 says.

### 5 — The loss on Schedule D line 7, as a positive amount (zero if line 7 is not a loss)
Status: **MATCH**

Model: Zero minus Schedule D line 7 gives a positive loss and floors gains to zero, matching 'Enter the loss ... line 7, as a positive amount.'

### 6 — Any gain on Schedule D line 15. If a loss, enter -0-
Status: **MATCH**

Model: Schedule D line 15 with a loss floored to zero matches 'Enter any gain ... If a loss, enter -0-.'

### 7 — Add lines 4 and 6
Status: **MATCH**

Model: Adds lines 4 and 6, matching IRS line 7.

### 8 — Short-term capital loss carryover to 2026. Subtract line 7 from line 5. If zero or less, e
Status: **MATCH**

Model: Subtracts line 7 from line 5 with a zero floor, matching IRS line 8.

### 9 — The loss on Schedule D line 15, as a positive amount
Status: **MATCH**

Model: Zero minus Schedule D line 15 gives a positive loss and floors gains to zero, matching 'Enter the loss ... line 15, as a positive amount.'

### 10 — Any gain on Schedule D line 7. If a loss, enter -0-
Status: **MATCH**

Model: Schedule D line 7 with a loss floored to zero matches 'Enter any gain ... If a loss, enter -0-.'

### 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **MATCH**

Model: Subtracts line 5 from line 4 with a zero floor, matching IRS line 11.

### 12 — Add lines 10 and 11
Status: **MATCH**

Model: Adds lines 10 and 11, matching IRS line 12.

### 13 — Long-term capital loss carryover to 2026. Subtract line 12 from line 9. If zero or less, e
Status: **MATCH**

Model: Subtracts line 12 from line 9 with a zero floor, matching IRS line 13.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Subtracting f1040 line 14 from line 11b gives the Form 1040 line 15 amount the worksheet asks for, and the gate mirrors the carryover condition."
  - key: "2"
    status: MATCH
    reason: "Zero minus signed Schedule D line 21 converts a loss to a positive amount and floors nonlosses at zero, matching 'Enter the loss ... as a positive amount.'"
  - key: "3"
    status: MATCH
    reason: "Adds lines 1 and 2 and floors at zero, matching 'Combine lines 1 and 2. If zero or less, enter -0-.'"
  - key: "4"
    status: MATCH
    reason: "Enters the smaller of line 2 or line 3, exactly as IRS line 4 says."
  - key: "5"
    status: MATCH
    reason: "Zero minus Schedule D line 7 gives a positive loss and floors gains to zero, matching 'Enter the loss ... line 7, as a positive amount.'"
  - key: "6"
    status: MATCH
    reason: "Schedule D line 15 with a loss floored to zero matches 'Enter any gain ... If a loss, enter -0-.'"
  - key: "7"
    status: MATCH
    reason: "Adds lines 4 and 6, matching IRS line 7."
  - key: "8"
    status: MATCH
    reason: "Subtracts line 7 from line 5 with a zero floor, matching IRS line 8."
  - key: "9"
    status: MATCH
    reason: "Zero minus Schedule D line 15 gives a positive loss and floors gains to zero, matching 'Enter the loss ... line 15, as a positive amount.'"
  - key: "10"
    status: MATCH
    reason: "Schedule D line 7 with a loss floored to zero matches 'Enter any gain ... If a loss, enter -0-.'"
  - key: "11"
    status: MATCH
    reason: "Subtracts line 5 from line 4 with a zero floor, matching IRS line 11."
  - key: "12"
    status: MATCH
    reason: "Adds lines 10 and 11, matching IRS line 12."
  - key: "13"
    status: MATCH
    reason: "Subtracts line 12 from line 9 with a zero floor, matching IRS line 13."
```
