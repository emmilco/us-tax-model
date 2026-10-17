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

## (helper) — `div.box2e`

- **Authored helper label:** Section 897 ordinary dividends, box 2e
- **Encoded (NonNegDollars):** Input — Section 897 ordinary dividends, box 2e
- Expr: `{"op":"input","source":"Section 897 ordinary dividends, box 2e"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box2f`

- **Authored helper label:** Section 897 capital gain, box 2f
- **Encoded (NonNegDollars):** Input — Section 897 capital gain, box 2f
- Expr: `{"op":"input","source":"Section 897 capital gain, box 2f"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box3`

- **Authored helper label:** Nondividend distributions/return of capital, box 3
- **Encoded (NonNegDollars):** Input — Nondividend distributions/return of capital, box 3
- Expr: `{"op":"input","source":"Nondividend distributions/return of capital, box 3"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box4`

- **Authored helper label:** Federal income tax withheld, box 4
- **Encoded (NonNegDollars):** Input — Federal income tax withheld, box 4
- Expr: `{"op":"input","source":"Federal income tax withheld, box 4"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box6`

- **Authored helper label:** Investment expenses already included in box 1a, box 6
- **Encoded (NonNegDollars):** Input — Investment expenses already included in box 1a, box 6
- Expr: `{"op":"input","source":"Investment expenses already included in box 1a, box 6"}`
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
- **Encoded (NonNegDollars):** Input — Exempt-interest dividends, box 12
- Expr: `{"op":"input","source":"Exempt-interest dividends, box 12"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box13`

- **Authored helper label:** Specified private activity bond interest dividends, box 13
- **Encoded (NonNegDollars):** Input — Specified private activity bond interest dividends, box 13
- Expr: `{"op":"input","source":"Specified private activity bond interest dividends, box 13"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.basis_reconciled`

- **Authored helper label:** For box 3, have basis reductions been applied to records with no distribution exceeding basis?
- **Encoded (Bool):** Input — For box 3, have basis reductions been applied to records with no distribution exceeding basis?
- Expr: `{"op":"input","source":"For box 3, have basis reductions been applied to records with no distribution exceeding basis?"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.fatca`

- **Authored helper label:** Is the FATCA reporting checkbox checked? Review Form 8938 requirements separately.
- **Encoded (Bool):** Input — Is the FATCA reporting checkbox checked? Review Form 8938 requirements separately.
- Expr: `{"op":"input","source":"Is the FATCA reporting checkbox checked? Review Form 8938 requirements separately."}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box1a`

- **Authored helper label:** Amount from sb.ordinary_dividends
- **Encoded (NonNegDollars):** Enter the amount from sb helper "Total ordinary dividends, Form 1099-DIV box 1a".
- Expr: `{"from":"sb.ordinary_dividends","op":"copy"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box1b`

- **Authored helper label:** Amount from f1040.line3a
- **Encoded (NonNegDollars):** Enter the amount from f1040 line 3a.
- Expr: `{"from":"f1040.line3a","op":"copy"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box2a`

- **Authored helper label:** Amount from sd.distributions
- **Encoded (NonNegDollars):** Enter the amount from sd helper "Capital gain distributions, generally Form 1099-DIV box 2a".
- Expr: `{"from":"sd.distributions","op":"copy"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.box5`

- **Authored helper label:** Amount from qbi.dividends
- **Encoded (NonNegDollars):** Enter the amount from qbi helper "Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements".
- Expr: `{"from":"qbi.dividends","op":"copy"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.section1202`

- **Authored helper label:** Section 1202 distribution present
- **Encoded (Bool):** helper "Section 1202 gain, box 2c" > $0
- Expr: `{"gt":["div.box2c",{"const":0}],"op":"test"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.amt`

- **Authored helper label:** Specified private activity bond dividends present
- **Encoded (Bool):** helper "Specified private activity bond interest dividends, box 13" > $0
- Expr: `{"gt":["div.box13",{"const":0}],"op":"test"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.unsupported`

