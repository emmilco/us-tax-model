# Schedule E, Part I — one royalty property

- Document: `royalty` (form, tax year 2025)
- Collection: keyed entries; [i1040se] p. 3, Line 4 (2025; sha256 ad71de35)
- Note: One entry per royalty source (Schedule E type 6). Royalties are not passive and never go on Form 8582. Refused: royalties from the filer's own business or a working interest, and depletion.

## (helper) — `royalty.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040se] p. 3, Line 4 (2025; sha256 ad71de35)

## (helper) — `royalty.one`

- **Authored helper label:** One
- **Encoded (Count):** Enter 1 (rental.one).
- Expr: `{"op":"param","ref":"rental.one"}`
- Cite: [i1040se] p. 5, Line 1a (2025; sha256 ad71de35)

## 4 — `royalty.line4`

- **IRS:** Royalties received
- **Encoded (NonNegDollars):** Input — Royalties from it in 2025 before any taxes the payer withheld (Form 1099-MISC box 2), your share
- Expr: `{"op":"input","source":"Royalties from it in 2025 before any taxes the payer withheld (Form 1099-MISC box 2), your share"}`
- Cite: [i1040se] p. 6, Line 4, "Report on line 4 royalties from oil, gas, or mineral properties (not including operating interests)" (2025; sha256 ad71de35)

## (helper) — `royalty.business`

- **Authored helper label:** Royalty from the filer's own work as a self-employed writer, artist or inventor, or from a working interest
- **Encoded (Bool):** Input — Did it come from your own work as a self-employed writer, artist, musician or inventor, or from an oil or gas working interest?
- Expr: `{"op":"input","source":"Did it come from your own work as a self-employed writer, artist, musician or inventor, or from an oil or gas working interest?"}`
- Cite: [i1040se] p. 6, Line 4, "If you are in business as a self-employed writer, inventor, artist, etc., report your royalty income and expenses on Schedule C" (2025; sha256 ad71de35)

## (helper) — `royalty.depletion`

- **Authored helper label:** Depletion claimed
- **Encoded (Bool):** Input — Do you claim depletion for it (oil, gas or minerals)?
- Expr: `{"op":"input","source":"Do you claim depletion for it (oil, gas or minerals)?"}`
- Cite: [i1040se] p. 6, Line 18, "Depletion" (2025; sha256 ad71de35)

## (helper) — `royalty.expenses_any`

