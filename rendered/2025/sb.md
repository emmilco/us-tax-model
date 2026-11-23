# Schedule B — supported interest and ordinary dividends

- Document: `sb` (form, tax year 2025)
- Note: Payer keys identify records. Foreign-account and trust answers are retained even where income is below the threshold. FBAR/Form 8938 determinations remain explicit taxpayer answers; required foreign forms cause named refusals.

## (helper) — `sb.nominee`

- **Authored helper label:** Interest or ordinary dividends received as a nominee
- **Encoded (Bool):** Input — Does any of the interest or dividends you (or, on a joint return, your spouse) received in 2025 belong to someone else, for example to the other owner of a joint account who is not your spouse?
- Expr: `{"op":"input","source":"Does any of the interest or dividends you (or, on a joint return, your spouse) received in 2025 belong to someone else, for example to the other owner of a joint account who is not your spouse?"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.bonds_any`

- **Authored helper label:** Bonds or notes owned directly, U.S. savings bonds cashed, or interest on a loan made or a property sold
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) own bonds or notes directly (not through a fund), cash in U.S. savings bonds, or receive interest on money you lent or on a property you sold?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) own bonds or notes directly (not through a fund), cash in U.S. savings bonds, or receive interest on money you lent or on a property you sold?"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.bond_special`

- **Authored helper label:** Original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, or other special treatment
- **Encoded (Bool):** Input — Does any of these apply to that interest?

  - you bought a bond between interest dates and paid the seller the interest earned up to then
  - you paid more than face value for a bond (bond premium), or a Form 1099-INT shows an amount in box 10, 11, 12 or 13, or a Form 1099-OID in box 6 or 10
  - you report a different amount of original issue discount than a Form 1099-OID shows, or have market discount to report
  - a bond whose payments depend on something uncertain (a contingent payment debt instrument)
  - the buyer of your home or other property pays you interest on the price (a seller-financed mortgage)
  - you want to leave out U.S. savings bond interest because you paid for higher education (Form 8815)
  - any other adjustment to the interest or dividends shown on your forms
- Expr: `{"op":"input","source":"Does any of these apply to that interest?\n\n- you bought a bond between interest dates and paid the seller the interest earned up to then\n- you paid more than face value for a bond (bond premium), or a Form 1099-INT shows an amount in box 10, 11, 12 or 13, or a Form 1099-OID in box 6 or 10\n- you report a different amount of original issue discount than a Form 1099-OID shows, or have market discount to report\n- a bond whose payments depend on something uncertain (a contingent payment debt instrument)\n- the buyer of your home or other property pays you interest on the price (a seller-financed mortgage)\n- you want to leave out U.S. savings bond interest because you paid for higher education (Form 8815)\n- any other adjustment to the interest or dividends shown on your forms"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee"; f1099oid p. 7, Box 6, "shows the amount of acquisition premium amortization for the year that reduces the amount of OID", Box 10, "shows the amount of premium amortization" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.unsupported`

- **Authored helper label:** Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, or other special treatment
- **Encoded (Bool):** (helper "Interest or ordinary dividends received as a nominee, when taxable interest, ordinary dividends or capital gain distributions are above zero; false otherwise" = true or helper "Special treatment of bond or loan interest, when bonds or notes were owned directly, savings bonds cashed, or interest received on a loan or a sale; false otherwise" = true)
- Expr: `{"any":[{"eq":["sb.nominee_if_income",{"const":true}],"op":"test"},{"eq":["sb.bond_special_if_bonds",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.ordinary_dividends`