- **Authored helper label:** Unsupported section 897, liquidation or unreconciled basis/excess distribution
- **Encoded (Bool):** (helper "Section 897 ordinary dividends, box 2e" > $0 or helper "Section 897 capital gain, box 2f" > $0 or helper "Cash liquidation distributions, box 9" > $0 or helper "Noncash liquidation distributions, box 10" > $0 or helper "Nondividend distributions/return of capital, box 3" > $0 and helper "For box 3, have basis reductions been applied to records with no distribution exceeding basis?" = false)
- Expr: `{"any":[{"gt":["div.box2e",{"const":0}],"op":"test"},{"gt":["div.box2f",{"const":0}],"op":"test"},{"gt":["div.box9",{"const":0}],"op":"test"},{"gt":["div.box10",{"const":0}],"op":"test"},{"all":[{"gt":["div.box3",{"const":0}],"op":"test"},{"eq":["div.basis_reconciled",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.bad_special`

- **Authored helper label:** A gain component exceeds total capital gain distributions
- **Encoded (Bool):** (helper "Unrecaptured section 1250 gain, box 2b" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Section 1202 gain, box 2c" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Collectibles (28%) gain, box 2d" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Total special capital-gain distribution components" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a")
- Expr: `{"any":[{"gt":["div.box2b","sd.distributions"],"op":"test"},{"gt":["div.box2c","sd.distributions"],"op":"test"},{"gt":["div.box2d","sd.distributions"],"op":"test"},{"gt":["div.special_total","sd.distributions"],"op":"test"}],"op":"test"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.screen`

- **Authored helper label:** Zero only after distribution scope checks
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when div.section1202 is true, cannot complete Form 8949 code Q / Form 6251. Section 1202 distributions require exclusion analysis and may require AMT. Code Q and Form 6251 remain outside scope. Cite: [i1040sd] p. 8, Gain from Form 1099-DIV and Alternative Minimum Tax (2025; printed date 2025-12-11; sha256 650643a6)
- **Refusal:** when div.amt is true, cannot complete Form 6251. Review private activity bond interest for the alternative minimum tax; Form 6251 is outside scope. Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)
- **Refusal:** when div.unsupported is true, cannot complete Form 1099-DIV special distribution treatment. Prepare the required section 897/liquidation treatment or reconcile return-of-capital basis and any excess gain. Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)
- **Refusal:** when div.bad_special is true, cannot complete Form 1099-DIV corrected amounts. Boxes 2b, 2c and 2d are portions of box 2a. Correct inconsistent supplied amounts. Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)
- **Refusal:** when div.bad_components is true, cannot complete Form 1099-DIV dividend components. Correct the supplied totals: qualified dividends and section 199A dividends are portions of ordinary dividends. Cite: [f1099div] Instructions for Recipient, boxes 1a, 1b and 5 (January 2024 (continuous-use form); sha256 4ea1de80)
- Interpretation: amb.2025.box2c_scope
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1–16 (January 2024 (continuous-use form); sha256 4ea1de80)

## (gate) — `div.bad_components`

- **Authored helper label:** Qualified or section 199A dividends exceed ordinary dividends
- **Encoded (Bool):** (f1040 line 3a > sb helper "Total ordinary dividends, Form 1099-DIV box 1a" or qbi helper "Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements" > sb helper "Total ordinary dividends, Form 1099-DIV box 1a")
- Expr: `{"any":[{"gt":["f1040.line3a","sb.ordinary_dividends"],"op":"test"},{"gt":["qbi.dividends","sb.ordinary_dividends"],"op":"test"}],"op":"test"}`
- Cite: [f1099div] Instructions for Recipient, boxes 1a, 1b and 5 (January 2024 (continuous-use form); sha256 4ea1de80)

## (helper) — `div.special_total`

- **Authored helper label:** Total special capital-gain distribution components
- **Encoded (NonNegDollars):** Add helper "Unrecaptured section 1250 gain, box 2b", helper "Section 1202 gain, box 2c", and helper "Collectibles (28%) gain, box 2d".
- Expr: `{"of":["div.box2b","div.box2c","div.box2d"],"op":"sum"}`
- Cite: [f1099div] Instructions for Recipient, capital gain components in boxes 2b–2d (January 2024 (continuous-use form); sha256 4ea1de80)
