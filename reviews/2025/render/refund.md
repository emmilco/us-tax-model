# Render comparison — refund

The rendered English of every printed line of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` (`rendered/2025/refund.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 426245555b278bfc18ada64f569fad3fca8aa4eb4282c85f898afc290d05da79 |
| subject sha256 | ef029ff307f2d24ccfc93e74a7d4ea97f21461fa75342ff059fbf824853f3c5f |
| lines judged | 9 |
| match / mismatch / unclear / missing | 7 / 1 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 33, 88, 89, 90 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 88, 89 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 24, 25 | cited pages | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 24, 25 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |
| f1099g | Rev. March 2024 (continuous-use form for calendar year 2025; the December 2026 revision is first used for 2026) | 1, 2, 3, 4, 5, 6 | whole document | c3505294585e00ec5e957f73aa97dee32ad4b6916cd3eb48fef7f3c79f123270 | 5 | 49cc781de5cf6d881cc347361880de4b4b20fca0f13397bc94c94e84a20cff6d |

## Lines

### 1 — Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter mo
Status: **MISMATCH**

Restated: Enter the smaller of helper "State or local income tax refunds, credits or offsets you received in 2025" or helper "The amount on your 2024 Schedule A, line 5d".

Model: Taking the smaller of the 1099-G refund and 2024 Schedule A line 5d matches the worksheet. But neither refusal covers three Pub. 525 exceptions: "You received a refund in 2025 that is for a tax year other than 2024", "You made your last payment of 2024 estimated state or local income tax in 2025", and the precondition that the refund be "for a tax you paid in 2024 and you deducted state and local income taxes on your 2024 Schedule A". The refund input counts every refund received in 2025, so those cases get computed here instead of being sent to Pub. 525.

Ruling: refusal located elsewhere; project retained. The cases named are refused on the line that reads this one: refund.taxable, which Schedule 1 line 1 enters, refuses on refund.not_2024 ("Is any of these refunds for a tax year other than 2024 (box 3 of Form 1099-G), or did you make your last payment of 2024 estimated state or local income tax in 2025?"), exceptions 1 and 5 (i1040gi p. 89, Line 1, "1. You received a refund in 2025 that is for a tax year other than 2024", "5. You made your last payment of 2024 estimated state or local income tax in 2025"), and gives zero, without the worksheet, unless you itemized for 2024 and deducted income rather than sales taxes (refund.worksheet; p. 88, Line 1, "If the refund was for a tax you paid in 2024 and you deducted state and local income taxes on your 2024 Schedule A, use the State and Local Income Tax Refund Worksheet"). Exceptions 3, 4 and 6 to 9 are the two refusals on this line (refund.exc_tax, refund.exc_who), exception 2 is refused on Schedule 1 line 1 (refund.other).

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **MATCH**

Model: The worksheet says "Subtract the amount on your 2024 Schedule A, line 5e, from" the line 5d amount when 5d is more than 5e. On "No", line 1 goes straight to line 3, which is what a zero line 2 does in the next step.

### 3 — Subtract line 2 from line 1
Status: **MATCH**

Model: The worksheet says "Subtract line 2 from line 1" when line 1 is more, and STOP (nothing taxable) otherwise. Entering zero gives the same final result, because line 9 then becomes zero.

### 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **MATCH**

Model: The worksheet says "Enter your total itemized deductions from your 2024 Schedule A, line 17."

### 5 — Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-
Status: **MATCH**

Model: The amounts by filing status match the worksheet: "Single or married filing separately—$14,600; Married filing jointly or qualifying surviving spouse—$29,200; Head of household—$21,900."

### 6 — Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your
Status: **UNCLEAR**

Restated: Add helper "The amount for the box "You were born before January 2, 1960" (zero if not checked)", helper "The amount for the box "You are blind" (zero if not checked)", helper "The amount for the box "Spouse was born before January 2, 1960" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)", and helper "The amount for the box "Spouse is blind" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)".

