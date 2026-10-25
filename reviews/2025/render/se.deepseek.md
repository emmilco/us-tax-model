# Render comparison — se

The rendered English of every printed line of `Schedule SE (Form 1040) — Self-Employment Tax, one per person` (`rendered/2025/se.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 9a71ee87a63dbef4e86d759624652cbf28d8e3ae1dbeace001109ad7097356ef |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: IRS line 2 includes "Schedule K-1 (Form 1065), box 14, code A" and other income per instructions; restatement uses only this person Schedule C results.

Ruling: open

### 8a — Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad 
Status: **MATCH**

Model: Restatement takes W-2 boxes 3 and 7 and refuses railroad retirement compensation, an allowed narrowing of the IRS line.

### 3 — Combine lines 1a, 1b, and 2
Status: **MISMATCH**

Restated: Enter the amount from line 2.

Model: IRS line 3 says "Combine lines 1a, 1b, and 2"; restatement enters only the amount from line 2.

Ruling: open

### 4a — If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount f
Status: **MATCH**

Model: Matches the IRS conditional: if line 3 is more than zero multiply by 92.35%, otherwise enter line 3.

### 4b — If you elect one or both of the optional methods, enter the total of lines 15 and 17
Status: **MISMATCH**

Restated: Enter the amount from helper "Zero".

Model: IRS line 4b says "If you elect one or both of the optional methods, enter the total of lines 15 and 17 here"; restatement always enters zero.

Ruling: open

### 4c — Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax
Status: **MATCH**

Model: Matches combining lines 4a and 4b, entering the combined amount when $400 or more, otherwise zero for the stop and church-employee exception.

### 5b — Multiply line 5a by 92.35% (0.9235)
Status: **MISMATCH**

Restated: Enter the amount from helper "Zero".

Model: IRS line 5b says "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-"; restatement always enters zero.

Ruling: open

### 6 — Add lines 4c and 5b
Status: **MATCH**

Model: Adds line 4c and line 5b as the IRS line says.

### 7 — Maximum amount of combined wages and self-employment earnings subject to social security t
Status: **MATCH**

Model: Enters the 2025 maximum of $176,100 as printed on the IRS line.

### 8d — Add lines 8a, 8b, and 8c
Status: **MISMATCH**

Restated: Enter the amount from line 8a.

Model: IRS line 8d says "Add lines 8a, 8b, and 8c"; restatement enters only line 8a.

Ruling: open

### 9 — Subtract line 8d from line 7. If zero or less, enter -0-
Status: **MATCH**

Model: Subtracts line 8d from line 7 and floors at -0- as the IRS line says.

### 10 — Multiply the smaller of line 6 or line 9 by 12.4% (0.124)
Status: **MATCH**

Model: Multiplies the smaller of line 6 or line 9 by 12.4% as the IRS line says.

### 11 — Multiply line 6 by 2.9% (0.029)
Status: **MATCH**

Model: Multiplies line 6 by 2.9% as the IRS line says.

### 12 — Self-employment tax. Add lines 10 and 11
Status: **MATCH**

Model: Adds lines 10 and 11 as the IRS line says.

### 13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
Status: **MATCH**

Model: Multiplies line 12 by 50% as the IRS line says.

## Raw response

```yaml
lines:
  - key: "2"
    status: MISMATCH
    reason: 'IRS line 2 includes "Schedule K-1 (Form 1065), box 14, code A" and other income per instructions; restatement uses only this person Schedule C results.'
  - key: "8a"
    status: MATCH
    reason: 'Restatement takes W-2 boxes 3 and 7 and refuses railroad retirement compensation, an allowed narrowing of the IRS line.'
  - key: "3"
    status: MISMATCH
    reason: 'IRS line 3 says "Combine lines 1a, 1b, and 2"; restatement enters only the amount from line 2.'
  - key: "4a"
    status: MATCH
    reason: 'Matches the IRS conditional: if line 3 is more than zero multiply by 92.35%, otherwise enter line 3.'
  - key: "4b"
    status: MISMATCH
    reason: 'IRS line 4b says "If you elect one or both of the optional methods, enter the total of lines 15 and 17 here"; restatement always enters zero.'
  - key: "4c"
    status: MATCH
    reason: 'Matches combining lines 4a and 4b, entering the combined amount when $400 or more, otherwise zero for the stop and church-employee exception.'
  - key: "5b"
    status: MISMATCH
    reason: 'IRS line 5b says "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-"; restatement always enters zero.'
  - key: "6"
    status: MATCH
    reason: 'Adds line 4c and line 5b as the IRS line says.'
  - key: "7"
    status: MATCH
    reason: 'Enters the 2025 maximum of $176,100 as printed on the IRS line.'
  - key: "8d"
    status: MISMATCH
    reason: 'IRS line 8d says "Add lines 8a, 8b, and 8c"; restatement enters only line 8a.'
  - key: "9"
    status: MATCH
    reason: 'Subtracts line 8d from line 7 and floors at -0- as the IRS line says.'
  - key: "10"
    status: MATCH
    reason: 'Multiplies the smaller of line 6 or line 9 by 12.4% as the IRS line says.'
  - key: "11"
    status: MATCH
    reason: 'Multiplies line 6 by 2.9% as the IRS line says.'
  - key: "12"
    status: MATCH
    reason: 'Adds lines 10 and 11 as the IRS line says.'
  - key: "13"
    status: MATCH
    reason: 'Multiplies line 12 by 50% as the IRS line says.'
```
