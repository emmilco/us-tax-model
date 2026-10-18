# Render comparison — qbi

The rendered English of every printed line of `Section 199A dividend-only deduction and form selection` (`rendered/2025/qbi.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2d0bef0de2689cf174b26e6712dc876d8bab8b044518a7872239c7b8fbfa5c64 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 8 / 1 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb | - | - |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### dividends — Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period 
Status: **MATCH**

Model: The i8995 text says qualified REIT dividends are those held more than 45 days, where the payment isn't obligated to someone else, and that 'This amount is reported to you on Form 1099-DIV, line 5.' The input asks for that amount after those checks.

### unsupported — Do you have any of these: qualified business income or loss, or PTP income or loss, other 
Status: **MATCH**

Model: This yes/no gate catches the items handled on lines 1–3 and 6–7 of Form 8995 other than REIT dividends: business income, PTP income, carryforwards and suspended losses allowed this year. It also catches qualified 1099-PATR payments, which the text says require that you 'use Form 8995-A to compute your QBI deduction.' The gate is a fair test for the cases the program leaves out.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: This is a constant $0 used only as a placeholder, and nothing in the IRS text conflicts with it.

### eligible — Amount from qbi.dividends
Status: **MATCH**

Model: Line 8 says to 'Combine lines 6 and 7. If zero or less, enter -0-'. With no PTP income and no carryforward, which the refusal excludes, line 8 equals the qualified REIT dividends on line 6, so passing the dividends through is correct within the supported cases.

### deductions_before — Form 1040 lines 12e and 13b, the deductions taken before the QBI deduction
Status: **MATCH**

Model: The corrected line 11 instructions subtract 'lines 12e and 13b' from line 11a. This helper adds the deduction the program chose for line 12e and Form 1040 line 13b.

### taxable_before — Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floor
Status: **MATCH**

Model: Line 11 is 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b', and line 11b is the 'Amount from line 11a', so the subtraction matches. The text gives no zero floor. Still, the floor cannot change the threshold test or line 13, which already says 'If zero or less, enter -0-'.

### net_capital_gain — Add sd.net_gain, f1040.line3a
Status: **MISMATCH**

Restated: Add sd helper "Nonnegative net capital gain for QDCGT" and f1040 line 3a.

Model: The restatement always takes net capital gain from Schedule D and has no refusal for filers without one. The instructions say: 'If you're not required to file Schedule D (Form 1040), your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a.' The Schedule D case (smaller of line 15 or 16, adding nothing if zero or less) does match.

Ruling: representation; project retained. For a Schedule D filer the helper is the smaller of Schedule D lines 15 and 16, floored at zero, plus Form 1040 line 3a, as the instructions say. When Schedule D is not required (i8995 p. 4: "your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a") the Schedule D lines are still computed from line 13 alone, so lines 15 and 16 both equal the box 2a total that line 7a carries, and the helper gives the same amount. No change to the data.

### threshold — Year parameter qbi.threshold
Status: **MATCH**

Model: The form says to use it if taxable income 'is at or below $197,300 ($394,600 if married filing jointly)'. Only joint filers get the higher amount, so $197,300 for single, MFS, HOH and QSS agrees with the text.

### use_8995a — Taxable income before QBI exceeds the Form 8995 threshold
Status: **MATCH**

Model: Form 8995 is limited to filers whose taxable income before the QBI deduction 'is at or below' the threshold, so switching away from it when that income is strictly greater than the threshold is correct. The cooperative-patron condition is handled by the unsupported refusal.

### deduction — Select Form 8995 or dividend-only Form 8995-A
Status: **UNCLEAR**

Restated: Choose — [helper "Taxable income before QBI exceeds the Form 8995 threshold" = true → f8995a line 39] [helper "Taxable income before QBI exceeds the Form 8995 threshold" = false → f8995 line 15]

Model: The Form 8995 branch matches: line 15 is the 'Qualified business income deduction. Enter the smaller of line 10 or line 14.' But none of the Form 8995-A form or instruction text is provided. Without it, I can't confirm that line 39 ('Add f8995a.line37, f8995a.line38') is the final QBI deduction for a filer with only dividends above the threshold.

Ruling: representation; project retained. Form 8995-A line 39 is "Total qualified business income deduction. Add lines 37 and 38" (f8995a p. 2), the amount the form carries to Form 1040 line 13a; the dividend-only Form 8995-A path has its own render log (all lines MATCH after the line 33 and 34 rulings). No change to the data.

## Raw response

```yaml
```yaml
lines:
  - key: "dividends"
    status: MATCH
    reason: "The i8995 text says qualified REIT dividends are those held more than 45 days, where the payment isn't obligated to someone else, and that 'This amount is reported to you on Form 1099-DIV, line 5.' The input asks for that amount after those checks."
  - key: "unsupported"
    status: MATCH
    reason: "This yes/no gate catches the items handled on lines 1–3 and 6–7 of Form 8995 other than REIT dividends: business income, PTP income, carryforwards and suspended losses allowed this year. It also catches qualified 1099-PATR payments, which the text says require that you 'use Form 8995-A to compute your QBI deduction.' The gate is a fair test for the cases the program leaves out."
  - key: "zero"
    status: MATCH
    reason: "This is a constant $0 used only as a placeholder, and nothing in the IRS text conflicts with it."
  - key: "eligible"
    status: MATCH
    reason: "Line 8 says to 'Combine lines 6 and 7. If zero or less, enter -0-'. With no PTP income and no carryforward, which the refusal excludes, line 8 equals the qualified REIT dividends on line 6, so passing the dividends through is correct within the supported cases."
  - key: "deductions_before"
    status: MATCH
    reason: "The corrected line 11 instructions subtract 'lines 12e and 13b' from line 11a. This helper adds the deduction the program chose for line 12e and Form 1040 line 13b."
  - key: "taxable_before"
    status: MATCH
    reason: "Line 11 is 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b', and line 11b is the 'Amount from line 11a', so the subtraction matches. The text gives no zero floor. Still, the floor cannot change the threshold test or line 13, which already says 'If zero or less, enter -0-'."
  - key: "net_capital_gain"
    status: MISMATCH
    reason: "The restatement always takes net capital gain from Schedule D and has no refusal for filers without one. The instructions say: 'If you're not required to file Schedule D (Form 1040), your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a.' The Schedule D case (smaller of line 15 or 16, adding nothing if zero or less) does match."
  - key: "threshold"
    status: MATCH
    reason: "The form says to use it if taxable income 'is at or below $197,300 ($394,600 if married filing jointly)'. Only joint filers get the higher amount, so $197,300 for single, MFS, HOH and QSS agrees with the text."
  - key: "use_8995a"
    status: MATCH
    reason: "Form 8995 is limited to filers whose taxable income before the QBI deduction 'is at or below' the threshold, so switching away from it when that income is strictly greater than the threshold is correct. The cooperative-patron condition is handled by the unsupported refusal."
  - key: "deduction"
    status: UNCLEAR
    reason: "The Form 8995 branch matches: line 15 is the 'Qualified business income deduction. Enter the smaller of line 10 or line 14.' But none of the Form 8995-A form or instruction text is provided. Without it, I can't confirm that line 39 ('Add f8995a.line37, f8995a.line38') is the final QBI deduction for a filer with only dividends above the threshold."
```
```