Model: The worksheet says to "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)". The per-box helper amounts are not defined in the glossary, so the rates cannot be checked. The restatement also leaves out the married-filing-separately rule that spouse boxes count only "if your spouse had no income, isn't filing a return, and can't be claimed as a dependent".

Ruling: representation; project retained. Each per-box helper is refund.per_box when its box is checked and zero otherwise, and refund.per_box is $1,550, or $1,950 when the 2024 status was single or head of household (refund.box_married, refund.box_unmarried), so the sum is the number of boxes times the amount (i1040gi p. 90, State and Local Income Tax Refund Worksheet, line 6, "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)"). The married filing separately condition for the spouse boxes is in the spouse questions themselves (refund.spouse_born, refund.spouse_blind: "answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return"), as the footnote says ("you can check the boxes for your spouse only if your spouse had no income, isn't filing a return, and can't be claimed as a dependent"); amb.2025.refund_boxes_2024 records the reading.

### 7 — Add lines 5 and 6
Status: **MATCH**

Model: The worksheet says "Add lines 5 and 6."

### 8 — Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and 
Status: **MATCH**

Model: The worksheet says "Subtract line 7 from line 4" when line 7 is less, and STOP otherwise (zero gives the same result). For married filing separately where the spouse itemized, it says "skip lines 5 through 7, enter the amount from line 4 on line 8", which the mfs branch does.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **MATCH**

Model: The worksheet says "Enter the smaller of line 3 or line 8". The zero branch when line 1 is not more than line 2 matches the line 3 STOP, "None of your refund is taxable."

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "Taking the smaller of the 1099-G refund and 2024 Schedule A line 5d matches the worksheet. But neither refusal covers three Pub. 525 exceptions: \"You received a refund in 2025 that is for a tax year other than 2024\", \"You made your last payment of 2024 estimated state or local income tax in 2025\", and the precondition that the refund be \"for a tax you paid in 2024 and you deducted state and local income taxes on your 2024 Schedule A\". The refund input counts every refund received in 2025, so those cases get computed here instead of being sent to Pub. 525."
  - key: "2"
    status: MATCH
    reason: "The worksheet says \"Subtract the amount on your 2024 Schedule A, line 5e, from\" the line 5d amount when 5d is more than 5e. On \"No\", line 1 goes straight to line 3, which is what a zero line 2 does in the next step."
  - key: "3"
    status: MATCH
    reason: "The worksheet says \"Subtract line 2 from line 1\" when line 1 is more, and STOP (nothing taxable) otherwise. Entering zero gives the same final result, because line 9 then becomes zero."
  - key: "4"
    status: MATCH
    reason: "The worksheet says \"Enter your total itemized deductions from your 2024 Schedule A, line 17.\""
  - key: "5"
    status: MATCH
    reason: "The amounts by filing status match the worksheet: \"Single or married filing separately—$14,600; Married filing jointly or qualifying surviving spouse—$29,200; Head of household—$21,900.\""
  - key: "6"
    status: UNCLEAR
    reason: "The worksheet says to \"Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)\". The per-box helper amounts are not defined in the glossary, so the rates cannot be checked. The restatement also leaves out the married-filing-separately rule that spouse boxes count only \"if your spouse had no income, isn't filing a return, and can't be claimed as a dependent\"."
  - key: "7"
    status: MATCH
    reason: "The worksheet says \"Add lines 5 and 6.\""
  - key: "8"
    status: MATCH
    reason: "The worksheet says \"Subtract line 7 from line 4\" when line 7 is less, and STOP otherwise (zero gives the same result). For married filing separately where the spouse itemized, it says \"skip lines 5 through 7, enter the amount from line 4 on line 8\", which the mfs branch does."
  - key: "9"
    status: MATCH
    reason: "The worksheet says \"Enter the smaller of line 3 or line 8\". The zero branch when line 1 is not more than line 2 matches the line 3 STOP, \"None of your refund is taxable.\""
```
```
