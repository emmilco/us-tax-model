# Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer

- Document: `tipjob` (form, tax year 2025)
- Collection: keyed entries within person; [i1040gi] p. 104, Schedule 1-A, line 4c, and the Qualified Tips From More Than One Employer Worksheet (one row per employer) (2025; printed date 2026-02-25; sha256 482e9c48)
- Note: One entry per employer from which you received tips as an employee that you are deducting. Tips reported on Form 4137 (column (c)) are refused with Form 4137, so column (d) is the column (b) amount.

## (helper) — `tipjob.one`

- **Authored helper label:** One employer
- **Encoded (Count):** Enter 1 (ss.one).
- Expr: `{"op":"param","ref":"ss.one"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4c, "with respect to employment with more than one employer" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `tipjob.qualified`

- **Authored helper label:** Were all the tips you are counting from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024, paid in cash (including by check, card or app), voluntarily, without negotiation and in an amount the customer decided, and not for a service that is a crime under applicable law?
- **Encoded (Bool):** Input — Were all the tips you are counting from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024 (IRS.gov/TippedOccupations), paid in cash (including by check, card or app), voluntarily, without negotiation and in an amount the customer decided, and not for a service that is a crime under applicable law?
- Expr: `{"op":"input","source":"Were all the tips you are counting from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024 (IRS.gov/TippedOccupations), paid in cash (including by check, card or app), voluntarily, without negotiation and in an amount the customer decided, and not for a service that is a crime under applicable law?"}`
- Cite: [i1040gi] pp. 101-103, Schedule 1-A, Qualified Tips, Cash tips, "Paid voluntarily, not subject to negotiation, and determined by the customer/payor," "Amounts received that are not qualified tips" and "Occupations that customarily and regularly received tips"; "Do not include tips received in occupations that are not included on this list" (2025; printed date 2026-02-25; sha256 482e9c48)

## 1(b) — `tipjob.amount`

- **IRS:** Amount of qualified tips reported by this employer on Form W-2, or reported by you to this employer on Form(s) 4070
- **Encoded (NonNegDollars):** Input — Qualified tips from this employer, taken from one of these (your choice): Form W-2 box 7 (social security tips); the total of the tips you reported to this employer on Forms 4070 or a similar monthly report (which may be more accurate if Form W-2 box 1 or box 5 is more than $176,100); or an amount of tips your employer reported in Form W-2 box 14 or on a separate statement
- **Refusal:** when tipjob.mixed is true, cannot complete Qualified tips from an employer where some tips were not qualified tips. Splitting one employer's reported tips between qualified and nonqualified tips is outside this tool. Cite: [i1040gi] p. 103, "If you received tips as an employee in more than one occupation for the same employer, only those tips that were received in an occupation on the list ... are considered qualified tips. Do not include tips received in occupations that are not included on this list in line 4a, 4b, or 4c" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"input","source":"Qualified tips from this employer, taken from one of these (your choice): Form W-2 box 7 (social security tips); the total of the tips you reported to this employer on Forms 4070 or a similar monthly report (which may be more accurate if Form W-2 box 1 or box 5 is more than $176,100); or an amount of tips your employer reported in Form W-2 box 14 or on a separate statement"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (b); pp. 103-104, methods 1 to 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `tipjob.mixed`

- **Authored helper label:** Some of this employer's tips are not qualified tips
- **Encoded (Bool):** helper "Were all the tips you are counting from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024, paid in cash (including by check, card or app), voluntarily, without negotiation and in an amount the customer decided, and not for a service that is a crime under applicable law?" = false
- Expr: `{"eq":["tipjob.qualified",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 103, Schedule 1-A, "Determining the amount of qualified tips received by an employee for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## 1(c) — `tipjob.col_c`

- **IRS:** Qualified tips reported on Form 4137, column 1(c), for this employer
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when s2.other is true, cannot complete Form 4137 (Social Security and Medicare Tax on Unreported Tip Income). Tips reported on Form 4137 are outside this tool. Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (c), and p. 103, method 4 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (c) (2025; printed date 2026-02-25; sha256 482e9c48)

## 1(d) — `tipjob.col_d`

- **IRS:** Enter the greater of column (b) or column (c)
- **Encoded (NonNegDollars):** Enter the larger of line 1(b) or line 1(c).
- Expr: `{"of":["tipjob.amount","tipjob.col_c"],"op":"larger_of"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (d) (2025; printed date 2026-02-25; sha256 482e9c48)
