# Render comparison — qbi

The rendered English of every printed line of `Section 199A dividend-only deduction and form selection` (`rendered/2025/qbi.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0e77c2b636ca5a38db62f29fdd483877ca1f1c9c2a8799a75269e9eef486889c |
| lines judged | 10 |
| match / mismatch / unclear / missing | 8 / 1 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb | - | - |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | bfdf022f2a6af7d4bc0be6b72286aa5dc86aa8f0ddab24c4ad8ccce36f5e8683 |

## Lines

### dividends — Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period 
Status: **MATCH**

Model: The instructions say qualified REIT dividends must be held more than 45 days and not obligated to someone else, and that this amount 'is reported to you on Form 1099-DIV, line 5.' The input is box 5 after confirming those requirements, which matches.

### unsupported — Any QBI or PTP income/loss other than section 199A dividends, prior-year QBI/REIT/PTP loss
Status: **MATCH**

Model: The Form 8995 note lists QBI, REIT dividends, PTP income and cooperative items, and the form excludes cooperative patrons. Line 3 and line 7 describe the prior-year loss carryforwards. This gate correctly identifies everything other than dividend-only income so the program can refuse those cases.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: This is a constant $0 used as a placeholder; nothing in the IRS text contradicts it.

### eligible — Amount from qbi.dividends
Status: **MATCH**

Model: Within the supported case (only section 199A dividends, with no PTP items and no line 7 carryforward), line 6 and line 8 ('Combine lines 6 and 7') both equal the qualified REIT dividends. The refusal names the excluded business, PTP and carryover cases.

### deductions_before — Form 1040 lines 12e and 13b, the deductions taken before the QBI deduction
Status: **MATCH**

Model: The corrected line 11 instructions subtract 'lines 12e and 13b' from line 11a. Summing the line 12e deduction and line 13b gives that subtrahend.

### taxable_before — Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floor
Status: **MATCH**

Model: The IRS text is 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b', and line 11b is the 'Amount from line 11a', so the computation matches. The IRS text does not say to floor at zero, but flooring cannot change line 13 (which is itself floored) or the threshold comparison.

### net_capital_gain — Add sd.net_gain, f1040.line3a
Status: **MISMATCH**

Restated: Add sd helper "Nonnegative net capital gain for QDCGT" and f1040 line 3a.

Model: The program always takes the smaller of Schedule D lines 15 and 16, floored at zero, plus line 3a. It has no path for filers without Schedule D, for whom the instructions say: 'If you're not required to file Schedule D (Form 1040), your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a.' No refusal excludes that case.

Ruling: representation; project retained. For a Schedule D filer the helper is the smaller of Schedule D lines 15 and 16, floored at zero, plus Form 1040 line 3a, as the instructions say. When Schedule D is not required (i8995 p. 4: "your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a") the Schedule D lines are still computed from line 13 alone, so lines 15 and 16 both equal the box 2a total that line 7a carries, and the helper gives the same amount. No change to the data.

### threshold — Year parameter qbi.threshold
Status: **MATCH**

Model: Form 8995 gives the threshold as '$197,300 ($394,600 if married filing jointly)', and the program uses $197,300 for all other filing statuses.

### use_8995a — Taxable income before QBI exceeds the Form 8995 threshold
Status: **MATCH**

Model: Form 8995 is used if taxable income 'is at or below $197,300 ($394,600 if married filing jointly)', so a value strictly greater than the threshold selects 8995-A. Cooperative patrons, the other 8995-A trigger, are excluded by the unsupported gate.

### deduction — Select Form 8995 or dividend-only Form 8995-A
Status: **UNCLEAR**

Restated: Choose — [helper "Taxable income before QBI exceeds the Form 8995 threshold" = true → f8995a line 39] [helper "Taxable income before QBI exceeds the Form 8995 threshold" = false → f8995 line 15]

Model: The Form 8995 branch matches line 15, which is the 'Qualified business income deduction'. No Form 8995-A text is provided, so it cannot be confirmed that 8995-A line 39 ('Add f8995a.line37, f8995a.line38') is that form's final QBI deduction.

Ruling: representation; project retained. Form 8995-A line 39 is "Total qualified business income deduction. Add lines 37 and 38" (f8995a p. 2), the amount the form carries to Form 1040 line 13a; the dividend-only Form 8995-A path has its own render log (all lines MATCH after the line 33 and 34 rulings). No change to the data.

## Raw response

```yaml
lines:
  - key: "dividends"
    status: MATCH
    reason: "The instructions say qualified REIT dividends must be held more than 45 days and not obligated to someone else, and that this amount 'is reported to you on Form 1099-DIV, line 5.' The input is box 5 after confirming those requirements, which matches."
  - key: "unsupported"
    status: MATCH
    reason: "The Form 8995 note lists QBI, REIT dividends, PTP income and cooperative items, and the form excludes cooperative patrons. Line 3 and line 7 describe the prior-year loss carryforwards. This gate correctly identifies everything other than dividend-only income so the program can refuse those cases."
  - key: "zero"
    status: MATCH
    reason: "This is a constant $0 used as a placeholder; nothing in the IRS text contradicts it."
  - key: "eligible"
    status: MATCH
    reason: "Within the supported case (only section 199A dividends, with no PTP items and no line 7 carryforward), line 6 and line 8 ('Combine lines 6 and 7') both equal the qualified REIT dividends. The refusal names the excluded business, PTP and carryover cases."
  - key: "deductions_before"
    status: MATCH
    reason: "The corrected line 11 instructions subtract 'lines 12e and 13b' from line 11a. Summing the line 12e deduction and line 13b gives that subtrahend."
  - key: "taxable_before"
    status: MATCH
    reason: "The IRS text is 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b', and line 11b is the 'Amount from line 11a', so the computation matches. The IRS text does not say to floor at zero, but flooring cannot change line 13 (which is itself floored) or the threshold comparison."
  - key: "net_capital_gain"
    status: MISMATCH
    reason: "The program always takes the smaller of Schedule D lines 15 and 16, floored at zero, plus line 3a. It has no path for filers without Schedule D, for whom the instructions say: 'If you're not required to file Schedule D (Form 1040), your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a.' No refusal excludes that case."
  - key: "threshold"
    status: MATCH
    reason: "Form 8995 gives the threshold as '$197,300 ($394,600 if married filing jointly)', and the program uses $197,300 for all other filing statuses."
  - key: "use_8995a"
    status: MATCH
    reason: "Form 8995 is used if taxable income 'is at or below $197,300 ($394,600 if married filing jointly)', so a value strictly greater than the threshold selects 8995-A. Cooperative patrons, the other 8995-A trigger, are excluded by the unsupported gate."
  - key: "deduction"
    status: UNCLEAR
    reason: "The Form 8995 branch matches line 15, which is the 'Qualified business income deduction'. No Form 8995-A text is provided, so it cannot be confirmed that 8995-A line 39 ('Add f8995a.line37, f8995a.line38') is that form's final QBI deduction."
```