- **Authored helper label:** Any expenses for this royalty
- **Encoded (Bool):** Input — Did you pay any costs for it, such as fees, taxes or production costs?
- Expr: `{"op":"input","source":"Did you pay any costs for it, such as fees, taxes or production costs?"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `royalty.amt10`

- **Authored helper label:** Legal and other professional fees paid in 2025
- **Encoded (NonNegDollars):** Input — Legal and other professional fees for it, paid in 2025; zero if none
- Expr: `{"op":"input","source":"Legal and other professional fees for it, paid in 2025; zero if none"}`
- Cite: [i1040se] p. 6, Line 10 (2025; sha256 ad71de35)

## 10 — `royalty.line10`

- **IRS:** Legal and other professional fees
- **Encoded (NonNegDollars):** Choose — [helper "Any expenses for this royalty" = true → helper "Legal and other professional fees paid in 2025"] [helper "Any expenses for this royalty" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["royalty.expenses_any",{"const":true}],"op":"test"},"then":"royalty.amt10"},{"guard":{"eq":["royalty.expenses_any",{"const":false}],"op":"test"},"then":"royalty.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, Line 10 (2025; sha256 ad71de35)

## (helper) — `royalty.amt16`

- **Authored helper label:** Taxes paid in 2025
- **Encoded (NonNegDollars):** Input — Taxes on it paid in 2025, such as severance or production taxes, including any the payer withheld; zero if none
- Expr: `{"op":"input","source":"Taxes on it paid in 2025, such as severance or production taxes, including any the payer withheld; zero if none"}`
- Cite: [i1040se] p. 6, Line 16 (2025; sha256 ad71de35)

## 16 — `royalty.line16`

- **IRS:** Taxes
- **Encoded (NonNegDollars):** Choose — [helper "Any expenses for this royalty" = true → helper "Taxes paid in 2025"] [helper "Any expenses for this royalty" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["royalty.expenses_any",{"const":true}],"op":"test"},"then":"royalty.amt16"},{"guard":{"eq":["royalty.expenses_any",{"const":false}],"op":"test"},"then":"royalty.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, Line 16 (2025; sha256 ad71de35)

## (helper) — `royalty.amt19`

- **Authored helper label:** Other paid in 2025
- **Encoded (NonNegDollars):** Input — Other costs of it (not depletion), paid in 2025; zero if none
- Expr: `{"op":"input","source":"Other costs of it (not depletion), paid in 2025; zero if none"}`
- Cite: [i1040se] p. 6, Line 19 (2025; sha256 ad71de35)

## 19 — `royalty.line19`

- **IRS:** Other
- **Encoded (NonNegDollars):** Choose — [helper "Any expenses for this royalty" = true → helper "Other paid in 2025"] [helper "Any expenses for this royalty" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["royalty.expenses_any",{"const":true}],"op":"test"},"then":"royalty.amt19"},{"guard":{"eq":["royalty.expenses_any",{"const":false}],"op":"test"},"then":"royalty.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 7, Line 19, "Enter on line 19 any ordinary and necessary expenses not listed on lines 5 through 18" (2025; sha256 ad71de35)

## 20 — `royalty.line20`

- **IRS:** Total expenses. Add lines 5 through 19
- **Encoded (NonNegDollars):** Add line 10, line 16, and line 19.
- Expr: `{"of":["royalty.line10","royalty.line16","royalty.line19"],"op":"sum"}`
- Cite: [f1040se] Schedule E (2025), line 20 (2025; sha256 c5e2c8fa)

## 21 — `royalty.line21`

- **IRS:** Subtract line 20 from line 4 (royalties)
- **Encoded (Dollars):** Subtract line 20 from line 4.
- **Refusal:** when royalty.business is true, cannot complete Schedule C (royalties from your own trade or business). Royalties from your own work as a self-employed writer, artist or inventor, or from a working interest, are reported on Schedule C; this tool does not prepare them on Schedule E. Cite: [i1040se] p. 6, Line 4, "If you are in business as a self-employed writer, inventor, artist, etc., report your royalty income and expenses on Schedule C" (2025; sha256 ad71de35)
- **Refusal:** when royalty.depletion is true, cannot complete Schedule E, line 18 (depletion). Depletion is outside this tool. Cite: [i1040se] p. 6, Line 18, "Depletion" (2025; sha256 ad71de35)
- Expr: `{"from":"royalty.line4","op":"subtract","take":"royalty.line20"}`
- Cite: [f1040se] Schedule E (2025), line 21; i1040se p. 7, Line 21, "If you have amounts for which you are not at risk, use Form 6198 to determine the amount of your deductible loss" (2025; sha256 c5e2c8fa)

## (helper) — `royalty.income`

- **Authored helper label:** Royalty income (positive line 21)
- **Encoded (NonNegDollars):** Subtract helper "Zero" from line 21. If zero or less, enter -0-.
- Expr: `{"from":"royalty.line21","op":"subtract_floor0","take":"royalty.zero"}`
- Cite: [f1040se] Schedule E (2025), line 24, "Add positive amounts shown on line 21" (2025; sha256 c5e2c8fa)

## (helper) — `royalty.loss`

- **Authored helper label:** Royalty loss (negative line 21)
- **Encoded (Dollars):** Subtract helper "Royalty loss as a positive amount" from helper "Zero".
- Expr: `{"from":"royalty.zero","op":"subtract","take":"royalty.loss_abs"}`
- Cite: [f1040se] Schedule E (2025), line 25, "Add royalty losses from line 21" (2025; sha256 c5e2c8fa)

## (helper) — `royalty.loss_abs`

- **Authored helper label:** Royalty loss as a positive amount
- **Encoded (NonNegDollars):** Subtract line 21 from helper "Zero". If zero or less, enter -0-.
- Expr: `{"from":"royalty.zero","op":"subtract_floor0","take":"royalty.line21"}`
- Cite: [f1040se] Schedule E (2025), line 25, "Add royalty losses from line 21" (2025; sha256 c5e2c8fa)
