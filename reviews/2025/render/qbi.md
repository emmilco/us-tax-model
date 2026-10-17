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
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### dividends — Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period 
Status: **MATCH**

Model: The i8995 text says qualified REIT dividends must be held more than 45 days and not obligated to someone else, and are 'reported to you on Form 1099-DIV, line 5'. The input asks for box 5 dividends after confirming those requirements.

### unsupported — Any QBI or PTP income/loss other than section 199A dividends, prior-year QBI/REIT/PTP loss
Status: **MATCH**

Model: This is a scoping gate that flags QBI, PTP, carryforward (lines 3 and 7) and cooperative patron cases. Those are the cases the form and instructions handle outside a dividend-only computation, so the gate narrows the scope correctly.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: This is a constant $0 helper, and nothing in the IRS text conflicts with it.

### eligible — Amount from qbi.dividends
Status: **MATCH**

Model: Line 6 is 'Qualified REIT dividends and publicly traded partnership (PTP) income or (loss)'. With PTP income and line 7 carryforwards refused, this reduces to the qualified REIT dividends, and the refusal names the excluded 8995/8995-A business or PTP path.

### deductions_before — Form 1040 lines 12e and 13b, the deductions taken before the QBI deduction
Status: **MATCH**

Model: The line 11 instructions, as corrected, compute taxable income as 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b'. This helper sums the line 12e deduction and line 13b, which are the amounts subtracted.

### taxable_before — Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floor
Status: **MATCH**

Model: Line 11b is defined as 'Amount from line 11a', so subtracting 12e and 13b from it matches 'line 11a, minus lines 12e and 13b'. The IRS text does not state a zero floor, but the floor cannot change line 13, which is itself floored, or the comparison with the positive threshold.

### net_capital_gain — Add sd.net_gain, f1040.line3a
Status: **MISMATCH**

Restated: Add sd helper "Nonnegative net capital gain for QDCGT" and f1040 line 3a.

Model: The instructions say 'If you're not required to file Schedule D (Form 1040), your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a.' The restatement always uses the smaller of Schedule D lines 15 and 16, floored at zero, and has no line 7a branch and no refusal for that case.

Ruling: representation; project retained. For a Schedule D filer the helper is the smaller of Schedule D lines 15 and 16, floored at zero, plus Form 1040 line 3a, as the instructions say. When Schedule D is not required (i8995 p. 4: "your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a") the Schedule D lines are still computed from line 13 alone, so lines 15 and 16 both equal the box 2a total that line 7a carries, and the helper gives the same amount. No change to the data.

### threshold — Year parameter qbi.threshold
Status: **MATCH**

Model: Form 8995 says 'at or below $197,300 ($394,600 if married filing jointly)'. The restatement uses $394,600 for MFJ and $197,300 for every other filing status.

### use_8995a — Taxable income before QBI exceeds the Form 8995 threshold
Status: **MATCH**

Model: Form 8995 is for taxable income 'at or below' the threshold, so taxable income above it routes to Form 8995-A. Cooperative patrons are excluded by the unsupported gate.

### deduction — Select Form 8995 or dividend-only Form 8995-A
Status: **UNCLEAR**

Restated: Choose — [helper "Taxable income before QBI exceeds the Form 8995 threshold" = true → f8995a line 39] [helper "Taxable income before QBI exceeds the Form 8995 threshold" = false → f8995 line 15]

Model: The Form 8995 branch matches line 15, 'Qualified business income deduction. Enter the smaller of line 10 or line 14.' No Form 8995-A text or instructions were provided, so I cannot confirm that f8995a line 39 is the dividend-only deduction amount.

Ruling: representation; project retained. Form 8995-A line 39 is "Total qualified business income deduction. Add lines 37 and 38" (f8995a p. 2), the amount the form carries to Form 1040 line 13a; the dividend-only Form 8995-A path has its own render log (all lines MATCH after the line 33 and 34 rulings). No change to the data.

## Raw response

```yaml
```yaml
lines:
  - key: "dividends"
    status: MATCH
    reason: "The i8995 text says qualified REIT dividends must be held more than 45 days and not obligated to someone else, and are 'reported to you on Form 1099-DIV, line 5'. The input asks for box 5 dividends after confirming those requirements."
  - key: "unsupported"
    status: MATCH
    reason: "This is a scoping gate that flags QBI, PTP, carryforward (lines 3 and 7) and cooperative patron cases. Those are the cases the form and instructions handle outside a dividend-only computation, so the gate narrows the scope correctly."
  - key: "zero"
    status: MATCH
    reason: "This is a constant $0 helper, and nothing in the IRS text conflicts with it."
  - key: "eligible"
    status: MATCH
    reason: "Line 6 is 'Qualified REIT dividends and publicly traded partnership (PTP) income or (loss)'. With PTP income and line 7 carryforwards refused, this reduces to the qualified REIT dividends, and the refusal names the excluded 8995/8995-A business or PTP path."
  - key: "deductions_before"
    status: MATCH
    reason: "The line 11 instructions, as corrected, compute taxable income as 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b'. This helper sums the line 12e deduction and line 13b, which are the amounts subtracted."
  - key: "taxable_before"
    status: MATCH
    reason: "Line 11b is defined as 'Amount from line 11a', so subtracting 12e and 13b from it matches 'line 11a, minus lines 12e and 13b'. The IRS text does not state a zero floor, but the floor cannot change line 13, which is itself floored, or the comparison with the positive threshold."
  - key: "net_capital_gain"
    status: MISMATCH
    reason: "The instructions say 'If you're not required to file Schedule D (Form 1040), your net capital gain is the amount reported on Form 1040, 1040-SR, or 1040-NR, line 7a.' The restatement always uses the smaller of Schedule D lines 15 and 16, floored at zero, and has no line 7a branch and no refusal for that case."
  - key: "threshold"
    status: MATCH
    reason: "Form 8995 says 'at or below $197,300 ($394,600 if married filing jointly)'. The restatement uses $394,600 for MFJ and $197,300 for every other filing status."
  - key: "use_8995a"
    status: MATCH
    reason: "Form 8995 is for taxable income 'at or below' the threshold, so taxable income above it routes to Form 8995-A. Cooperative patrons are excluded by the unsupported gate."
  - key: "deduction"
    status: UNCLEAR
    reason: "The Form 8995 branch matches line 15, 'Qualified business income deduction. Enter the smaller of line 10 or line 14.' No Form 8995-A text or instructions were provided, so I cannot confirm that f8995a line 39 is the dividend-only deduction amount."
```
```
