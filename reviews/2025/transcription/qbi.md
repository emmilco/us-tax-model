# Transcription agreement — qbi

Second transcription of `Section 199A dividend-only deduction and form selection` by an isolated model (spec 6.5), compared line by line with `forms/2025/qbi.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0eb6377be4a46f8ee41e27c7cb084662de8c4480b5c20e7aca870f7a0bc227aa |
| printed lines compared | 5 |
| agree / disagree / missing | 5 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb |

## Lines

### qbi.zero — Year parameter sales.zero
Status: **AGREE**

### qbi.eligible — Amount from qbi.dividends
Status: **AGREE**

### qbi.taxable_before — Subtract sa.deduction from sa.agi; if zero or less, enter zero
Status: **AGREE**

### qbi.net_capital_gain — Add sd.net_gain, f1040.line3a
Status: **AGREE**

### qbi.deduction — Select Form 8995 or dividend-only Form 8995-A
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: qbi.zero
    printed: "(helper)"
    label: "Year parameter sales.zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    cite: "Form 8995 (2025), lines 2, 3, 4, 5, 7, 16, 17 (no amounts within the dividend-only scope)"

  - id: qbi.eligible
    printed: "(helper)"
    label: "Amount from qbi.dividends"
    type: NonNegDollars
    expr: {op: copy, from: qbi.dividends}
    cite: "Form 8995 (2025), line 6: Qualified REIT dividends and publicly traded partnership (PTP) income or (loss)"
    note: "Open point: line 6 names qualified REIT dividends and PTP income. The provided input is qualified section 199A dividends from Form 1099-DIV box 5. Chosen reading: under the dividend-only scope these dividends are the whole of line 6. PTP income is screened out by qbi.unsupported."

  - id: qbi.taxable_before
    printed: "(helper)"
    label: "Subtract sa.deduction from sa.agi; if zero or less, enter zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: sa.deduction}
    cite: "Form 8995 (2025), line 11; Instructions for Form 8995 (2025), line 11 as corrected (post-release correction, Jan. 27, 2026): Form 1040 line 11a, minus lines 12e and 13b"
    note: "Open point 1: the corrected instructions say line 11a minus lines 12e and 13b. The model uses sa.agi (Form 1040 line 11b, which equals 11a) minus sa.deduction (line 12e). Line 13b (Schedule 1-A) is taken as zero, because scope.schedule1a screens out Schedule 1-A deductions. Open point 2: the instruction text gives no zero floor. Chosen reading: floor at zero as the requested helper specifies. A negative value would make line 13 zero anyway, so the floor does not change lines 13-15."

  - id: qbi.net_capital_gain
    printed: "(helper)"
    label: "Add sd.net_gain, f1040.line3a"
    type: NonNegDollars
    expr: {op: sum, of: [sd.net_gain, f1040.line3a]}
    cite: "Form 8995 (2025), line 12: Enter your net capital gain, if any, increased by any qualified dividends"
    note: "Open point: the form says 'net capital gain, if any' and refers to the instructions, which were not provided. Chosen reading: the nonnegative net capital gain from Schedule D (sd.net_gain) plus Form 1040 line 3a qualified dividends."

  - id: qbi.h_threshold
    printed: "(helper)"
    label: "Form 8995 taxable income threshold: $197,300 ($394,600 if married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: qbi.threshold}
    cite: "Form 8995 (2025), header: Use this form if your taxable income, before your qualified business income deduction, is at or below $197,300 ($394,600 if married filing jointly)"
    note: "The parameter is keyed by filing status (f1040.status)."

  - id: qbi.h_use8995
    printed: "(helper)"
    label: "Taxable income before QBI deduction is at or below the Form 8995 threshold"
    type: Bool
    expr: {op: test, le: [qbi.taxable_before, qbi.h_threshold]}
    cite: "Form 8995 (2025), header eligibility statement"

  - id: qbi.h_use8995a
    printed: "(helper)"
    label: "Taxable income before QBI deduction is above the Form 8995 threshold"
    type: Bool
    expr: {op: test, not: qbi.h_use8995}
    cite: "Form 8995 (2025), header eligibility statement (complement)"

  - id: qbi.deduction
    printed: "(helper)"
    label: "Select Form 8995 or dividend-only Form 8995-A"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: qbi.h_use8995, then: f8995.line15}
        - {guard: qbi.h_use8995a, then: f8995a.line39}
    cite: "Form 8995 (2025), header and line 15; Form 1040 line 13a"
    note: "Open point: Form 8995 is also unavailable to a patron of an agricultural or horticultural cooperative. Chosen reading: qbi.unsupported, which covers cooperative patronage, carryovers and other QBI/PTP items, screens these cases before this line, so the only remaining guard is the taxable-income threshold. Form 8995-A was not provided in this text, so above the threshold the line uses the existing f8995a.line39 helper."
```
```
