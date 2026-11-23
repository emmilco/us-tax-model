# Schedule E, Part I — one royalty property

- Document: `royalty` (form, tax year 2025)
- Collection: keyed entries; [i1040se] p. 3, Line 4 (2025; sha256 ad71de35)
- Note: One entry per royalty source (Schedule E type 6). Royalties are not passive and never go on Form 8582. Refused: royalties from the filer's own business or services or a working interest, a patent transfer or coal or iron ore, car and travel costs, depreciation, depletion, and a loss with amounts not at risk.

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

- **Authored helper label:** Royalty from the filer's own business or services (a self-employed writer, artist, inventor or other creator, or name, image and likeness income from sponsorships or services), or from an operating (working) interest in minerals
- **Encoded (Bool):** Input — Did it come from your own business or services (as a self-employed writer, artist, musician, inventor or other creator, or name, image and likeness income from sponsorships or services), or from an operating (working) interest in oil, gas or other minerals?
- Expr: `{"op":"input","source":"Did it come from your own business or services (as a self-employed writer, artist, musician, inventor or other creator, or name, image and likeness income from sponsorships or services), or from an operating (working) interest in oil, gas or other minerals?"}`
- Cite: [i1040se] p. 6, Line 4, "If you are in business as a self-employed writer, inventor, artist, etc., report your royalty income and expenses on Schedule C", "Report on line 4 royalties from oil, gas, or mineral properties (not including operating interests)", and "If your NIL income is derived from business activities such as sponsorship deals or service income, report your income and expenses on Schedule C" (2025; sha256 ad71de35)

## (helper) — `royalty.depletion`

- **Authored helper label:** Depletion claimed
- **Encoded (Bool):** Input — Do you claim depletion for it (oil, gas or minerals)?
- Expr: `{"op":"input","source":"Do you claim depletion for it (oil, gas or minerals)?"}`
- Cite: [i1040se] p. 6, Line 18, "Depletion" (2025; sha256 ad71de35)

## (helper) — `royalty.capital`

- **Authored helper label:** Payment for a transferred patent, or for coal or iron ore disposed of, that may be a sale of a capital asset
- **Encoded (Bool):** Input — Is it a payment for a patent you transferred, or for coal or iron ore you disposed of?
- Expr: `{"op":"input","source":"Is it a payment for a patent you transferred, or for coal or iron ore you disposed of?"}`
- Cite: [i1040se] p. 6, "You may be able to treat amounts received as 'royalties' for the transfer of a patent or amounts received on the disposal of coal and iron ore as the sale of a capital asset" (2025; sha256 ad71de35)

## (helper) — `royalty.vehicle`

- **Authored helper label:** Car, truck or travel expenses for the royalty (line 6)
- **Encoded (Bool):** Input — Do you have car, truck or travel costs for it?
- Expr: `{"op":"input","source":"Do you have car, truck or travel costs for it?"}`
- Cite: [i1040se] p. 4, Line 6 (2025; sha256 ad71de35)

## (helper) — `royalty.depreciation`

- **Authored helper label:** Depreciation or amortization for the royalty (line 18)
- **Encoded (Bool):** Input — Do you depreciate or amortize anything for it, such as a copyright or patent you bought?
- Expr: `{"op":"input","source":"Do you depreciate or amortize anything for it, such as a copyright or patent you bought?"}`
- Cite: [f1040se] Schedule E (2025), line 18, "Depreciation expense or depletion" (2025; sha256 c5e2c8fa)

## (helper) — `royalty.expenses_any`