- **Authored helper label:** Total ordinary dividends, Form 1099-DIV box 1a
- **Encoded (NonNegDollars):** Input — Total ordinary dividends, Form 1099-DIV box 1a
- Expr: `{"op":"input","source":"Total ordinary dividends, Form 1099-DIV box 1a"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (gate) — `sb.account_any`

- **Authored helper label:** At any time in 2025, did you (or, on a joint return, your spouse) have an account in another country (a bank, investment, pension, payment or crypto account), or the power to sign for one?
- **Encoded (Bool):** Input — At any time in 2025, did you (or, on a joint return, your spouse) have an account in another country (a bank, investment, pension, payment or crypto account), or the power to sign for one?
- Expr: `{"op":"input","source":"At any time in 2025, did you (or, on a joint return, your spouse) have an account in another country (a bank, investment, pension, payment or crypto account), or the power to sign for one?"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust"; i1040sb pp. 2–3, Part III, lines 7a and 8; fincen114 pp. 4–5, Who Must File an FBAR, Financial Account, Foreign Financial Account, Financial Interest, Signature Authority; i8938 pp. 7–8, Specified Foreign Financial Assets, Interests in Foreign Estates and Foreign Trusts, Interests in Foreign Pension Plans and Foreign Deferred Compensation Plans (2025; created 2025-04-23; sha256 dd1ec371)

## (gate) — `sb.asset_any`

- **Authored helper label:** At any time in 2025, did you (or, on a joint return, your spouse) own anything else of value outside the United States, or were you owed money by someone abroad?
- **Encoded (Bool):** Input — At any time in 2025, did you (or, on a joint return, your spouse) own anything else of value outside the United States, or were you owed money by someone abroad?
- Expr: `{"op":"input","source":"At any time in 2025, did you (or, on a joint return, your spouse) own anything else of value outside the United States, or were you owed money by someone abroad?"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust"; i1040sb pp. 2–3, Part III, lines 7a and 8; fincen114 pp. 4–5, Who Must File an FBAR, Financial Account, Foreign Financial Account, Financial Interest, Signature Authority; i8938 pp. 7–8, Specified Foreign Financial Assets, Interests in Foreign Estates and Foreign Trusts, Interests in Foreign Pension Plans and Foreign Deferred Compensation Plans (2025; created 2025-04-23; sha256 dd1ec371)

## (gate) — `sb.trust_any`

- **Authored helper label:** Do you (or, on a joint return, your spouse) have anything to do with a trust or family foundation that is outside the United States or has a trustee abroad, as the person who set it up, gave to it, or may receive from it?
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) have anything to do with a trust or family foundation that is outside the United States or has a trustee abroad, as the person who set it up, gave to it, or may receive from it?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) have anything to do with a trust or family foundation that is outside the United States or has a trustee abroad, as the person who set it up, gave to it, or may receive from it?"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust"; i1040sb pp. 2–3, Part III, lines 7a and 8; fincen114 pp. 4–5, Who Must File an FBAR, Financial Account, Foreign Financial Account, Financial Interest, Signature Authority; i8938 pp. 7–8, Specified Foreign Financial Assets, Interests in Foreign Estates and Foreign Trusts, Interests in Foreign Pension Plans and Foreign Deferred Compensation Plans (2025; created 2025-04-23; sha256 dd1ec371)

## (gate) — `sb.company_any`

- **Authored helper label:** In 2025, were you (or, on a joint return, your spouse) a director, officer or manager of a company set up outside the United States, or an owner, alone or with your family, of 10% or more of one?
- **Encoded (Bool):** Input — In 2025, were you (or, on a joint return, your spouse) a director, officer or manager of a company set up outside the United States, or an owner, alone or with your family, of 10% or more of one?
- Expr: `{"op":"input","source":"In 2025, were you (or, on a joint return, your spouse) a director, officer or manager of a company set up outside the United States, or an owner, alone or with your family, of 10% or more of one?"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust"; i1040sb pp. 2–3, Part III, lines 7a and 8; fincen114 pp. 4–5, Who Must File an FBAR, Financial Account, Foreign Financial Account, Financial Interest, Signature Authority; i8938 pp. 7–8, Specified Foreign Financial Assets, Interests in Foreign Estates and Foreign Trusts, Interests in Foreign Pension Plans and Foreign Deferred Compensation Plans (2025; created 2025-04-23; sha256 dd1ec371)

## (gate) — `sb.territory_any`

- **Authored helper label:** At any time in 2025, did you (or, on a joint return, your spouse) have an account, an investment, a company or a trust in Puerto Rico, Guam or another U.S. territory?
- **Encoded (Bool):** Input — At any time in 2025, did you (or, on a joint return, your spouse) have an account, an investment, a company or a trust in Puerto Rico, Guam or another U.S. territory?
- Expr: `{"op":"input","source":"At any time in 2025, did you (or, on a joint return, your spouse) have an account, an investment, a company or a trust in Puerto Rico, Guam or another U.S. territory?"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust"; i1040sb pp. 2–3, Part III, lines 7a and 8; fincen114 pp. 4–5, Who Must File an FBAR, Financial Account, Foreign Financial Account, Financial Interest, Signature Authority; i8938 pp. 7–8, Specified Foreign Financial Assets, Interests in Foreign Estates and Foreign Trusts, Interests in Foreign Pension Plans and Foreign Deferred Compensation Plans (2025; created 2025-04-23; sha256 dd1ec371)

## (gate) — `sb.foreign_any`

- **Authored helper label:** A foreign account, another foreign financial asset, a connection to a foreign trust or a role in a foreign corporation, or any of these in a U.S. territory, at any time in 2025
- **Encoded (Bool):** (helper "At any time in 2025, did you (or, on a joint return, your spouse) have an account in another country (a bank, investment, pension, payment or crypto account), or the power to sign for one?" = true or helper "At any time in 2025, did you (or, on a joint return, your spouse) own anything else of value outside the United States, or were you owed money by someone abroad?" = true or helper "Do you (or, on a joint return, your spouse) have anything to do with a trust or family foundation that is outside the United States or has a trustee abroad, as the person who set it up, gave to it, or may receive from it?" = true or helper "In 2025, were you (or, on a joint return, your spouse) a director, officer or manager of a company set up outside the United States, or an owner, alone or with your family, of 10% or more of one?" = true or helper "At any time in 2025, did you (or, on a joint return, your spouse) have an account, an investment, a company or a trust in Puerto Rico, Guam or another U.S. territory?" = true)
- Expr: `{"any":[{"eq":["sb.account_any",{"const":true}],"op":"test"},{"eq":["sb.asset_any",{"const":true}],"op":"test"},{"eq":["sb.trust_any",{"const":true}],"op":"test"},{"eq":["sb.company_any",{"const":true}],"op":"test"},{"eq":["sb.territory_any",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust"; i1040sb pp. 2–3, Part III, lines 7a and 8; fincen114 pp. 4–5, Who Must File an FBAR, Financial Account, Foreign Financial Account, Financial Interest, Signature Authority; i8938 pp. 7–8, Specified Foreign Financial Assets, Interests in Foreign Estates and Foreign Trusts, Interests in Foreign Pension Plans and Foreign Deferred Compensation Plans (2025; created 2025-04-23; sha256 dd1ec371)

## (gate) — `sb.foreign_trust_any`

- **Authored helper label:** A connection to a foreign trust, or an account, investment, company or trust in a U.S. territory
- **Encoded (Bool):** (helper "Do you (or, on a joint return, your spouse) have anything to do with a trust or family foundation that is outside the United States or has a trustee abroad, as the person who set it up, gave to it, or may receive from it?" = true or helper "At any time in 2025, did you (or, on a joint return, your spouse) have an account, an investment, a company or a trust in Puerto Rico, Guam or another U.S. territory?" = true)
- Expr: `{"any":[{"eq":["sb.trust_any",{"const":true}],"op":"test"},{"eq":["sb.territory_any",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust"; i1040sb pp. 2–3, Part III, lines 7a and 8; fincen114 pp. 4–5, Who Must File an FBAR, Financial Account, Foreign Financial Account, Financial Interest, Signature Authority; i8938 pp. 7–8, Specified Foreign Financial Assets, Interests in Foreign Estates and Foreign Trusts, Interests in Foreign Pension Plans and Foreign Deferred Compensation Plans (2025; created 2025-04-23; sha256 dd1ec371)

## (gate) — `sb.foreign_company_any`

- **Authored helper label:** A role in or 10% of a foreign company, or an account, investment, company or trust in a U.S. territory
- **Encoded (Bool):** (helper "In 2025, were you (or, on a joint return, your spouse) a director, officer or manager of a company set up outside the United States, or an owner, alone or with your family, of 10% or more of one?" = true or helper "At any time in 2025, did you (or, on a joint return, your spouse) have an account, an investment, a company or a trust in Puerto Rico, Guam or another U.S. territory?" = true)
- Expr: `{"any":[{"eq":["sb.company_any",{"const":true}],"op":"test"},{"eq":["sb.territory_any",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust"; i1040sb pp. 2–3, Part III, lines 7a and 8; fincen114 pp. 4–5, Who Must File an FBAR, Financial Account, Foreign Financial Account, Financial Interest, Signature Authority; i8938 pp. 7–8, Specified Foreign Financial Assets, Interests in Foreign Estates and Foreign Trusts, Interests in Foreign Pension Plans and Foreign Deferred Compensation Plans (2025; created 2025-04-23; sha256 dd1ec371)

## (helper) — `sb.foreign_no`

- **Authored helper label:** No foreign account, asset, trust or corporation question without a foreign connection
- **Encoded (Bool):** Enter false (sb.foreign_no).
- Expr: `{"op":"param","ref":"sb.foreign_no"}`
- Cite: [f1040sb] Part III, Foreign Accounts and Trusts, "You must complete this part if you (a) had over $1,500 of taxable interest or ordinary dividends; (b) had a foreign account; or (c) received a distribution from, or were a grantor of, or a transferor to, a foreign trust" (2025; created 2025-04-23; sha256 dd1ec371)

## 7a — `sb.line7a`

- **IRS:** Any financial interest in or signature authority over a foreign financial account during 2025?
- **Encoded (Bool):** Input — Any financial interest in or signature authority over a foreign financial account during 2025?
- Expr: `{"op":"input","source":"Any financial interest in or signature authority over a foreign financial account during 2025?"}`
- Cite: [i1040sb] pp. 2–3, Line 7a—Question 1, "Check the “Yes” box even if you aren't required to file FinCEN Form 114", "an insurance policy with a cash value", "shares in a mutual fund or similar pooled fund", "A financial account is located in a foreign country if the account is physically located outside of the United States", "Don't consider the exceptions relating to signature authority in answering Question 1 on line 7a"; fincen114 p. 4, Foreign Financial Account, "An account maintained with a branch of a foreign bank that is physically located in the United States is not a foreign financial account"; fincen114 p. 5, United States, "all United States territories and possessions" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.fbar_required`

- **Authored helper label:** Are you (or, on a joint return, your spouse) required to file FinCEN Form 114 (FBAR)? Determine under its instructions; this tool does not determine foreign account values or exceptions.
- **Encoded (Bool):** Input — Are you (or, on a joint return, your spouse) required to file FinCEN Form 114 (FBAR)? Determine under its instructions; this tool does not determine foreign account values or exceptions.
- Expr: `{"op":"input","source":"Are you (or, on a joint return, your spouse) required to file FinCEN Form 114 (FBAR)? Determine under its instructions; this tool does not determine foreign account values or exceptions."}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.form8938`

- **Authored helper label:** Are you (or, on a joint return, your spouse) required to file Form 8938 for specified foreign financial assets?
- **Encoded (Bool):** Input — Are you (or, on a joint return, your spouse) required to file Form 8938 for specified foreign financial assets?
- Expr: `{"op":"input","source":"Are you (or, on a joint return, your spouse) required to file Form 8938 for specified foreign financial assets?"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 8 — `sb.line8`

- **IRS:** During 2025, did you (or, on a joint return, your spouse) receive a distribution from a foreign trust, including money or property that reached you through another person or company (a loan of cash or marketable securities counts, and so does free or below-market use of a home, car or other property the trust owns), or were you (or, on a joint return, your spouse) the grantor of, or a transferor to, a foreign trust that existed at any time during 2025, even one created or funded in an earlier year (a transferor is anyone who gave, sold, lent or otherwise transferred money or property to the trust, directly or through another person, in 2025 or any earlier year)? A foreign foundation, a waqf or another arrangement that holds property for beneficiaries counts as a trust; a trust counts as foreign unless a court in one of the 50 states or the District of Columbia (not one in Puerto Rico, Guam or another US territory) can supervise its administration and US persons (US citizens or residents, or US companies such as a US bank) control all of its substantial decisions, so it is foreign if anyone else can make or veto any of them, even if the trust was set up under US law or has a US address; if you are not sure whether an arrangement is a trust or whether a trust is foreign, answer Yes.
- **Encoded (Bool):** Input — During 2025, did you (or, on a joint return, your spouse) receive a distribution from a foreign trust, including money or property that reached you through another person or company (a loan of cash or marketable securities counts, and so does free or below-market use of a home, car or other property the trust owns), or were you (or, on a joint return, your spouse) the grantor of, or a transferor to, a foreign trust that existed at any time during 2025, even one created or funded in an earlier year (a transferor is anyone who gave, sold, lent or otherwise transferred money or property to the trust, directly or through another person, in 2025 or any earlier year)? A foreign foundation, a waqf or another arrangement that holds property for beneficiaries counts as a trust; a trust counts as foreign unless a court in one of the 50 states or the District of Columbia (not one in Puerto Rico, Guam or another US territory) can supervise its administration and US persons (US citizens or residents, or US companies such as a US bank) control all of its substantial decisions, so it is foreign if anyone else can make or veto any of them, even if the trust was set up under US law or has a US address; if you are not sure whether an arrangement is a trust or whether a trust is foreign, answer Yes.
- Expr: `{"op":"input","source":"During 2025, did you (or, on a joint return, your spouse) receive a distribution from a foreign trust, including money or property that reached you through another person or company (a loan of cash or marketable securities counts, and so does free or below-market use of a home, car or other property the trust owns), or were you (or, on a joint return, your spouse) the grantor of, or a transferor to, a foreign trust that existed at any time during 2025, even one created or funded in an earlier year (a transferor is anyone who gave, sold, lent or otherwise transferred money or property to the trust, directly or through another person, in 2025 or any earlier year)? A foreign foundation, a waqf or another arrangement that holds property for beneficiaries counts as a trust; a trust counts as foreign unless a court in one of the 50 states or the District of Columbia (not one in Puerto Rico, Guam or another US territory) can supervise its administration and US persons (US citizens or residents, or US companies such as a US bank) control all of its substantial decisions, so it is foreign if anyone else can make or veto any of them, even if the trust was set up under US law or has a US address; if you are not sure whether an arrangement is a trust or whether a trust is foreign, answer Yes."}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts; p. 3, Line 8, "a loan of cash or marketable securities is generally considered to be a distribution"; "If you were the grantor of, or transferor to, a foreign trust that existed during 2025, you may have to file Form 3520."; cfr-26-301-7701-7 pp. 1–2, In general, "A trust is a United States person if", "The term foreign trust means any trust other than a domestic trust"; cfr-26-301-7701-7 p. 2, The court test, "a court within a territory or possession of the United States or within a foreign country is not a court within the United States"; cfr-26-301-7701-7 p. 4, Control test, "with no other person having the power to veto any of the substantial decisions" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 2 — `sb.line2`

- **IRS:** Total taxable interest from all payers
- **Encoded (NonNegDollars):** Add interest.amount over every confirmed interest entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sb.unsupported_if_income is true, cannot complete Schedule B special treatment / Form 8815. Prepare the applicable adjustment or exclusion; this tool supports unadjusted taxable interest and ordinary dividends. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.fbar_required_if_foreign is true, cannot complete FinCEN Form 114 (FBAR). Foreign-account reporting and the required country list are outside this tool. Prepare the separate FBAR and Schedule B disclosures. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form8938_if_foreign is true, cannot complete Form 8938. Prepare the required foreign financial asset disclosure; this tool does not prepare Form 8938. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.line8_if_foreign is true, cannot complete Form 3520 / Form 3520-A. Review and prepare the required foreign-trust information returns; this path is outside scope. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form5471_if_foreign is true, cannot complete Form 5471. You may have to file Form 5471 for a foreign corporation; this tool does not prepare it. Cite: [i1040sb] p. 2, Part II. Ordinary Dividends, TIP, "You may have to file Form 5471 if, in 2025, you were an officer or director of a foreign corporation", "You may also have to file Form 5471 if, in 2025, you owned 10% or more of the total (a) value of a foreign corporation’s stock, or (b) combined voting power of all classes of a foreign corporation’s stock with voting rights" (TY2025; printed April 23, 2025; sha256 b92f31ec)
- Expr: `{"collection":"interest","field":"interest.amount","op":"sum_over"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## 3 — `sb.line3`

- **IRS:** Amount from sb.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sb.unsupported_if_income is true, cannot complete Schedule B special treatment / Form 8815. Prepare the applicable adjustment or exclusion; this tool supports unadjusted taxable interest and ordinary dividends. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.fbar_required_if_foreign is true, cannot complete FinCEN Form 114 (FBAR). Foreign-account reporting and the required country list are outside this tool. Prepare the separate FBAR and Schedule B disclosures. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form8938_if_foreign is true, cannot complete Form 8938. Prepare the required foreign financial asset disclosure; this tool does not prepare Form 8938. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.line8_if_foreign is true, cannot complete Form 3520 / Form 3520-A. Review and prepare the required foreign-trust information returns; this path is outside scope. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form5471_if_foreign is true, cannot complete Form 5471. You may have to file Form 5471 for a foreign corporation; this tool does not prepare it. Cite: [i1040sb] p. 2, Part II. Ordinary Dividends, TIP, "You may have to file Form 5471 if, in 2025, you were an officer or director of a foreign corporation", "You may also have to file Form 5471 if, in 2025, you owned 10% or more of the total (a) value of a foreign corporation’s stock, or (b) combined voting power of all classes of a foreign corporation’s stock with voting rights" (TY2025; printed April 23, 2025; sha256 b92f31ec)
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
- **Refusal:** when sb.fbar_required_if_foreign is true, cannot complete FinCEN Form 114 (FBAR). Foreign-account reporting and the required country list are outside this tool. Prepare the separate FBAR and Schedule B disclosures. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form8938_if_foreign is true, cannot complete Form 8938. Prepare the required foreign financial asset disclosure; this tool does not prepare Form 8938. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.line8_if_foreign is true, cannot complete Form 3520 / Form 3520-A. Review and prepare the required foreign-trust information returns; this path is outside scope. Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)
- **Refusal:** when sb.form5471_if_foreign is true, cannot complete Form 5471. You may have to file Form 5471 for a foreign corporation; this tool does not prepare it. Cite: [i1040sb] p. 2, Part II. Ordinary Dividends, TIP, "You may have to file Form 5471 if, in 2025, you were an officer or director of a foreign corporation", "You may also have to file Form 5471 if, in 2025, you owned 10% or more of the total (a) value of a foreign corporation’s stock, or (b) combined voting power of all classes of a foreign corporation’s stock with voting rights" (TY2025; printed April 23, 2025; sha256 b92f31ec)
- Expr: `{"from":"sb.ordinary_dividends_if_dividends","op":"copy"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.partIII`

- **Authored helper label:** Complete Part III for interest/dividends over $1,500 or foreign account/trust
- **Encoded (Bool):** (line 4 > $1,500 or line 6 > $1,500 or helper "Schedule B line 7a (a financial interest in or signature authority over a foreign financial account), when you or your spouse had a foreign account, other foreign financial asset, foreign trust or foreign corporation, or any of these in a U.S. territory; false otherwise" = true or helper "Schedule B line 8 (a foreign trust distribution, or the grantor of or a transferor to a foreign trust), when you or your spouse had a foreign account, other foreign financial asset, foreign trust or foreign corporation; false otherwise" = true)
- Expr: `{"any":[{"gt":["sb.line4",{"const":150000}],"op":"test"},{"gt":["sb.line6",{"const":150000}],"op":"test"},{"eq":["sb.line7a_if_foreign",{"const":true}],"op":"test"},{"eq":["sb.line8_if_foreign",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sb] pp. 1–3, interest, dividends and foreign accounts/trusts (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.form5471`

- **Authored helper label:** In 2025, were you (or, on a joint return, your spouse) an officer, director, managing director or manager of a foreign corporation or other company, whatever it is called, that is organized outside the 50 states and the District of Columbia, including in Puerto Rico, Guam or another US territory, or did you (or, on a joint return, your spouse) own 10% or more of the total value of a foreign corporation's stock, or of the combined voting power of all classes of a foreign corporation's stock with voting rights, counting shares owned by your spouse, children, grandchildren or parents and by partnerships, corporations, trusts or estates you have an interest in, and shares any of you could acquire through options or warrants?
- **Encoded (Bool):** Input — In 2025, were you (or, on a joint return, your spouse) an officer, director, managing director or manager of a foreign corporation or other company, whatever it is called, that is organized outside the 50 states and the District of Columbia, including in Puerto Rico, Guam or another US territory, or did you (or, on a joint return, your spouse) own 10% or more of the total value of a foreign corporation's stock, or of the combined voting power of all classes of a foreign corporation's stock with voting rights, counting shares owned by your spouse, children, grandchildren or parents and by partnerships, corporations, trusts or estates you have an interest in, and shares any of you could acquire through options or warrants?
- Expr: `{"op":"input","source":"In 2025, were you (or, on a joint return, your spouse) an officer, director, managing director or manager of a foreign corporation or other company, whatever it is called, that is organized outside the 50 states and the District of Columbia, including in Puerto Rico, Guam or another US territory, or did you (or, on a joint return, your spouse) own 10% or more of the total value of a foreign corporation's stock, or of the combined voting power of all classes of a foreign corporation's stock with voting rights, counting shares owned by your spouse, children, grandchildren or parents and by partnerships, corporations, trusts or estates you have an interest in, and shares any of you could acquire through options or warrants?"}`
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
- **Encoded (NonNegDollars):** Choose — [div helper "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?" = true → helper "Total ordinary dividends, Form 1099-DIV box 1a"] [div helper "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.any",{"const":true}],"op":"test"},"then":"sb.ordinary_dividends"},{"guard":{"eq":["div.any",{"const":false}],"op":"test"},"then":"sb.zero"}],"op":"choose"}`
- Cite: [i1040sb] p. 2, Line 5, "Report on line 5 all of your ordinary dividends. This amount should be shown in box 1a of your Forms 1099-DIV or substitute statements" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.nominee_if_income`

- **Authored helper label:** Interest or ordinary dividends received as a nominee, when taxable interest, ordinary dividends or capital gain distributions are above zero; false otherwise
- **Encoded (Bool):** Choose — [helper "Taxable interest, ordinary dividends or capital gain distributions are above zero" = true → helper "Interest or ordinary dividends received as a nominee"] [helper "Taxable interest, ordinary dividends or capital gain distributions are above zero" = false → helper "No special treatment without interest, ordinary dividends or capital gain distributions"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.has_income",{"const":true}],"op":"test"},"then":"sb.nominee"},{"guard":{"eq":["sb.has_income",{"const":false}],"op":"test"},"then":"sb.no"}],"op":"choose"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.bonds_any_if_income`

- **Authored helper label:** Bonds or notes owned directly, savings bonds cashed, or interest on a loan or a sale, when taxable interest, ordinary dividends or capital gain distributions are above zero; false otherwise
- **Encoded (Bool):** Choose — [helper "Taxable interest, ordinary dividends or capital gain distributions are above zero" = true → helper "Bonds or notes owned directly, U.S. savings bonds cashed, or interest on a loan made or a property sold"] [helper "Taxable interest, ordinary dividends or capital gain distributions are above zero" = false → helper "No special treatment without interest, ordinary dividends or capital gain distributions"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.has_income",{"const":true}],"op":"test"},"then":"sb.bonds_any"},{"guard":{"eq":["sb.has_income",{"const":false}],"op":"test"},"then":"sb.no"}],"op":"choose"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.bond_special_if_bonds`

- **Authored helper label:** Special treatment of bond or loan interest, when bonds or notes were owned directly, savings bonds cashed, or interest received on a loan or a sale; false otherwise
- **Encoded (Bool):** Choose — [helper "Bonds or notes owned directly, savings bonds cashed, or interest on a loan or a sale, when taxable interest, ordinary dividends or capital gain distributions are above zero; false otherwise" = true → helper "Original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, or other special treatment"] [helper "Bonds or notes owned directly, savings bonds cashed, or interest on a loan or a sale, when taxable interest, ordinary dividends or capital gain distributions are above zero; false otherwise" = false → helper "No special treatment without interest, ordinary dividends or capital gain distributions"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.bonds_any_if_income",{"const":true}],"op":"test"},"then":"sb.bond_special"},{"guard":{"eq":["sb.bonds_any_if_income",{"const":false}],"op":"test"},"then":"sb.no"}],"op":"choose"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.unsupported_if_income`

- **Authored helper label:** Schedule B special treatment (any nominee income or special treatment of bond or loan interest, each asked only when taxable interest, ordinary dividends or capital gain distributions are above zero, so false otherwise)
- **Encoded (Bool):** Enter the amount from helper "Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment, accrued market discount, a contingent payment debt instrument, seller-financed mortgage interest, a savings bond interest exclusion, or other special treatment".
- Expr: `{"from":"sb.unsupported","op":"copy"}`
- Cite: [i1040sb] p. 1, General Instructions, "Use Schedule B (Form 1040) if any of the following applies", "You received interest from a seller-financed mortgage", "You have accrued interest from a bond", "You are reporting original issue discount (OID) of less than the amount shown on Form 1099-OID", "You are reporting interest income of less than the amount shown on a Form 1099 due to amortizable bond premium", "You are claiming the exclusion of interest from series EE or I U.S. savings bonds issued after 1989", "You received interest or ordinary dividends as a nominee" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.fbar_required_if_foreign`

- **Authored helper label:** FinCEN Form 114 (FBAR) required, when you or your spouse had a foreign account, other foreign financial asset, foreign trust or foreign corporation; false otherwise
- **Encoded (Bool):** Choose — [helper "A foreign account, another foreign financial asset, a connection to a foreign trust or a role in a foreign corporation, or any of these in a U.S. territory, at any time in 2025" = true → helper "Are you (or, on a joint return, your spouse) required to file FinCEN Form 114 (FBAR)? Determine under its instructions; this tool does not determine foreign account values or exceptions."] [helper "A foreign account, another foreign financial asset, a connection to a foreign trust or a role in a foreign corporation, or any of these in a U.S. territory, at any time in 2025" = false → helper "No foreign account, asset, trust or corporation question without a foreign connection"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.foreign_any",{"const":true}],"op":"test"},"then":"sb.fbar_required"},{"guard":{"eq":["sb.foreign_any",{"const":false}],"op":"test"},"then":"sb.foreign_no"}],"op":"choose"}`
- Cite: [i1040sb] p. 3, Line 7a—Question 2, "See FinCEN Form 114 and its instructions at FINCEN.gov to determine whether you must file the form"; fincen114 p. 4, Who Must File an FBAR, "A United States person that has a financial interest in or signature authority over foreign financial accounts must file an FBAR if the aggregate value of the foreign financial accounts exceeds $10,000 at any time during the calendar year" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.form8938_if_foreign`

- **Authored helper label:** Form 8938 required, when you or your spouse had a foreign account, other foreign financial asset, foreign trust or foreign corporation; false otherwise
- **Encoded (Bool):** Choose — [helper "A foreign account, another foreign financial asset, a connection to a foreign trust or a role in a foreign corporation, or any of these in a U.S. territory, at any time in 2025" = true → helper "Are you (or, on a joint return, your spouse) required to file Form 8938 for specified foreign financial assets?"] [helper "A foreign account, another foreign financial asset, a connection to a foreign trust or a role in a foreign corporation, or any of these in a U.S. territory, at any time in 2025" = false → helper "No foreign account, asset, trust or corporation question without a foreign connection"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.foreign_any",{"const":true}],"op":"test"},"then":"sb.form8938"},{"guard":{"eq":["sb.foreign_any",{"const":false}],"op":"test"},"then":"sb.foreign_no"}],"op":"choose"}`
- Cite: [i1040sb] p. 2, Part III. Foreign Accounts and Trusts, "Statement of Specified Foreign Financial Assets, with your income tax return"; i8938 pp. 7–8, Specified Foreign Financial Assets (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.line7a_if_foreign`

- **Authored helper label:** Schedule B line 7a (a financial interest in or signature authority over a foreign financial account), when you or your spouse had a foreign account, other foreign financial asset, foreign trust or foreign corporation, or any of these in a U.S. territory; false otherwise
- **Encoded (Bool):** Choose — [helper "A foreign account, another foreign financial asset, a connection to a foreign trust or a role in a foreign corporation, or any of these in a U.S. territory, at any time in 2025" = true → line 7a] [helper "A foreign account, another foreign financial asset, a connection to a foreign trust or a role in a foreign corporation, or any of these in a U.S. territory, at any time in 2025" = false → helper "No foreign account, asset, trust or corporation question without a foreign connection"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.foreign_any",{"const":true}],"op":"test"},"then":"sb.line7a"},{"guard":{"eq":["sb.foreign_any",{"const":false}],"op":"test"},"then":"sb.foreign_no"}],"op":"choose"}`
- Cite: [i1040sb] p. 2, Line 7a—Question 1, "Check the “Yes” box if at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.line8_if_foreign`

- **Authored helper label:** Schedule B line 8 (a foreign trust distribution, or the grantor of or a transferor to a foreign trust), when you or your spouse had a foreign account, other foreign financial asset, foreign trust or foreign corporation; false otherwise
- **Encoded (Bool):** Choose — [helper "A connection to a foreign trust, or an account, investment, company or trust in a U.S. territory" = true → line 8] [helper "A connection to a foreign trust, or an account, investment, company or trust in a U.S. territory" = false → helper "No foreign account, asset, trust or corporation question without a foreign connection"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.foreign_trust_any",{"const":true}],"op":"test"},"then":"sb.line8"},{"guard":{"eq":["sb.foreign_trust_any",{"const":false}],"op":"test"},"then":"sb.foreign_no"}],"op":"choose"}`
- Cite: [i1040sb] p. 3, Line 8, "If you received a distribution from a foreign trust, you must provide additional information", "If you were the grantor of, or transferor to, a foreign trust that existed during 2025, you may have to file Form 3520" (TY2025; printed April 23, 2025; sha256 b92f31ec)

## (helper) — `sb.form5471_if_foreign`

- **Authored helper label:** Form 5471 officer, director or 10% shareholder of a foreign corporation, when you or your spouse had a foreign account, other foreign financial asset, foreign trust or foreign corporation; false otherwise
- **Encoded (Bool):** Choose — [helper "A role in or 10% of a foreign company, or an account, investment, company or trust in a U.S. territory" = true → helper "In 2025, were you (or, on a joint return, your spouse) an officer, director, managing director or manager of a foreign corporation or other company, whatever it is called, that is organized outside the 50 states and the District of Columbia, including in Puerto Rico, Guam or another US territory, or did you (or, on a joint return, your spouse) own 10% or more of the total value of a foreign corporation's stock, or of the combined voting power of all classes of a foreign corporation's stock with voting rights, counting shares owned by your spouse, children, grandchildren or parents and by partnerships, corporations, trusts or estates you have an interest in, and shares any of you could acquire through options or warrants?"] [helper "A role in or 10% of a foreign company, or an account, investment, company or trust in a U.S. territory" = false → helper "No foreign account, asset, trust or corporation question without a foreign connection"]
- Expr: `{"alternatives":[{"guard":{"eq":["sb.foreign_company_any",{"const":true}],"op":"test"},"then":"sb.form5471"},{"guard":{"eq":["sb.foreign_company_any",{"const":false}],"op":"test"},"then":"sb.foreign_no"}],"op":"choose"}`
- Cite: [i1040sb] p. 2, Part II. Ordinary Dividends, TIP, "You may have to file Form 5471 if, in 2025, you were an officer or director of a foreign corporation" (TY2025; printed April 23, 2025; sha256 b92f31ec)
