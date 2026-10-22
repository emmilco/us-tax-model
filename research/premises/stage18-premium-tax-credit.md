> **Status: draft for the owner (2026-10-22).** Written by a read-only research agent from the archived
> sources in `sources/2025/`, before the stage it maps; its decision batch is a draft and nothing in it is
> decided. Every claim carries a locator and is testimony until checked again at authoring. Spot-checked by the integrating session: Form 8962 Worksheet 2 drops the decimals and enters 401 above 400% (i8962, Line 5), so no existing atom figures line 5. Follow-up recorded as TASKS.md T-049.

# Premise map: the premium tax credit (spec 2.4 roadmap item 4; Form 8962 with Form 1095-A)

Read-only research for a later stage, written from the archived snapshots in `sources/2025/` and the repository as it stands (commit `fcd2c26`, with Stage 15 being authored elsewhere and assumed to land first). Page N of a document is the N-th form-feed chunk of `<id>.cols.txt`. Locators follow the project style `doc p. N, heading, "quote"`. Everything here is testimony for the stage's authoring, not a verified encoding; section 10 separates what was checked from what was inferred.

## 0. How the project encodes what this stage touches (checked against the files)

- `s3.line9` (forms/2025/s3.yaml) is today an `input` whose source reads 'Net premium tax credit from Form 8962 (supplied subtotal; preparation outside Stage 2)'. It feeds `s3.line15`, which `f1040.line31` copies. Nothing refuses it: a filer with a net PTC can type the figure in.
- Schedule 2 has no line 1a. `s2.line2` and `s2.line3` are `copy s2.zero`, each refused when `s2.amt` or `s2.other` is true; `f1040.line17` copies `s2.line3`; `f1040.line18` sums lines 16 and 17. The question `s2.other` names 'repayment of excess advance premium tax credit' among the Schedule 2 sources it refuses.
- The coverage category `ptc` (tools/coverage/categories.json) has the single gate `s2.other`, the label 'Premium tax credit or advance payments (Form 8962 is not prepared; line 9 is a supplied subtotal)', IRS cells soi-23in27aca columns 3 (total PTC) and 5 (APTC), combined by `max`, and the microdata variable `premium_tax_credit`.
- Already refused elsewhere, and inherited by this stage: a filer or spouse whom someone can claim (`sa.dependent`, refused at the standard deduction, sa.yaml line 842); married filing separately (spec 2.2); Form 2555, 4563 or excluded Puerto Rico income (`sa.excluded_income`); Form 8814 (`scope.other_line16`, scope.yaml line 42); the self-employed health insurance deduction for a Marketplace plan with APTC or a claimed PTC (`sc.hi_screen`, sc.yaml, citing i1040gi p. 95).
- Atoms (spec 4.2; engine/src/check.ts): `sum` and `smaller_of`/`larger_of` take money only; `sum_over` takes a money or Count field; `test` compares Count with Count; `choose` branches must be money; `keyed_lookup` keys are enum or Count, its cell may be a Rate (between 0 and 1), Count, enum or money, and it is unknown when no row has the keys; `rate_lookup` requires a money key and a Rate line; `multiply_rate` rounds half-up to the cent (eval.ts; `amb.2025.multiplication_subcent`); `round` takes a unit and half_up/up/down; `prorate` rounds its ratio half-up and keeps it in [0, 1]. There is no division of money by money yielding a Count, no Count addition, and no Count minimum.
- Collections: `person` (role taxpayer or spouse; `household.persons` counts them), `dependent` (with `dependent.claimed`, the Bool "Your dependent"), and return-level collections such as `retirement`. A line may read its own entry and return-level lines (spec 4.4).
- Fixtures: 648 cases set `"s3.line9": 0`, one sets it to 123; 617 set `s2.other` false and 10 true (counted with grep over fixtures/2025/).

## 1. Scope

### 1.1 What the stage retires, and its measured share

reports/2025/filer_coverage.md (2023 counts): 'Premium tax credit or advance payments (Form 8962 is not prepared; line 9 is a supplied subtotal)', group `premium_tax_credit`, 6.0% of returns, 9,604,913 IRS returns (the APTC count, the larger of the two cells), 5.0% in the microdata before raking. The group's step is 4: '84.8% (+4.9)' after Steps 1 to 3, '+3.5' if covered alone now.

The SOI table behind it (soi-23in27aca, row "All returns", read with pandas) splits the 2023 returns: total PTC 8,860,422; APTC 9,604,913; net PTC (Schedule 3 line 9) 2,410,248; excess APTC repayment (Schedule 2 line 1a) 5,577,776. So about three in five Form 8962 filers repay something, and today each of them is refused through `s2.other`; the 2.4 million with a net PTC are not refused but get no preparation (they type the subtotal), which the estimator counts as not covered.

None of the sub-situations below (allocation, marriage, unpaid months, QSEHRA, lawful presence) has an IRS count or a microdata variable; their shares are unmeasured.

### 1.2 Recommended scope

Compute now:

