# Tax on an amount — Tax Table or Tax Computation Worksheet

- Document: `tax_on_amount` (def, tax year 2025)
- Parameters: amount, status

## (a) — `amount`

- **Authored helper label:** Amount to compute the tax on
- **Encoded (NonNegDollars):** Input — Bound by the calling line (the amount on a worksheet line).
- Expr: `{"op":"input","source":"Bound by the calling line (the amount on a worksheet line)."}`
- Cite: [i1040gi] Instructions for Form 1040, line 16 (2025; printed date 2026-02-25; sha256 482e9c48)

## (status) — `status`

- **Authored helper label:** The return's filing status
- **Encoded (Enum(filing_status)):** Input — Bound by the calling line (Form 1040 filing status).
- Expr: `{"op":"input","source":"Bound by the calling line (Form 1040 filing status)."}`
- Cite: [i1040gi] Instructions for Form 1040, line 16 (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `below_boundary`

- **Authored helper label:** Is the amount less than $100,000?
- **Encoded (Bool):** column (a) (amount) < $100,000 (ordinary.table_boundary)
- Expr: `{"lt":["amount",{"param":"ordinary.table_boundary"}],"op":"test"}`
- Cite: [i1040gi] p. 36, Line 16, Tax Table or Tax Computation Worksheet, "If your taxable income is less than $100,000, you must use the Tax Table", "If your taxable income is $100,000 or more, use the Tax Computation Worksheet right after the Tax Table" (2025; printed date 2026-02-25; sha256 482e9c48)

## (a) — `table_tax`

- **Authored helper label:** Use the Tax Table
- **Encoded (NonNegDollars):** Use 2025 Tax Table at column (a) (amount) for the filing status (helper "The return's filing status").
- Expr: `{"key":"amount","op":"table_lookup","status":"status","table":"tax_table"}`
- Cite: [i1040gi] p. 68, 2025 Tax Table, "If line 15 (taxable income) is—", "And you are—", "Your tax is—" (2025; printed date 2026-02-25; sha256 482e9c48)

## (a) — `worksheet_tax`

- **Authored helper label:** Use the Tax Computation Worksheet
- **Encoded (Dollars):** Enter "tax" of Tax Computation Worksheet—Line 16 with amount = column (a) (amount) and status = helper "The return's filing status".
- Expr: `{"from":{"bind":{"amount":"amount","status":"status"},"def":"tcw","line":"tax"},"op":"copy"}`
- Cite: [i1040gi] 2025 Tax Computation Worksheet, p. 80 (Note) (2025; printed date 2026-02-25; sha256 482e9c48)

## (b) — `tax`

- **Authored helper label:** Tax on the amount
- **Encoded (Dollars):** Choose — [helper "Is the amount less than $100,000?" = true → column (a) (table_tax)] [helper "Is the amount less than $100,000?" = false → column (a) (worksheet_tax)]
- Expr: `{"alternatives":[{"guard":{"eq":["below_boundary",{"const":true}],"op":"test"},"then":"table_tax"},{"guard":{"eq":["below_boundary",{"const":false}],"op":"test"},"then":"worksheet_tax"}],"op":"choose"}`
- Cite: [i1040gi] p. 36, Line 16, Tax Table or Tax Computation Worksheet, "If your taxable income is less than $100,000, you must use the Tax Table, later in these instructions, to figure your tax", "If your taxable income is $100,000 or more, use the Tax Computation Worksheet right after the Tax Table" (2025; printed date 2026-02-25; sha256 482e9c48)
