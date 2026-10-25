# Render comparison — refund

The rendered English of every printed line of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` (`rendered/2025/refund.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 62f69e18c59ce115c4f5d06567fbd962f287d7161ea6cc2a479c8e7e30cf03bd |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 5d0982533b132432ca85e78e925207b136acb2d4bccc973bc90d61fb1af0414e |
| lines judged | 9 |
| match / mismatch / unclear / missing | 7 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 33, 88, 89, 90 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 88, 89 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1099g | Rev. March 2024 (continuous-use form for calendar year 2025; the December 2026 revision is first used for 2026) | 1, 2, 3, 4, 5, 6 | whole document | c3505294585e00ec5e957f73aa97dee32ad4b6916cd3eb48fef7f3c79f123270 | 5 | 49cc781de5cf6d881cc347361880de4b4b20fca0f13397bc94c94e84a20cff6d |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 24 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 24 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### 1 — Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter mo
Status: **MISMATCH**

Restated: Enter the smaller of helper "State or local income tax refunds, credits or offsets you received in 2025" or helper "The amount on your 2024 Schedule A, line 5d".

Model: The IRS Exception also requires Pub. 525 when 'You received a refund in 2025 that is for a tax year other than 2024' or 'You made your last payment of 2024 estimated state or local income tax in 2025'; the program's refusals do not exclude those cases.

Ruling: open

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **MATCH**

Model: Matches the line 2 subtraction and zero floor; the line5e>5d refusal correctly handles an amount inconsistent with 2024 Schedule A line 5e being the smaller of line 5d and the limit.

### 3 — Subtract line 2 from line 1
Status: **MATCH**

Model: Subtracting line 2 from line 1 with a zero floor gives the same result as the worksheet's 'No' STOP branch (none taxable).

### 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **MATCH**

Model: Enters the 2024 Schedule A line 17 total itemized deductions as the worksheet says.

### 5 — Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-
Status: **MATCH**

Model: The filing-status amounts ($14,600 single/MFS, $29,200 MFJ/QSS, $21,900 HOH) match the worksheet.

### 6 — Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your
Status: **MISMATCH**

Restated: Add helper "The amount for the box "You were born before January 2, 1960" (zero if not checked)", helper "The amount for the box "You are blind" (zero if not checked)", helper "The amount for the box "Spouse was born before January 2, 1960" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)", and helper "The amount for the box "Spouse is blind" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)".

Model: The IRS line says 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)' and for married filing separately allows spouse boxes only if 'your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent'; the restatement only adds helper amounts and zeroes spouse boxes for statuses other than MFJ/MFS, omitting those conditions.

Ruling: open

### 7 — Add lines 5 and 6
Status: **MATCH**

Model: Adds lines 5 and 6 as the worksheet says.

### 8 — Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and 
Status: **MATCH**

Model: Matches the line 8 subtraction/STOP result and the special MFS rule using line 4 when the spouse itemized in 2024.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **MATCH**

Model: Enters the smaller of line 3 or line 8, with zero when line 1 is not more than line 2, matching the worksheet's taxable-part line and STOP branch.

## Raw response

```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The IRS Exception also requires Pub. 525 when 'You received a refund in 2025 that is for a tax year other than 2024' or 'You made your last payment of 2024 estimated state or local income tax in 2025'; the program's refusals do not exclude those cases."
  - key: "2"
    status: MATCH
    reason: "Matches the line 2 subtraction and zero floor; the line5e>5d refusal correctly handles an amount inconsistent with 2024 Schedule A line 5e being the smaller of line 5d and the limit."
  - key: "3"
    status: MATCH
    reason: "Subtracting line 2 from line 1 with a zero floor gives the same result as the worksheet's 'No' STOP branch (none taxable)."
  - key: "4"
    status: MATCH
    reason: "Enters the 2024 Schedule A line 17 total itemized deductions as the worksheet says."
  - key: "5"
    status: MATCH
    reason: "The filing-status amounts ($14,600 single/MFS, $29,200 MFJ/QSS, $21,900 HOH) match the worksheet."
  - key: "6"
    status: MISMATCH
    reason: "The IRS line says 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)' and for married filing separately allows spouse boxes only if 'your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent'; the restatement only adds helper amounts and zeroes spouse boxes for statuses other than MFJ/MFS, omitting those conditions."
  - key: "7"
    status: MATCH
    reason: "Adds lines 5 and 6 as the worksheet says."
  - key: "8"
    status: MATCH
    reason: "Matches the line 8 subtraction/STOP result and the special MFS rule using line 4 when the spouse itemized in 2024."
  - key: "9"
    status: MATCH
    reason: "Enters the smaller of line 3 or line 8, with zero when line 1 is not more than line 2, matching the worksheet's taxable-part line and STOP branch."
```
