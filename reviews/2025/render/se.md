# Render comparison — se

The rendered English of every printed line of `Schedule SE (Form 1040) — Self-Employment Tax, one per person` (`rendered/2025/se.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 07ac9e5bebaf9b5eec4146f5eba6ba9f4356e1650db6c659a2cf2c1bd8a1823a |
| lines judged | 15 |
| match / mismatch / unclear / missing | 9 / 6 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |

## Lines

### 2 — Net profit or (loss) from Schedule C, line 31
Status: **MISMATCH**

Restated: Input — Bound by the calling line (this person's Schedule C results).

Model: The IRS line is "Net profit or (loss) from Schedule C, line 31; and Schedule K-1 (Form 1065), box 14, code A (other than farming)". The restatement takes only Schedule C results and has no refusal naming the excluded partnership income.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names net earnings from a partnership (Schedule K-1, box 14, code A) and other self-employment income not on a Schedule C.

### 8a — Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2)
Status: **MISMATCH**

Restated: Input — Bound by the calling line (this person's Forms W-2, boxes 3 and 7).

Model: The IRS line is "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation". The restatement leaves out railroad retirement (tier 1) compensation and has no refusal.

Ruling: refusal located elsewhere; restatement accepted. Railroad retirement (tier 1) compensation is refused for the whole return through person.rrta (the wage statements' RRTA question), which stops Schedule 3 line 11 (person.credit) and Form 8959 line 1 (person.medicare5); with it refused, line 8a is the Form W-2 boxes 3 and 7 total.

### 3 — Combine lines 1a, 1b, and 2
Status: **MISMATCH**

Restated: Enter the amount from line 2.

Model: The IRS line says "Combine lines 1a, 1b, and 2". The restatement uses line 2 only, dropping the farm profit (1a) and the CRP payment line (1b), with no refusal.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names farm income (Schedule F) and Conservation Reserve Program payments, the sources of lines 1a and 1b.

### 4a — If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount f
Status: **MATCH**

Model: This matches "If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3". When line 3 is positive, the helper is line 3 times 0.9235; otherwise it is line 3.

### 4b — If you elect one or both of the optional methods, enter the total of lines 15 and 17
Status: **MISMATCH**

Restated: Enter the amount from helper "Zero".

Model: The IRS line says "If you elect one or both of the optional methods, enter the total of lines 15 and 17 here". The restatement always enters $0 and has no refusal for filers who elect an optional method.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names electing an optional method (Schedule SE Part II).

### 4c — Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax
Status: **MATCH**

Model: This combines lines 4a and 4b, and enters 0 when the total is under $400, consistent with "If less than $400, stop; you don't owe self-employment tax". Line 5b is always 0 in this program, so continuing with 0 gives no tax.

### 5b — Multiply line 5a by 92.35% (0.9235)
Status: **MISMATCH**

Restated: Enter the amount from helper "Zero".

Model: The IRS line says "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-". The restatement always enters $0, ignoring church employee income, with no refusal.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names church employee income, the source of line 5a.

### 6 — Add lines 4c and 5b
Status: **MATCH**

Model: This matches "Add lines 4c and 5b".

### 7 — Maximum amount of combined wages and self-employment earnings subject to social security t
Status: **MATCH**

Model: The form prints $176,100 for 2025.

### 8d — Add lines 8a, 8b, and 8c
Status: **MISMATCH**

Restated: Enter the amount from line 8a.

Model: The IRS line says "Add lines 8a, 8b, and 8c". The restatement uses line 8a only, omitting unreported tips (Form 4137) and Form 8919 wages, with no refusal.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names tips reported on Form 4137 and wages on Form 8919, the sources of lines 8b and 8c.

### 9 — Subtract line 8d from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: This matches "Subtract line 8d from line 7. If zero or less, enter -0-".

### 10 — Multiply the smaller of line 6 or line 9 by 12.4% (0.124)
Status: **MATCH**

Model: This matches "Multiply the smaller of line 6 or line 9 by 12.4% (0.124)". When line 9 is 0, line 10 is 0, as the form directs.

### 11 — Multiply line 6 by 2.9% (0.029)
Status: **MATCH**

Model: This matches "Multiply line 6 by 2.9% (0.029)".

### 12 — Self-employment tax. Add lines 10 and 11
Status: **MATCH**

Model: This matches "Self-employment tax. Add lines 10 and 11".

### 13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
Status: **MATCH**

Model: This matches "Multiply line 12 by 50% (0.50)".

## Raw response

```yaml
lines:
  - key: "2"
    status: MISMATCH
    reason: "The IRS line is \"Net profit or (loss) from Schedule C, line 31; and Schedule K-1 (Form 1065), box 14, code A (other than farming)\". The restatement takes only Schedule C results and has no refusal naming the excluded partnership income."
  - key: "8a"
    status: MISMATCH
    reason: "The IRS line is \"Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation\". The restatement leaves out railroad retirement (tier 1) compensation and has no refusal."
  - key: "3"
    status: MISMATCH
    reason: "The IRS line says \"Combine lines 1a, 1b, and 2\". The restatement uses line 2 only, dropping the farm profit (1a) and the CRP payment line (1b), with no refusal."
  - key: "4a"
    status: MATCH
    reason: "This matches \"If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3\". When line 3 is positive, the helper is line 3 times 0.9235; otherwise it is line 3."
  - key: "4b"
    status: MISMATCH
    reason: "The IRS line says \"If you elect one or both of the optional methods, enter the total of lines 15 and 17 here\". The restatement always enters $0 and has no refusal for filers who elect an optional method."
  - key: "4c"
    status: MATCH
    reason: "This combines lines 4a and 4b, and enters 0 when the total is under $400, consistent with \"If less than $400, stop; you don't owe self-employment tax\". Line 5b is always 0 in this program, so continuing with 0 gives no tax."
  - key: "5b"
    status: MISMATCH
    reason: "The IRS line says \"Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-\". The restatement always enters $0, ignoring church employee income, with no refusal."
  - key: "6"
    status: MATCH
    reason: "This matches \"Add lines 4c and 5b\"."
  - key: "7"
    status: MATCH
    reason: "The form prints $176,100 for 2025."
  - key: "8d"
    status: MISMATCH
    reason: "The IRS line says \"Add lines 8a, 8b, and 8c\". The restatement uses line 8a only, omitting unreported tips (Form 4137) and Form 8919 wages, with no refusal."
  - key: "9"
    status: MATCH
    reason: "This matches \"Subtract line 8d from line 7. If zero or less, enter -0-\"."
  - key: "10"
    status: MATCH
    reason: "This matches \"Multiply the smaller of line 6 or line 9 by 12.4% (0.124)\". When line 9 is 0, line 10 is 0, as the form directs."
  - key: "11"
    status: MATCH
    reason: "This matches \"Multiply line 6 by 2.9% (0.029)\"."
  - key: "12"
    status: MATCH
    reason: "This matches \"Self-employment tax. Add lines 10 and 11\"."
  - key: "13"
    status: MATCH
    reason: "This matches \"Multiply line 12 by 50% (0.50)\"."
```