- **Authored helper label:** Any expenses for this royalty
- **Encoded (Bool):** Input — Did you pay costs for it, or were any taken out of your payments (such as fees, severance or production taxes, or production costs)?
- Expr: `{"op":"input","source":"Did you pay costs for it, or were any taken out of your payments (such as fees, severance or production taxes, or production costs)?"}`
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
- **Encoded (NonNegDollars):** Input — Other costs of it (not depletion), paid in 2025, or taken out of your payments if the royalties you entered are before they were taken out; zero if none
- Expr: `{"op":"input","source":"Other costs of it (not depletion), paid in 2025, or taken out of your payments if the royalties you entered are before they were taken out; zero if none"}`
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
- **Refusal:** when royalty.business is true, cannot complete Schedule C (royalties from your own trade or business). Royalties from your own business or services (as a self-employed writer, artist, inventor or other creator, or name, image and likeness income from sponsorships or services), or from a working interest, are reported on Schedule C; this tool does not prepare them on Schedule E. Cite: [i1040se] p. 6, Line 4, "If you are in business as a self-employed writer, inventor, artist, etc., report your royalty income and expenses on Schedule C" (2025; sha256 ad71de35)
- **Refusal:** when royalty.depletion is true, cannot complete Schedule E, line 18 (depletion). Depletion is outside this tool. Cite: [i1040se] p. 6, Line 18, "Depletion" (2025; sha256 ad71de35)
- **Refusal:** when royalty.capital is true, cannot complete Form 4797 or Schedule D (patent transfer, or coal or iron ore). Royalties that may be treated as the sale of a capital asset (from a patent you transferred, or coal or iron ore you disposed of) are outside this tool. Cite: [i1040se] p. 6, "You may be able to treat amounts received as 'royalties' for the transfer of a patent or amounts received on the disposal of coal and iron ore as the sale of a capital asset" (2025; sha256 ad71de35)
- **Refusal:** when royalty.vehicle is true, cannot complete Schedule E, line 6 (auto and travel). Car, truck and travel costs of a royalty are outside this tool. Cite: [i1040se] p. 4, Line 6 (2025; sha256 ad71de35)
- **Refusal:** when royalty.depreciation is true, cannot complete Schedule E, line 18 (depreciation). Depreciation or amortization for a royalty is outside this tool. Cite: [f1040se] Schedule E (2025), line 18, "Depreciation expense or depletion" (2025; sha256 c5e2c8fa)
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
- **Refusal:** when royalty.not_at_risk_if_loss is true, cannot complete Form 6198 (at-risk limits). A royalty loss with an amount not at risk is outside this tool. Cite: [i1040se] p. 3, At-Risk Rules (2025; sha256 ad71de35)
- Expr: `{"from":"royalty.zero","op":"subtract_floor0","take":"royalty.line21"}`
- Cite: [f1040se] Schedule E (2025), line 25, "Add royalty losses from line 21" (2025; sha256 c5e2c8fa)

## (helper) — `royalty.has_loss`

- **Authored helper label:** Line 21 is a loss
- **Encoded (Bool):** line 21 < $0
- Expr: `{"lt":["royalty.line21",{"const":0}],"op":"test"}`
- Cite: [i1040se] p. 7, Line 21 (2025; sha256 ad71de35)

## (helper) — `royalty.no`

- **Authored helper label:** No (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [i1040se] p. 7, Line 21 (2025; sha256 ad71de35)

## (helper) — `royalty.not_at_risk`

- **Authored helper label:** Some investment not at risk
- **Encoded (Bool):** Input — Was any money you put in borrowed without personal liability (from any lender, a bank included), protected from loss by a guarantee, stop-loss agreement or similar arrangement, or lent by someone with a stake in it or a relative of such a person?
- Expr: `{"op":"input","source":"Was any money you put in borrowed without personal liability (from any lender, a bank included), protected from loss by a guarantee, stop-loss agreement or similar arrangement, or lent by someone with a stake in it or a relative of such a person?"}`
- Cite: [i1040se] p. 3, At-Risk Rules, "In most cases, you must complete Form 6198 to figure your loss if you have" (2025; sha256 ad71de35)

## (gate) — `royalty.not_at_risk_if_loss`

- **Authored helper label:** Asked only when the royalty has a loss (false otherwise)
- **Encoded (Bool):** Choose — [helper "Line 21 is a loss" = true → helper "Some investment not at risk"] [helper "Line 21 is a loss" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["royalty.has_loss",{"const":true}],"op":"test"},"then":"royalty.not_at_risk"},{"guard":{"eq":["royalty.has_loss",{"const":false}],"op":"test"},"then":"royalty.no"}],"op":"choose"}`
- Cite: [i1040se] p. 7, Line 21, "If you have amounts for which you are not at risk, use Form 6198 to determine the amount of your deductible loss" (2025; sha256 ad71de35)
