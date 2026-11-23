# Schedule B — interest payer entries

- Document: `interest` (form, tax year 2025)
- Collection: keyed entries; [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- Note: Amounts are supplied from payer records; special treatments are screened at Schedule B. The early withdrawal penalty of each payer is totaled on Schedule 1 line 18.

## (helper) — `interest.amount`

- **Authored helper label:** Taxable interest from this payer, including Treasury interest; exclude tax-exempt interest
- **Encoded (NonNegDollars):** Input — Taxable interest from this payer, including Treasury interest and original issue discount (Form 1099-INT boxes 1 and 3; Form 1099-OID boxes 1, 2 and 8, box 2 only when box 11 is blank); exclude tax-exempt interest
- Expr: `{"op":"input","source":"Taxable interest from this payer, including Treasury interest and original issue discount (Form 1099-INT boxes 1 and 3; Form 1099-OID boxes 1, 2 and 8, box 2 only when box 11 is blank); exclude tax-exempt interest"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts; i1040gi p. 25, Line 2b, "Each payer should send you a Form 1099-INT or Form 1099-OID. Enter your total taxable interest income on line 2b"; f1099oid p. 5, Box 1, "Report the amount in box 1 as interest income on your income tax return", Box 2, "report this amount as interest income on your tax return", "If there is an amount in both boxes 2 and 11, the amount in box 2 is tax-exempt interest"; f1099oid p. 7, Box 8, "Report this amount as interest income on your federal income tax return" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `interest.penalty`

- **Authored helper label:** Early withdrawal penalty charged by this payer (Form 1099-INT box 2, or the penalty shown on Form 1099-OID)
- **Encoded (NonNegDollars):** Input — Penalty on early withdrawal of savings this payer charged you (box 2 of Form 1099-INT, or the early withdrawal penalty shown on Form 1099-OID); zero if none. Do not subtract it from the interest.
- Expr: `{"op":"input","source":"Penalty on early withdrawal of savings this payer charged you (box 2 of Form 1099-INT, or the early withdrawal penalty shown on Form 1099-OID); zero if none. Do not subtract it from the interest."}`
- Cite: [i1040gi] p. 95, Line 18, "The Form 1099-INT or Form 1099-OID you received will show the amount of any penalty you were charged"; f1099int p. 5, Instructions for Recipient, "Box 2. Shows interest or principal forfeited because of early withdrawal of time savings. You may deduct this amount to figure your adjusted gross income on your income tax return" (2025; printed date 2026-02-25; sha256 482e9c48)
