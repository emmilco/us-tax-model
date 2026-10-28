# Render comparison — clcw

The rendered English of every printed line of `Capital Loss Carryover Worksheet—Lines 6 and 14` (`rendered/2025/clcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d25fd14f39ed065fe1e89ae203b64d39fb2d6298534400a99100dd2480651f12 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | ee542d2249ed46670d176c89ce2496b0a4068c3e91aeb7be89421d1ccb132ea6 |
| lines judged | 13 |
| match / mismatch / unclear / missing | 12 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 3, 10 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 3 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 102, 103 | cited pages | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | - | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### 1 — Your 2024 taxable income (2024 Form 1040 line 15), negative if it would have been a loss
Status: **UNCLEAR**

Restated: Subtract helper "The amount on line 14 of your 2024 Form 1040 or 1040-SR (your deductions)" from helper "The amount on line 11 of your 2024 Form 1040 or 1040-SR (adjusted gross income)".

Model: The IRS line says "Enter the amount from your 2024 Form 1040, 1040-SR, or 1040-NR, line 15," enclosed in parentheses if it would have been a loss. The restatement instead computes 2024 line 11 minus line 14, and nothing in the text given says line 15 equals line 11 minus line 14. The restatement also leaves out Form 1040-NR without a refusal.

Ruling: ambiguity; amb.2025.clcw_line1_signed. UNCLEAR: the model says nothing in the text given says line 15 equals line 11 minus line 14, and that Form 1040-NR is left out without a refusal. i1040sd p. 10, line 1: "Enter the amount from your 2024 Form 1040, 1040-SR, or 1040-NR, line 15. If the amount would have been a loss if you could enter a negative number on that line, enclose the amount in parentheses". The rendering states the reading recorded in amb.2025.clcw_line1_signed (owner's decision D2(a), 2026-10-27): ask for 2024 lines 11 and 14 as printed and take line 1 as their difference, because the printed line 15 is floored at zero and the worksheet wants the amount before the floor. The identity is printed on the 2024 Form 1040 (sources/2024/f1040 p. 1, line 15: "Subtract line 14 from line 11. If zero or less, enter -0-. This is your taxable income"), a page the review was not given (it had i1040sd pp. 3 and 10 and p550 pp. 102-103), because the line's citation names only the worksheet. Form 1040-NR is outside the tool (this tool prepares Form 1040 or 1040-SR only), so leaving it out changes nothing. Same ruling as the first Stage 20 round. The BUG-0185 change (line 1 shown only when clcw.applies) agrees with p. 10, "Otherwise, you don't have any carryovers", and is not disputed.

### 2 — Enter the loss from your 2024 Schedule D, line 21, as a positive amount
Status: **MATCH**

Model: This matches "Enter the loss from your 2024 Schedule D, line 21, as a positive amount." The refusal only screens out inconsistent entries.

### 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **MATCH**

Model: Adding line 1 and line 2, with a floor at zero, matches "Combine lines 1 and 2. If zero or less, enter -0-."

### 4 — Enter the smaller of line 2 or line 3
Status: **MATCH**

Model: This matches "Enter the smaller of line 2 or line 3."

### 5 — Enter the loss from your 2024 Schedule D, line 7, as a positive amount (zero if line 7 is
Status: **MATCH**

Model: Zero minus 2024 line 7, floored at zero, gives the loss as a positive amount. It also gives -0- when line 7 is not a loss, which matches "otherwise, enter -0- on line 5."

### 6 — Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-
Status: **MATCH**

Model: Line 15 floored at zero matches "Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-." The gate on a line 7 loss reflects the instruction to skip to line 9 otherwise.

### 7 — Add lines 4 and 6
Status: **MATCH**

Model: This matches "Add lines 4 and 6."

### 8 — Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero or less,
Status: **MATCH**

Model: This matches "Subtract line 7 from line 5. If zero or less, enter -0-."

### 9 — Enter the loss from your 2024 Schedule D, line 15, as a positive amount
Status: **MATCH**

Model: Zero minus line 15, floored at zero, matches "Enter the loss from your 2024 Schedule D, line 15, as a positive amount." The line is gated on line 15 being a loss, as the IRS text directs.

### 10 — Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-
Status: **MATCH**

Model: Line 7 floored at zero matches "Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-."

### 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **MATCH**

Model: This matches "Subtract line 5 from line 4. If zero or less, enter -0-."

### 12 — Add lines 10 and 11
Status: **MATCH**

Model: This matches "Add lines 10 and 11."

### 13 — Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero or less,
Status: **MATCH**

Model: This matches "Subtract line 12 from line 9. If zero or less, enter -0-."

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: UNCLEAR
    reason: "The IRS line says \"Enter the amount from your 2024 Form 1040, 1040-SR, or 1040-NR, line 15,\" enclosed in parentheses if it would have been a loss. The restatement instead computes 2024 line 11 minus line 14, and nothing in the text given says line 15 equals line 11 minus line 14. The restatement also leaves out Form 1040-NR without a refusal."
  - key: "2"
    status: MATCH
    reason: "This matches \"Enter the loss from your 2024 Schedule D, line 21, as a positive amount.\" The refusal only screens out inconsistent entries."
  - key: "3"
    status: MATCH
    reason: "Adding line 1 and line 2, with a floor at zero, matches \"Combine lines 1 and 2. If zero or less, enter -0-.\""
  - key: "4"
    status: MATCH
    reason: "This matches \"Enter the smaller of line 2 or line 3.\""
  - key: "5"
    status: MATCH
    reason: "Zero minus 2024 line 7, floored at zero, gives the loss as a positive amount. It also gives -0- when line 7 is not a loss, which matches \"otherwise, enter -0- on line 5.\""
  - key: "6"
    status: MATCH
    reason: "Line 15 floored at zero matches \"Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-.\" The gate on a line 7 loss reflects the instruction to skip to line 9 otherwise."
  - key: "7"
    status: MATCH
    reason: "This matches \"Add lines 4 and 6.\""
  - key: "8"
    status: MATCH
    reason: "This matches \"Subtract line 7 from line 5. If zero or less, enter -0-.\""
  - key: "9"
    status: MATCH
    reason: "Zero minus line 15, floored at zero, matches \"Enter the loss from your 2024 Schedule D, line 15, as a positive amount.\" The line is gated on line 15 being a loss, as the IRS text directs."
  - key: "10"
    status: MATCH
    reason: "Line 7 floored at zero matches \"Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-.\""
  - key: "11"
    status: MATCH
    reason: "This matches \"Subtract line 5 from line 4. If zero or less, enter -0-.\""
  - key: "12"
    status: MATCH
    reason: "This matches \"Add lines 10 and 11.\""
  - key: "13"
    status: MATCH
    reason: "This matches \"Subtract line 12 from line 9. If zero or less, enter -0-.\""
```
```
