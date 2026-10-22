# Render comparison — se

The rendered English of every printed line of `Schedule SE (Form 1040) — Self-Employment Tax, one per person` (`rendered/2025/se.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9a71ee87a63dbef4e86d759624652cbf28d8e3ae1dbeace001109ad7097356ef |
| subject sha256 | 8a81da1ead4f3c6b6d3ca69527ccbdc522853d4ad73ce923cf1871f59bef82f0 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 10 / 5 / 0 / 0 |
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

Model: The IRS line covers more than Schedule C results: "Net profit or (loss) from Schedule C, line 31; and Schedule K-1 (Form 1065), box 14, code A (other than farming)." The restatement binds only this person's Schedule C and names no refusal for partnership amounts.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names net earnings from a partnership (Schedule K-1, box 14, code A) and other self-employment income not on a Schedule C.

### 8a — Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad 
Status: **MATCH**

Model: The line is "total of boxes 3 and 7 on Form(s) W-2" plus railroad retirement (tier 1) compensation. The restatement takes boxes 3 and 7 and refuses the railroad case (person.se_rrta), so it is right within the supported cases.

### 3 — Combine lines 1a, 1b, and 2
Status: **MISMATCH**

Restated: Enter the amount from line 2.

Model: The IRS says "Combine lines 1a, 1b, and 2," and line 1b is a subtraction (entered in parentheses). The restatement uses line 2 alone, and no refusal names the excluded farm amounts on lines 1a and 1b.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names farm income (Schedule F) and Conservation Reserve Program payments, the sources of lines 1a and 1b.

### 4a — If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount f
Status: **MATCH**

Model: The IRS says "If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3." The restatement computes exactly that, since the helper equals line 3 when line 3 is positive.

### 4b — If you elect one or both of the optional methods, enter the total of lines 15 and 17
Status: **MISMATCH**

Restated: Enter the amount from helper "Zero".

Model: The IRS says "If you elect one or both of the optional methods, enter the total of lines 15 and 17 here." The restatement always enters $0, and no refusal names the excluded optional-method elections.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names electing an optional method (Schedule SE Part II).

### 4c — Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax
Status: **MATCH**

Model: The IRS says "Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax." The restatement enters the sum when it is $400 or more and $0 otherwise, which carries the same no-tax result through the remaining lines. Church employee income only reaches this line through line 5b, which the program sets to zero.

### 5b — Multiply line 5a by 92.35% (0.9235)
Status: **MISMATCH**

Restated: Enter the amount from helper "Zero".

Model: The IRS says "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-." The restatement always enters $0, and no refusal names church employee income as excluded.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names church employee income, the source of line 5a.

### 6 — Add lines 4c and 5b
Status: **MATCH**

Model: The IRS says "Add lines 4c and 5b," which is what the restatement does.

### 7 — Maximum amount of combined wages and self-employment earnings subject to social security t
Status: **MATCH**

Model: The form prints $176,100 for 2025, and the restatement enters $176,100.

### 8d — Add lines 8a, 8b, and 8c
Status: **MISMATCH**

Restated: Enter the amount from line 8a.

Model: The IRS says "Add lines 8a, 8b, and 8c," which includes unreported tips from Form 4137, line 10, and wages from Form 8919, line 10. The restatement uses line 8a alone, and no refusal names these exclusions.

Ruling: refusal located elsewhere; restatement accepted. This is a line of the Schedule SE definition, bound per person; the cases the IRS line adds are refused before the definition is used, by person.se_screen ('Does any of these apply to this person', i1040sse pp. 1-5), which names tips reported on Form 4137 and wages on Form 8919, the sources of lines 8b and 8c.

### 9 — Subtract line 8d from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: The IRS says "Subtract line 8d from line 7. If zero or less, enter -0-." When line 9 is zero, line 10 becomes zero automatically, consistent with the instruction to enter -0- on line 10 as well.

### 10 — Multiply the smaller of line 6 or line 9 by 12.4% (0.124)
Status: **MATCH**

Model: The IRS says "Multiply the smaller of line 6 or line 9 by 12.4% (0.124)." The skip when line 8a is $176,100 or more gives the same result, because line 9 is then zero.

### 11 — Multiply line 6 by 2.9% (0.029)
Status: **MATCH**

Model: The IRS says "Multiply line 6 by 2.9% (0.029)," which is what the restatement does.

### 12 — Self-employment tax. Add lines 10 and 11
Status: **MATCH**

Model: The IRS says "Add lines 10 and 11," which is what the restatement does.

### 13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
Status: **MATCH**

Model: The IRS says "Multiply line 12 by 50% (0.50)," which is what the restatement does. The instruction to skip this line applies only to Form 1040-SS filers, which this Form 1040 computation does not cover.

## Raw response

```yaml
```yaml
lines:
  - key: "2"
    status: MISMATCH
    reason: "The IRS line covers more than Schedule C results: \"Net profit or (loss) from Schedule C, line 31; and Schedule K-1 (Form 1065), box 14, code A (other than farming).\" The restatement binds only this person's Schedule C and names no refusal for partnership amounts."
  - key: "8a"
    status: MATCH
    reason: "The line is \"total of boxes 3 and 7 on Form(s) W-2\" plus railroad retirement (tier 1) compensation. The restatement takes boxes 3 and 7 and refuses the railroad case (person.se_rrta), so it is right within the supported cases."
  - key: "3"
    status: MISMATCH
    reason: "The IRS says \"Combine lines 1a, 1b, and 2,\" and line 1b is a subtraction (entered in parentheses). The restatement uses line 2 alone, and no refusal names the excluded farm amounts on lines 1a and 1b."
  - key: "4a"
    status: MATCH
    reason: "The IRS says \"If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3.\" The restatement computes exactly that, since the helper equals line 3 when line 3 is positive."
  - key: "4b"
    status: MISMATCH
    reason: "The IRS says \"If you elect one or both of the optional methods, enter the total of lines 15 and 17 here.\" The restatement always enters $0, and no refusal names the excluded optional-method elections."
  - key: "4c"
    status: MATCH
    reason: "The IRS says \"Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax.\" The restatement enters the sum when it is $400 or more and $0 otherwise, which carries the same no-tax result through the remaining lines. Church employee income only reaches this line through line 5b, which the program sets to zero."
  - key: "5b"
    status: MISMATCH
    reason: "The IRS says \"Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-.\" The restatement always enters $0, and no refusal names church employee income as excluded."
  - key: "6"
    status: MATCH
    reason: "The IRS says \"Add lines 4c and 5b,\" which is what the restatement does."
  - key: "7"
    status: MATCH
    reason: "The form prints $176,100 for 2025, and the restatement enters $176,100."
  - key: "8d"
    status: MISMATCH
    reason: "The IRS says \"Add lines 8a, 8b, and 8c,\" which includes unreported tips from Form 4137, line 10, and wages from Form 8919, line 10. The restatement uses line 8a alone, and no refusal names these exclusions."
  - key: "9"
    status: MATCH
    reason: "The IRS says \"Subtract line 8d from line 7. If zero or less, enter -0-.\" When line 9 is zero, line 10 becomes zero automatically, consistent with the instruction to enter -0- on line 10 as well."
  - key: "10"
    status: MATCH
    reason: "The IRS says \"Multiply the smaller of line 6 or line 9 by 12.4% (0.124).\" The skip when line 8a is $176,100 or more gives the same result, because line 9 is then zero."
  - key: "11"
    status: MATCH
    reason: "The IRS says \"Multiply line 6 by 2.9% (0.029),\" which is what the restatement does."
  - key: "12"
    status: MATCH
    reason: "The IRS says \"Add lines 10 and 11,\" which is what the restatement does."
  - key: "13"
    status: MATCH
    reason: "The IRS says \"Multiply line 12 by 50% (0.50),\" which is what the restatement does. The instruction to skip this line applies only to Form 1040-SS filers, which this Form 1040 computation does not cover."
```
```
