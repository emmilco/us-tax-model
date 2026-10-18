# Schedule B — supported interest and ordinary dividends

- Document: `sb` (form, tax year 2025)
- Note: Payer keys identify records. Foreign-account and trust answers are retained even where income is below the threshold. FBAR/Form 8938 determinations remain explicit taxpayer answers; required foreign forms cause named refusals.

## (helper) — `sb.unsupported`

- **Authored helper label:** Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, foreign corporation reporting, or other special treatment?
- **Encoded (Bool):** Input — Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, foreign corporation reporting, or other special treatment?
- Expr: `{"op":"input","source":"Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, foreign corporation reporting, or other special treatment?"}`
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

- **IRS:** Received a distribution from, or were grantor of or transferor to, a foreign trust during 2025?
- **Encoded (Bool):** Input — Received a distribution from, or were grantor of or transferor to, a foreign trust during 2025?
- Expr: `{"op":"input","source":"Received a distribution from, or were grantor of or transferor to, a foreign trust during 2025?"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 2 — `sb.line2`

- **IRS:** Total taxable interest from all payers
- **Encoded (NonNegDollars):** Add interest.amount over every confirmed interest entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sb.unsupported is true, cannot complete Schedule B special treatment / Form 8815. Prepare the applicable adjustment or exclusion; this tool supports unadjusted taxable interest and ordinary dividends. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.fbar_required is true, cannot complete FinCEN Form 114 (FBAR). Foreign-account reporting and the required country list are outside this tool. Prepare the separate FBAR and Schedule B disclosures. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form8938 is true, cannot complete Form 8938. Prepare the required foreign financial asset disclosure; this tool does not prepare Form 8938. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.line8 is true, cannot complete Form 3520 / Form 3520-A. Review and prepare the required foreign-trust information returns; this path is outside scope. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- Expr: `{"collection":"interest","field":"interest.amount","op":"sum_over"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 3 — `sb.line3`

- **IRS:** Amount from sb.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sb.unsupported is true, cannot complete Schedule B special treatment / Form 8815. Prepare the applicable adjustment or exclusion; this tool supports unadjusted taxable interest and ordinary dividends. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
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

- **IRS:** Amount from sb.ordinary_dividends
- **Encoded (NonNegDollars):** Enter the amount from helper "Total ordinary dividends, Form 1099-DIV box 1a".
- **Refusal:** when sb.unsupported is true, cannot complete Schedule B special treatment / Form 8815. Prepare the applicable adjustment or exclusion; this tool supports unadjusted taxable interest and ordinary dividends. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.fbar_required is true, cannot complete FinCEN Form 114 (FBAR). Foreign-account reporting and the required country list are outside this tool. Prepare the separate FBAR and Schedule B disclosures. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form8938 is true, cannot complete Form 8938. Prepare the required foreign financial asset disclosure; this tool does not prepare Form 8938. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.line8 is true, cannot complete Form 3520 / Form 3520-A. Review and prepare the required foreign-trust information returns; this path is outside scope. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- Expr: `{"from":"sb.ordinary_dividends","op":"copy"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.partIII`

- **Authored helper label:** Complete Part III for interest/dividends over $1,500 or foreign account/trust
- **Encoded (Bool):** (line 4 > $1,500 or line 6 > $1,500 or line 7a = true or line 8 = true)
- Expr: `{"any":[{"gt":["sb.line4",{"const":150000}],"op":"test"},{"gt":["sb.line6",{"const":150000}],"op":"test"},{"eq":["sb.line7a",{"const":true}],"op":"test"},{"eq":["sb.line8",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
