# Section 199A dividend-only deduction and form selection

- Document: `qbi` (form, tax year 2025)
- Note: Only qualified REIT/RIC section 199A dividends, not trade/business or PTP amounts. Taxable income before QBI is AGI less the selected deduction; Schedule 1-A is outside scope. The Jan. 27, 2026 Form 8995 instruction correction is followed.

## (helper) — `qbi.dividends`

- **Authored helper label:** Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements
- **Encoded (NonNegDollars):** Input — Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements
- Expr: `{"op":"input","source":"Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.unsupported`

- **Authored helper label:** Any QBI or PTP income/loss other than section 199A dividends, prior-year QBI/REIT/PTP loss carryover, or agricultural/horticultural cooperative patronage?
- **Encoded (Bool):** Input — Any QBI or PTP income/loss other than section 199A dividends, prior-year QBI/REIT/PTP loss carryover, or agricultural/horticultural cooperative patronage?
- Expr: `{"op":"input","source":"Any QBI or PTP income/loss other than section 199A dividends, prior-year QBI/REIT/PTP loss carryover, or agricultural/horticultural cooperative patronage?"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.eligible`

- **Authored helper label:** Amount from qbi.dividends
- **Encoded (NonNegDollars):** Enter the amount from helper "Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements".
- **Refusal:** when qbi.unsupported is true, cannot complete Forms 8995 / 8995-A business or PTP path. Only section 199A dividend income without loss carryovers is supported. Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)
- Expr: `{"from":"qbi.dividends","op":"copy"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.deductions_before`

- **Authored helper label:** Form 1040 lines 12e and 13b, the deductions taken before the QBI deduction
- **Encoded (NonNegDollars):** Add sa helper "Deduction selected for Form 1040 line 12e" and f1040 line 13b.
- Expr: `{"of":["sa.deduction","f1040.line13b"],"op":"sum"}`
- Cite: [i8995-correction] Correction to 2025 Form 8995 instructions, line 11: Form 1040 line 11a minus lines 12e and 13b (Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28; sha256 926735a0)

## (helper) — `qbi.taxable_before`

- **Authored helper label:** Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floored at zero
- **Encoded (NonNegDollars):** Subtract helper "Form 1040 lines 12e and 13b, the deductions taken before the QBI deduction" from sa helper "Form 1040 line 11b adjusted gross income". If zero or less, enter -0-.
- Expr: `{"from":"sa.agi","op":"subtract_floor0","take":"qbi.deductions_before"}`
- Cite: [i8995-correction] Correction to 2025 Form 8995 instructions, line 11: Form 1040 line 11a minus lines 12e and 13b (Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28; sha256 926735a0)

## (helper) — `qbi.net_capital_gain`

- **Authored helper label:** Add sd.net_gain, f1040.line3a
- **Encoded (NonNegDollars):** Add sd helper "Nonnegative net capital gain for QDCGT" and f1040 line 3a.
- Expr: `{"of":["sd.net_gain","f1040.line3a"],"op":"sum"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.threshold`

- **Authored helper label:** Year parameter qbi.threshold
- **Encoded (NonNegDollars):** Enter single $197,300; mfj $394,600; mfs $197,300; hoh $197,300; qss $197,300 (qbi.threshold).
- Expr: `{"op":"param","ref":"qbi.threshold"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.use_8995a`

- **Authored helper label:** Taxable income before QBI exceeds the Form 8995 threshold
- **Encoded (Bool):** helper "Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floored at zero" > helper "Year parameter qbi.threshold"
- Expr: `{"gt":["qbi.taxable_before","qbi.threshold"],"op":"test"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.deduction`

- **Authored helper label:** Select Form 8995 or dividend-only Form 8995-A
- **Encoded (NonNegDollars):** Choose — [helper "Taxable income before QBI exceeds the Form 8995 threshold" = true → f8995a line 39] [helper "Taxable income before QBI exceeds the Form 8995 threshold" = false → f8995 line 15]
- Expr: `{"alternatives":[{"guard":{"eq":["qbi.use_8995a",{"const":true}],"op":"test"},"then":"f8995a.line39"},{"guard":{"eq":["qbi.use_8995a",{"const":false}],"op":"test"},"then":"f8995.line15"}],"op":"choose"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)
