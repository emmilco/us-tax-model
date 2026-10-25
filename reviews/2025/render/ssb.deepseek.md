# Render comparison — ssb

The rendered English of every printed line of `Social Security Benefits Worksheet—Lines 6a and 6b` (`rendered/2025/ssb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d93f3a175d41c095503b80ff2b8f5aaa59dc68ee437d8af00c02fc7e50ad532a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 28a23844745911cf6d389a6f3161895bff42580d38d0192310c40870fb35db9b |
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

Model: Matches the IRS line 1 amount from box 5 of all Forms SSA-1099 and RRB-1099.

### 2 — Multiply line 1 by 50% (0.50)
Status: **MATCH**

Model: Multiplies line 1 by 50% (1/2); the refusals properly narrow out the worksheet exceptions and outside-tool cases.

### 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
Status: **MATCH**

Model: Adds the same Form 1040 lines 1z, 2b, 3b, 4b, 5b, 7a, and 8 that the IRS line says to combine.

### 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **MATCH**

Model: Enters the Form 1040 line 2a amount, matching the IRS line 4 instruction.

### 5 — Combine lines 2, 3, and 4
Status: **MATCH**

Model: Adds lines 2, 3, and 4, matching the IRS instruction to combine those lines.

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MATCH**

Model: Matches within supported cases by adding the Schedule 1 adjustment lines and refusing lines 12, 14, and 23 as outside the tool.

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line 
Status: **MATCH**

Model: Computes line 5 minus line 6 with a zero floor, equivalent to the IRS yes/no instruction for line 7.

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **MATCH**

Model: Uses $25,000 or $32,000 by filing status and handles the MFS-lived-with-spouse skip as the IRS line directs.

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line 
Status: **MATCH**

Model: Computes line 7 minus line 8 with a zero floor, equivalent to the IRS yes/no instruction for line 9.

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **MATCH**

Model: Uses $9,000 or $12,000 by filing status and handles the MFS-lived-with-spouse skip as the IRS line directs.

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **MATCH**

Model: Subtracts line 10 from line 9 and floors at zero, matching the IRS line 11.

### 12 — Enter the smaller of line 9 or line 10
Status: **MATCH**

Model: Enters the smaller of line 9 or line 10, matching the IRS line 12.

### 13 — Enter one-half of line 12
Status: **MATCH**

Model: Enters one-half of line 12, matching the IRS line 13.

### 14 — Enter the smaller of line 2 or line 13
Status: **MATCH**

Model: Enters the smaller of line 2 or line 13, matching the IRS line 14.

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **MATCH**

Model: Multiplies line 11 by 85% (0.85), matching the IRS line 15.

### 16 — Add lines 14 and 15
Status: **MATCH**

Model: Adds lines 14 and 15, and applies the line 8 MFS-lived-with-spouse instruction to use line 7 times 85% on line 16.

### 17 — Multiply line 1 by 85% (0.85)
Status: **MATCH**

Model: Multiplies line 1 by 85% (0.85), matching the IRS line 17.

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **MATCH**

Model: Enters the smaller of line 16 or line 17 when benefits exist; the no-benefit case is effectively zero, consistent with line 18.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Matches the IRS line 1 amount from box 5 of all Forms SSA-1099 and RRB-1099."
  - key: "2"
    status: MATCH
    reason: "Multiplies line 1 by 50% (1/2); the refusals properly narrow out the worksheet exceptions and outside-tool cases."
  - key: "3"
    status: MATCH
    reason: "Adds the same Form 1040 lines 1z, 2b, 3b, 4b, 5b, 7a, and 8 that the IRS line says to combine."
  - key: "4"
    status: MATCH
    reason: "Enters the Form 1040 line 2a amount, matching the IRS line 4 instruction."
  - key: "5"
    status: MATCH
    reason: "Adds lines 2, 3, and 4, matching the IRS instruction to combine those lines."
  - key: "6"
    status: MATCH
    reason: "Matches within supported cases by adding the Schedule 1 adjustment lines and refusing lines 12, 14, and 23 as outside the tool."
  - key: "7"
    status: MATCH
    reason: "Computes line 5 minus line 6 with a zero floor, equivalent to the IRS yes/no instruction for line 7."
  - key: "8"
    status: MATCH
    reason: "Uses $25,000 or $32,000 by filing status and handles the MFS-lived-with-spouse skip as the IRS line directs."
  - key: "9"
    status: MATCH
    reason: "Computes line 7 minus line 8 with a zero floor, equivalent to the IRS yes/no instruction for line 9."
  - key: "10"
    status: MATCH
    reason: "Uses $9,000 or $12,000 by filing status and handles the MFS-lived-with-spouse skip as the IRS line directs."
  - key: "11"
    status: MATCH
    reason: "Subtracts line 10 from line 9 and floors at zero, matching the IRS line 11."
  - key: "12"
    status: MATCH
    reason: "Enters the smaller of line 9 or line 10, matching the IRS line 12."
  - key: "13"
    status: MATCH
    reason: "Enters one-half of line 12, matching the IRS line 13."
  - key: "14"
    status: MATCH
    reason: "Enters the smaller of line 2 or line 13, matching the IRS line 14."
  - key: "15"
    status: MATCH
    reason: "Multiplies line 11 by 85% (0.85), matching the IRS line 15."
  - key: "16"
    status: MATCH
    reason: "Adds lines 14 and 15, and applies the line 8 MFS-lived-with-spouse instruction to use line 7 times 85% on line 16."
  - key: "17"
    status: MATCH
    reason: "Multiplies line 1 by 85% (0.85), matching the IRS line 17."
  - key: "18"
    status: MATCH
    reason: "Enters the smaller of line 16 or line 17 when benefits exist; the no-benefit case is effectively zero, consistent with line 18."
```
