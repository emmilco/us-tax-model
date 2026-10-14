# Tax on an amount — Tax Table or Tax Computation Worksheet

- Document: `tax_on_amount` (def, tax year 2025)
- Parameters: amount, status

## (a) — `amount`

- **IRS:** Amount to compute the tax on
- **Encoded (NonNegDollars):** Input — Bound by the calling line (the amount on a worksheet line).
- Expr: `{"op":"input","source":"Bound by the calling line (the amount on a worksheet line)."}`
- Cite: [i1040gi] Instructions for Form 1040, line 16 (2025; printed date 2026-02-25; sha256 482e9c48)

## (status) — `status`

- **IRS:** The return's filing status
- **Encoded (Enum(filing_status)):** Input — Bound by the calling line (Form 1040 filing status).
- Expr: `{"op":"input","source":"Bound by the calling line (Form 1040 filing status)."}`
- Cite: [i1040gi] Instructions for Form 1040, line 16 (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `below_boundary`

- **IRS:** Is the amount less than $100,000?
- **Encoded (Bool):** line (a) < $100,000 (ordinary.table_boundary)
- Expr: `{"lt":["amount",{"param":"ordinary.table_boundary"}],"op":"test"}`
- Cite: [i1040gi] Instructions for Form 1040, line 16 (2025; printed date 2026-02-25; sha256 482e9c48)

## (a) — `table_tax`

- **IRS:** Use the Tax Table
- **Encoded (NonNegDollars):** Use 2025 Tax Table at line (a) for the filing status (line (status)).
- Expr: `{"key":"amount","op":"table_lookup","status":"status","table":"tax_table"}`
- Cite: [i1040gi] 2025 Tax Table, p. 68 (2025; printed date 2026-02-25; sha256 482e9c48)

## (a) — `worksheet_tax`

- **IRS:** Use the Tax Computation Worksheet
- **Encoded (Dollars):** Enter the amount from tcw(amount = line (a), status = line (status)).tax.
- Expr: `{"from":{"bind":{"amount":"amount","status":"status"},"def":"tcw","line":"tax"},"op":"copy"}`
- Cite: [i1040gi] 2025 Tax Computation Worksheet, p. 80 (Note) (2025; printed date 2026-02-25; sha256 482e9c48)

## (b) — `tax`

- **IRS:** Tax on the amount
- **Encoded (Dollars):** Choose — [line (gate) = true → line (a)] [line (gate) = false → line (a)]
- Expr: `{"alternatives":[{"guard":{"eq":["below_boundary",{"const":true}],"op":"test"},"then":"table_tax"},{"guard":{"eq":["below_boundary",{"const":false}],"op":"test"},"then":"worksheet_tax"}],"op":"choose"}`
- Cite: [i1040gi] Instructions for Form 1040, line 16 (2025; printed date 2026-02-25; sha256 482e9c48)
