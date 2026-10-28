# Render comparison — clcw26

The rendered English of every printed line of `Capital loss carryover to 2026 (Capital Loss Carryover Worksheet applied to this return)` (`rendered/2025/clcw26.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 14cc7b7f9fb5d460bd6381a4b9ee80671f838cfdb2ddbe8ce4ac0a115f0a3f1e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | ec31b327d7815597f047931f9ef880444410d2c7e017bf072ec03703a5d22d8b |
| lines judged | 13 |
| match / mismatch / unclear / missing | 12 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 10, 14 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 14 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 103 | cited pages | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | - | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### 1 — Form 1040 line 15 for 2025, negative if it would have been a loss (line 11b less line 14)
Status: **UNCLEAR**

Restated: Subtract f1040 line 14 from f1040 line 11b.

Model: The IRS line says "Enter the amount from your ... Form 1040 ... line 15" and to show it in parentheses if it "would have been a loss." The pages given never define Form 1040 line 15, so they don't confirm it equals line 11b minus line 14 without a floor at zero.

Ruling: interface gap; the model says the pages given never define Form 1040 line 15, so they do not confirm it equals line 11b minus line 14 without a floor at zero. The worksheet is applied to this return with each 2024 figure read as the 2025 one (amb.2025.clcw_to_2026). Line 1 is held before the zero floor, as i1040sd p. 14, Line 21 requires ("would be less than zero if you could enter a negative amount on that line"), and as amb.2025.clcw_line1_signed does for the 2024 worksheet. The identity is printed on Form 1040 (2025) p. 2, line 15: "Subtract line 14 from line 11b. If zero or less, enter -0-. This is your taxable income". That page was not given to the reviewer (only i1040sd pp. 10 and 14 and p550 p. 103 were). The English states the source correctly; the UNCLEAR is a coverage gap of the review. Same ruling as the first Stage 20 round.

### 2 — The loss on Schedule D line 21, as a positive amount
Status: **MATCH**

Model: The IRS says "Enter the loss from your ... Schedule D, line 21, as a positive amount." Subtracting the signed line 21 loss from zero gives that positive amount.

### 3 — Combine lines 1 and 2. If zero or less, enter -0-
Status: **MATCH**

Model: The IRS says "Combine lines 1 and 2. If zero or less, enter -0-." Subtracting zero from lines 1 and 2 combined, with a floor at zero, gives the same value.

### 4 — Enter the smaller of line 2 or line 3
Status: **MATCH**

Model: Both say to enter the smaller of line 2 or line 3.

### 5 — The loss on Schedule D line 7, as a positive amount (zero if line 7 is not a loss)
Status: **MATCH**

Model: The IRS says to enter the line 7 loss as a positive amount, or "enter -0- on line 5" if line 7 is not a loss. Zero minus signed line 7, with a floor at zero, gives this.

### 6 — Any gain on Schedule D line 15. If a loss, enter -0-
Status: **MATCH**

Model: The IRS says "Enter any gain from your ... Schedule D, line 15. If a loss, enter -0-." Line 15 minus zero, with a floor at zero, matches. The condition that line 7 is a loss matches "If line 7 ... is a loss, go to line 5."

### 7 — Add lines 4 and 6
Status: **MATCH**

Model: Both say to add lines 4 and 6.

### 8 — Short-term capital loss carryover to 2026. Subtract line 7 from line 5. If zero or less, e
Status: **MATCH**

Model: Both say "Subtract line 7 from line 5. If zero or less, enter -0-."

### 9 — The loss on Schedule D line 15, as a positive amount
Status: **MATCH**

Model: The IRS says "Enter the loss from your ... Schedule D, line 15, as a positive amount." The condition that line 15 is a loss matches "If line 15 ... is a loss, go to line 9; otherwise, skip lines 9 through 13."

### 10 — Any gain on Schedule D line 7. If a loss, enter -0-
Status: **MATCH**

Model: The IRS says "Enter any gain from your ... Schedule D, line 7. If a loss, enter -0-." Line 7 minus zero, with a floor at zero, matches.

### 11 — Subtract line 5 from line 4. If zero or less, enter -0-
Status: **MATCH**

Model: Both say "Subtract line 5 from line 4. If zero or less, enter -0-."

### 12 — Add lines 10 and 11
Status: **MATCH**

Model: Both say to add lines 10 and 11.

### 13 — Long-term capital loss carryover to 2026. Subtract line 12 from line 9. If zero or less, e
Status: **MATCH**

Model: Both say "Subtract line 12 from line 9. If zero or less, enter -0-."

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: UNCLEAR
    reason: "The IRS line says \"Enter the amount from your ... Form 1040 ... line 15\" and to show it in parentheses if it \"would have been a loss.\" The pages given never define Form 1040 line 15, so they don't confirm it equals line 11b minus line 14 without a floor at zero."
  - key: "2"
    status: MATCH
    reason: "The IRS says \"Enter the loss from your ... Schedule D, line 21, as a positive amount.\" Subtracting the signed line 21 loss from zero gives that positive amount."
  - key: "3"
    status: MATCH
    reason: "The IRS says \"Combine lines 1 and 2. If zero or less, enter -0-.\" Subtracting zero from lines 1 and 2 combined, with a floor at zero, gives the same value."
  - key: "4"
    status: MATCH
    reason: "Both say to enter the smaller of line 2 or line 3."
  - key: "5"
    status: MATCH
    reason: "The IRS says to enter the line 7 loss as a positive amount, or \"enter -0- on line 5\" if line 7 is not a loss. Zero minus signed line 7, with a floor at zero, gives this."
  - key: "6"
    status: MATCH
    reason: "The IRS says \"Enter any gain from your ... Schedule D, line 15. If a loss, enter -0-.\" Line 15 minus zero, with a floor at zero, matches. The condition that line 7 is a loss matches \"If line 7 ... is a loss, go to line 5.\""
  - key: "7"
    status: MATCH
    reason: "Both say to add lines 4 and 6."
  - key: "8"
    status: MATCH
    reason: "Both say \"Subtract line 7 from line 5. If zero or less, enter -0-.\""
  - key: "9"
    status: MATCH
    reason: "The IRS says \"Enter the loss from your ... Schedule D, line 15, as a positive amount.\" The condition that line 15 is a loss matches \"If line 15 ... is a loss, go to line 9; otherwise, skip lines 9 through 13.\""
  - key: "10"
    status: MATCH
    reason: "The IRS says \"Enter any gain from your ... Schedule D, line 7. If a loss, enter -0-.\" Line 7 minus zero, with a floor at zero, matches."
  - key: "11"
    status: MATCH
    reason: "Both say \"Subtract line 5 from line 4. If zero or less, enter -0-.\""
  - key: "12"
    status: MATCH
    reason: "Both say to add lines 10 and 11."
  - key: "13"
    status: MATCH
    reason: "Both say \"Subtract line 12 from line 9. If zero or less, enter -0-.\""
```
```
