# Render comparison — qbi

The rendered English of every printed line of `Section 199A dividend-only deduction and form selection` (`rendered/2025/qbi.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 668943c0757862182383e701f3cb6d5820efe5415d56eb9bcddf9487d406d608 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 8 / 1 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 |

## Lines

### dividends — Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period 
Status: **MATCH**

Model: The i8995 text says qualified REIT dividends must be held more than 45 days, must not be payments obligated to someone else, and are "reported to you on Form 1099-DIV, line 5." The input label covers both the holding-period and related-payment requirements.

### unsupported — Any QBI or PTP income/loss other than section 199A dividends, prior-year QBI/REIT/PTP loss
Status: **MATCH**

Model: This is a scoping gate, not an IRS line. It correctly separates out other QBI or PTP income, prior-year carryforwards (f8995 lines 3 and 7) and cooperative patrons, who the text says "must ... use Form 8995-A." This leaves only section 199A dividends.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: This is a constant $0 helper. It does not correspond to an IRS line and changes no value.

### eligible — Amount from qbi.dividends
Status: **MATCH**

Model: Once the refusal excludes PTP income and prior-year carryforwards, f8995 line 6 is just the qualified REIT dividends, and line 8 ("Combine lines 6 and 7. If zero or less, enter -0-") equals the box 5 amount. The refusal names what it excludes.

### deductions_before — Form 1040 lines 12e and 13b, the deductions taken before the QBI deduction
Status: **MATCH**

Model: The corrected line 11 instructions subtract "lines 12e and 13b" from line 11a. This helper adds Form 1040 line 12e (the selected deduction) and line 13b.

### taxable_before — Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floor
Status: **MATCH**

Model: This computes "Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b" (line 11b is the "Amount from line 11a"). The zero floor isn't in the IRS text, but it doesn't change line 13 ("If zero or less, enter -0-") or the threshold comparison.

### net_capital_gain — Add sd.net_gain, f1040.line3a
Status: **MISMATCH**

Restated: Add sd helper "Nonnegative net capital gain for QDCGT" and f1040 line 3a.

Model: It adds line 3a to the Schedule D amount (the smaller of lines 15 and 16, floored at zero) and nothing else. The instructions also say "If you're not required to file Schedule D (Form 1040), your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a." That path is missing, and no refusal covers it.

Ruling: representation; project retained. For a Schedule D filer the helper is the smaller of Schedule D lines 15 and 16, floored at zero, plus Form 1040 line 3a, as the instructions say. When Schedule D is not required (i8995 p. 4: "your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a") the Schedule D lines are still computed from line 13 alone, so lines 15 and 16 both equal the box 2a total that line 7a carries, and the helper gives the same amount. No change to the data.

### threshold — Year parameter qbi.threshold
Status: **MATCH**

Model: Form 8995 says "at or below $197,300 ($394,600 if married filing jointly)". Only MFJ gets the higher amount, so $197,300 is right for every other filing status.

### use_8995a — Taxable income before QBI exceeds the Form 8995 threshold
Status: **MATCH**

Model: Form 8995 is for taxable income before the QBI deduction that "is at or below" the threshold. So taxable income strictly above the threshold means Form 8995-A, and the cooperative-patron case is covered by the refusal.

### deduction — Select Form 8995 or dividend-only Form 8995-A
Status: **UNCLEAR**

Restated: Choose — [helper "Taxable income before QBI exceeds the Form 8995 threshold" = true → f8995a line 39] [helper "Taxable income before QBI exceeds the Form 8995 threshold" = false → f8995 line 15]

Model: The Form 8995 branch matches line 15 ("Enter the smaller of line 10 or line 14"). The Form 8995-A text isn't provided, so I can't confirm that f8995a line 39 is the QBI deduction or that a dividend-only 8995-A computes it correctly.

Ruling: representation; project retained. Form 8995-A line 39 is "Total qualified business income deduction. Add lines 37 and 38" (f8995a p. 2), the amount the form carries to Form 1040 line 13a; the dividend-only Form 8995-A path has its own render log (all lines MATCH after the line 33 and 34 rulings). No change to the data.

## Raw response

```yaml
```yaml
lines:
  - key: "dividends"
    status: MATCH
    reason: "The i8995 text says qualified REIT dividends must be held more than 45 days, must not be payments obligated to someone else, and are \"reported to you on Form 1099-DIV, line 5.\" The input label covers both the holding-period and related-payment requirements."
  - key: "unsupported"
    status: MATCH
    reason: "This is a scoping gate, not an IRS line. It correctly separates out other QBI or PTP income, prior-year carryforwards (f8995 lines 3 and 7) and cooperative patrons, who the text says \"must ... use Form 8995-A.\" This leaves only section 199A dividends."
  - key: "zero"
    status: MATCH
    reason: "This is a constant $0 helper. It does not correspond to an IRS line and changes no value."
  - key: "eligible"
    status: MATCH
    reason: "Once the refusal excludes PTP income and prior-year carryforwards, f8995 line 6 is just the qualified REIT dividends, and line 8 (\"Combine lines 6 and 7. If zero or less, enter -0-\") equals the box 5 amount. The refusal names what it excludes."
  - key: "deductions_before"
    status: MATCH
    reason: "The corrected line 11 instructions subtract \"lines 12e and 13b\" from line 11a. This helper adds Form 1040 line 12e (the selected deduction) and line 13b."
  - key: "taxable_before"
    status: MATCH
    reason: "This computes \"Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b\" (line 11b is the \"Amount from line 11a\"). The zero floor isn't in the IRS text, but it doesn't change line 13 (\"If zero or less, enter -0-\") or the threshold comparison."
  - key: "net_capital_gain"
    status: MISMATCH
    reason: "It adds line 3a to the Schedule D amount (the smaller of lines 15 and 16, floored at zero) and nothing else. The instructions also say \"If you're not required to file Schedule D (Form 1040), your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a.\" That path is missing, and no refusal covers it."
  - key: "threshold"
    status: MATCH
    reason: "Form 8995 says \"at or below $197,300 ($394,600 if married filing jointly)\". Only MFJ gets the higher amount, so $197,300 is right for every other filing status."
  - key: "use_8995a"
    status: MATCH
    reason: "Form 8995 is for taxable income before the QBI deduction that \"is at or below\" the threshold. So taxable income strictly above the threshold means Form 8995-A, and the cooperative-patron case is covered by the refusal."
  - key: "deduction"
    status: UNCLEAR
    reason: "The Form 8995 branch matches line 15 (\"Enter the smaller of line 10 or line 14\"). The Form 8995-A text isn't provided, so I can't confirm that f8995a line 39 is the QBI deduction or that a dividend-only 8995-A computes it correctly."
```
```
