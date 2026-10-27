# Render comparison — refund

The rendered English of every printed line of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` (`rendered/2025/refund.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4fa4491b4588d1e4a1ca9e8b2408ce5c4611b305a7e1d6a8958b1979f05ec53f |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 91b3cbebdd7d66acede0e17c69121bdfe9f004247da995655c6e3a5dd53cc155 |
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

Model: The min(refund, 2024 Schedule A line 5d) computation is right, but the IRS says to use Pub. 525 instead of this worksheet if the refund is for a tax year other than 2024 or if the last 2024 estimated state or local income tax payment was made in 2025; the refusal rules omit those exceptions.

Ruling: scope; i1040gi p. 89, Line 1, Exception: "See Itemized Deduction Recoveries in Pub. 525 instead of using the State and Local Income Tax Refund Worksheet ... if any of the following applies", "1. You received a refund in 2025 that is for a tax year other than 2024" and "5. You made your last payment of 2024 estimated state or local income tax in 2025". Both are screened by refund.not_2024 ("Is any of these refunds for a tax year other than 2024 (box 3 of Form 1099-G), or did you make your last payment of 2024 estimated state or local income tax in 2025?"), whose refusal sits on refund.taxable, the line Schedule 1 line 1 enters, so no such refund reaches a completed return through line 1. The refusal is located on the reading line rather than line 1 itself; the model saw only line 1's two refusals (exc_tax, exc_who: items 3, 4, 6-9). The min with 2024 Schedule A line 5d matches ("But don't enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d"). Same as the archived ruling, rechecked.

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **MATCH**

Model: It computes line 5d less line 5e with a zero floor, matching the worksheet's line 2 subtraction; the line5e > line5d refusal addresses an inconsistent entry.

### 3 — Subtract line 2 from line 1
Status: **MATCH**

Model: It subtracts line 2 from line 1 with a zero floor, matching the worksheet's yes branch and the none-taxable result when line 1 is not greater than line 2.

### 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **MATCH**

Model: It uses the 2024 Schedule A line 17 total itemized deductions, as the worksheet says.

### 5 — Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-
Status: **MATCH**

Model: The filing-status amounts match the worksheet: $14,600 for single/MFS, $29,200 for MFJ/QSS, and $21,900 for HOH.

### 6 — Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your
Status: **MISMATCH**

Restated: Add helper "The amount for the box "You were born before January 2, 1960" (zero if not checked)", helper "The amount for the box "You are blind" (zero if not checked)", helper "The amount for the box "Spouse was born before January 2, 1960" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)", and helper "The amount for the box "Spouse is blind" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)".

Model: IRS line 6 says to multiply the number of boxes checked by $1,550 ($1,950 if the 2024 status was single or head of household), and for MFS the spouse boxes count only if the spouse had no income, isn’t filing, and can’t be claimed as a dependent; the restatement adds per-box amounts and omits the MFS conditions.

Ruling: representation; i1040gi p. 90, State and Local Income Tax Refund Worksheet, line 6: "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)". Each per-box helper is refund.per_box ("$1,550 ($1,950 if your 2024 filing status was single or head of household)": single/hoh -> refund.box_unmarried $1,950; mfj/mfs/qss -> refund.box_married $1,550) when its box is checked and zero otherwise, so the sum is boxes times the rate. The MFS footnote ("If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn't filing a return, and can't be claimed as a dependent on another person's return") is carried in the spouse questions refund.spouse_born and refund.spouse_blind ("If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent"). The model's "adds per-box amounts" is the same quantity as the count times the rate. On the qualifying-surviving-spouse point (spouse boxes zero unless 2024 status MFJ or MFS): ambiguity, amb.2025.refund_boxes_2024 (chosen reading: "ask the spouse questions only when the 2024 filing status was married filing jointly or married filing separately"); the worksheet is silent on QSS, and on the 2024 Form 1040 the spouse boxes belong to a spouse on the return.

### 7 — Add lines 5 and 6
Status: **MATCH**

Model: It adds lines 5 and 6, as the worksheet says.

### 8 — Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and
Status: **MATCH**

Model: It returns line 4 when 2024 MFS spouse itemized and otherwise subtracts line 7 from line 4 with a zero floor, matching the line 8 note and computation.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **MATCH**

Model: It enters zero when line 1 is not more than line 2 and otherwise the smaller of line 3 or line 8, matching the worksheet's taxable-refund line.

## Raw response

```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The min(refund, 2024 Schedule A line 5d) computation is right, but the IRS says to use Pub. 525 instead of this worksheet if the refund is for a tax year other than 2024 or if the last 2024 estimated state or local income tax payment was made in 2025; the refusal rules omit those exceptions."
  - key: "2"
    status: MATCH
    reason: "It computes line 5d less line 5e with a zero floor, matching the worksheet's line 2 subtraction; the line5e > line5d refusal addresses an inconsistent entry."
  - key: "3"
    status: MATCH
    reason: "It subtracts line 2 from line 1 with a zero floor, matching the worksheet's yes branch and the none-taxable result when line 1 is not greater than line 2."
  - key: "4"
    status: MATCH
    reason: "It uses the 2024 Schedule A line 17 total itemized deductions, as the worksheet says."
  - key: "5"
    status: MATCH
    reason: "The filing-status amounts match the worksheet: $14,600 for single/MFS, $29,200 for MFJ/QSS, and $21,900 for HOH."
  - key: "6"
    status: MISMATCH
    reason: "IRS line 6 says to multiply the number of boxes checked by $1,550 ($1,950 if the 2024 status was single or head of household), and for MFS the spouse boxes count only if the spouse had no income, isn’t filing, and can’t be claimed as a dependent; the restatement adds per-box amounts and omits the MFS conditions."
  - key: "7"
    status: MATCH
    reason: "It adds lines 5 and 6, as the worksheet says."
  - key: "8"
    status: MATCH
    reason: "It returns line 4 when 2024 MFS spouse itemized and otherwise subtracts line 7 from line 4 with a zero floor, matching the line 8 note and computation."
  - key: "9"
    status: MATCH
    reason: "It enters zero when line 1 is not more than line 2 and otherwise the smaller of line 3 or line 8, matching the worksheet's taxable-refund line."
```