- Form 8962 Parts I to III for single, head of household, qualifying surviving spouse and married filing jointly returns, with one or more Forms 1095-A, the annual (line 11) and monthly (lines 12 to 23) calculations, and the line 10 choice between them derived from the entries.
- Household income from the filer's AGI, tax-exempt interest and nontaxable social security, plus the modified AGI of claimed dependents who are required to file (per-dependent inputs).
- The three federal poverty tables and families of any size up to a cap (section 7), Table 2, and the Table 5 repayment limitation.
- Household income below 100% of the federal poverty line, both as not an applicable taxpayer (full repayment up to the Table 5 limit) and with the APTC exception (one question).
- A filer-supplied applicable SLCSP premium where column B is blank, zero or wrong (the Marketplace tool's figure), per month.
- The cross-form edits: Schedule 3 line 9 computed, Schedule 2 lines 1a, 1z and 3 computed, the `s2.other` question narrowed, the coverage category rewired.

Refuse in the first build (section 6 gives the reasons): Part IV allocations (all four situations), the year-of-marriage cases (Part V and the column B marriage rule), anyone enrolled who is not lawfully present, a QSEHRA or individual coverage HRA, APTC for someone in no tax family, months with unpaid premiums, tax family size zero, and a family above the size cap. Inherited refusals stay (MFS, claimable filer, Form 2555, Form 8814, self-employed health insurance with the PTC).

Reasoning: the computed set is the plain reconciliation every Form 8962 filer goes through; the refused set either needs another taxpayer's agreement or figures (allocation), a Pub. 974 worksheet family of its own (Part V, lawful presence, QSEHRA, self-employed health insurance), or facts the form does not carry (unpaid premiums). This follows the Stage 15 pattern in sources/2025/PREMISES.md: refuse rare and hard situations, compute common ones, record readings.

## 2. Sources

Archived and used (revisions as the manifest records them; not inspected beyond that):

| id | What | Manifest revision |
|---|---|---|
| f8962 | Form 8962 (2025), 3 pages; footer "Form 8962 (2025) Created 3/25/25" | "2025" |
| i8962 | Instructions for Form 8962 (2025), 25 pages, dated Oct 1, 2025 (p. 1) | "2025" |
| p974 | Pub. 974 (2025), 69 pages, dated Jan 12, 2026 (p. 1) | "2025" |
| f1095a | Form 1095-A (2025), with the Instructions for Recipient (p. 3) | "2025" |
| i1095a | Instructions for Form 1095-A (2025), for the Marketplaces | "2025" |
| i1040gi | Form 1040 instructions: Chart B and C (pp. 10 to 11), Schedule 2 line 1a (p. 111), Schedule 3 line 9 (p. 117), Schedule 1 line 17 exception (p. 95) | as archived |
| f1040s2, f1040s3 | Schedule 2 lines 1a, 1z, 3; Schedule 3 line 9 | as archived |
| plaw-119-21 | P.L. 119-21, sections 71301 to 71305 (pp. 251 to 255) | as archived |
| soi-23in27aca | SOI Table 2.7, Affordable Care Act items | as archived |

Not archived, and needed or useful (no fetch was made):

- 26 U.S.C. 36B (the statute; would settle Q7 on dependents required to file, and the applicable percentage schedule): https://www.govinfo.gov/content/pkg/USCODE-2024-title26/pdf/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartC-sec36B.pdf (or the uscode.house.gov page for 26 USC 36B).
- Rev. Proc. 2024-35 (the 2025 required contribution percentage, 9.02%, and the 2025 repayment limitation amounts): https://www.irs.gov/pub/irs-drop/rp-24-35.pdf. It would give an independent second printing of Table 5 and the 9.02% figure.
- The 2024 HHS poverty guidelines (89 FR 2961, January 17, 2024), the only independent printing of Tables 1-1 to 1-3: https://www.federalregister.gov/documents/2024/01/17/2024-00796/annual-update-of-the-hhs-poverty-guidelines
- The About Form 8962 page, for post-release corrections: https://www.irs.gov/forms-pubs/about-form-8962
- Not needed if the refusals in 1.2 stand: Form 1095-B, 1095-C, Pub. 3865, Form 8857.

## 3. Line map

### 3.1 Form 1095-A as the input record (new return-level collection, one entry per Form 1095-A)

f1095a p. 3, Instructions for Recipient: "If you or your family members enrolled at the Marketplace in more than one qualified health plan policy, you will receive a Form 1095-A for each policy." So the entry is the form (one policy), not a person. The collection is return-level with no parent, like `retirement`, because a policy can cover the taxpayer, the spouse and dependents together, and Form 8962 is one per return.

| Box (f1095a p. 2) | Use | Proposed line on the entry |
|---|---|---|
| Part I lines 1 to 15 (identifiers, recipient, spouse, policy dates, address) | None in the arithmetic. Line 2 (policy number) is used only by Part IV, which is refused. Line 1 "Marketplace identifier" (f1095a p. 2) names the state (i1095a p. 1, "Line 1. Enter the Marketplace state name or abbreviation"), relevant to the column B rule below. | none, or an interview label only (no strings in the model) |
| Part II lines 16 to 20 (covered individuals) | Who is covered; needed only to detect a policy shared with another tax family (refused) | a screen, not data |
| Part III lines 21 to 32, "A. Monthly enrollment premiums" | Form 8962 column (a) | 12 inputs `f1095a.a_jan` ... `f1095a.a_dec`, NonNegDollars |
| Part III lines 21 to 32, "B. Monthly second lowest cost silver plan (SLCSP) premium" | Form 8962 column (b) | 12 inputs `f1095a.b_jan` ... `b_dec`, each 'the amount in column B, or the correct applicable SLCSP premium if column B is blank, zero or wrong' (proposed wording; see 4.6) |
| Part III lines 21 to 32, "C. Monthly advance payment of premium tax credit" | Form 8962 column (f) | 12 inputs `f1095a.c_jan` ... `c_dec` |
| Line 33, "Annual Totals" (f1095a p. 2) | Form 8962 line 11 columns (a), (b), (f) | 3 computed lines, `sum` of the twelve months (i1095a p. 2: "Total the amounts on lines 21 through 32 and enter on line 33.") |
| (none printed) | Whether this form's column B is the one counted (section 4.5) | new Bool input `f1095a.b_counted` |
| (none printed) | Line 10 tests: premium and SLCSP the same in all 12 months, coverage in all 12 | 2 to 3 computed Bool lines on the entry (all-equal tests on the twelve inputs, and column A above zero each month) |

Help text the interview needs (testimony, not lines): i8962 p. 2, "Do not use the information on the Form 1095-A with the" ... VOID box; "use the information on the Form 1095-A with the" ... CORRECTED box (both quoted from f1095a p. 3 more cleanly: "Don’t use the information on this or the previously received Form 1095-A to figure your premium tax credit on Form 8962" and "use the information on this Form 1095-A to figure the premium tax credit and reconcile any advance credit payments on Form 8962"); f1095a p. 3, "If you or your family members were enrolled in a Marketplace catastrophic health plan or separate dental policy, you aren’t entitled to take a premium tax credit for this coverage when you file your return, even if you received a Form 1095-A for this coverage."

### 3.2 Form 8962 (2025), new return-level form `f8962`

Printed text is from f8962 p. 1 unless noted.

**Line A.** f8962 p. 1, "You cannot take the PTC if your filing status is married filing separately unless you qualify for an exception. See instructions. If you qualify, check the box". MFS is refused (spec 2.2), so no line; the refusal already covers Exception 2 (i8962 p. 7, "Check the box on line A, above Part I of Form 8962, if you are filing as married filing separately").

**Part I, Annual and Monthly Contribution Amount**

| Line | Printed text (f8962 p. 1) | Computes | Existing supply | New inputs / notes |
|---|---|---|---|---|
| 1 | f8962: "Tax family size. Enter your tax family size. See instructions" | Count: you, your spouse if joint, and dependents claimed | `household.persons` (Count of person entries); a new Count `sum_over dependent dependent.one where dependent.claimed` | Adding the two Counts has no atom (section 5.3, Q1). Filer and spouse are never claimable here (`sa.dependent` refuses), so the "Someone can claim you" exclusion (i8962 p. 8) never applies. |
| 2a | f8962: "Modified AGI. Enter your modified AGI. See instructions" | Worksheet 1-1 line 5 (below) | `f1040.line11a`, `f1040.line2a`, `f1040.line6a`, `f1040.line6b` | none |
| 2b | "Enter the total of your dependents’ modified AGI. See instructions" | Worksheet 1-2 line 5: `sum_over dependent` of a per-dependent MAGI, filtered by claimed and required to file | none | per dependent: `dependent.files_required` (Bool) and `dependent.magi` (Dollars, may be negative), or the four Worksheet 1-2 components (Q6) |
| 3 | f8962: "Household income. Add the amounts on lines 2a and 2b. See instructions" | `sum` then `larger_of` with zero (two lines): i8962 p. 8, Line 3, "Combine them even if one or both of them are negative. If the total is less than zero, enter -0- on line 3." | n/a | n/a |
| 4 | "Federal poverty line. Enter the federal poverty line amount from Table 1-1, 1-2, or 1-3. See instructions. Check the appropriate box for the federal poverty table used." | `keyed_lookup` in a pinned table keyed by (fpl_state, family size) | line 1 | new return-level Enum input `f8962.fpl_state` ∈ {contiguous, alaska, hawaii} with the 'higher table' rule as help (4.3) |
| 5 | "Household income as a percentage of federal poverty line (see instructions)" | Worksheet 2: Count, 401 if line 3 exceeds 4 × line 4, else the truncated percentage | lines 3, 4 | no atom computes it (section 5.3, Q2) |
| 6 | "Reserved for future use" | nothing | n/a | n/a |
| 7 | "Applicable figure. Using your line 5 percentage, locate your" applicable figure "on the table in the instructions" | Rate from Table 2 keyed by line 5 | line 5 | `keyed_lookup` on a Count key (5.3) |
| 8a | "Annual contribution amount. Multiply line 3 by line 7. Round to nearest whole dollar amount" | `multiply_rate` then `round` (unit 100, half_up) | lines 3, 7 | double rounding, Q3 |
| 8b | "Monthly contribution amount. Divide line 8a by 12. Round to nearest whole dollar amount" | `multiply_rate` by a 1/12 parameter, then `round` to the dollar | line 8a | exact (see 4.4) |

Worksheet 1-1, Taxpayer's Modified AGI (i8962 p. 8):

| WS line | Printed text | Encoding |
|---|---|---|
| 1 | i8962: "Enter your AGI* from Form 1040, 1040-SR, or 1040-NR, line 11a" | `copy f1040.line11a` |
| 2 | i8962: "Enter any tax-exempt interest from Form 1040, 1040-SR, or 1040-NR, line 2a" | `copy f1040.line2a` (which already includes 1099-DIV box 12, T-029) |
| 3 | "Enter any amounts from Form 2555, lines 45 and 50" | zero, refused when `sa.excluded_income` (the same gate as s8812 lines 2a to 2c and s1a; it also catches Form 4563 and Puerto Rico income, which Worksheet 1-1 does not name; over-refusal, Q11) |
| 4 | i8962: "Form 1040 or 1040-SR filers: If line 6a is more than line 6b, subtract line 6b from line 6a and enter the result" | `subtract_floor0 f1040.line6a f1040.line6b` |
| 5 | "Add lines 1 through 4. Enter here and on Form 8962, line 2a" | `sum` |
| footnote | "If you are filing Form 8814 and the amount on Form 8814, line 4, is more than $1,350, you must enter certain amounts from that form on Worksheet 1-2." | inherited refusal (`scope.other_line16`) |

Worksheet 1-2, Dependents' Combined Modified AGI (i8962 p. 8): lines 1 to 5 mirror Worksheet 1-1 for the dependents ("Enter the AGI* for your dependents from Form 1040, 1040-SR, or 1040-NR, line 11a"; "For each dependent filing Form 1040 or 1040-SR: If line 6a is more than line 6b, subtract line 6b from line 6a and enter the result"), with the footnote "Only include your dependents who are required to file an income tax return because their income meets the income tax return filing threshold." The dependents' returns are not in this tool, so each dependent's figures are inputs.

Worksheet 2, Household Income as a Percentage of the Federal Poverty Line (i8962 p. 9):

| WS line | Printed text | Encoding |
|---|---|---|
| 1 | i8962: "Enter the amount from line 3 of Form 8962" | `copy f8962.line3` |
| 2 | i8962: "Enter the amount from line 4 of Form 8962" | `copy f8962.line4` |
| 3 | "Multiply the amount on line 2 by 4.0" | `multiply_count` by a Count parameter 4 (exact) |
| 4 | "Is the amount on line 1 more than the amount on line 3?" Yes: "Enter 401 here and on line 5 of Form 8962." No: "Divide the amount on line 1 above by the amount on line 2 above. Do not round; instead, multiply this number by 100 (to express it as a percentage) and then drop any numbers after the decimal point." with the examples "for 0.9984, enter the result as 99; for 1.8565, enter the result as 185; and for 3.997, enter the result as 399." | the new atom of Q2, or not expressible |

**Part II, Premium Tax Credit Claim and Reconciliation of Advance Payment of Premium Tax Credit**

| Line | Printed text | Computes | Notes |
|---|---|---|---|
| 9 | "Are you allocating policy amounts with another taxpayer or do you want to use the alternative calculation for year of marriage? See instructions." | Bool; Yes leads to Parts IV and V | Refused when Yes (section 6). Encoded as a screen gate, derived from two questions (shared policy; married in 2025 with pre-marriage coverage). |
| 10 | f8962: "See the instructions to determine if you can use line 11 or must complete lines 12 through 23." | Bool, derived: every counted 1095-A has 12 months of coverage, the same column A each month and the same column B each month (i8962 p. 14, "Full-year coverage with no changes on Form 1095-A, Part III, column A or B.") | Not an election: "Check “Yes” and continue to line 11 if all of the following apply" (i8962 p. 14). Derived from the entries, not asked (Q5). |
| 11 (a) | f8962: "(a) Annual enrollment premiums (Form(s) 1095-A, line 33A)" | `sum_over f1095a line33a` | i8962 p. 15, Column (a), "If you have more than one Form 1095-A, add the amounts together and enter the total on Form 8962, line 11, column (a)." |
| 11 (b) | f8962: "(b) Annual applicable SLCSP premium (Form(s) 1095-A, line 33B)" | `sum_over f1095a line33b where b_counted` | the one-form-per-state rule, 4.5 |
| 11 (c) | "(c) Annual contribution amount (line 8a)" | `copy f8962.line8a` | |
| 11 (d) | "(d) Annual maximum premium assistance (subtract (c) from (b); if zero or less, enter -0-)" | `subtract_floor0` | |
| 11 (e) | f8962: "(e) Annual PTC allowed ... (smaller of (a) or (d))" | `smaller_of` | QSEHRA note (i8962 p. 16, Column (e)) refused |
| 11 (f) | f8962: "(f) Annual advance ... payment of PTC (Form(s) ... 1095-A, line 33C)" | `sum_over f1095a line33c` | all forms added, i8962 p. 16, Column (f) |
| 12 to 23 (a) | f8962: "(a) Monthly enrollment ... premiums (Form(s) ... 1095-A, lines 21–32, ... column A)" | per month `sum_over f1095a a_<month>` | i8962 p. 16, Column (a), "If you have more than one Form 1095-A affecting a particular month, add the amounts together for that month and enter the total on the appropriate line on Form 8962, column (a)." |
| 12 to 23 (b) | f8962: "(b) Monthly applicable ... SLCSP premium ... 21–32, column B)" | per month `sum_over f1095a b_<month> where b_counted` | i8962 p. 16, Column (b), "Enter the amount from column B of only one Form 1095-A—do not add the amounts from each form." |
| 12 to 23 (c) | "(c) Monthly contribution amount (amount from line 8b or alternative marriage monthly calculation)" | `copy f8962.line8b` per month (the alternative is refused) | i8962 p. 17, "If columns (a) and (b) of any of lines 12 through 23 are blank, leave column (c) of the corresponding line blank." Blank versus zero changes no total (Q9). |
| 12 to 23 (d) | f8962: "(d) Monthly maximum ... premium assistance ... (subtract (c) from (b); if ... zero or less, enter -0-)" | `subtract_floor0` per month | |
| 12 to 23 (e) | f8962: "(e) Monthly PTC allowed ... (smaller of (a) or (d))" | `smaller_of` per month | |
| 12 to 23 (f) | f8962: "(f) Monthly advance ... payment of PTC (Form(s) ... column C)" | per month `sum_over f1095a c_<month>` | i8962 p. 17, "If you have more than one Form 1095-A affecting a particular month, add the amounts together for that month and enter the total on the appropriate line on Form 8962, column (f)." |
| 24 | "Total PTC. Enter the amount from line 11, column (e), or add lines 12 through 23, column (e), and enter the total here" | `choose` on line 10: line 11(e), or the `sum` of the twelve (e); zero when not an applicable taxpayer (4.2) | |
| 25 | "Advance payment of PTC. Enter the amount from line 11, column (f), or add lines 12 through 23, column (f), and enter the total here" | `choose` on line 10 | |
| 26 | "Net PTC. If line 24 is greater than line 25, subtract line 25 from line 24. Enter the difference here and on Schedule 3 (Form 1040), line 9. If line 24 equals line 25, enter -0-. Stop here." | `subtract_floor0 line24 line25` | "blank" when line 25 exceeds 24 is shown as zero (Q9) |

Lines 12 to 23 are 12 months × 6 columns = 72 lines, spelled out (no loops). Per month the column (c) copy could be dropped and column (d) could read line 8b directly; keeping (c) keeps the printed form on the values sheet.

**Part III, Repayment of Excess Advance Payment of the Premium Tax Credit**

| Line | Printed text | Computes |
|---|---|---|
| 27 | "Excess advance payment of PTC. If line 25 is greater than line 24, subtract line 24 from line 25. Enter the difference here" | `subtract_floor0 line25 line24` |
| 28 | "Repayment limitation (see instructions)" | Table 5 by line 5 and filing status: a `choose` over Count tests on line 5 (< 200, < 300, < 400, otherwise) returning status-keyed parameters, and line 27 itself in the last branch ("leave line 28 blank"), so line 29 is line 27 |
| 29 | "Excess advance PTC repayment. Enter the smaller of line 27 or line 28 here and on Schedule 2 (Form 1040), line 1a" | `smaller_of` |

**Parts IV and V** (f8962 p. 2: lines 30 to 34, "Allocation of Policy Amounts"; lines 35 and 36, "Alternative Calculation for Year of Marriage"): refused in the recommended scope; their map is in section 6 (R1, R2) so the refusal can be cited and so a later stage can start from it.

### 3.3 Schedules 2 and 3

| Line | Printed text | Change |
|---|---|---|
| s2 1a (new `s2.line1a`) | f1040s2 p. 1, "Excess advance premium tax credit repayment. Attach Form 8962" | `copy f8962.line29`; i1040gi p. 111, Line 1a, "If the advance credit payments were more than the premium tax credit you can claim, the amount you must repay will be shown on Form 8962, line 29. Enter that amount, if any, on line 1a." |
| s2 1z (new `s2.line1z`) | f1040s2 p. 1, "Add lines 1a through 1y" | `sum` of 1a (1b to 1y stay under `s2.other`) |
| s2 3 (`s2.line3`, changed) | f1040s2 p. 1, "Add lines 1z and 2. Enter here and on Form 1040, 1040-SR, or 1040-NR, line 17" | from `copy s2.zero` to `sum s2.line1z s2.line2`; its refusals stay |
| s3 9 (`s3.line9`, changed) | f1040s3 p. 1, "Net premium tax credit. Attach Form 8962" | from `input` to `copy f8962.line26`; i1040gi p. 117, "If the premium tax credit you can claim exceeds your advance credit payments, your net premium tax credit will be shown on Form 8962, line 26. Enter that amount, if any, on line 9." |

## 4. Rules

### 4.1 Who must file, who can take the PTC

- Must file: i8962 p. 3, Who Must File, "You are taking the PTC." / "APTC was paid for you or another individual in your tax family." / "APTC was paid for an individual you told the Marketplace would be in your tax family and neither you nor anyone else included that individual in a tax family." The third is refused (R8).
- Can take: i8962 p. 3, Who Can Take the PTC, conditions (1) to (3): an individual "was enrolled in one or more qualified health plans offered through the Marketplace on the first day of the month", "That individual was not eligible for MEC for the month, other than coverage in the individual market", premiums paid; "2. No one can claim you as a dependent for the year."; and "3. You are an applicable taxpayer for 2025."
- Tax family: i8962 p. 3, Terms You May Need To Know, "You, if you file a tax return for the year and you can’t be claimed as a dependent on someone else’s 2025 tax return." / "Your spouse if filing jointly and your spouse can’t be claimed as a dependent on someone else’s 2025 tax return." / "Your dependents whom you claim on your 2025 tax return."
- Coverage family (the people whose coverage counts in a month): i8962 p. 4, Coverage family, "Your coverage family includes only individuals in your tax family who are enrolled in a qualified health plan and are not eligible for MEC (other than coverage in the individual market)." The coverage family is reflected only through column B (the SLCSP for the coverage family), so the model carries no per-individual monthly data (4.6).
- Monthly credit amount: i8962 p. 4, "Your credit amount for each month is the lesser of:" the enrollment premiums, or "The amount of the monthly applicable second lowest cost silver plan (SLCSP) premium (described later) less your monthly contribution amount (described later)."
- First day of the month: i8962 p. 4, "To qualify for a monthly credit amount, at least one individual in your tax family must be enrolled in a qualified health plan on the first day of that month." The 1095-A already reflects this (i1095a p. 2, Column B: "who are enrolled in the coverage on the first day of the month").
- Qualified health plan: i8962 p. 5, "Catastrophic health plans and stand-alone dental plans purchased through the Marketplace, and all plans purchased through the Small Business Health Options Program (SHOP), are not qualified health plans for purposes of the PTC." Interview help: do not enter such a Form 1095-A.

### 4.2 Applicable taxpayer and household income below 100% of the line

- i8962 p. 6, Applicable taxpayer, "Generally, you are an applicable taxpayer if your household income for 2025 (described earlier) is at least 100% of the federal poverty line for your family size".
- Below 100%: i8962 p. 9, Estimated household income at least 100% of the federal poverty line, all of "No one can claim you as a dependent for the year." / "You or an individual in your tax family enrolled in a qualified health plan through a Marketplace." / "The Marketplace estimated at the time of enrollment that your household income would be at least 100% of the federal poverty line for your family size for 2025." / "APTC was paid for the coverage of 1 or more months during 2025." / "You otherwise qualify as an applicable taxpayer (except for the federal poverty line percentage)." The caution adds: "No APTC was paid for your or your family’s coverage; or" (then not met).
- The lawfully present alien branch (i8962 pp. 9 to 10, Alien lawfully present in the United States): "The enrolled individual is lawfully present in the United States and is not eligible for Medicaid because of immigration status." Recommended refused with the other immigration-status cases (R3).
- Not applicable: i8962 p. 10, "you are not an applicable taxpayer and you are not eligible to take the PTC. If APTC was paid for any individuals in your tax family, skip lines 7 and 8, and go to line 9. However, if no APTC was paid for any individuals in your tax family, stop; do not complete Form 8962." Encoding: a Bool `f8962.applicable` (line 5 at least 100, or the exception answered yes); when false, line 24 is zero, lines 7 and 8 are not used, and line 28 comes from the "Less than 200" row. The instructions do not say "enter -0- on line 24" for this case (they do for MFS, i8962 p. 16); the zero follows from "not eligible to take the PTC" (Q4).

### 4.3 Federal poverty line (line 4)

- i8962 p. 8, Line 4: "(For 2025, the 2024 federal poverty lines are used for this purpose and are shown below.)" and "If you moved during 2025 and you lived in Alaska and/or Hawaii, or you are filing jointly and you and your spouse lived in different states, use the table with the higher dollar amounts for your family size." Alaska's amounts are higher than Hawaii's at every size (below), so the rule reduces to: Alaska if anyone on the return lived there in 2025, else Hawaii if anyone did, else the 48-state table. One Enum question with this help.
- Table 1-1 (i8962 p. 8), sizes 1 to 8: $15,060 $20,440 $25,820 $31,200 $36,580 $41,960 $47,340 $52,720; footnote "If your family size was more than 8 people, add $5,380 for each additional person." with the example "Enter the result of $68,860 on Form 8962, line 4." (size 11).
- Table 1-2, Alaska (i8962 p. 9): $18,810 $25,540 $32,270 $39,000 $45,730 $52,460 $59,190 $65,920; "add $6,730 for each additional person"; example "Enter the result of $86,110 on Form 8962, line 4."
- Table 1-3, Hawaii (i8962 p. 9): $17,310 $23,500 $29,690 $35,880 $42,070 $48,260 $54,450 $60,640; "add $6,190 for each additional person"; example "Enter the result of $79,210 on Form 8962, line 4."
- Checked arithmetic: in each table every printed size from 2 to 8 is the size-1 amount plus the footnote increment times (size − 1); the footnote examples equal the size-8 amount plus three increments. So a pinned table generated past 8 by the footnote reproduces every printed number.

### 4.4 Table 2, the contribution amount and rounding

- i8962 p. 10, Line 7, "Enter on line 7 the decimal number from Table 2 that applies to the amount you entered on line 5." Table 2 (i8962 p. 11) has 252 printed rows: "less than 150" (0.0000), each whole number from 150 to 399, and the row 400 or more (0.0850); its tip, "If the amount on line 5 is 150 or less, your applicable figure is 0.0000. If the amount on line 5 is 400 or more, your applicable figure is 0.0850."
- Checked: every printed row equals 0 at 150 or less; (p − 150) × 0.0004 from 150 to 300; and 0.06 + (p − 300) × 0.00025 rounded half-up to four places from 300 to 399 (for example 301 prints 0.0603, 302 prints 0.0605). This is a check on the extraction, not a substitute for the printed table.
- Line 8a: i8962 p. 12, "Multiply line 3 by line 7 and enter the result on line 8a, rounded to the nearest whole dollar amount." Line 8b: "Divide line 8a by 12.0 and enter the result on line 8b, rounded to the nearest whole dollar amount."
- Line 8b via `multiply_rate` (1/12, half-up to the cent) then `round` to the dollar is exact: line 8a is whole dollars, so line 8a ÷ 12 has a fractional dollar part that is a multiple of 1/12, which is never within half a cent below one half. Line 8a is not exact the same way (Q3).

### 4.5 Several Forms 1095-A

- Columns (a) and (f) add across forms, month by month (quotes in 3.2).
- Column (b): i8962 p. 15, Column (b), "If individuals in your coverage family enrolled in more than one policy in the same state, you will receive a Form 1095-A for each policy. The Marketplace should have entered the same SLCSP premium, which applies to all members of your coverage family, on each Form 1095-A." Then "Enter the amount from column B of only one Form 1095-A—do not add the amounts from each form." and, for different states, "add together the amounts from column B of the Forms 1095-A from each state and enter the total on Form 8962, line 11, column (b)." The same rules for months on i8962 p. 16. Encoding: the per-entry Bool `b_counted` ('Count this form's column B: yes for one form per state', proposed wording), summed with a `sum_over ... where`. The checker cannot see states (no strings); a test that at least one counted form exists when any form has column B above zero is possible.
- Marriage in 2025 overrides the one-form rule for pre-marriage months (i8962 p. 17, Marriage in 2025, "add together the amounts from column B of the Forms 1095-A for each month before the first full month of marriage and enter the total."). Refused with R2.
- Pediatric dental: i1095a p. 2, Column A, the dental share goes "in the amount in column A on only one Form 1095-A", so adding column A across forms does not double count.

### 4.6 A column B that is blank, zero or wrong

- i8962 p. 14, Missing or incorrect SLCSP premium on Form 1095-A: "If either of these two situations applies to you, or if you have reason to believe the Marketplace reported the wrong applicable SLCSP premium, you must determine the correct applicable SLCSP premium for every month." The two situations are no APTC paid ("the SLCSP premium reported in Part III, lines 21 through 32, column B, of Form 1095-A may be wrong, left blank, or reported as -0-") and an unreported change in circumstances (list on i8962 p. 15: newborn, partial-year member, MEC eligibility gained or lost, a tax family different from the enrollment, a death, a move).
- p974 p. 27, Applicable SLCSP premium tools, "Only the Marketplaces are able to provide applicable SLCSP premiums." and "If you enrolled through the federally facilitated Marketplace, you will find the tool at HealthCare.gov/Tax-Tool/."
- So the correct figure cannot be computed here; it is an input. Recommended: each month's column B input is the corrected figure when one is needed, with help quoting these passages; line 10 then follows from the corrected figures, as i8962 p. 15 says: "If your correct applicable SLCSP premium is not the same for all 12 months, check “No” and continue to lines 12 through 23." (the quote stops before the inner quotation marks in the checker's terms; see section 10).

### 4.7 Months with unpaid premiums

- i8962 p. 4, Enrollment premiums: "You are generally not allowed a monthly credit amount for the month if any part of that month’s enrollment premium for which you are responsible has not been paid by the due date of your tax return (not including extensions)", with three exceptions (first grace month, premium payment threshold, a state emergency order) and the reduction "must be reduced by any portion of the premium that is unpaid as of the unextended due date".
- i8962 p. 16, Column (a): when column A shows zero but the premiums were paid by the due date, "enter the enrollment premiums for the month on the appropriate line on Form 8962, column (a), even if your Form 1095-A shows -0- as the enrollment premium for the month."
- f1095a p. 3, Column C: "If this is the only column in Part III that is filled in with an amount other than zero for a month, it means your policy was terminated by your insurance company due to nonpayment of premiums, and you aren’t entitled to take the premium tax credit for that month". With columns A and B at zero for that month, the arithmetic already gives (e) zero and counts (f).

### 4.8 Household income: whose MAGI counts

- i8962 p. 4, Household income: "household income is the modified adjusted gross income (modified AGI) of you and your spouse (if filing a joint return) (see Line 2a, later) plus the modified AGI of each individual whom you claim as a dependent and who is required to file an income tax return because their income meets the income tax return filing threshold (see Line 2b, later)." and "Household income does not include the modified AGI of those individuals whom you claim as dependents and who are filing a 2025 return only to claim a refund of withheld income tax or estimated tax."
- i8962 p. 8, Line 2b, "Do not include the modified AGI of dependents who are filing a tax return only to claim a refund of tax withheld or estimated tax."
- Modified AGI: i8962 p. 4, "modified AGI is the AGI on your tax return plus certain income that is not subject to tax (foreign earned income, tax-exempt interest, and the portion of social security benefits that is not taxable)."
- So the dependents counted are those claimed on this return (`dependent.claimed`) and required to file by their income (i1040gi p. 10, Chart B—For Children and Other Dependents: for a single dependent, "Your unearned income was over $1,350." / "Your earned income was over $15,750."). The tool has no dependent's own return, so "required to file" is a per-dependent question with Chart B as help, and that dependent's MAGI is an input. Not counted: dependents enrolled or not, a person in the coverage family who is not claimed (they are in no household income here), and dependents filing only for a refund.
- Whether a dependent required to file only under Chart C (for example "You had net earnings from self-employment of at least $400." i1040gi p. 11) counts is Q7.

### 4.9 The repayment limitation, and P.L. 119-21

- i8962 p. 18, Line 28, "The excess APTC you must repay may be limited to the amounts in Table 5." and "If your entry on Form 8962, line 5, is 400 or more, there is no repayment limitation. You must repay the amount shown on line 27. Leave line 28 blank and enter the amount from line 27 on line 29."
- Table 5 (i8962 p. 18, read against the layout text): "Less than 200": Single $375, any other filing status $750; "At least 200 but less than 300": $975 / $1,950; "At least 300 but less than 400": $1,625 / $3,250; "400 or more": "leave line 28 blank". Second printing of the same six amounts: p974 p. 52, Worksheet X, "enter $750 ($375 if your filing status is single)", "or $1,950 ($975 if your filing status is single)", "or $3,250 ($1,625 if your filing status is single)".
- Line 28 special cases: "If you are self-employed and are claiming the self-employed health insurance deduction, see Self-Employed Health Insurance Deduction and PTC in Pub. 974 for the amount to enter on line 28." (inherited refusal) and "the repayment limitation does not apply to APTC paid for individuals who are not lawfully present" (R3).
- P.L. 119-21 for 2025: plaw-119-21 p. 254, SEC. 71305, "Section 36B(f)(2) is amended by striking subparagraph (B)." (the limitation); p. 255, its effective date, "The amendments made by this section shall apply to taxable years beginning after December 31, 2025." So Table 5 still applies for 2025 and is gone for 2026. The other PTC sections also start after 2025: section 71302 (striking 36B(c)(1)(B), the lawfully present alien rule below 100%) applies "to taxable years beginning after December 31, 2025" (p. 253); 71304 "with respect to plan years beginning after December 31, 2025" (p. 254); 71303 "to taxable years beginning after December 31, 2027" (p. 254); 71301 "to taxable years beginning after December 31, 2026" (p. 252). None changes the 2025 form; the 2026 year-diff will meet Table 5's removal, the alien rule's removal and (from the expiring 2021 and 2022 enhancements, not in the archived text) a different Table 2.
- The 2025 text also states the 400% rule: i8962 p. 1, "For tax year 2025, taxpayers with household income that exceeds 400% of the federal poverty line for their family size may be allowed a PTC."

### 4.10 Shared policies, Part IV (for the refusal citation and a later stage)

- When to allocate: i8962 p. 12, Allocating policy amounts, "1. The policy covered at least one individual in your tax family and at least one individual in another tax family; and" a Form 1095-A that misstates the members. Examples given: divorce, MFS, an ex-spouse enrolling a child.
- Table 3 (i8962 p. 13): Step 1 divorced or legally separated in 2025 (Situation 1); Step 2 married at year end, separate returns, including Exceptions 1 and 2 (Situation 2); Step 3 no APTC (Situation 3); otherwise Situation 4.
- Situation 1 (i8962 p. 18): any agreed percentage, the same for all three amounts, else 50%. Situation 2 (p. 19): 50% of premiums and APTC, SLCSP not allocated (the filer's own SLCSP instead). Situation 3 (p. 20): premiums in proportion to each family's SLCSP. Situation 4 (pp. 20 to 21): any agreed percentage per month, else "the number of individuals enrolled by one taxpayer who are included in the tax family of the other taxpayer for the tax year divided by the total number of individuals enrolled in the same policy".
- Lines 30 to 33 columns (e) to (g): i8962 p. 22, "Enter your allocation percentage as a decimal rounded to two places (for example, for 40%, enter “0.40”)." (quoted up to the inner marks); more than three tax families: i8962 p. 12, "see the rules in Pub. 974 under Allocation of Policy Amounts Among Three or More Taxpayers."
- Encodable later: per entry, a Rate for each of (e), (f), (g) and a start and stop month (Count), with each monthly amount a `choose` between the amount and `multiply_rate(amount, pct)` by a Count test on the month. About 36 more lines per entry; no new atom.

### 4.11 Year of marriage, Part V (for the refusal citation)

- Table 4 (i8962 p. 13): five questions, "Were you and your spouse each unmarried on January 1, 2025?", "Were you married on December 31, 2025?", "Are you filing a joint return with your spouse for 2025?", "Was anyone in your tax family enrolled in a qualified health plan before your first full month of marriage?", "Was APTC paid for anyone in your tax family during 2025?"; then Worksheet 3 (p. 14), whose line 14 asks "Is line 13, column (e), less than line 13, column (f)?"
- Part V itself defers to Pub. 974: i8962 p. 22, "Line 35. Complete line 35, columns (a) through (d), as indicated in Pub. 974 under Alternative Calculation for Year of Marriage." (Pub. 974 Worksheets I to V, pp. 39 to 46.) Optional: i8962 p. 22, "Electing the alternative calculation is optional but may reduce the amount of excess APTC you must repay."

### 4.12 Other eligibility rules that become screens

- Individual coverage HRA: i8962 p. 3, "If you were covered under an individual coverage HRA for 2025, you are not allowed a PTC for your 2025 Marketplace health insurance." (opt-out and affordability go to Pub. 974).
- QSEHRA: i8962 p. 1, "If the QSEHRA is affordable for a month, no PTC is allowed for the month." and the unaffordable case reduces the monthly PTC (Pub. 974 Worksheets N and Q, pp. 16 to 18).
- Employer coverage: i8962 p. 5, affordable if the employee's share "is not more than 9.02% of your household income"; the Marketplace determination protects the filer who "gave accurate information about the availability of employer coverage to the Marketplace". This decides the coverage family, hence column B; it reaches the model only through the corrected column B of 4.6.
- Not lawfully present: i8962 p. 6, "Individuals who are not lawfully present in the United States are not eligible for the PTC for their coverage in a qualified health plan through a Marketplace." with its own line-by-line override and Pub. 974 Worksheets A and B (pp. 20 to 26).
- Retroactive enrollment after an appeal: i8962 p. 3, "the portion of the enrollment premium for which you are responsible must be paid on or before the 120th day following the date of the appeals decision." Folded into the unpaid-premium screen.

## 5. Ordering and every existing line that changes

### 5.1 Where the PTC sits

- Inputs to Form 8962: `f1040.line11a` (AGI), `f1040.line2a`, `f1040.line6a`, `f1040.line6b`, `household.persons`, `dependent.claimed`, `f1040.status`. AGI does not depend on Form 8962 in this tool because the one feedback path the text names, the self-employed health insurance deduction (p974 p. 47, "Because the amount of the self-employed health insurance deduction may affect the amount of the PTC, and the amount of the PTC may affect the amount of the deduction"), is refused by `sc.hi_screen`. No cycle.
- Outputs: line 26 to Schedule 3 line 9 (Part II, refundable; with no ordering against other credits), line 29 to Schedule 2 line 1a, then line 1z, line 3, Form 1040 line 17, line 18.
- The repayment raises line 18, which is the tax every nonrefundable credit limit starts from. That is as the forms say (Schedule 2 Part I is "Tax"), and it moves credits: - `s8812` Credit Limit Worksheet A line 1 (`from: f1040.line18`, s8812.yaml line 238): more room for the nonrefundable CTC/ODC, so less of the child tax credit is refundable (ACTC). Correct per the worksheet, but every 8812 fixture with a repayment changes. - Stage 15's Credit Limit Worksheets (Form 2441 line 10, Form 8880 line 11, Form 5695 lines 14 and 31) all start from line 18 (PREMISES.md, Stage 15 maps). Same effect. - `f1040.line22` (subtract line 21 from line 18) and through it lines 24, 37. - Not affected: the foreign tax credit simple-path limit reads `f1040.line16` (ftc.yaml line 151); the EIC; Form 8959 and 8960.

### 5.2 Lines that change, by id

| Id | Today | After |
|---|---|---|
| `s3.line9` | input, supplied subtotal | `copy f8962.line26`; drop its interview question (interview/questions-2025.yaml line 180; profiles 2025.yaml and stage4-2025.yaml list it) |
| `s2.line1a`, `s2.line1z` | absent | new (3.3) |
| `s2.line3` | `copy s2.zero` | `sum s2.line1z s2.line2` (refusals kept) |
| `s2.other` | question naming 'repayment of excess advance premium tax credit' | the phrase removed; the same text is repeated in its `source` |
| `f1040.line17`, `f1040.line18` | unchanged expressions | now carry the repayment (fixtures change where APTC is present) |
| `s8812` CLW A line 1 and the Stage 15 CLWs | unchanged expressions | values change (5.1) |
| `amb.2025.dc_rate_nonpositive_agi` | its reason says the readings cannot differ because line 18 is zero when AGI is zero or less, 'the alternative minimum tax and the repayment of excess advance premium tax credit being refused' | no longer true: with AGI ≤ 0 a filer can owe a Table 5 repayment ($375 or $750), so line 18 > 0 and the Form 2441 credit limit is positive. The reasoning must be revisited (the reading may stand; its reason does not). Check the Stage 15 saver's credit table for the same argument. |
| `tools/coverage/categories.json` `ptc` | gates `["s2.other"]` | the new Form 8962 refusal gates; `s2.other` no longer stands for it. The label changes. |
| `dependent` | no own-income lines beyond `dependent.gross_income` | two new per-dependent inputs (3.2, line 2b) |
| fixtures | 648 with `s3.line9` 0, one with 123 | `s3.line9` becomes computed: the input key is dropped from every case, and the case with 123 needs a Form 1095-A in its place or removal |

### 5.3 What the atoms can and cannot carry

| Table or step | Keyed by | Fits | Notes |
|---|---|---|---|
| Tables 1-1 to 1-3 (line 4) | state (enum) and family size (Count) | `keyed_lookup`, cell money | rows for sizes 1 to 8 as printed, extended by the footnote to a cap (7.2); keyed_lookup is unknown past the last row, so the cap needs a refusal, or a `choose` with the footnote arithmetic for sizes above 8 (`multiply_count` of the increment by line 1, less 8 increments, plus the size-8 amount), if an unknown helper line off the chosen branch is acceptable (Q1b) |
| Line 1 itself | the sum of two Counts | none | `sum` takes money only (check.ts); see Q1 |
| Line 5 (Worksheet 2) | a ratio of two money lines, truncated to a whole percentage and capped at 401 | **no atom** | `prorate` rounds half-up, clamps to 1 and returns money; `multiply_rate`'s rate is a line or parameter, not a quotient. This is the ratio no atom expresses (Q2). |
| Table 2 (line 7) | line 5, a Count | `keyed_lookup` with a Count key and Rate cells (402 rows: 0 to 401, the rows below 150 all 0.0000, 400 and 401 0.0850), or `rate_lookup` if it accepted a Count key (252 bands exactly as printed: open below at 149, one band per whole number, open above at 399) | `rate_lookup` as specified needs a money key, so it cannot carry Table 2 as it stands. keyed_lookup can, once line 5 exists. |
| Table 5 (line 28) | line 5 (Count) and filing status, returning money | neither lookup: `rate_lookup` returns rates, `table_lookup` keys on money, `keyed_lookup` would need 402 × 5 rows | a `choose` over Count tests (`lt` 200, 300, 400) with status-keyed money parameters; no new atom |
| Line 8b | division by 12 | `multiply_rate` by a 1/12 parameter, then `round` | exact (4.4) |
| Line 8a | Rate × money to the dollar | `multiply_rate` then `round` | double rounding (Q3) |
| Line 10 | equality of twelve inputs | `test` with `all` of `eq` | per entry; then `sum_over` a Count of failing entries, compared with zero |

## 6. Refuse or compute

| # | Situation | Why it is hard | Recommendation |
|---|---|---|---|
| R1 | Part IV allocation, any situation (divorce in 2025, a policy shared with another tax family, Exception 1 married living apart sharing a policy with the spouse, no-APTC shared policy) | Needs the other taxpayer's agreement or their SLCSP figures; Situation 3 needs both families' SLCSPs; three or more families go to Pub. 974; per-month ranges | Refuse via a screen (proposed wording): 'Did any Form 1095-A policy cover someone in your tax family and someone not in it (for example a former spouse, or a child someone else claims)?' Later stage: compute Situations 1, 2 (with Exception 1) and 4 with entered percentages and month ranges (4.10). |
| R2 | Married during 2025 with Marketplace coverage before the first full month of marriage | Part V and Pub. 974 Worksheets I to V; the pre-marriage column B rule | Refuse when married in 2025, joint, and anyone enrolled before the first full month of marriage. Alternative: compute without the election and notify that it may lower the repayment (it is optional), refusing only the column B marriage rule. Owner decision. |
| R3 | Anyone enrolled who is not lawfully present; the lawfully present alien below 100% exception | Own line overrides (i8962 p. 6) and Pub. 974 Worksheets A and B | Refuse (one screen). |
| R4 | QSEHRA (W-2 box 12 code FF) or individual coverage HRA, offered or covered | Affordability tests and Worksheets N and Q in Pub. 974 | Refuse (one screen). |
| R5 | A month whose premium was not fully paid by the due date (grace periods, payment thresholds, unpaid portions, retroactive enrollment after an appeal), or column A shows zero but the premium was paid | Facts the 1095-A does not show; reduced premiums | Refuse (one screen). Alternative: compute the 'paid by the due date though column A shows zero' case by letting the filer enter the premium. |
| R6 | Column B blank, zero or wrong (no APTC; unreported change; MEC eligibility for part of the year) | The correct SLCSP is a Marketplace lookup | Compute: the filer enters the corrected figure per month, with the tool's citation and a notice. Alternative: refuse whenever a correction is needed (simpler, but refuses most PTC claims without APTC). |
| R7 | Household income below 100% | Applicability, exceptions | Compute both branches (4.2) with one question for the Marketplace-estimate exception; refuse the alien branch (R3). |
| R8 | APTC for an individual in no tax family; a tax family size of zero | Allocation with family size zero (p974 p. 27) | Refuse (one screen; family size zero is caught by line 1 = 0 when any 1095-A is present). |
| R9 | Married filing separately (repay half, Exception 2) | MFS is refused across the tool | Inherited. |
| R10 | Filer or spouse can be claimed as a dependent | i8962 p. 3 tip: the claimer files Form 8962 | Inherited (`sa.dependent`). |
| R11 | Form 2555 amounts (Worksheet 1-1 line 3; also a dependent's) | Form 2555 not prepared | Inherited for the filer (`sa.excluded_income`); add 'a counted dependent files Form 2555' to the dependent MAGI help or a screen. |
| R12 | Form 8814 (the footnote to Worksheet 1-1) | Form 8814 refused | Inherited (`scope.other_line16`). |
| R13 | Self-employed health insurance on a Marketplace plan with APTC or the PTC (the circular calculation of p974 pp. 47 to 63) | Iterative or simplified two-pass method; Worksheets P, W, X, Y, Z | Inherited (`sc.hi_screen`). Later: the Simplified Calculation Method is a fixed two-pass computation (Step 2 then Step 4), expressible as two parameterized instances of Form 8962 (spec 4.4), not an iteration; the Iterative method is not expressible. |
| R14 | Family size above the table cap | keyed_lookup has no row | Refuse above the cap (7.2), or the footnote arithmetic (Q1b). |
| R15 | More than one Form 1095-A in the same state with different column B, or none counted | The one-form rule assumes equal column B | Compute with `b_counted`; screen or refuse when two counted forms show different column B in a month (Q8). |
| R16 | Catastrophic, stand-alone dental or SHOP policies | Not qualified health plans | Not data: help text says not to enter them. |
| R17 | VOID and CORRECTED forms | Which form to use | Help text only. |
| R18 | Moved between the 48 states and Alaska or Hawaii; spouses in different states | Which poverty table | Compute: the Enum question with the higher-table rule (4.3). |
| R19 | The dependent filing requirement and dependent MAGI | No dependent return in the tool | Compute from per-dependent inputs (Q6, Q7). |

## 7. Parameters and tables for 2025 (values in cents)

### 7.1 `params/2025.yaml`

| Proposed id | Type | Value | Locator |
|---|---|---|---|
| `ptc.repay_200` | NonNegDollars by status | single 37500; hoh, mfj, qss, mfs 75000 | i8962 p. 18, Table 5, "Less than 200"; second printing p974 p. 52, Worksheet X |
| `ptc.repay_300` | NonNegDollars by status | single 97500; others 195000 | i8962 p. 18, Table 5, "At least 200 but less than 300"; p974 p. 52 |
| `ptc.repay_400` | NonNegDollars by status | single 162500; others 325000 | i8962 p. 18, Table 5, "At least 300 but less than 400"; p974 p. 52 |
| `ptc.pct_200`, `ptc.pct_300`, `ptc.pct_400` | Count | 200, 300, 400 | i8962 p. 18, Table 5 rows |
| `ptc.pct_100` | Count | 100 | i8962 p. 6, Applicable taxpayer, "at least 100% of the federal poverty line" |
| `ptc.fpl_multiple` | Count | 4 | i8962 p. 9, Worksheet 2 line 3, "Multiply the amount on line 2 by 4.0" |
| `ptc.over_400` | Count | 401 | i8962 p. 9, Worksheet 2 line 4, "Enter 401 here and on line 5 of Form 8962." (only if the new atom takes it as an operand) |
| `ptc.twelfth` | Rate | {num: 1, den: 12} | i8962 p. 12, Line 8b, "Divide line 8a by 12.0" |
| `ptc.fpl_size_cap` | Count | for example 20 (owner's choice) | the footnotes to Tables 1-1 to 1-3 |

Not parameters, but help text: the 9.02% employer affordability figure (i8962 p. 5); Chart B amounts (i1040gi p. 10).

MFS values exist only because every status-keyed parameter carries all five; MFS is refused. The "any other filing status" column is the text's.

### 7.2 Pinned tables (`tables/2025/`)

- `fpl.yaml`, kind `keyed`, keys (Enum `fpl_state`, Count family size), cell NonNegDollars. Rows for sizes 1 to 8 transcribed from i8962 pp. 8 to 9 (cents: contiguous 1506000, 2044000, 2582000, 3120000, 3658000, 4196000, 4734000, 5272000; Alaska 1881000, 2554000, 3227000, 3900000, 4573000, 5246000, 5919000, 6592000; Hawaii 1731000, 2350000, 2969000, 3588000, 4207000, 4826000, 5445000, 6064000), and sizes 9 to the cap generated by the footnotes (increments 538000, 673000, 619000), with a check against the size-11 examples (6886000, 8611000, 7921000). Single printing in the archive: none of these amounts appears in p974 or elsewhere in i1040gi (searched for "15,060" and "5,380"); the HHS notice is the independent source (section 2).
- `applicable_figure.yaml`, kind `keyed`, key Count (line 5), cell Rate, 402 rows (0 to 401), written by an extractor from the i8962 p. 11 layout text and checked against the derivation in 4.4. Or 252 bands if `rate_lookup` takes a Count key. Single printing in the archive (p974 has no copy: "0.0850" does not occur in it).
- The `enums` entry `fpl_state` with values contiguous, alaska, hawaii (f8962 p. 1, line 4 boxes "Alaska", "Hawaii", "Other 48 states and DC").

## 8. Open questions

- **Q1. Line 1 as one Count.** Family size is the Count of person entries plus the Count of claimed dependents, from two collections. `sum` accepts only money in the checker, and no other atom adds Counts. Options: let `sum` accept Count operands when all are Count (a checker and rendering change, no new atom; Lean's sum is already over integers); or a pinned keyed table from (persons, dependents) to family size (a workaround the renderer would show as a lookup). **Q1b.** If line 4 uses `keyed_lookup` only to size 8 and a `choose` for larger families, the keyed helper is unknown for families above 8 while not on the chosen branch; spec 4.1 allows a return only when 'every reachable line is known', and spec 4.4 says every line of every entry is evaluated. Is such a helper acceptable, or must the table run to the cap?
- **Q2. Line 5.** No atom computes 'divide, multiply by 100, drop any numbers after the decimal point', nor the 401 for more than 400%. A new atom is needed (spec 4.2 additions require a justification, a rendering template, a Lean definition and lemmas). A candidate: `percent_floor` with a part (money, zero or more), a whole (money, above zero) and a cap (Count): the result is cap + 1 if part is more than whole × cap ÷ 100, else floor(100 × part ÷ whole); lemmas: monotone in the part, at most cap + 1, equal to the floor below the cap. Without the cap clause, line 5 would print 400 instead of 401 when household income is between 400% and 401% of the line, and above 401% would print the true percentage; Tables 2 and 5 give the same results either way, but the printed line 5 would differ from Worksheet 2.
- **Q3. Line 8a double rounding.** `multiply_rate` rounds half-up to the cent, and `round` then rounds to the dollar. When household income is in cents, the exact product can have a fractional dollar part in [0.495, 0.5), which this rounds up and a single rounding would round down (a $1 difference in line 8a, then possibly in 8b and the PTC). Options: accept it and record it in the register (it arises only with cents in line 3); give `multiply_rate` an optional rounding unit; or apply `round` to line 3 first (the instructions do not say so).
- **Q4. Line 24 when not an applicable taxpayer.** The MFS text says to enter -0- on line 24; the below-100% text says only "not eligible to take the PTC" and "skip lines 7 and 8". Reading: line 24 is zero and line 25 is the APTC; record it.
- **Q5. Line 10 derived or asked.** Derive it from the entries (twelve months of column A above zero and equal, column B equal, on every counted form), or ask the filer? The instructions make it a test, not a choice. Is a month with column A above zero a fair stand-in for "enrolled ... for all 12 months"? A policy could start mid-month (no premium for that month) or cover only some members.
- **Q6. Dependents' MAGI shape.** One per-dependent MAGI input (the Worksheet 1-2 total for that dependent) or four (AGI, tax-exempt interest, Form 2555 amounts, social security less taxable part)? The worksheet sums each line across dependents first; the total is the same.
- **Q7. Which filing requirement.** The text counts a dependent "required to file an income tax return because their income meets the income tax return filing threshold". Does a dependent required to file only under Chart C (self-employment earnings of $400 or more, or APTC paid for their own coverage) count? The literal text says no; the statute (36B(d)(2)(A)(ii), not archived) speaks of a requirement to file under section 6012. Recommendation: the literal reading (Chart B only), recorded; archive 26 USC 36B to confirm.
- **Q8. Several forms, one state.** The one-form rule says the Marketplace "should have entered the same SLCSP premium" on each. What if the counted and uncounted forms show different column B in a month? Refuse, or let the filer choose the counted one, which is then the corrected figure?
- **Q9. Blank and zero.** Several lines are "blank" in the text (column (c) for a month with no coverage, line 26 when there is excess APTC, line 28 at 400 or more). The values sheet shows zero (or, for line 28, line 27). Record that the totals are the same, and render blank where the form says so?
- **Q10. Cents on Form 1095-A.** i8962 p. 22, Entering amounts from Form 1095-A: "You should round the amounts on Form 1095-A to the nearest whole dollar and enter dollars only on Form 8962." and "If you file a paper return and do not round amounts to whole dollars, be sure to enter the decimal point to separate dollars and cents." Keep exact cents (as `amb.2025.sales_rounding` does), or round each monthly input? With cents, line 26 or 29 can differ by a few dollars from a return that rounds.
- **Q11. `sa.excluded_income` as the Worksheet 1-1 line 3 gate.** It also asks about Form 4563 and Puerto Rico income, which Worksheet 1-1 does not add. Reuse it (over-refusing those) or add a Form 2555-only question?
- **Q12. Monthly versus annual when they differ only by rounding.** With line 10 Yes, line 11 uses line 8a; monthly would use 12 × line 8b. They can differ by up to $6. The derivation in Q5 makes the choice for the filer; is that acceptable without telling them?
- **Q13. The size cap.** Which family size should the pinned poverty table stop at, with a refusal above it?

## 9. Draft owner decision batch (drafts; nothing here is decided)

1. **Scope.** Compute Form 8962 Parts I to III with any number of Forms 1095-A, the annual and monthly calculations and Table 5; refuse Parts IV and V and the cases R3 to R5 and R8. *Recommended: yes.* Alternative: also compute Part IV Situations 1, 2 and 4 with entered percentages (about 36 more lines per form).
2. **The line 5 atom (Q2).** Add `percent_floor` with the cap, as drafted. *Recommended: yes.* Alternatives: the atom without the cap (line 5 printed differently above 400%); or refuse every Form 8962 (no other route exists).
3. **Table 2 (5.3).** `keyed_lookup` with 402 rows. *Recommended.* Alternative: let `rate_lookup` take a Count key and store the 252 printed bands.
4. **Line 1 (Q1).** Let `sum` accept Count operands. *Recommended.* Alternative: a keyed table from (persons, dependents) to size.
5. **Poverty table (Q1b, Q13).** Pinned rows to family size 20 generated by the footnotes, refusing above. *Recommended.* Alternative: rows 1 to 8 and the footnote arithmetic in a `choose`.
6. **Line 8a (Q3).** Accept the double rounding and record it. *Recommended*, because it bites only with cents in household income. Alternative: an optional rounding unit on `multiply_rate`.
7. **Column B corrections (R6).** The filer enters the corrected SLCSP per month, with a notice. *Recommended.* Alternative: refuse when a correction is needed.
8. **Year of marriage (R2).** Refuse when married in 2025 and anyone was enrolled before the first full month of marriage. *Recommended.* Alternative: compute without the election and notify.
9. **Below 100% (R7, Q4).** Compute both branches; ask one question for the Marketplace-estimate exception; line 24 zero when not applicable. *Recommended.* Alternative: refuse below 100%.
10. **Line 10 (Q5, Q12).** Derived from the entries. *Recommended.* Alternative: a filer question.
11. **Dependents (Q6, Q7).** Per dependent a 'required to file because of income (Chart B)' question and one MAGI input; Chart C alone does not count; recorded in the register. *Recommended.* Alternative: four inputs; or refuse any dependent required to file.
12. **Rounding of Form 1095-A amounts (Q10).** Exact cents. *Recommended.* Alternative: round each input to the dollar.
13. **Several forms (R15, Q8).** One `b_counted` question per form; a screen refuses when the filer says two counted forms are from the same state (the model cannot see states). *Recommended.* Alternative: refuse more than one form with a column B.
14. **Downstream (5.2).** Revisit `amb.2025.dc_rate_nonpositive_agi`'s reason; rewire the `ptc` coverage category to the new gates; drop `s3.line9` from fixtures and profiles. *Recommended: yes* (these are consequences, listed for approval).
15. **Sources.** Archive 26 USC 36B, Rev. Proc. 2024-35 and the 2024 HHS poverty guidelines for second printings. *Recommended: yes* (the tables otherwise rest on one printing each).

## 10. Verified versus inferred

Checked against the archived text or the repository:

- Every Form 8962 line text in 3.2, the Worksheet 1-1, 1-2 and 2 lines, Tables 1-1 to 1-3, Table 2 and Table 5, read from f8962 and i8962 (`.cols.txt` and the layout `.txt`).
- Table 2: all 252 printed entries parsed from the i8962 p. 11 layout text and matched to the derivation in 4.4 with no mismatch. Tables 1-1 to 1-3: the linear pattern and the footnote examples, by hand arithmetic. Table 5: layout text, and its second printing in p974 p. 52.
- P.L. 119-21 sections 71301 to 71305 and their effective dates (pp. 251 to 255).
- The SOI counts (soi-23in27aca row "All returns", columns 3, 5, 7, 9) and the coverage report rows.
- The project facts in section 0 and 5.2: s2.yaml, s3.yaml, f1040.yaml lines 17, 18, 22, 31, s8812.yaml line 238, ftc.yaml line 151, sa.yaml `sa.dependent` and `sa.excluded_income`, sc.yaml `sc.hi_screen`, scope.yaml line 42, household.yaml, dependent.yaml ids, categories.json `ptc`, the register entry `amb.2025.dc_rate_nonpositive_agi`, check.ts atom typing, eval.ts multiply_rate rounding, and the fixture counts by grep.
- The quote check (`python3 -I /tmp/premises/check_quotes.py`) was run on this file and reports no misses. Passages that are project text (YAML labels, the register, the coverage report), proposed interview wording or spec text are in single quotes, which the check does not read; quotes shorter than 12 characters are not checked. Source passages cut at an inner quotation mark are quoted only up to it.

Inferred, not checked:

- That the 2.4 million 2023 net-PTC returns and the 5.6 million repayment returns resemble 2025 (the report's own assumption), and every share of a sub-situation (none is measured).
- That no Form 8962 situation outside section 6 is common; in particular how often allocation (R1) or unpaid months (R5) occur among Form 8962 filers.
- That `sum` could take Counts with only a checker and rendering change; that an unknown helper line off a `choose` branch would block a return (Q1b); how the interview would present 36 monthly inputs.
- That the double-rounding case in Q3 occurs in practice with the tool's cents.
- The not-archived sources in section 2 (URLs given from knowledge, not fetched); the statement that the 2026 Table 2 will differ rests on knowledge of the expiring enhancement, not on archived text.
- The revisions of f8962, i8962, p974, f1095a and i1095a (the manifest records only "2025").
