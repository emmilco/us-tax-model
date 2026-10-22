# Render comparison — ssb

The rendered English of every printed line of `Social Security Benefits Worksheet—Lines 6a and 6b` (`rendered/2025/ssb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1773707a4583191d11f2f668a92ce2a3973927a620c5263d04b9dc5d186288fd |
| subject sha256 | 28a23844745911cf6d389a6f3161895bff42580d38d0192310c40870fb35db9b |
| lines judged | 18 |
| match / mismatch / unclear / missing | 17 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **MATCH**

Model: The IRS line says 'Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099.' The helper is exactly that input.

### 2 — Multiply line 1 by 50% (0.50)
Status: **MATCH**

Model: 1/2 is the same as the IRS 'Multiply line 1 by 50% (0.50)'. The refusals match the Exception list that sends filers to Pub. 590-A or Pub. 915, and they name the lump-sum and terrorist-attack disability cases, which the instructions refer to Pub. 915 and Pub. 3920.

### 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
Status: **MATCH**

Model: The IRS line says 'Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8.' The restatement uses the same lines.

### 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **MATCH**

Model: The IRS line says 'Enter the amount, if any, from Form 1040 or 1040-SR, line 2a.' The restatement does the same.

### 5 — Combine lines 2, 3, and 4
Status: **MATCH**

Model: The IRS line says 'Combine lines 2, 3, and 4.' The restatement does the same.

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MATCH**

Model: The IRS line says 'Schedule 1, lines 11 through 20, and 23 and 25.' The restatement leaves out lines 12, 14 and 23, but the scope.schedule1 refusal names exactly those lines. Figuring line 20 with no one covered by a retirement plan is consistent, because the ssb.pub915 refusal excludes the case where someone is covered.

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line 
Status: **MATCH**

Model: The IRS STOP rule (line 6 not less than line 5 means none taxable) is reached here by entering -0-. That zero carries through to line 18 = 0 in every branch.

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **MATCH**

Model: The amounts match the IRS text: $32,000 for married filing jointly; $25,000 for single, HOH, QSS, or MFS who lived apart all year. MFS who lived with the spouse gets no amount, matching 'skip lines 8 through 15.'

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line 
Status: **MISMATCH**

Restated: Subtract line 8 from line 7. If zero or less, enter -0-.

Model: The IRS says MFS filers who lived with their spouse 'skip lines 8 through 15.' The restatement computes line 9 anyway, giving line 7 minus 0, so lines 9, 11 and 15 get nonzero amounts where the IRS has none. Line 16 is unaffected, and in all other cases the restatement matches 'Subtract line 8 from line 7' with the STOP shown as -0-.

Ruling: equivalent on every return the tool completes; project retained. A separate return is refused (scope.ready, s3.mfs), so the case the model raises (married filing separately, lived with the spouse: "skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16", i1040gi p. 32, line 8) is not reached; even there line 16 takes line 7 times 85% (ssb.line16_together) and line 18 is unaffected, as the model notes. Otherwise line 9 is line 7 less line 8 with the STOP shown as zero, as the model accepts.

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **MATCH**

Model: The IRS line says 'Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025.' The restatement gives the same amounts, and the MFS-lived-together case is skipped per line 8.

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **MATCH**

Model: The IRS line says 'Subtract line 10 from line 9. If zero or less, enter -0-.' The restatement does the same.

### 12 — Enter the smaller of line 9 or line 10
Status: **MATCH**

Model: The IRS line says 'Enter the smaller of line 9 or line 10.' The restatement does the same.

### 13 — Enter one-half of line 12
Status: **MATCH**

Model: The IRS line says 'Enter one-half of line 12.' The restatement multiplies line 12 by 1/2, which is the same.

### 14 — Enter the smaller of line 2 or line 13
Status: **MATCH**

Model: The IRS line says 'Enter the smaller of line 2 or line 13.' The restatement does the same.

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **MATCH**

Model: The IRS line says 'Multiply line 11 by 85% (0.85).' The restatement does the same, and it yields zero when line 11 is zero.

### 16 — Add lines 14 and 15
Status: **MATCH**

Model: The IRS line says 'Add lines 14 and 15.' For MFS who lived with the spouse, the line 8 text says 'multiply line 7 by 85% (0.85) and enter the result on line 16.' The restatement does both.

### 17 — Multiply line 1 by 85% (0.85)
Status: **MATCH**

Model: The IRS line says 'Multiply line 1 by 85% (0.85).' The restatement does the same.

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **MATCH**

Model: The IRS line says 'Enter the smaller of line 16 or line 17.' When line 1 is zero, line 17 is zero, so entering $0 gives the same value.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The IRS line says 'Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099.' The helper is exactly that input."
  - key: "2"
    status: MATCH
    reason: "1/2 is the same as the IRS 'Multiply line 1 by 50% (0.50)'. The refusals match the Exception list that sends filers to Pub. 590-A or Pub. 915, and they name the lump-sum and terrorist-attack disability cases, which the instructions refer to Pub. 915 and Pub. 3920."
  - key: "3"
    status: MATCH
    reason: "The IRS line says 'Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8.' The restatement uses the same lines."
  - key: "4"
    status: MATCH
    reason: "The IRS line says 'Enter the amount, if any, from Form 1040 or 1040-SR, line 2a.' The restatement does the same."
  - key: "5"
    status: MATCH
    reason: "The IRS line says 'Combine lines 2, 3, and 4.' The restatement does the same."
  - key: "6"
    status: MATCH
    reason: "The IRS line says 'Schedule 1, lines 11 through 20, and 23 and 25.' The restatement leaves out lines 12, 14 and 23, but the scope.schedule1 refusal names exactly those lines. Figuring line 20 with no one covered by a retirement plan is consistent, because the ssb.pub915 refusal excludes the case where someone is covered."
  - key: "7"
    status: MATCH
    reason: "The IRS STOP rule (line 6 not less than line 5 means none taxable) is reached here by entering -0-. That zero carries through to line 18 = 0 in every branch."
  - key: "8"
    status: MATCH
    reason: "The amounts match the IRS text: $32,000 for married filing jointly; $25,000 for single, HOH, QSS, or MFS who lived apart all year. MFS who lived with the spouse gets no amount, matching 'skip lines 8 through 15.'"
  - key: "9"
    status: MISMATCH
    reason: "The IRS says MFS filers who lived with their spouse 'skip lines 8 through 15.' The restatement computes line 9 anyway, giving line 7 minus 0, so lines 9, 11 and 15 get nonzero amounts where the IRS has none. Line 16 is unaffected, and in all other cases the restatement matches 'Subtract line 8 from line 7' with the STOP shown as -0-."
  - key: "10"
    status: MATCH
    reason: "The IRS line says 'Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025.' The restatement gives the same amounts, and the MFS-lived-together case is skipped per line 8."
  - key: "11"
    status: MATCH
    reason: "The IRS line says 'Subtract line 10 from line 9. If zero or less, enter -0-.' The restatement does the same."
  - key: "12"
    status: MATCH
    reason: "The IRS line says 'Enter the smaller of line 9 or line 10.' The restatement does the same."
  - key: "13"
    status: MATCH
    reason: "The IRS line says 'Enter one-half of line 12.' The restatement multiplies line 12 by 1/2, which is the same."
  - key: "14"
    status: MATCH
    reason: "The IRS line says 'Enter the smaller of line 2 or line 13.' The restatement does the same."
  - key: "15"
    status: MATCH
    reason: "The IRS line says 'Multiply line 11 by 85% (0.85).' The restatement does the same, and it yields zero when line 11 is zero."
  - key: "16"
    status: MATCH
    reason: "The IRS line says 'Add lines 14 and 15.' For MFS who lived with the spouse, the line 8 text says 'multiply line 7 by 85% (0.85) and enter the result on line 16.' The restatement does both."
  - key: "17"
    status: MATCH
    reason: "The IRS line says 'Multiply line 1 by 85% (0.85).' The restatement does the same."
  - key: "18"
    status: MATCH
    reason: "The IRS line says 'Enter the smaller of line 16 or line 17.' When line 1 is zero, line 17 is zero, so entering $0 gives the same value."
```
```
