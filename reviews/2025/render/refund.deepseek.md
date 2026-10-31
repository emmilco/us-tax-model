# Render comparison — refund

The rendered English of every printed line of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` (`rendered/2025/refund.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4fa4491b4588d1e4a1ca9e8b2408ce5c4611b305a7e1d6a8958b1979f05ec53f |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | eb01f3f0f28ed0f6129229faa18e94ccc37f2c176bfc49be1d74de4360a82bbc |
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

Model: The restatement omits required Pub. 525 exceptions: the worksheet cannot be used if the 2025 refund is for a tax year other than 2024 or if the filer made the last 2024 estimated state or local income tax payment in 2025; the IRS says to use Itemized Deduction Recoveries instead.

Ruling: scope; i1040gi p. 89, Line 1, Exception: "1. You received a refund in 2025 that is for a tax year other than 2024", "2. You received a refund other than an income tax refund, such as a general sales tax or real property tax refund, in 2025 of an amount deducted or credit claimed in an earlier year" and "5. You made your last payment of 2024 estimated state or local income tax in 2025". Exceptions 1 and 5 are refused by refund.not_2024 ("Is any of these refunds for a tax year other than 2024 (box 3 of Form 1099-G), or did you pay any of your 2024 state or local income tax in 2025?", reworded under BUG-0230 and now wider than exception 5), whose refusal sits on refund.taxable, the line Schedule 1 line 1 enters, so no such refund reaches line 1 on a completed return; the model saw only line 1's two refusals (exc_tax, exc_who: items 3, 4, 6 to 9). Exception 2 is outside refund.received ("State or local income tax refunds, credits or offsets") and refused by scope.schedule1 ("a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund (for example a refund of general sales tax, real estate tax or personal property tax ...)"): refusal located on the reading line. The smaller of refund.received and 2024 Schedule A line 5d matches the worksheet (amb.2025.refund_cap_5d (owner decision D6(a), Stage 16: cap line 1 at 2024 Schedule A line 5d as printed; a refund above the income tax part is exception 4 territory, refund.exc_tax)). Same as the archived ruling, rechecked against the reworded screen. Project retained. Fix round 5: the restatement of this line is word for word the one ruled in fix round 2 (the render was rerun for a change in a shared line elsewhere), the reply raises the same points, and refund.not_2024, refund.received, scope.schedule1 and the register entries quoted were rechecked in the current forms.

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **MATCH**

Model: Subtracting 2024 Schedule A line 5e from line 5d, with a zero floor, matches the worksheet's Yes branch; the refusal correctly blocks line 5e exceeding line 5d.

### 3 — Subtract line 2 from line 1
Status: **MATCH**

Model: The IRS line subtracts line 2 from line 1 only when line 1 is more than line 2 and otherwise stops with none taxable; the zero-floor subtraction produces the same taxable amount.

### 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **MATCH**

Model: Directly uses 2024 Schedule A line 17 total itemized deductions.

### 5 — Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-
Status: **MATCH**

Model: The filing-status amounts match the worksheet: single/MFS $14,600, MFJ/QSS $29,200, HOH $21,900.

### 6 — Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your
Status: **MISMATCH**

Restated: Add helper "The amount for the box "You were born before January 2, 1960" (zero if not checked)", helper "The amount for the box "You are blind" (zero if not checked)", helper "The amount for the box "Spouse was born before January 2, 1960" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)", and helper "The amount for the box "Spouse is blind" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)".

Model: IRS line 6 says 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)' and for MFS permits spouse boxes only if the spouse had no income, isn't filing, and can't be claimed; the restatement just adds box amounts and omits the MFS spouse eligibility condition.

Ruling: representation; i1040gi p. 90, worksheet line 6: "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)" and footnote "*If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent on another person’s return"; p. 33, Line 12d: "Don’t check any boxes for your spouse if your filing status is head of household". The married filing separately condition is in the spouse questions themselves (refund.spouse_born, refund.spouse_blind: "If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return"), as the footnote says; amb.2025.refund_boxes_2024 records the status reading; the restatement's status condition zeroes the spouse boxes for single, head of household and qualifying surviving spouse, and the footnote's further conditions for a separate return are answered in the questions, not in the expression. Each per-box helper is refund.per_box when its box is checked and zero otherwise, and refund.per_box is labelled and encoded "$1,550 ($1,950 if your 2024 filing status was single or head of household)" (single/hoh -> refund.box_unmarried $1,950; mfj/mfs/qss -> refund.box_married $1,550), so the sum is the number of boxes times the amount. Same as the archived ruling. Project retained. Fix round 5: the restatement of this line is word for word the one ruled in fix round 2 (the render was rerun for a change in a shared line elsewhere), the reply raises the same points, and refund.per_box, refund.spouse_born, refund.spouse_blind and amb.2025.refund_boxes_2024 were rechecked in the current forms.

### 7 — Add lines 5 and 6
Status: **MATCH**

Model: Adds lines 5 and 6 exactly as the worksheet line says.

### 8 — Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and
Status: **MATCH**

Model: The normal branch subtracts line 7 from line 4 with a zero floor, and the MFS branch follows the note to skip lines 5-7 and use line 4 when the spouse itemized.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **MATCH**

Model: The IRS line is the smaller of line 3 or line 8; the extra line-1-more-than-line-2 condition only reproduces the earlier STOP case, so the result is unchanged.

## Raw response

```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement omits required Pub. 525 exceptions: the worksheet cannot be used if the 2025 refund is for a tax year other than 2024 or if the filer made the last 2024 estimated state or local income tax payment in 2025; the IRS says to use Itemized Deduction Recoveries instead."
  - key: "2"
    status: MATCH
    reason: "Subtracting 2024 Schedule A line 5e from line 5d, with a zero floor, matches the worksheet's Yes branch; the refusal correctly blocks line 5e exceeding line 5d."
  - key: "3"
    status: MATCH
    reason: "The IRS line subtracts line 2 from line 1 only when line 1 is more than line 2 and otherwise stops with none taxable; the zero-floor subtraction produces the same taxable amount."
  - key: "4"
    status: MATCH
    reason: "Directly uses 2024 Schedule A line 17 total itemized deductions."
  - key: "5"
    status: MATCH
    reason: "The filing-status amounts match the worksheet: single/MFS $14,600, MFJ/QSS $29,200, HOH $21,900."
  - key: "6"
    status: MISMATCH
    reason: "IRS line 6 says 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)' and for MFS permits spouse boxes only if the spouse had no income, isn't filing, and can't be claimed; the restatement just adds box amounts and omits the MFS spouse eligibility condition."
  - key: "7"
    status: MATCH
    reason: "Adds lines 5 and 6 exactly as the worksheet line says."
  - key: "8"
    status: MATCH
    reason: "The normal branch subtracts line 7 from line 4 with a zero floor, and the MFS branch follows the note to skip lines 5-7 and use line 4 when the spouse itemized."
  - key: "9"
    status: MATCH
    reason: "The IRS line is the smaller of line 3 or line 8; the extra line-1-more-than-line-2 condition only reproduces the earlier STOP case, so the result is unchanged."
```
