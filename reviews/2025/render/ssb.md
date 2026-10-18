# Render comparison — ssb

The rendered English of every printed line of `Social Security Benefits Worksheet—Lines 6a and 6b` (`rendered/2025/ssb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2cda1e8fa8da9fad8e87a25a87a1db4de3c3b4e31464fbd23a32f91712ed5ba6 |
| lines judged | 18 |
| match / mismatch / unclear / missing | 18 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **MATCH**

Model: The IRS line says 'Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099', and the restatement enters that same input.

### 2 — Multiply line 1 by 50% (0.50)
Status: **MATCH**

Model: 'Multiply line 1 by 50% (0.50)' is the same as multiplying by 1/2. The three refusals cover cases the instructions send to Pub. 590-A/915 ('Exception'), to the Lump-Sum Election in Pub. 915, and to the terrorist-attack disability exclusion (Pub. 3920), and each names what is excluded.

### 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
Status: **MATCH**

Model: The IRS line says 'Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8'. The restatement adds the same lines, and its signed Dollars type lets a capital loss on line 7a reduce the total.

### 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **MATCH**

Model: Both enter the amount, if any, from Form 1040 line 2a.

### 5 — Combine lines 2, 3, and 4
Status: **MATCH**

Model: 'Combine lines 2, 3, and 4' is the same as adding lines 2, 3 and 4 with signed amounts.

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MATCH**

Model: The IRS line adds 'Schedule 1, lines 11 through 20, and 23 and 25'. The restatement adds only lines 11 and 13, but the scope.schedule1 refusal blocks every other Schedule 1 adjustment and names lines 12, 14 to 20, 23 and 25 as excluded. So within the supported cases the two totals are the same.

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line 
Status: **MATCH**

Model: The IRS line stops with taxable benefits of -0- when line 6 is not less than line 5, and otherwise subtracts line 6 from line 5. Entering -0- when the result is zero or less sends zero through lines 9 to 18, so line 18 is also -0-.

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **MATCH**

Model: The IRS amounts are $32,000 for married filing jointly and $25,000 for single, head of household, qualifying surviving spouse, or married filing separately and lived apart all year. For married filing separately and lived together it says 'skip lines 8 through 15', and the restatement enters $0 there and handles that case on line 16.

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line 
Status: **MATCH**

Model: The IRS line stops with -0- taxable when line 8 is not less than line 7, and otherwise subtracts line 8 from line 7. Using the floored subtraction gives the same final result.

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **MATCH**

Model: The IRS line says 'Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart', and the restatement uses those amounts. Married filing separately while living together is skipped under line 8, and that case is overridden on line 16.

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **MATCH**

Model: Both say: subtract line 10 from line 9, and if zero or less, enter -0-.

### 12 — Enter the smaller of line 9 or line 10
Status: **MATCH**

Model: Both say: enter the smaller of line 9 or line 10.

### 13 — Enter one-half of line 12
Status: **MATCH**

Model: 'Enter one-half of line 12' is the same as multiplying line 12 by 1/2.

### 14 — Enter the smaller of line 2 or line 13
Status: **MATCH**

Model: Both say: enter the smaller of line 2 or line 13.

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **MATCH**

Model: Both multiply line 11 by 85% (0.85), and a zero line 11 gives -0-.

### 16 — Add lines 14 and 15
Status: **MATCH**

Model: The IRS line says 'Add lines 14 and 15'. For married filing separately and lived with your spouse at any time in 2025, line 8 says to 'multiply line 7 by 85% (0.85) and enter the result on line 16', and the restatement follows both rules.

### 17 — Multiply line 1 by 85% (0.85)
Status: **MATCH**

Model: Both multiply line 1 by 85% (0.85).

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **MATCH**

Model: The IRS line says 'Enter the smaller of line 16 or line 17'. When line 1 is zero, line 17 is zero, so entering $0 when there are no benefits gives the same value.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The IRS line says 'Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099', and the restatement enters that same input."
  - key: "2"
    status: MATCH
    reason: "'Multiply line 1 by 50% (0.50)' is the same as multiplying by 1/2. The three refusals cover cases the instructions send to Pub. 590-A/915 ('Exception'), to the Lump-Sum Election in Pub. 915, and to the terrorist-attack disability exclusion (Pub. 3920), and each names what is excluded."
  - key: "3"
    status: MATCH
    reason: "The IRS line says 'Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8'. The restatement adds the same lines, and its signed Dollars type lets a capital loss on line 7a reduce the total."
  - key: "4"
    status: MATCH
    reason: "Both enter the amount, if any, from Form 1040 line 2a."
  - key: "5"
    status: MATCH
    reason: "'Combine lines 2, 3, and 4' is the same as adding lines 2, 3 and 4 with signed amounts."
  - key: "6"
    status: MATCH
    reason: "The IRS line adds 'Schedule 1, lines 11 through 20, and 23 and 25'. The restatement adds only lines 11 and 13, but the scope.schedule1 refusal blocks every other Schedule 1 adjustment and names lines 12, 14 to 20, 23 and 25 as excluded. So within the supported cases the two totals are the same."
  - key: "7"
    status: MATCH
    reason: "The IRS line stops with taxable benefits of -0- when line 6 is not less than line 5, and otherwise subtracts line 6 from line 5. Entering -0- when the result is zero or less sends zero through lines 9 to 18, so line 18 is also -0-."
  - key: "8"
    status: MATCH
    reason: "The IRS amounts are $32,000 for married filing jointly and $25,000 for single, head of household, qualifying surviving spouse, or married filing separately and lived apart all year. For married filing separately and lived together it says 'skip lines 8 through 15', and the restatement enters $0 there and handles that case on line 16."
  - key: "9"
    status: MATCH
    reason: "The IRS line stops with -0- taxable when line 8 is not less than line 7, and otherwise subtracts line 8 from line 7. Using the floored subtraction gives the same final result."
  - key: "10"
    status: MATCH
    reason: "The IRS line says 'Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart', and the restatement uses those amounts. Married filing separately while living together is skipped under line 8, and that case is overridden on line 16."
  - key: "11"
    status: MATCH
    reason: "Both say: subtract line 10 from line 9, and if zero or less, enter -0-."
  - key: "12"
    status: MATCH
    reason: "Both say: enter the smaller of line 9 or line 10."
  - key: "13"
    status: MATCH
    reason: "'Enter one-half of line 12' is the same as multiplying line 12 by 1/2."
  - key: "14"
    status: MATCH
    reason: "Both say: enter the smaller of line 2 or line 13."
  - key: "15"
    status: MATCH
    reason: "Both multiply line 11 by 85% (0.85), and a zero line 11 gives -0-."
  - key: "16"
    status: MATCH
    reason: "The IRS line says 'Add lines 14 and 15'. For married filing separately and lived with your spouse at any time in 2025, line 8 says to 'multiply line 7 by 85% (0.85) and enter the result on line 16', and the restatement follows both rules."
  - key: "17"
    status: MATCH
    reason: "Both multiply line 1 by 85% (0.85)."
  - key: "18"
    status: MATCH
    reason: "The IRS line says 'Enter the smaller of line 16 or line 17'. When line 1 is zero, line 17 is zero, so entering $0 when there are no benefits gives the same value."
```
