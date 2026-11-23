# Form 1099-DIV — distribution components and scope screening

- Document: `div` (form, tax year 2025)
- Note: Boxes 1a/1b/2a/5 are the shared supplied totals used by the other forms. Box 7 feeds the supplied creditable foreign-tax total in ftc.taxes; box 8 is supporting country information. Boxes 14–16 concern state reporting; state tax paid is entered once on Schedule A. This is a values sheet, not a prepared information return.

## (helper) — `div.box2b`

- **Authored helper label:** Unrecaptured section 1250 gain, box 2b
- **Encoded (NonNegDollars):** Input — Unrecaptured section 1250 gain, box 2b
- Expr: `{"op":"input","source":"Unrecaptured section 1250 gain, box 2b"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box2c`

- **Authored helper label:** Section 1202 gain, box 2c
- **Encoded (NonNegDollars):** Input — Section 1202 gain, box 2c
- Expr: `{"op":"input","source":"Section 1202 gain, box 2c"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box2d`

- **Authored helper label:** Collectibles (28%) gain, box 2d
- **Encoded (NonNegDollars):** Input — Collectibles (28%) gain, box 2d
- Expr: `{"op":"input","source":"Collectibles (28%) gain, box 2d"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box3`

- **Authored helper label:** Nondividend distributions/return of capital, box 3
- **Encoded (NonNegDollars):** Input — Nondividend distributions/return of capital, box 3 (total of all your Forms 1099-DIV, with your share of amounts paid in someone else's name and any received without a form)
- Expr: `{"op":"input","source":"Nondividend distributions/return of capital, box 3 (total of all your Forms 1099-DIV, with your share of amounts paid in someone else's name and any received without a form)"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box9`

- **Authored helper label:** Cash liquidation distributions, box 9
- **Encoded (NonNegDollars):** Input — Cash liquidation distributions, box 9
- Expr: `{"op":"input","source":"Cash liquidation distributions, box 9"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box10`

- **Authored helper label:** Noncash liquidation distributions, box 10
- **Encoded (NonNegDollars):** Input — Noncash liquidation distributions, box 10
- Expr: `{"op":"input","source":"Noncash liquidation distributions, box 10"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box12`

- **Authored helper label:** Exempt-interest dividends, box 12
- **Encoded (NonNegDollars):** Input — Exempt-interest dividends, box 12 (total of all your Forms 1099-DIV, with your share of amounts paid in someone else's name and any received without a form; box 13 amounts are already included)
- Expr: `{"op":"input","source":"Exempt-interest dividends, box 12 (total of all your Forms 1099-DIV, with your share of amounts paid in someone else's name and any received without a form; box 13 amounts are already included)"}`
- Cite: [f1099div] Instructions for Recipient, Box 12 ("Shows exempt-interest dividends from a mutual fund or other RIC paid to you during the calendar year. See the Instructions for Form 1040 for where to report") and Box 13 ("This amount is included in box 12") (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box13`

- **Authored helper label:** Specified private activity bond interest dividends, box 13
- **Encoded (NonNegDollars):** Input — Specified private activity bond interest dividends, box 13
- Expr: `{"op":"input","source":"Specified private activity bond interest dividends, box 13"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.basis_reconciled`

- **Authored helper label:** Was every nondividend distribution (box 3) no more than the remaining basis in the shares it was paid on?
- **Encoded (Bool):** Input — Was every nondividend distribution (Form 1099-DIV box 3, a return of capital) that you (or, on a joint return, your spouse) received in 2025 no more than the remaining basis in the shares it was paid on (their cost or other basis, already reduced by any earlier returns of capital)? Answer No if any distribution was more than that remaining basis, for example because earlier returns of capital had already reduced the basis to zero; the part above the basis is a taxable capital gain, which this tool does not report.
- Expr: `{"op":"input","source":"Was every nondividend distribution (Form 1099-DIV box 3, a return of capital) that you (or, on a joint return, your spouse) received in 2025 no more than the remaining basis in the shares it was paid on (their cost or other basis, already reduced by any earlier returns of capital)? Answer No if any distribution was more than that remaining basis, for example because earlier returns of capital had already reduced the basis to zero; the part above the basis is a taxable capital gain, which this tool does not report."}`
- Cite: [f1099div] p. 5, Instructions for Recipient, Box 3, "To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable. Any amount received in excess of your basis is taxable to you as capital gain" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box1a`

- **Authored helper label:** Amount from sb.ordinary_dividends_if_dividends
- **Encoded (NonNegDollars):** Enter the amount from sb helper "Total ordinary dividends, Form 1099-DIV box 1a, when you or your spouse received dividends or other distributions; zero otherwise".
- Expr: `{"from":"sb.ordinary_dividends_if_dividends","op":"copy"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box1b`

- **Authored helper label:** Amount from f1040.line3a_if_ordinary
- **Encoded (NonNegDollars):** Enter the amount from f1040 helper "Qualified dividends (Form 1040 line 3a), when ordinary dividends (box 1a) are above zero; zero otherwise".
- Expr: `{"from":"f1040.line3a_if_ordinary","op":"copy"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box2a`

- **Authored helper label:** Amount from sd.distributions_if_dividends
- **Encoded (NonNegDollars):** Enter the amount from sd helper "Capital gain distributions, generally Form 1099-DIV box 2a, when you or your spouse received dividends or other distributions; zero otherwise".
- Expr: `{"from":"sd.distributions_if_dividends","op":"copy"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box5`

- **Authored helper label:** Amount from qbi.dividends_if_ordinary
- **Encoded (NonNegDollars):** Enter the amount from qbi helper "Qualified section 199A dividends (Form 1099-DIV box 5), when ordinary dividends (box 1a) are above zero; zero otherwise".
- Expr: `{"from":"qbi.dividends_if_ordinary","op":"copy"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.section1202`

- **Authored helper label:** Section 1202 distribution present
- **Encoded (Bool):** helper "Section 1202 gain, box 2c, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > $0
- Expr: `{"gt":["div.box2c_if_capital_gain",{"const":0}],"op":"test"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, Box 2c, "Shows the portion of the amount in box 2a that is section 1202 gain from certain small business stock that may be subject to an exclusion" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.amt`

- **Authored helper label:** Specified private activity bond dividends present
- **Encoded (Bool):** helper "Specified private activity bond interest dividends, box 13, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > $0
- Expr: `{"gt":["div.box13_if_dividends",{"const":0}],"op":"test"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, Box 13, "Shows exempt-interest dividends subject to the alternative minimum tax" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.unsupported`

- **Authored helper label:** Unsupported liquidation or unreconciled basis/excess distribution
- **Encoded (Bool):** (helper "Cash liquidation distributions, box 9, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > $0 or helper "Noncash liquidation distributions, box 10, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > $0 or helper "Nondividend distributions/return of capital, box 3, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > $0 and helper "For box 3, basis reductions applied, when nondividend distributions (box 3) are above zero; false otherwise" = false)
- Expr: `{"any":[{"gt":["div.box9_if_dividends",{"const":0}],"op":"test"},{"gt":["div.box10_if_dividends",{"const":0}],"op":"test"},{"all":[{"gt":["div.box3_if_dividends",{"const":0}],"op":"test"},{"eq":["div.basis_reconciled_if_return_of_capital",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, boxes 3, 9 and 10, "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable", "Boxes 9 and 10. Show cash and noncash liquidation distributions" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.bad_special`

- **Authored helper label:** A gain component exceeds total capital gain distributions
- **Encoded (Bool):** (helper "Unrecaptured section 1250 gain, box 2b, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a, when you or your spouse received dividends or other distributions; zero otherwise" or helper "Section 1202 gain, box 2c, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a, when you or your spouse received dividends or other distributions; zero otherwise" or helper "Collectibles (28%) gain, box 2d, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a, when you or your spouse received dividends or other distributions; zero otherwise" or helper "Total special capital-gain distribution components" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a, when you or your spouse received dividends or other distributions; zero otherwise")
- Interpretation: amb.2025.div_gain_portions_disjoint
- Expr: `{"any":[{"gt":["div.box2b_if_capital_gain","sd.distributions_if_dividends"],"op":"test"},{"gt":["div.box2c_if_capital_gain","sd.distributions_if_dividends"],"op":"test"},{"gt":["div.box2d_if_capital_gain","sd.distributions_if_dividends"],"op":"test"},{"gt":["div.special_total","sd.distributions_if_dividends"],"op":"test"}],"op":"test"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, boxes 2b to 2d, "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain", "Box 2c. Shows the portion of the amount in box 2a that is section 1202 gain", "Box 2d. Shows the portion of the amount in box 2a that is 28% rate gain" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.screen`

- **Authored helper label:** Zero only after distribution scope checks
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when div.section1202 is true, cannot complete Form 8949 code Q / Form 6251. Section 1202 distributions require exclusion analysis and may require AMT. Code Q and Form 6251 remain outside scope. Cite: [i1040sd] p. 8, Gain from Form 1099-DIV and Alternative Minimum Tax (2025; printed date 2025-12-11; sha256 650643a6)
- **Refusal:** when div.bad_special is true, cannot complete Form 1099-DIV corrected amounts. Boxes 2b, 2c and 2d are portions of box 2a. Correct inconsistent supplied amounts. Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)
- **Refusal:** when div.amt is true, cannot complete Form 6251. Review private activity bond interest for the alternative minimum tax; Form 6251 is outside scope. Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)
- **Refusal:** when div.unsupported is true, cannot complete Form 1099-DIV special distribution treatment. Prepare the required liquidation treatment or reconcile return-of-capital basis and any excess gain. Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)
- **Refusal:** when div.bad_components is true, cannot complete Form 1099-DIV dividend components. Correct the supplied totals: qualified dividends and section 199A dividends are portions of ordinary dividends. Cite: [f1099div] Instructions for Recipient, boxes 1a, 1b and 5 (January 2024 (continuous-use form); sha256 4ea1de80)
- Interpretation: amb.2025.box2c_scope
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (gate) — `div.bad_components`

- **Authored helper label:** Qualified or section 199A dividends exceed ordinary dividends
- **Encoded (Bool):** (f1040 helper "Qualified dividends (Form 1040 line 3a), when ordinary dividends (box 1a) are above zero; zero otherwise" > sb helper "Total ordinary dividends, Form 1099-DIV box 1a, when you or your spouse received dividends or other distributions; zero otherwise" or qbi helper "Qualified section 199A dividends (Form 1099-DIV box 5), when ordinary dividends (box 1a) are above zero; zero otherwise" > sb helper "Total ordinary dividends, Form 1099-DIV box 1a, when you or your spouse received dividends or other distributions; zero otherwise")
- Expr: `{"any":[{"gt":["f1040.line3a_if_ordinary","sb.ordinary_dividends_if_dividends"],"op":"test"},{"gt":["qbi.dividends_if_ordinary","sb.ordinary_dividends_if_dividends"],"op":"test"}],"op":"test"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, boxes 1b and 5, "Box 1b. Shows the portion of the amount in box 1a that may be eligible for reduced capital gains rates", "Box 5. Shows the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction under section 199A" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.special_total`

- **Authored helper label:** Total special capital-gain distribution components
- **Encoded (NonNegDollars):** Add helper "Unrecaptured section 1250 gain, box 2b, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise", helper "Section 1202 gain, box 2c, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise", and helper "Collectibles (28%) gain, box 2d, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise".
- Expr: `{"of":["div.box2b_if_capital_gain","div.box2c_if_capital_gain","div.box2d_if_capital_gain"],"op":"sum"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, boxes 2b to 2d, "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain", "Box 2c. Shows the portion of the amount in box 2a that is section 1202 gain", "Box 2d. Shows the portion of the amount in box 2a that is 28% rate gain" (January 2024 (continuous-use form); sha256 4ea1de80)

## (gate) — `div.any`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, boxes 1a, 2a, 3, 9, 10, 12 and 13, Box 1b, "The amount shown may be dividends a corporation paid directly to you as a participant (or beneficiary of a participant) in an employee stock ownership plan (ESOP)", Nominees, "If this form includes amounts belonging to another person, you are considered a nominee recipient", "Box 1a. Shows total ordinary dividends that are taxable", "Box 2a. Shows total capital gain distributions from a regulated investment company (RIC) or real estate investment trust (REIT)", "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable", "Boxes 9 and 10. Show cash and noncash liquidation distributions", "Box 12. Shows exempt-interest dividends from a mutual fund or other RIC paid to you during the calendar year", "Box 13. Shows exempt-interest dividends subject to the alternative minimum tax. This amount is included in box 12" (January 2024 (continuous-use form); sha256 4ea1de80)

## (gate) — `div.has_ordinary`

- **Authored helper label:** Ordinary dividends (box 1a) are above zero
- **Encoded (Bool):** sb helper "Total ordinary dividends, Form 1099-DIV box 1a, when you or your spouse received dividends or other distributions; zero otherwise" > $0
- Expr: `{"gt":["sb.ordinary_dividends_if_dividends",{"const":0}],"op":"test"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, boxes 1b and 5, "Box 1b. Shows the portion of the amount in box 1a that may be eligible for reduced capital gains rates", "Box 5. Shows the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction under section 199A" (January 2024 (continuous-use form); sha256 4ea1de80)

## (gate) — `div.has_capital_gain`

- **Authored helper label:** Capital gain distributions (box 2a) are above zero
- **Encoded (Bool):** sd helper "Capital gain distributions, generally Form 1099-DIV box 2a, when you or your spouse received dividends or other distributions; zero otherwise" > $0
- Expr: `{"gt":["sd.distributions_if_dividends",{"const":0}],"op":"test"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, boxes 2b, 2c and 2d, "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain from certain depreciable real property", "Box 2c. Shows the portion of the amount in box 2a that is section 1202 gain from certain small business stock that may be subject to an exclusion", "Box 2d. Shows the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles" (January 2024 (continuous-use form); sha256 4ea1de80)

## (gate) — `div.has_return_of_capital`

- **Authored helper label:** Nondividend distributions (box 3) are above zero
- **Encoded (Bool):** helper "Nondividend distributions/return of capital, box 3, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise" > $0
- Expr: `{"gt":["div.box3_if_dividends",{"const":0}],"op":"test"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, Box 3, "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.zero`

- **Authored helper label:** No amount in a box whose condition does not hold
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.no`

- **Authored helper label:** No answer needed where the question is not asked
- **Encoded (Bool):** Enter false (div.no).
- Expr: `{"op":"param","ref":"div.no"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, Box 3, "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable" (January 2024 (continuous-use form); sha256 4ea1de80)

## (gate) — `div.other_boxes`

- **Authored helper label:** An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV
- **Encoded (Bool):** Input — Look at your (or, on a joint return, your spouse's) Forms 1099-DIV for 2025. Does any of them show an amount in box 2b, 2c, 2d, 3, 9, 10 or 13?
- Expr: `{"op":"input","source":"Look at your (or, on a joint return, your spouse's) Forms 1099-DIV for 2025. Does any of them show an amount in box 2b, 2c, 2d, 3, 9, 10 or 13?"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.other_boxes_if_dividends`

- **Authored helper label:** An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?" = true → helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV"] [helper "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?" = false → helper "No answer needed where the question is not asked"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.any",{"const":true}],"op":"test"},"then":"div.other_boxes"},{"guard":{"eq":["div.any",{"const":false}],"op":"test"},"then":"div.no"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain", "Box 2c. Shows the portion of the amount in box 2a that is section 1202 gain", "Box 2d. Shows the portion of the amount in box 2a that is 28% rate gain", "Box 3. Shows a return of capital", "Boxes 9 and 10. Show cash and noncash liquidation distributions", "Box 13. Shows exempt-interest dividends subject to the alternative minimum tax"; boxes 2e and 2f are not asked: "Note: Boxes 2e and 2f apply only to foreign persons and entities whose income maintains its character when passed through or distributed to its direct or indirect foreign owners or beneficiaries" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.capital_gain_boxes`

- **Authored helper label:** An amount in one of those boxes, when capital gain distributions (box 2a) are above zero; false otherwise
- **Encoded (Bool):** Choose — [helper "Capital gain distributions (box 2a) are above zero" = true → helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise"] [helper "Capital gain distributions (box 2a) are above zero" = false → helper "No answer needed where the question is not asked"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.has_capital_gain",{"const":true}],"op":"test"},"then":"div.other_boxes_if_dividends"},{"guard":{"eq":["div.has_capital_gain",{"const":false}],"op":"test"},"then":"div.no"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain", "Box 2c. Shows the portion of the amount in box 2a that is section 1202 gain", "Box 2d. Shows the portion of the amount in box 2a that is 28% rate gain", "Box 3. Shows a return of capital", "Boxes 9 and 10. Show cash and noncash liquidation distributions", "Box 13. Shows exempt-interest dividends subject to the alternative minimum tax" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box2b_if_capital_gain`

- **Authored helper label:** Unrecaptured section 1250 gain, box 2b, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "An amount in one of those boxes, when capital gain distributions (box 2a) are above zero; false otherwise" = true → helper "Unrecaptured section 1250 gain, box 2b"] [helper "An amount in one of those boxes, when capital gain distributions (box 2a) are above zero; false otherwise" = false → helper "No amount in a box whose condition does not hold"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.capital_gain_boxes",{"const":true}],"op":"test"},"then":"div.box2b"},{"guard":{"eq":["div.capital_gain_boxes",{"const":false}],"op":"test"},"then":"div.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain from certain depreciable real property" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box2c_if_capital_gain`

- **Authored helper label:** Section 1202 gain, box 2c, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "An amount in one of those boxes, when capital gain distributions (box 2a) are above zero; false otherwise" = true → helper "Section 1202 gain, box 2c"] [helper "An amount in one of those boxes, when capital gain distributions (box 2a) are above zero; false otherwise" = false → helper "No amount in a box whose condition does not hold"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.capital_gain_boxes",{"const":true}],"op":"test"},"then":"div.box2c"},{"guard":{"eq":["div.capital_gain_boxes",{"const":false}],"op":"test"},"then":"div.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 2c. Shows the portion of the amount in box 2a that is section 1202 gain from certain small business stock that may be subject to an exclusion" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box2d_if_capital_gain`

- **Authored helper label:** Collectibles (28%) gain, box 2d, when capital gain distributions (box 2a) are above zero and a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "An amount in one of those boxes, when capital gain distributions (box 2a) are above zero; false otherwise" = true → helper "Collectibles (28%) gain, box 2d"] [helper "An amount in one of those boxes, when capital gain distributions (box 2a) are above zero; false otherwise" = false → helper "No amount in a box whose condition does not hold"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.capital_gain_boxes",{"const":true}],"op":"test"},"then":"div.box2d"},{"guard":{"eq":["div.capital_gain_boxes",{"const":false}],"op":"test"},"then":"div.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 2d. Shows the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box3_if_dividends`

- **Authored helper label:** Nondividend distributions/return of capital, box 3, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise" = true → helper "Nondividend distributions/return of capital, box 3"] [helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise" = false → helper "No amount in a box whose condition does not hold"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.other_boxes_if_dividends",{"const":true}],"op":"test"},"then":"div.box3"},{"guard":{"eq":["div.other_boxes_if_dividends",{"const":false}],"op":"test"},"then":"div.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box9_if_dividends`

- **Authored helper label:** Cash liquidation distributions, box 9, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise" = true → helper "Cash liquidation distributions, box 9"] [helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise" = false → helper "No amount in a box whose condition does not hold"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.other_boxes_if_dividends",{"const":true}],"op":"test"},"then":"div.box9"},{"guard":{"eq":["div.other_boxes_if_dividends",{"const":false}],"op":"test"},"then":"div.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Boxes 9 and 10. Show cash and noncash liquidation distributions" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box10_if_dividends`

- **Authored helper label:** Noncash liquidation distributions, box 10, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise" = true → helper "Noncash liquidation distributions, box 10"] [helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise" = false → helper "No amount in a box whose condition does not hold"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.other_boxes_if_dividends",{"const":true}],"op":"test"},"then":"div.box10"},{"guard":{"eq":["div.other_boxes_if_dividends",{"const":false}],"op":"test"},"then":"div.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Boxes 9 and 10. Show cash and noncash liquidation distributions" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box12_if_dividends`

- **Authored helper label:** Exempt-interest dividends, box 12, when you or your spouse owned shares or received a Form 1099-DIV; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?" = true → helper "Exempt-interest dividends, box 12"] [helper "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?" = false → helper "No amount in a box whose condition does not hold"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.any",{"const":true}],"op":"test"},"then":"div.box12"},{"guard":{"eq":["div.any",{"const":false}],"op":"test"},"then":"div.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 12. Shows exempt-interest dividends from a mutual fund or other RIC paid to you during the calendar year" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box13_if_dividends`

- **Authored helper label:** Specified private activity bond interest dividends, box 13, when a Form 1099-DIV shows an amount in one of the less common boxes; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise" = true → helper "Specified private activity bond interest dividends, box 13"] [helper "An amount in box 2b, 2c, 2d, 3, 9, 10 or 13 of any Form 1099-DIV, when you or your spouse owned shares or received a Form 1099-DIV; false otherwise" = false → helper "No amount in a box whose condition does not hold"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.other_boxes_if_dividends",{"const":true}],"op":"test"},"then":"div.box13"},{"guard":{"eq":["div.other_boxes_if_dividends",{"const":false}],"op":"test"},"then":"div.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 13. Shows exempt-interest dividends subject to the alternative minimum tax. This amount is included in box 12" (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.basis_reconciled_if_return_of_capital`

- **Authored helper label:** For box 3, basis reductions applied, when nondividend distributions (box 3) are above zero; false otherwise
- **Encoded (Bool):** Choose — [helper "Nondividend distributions (box 3) are above zero" = true → helper "Was every nondividend distribution (box 3) no more than the remaining basis in the shares it was paid on?"] [helper "Nondividend distributions (box 3) are above zero" = false → helper "No answer needed where the question is not asked"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.has_return_of_capital",{"const":true}],"op":"test"},"then":"div.basis_reconciled"},{"guard":{"eq":["div.has_return_of_capital",{"const":false}],"op":"test"},"then":"div.no"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable" (January 2024 (continuous-use form); sha256 4ea1de80)
