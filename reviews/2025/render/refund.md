# Render comparison — refund

The rendered English of every printed line of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` (`rendered/2025/refund.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 62f69e18c59ce115c4f5d06567fbd962f287d7161ea6cc2a479c8e7e30cf03bd |
| subject sha256 | 5d0982533b132432ca85e78e925207b136acb2d4bccc973bc90d61fb1af0414e |
| lines judged | 9 |
| match / mismatch / unclear / missing | 7 / 1 / 1 / 0 |
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

Model: Taking the smaller of the 2025 refunds received and 2024 Schedule A line 5d matches the worksheet's 'But don't enter more than the amount... shown on your 2024 Schedule A, line 5d'. But the refusals leave out some Exception cases, so the worksheet would still be used for them: '1. You received a refund in 2025 that is for a tax year other than 2024' and '5. You made your last payment of 2024 estimated state or local income tax in 2025.' Exception 2 ('a refund other than an income tax refund') is also not refused; the input label limits the amount to income tax refunds, but no refusal names that case.

Ruling: refusal located elsewhere; project retained. The cases named are refused on the line that reads this one: refund.taxable, which Schedule 1 line 1 enters, refuses on refund.not_2024 ("Is any of these refunds for a tax year other than 2024 (box 3 of Form 1099-G), or did you make your last payment of 2024 estimated state or local income tax in 2025?"), exceptions 1 and 5 (i1040gi p. 89, Line 1, "1. You received a refund in 2025 that is for a tax year other than 2024", "5. You made your last payment of 2024 estimated state or local income tax in 2025"), and gives zero, without the worksheet, unless you itemized for 2024 and deducted income rather than sales taxes (refund.worksheet; p. 88, Line 1, "If the refund was for a tax you paid in 2024 and you deducted state and local income taxes on your 2024 Schedule A, use the State and Local Income Tax Refund Worksheet"). Exceptions 3, 4 and 6 to 9 are the two refusals on this line (refund.exc_tax, refund.exc_who), exception 2 is refused by the Schedule 1 screen (scope.schedule1, which names other recoveries of amounts deducted or credited in an earlier year).

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **MATCH**

Model: The worksheet subtracts 2024 Schedule A line 5e from line 5d when 5d is more than 5e. Otherwise, line 1 goes to line 3 unchanged, which a line 2 of zero also produces. The refusal covers the case where line 5e is more than line 5d.

### 3 — Subtract line 2 from line 1
Status: **MATCH**

Model: 'Yes. Subtract line 2 from line 1.' In the 'No... None of your refund is taxable' case, the program's floor of zero plus the line 9 gate give zero.

### 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **MATCH**

Model: 'Enter your total itemized deductions from your 2024 Schedule A, line 17.'

### 5 — Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-
Status: **MATCH**

Model: The amounts by filing status match: single or married filing separately $14,600; married filing jointly or qualifying surviving spouse $29,200; head of household $21,900.

### 6 — Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your
Status: **UNCLEAR**

Restated: Add helper "The amount for the box "You were born before January 2, 1960" (zero if not checked)", helper "The amount for the box "You are blind" (zero if not checked)", helper "The amount for the box "Spouse was born before January 2, 1960" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)", and helper "The amount for the box "Spouse is blind" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)".

Model: The worksheet says 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)'. The restatement adds per-box 'amounts' that are not defined in the glossary, so the $1,550/$1,950 rates can't be checked. The married-filing-separately spouse-box condition ('only if your spouse had no income, isn't filing a return, and can't be claimed as a dependent') is also not shown in the restatement.

Ruling: representation; project retained. Each per-box helper is refund.per_box when its box is checked and zero otherwise, and refund.per_box is $1,550, or $1,950 when the 2024 status was single or head of household (refund.box_married, refund.box_unmarried), so the sum is the number of boxes times the amount (i1040gi p. 90, State and Local Income Tax Refund Worksheet, line 6, "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)"). The married filing separately condition for the spouse boxes is in the spouse questions themselves (refund.spouse_born, refund.spouse_blind: "answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return"), as the footnote says ("you can check the boxes for your spouse only if your spouse had no income, isn't filing a return, and can't be claimed as a dependent"); amb.2025.refund_boxes_2024 records the reading.

### 7 — Add lines 5 and 6
Status: **MATCH**

Model: 'Add lines 5 and 6.'

### 8 — Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and 
Status: **MATCH**

Model: 'Yes. Subtract line 7 from line 4'. The 'No... STOP' case gives zero, which then flows to zero on line 9. For married filing separately with a spouse who itemized, the Note says to 'skip lines 5 through 7, enter the amount from line 4 on line 8', which is what the restatement does.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **MATCH**

Model: 'Enter the smaller of line 3 or line 8'. The program enters zero when line 1 is not more than line 2, matching line 3's 'No. STOP None of your refund is taxable.'

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "Taking the smaller of the 2025 refunds received and 2024 Schedule A line 5d matches the worksheet's 'But don't enter more than the amount... shown on your 2024 Schedule A, line 5d'. But the refusals leave out some Exception cases, so the worksheet would still be used for them: '1. You received a refund in 2025 that is for a tax year other than 2024' and '5. You made your last payment of 2024 estimated state or local income tax in 2025.' Exception 2 ('a refund other than an income tax refund') is also not refused; the input label limits the amount to income tax refunds, but no refusal names that case."
  - key: "2"
    status: MATCH
    reason: "The worksheet subtracts 2024 Schedule A line 5e from line 5d when 5d is more than 5e. Otherwise, line 1 goes to line 3 unchanged, which a line 2 of zero also produces. The refusal covers the case where line 5e is more than line 5d."
  - key: "3"
    status: MATCH
    reason: "'Yes. Subtract line 2 from line 1.' In the 'No... None of your refund is taxable' case, the program's floor of zero plus the line 9 gate give zero."
  - key: "4"
    status: MATCH
    reason: "'Enter your total itemized deductions from your 2024 Schedule A, line 17.'"
  - key: "5"
    status: MATCH
    reason: "The amounts by filing status match: single or married filing separately $14,600; married filing jointly or qualifying surviving spouse $29,200; head of household $21,900."
  - key: "6"
    status: UNCLEAR
    reason: "The worksheet says 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)'. The restatement adds per-box 'amounts' that are not defined in the glossary, so the $1,550/$1,950 rates can't be checked. The married-filing-separately spouse-box condition ('only if your spouse had no income, isn't filing a return, and can't be claimed as a dependent') is also not shown in the restatement."
  - key: "7"
    status: MATCH
    reason: "'Add lines 5 and 6.'"
  - key: "8"
    status: MATCH
    reason: "'Yes. Subtract line 7 from line 4'. The 'No... STOP' case gives zero, which then flows to zero on line 9. For married filing separately with a spouse who itemized, the Note says to 'skip lines 5 through 7, enter the amount from line 4 on line 8', which is what the restatement does."
  - key: "9"
    status: MATCH
    reason: "'Enter the smaller of line 3 or line 8'. The program enters zero when line 1 is not more than line 2, matching line 3's 'No. STOP None of your refund is taxable.'"
```
```
