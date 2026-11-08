# Schedule B — supported interest and ordinary dividends

- Document: `sb` (form, tax year 2025)
- Note: Payer keys identify records. Foreign-account and trust answers are retained even where income is below the threshold. FBAR/Form 8938 determinations remain explicit taxpayer answers; required foreign forms cause named refusals.

## (helper) — `sb.unsupported`

- **Authored helper label:** Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, or other special treatment?
- **Encoded (Bool):** Input — Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, or other special treatment?
- Expr: `{"op":"input","source":"Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, or other special treatment?"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.ordinary_dividends`

- **Authored helper label:** Total ordinary dividends, Form 1099-DIV box 1a
- **Encoded (NonNegDollars):** Input — Total ordinary dividends, Form 1099-DIV box 1a
- Expr: `{"op":"input","source":"Total ordinary dividends, Form 1099-DIV box 1a"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 7a — `sb.line7a`

- **IRS:** Any financial interest in or signature authority over a foreign financial account during 2025?
- **Encoded (Bool):** Input — Any financial interest in or signature authority over a foreign financial account during 2025?
- Expr: `{"op":"input","source":"Any financial interest in or signature authority over a foreign financial account during 2025?"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.fbar_required`

- **Authored helper label:** Are you required to file FinCEN Form 114 (FBAR)? Determine under its instructions; this tool does not determine foreign account values or exceptions.
- **Encoded (Bool):** Input — Are you required to file FinCEN Form 114 (FBAR)? Determine under its instructions; this tool does not determine foreign account values or exceptions.
- Expr: `{"op":"input","source":"Are you required to file FinCEN Form 114 (FBAR)? Determine under its instructions; this tool does not determine foreign account values or exceptions."}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.form8938`

- **Authored helper label:** Are you required to file Form 8938 for specified foreign financial assets?
- **Encoded (Bool):** Input — Are you required to file Form 8938 for specified foreign financial assets?
- Expr: `{"op":"input","source":"Are you required to file Form 8938 for specified foreign financial assets?"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 8 — `sb.line8`

- **IRS:** During 2025, did you receive a distribution from a foreign trust (a loan of cash or marketable securities counts), or were you the grantor of, or a transferor to, a foreign trust that existed at any time during 2025?
- **Encoded (Bool):** Input — During 2025, did you receive a distribution from a foreign trust (a loan of cash or marketable securities counts), or were you the grantor of, or a transferor to, a foreign trust that existed at any time during 2025?
- Expr: `{"op":"input","source":"During 2025, did you receive a distribution from a foreign trust (a loan of cash or marketable securities counts), or were you the grantor of, or a transferor to, a foreign trust that existed at any time during 2025?"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts; p. 3, Line 8, "a loan of cash or marketable securities is generally considered to be a distribution"; "If you were the grantor of, or transferor to, a foreign trust that existed during 2025, you may have to file Form 3520." (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 2 — `sb.line2`

- **IRS:** Total taxable interest from all payers
- **Encoded (NonNegDollars):** Add interest.amount over every confirmed interest entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sb.unsupported_if_income is true, cannot complete Schedule B special treatment / Form 8815. Prepare the applicable adjustment or exclusion; this tool supports unadjusted taxable interest and ordinary dividends. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form5471 is true, cannot complete Form 5471. You may have to file Form 5471 for a foreign corporation; this tool does not prepare it. Cite: [i1040sb] p. 2, Part II. Ordinary Dividends, TIP, "You may have to file Form 5471 if, in 2025, you were an officer or director of a foreign corporation", "You may also have to file Form 5471 if, in 2025, you owned 10% or more of the total (a) value of a foreign corporation’s stock, or (b) combined voting power of all classes of a foreign corporation’s stock with voting rights" (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.fbar_required is true, cannot complete FinCEN Form 114 (FBAR). Foreign-account reporting and the required country list are outside this tool. Prepare the separate FBAR and Schedule B disclosures. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form8938 is true, cannot complete Form 8938. Prepare the required foreign financial asset disclosure; this tool does not prepare Form 8938. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.line8 is true, cannot complete Form 3520 / Form 3520-A. Review and prepare the required foreign-trust information returns; this path is outside scope. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- Expr: `{"collection":"interest","field":"interest.amount","op":"sum_over"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 3 — `sb.line3`

- **IRS:** Amount from sb.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sb.unsupported_if_income is true, cannot complete Schedule B special treatment / Form 8815. Prepare the applicable adjustment or exclusion; this tool supports unadjusted taxable interest and ordinary dividends. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form5471 is true, cannot complete Form 5471. You may have to file Form 5471 for a foreign corporation; this tool does not prepare it. Cite: [i1040sb] p. 2, Part II. Ordinary Dividends, TIP, "You may have to file Form 5471 if, in 2025, you were an officer or director of a foreign corporation", "You may also have to file Form 5471 if, in 2025, you owned 10% or more of the total (a) value of a foreign corporation’s stock, or (b) combined voting power of all classes of a foreign corporation’s stock with voting rights" (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.fbar_required is true, cannot complete FinCEN Form 114 (FBAR). Foreign-account reporting and the required country list are outside this tool. Prepare the separate FBAR and Schedule B disclosures. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form8938 is true, cannot complete Form 8938. Prepare the required foreign financial asset disclosure; this tool does not prepare Form 8938. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.line8 is true, cannot complete Form 3520 / Form 3520-A. Review and prepare the required foreign-trust information returns; this path is outside scope. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- Expr: `{"from":"sb.zero","op":"copy"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 4 — `sb.line4`

- **IRS:** Subtract sb.line3 from sb.line2
- **Encoded (Dollars):** Subtract line 3 from line 2.
- Expr: `{"from":"sb.line2","op":"subtract","take":"sb.line3"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 6 — `sb.line6`

- **IRS:** Amount from sb.ordinary_dividends_if_dividends
- **Encoded (NonNegDollars):** Enter the amount from helper "Total ordinary dividends, Form 1099-DIV box 1a, when you or your spouse received dividends or other distributions; zero otherwise".
- **Refusal:** when sb.unsupported_if_income is true, cannot complete Schedule B special treatment / Form 8815. Prepare the applicable adjustment or exclusion; this tool supports unadjusted taxable interest and ordinary dividends. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form5471 is true, cannot complete Form 5471. You may have to file Form 5471 for a foreign corporation; this tool does not prepare it. Cite: [i1040sb] p. 2, Part II. Ordinary Dividends, TIP, "You may have to file Form 5471 if, in 2025, you were an officer or director of a foreign corporation", "You may also have to file Form 5471 if, in 2025, you owned 10% or more of the total (a) value of a foreign corporation’s stock, or (b) combined voting power of all classes of a foreign corporation’s stock with voting rights" (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.fbar_required is true, cannot complete FinCEN Form 114 (FBAR). Foreign-account reporting and the required country list are outside this tool. Prepare the separate FBAR and Schedule B disclosures. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form8938 is true, cannot complete Form 8938. Prepare the required foreign financial asset disclosure; this tool does not prepare Form 8938. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.line8 is true, cannot complete Form 3520 / Form 3520-A. Review and prepare the required foreign-trust information returns; this path is outside scope. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- Expr: `{"from":"sb.ordinary_dividends_if_dividends","op":"copy"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.partIII`

- **Authored helper label:** Complete Part III for interest/dividends over $1,500 or foreign account/trust
- **Encoded (Bool):** (line 4 > $1,500 or line 6 > $1,500 or line 7a = true or line 8 = true)
- Expr: `{"any":[{"gt":["sb.line4",{"const":150000}],"op":"test"},{"gt":["sb.line6",{"const":150000}],"op":"test"},{"eq":["sb.line7a",{"const":true}],"op":"test"},{"eq":["sb.line8",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.form5471`

- **Authored helper label:** In 2025, were you (or your spouse) an officer or director of a foreign corporation, or did you (or your spouse) own 10% or more of the total value of a foreign corporation's stock, or of the combined voting power of all classes of a foreign corporation's stock with voting rights?
- **Encoded (Bool):** Input — In 2025, were you (or your spouse) an officer or director of a foreign corporation, or did you (or your spouse) own 10% or more of the total value of a foreign corporation's stock, or of the combined voting power of all classes of a foreign corporation's stock with voting rights?
- Expr: `{"op":"input","source":"In 2025, were you (or your spouse) an officer or director of a foreign corporation, or did you (or your spouse) own 10% or more of the total value of a foreign corporation's stock, or of the combined voting power of all classes of a foreign corporation's stock with voting rights?"}`
- Cite: [i1040sb] p. 2, Part II. Ordinary Dividends, TIP, "You may have to file Form 5471 if, in 2025, you were an officer or director of a foreign corporation", "You may also have to file Form 5471 if, in 2025, you owned 10% or more of the total (a) value of a foreign corporation’s stock, or (b) combined voting power of all classes of a foreign corporation’s stock with voting rights" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.interest_total`

- **Authored helper label:** Taxable interest from all payers, before any Schedule B adjustment
- **Encoded (NonNegDollars):** Add interest.amount over every confirmed interest entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"interest","field":"interest.amount","op":"sum_over"}`
- Cite: [i1040sb] p. 1, Line 1, "Report on line 1 all of your taxable interest" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (gate) — `sb.has_income`

- **Authored helper label:** Taxable interest, ordinary dividends or capital gain distributions are above zero
- **Encoded (Bool):** (helper "Taxable interest from all payers, before any Schedule B adjustment" > $0 or helper "Total ordinary dividends, Form 1099-DIV box 1a, when you or your spouse received dividends or other distributions; zero otherwise" > $0 or sd helper "Capital gain distributions, generally Form 1099-DIV box 2a, when you or your spouse received dividends or other distributions; zero otherwise" > $0)
- Expr: `{"any":[{"gt":["sb.interest_total",{"const":0}],"op":"test"},{"gt":["sb.ordinary_dividends_if_dividends",{"const":0}],"op":"test"},{"gt":["sd.distributions_if_dividends",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.no`

- **Authored helper label:** No special treatment without interest, ordinary dividends or capital gain distributions
- **Encoded (Bool):** Enter false (sb.no).
- Expr: `{"op":"param","ref":"sb.no"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.ordinary_dividends_if_dividends`

- **Authored helper label:** Total ordinary dividends, Form 1099-DIV box 1a, when you or your spouse received dividends or other distributions; zero otherwise
- **Encoded (NonNegDollars):** Choose — [div helper "In 2025, did you (or your spouse) receive any dividends or other distributions from a company or a fund, with or without a Form 1099-DIV? Count amounts that were reinvested, credited to an account or paid in shares or other property. Answer Yes if any of these applies:" = true → helper "Total ordinary dividends, Form 1099-DIV box 1a"] [div helper "In 2025, did you (or your spouse) receive any dividends or other distributions from a company or a fund, with or without a Form 1099-DIV? Count amounts that were reinvested, credited to an account or paid in shares or other property. Answer Yes if any of these applies:" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.any",{"const":true}],"op":"test"},"then":"sb.ordinary_dividends"},{"guard":{"eq":["div.any",{"const":false}],"op":"test"},"then":"sb.zero"}],"op":"choose"}`
- Cite: [i1040sb] p. 2, Line 5, "Report on line 5 all of your ordinary dividends. This amount should be shown in box 1a of your Forms 1099-DIV or substitute statements" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.unsupported_if_income`

- **Authored helper label:** Schedule B special treatment, when taxable interest, ordinary dividends or capital gain distributions are above zero; false otherwise
- **Encoded (Bool):** Choose — [helper "Taxable interest, ordinary dividends or capital gain distributions are above zero" = true → helper "Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, or other special treatment?"] [helper "Taxable interest, ordinary dividends or capital gain distributions are above zero" = false → helper "No special treatment without interest, ordinary dividends or capital gain distributions"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.has_income",{"const":true}],"op":"test"},"then":"sb.unsupported"},{"guard":{"eq":["sb.has_income",{"const":false}],"op":"test"},"then":"sb.no"}],"op":"choose"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)
