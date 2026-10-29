# Render comparison — aqee

The rendered English of every printed line of `Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student` (`rendered/2025/aqee.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 1a15b7ff93505c1a88d41451119428a55512a36d5a41aa9b77f2bd1682cd2ce7 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a2ffd4fbb4c4bae96972fc8469042a1fe83956bf393454eaf708eb9e764165db |
| lines judged | 4 |
| match / mismatch / unclear / missing | 4 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8863 | 2025 | 3, 4, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 3, 4, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |

## Lines

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MATCH**

Model: The IRS line enters the student’s adjusted qualified education expenses from the worksheet and says not to enter more than $4,000; the restatement uses worksheet line 4 capped at $4,000.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MATCH**

Model: The IRS line says to subtract $2,000 from line 27 and enter -0- if zero or less; the restatement does the same.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MATCH**

Model: The IRS line says to multiply line 28 by 25% (0.25); the restatement uses the same 25% rate.

### 30 — If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on
Status: **MATCH**

Model: The IRS line says that if line 28 is zero, enter line 27; otherwise add $2,000 to line 29. The restatement uses exactly that condition and calculation.

## Raw response

```yaml
lines:
  - key: "27"
    status: MATCH
    reason: "The IRS line enters the student’s adjusted qualified education expenses from the worksheet and says not to enter more than $4,000; the restatement uses worksheet line 4 capped at $4,000."
  - key: "28"
    status: MATCH
    reason: "The IRS line says to subtract $2,000 from line 27 and enter -0- if zero or less; the restatement does the same."
  - key: "29"
    status: MATCH
    reason: "The IRS line says to multiply line 28 by 25% (0.25); the restatement uses the same 25% rate."
  - key: "30"
    status: MATCH
    reason: "The IRS line says that if line 28 is zero, enter line 27; otherwise add $2,000 to line 29. The restatement uses exactly that condition and calculation."
```
