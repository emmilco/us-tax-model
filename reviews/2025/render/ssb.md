# Render comparison — ssb

The rendered English of every printed line of `Social Security Benefits Worksheet—Lines 6a and 6b` (`rendered/2025/ssb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 74b96d2b6c0024ca6216e915dc9f48245f9360d636ac0c3d8de90c6f9e7e727b |
| subject sha256 | 8f8000edb61eeaccbb106b30009ca8503893bd119c8d8b2f7184cff5dd90dea6 |
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

Model: The IRS line says to enter the total from box 5 of all Forms SSA-1099 and RRB-1099. The helper is exactly that input.

### 2 — Multiply line 1 by 50% (0.50)
Status: **MATCH**

Model: 1/2 equals the IRS's '50% (0.50)'. The refusals name the cases the IRS text excludes or sends elsewhere: the Exception list (Pub. 590-A/Pub. 915), the terrorist-attack disability exclusion (Pub. 3920) and the lump-sum election (Pub. 915).

### 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
Status: **MATCH**

Model: The IRS says 'Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8'. The restatement adds the same lines as signed Dollars, so a loss on 7a is allowed for.

### 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **MATCH**

Model: The IRS says 'Enter the amount, if any, from Form 1040 or 1040-SR, line 2a'. The restatement does the same.

### 5 — Combine lines 2, 3, and 4
Status: **MATCH**

Model: The IRS says 'Combine lines 2, 3, and 4'. The restatement adds the same three lines.

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MATCH**

Model: The IRS says 'Schedule 1, lines 11 through 20, and 23 and 25'. The restatement keeps lines 11, 13, 15, 16 and 17, and the scope.schedule1 refusal names lines 12, 14, 18 to 20, 23 and 25 as outside the tool.

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line 
Status: **MATCH**

Model: The IRS says to stop and enter -0- on line 6b if line 6 is not less than line 5, otherwise to subtract line 6 from line 5. Flooring line 7 at zero carries through to a line 18 of zero, so the result is the same.

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **MATCH**

Model: The thresholds match the IRS text: $32,000 for married filing jointly; $25,000 for single, HOH, QSS, or MFS who lived apart all year. For MFS who lived with the spouse, the IRS says to skip lines 8 through 15, and those lines do not reach line 16 in that case.

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line 
Status: **MATCH**

Model: The IRS says to stop with -0- if line 8 is not less than line 7, otherwise to subtract line 8 from line 7. Flooring at zero makes lines 11 through 16, and so line 18, zero, which is the same result.

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **MATCH**

Model: The amounts match the IRS text: '$12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart'. The MFS lived-together case skips this line.

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **MATCH**

Model: The IRS says 'Subtract line 10 from line 9. If zero or less, enter -0-'. The restatement is the same.

### 12 — Enter the smaller of line 9 or line 10
Status: **MATCH**

Model: The IRS says 'Enter the smaller of line 9 or line 10'. The restatement is the same.

### 13 — Enter one-half of line 12
Status: **MATCH**

Model: The IRS says 'Enter one-half of line 12'. The restatement multiplies line 12 by 1/2, which is the same.

### 14 — Enter the smaller of line 2 or line 13
Status: **MATCH**

Model: The IRS says 'Enter the smaller of line 2 or line 13'. The restatement is the same.

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **MATCH**

Model: The IRS says 'Multiply line 11 by 85% (0.85)'. The restatement uses the same operand and rate.

### 16 — Add lines 14 and 15
Status: **MATCH**

Model: The IRS says 'Add lines 14 and 15', and for married filing separately living with the spouse at any time in 2025: 'multiply line 7 by 85% (0.85) and enter the result on line 16'. The restatement follows both branches.

### 17 — Multiply line 1 by 85% (0.85)
Status: **MATCH**

Model: The IRS says 'Multiply line 1 by 85% (0.85)'. The restatement is the same.

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **MATCH**

Model: The IRS says 'Enter the smaller of line 16 or line 17'. The restatement uses $0 when line 1 is zero, and in that case line 17 is zero anyway, so the value is the same.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The IRS line says to enter the total from box 5 of all Forms SSA-1099 and RRB-1099. The helper is exactly that input."
  - key: "2"
    status: MATCH
    reason: "1/2 equals the IRS's '50% (0.50)'. The refusals name the cases the IRS text excludes or sends elsewhere: the Exception list (Pub. 590-A/Pub. 915), the terrorist-attack disability exclusion (Pub. 3920) and the lump-sum election (Pub. 915)."
  - key: "3"
    status: MATCH
    reason: "The IRS says 'Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8'. The restatement adds the same lines as signed Dollars, so a loss on 7a is allowed for."
  - key: "4"
    status: MATCH
    reason: "The IRS says 'Enter the amount, if any, from Form 1040 or 1040-SR, line 2a'. The restatement does the same."
  - key: "5"
    status: MATCH
    reason: "The IRS says 'Combine lines 2, 3, and 4'. The restatement adds the same three lines."
  - key: "6"
    status: MATCH
    reason: "The IRS says 'Schedule 1, lines 11 through 20, and 23 and 25'. The restatement keeps lines 11, 13, 15, 16 and 17, and the scope.schedule1 refusal names lines 12, 14, 18 to 20, 23 and 25 as outside the tool."
  - key: "7"
    status: MATCH
    reason: "The IRS says to stop and enter -0- on line 6b if line 6 is not less than line 5, otherwise to subtract line 6 from line 5. Flooring line 7 at zero carries through to a line 18 of zero, so the result is the same."
  - key: "8"
    status: MATCH
    reason: "The thresholds match the IRS text: $32,000 for married filing jointly; $25,000 for single, HOH, QSS, or MFS who lived apart all year. For MFS who lived with the spouse, the IRS says to skip lines 8 through 15, and those lines do not reach line 16 in that case."
  - key: "9"
    status: MATCH
    reason: "The IRS says to stop with -0- if line 8 is not less than line 7, otherwise to subtract line 8 from line 7. Flooring at zero makes lines 11 through 16, and so line 18, zero, which is the same result."
  - key: "10"
    status: MATCH
    reason: "The amounts match the IRS text: '$12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart'. The MFS lived-together case skips this line."
  - key: "11"
    status: MATCH
    reason: "The IRS says 'Subtract line 10 from line 9. If zero or less, enter -0-'. The restatement is the same."
  - key: "12"
    status: MATCH
    reason: "The IRS says 'Enter the smaller of line 9 or line 10'. The restatement is the same."
  - key: "13"
    status: MATCH
    reason: "The IRS says 'Enter one-half of line 12'. The restatement multiplies line 12 by 1/2, which is the same."
  - key: "14"
    status: MATCH
    reason: "The IRS says 'Enter the smaller of line 2 or line 13'. The restatement is the same."
  - key: "15"
    status: MATCH
    reason: "The IRS says 'Multiply line 11 by 85% (0.85)'. The restatement uses the same operand and rate."
  - key: "16"
    status: MATCH
    reason: "The IRS says 'Add lines 14 and 15', and for married filing separately living with the spouse at any time in 2025: 'multiply line 7 by 85% (0.85) and enter the result on line 16'. The restatement follows both branches."
  - key: "17"
    status: MATCH
    reason: "The IRS says 'Multiply line 1 by 85% (0.85)'. The restatement is the same."
  - key: "18"
    status: MATCH
    reason: "The IRS says 'Enter the smaller of line 16 or line 17'. The restatement uses $0 when line 1 is zero, and in that case line 17 is zero anyway, so the value is the same."
```
```
