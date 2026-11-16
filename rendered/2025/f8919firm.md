# Form 8919, lines 1 to 5 — one row per firm that treated this person as an independent contractor

- Document: `f8919firm` (form, tax year 2025)
- Collection: keyed entries within person; [f8919] p. 2, Lines 1 through 5, "Complete a separate line for each firm", "The line 6 amount on that Form 8919 should be the combined totals of all lines 1 through 5 of all your Forms 8919" (2025; created 2025-10-22 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 84102b12)
- Note: One entry per firm. Columns (c) (the reason code) and (f) (the wages) are asked; columns (a), (b), (d) and (e) identify the firm and the IRS letter and change no amount.

## 1(c) — `f8919firm.reason`

- **IRS:** Enter reason code from above
- **Encoded (Enum(contractor_reason)):** Input — Which reason code applies to this firm: a (you filed Form SS-8 and received a determination letter stating that you are an employee of this firm), c (you received other correspondence from the IRS stating that you are an employee), g (you filed Form SS-8 with the IRS and have not received a reply, or none of the reason codes applies but you believe you should have been treated as an employee and file Form SS-8 on or before the date you file your return) or h (you received a Form W-2 and a Form 1099-MISC or 1099-NEC from this firm for 2025, and the amount on the Form 1099-MISC or 1099-NEC should have been included as wages on the Form W-2)?
- Expr: `{"op":"input","source":"Which reason code applies to this firm: a (you filed Form SS-8 and received a determination letter stating that you are an employee of this firm), c (you received other correspondence from the IRS stating that you are an employee), g (you filed Form SS-8 with the IRS and have not received a reply, or none of the reason codes applies but you believe you should have been treated as an employee and file Form SS-8 on or before the date you file your return) or h (you received a Form W-2 and a Form 1099-MISC or 1099-NEC from this firm for 2025, and the amount on the Form 1099-MISC or 1099-NEC should have been included as wages on the Form W-2)?"}`
- Cite: [f8919] p. 1, Reason codes, "For each firm listed below, enter in column (c) the applicable reason code for filing this form", "If none of the reason codes apply to you, but you believe you should have been treated as an employee, enter reason code G and file", "I filed Form SS-8 and received a determination letter stating that I am an employee of this firm", "I received other correspondence from the IRS stating that I am an employee", "I filed Form SS-8 with the IRS and haven’t received a reply", "I received a Form W-2 and a Form 1099-MISC and/or 1099-NEC from this firm for 2025" (2025; created 2025-10-22 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 84102b12)

## 1(f) — `f8919firm.wages`

- **IRS:** Total wages received with no social security or Medicare tax withholding and not reported on Form W-2
- **Encoded (NonNegDollars):** Input — Total wages you received from this firm in 2025 with no social security or Medicare tax withholding and not reported on a Form W-2
- Expr: `{"op":"input","source":"Total wages you received from this firm in 2025 with no social security or Medicare tax withholding and not reported on a Form W-2"}`
- Cite: [f8919] p. 1, Total wages, "(f) Total wages", "withholding and not", "reported on Form W-2" (2025; created 2025-10-22 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 84102b12)
