> **Status: draft for the owner (2026-11-04).** Written in a Claude cloud session on branch `ny/2025-foundation`
> (brief: `docs/ny/2026-11-04_ny_cloud_brief.md`, Phase 2) from the archived New York sources in `sources/ny/2025/`,
> before any New York encoding. Every claim about a form carries a locator and is testimony until checked again at
> authoring. Nothing here is decided: the owner's questions are in `docs/ny/DECISIONS.md`.
> **Verified:** see `ny-it201-nyc-resident.verification.md`, which supersedes this map where they differ.

# Premise map — New York Form IT-201 for a full-year New York City resident (tax year 2025 documents)

The target is the owner's own 2026 New York return: a full-year New York City resident filing Form IT-201 with the
New York standard deduction, no New York credit or subtraction known to apply. It is built on the final tax-year 2025
documents and carried to 2026 with `tools/year_diff.py` and `tools/fixtures_year.py` once the 2026 editions
publish. No return data was used or asked for.

**Locator convention** (PROJECT_INDEX): `doc p. N, heading, "quote"`, where page N is the N-th form-feed chunk of
`sources/ny/2025/<doc>.cols.txt` (for these PDFs, the printed page number). The two web pages
(`ny_it201i-html`, `ny_it201_tax_tables`) are one chunk each and are cited by heading. Quotes are verbatim with
`...` for an omission; proposed project wording is in single quotes or backticks, never double quotes. Every
double-quoted string was checked against the archived text by a script (normalizing whitespace, quote marks, dashes
and leader dots; the filing-status glyphs below removed).

**Filing-status numbers.** IT-201 and IT-201-I print the statuses as circled digits: ① Single, ② Married filing joint
return, ③ Married filing separate return, ④ Head of household (with qualifying person), ⑤ Qualifying surviving spouse
(`ny_it201 p. 1`, item A; `ny_it201i-html`, "New York State standard deduction table"). In the PDF text layer the
digits are private-use characters that read as blanks (`sources/ny/2025/README.md`), so a PDF quote below shows
"filing status  only (Single)"-style gaps; where the digit decides a rule, the web edition's wording is quoted with it.

**Federal ids** are the project's (`forms/2025/`), checked in the files on this branch.

---

## 1. Sources

| id | document | used for |
| --- | --- | --- |
| `ny_it201` | Form IT-201 (2025), 4 pages | line numbers and labels |
| `ny_it201i` | Form IT-201-I (2025), 41 pages | every rule |
| `ny_it201i-html` | its web edition | filing-status digits and tables (`sources/ny/2025/README.md` lists the PDF pages whose reading order is doubtful) |
| `ny_it201_tax_tables` | 2025 New York State and City Tax Tables (web only) | lines 39 and 47a below $65,000 |
| `ny_it201att` | Form IT-201-ATT (2025) | lines 42, 45, 51, 53, 71 |
| `ny_it2` | Form IT-2 (2025) | lines 72 to 74 |
| `ny_it270i` | Form IT-270-I (2025) | line 70a's eligibility |

Named but not archived (each refusal cites the IT-201-I page that names it): Forms IT-196, IT-203, IT-225, IT-360.1,
IT-112-R, IT-213, IT-214, IT-215, IT-216, IT-209, IT-272, IT-227, IT-195, IT-1099-R, IT-2105.9, IT-6-SNY, IT-203-A,
Y-203, IT-370.

Not found: any official worked example of a whole IT-201. The only official examples of a computation in scope are the
two tax-table examples (`ny_it201_tax_tables`: State, "Their taxable income on line 38 is $38,275" ... "The amount shown
where the income line and filing status column meet is $1,773"; City, "Their taxable income on line 47 is $38,275" ...
"is $1,292"), both married filing jointly; they are class A candidates (spec 6.1) for the two table lookups.

---

## 2. General rules that bind every line

- **Whole dollars.** `ny_it201i p. 2`, Entering whole dollar amounts, "When you enter amounts on your return, enter
  whole dollar amounts only. This includes amounts on any credit forms, schedules, or other forms you submit with your
  New York State return." and "round cents to the nearest dollar using the following rules: • Drop amounts that are less
  than 50 cents. For example, $1.39 becomes $1. • Increase amounts that are 50 cents or more to the next dollar." The
  federal encoding is in cents; where New York rounds a federal amount, and whether a computed line (a rate schedule,
  a 0.171% credit) is rounded by this rule, is a design question (DECISIONS D8). Inferred: the rule reads as half-up
  at the dollar for every entry.
- **Same income as federal.** `ny_it201i p. 7`, Lines 1 through 19, "The calculation of your New York State, New York
  City, and Yonkers income tax is based on the information you reported on your federal income tax return, including
  your income and federal adjustments to income."
- **Losses.** `ny_it201i p. 3`, How to fill in the forms, "If you are entering a loss (an amount less than zero), place a
  minus sign immediately to the left of the loss amount." Lines 6, 7, 8, 11, 13 and 16 to 19 can be negative.
- **Credits that need a form.** `ny_it201i p. 2`, Other forms you may need to file, "To claim a tax credit (with the
  exception of the household credit and New York City school tax credit), you must complete and submit the appropriate
  credit form." This is the source's own line between the credits the target gets without claiming (household credits,
  school tax credit) and every other credit (refused when it applies).

---

## 3. Form IT-201, every line in order

Columns: **reads** (what the line takes), **rule** (quoted, with page), **target** (in scope: computed; zero: always
zero for the target, with the screen that makes it so; refused: a screen that refuses when it applies).

### 3.1 Page 1: identification and items A to H (`ny_it201 p. 1`; `ny_it201i pp. 4–6`)

| item | reads | rule | target |
| --- | --- | --- | --- |
| Name, address, SSN, date of birth, county, school district name and code, decedent dates | taxpayer facts | `ny_it201i p. 4`, School district name and code number, "Enter the name and code number of the school district where you live." | not computed. Personal data stays off the encoding; whether the tool prints a reminder list is a presentation choice (DECISIONS D13). A death in 2025 or 2026 before filing (decedent dates) is a refusal candidate, as federally |
| A Filing status | `f1040.status` | `ny_it201i p. 4`, Item A, "In most cases, you must use the same filing status you used on your federal return." Exceptions only for married couples filing jointly federally: one spouse "a New York State resident and the other is a nonresident or part-year resident", or the spouse's whereabouts unknown or refusal to sign (`p. 5`, "you may file a separate New York return using filing status") | in scope: copy of `f1040.status`. Refused: a joint federal return with one spouse not a full-year New York State (or City) resident, and the two separate-return exceptions |
| B Itemized federally | `sa.itemizes` | `ny_it201i p. 5`, Item B, "If you itemized your deductions on your 2025 federal income tax return, mark an X in the Yes box." | in scope: copy. Item B does not choose the New York deduction (line 34) |
| C Can be claimed as a dependent | new input (see note) | `ny_it201i p. 5`, Item C, "If you can be claimed as a dependent on another taxpayer’s federal return, you must mark an X in the Yes box. You must mark the Yes box even if the other taxpayer did not claim you as a dependent." | in scope as an input: it sets the single standard deduction (line 34) and denies both household credits and the school tax credit; note that the federal input `sa.dependent` (`forms/2025/sa.yaml`) asks to "Answer no if the person who could claim you is not required to file", a federal exception New York's item C does not print; and `sa.dependent` true is refused federally. So item C is not a copy of `sa.dependent` (DECISIONS D9) |
| D1 Foreign account | `sb.line7a` | `ny_it201i p. 5`, Item D1, "If you marked Yes on federal Schedule B (Form 1040), Interest and Ordinary Dividends, Part III then mark an X in the Yes box." | in scope: copy (a box, no amount) |
| D2 Yonkers | screen | `ny_it201i p. 5`, Item D2, "All IT-201 filers must complete item D2." | screen: a Yes on D2(1) or D2(4) refuses (Yonkers out of scope); the target answers No and 0 months |
| E NYC living quarters and days | none | `ny_it201i p. 5`, Item E, "If you are a full-year New York City resident (this includes the Bronx, Brooklyn, Manhattan, Queens, and Staten Island), leave item E blank." | blank for the target |
| F Months in NYC | 12 (and 12 for a spouse on a joint return) | `ny_it201i p. 5`, Item F, "Enter in the applicable box the number of months you and your spouse (if filing a joint return) lived in New York City during 2025. We need this information to verify your New York City school tax credit." | in scope: 12 for a full-year resident (a constant, given the residency screen) |
| G Special condition codes | screen | `ny_it201i p. 5`, Item G, "If you qualify for one or more of the special conditions below, enter the specified two-character code." | screen: code A6 (Build America Bond interest) changes the household-credit income (Note 1) and is refused; the others (C7, D9, K2, E3, E4, E5, 56, C2, M4 to M9, Y1) concern filing dates, collection, itemizing, military residence or Yonkers and are refused or outside the computation (DECISIONS D13) |
| H Dependents | count of `dependent.claimed` (as `f8962.deps` counts them) | `ny_it201i p. 6`, Item H, "Enter the required information for each dependent you claimed on federal Form 1040. Also enter the required information for any dependent you were entitled to claim on your federal return but chose not to" | in scope: the count feeds lines 36, 40, 48. Inferred: `dependent.claimed` (a qualifying child or relative, `dependent.yaml`) already means "entitled to claim", which matches; checked at authoring |

### 3.2 Federal income and adjustments, lines 1 to 19 (`ny_it201 p. 2`; `ny_it201i p. 7`)

`ny_it201i p. 7`, Lines 1 through 19, "The amount entered on line 1 (wages, salaries, tips, etc.) should be the same as
the amount reported on federal Form 1040, line 1z." No other line of 1 to 18 is tied to a federal line by the
instructions; each mapping below is from the printed labels (inferred, to be checked at authoring), and line 19's
label names federal adjusted gross income.

| line | label (`ny_it201 p. 2`) | federal source | target |
| --- | --- | --- | --- |
| 1 | "Wages, salaries, tips, etc." | `f1040.line1z` (stated, `p. 7`) | in scope |
| 2 | "Taxable interest income" | `f1040.line2b` | in scope |
| 3 | "Ordinary dividends" | `f1040.line3b` | in scope |
| 4 | "Taxable refunds, credits, or offsets of state and local income taxes (also enter on line 25)" | `s1.line1` | in scope; see line 25 for a tension |
| 5 | "Alimony received" | `s1.line2a` | in scope |
| 6 | "Business income or loss (submit a copy of federal Schedule C, Form 1040)" | `s1.line3` | in scope as a number; it brings the MCTMT screen (lines 54a–54e) |
| 7 | "Capital gain or loss (if required, submit a copy of federal Schedule D, Form 1040)" | `f1040.line7a` | in scope |
| 8 | "Other gains or losses (submit a copy of federal Form 4797)" | Schedule 1 line 4: no project line; Form 4797 is refused federally (`scope.schedule1`, "sales of business property (Form 4797)") | zero |
| 9 | "Taxable amount of IRA distributions. If received as a beneficiary, mark an X in the box" | `f1040.line4b` | in scope; the beneficiary box matters only to line 29 (refused) |
| 10 | "Taxable amount of pensions and annuities. If received as a beneficiary, mark an X in the box" | `f1040.line5b` | in scope |
| 11 | "Rental real estate, royalties, partnerships, S corporations, trusts, etc. (submit copy of federal Schedule E, Form 1040)" | Schedule 1 line 5: refused federally (`scope.schedule1`) | zero |
| 12 | "Rental real estate included in line 11" | (memo line, not in line 17) | zero |
| 13 | "Farm income or loss (submit a copy of federal Schedule F, Form 1040)" | Schedule 1 line 6: refused federally | zero |
| 14 | "Unemployment compensation" | `s1.line7` | in scope |
| 15 | "Taxable amount of Social Security benefits (also enter on line 27)" | `f1040.line6b` | in scope |
| 16 | "Other income Identify:" | `s1.line9` (Schedule 1 "Total other income") | in scope; inferred mapping: with lines 4 to 8, 11, 13, 14 and 16 the IT-201 lines take every Schedule 1 Part I line, so line 17 equals `f1040.line9` |
| 17 | "Add lines 1 through 11 and 13 through 16" | arithmetic | in scope |
| 18 | "Total federal adjustments to income Identify:" | `s1.line26` (= `f1040.line10`) | in scope |
| 19 | "Federal adjusted gross income ( subtract line 18 from line 17 )" | arithmetic; must equal `f1040.line11a` | in scope. `ny_it201i p. 7`, "Do not leave line 19 blank." Design: compute by the printed arithmetic and check it against `f1040.line11a` (DECISIONS D4) |

Whole-dollar rounding (section 2) applies to each of lines 1 to 18; rounding each then adding can differ from rounding
federal AGI by a few dollars (inferred). Which is correct is a design question (D8).

### 3.3 New York additions, lines 20 to 24 (`ny_it201 p. 2`; `ny_it201i pp. 7–8`)

| line | label | rule | target |
| --- | --- | --- | --- |
| 20 | "Interest income on state and local bonds and obligations (but not those of NYS or its local governments)" | `ny_it201i p. 7`, Line 20, "enter any such interest income that you received or that was credited to you during 2025 that was not included in your federal adjusted gross income. This includes interest income on: – state and local bonds, – interest and dividend income from tax-exempt bond mutual funds, and – tax-exempt money market funds that invest in obligations of states other than New York." | candidate: an input, the non-New York part of tax-exempt interest (`f1040.line2a`, which includes exempt-interest dividends, `div.box12`). The federal encoding does not split tax-exempt interest by issuing state; bond premium and purchase between interest dates (same page) send amounts to IT-225 or IT-196. DECISIONS D5 |
| 21 | "Public employee 414(h) retirement contributions from your wage and tax statements" | `ny_it201i p. 8`, Line 21, "enter the amount of 414(h) retirement contributions, if shown on any federal Form W-2, Wage and tax statement if you are:" (a list of New York public retirement systems) | screen: zero unless the owner is a New York public employee in one of the listed systems (owner checklist) |
| 22 | "New York’s 529 college savings program distributions" | `ny_it201i p. 8`, Line 22, "Did you make a nonqualified withdrawal during 2025 from an account established under New York’s 529 college savings program?" (if Yes, the Line 22 worksheet) | screen: zero, refused if yes (the worksheet needs prior years' totals) |
| 23 | "Other (Form IT-225, line 9)" | `ny_it201i p. 8`, Line 23, "Enter on line 23 the amount from Form IT-225, line 9. Submit Form IT-225 with your return." | refused when any IT-225 addition applies (screen) |
| 24 | "Add lines 19 through 23" | arithmetic | in scope |

### 3.4 New York subtractions, lines 25 to 33 (`ny_it201 p. 2`; `ny_it201i pp. 8–10`)

| line | label | rule | target |
| --- | --- | --- | --- |
| 25 | "Taxable refunds, credits, or offsets of state and local income taxes (from line 4)" | `ny_it201i p. 8`, Line 25, "If you received an inflation refund check from the Tax Department and included the check amount in the calculation of federal adjusted gross income reported on line 19, then enter that amount on line 25." | **tension**: the form's labels say line 25 is line 4 (`ny_it201 p. 2`, "(also enter on line 25)", "(from line 4)"); the 2025 instructions speak only of the inflation refund check. The web edition prints the same paragraph (`ny_it201i-html`, "Line 25: Taxable refunds, credits, or offsets of state and local income taxes"). Not resolvable from the archive; DECISIONS D6 |
| 26 | "Pensions of NYS and local governments and the federal government" | `ny_it201i p. 9`, Line 26, "Did you receive a pension or other distribution from a New York State or local government pension plan or federal government pension plan that was included in your federal adjusted gross income?" | screen: zero, refused if yes |
| 27 | "Taxable amount of Social Security benefits (from line 15)" | label | in scope: copy of line 15 |
| 28 | "Interest income on U.S. government bonds" | `ny_it201i p. 8–9`, Line 28, "Did you include interest income from U.S. government bonds or other U.S. government obligations on lines 2, 6, or 11?" ... "enter the amount of interest income you earned from bonds or other obligations of the U.S. government." Mutual-fund dividends qualify only for funds meeting "the 50% asset requirement each quarter" | candidate: an input (Treasury interest, Form 1099-INT box 3, is included in `interest.amount` with no separate field); a fund's qualifying share needs the fund's statement. DECISIONS D5 |
| 29 | "Pension and annuity income exclusion" | `ny_it201i p. 9`, Line 29, "If Yes, and you were 59½ before January 1, 2025, enter the qualifying pension and annuity income included in your 2025 federal adjusted gross income, but not more than $20,000." | screen: zero for a filer under 59½ with no pension received as a beneficiary; refused otherwise (owner checklist) |
| 30 | "New York’s 529 college savings program deduction/earnings." | `ny_it201i p. 10`, Line 30, "as an account owner, made contributions, enter the amount up to $5,000 ($10,000 for married taxpayers filing a joint return) on line 1 of the Line 30 worksheet." | candidate: computable from one input (contributions) capped by status; a withdrawal included in federal AGI also goes here. Needs no separate form. DECISIONS D5 |
| 31 | "Other ( Form IT-225, line 18)" | `ny_it201i p. 10`, Line 31, "Enter on line 31 the amount from Form IT-225, line 18. Submit Form IT-225 with your return." | refused when any IT-225 subtraction applies |
| 32 | "Add lines 25 through 31" | arithmetic | in scope |
| 33 | "New York adjusted gross income (subtract line 32 from line 24)" | `ny_it201i p. 10`, Line 33, "Do not leave line 33 blank." | in scope (can be negative; no floor printed) |

### 3.5 Deduction, exemptions and taxable income, lines 34 to 38 (`ny_it201 p. 2–3`; `ny_it201i pp. 10–11`)

| line | rule | target |
| --- | --- | --- |
| 34 | `ny_it201 p. 2`, "Enter your standard deduction or your itemized deduction (from Form IT-196)". `ny_it201i p. 10`, Line 34, "You may take either the New York standard deduction or the New York itemized deduction." The standard deduction table (`ny_it201i-html`, "New York State standard deduction table"): "① Single and you marked item C Yes" $3,100; "① Single and you marked item C No" $8,000; "② Married filing joint return" $16,050; "③ Married filing separate return" $8,000; "④ Head of household (with qualifying person)" $11,200; "⑤ Qualifying surviving spouse" $16,050 | in scope: the standard deduction, a parameter keyed by status (and item C for single). Itemizing (Form IT-196) refused. `ny_it201i p. 11`, Notes, "If you are married and filing separate returns (filing status ), both of you must take the standard deduction unless both of you choose to itemize deductions on your New York returns." Inferred: item C Yes with a status other than single has no row of its own (the table splits only Single by item C) |
| 35 | `ny_it201 p. 2`, "Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)" | in scope: `subtract_floor0` |
| 36 | `ny_it201i p. 11`, Line 36, "The value of each New York State dependent exemption is $1,000." and "Multiply the number of your dependents listed on Form IT-201, item H ... by 1,000" | in scope: item H count × $1,000 |
| 37 | `ny_it201i p. 11`, Lines 37 and 38, "Subtract line 36 from line 35. The result is your taxable income. Enter this amount on both line 37 and line 38. If line 36 is more than line 35, leave line 37 and line 38 blank." | in scope: `subtract_floor0`, a blank read as zero (inferred) |
| 38 | `ny_it201 p. 3`, "Taxable income (from line 37 on page 2)" | in scope: copy of line 37 |

### 3.6 New York State tax and credits, lines 39 to 46 (`ny_it201 p. 3`; `ny_it201i pp. 12–13`, 32–39)

| line | rule | target |
| --- | --- | --- |
| 39 | Section 4 | in scope |
| 40 | Section 5.1 | in scope |
| 41 | `ny_it201i p. 13`, Line 41, "Did you have income from sources outside New York State and pay income tax to another state, a local government of another state, the District of Columbia, or to a province of Canada?" (if Yes, Form IT-112-R) | refused if yes; zero otherwise |
| 42 | `ny_it201i p. 13`, Line 42, "If you are claiming any nonrefundable credits, complete the appropriate credit forms and Form IT-201-ATT." | refused if any; zero otherwise |
| 43 | `ny_it201 p. 3`, "Add lines 40, 41, and 42" | in scope |
| 44 | `ny_it201 p. 3`, "Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)" | in scope |
| 45 | `ny_it201i p. 13`, Line 45, "If you are subject to any other taxes, complete the appropriate forms and Part 2 of Form IT-201-ATT." (`ny_it201att p. 2`, Part 2: "New York State tax on capital gain portion of lump-sum distributions (Form IT-230)" and "Other New York State taxes") | refused if any; zero otherwise |
| 46 | `ny_it201 p. 3`, "Total New York State taxes (add lines 44 and 45)" | in scope |

### 3.7 New York City, Yonkers and MCTMT, lines 47 to 58 (`ny_it201 p. 3`; `ny_it201i pp. 13–18`)

| line | rule | target |
| --- | --- | --- |
| 47 | `ny_it201i p. 13`, Line 47, "did you claim an itemized deduction for that contribution on Form IT-196? • If No, enter the line 38 amount on line 47." (the question is about New York Charitable Gifts Trust Fund contributions) | in scope: copy of line 38 (the worksheet needs itemizing, refused) |
| 47a | Section 4.4 | in scope |
| 48 | Section 5.2 | in scope |
| 49 | `ny_it201 p. 3`, "Subtract line 48 from line 47a (if line 48 is more than" ... "line 47a, enter 0)" | in scope |
| 50 | `ny_it201i p. 14`, Line 50, "If you were a New York City resident for only part of 2025, complete Form IT-360.1" | zero (residency screen) |
| 51 | `ny_it201i p. 14`, Line 51, "Enter the total amount of other New York City taxes from Form IT-201-ATT, Part 3, line 34." (lump-sum distributions, Form IT-230); the joint-return rule for one spouse a nonresident (`p. 15`) | refused if any; zero otherwise |
| 52 | `ny_it201 p. 3`, "Add lines 49, 50, and 51" | in scope |
| 53 | `ny_it201i p. 15`, Line 53, "Can you claim the New York City unincorporated business tax (UBT) credit, the New York City accumulation distribution credit, or the part-year resident nonrefundable New York City child and dependent care credit?" | refused if yes; zero otherwise |
| 54 | `ny_it201 p. 3`, "Subtract line 53 from line 52 (if line 53 is more than" ... "line 52, enter 0)" | in scope |
| 54a–54e | `ny_it201i p. 14`, Lines 54a through 54e, "If an individual’s net earnings from self-employment allocated to either zone exceed $50,000 for the tax year, then you are subject to the MCTMT." Zone 1 is the five New York City counties (`p. 14`). `ny_it201i p. 17`, "Line 54c: MCTMT for Zone 1 Multiply the amount on line 54a by 0.60% (0.0060)." | zero when no person's net earnings from self-employment allocated to a zone exceed $50,000; otherwise a scope choice (DECISIONS D7). The federal encoding computes Schedule SE per person; `ny_it201i p. 16`, "Net earnings from self-employment generally is the amount reported on federal Schedule SE (Form 1040), Part 1, line 6, derived from the source of self-employment income." |
| 55 | `ny_it201i p. 17`, Line 55, "If you were a resident of Yonkers, did you enter an amount that is more than 0 on line 46?" | zero (Yonkers screen) |
| 56 | `ny_it201i p. 17`, Line 56, "If you were not a resident of Yonkers, did you earn wages there?" | zero; refused if yes |
| 57 | `ny_it201i p. 18`, Line 57, "If you were a resident of Yonkers for only part of 2025, complete Form IT-360.1" | zero |
| 58 | `ny_it201 p. 3`, "Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 54e through 57)" | in scope |

### 3.8 Sales or use tax and contributions, lines 59 to 62 (`ny_it201 p. 3–4`; `ny_it201i pp. 18–19`)

| line | rule | target |
| --- | --- | --- |
| 59 | `ny_it201 p. 3`, "Sales or use tax (do not leave blank)". `ny_it201i p. 19`, Line 59, "If you do not owe any sales or use tax, you must enter 0 on line 59." The chart (`ny_it201i p. 18`, "Sales and use tax chart") gives an amount by federal AGI band (up to $15,000: $3 ... 200,001 and greater: "0.0175% (0.000175) of income, or $125, whichever amount is smaller") for purchases "costing less than $1,000 each"; `p. 18`, "You must use Form ST-141 to calculate your sales and use tax liability to be reported on this return if any of the following apply" | scope choice (DECISIONS D3): an input the owner states, or the chart from line 19 with a screen for the ST-141 cases |
| 60 | `ny_it201i p. 19`, Line 60, "Do you want to make any voluntary contributions to the funds listed on Form IT-227?" | zero; refused if yes (or an input; D13) |
| 61 | `ny_it201 p. 3`, "voluntary contributions (add lines 46, 58, 59, and 60)" | in scope |
| 62 | `ny_it201 p. 4`, "Enter amount from line 61" | in scope |

### 3.9 Payments and refundable credits, lines 63 to 76 (`ny_it201 p. 4`; `ny_it201i pp. 19–22`)

| line | rule | target |
| --- | --- | --- |
| 63 Empire State child credit | `ny_it201i p. 19`, Line 63, "Do you have at least one qualifying child?" ... "(A qualifying child must be less than 17 years old on December 31st of the tax year.)" then Form IT-213 | refused when a dependent is under 17 (or the owner has a qualifying child); zero otherwise |
| 64 Child and dependent care | `ny_it201i p. 19`, Line 64, "Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you actually claimed it)?" then Form IT-216 | refused if yes (the federal Form 2441 is encoded, the New York form is not); zero otherwise |
| 65 NYS EIC | `ny_it201i p. 19`, Line 65, "Did you claim the federal earned income credit for 2025 on your federal income tax return, or could you have claimed it based on your federal adjusted gross income?" then Form IT-215 | refused when `f1040.line27a` is more than zero or the filer could have claimed it; zero otherwise. Note "or could you have claimed it based on your federal adjusted gross income?" is broader than the federal line (DECISIONS D10) |
| 66 Noncustodial parent EIC | `ny_it201i p. 19`, Line 66, "Did you make child support payments payable through a New York State Support Collection Unit?" | refused if yes |
| 67 Real property tax credit | `ny_it201i p. 19`, Line 67, "Review the instructions for Form IT-214, Claim for Real Property Tax Credit for Homeowners and Renters, to see if you qualify for this credit." | refused if the owner qualifies (the archive holds no IT-214 to state the test; a screen would ask the owner) |
| 68 College tuition credit | `ny_it201i p. 19`, Line 68, "Did you or your spouse or any dependents pay college tuition expenses during 2025?" | refused if yes (Form IT-272); zero otherwise |
| 69 NYC school tax credit (fixed amount) | Section 5.3 | in scope |
| 69a NYC school tax credit (rate reduction amount) | Section 5.3 | in scope |
| 70 NYC EIC | `ny_it201i p. 20`, Line 70, "Did you claim the federal earned income credit for 2025 on your federal return, or could you have claimed it based on your federal adjusted gross income?" | as line 65 |
| 70a NYC income tax elimination credit | `ny_it201i p. 21`, Line 70a, "Review the instructions for Form IT-270, New York City Income Tax Elimination Credit, to see if you qualify for this credit." `ny_it270i p. 1`, General information: "you claimed one or more dependents on Form IT-201, item H" and "your federal adjusted gross income (FAGI) is no more than $5,000 above your applicable income thresholds" and "your investment income is $10,000 or less" | zero when item H is empty (no dependents) or FAGI is more than the highest threshold plus $5,000 for the status ($91,902 married filing jointly with 7 or more dependents; $88,361 single, head of household or separate with 8 or more, `ny_it270i p. 1`, "Line 2: Income thresholds table"); refused otherwise (DECISIONS D11) |
| 71 Other refundable credits | `ny_it201i p. 21`, Line 71, "Enter the total amount of other refundable credits from Form IT-201-ATT, Part 1, Section D, line 18." | refused if any; zero otherwise |
| 72, 73, 74 Tax withheld | `ny_it201i p. 21`, Lines 72, 73, and 74, "Enter on the appropriate line your total New York State, New York City, and Yonkers tax withheld from any of the following: • Form IT-2, Summary of W-2 Statements • Form IT-1099-R, Summary of Federal Form 1099-R Statements • Form 1099-G, Certain Government Payments" and `p. 22`, "• Form W-2G, Certain Gambling Winnings" | in scope with new inputs: the federal `w2` entries have no state or local boxes (box 15 to 20), and the 1099-R, 1099-G and W-2G entries hold no state withholding (DECISIONS D2). Line 74 (Yonkers) zero |
| 75 Estimated payments | `ny_it201i p. 22`, Line 75, "your 2025 estimated tax payments for New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax" and "any amount of overpayment from your 2024 personal income tax return that you applied to your 2025 estimated tax" and "any amount you paid with Form IT-370" | in scope: an input |
| 76 | `ny_it201 p. 4`, "Total payments (add lines 63 through 75)" | in scope |

### 3.10 Refund or amount owed, lines 77 to 84 (`ny_it201 p. 4`; `ny_it201i pp. 22–25`)

| line | rule | target |
| --- | --- | --- |
| 77 | `ny_it201 p. 4`, "Amount overpaid (if line 76 is more than line 62, subtract line 62 from line 76)"; `ny_it201i p. 22`, Line 77, "If you have to pay an estimated tax penalty (see line 81 instructions), subtract the penalty from the overpayment and enter the net overpayment on line 77." | in scope (with line 81 zero unless computed) |
| 78 | `ny_it201i p. 23`, Line 78, "Subtract the amount on line 79 (estimated tax) from line 77." | in scope |
| 78a | `ny_it201i p. 23`, Line 78a, "Enter on line 78a the amount from Form IT-195, line 4." | zero; refused if the owner wants a 529 deposit (or an input; D13) |
| 78b | `ny_it201 p. 4`, "Total refund after NYS 529 account deposit (subtract line 78a from line 78)" | in scope |
| 79 | `ny_it201i p. 23`, Line 79, "Enter the amount of overpayment from line 77 that you want applied to your New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax estimated tax for 2026." | in scope: an input, as federal line 36 |
| 80 | `ny_it201i p. 23`, Line 80, "Enter on line 80 the amount of tax you owe plus any estimated tax penalty you owe (see line 81 instructions) and any other penalties and interest you owe (see line 82 instructions)." | in scope |
| 81 | `ny_it201i p. 23`, Line 81, "You may owe a penalty: • if line 80 is $300 or more and represents more than 10% of the income tax shown on your 2025 return; or • if you underpaid your estimated tax liability for any payment period." (Form IT-2105.9) | scope choice (DECISIONS D12): the federal encoding has no estimated-tax penalty line; a screen could refuse when the safe harbor of `p. 23` ("at least 100% of your 2024 New York income tax", 110% above $150,000 of 2024 New York AGI) is not met, which needs 2024 return figures the owner would type |
| 82 | `ny_it201i p. 24`, Line 82, "If you owe a late filing penalty, late payment penalty, or interest:" | zero (a return filed on time is assumed; D13) |
| 83, 84 | account and withdrawal information | not computed |

---

## 4. The tax computation

### 4.1 Which method (`ny_it201i p. 12`, Line 39; `ny_it201i p. 32`, How to calculate your 2025 New York State tax)

`ny_it201i p. 12`, Line 39, "Is line 33 (your New York adjusted gross income) $107,650 or less? • If Yes, find your
New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is
$65,000 or more, use the New York State tax rate schedule below. Enter the tax due on line 39. • If No, see Tax
computation – New York adjusted gross income of more than $107,650 below."

So: NY AGI ≤ $107,650 and taxable income < $65,000: the Tax Table; NY AGI ≤ $107,650 and taxable income ≥ $65,000:
the rate schedule; NY AGI > $107,650: the tax computation worksheets. The tax-tables page says the same
(`ny_it201_tax_tables`, "If your New York adjusted gross income, Form IT-201, line 33 is more than $107,650, you cannot
use these tables.").

### 4.2 The New York State Tax Table (`ny_it201_tax_tables`, 2025 New York State Tax Table)

Rows "At least" / "But less than", columns "Single or Married filing separately", "Married filing jointly*" (with
"*This column must also be used by a qualifying surviving spouse") and "Head of a household". Bands start $0–13,
13–25, 25–50, then $50 wide to $65,000; last line "$65,000 or more—compute your New York State tax using New York
State tax rate schedule." The project's `table_lookup` atom bands [at least, less than), which matches. To pin as
`tables/<year>/ny_*` with an extractor like `tools/extract_tax_table.py` (Phase 3; the web text has stray spaces
inside some numbers, `sources/ny/2025/README.md`). A midpoint conjecture against the rate schedule, as federally, is
a cheap check (spec 6.3) and is inferred, not stated, by the source.

### 4.3 The New York State tax rate schedule (`ny_it201i p. 33`; the web edition's "New York State tax rate schedule")

Read from the web edition (the PDF's rows are flattened); columns: line 38 over, but not over, the tax.

| status | bands (over – not over: base + rate of the excess over the lower bound) |
| --- | --- |
| ② ⑤ married filing jointly, qualifying surviving spouse | 0–17,150: 4%; 17,150–23,600: $686 + 4.5%; 23,600–27,900: 976 + 5.25%; 27,900–161,550: 1,202 + 5.5%; 161,550–323,200: 8,553 + 6%; 323,200–2,155,350: 18,252 + 6.85%; 2,155,350–5,000,000: 143,754 + 9.65%; 5,000,000–25,000,000: 418,263 + 10.3%; over 25,000,000: 2,478,263 + 10.9% |
| ① ③ single, married filing separately | 0–8,500: 4%; 8,500–11,700: $340 + 4.5%; 11,700–13,900: 484 + 5.25%; 13,900–80,650: 600 + 5.5%; 80,650–215,400: 4,271 + 6%; 215,400–1,077,550: 12,356 + 6.85%; 1,077,550–5,000,000: 71,413 + 9.65%; 5,000,000–25,000,000: 449,929 + 10.3%; over 25,000,000: 2,509,929 + 10.9% |
| ④ head of household | 0–12,800: 4%; 12,800–17,650: $512 + 4.5%; 17,650–20,900: 730 + 5.25%; 20,900–107,650: 901 + 5.5%; 107,650–269,300: 5,672 + 6%; 269,300–1,616,450: 15,371 + 6.85%; 1,616,450–5,000,000: 107,651 + 9.65%; 5,000,000–25,000,000: 434,163 + 10.3%; over 25,000,000: 2,494,163 + 10.9% |

Each base can be checked against the band below it (for example 686 = 4% of 17,150), a cheap internal consistency check
for Phase 3 (inferred). The schedule prints no rounding; the whole-dollar rule of section 2 applies to the line 39
entry (D8). The `bracket_schedule` atom is in the vocabulary but implemented by neither evaluator (spec 6.3); the
federal Tax Computation Worksheet is encoded with guarded rows of parameters instead, which fits here too.

### 4.4 Tax computation worksheets: recapture of the tax table benefit (`ny_it201i pp. 34–39`)

Sixteen worksheets, five or six per status group (married filing jointly and qualifying surviving spouse: 1 to 6;
single and married filing separately: 7 to 11; head of household: 12 to 16). Read from the web edition, which keeps each
printed amount on its line.

The first worksheet of each group phases the whole of taxable income into the flat rate of the bracket that contains
the start of the phase-in. Worksheet 1 (`ny_it201i p. 34`): "If your New York adjusted gross income (line 33) is more
than $107,650, but not more than $25,000,000, and your taxable income (line 38) is $161,550 or less, then you must
calculate your tax using this worksheet." Its lines: "3 Multiply line 2 by 5.5% (0.055) (Stop: If the line 1 amount is
$157,650 or more, skip lines 4 through 8 and enter the line 3 amount on line 9)"; 4 the rate-schedule tax; "5 Subtract
line 4 from line 3"; "6 Enter the excess of line 1 over $107,650"; "7 Divide line 6 by $50,000 and round the result to
the fourth decimal place"; "8 Multiply line 5 by line 7"; "9 Add lines 4 and 8". Worksheets 7 and 12 are the same
with 6% and taxable income limits of $215,400 and $269,300 (`ny_it201i-html`, "Tax computation worksheet 7": "Multiply
line 2 by 6% (0.06)").

The later worksheets add a printed "Recapture Base amount" and "Incremental Benefit amount" phased in over $50,000 of NY
AGI above the bracket's start. Worksheet 2 (`ny_it201i p. 34`): "If your New York adjusted gross income (line 33) is
more than $161,550, but not more than $25,000,000, and your taxable income (line 38) is more than $161,550 but not more
than $323,200, then you must calculate your tax using this worksheet." Lines: 3 the rate-schedule tax; "4 Recapture Base
amount"; "5 Incremental Benefit amount"; "6 Enter the excess of line 1 over $161,550"; "7 Enter the lesser of line 6 or
$50,000"; "8 Divide line 7 by $50,000 and round the result to the fourth decimal place"; "9 Multiply line 5 by line 8";
"10 Add lines 3, 4, and 9".

| worksheet | NY AGI over | taxable income over – not over | recapture base | incremental benefit |
| --- | --- | --- | --- | --- |
| 2 (②⑤) | 161,550 | 161,550 – 323,200 | 333 | 807 |
| 3 (②⑤) | 323,200 | 323,200 – 2,155,350 | 1,140 | 2,747 |
| 4 (②⑤) | 2,155,350 | 2,155,350 – 5,000,000 | 3,887 | 60,350 |
| 5 (②⑤) | 5,000,000 | over 5,000,000 | 64,237 | 32,500 |
| 8 (①③) | 215,400 | 215,400 – 1,077,550 | 568 | 1,831 |
| 9 (①③) | 1,077,550 | 1,077,550 – 5,000,000 | 2,399 | 30,172 |
| 10 (①③) | 5,000,000 | over 5,000,000 | 32,571 | 32,500 |
| 13 (④) | 269,300 | 269,300 – 1,616,450 | 787 | 2,289 |
| 14 (④) | 1,616,450 | 1,616,450 – 5,000,000 | 3,076 | 45,261 |
| 15 (④) | 5,000,000 | over 5,000,000 | 48,337 | 32,500 |

Each also requires NY AGI "not more than $25,000,000"; worksheets 6, 11 and 16 apply above that: "Multiply line 1 by
10.9% (0.109)" (`ny_it201i p. 35`, Tax computation worksheet 6). The amounts were read from the web edition
(`ny_it201i-html`, e.g. "4. _____333______"); the PDF prints the same numbers detached after each worksheet (`p. 34`,
"333" and "807"). Inferred and to be checked in Phase 3: the worksheets cover every return with NY AGI over $107,650,
because taxable income cannot exceed NY AGI (lines 34 and 36 are not negative). The "round the result to the fourth
decimal place" step fits the `prorate` atom with 4 places; the direction of rounding is not printed (half-up is the
reading the federal `amb.2025.sli_ratio_places` took for a similar instruction; register a New York entry).

Owner relevance: this recapture applies at NY AGI over $107,650. Whether the owner's income reaches it is for the owner
to see (checklist item 7); the target needs all of it computed, since 2026 income is not known.

### 4.5 New York City resident tax (`ny_it201i p. 13`, Line 47a; p. 40; `ny_it201_tax_tables`)

`ny_it201i p. 13`, Line 47a, "Is line 47 (your New York City taxable income) less than $65,000? • If Yes, find your New
York City resident tax using the 2025 New York City Tax Table. Enter the tax on line 47a. • If No, find your New York City
resident tax using the New York City tax rate schedule below." Unlike line 39, no NY AGI test and no recapture.

The City Tax Table (`ny_it201_tax_tables`, New York City Tax Table) has the same columns, bands $0–18, 18–25, 25–50,
then $50 wide to $65,000; "$65,000 or more—compute your New York City tax using New York City tax rate schedule."

The City rate schedule (`ny_it201i p. 40`; web edition, "New York City tax rate schedule"):

| status | bands |
| --- | --- |
| ② ⑤ | 0–21,600: 3.078%; 21,600–45,000: $665 + 3.762%; 45,000–90,000: 1,545 + 3.819%; over 90,000: 3,264 + 3.876% |
| ① ③ | 0–12,000: 3.078%; 12,000–25,000: $369 + 3.762%; 25,000–50,000: 858 + 3.819%; over 50,000: 1,813 + 3.876% |
| ④ | 0–14,400: 3.078%; 14,400–30,000: $443 + 3.762%; 30,000–60,000: 1,030 + 3.819%; over 60,000: 2,176 + 3.876% |

---

## 5. The household credits and the school tax credit

### 5.1 New York State household credit, line 40 (`ny_it201i pp. 12–13`)

`ny_it201i p. 12`, Line 40, "If you marked the Yes box at item C on the front of Form IT-201, you do not qualify for
this credit." Tables by status (`ny_it201i-html`, "Filing status ① only (Single): Use New York State household credit
table 1.", "Filing status ②, ④, and ⑤: Use New York State household credit table 2.", and table 3 for ③). The key is
federal AGI: `ny_it201i p. 13`, Note 1, "For most taxpayers, federal adjusted gross income is the amount from Form
IT-201, line 19." (less Build America Bond interest with code A6). "Note 2 This amount could be 0 or a negative amount."

- **Table 1 (single)**, federal AGI over, but not over, amount to enter: (Note 2)–5,000: $75; 5,000–6,000: 60; 6,000–7,000: 50;
  7,000–20,000: 45; 20,000–25,000: 40; 25,000–28,000: 20; over 28,000: "No credit is allowed; do not make an entry on
  Form IT-201, line 40."
- **Table 2 (②④⑤)**, keyed also by "the number of dependents listed on Form IT-201, item H, plus one for you (and one
  for your spouse if Married filing joint return)", columns 1 to 7 and "over 7" ("Note 3 For each individual over 7,
  add the amount in this column to the column 7 amount."). Rows: up to 5,000: 90 105 120 135 150 165 180 (+15);
  5,000–6,000: 75 … 165 (+15); 6,000–7,000: 65 … 155 (+15); 7,000–20,000: 60 … 150 (+15); 20,000–22,000: 60 70 80 90
  100 110 120 (+10); 22,000–25,000: 50 … 110 (+10); 25,000–28,000: 40 45 50 55 60 65 70 (+5); 28,000–32,000: 20 25 30
  35 40 45 50 (+5); over 32,000: no credit.
- **Table 3 (③)** needs the spouse's federal AGI and both returns' dependents (`ny_it201i p. 13`, Note 4, "If your
  spouse was not required to file a New York State return, use your spouse’s federal adjusted gross income as reported
  on their federal return"), amounts halved and rounded ("Note 5 The credit amounts have been rounded."). Ends over
  32,000.

The tables fit `keyed_lookup` (by band index and count) or `table_lookup` per column; "over 7" is an arithmetic
extension (inferred design). Owner relevance: no credit above federal AGI $28,000 (single) or $32,000 (others).

### 5.2 New York City household credit, line 48 (`ny_it201i pp. 13–14`)

`ny_it201i p. 13`, Line 48, "If you marked the Yes box at item C on the front of Form IT-201, you do not qualify for
this credit and should go to line 49." Tables 4 to 6 as 1 to 3 (same Notes 1 to 5):

- **Table 4 (single)**: up to 10,000: $15; 10,000–12,500: 10; over 12,500: no credit.
- **Table 5 (②④⑤)**, by people 1 to 7 and over 7: up to 15,000: 30 60 90 120 150 180 210 (+30); 15,000–17,500: 25 …
  175 (+25); 17,500–20,000: 15 … 105 (+15); 20,000–22,500: 10 … 70 (+10); over 22,500: no credit.
- **Table 6 (③)**: halved and rounded, ends over 22,500.

The PDF prints an asterisk after "17,500*", "20,000*" and "22,500*" in tables 5 and 6 (`ny_it201i.txt` p. 14) with
no footnote on the page; the web edition prints none. Unexplained; recorded, no effect found.

### 5.3 New York City school tax credit, lines 69 and 69a (`ny_it201i pp. 20–21`)

**Fixed amount, line 69.** `ny_it201i p. 20`, Line 69, "If you are a New York City resident or part-year resident and
marked the Yes box at item C on the front of Form IT-201 indicating that you can be claimed as a dependent on another
taxpayer’s federal return, or your income (see below) is more than $250,000, you do not qualify for this credit."
Table 1 for full-year residents: $63 for ① ③ ④ and $125 for ② ⑤ when income is "$250,000 or less" (`ny_it201i-html`,
"Table 1 - Full-year New York City residents"; "*The statutory credit amounts have been rounded."). Income: `ny_it201i
p. 20`, "Income, for purposes of determining your New York City school tax credit, means your federal adjusted gross
income from Form IT-201, line 19, minus distributions from an individual retirement account and an individual
retirement annuity, from Form IT-201, line 9, if they were included in your federal adjusted gross income." In project
terms: line 19 less line 9 (inferred: line 9 is the taxable, included amount).

**Rate reduction amount, line 69a.** `ny_it201i p. 20`, Line 69a, "or your income (see below) is more than $500,000,
you do not qualify to claim this credit." Then (`p. 21`) "use your New York City taxable income (see below) to calculate
your credit." For a full-year resident, "use the amount from Form IT-201, line 47." Tables (`ny_it201i-html`,
"Calculation of NYC school tax credit (rate reduction amount)"):

| status | city taxable income over – not over | credit |
| --- | --- | --- |
| ② ⑤ | 0 – 21,600 | 0.171% of taxable income |
| ② ⑤ | 21,600 – 500,000 | $37 plus 0.228% of the excess over $21,600 |
| ① ③ | 0 – 12,000 | 0.171% |
| ① ③ | 12,000 – 500,000 | $21 plus 0.228% of the excess over $12,000 |
| ④ | 0 – 14,400 | 0.171% |
| ④ | 14,400 – 500,000 | $25 plus 0.228% of the excess over $14,400 |

**Ambiguity (69a).** The $500,000 eligibility test reads "your income (see below)", but the text below line 69a
defines only "New York City taxable income"; the definition of "income" is printed above, under line 69. Two readings:
(a) the line-69 income (federal AGI less IRA distributions), (b) New York City taxable income. They differ when one is
above $500,000 and the other not, and the tables stop at $500,000 of city taxable income. Not resolvable from the
archive (the statute, NYC Administrative Code, is not archived). Proposed: register it and refuse when either is above
$500,000 (DECISIONS D14).

Rounding: 0.171% of a taxable income is not a whole-dollar amount; the whole-dollar rule (section 2) applies (D8).

---

## 6. Refusal screens the target needs

Each screen is a question whose Yes refuses, with the IT-201-I page it cites. The wording is proposed, not final.

| screen | proposed question | cite | refuses |
| --- | --- | --- | --- |
| residency (State) | 'Were you a New York State resident for all of 2025 (domiciled in New York, or keeping a permanent place of abode there and spending 184 days or more there)?' No refuses | `ny_it201i p. 3`, "If you were a New York State resident for only part of the year, do not file Form IT-201."; `p. 30`, Resident | Form IT-203 |
| residency (City) | 'Were you a New York City resident for all of 2025?' No refuses (part-year: IT-360.1; nonresident: no city tax) | `ny_it201i p. 31`, New York City and Yonkers, "substitute New York City or Yonkers in place of New York State"; `p. 14`, Line 50 | Form IT-360.1 or a non-City return |
| spouse residency | on a joint return: 'Was your spouse also a full-year New York State and New York City resident?' No refuses | `ny_it201i p. 4`, Item A exceptions; `p. 14`, Line 51 joint returns | separate New York returns; the line 51 separate-sheet computation |
| special accruals | 'Were you a New York City nonresident on December 31, 2024, or will you be a nonresident on January 1, 2026, and have accrued income?' Yes refuses | `ny_it201i p. 31`, Special accruals | IT-225 A-115 / S-129 |
| Yonkers | item D2 | `ny_it201i p. 5`, Item D2 | Yonkers lines 55 to 57 |
| itemizing | 'Do you want to itemize deductions on your New York return?' Yes refuses | `ny_it201i p. 11`, step 2, Form IT-196 | Form IT-196 |
| other additions and subtractions | 'Do any New York additions or subtractions on Form IT-225 apply to you?' with the common cases named (out-of-state municipal bond interest beyond line 20; partnership, S corporation or trust modifications; ...) | `ny_it201i pp. 7–10`, Lines 23 and 31 | Form IT-225 |
| additions and subtractions on the face of the form | lines 20, 21, 22, 26, 28, 29, 30: one question each, refused or computed per D5 | `ny_it201i pp. 7–10` | — |
| credits needing a form | 'Do you claim any New York credit other than the household credits and the New York City school tax credit (for example the resident credit for taxes paid to another state, the Empire State child credit, the child and dependent care credit, the earned income credit, the real property tax credit, the college tuition credit, the NYC income tax elimination credit)?' plus the tests that make some of them apply without asking (line 63: a dependent under 17; lines 65 and 70: federal EIC; line 70a: dependents and income) | `ny_it201i p. 2`, "To claim a tax credit (with the exception of the household credit and New York City school tax credit), you must complete and submit the appropriate credit form." | IT-112-R, IT-201-ATT, IT-213, IT-216, IT-215, IT-209, IT-214, IT-272, IT-270 |
| other taxes | 'Did you receive a lump-sum distribution taxed on federal Form 4972, or owe any other New York tax on Form IT-201-ATT Part 2 or 3?' | `ny_it201i p. 13`, Line 45; `p. 14`, Line 51 | IT-201-ATT, IT-230 |
| MCTMT | 'Did you (or your spouse) have net earnings from self-employment of more than $50,000 allocated to New York City (MCTD Zone 1) or Zone 2?' | `ny_it201i p. 15`, "Did you or your spouse have net earnings from self-employment allocated to Zone 1 or Zone 2, or both that exceed $50,000?" | lines 54a–54e, unless computed (D7) |
| special condition code A6 | 'Did you include Build America Bond interest in federal AGI?' | `ny_it201i p. 5`, Code A6 | the household-credit income adjustment |
| estimated tax penalty | per D12 | `ny_it201i p. 23`, Line 81 | IT-2105.9 |

The federal encoding's own screens run first; a federal refusal already refuses the New York return (inferred design).

---

## 7. Checklist for the owner (last year's IT-201)

Lines of the owner's tax-year 2025 IT-201 (or the 2024 one if that is the latest filed) to look at, each with what a
nonzero amount or a box would mean. Line numbers are the 2025 form's; the owner reads them and answers in
`docs/ny/DECISIONS.md` by typing, never by sending the return.

1. **Item A, filing status.** Anything but ① single changes which tables apply; ③ married filing separately needs the
   spouse's federal AGI and dependents for the household credits (table 3, 6).
2. **Item C.** Yes: the $3,100 single deduction and no household or school tax credit.
3. **Item D2, E, F.** D2 Yes: Yonkers, refused. E filled in or F less than 12: not a full-year City resident, refused.
4. **Item G.** Any code. A6 changes the household credits; the others are listed in section 3.1.
5. **Item H.** Any dependent: line 36, the household-credit column, line 63 (under 17), line 70a.
6. **Lines 20 to 23, 25 to 31.** Any amount: line 20 (out-of-state municipal interest), 21 (414(h)), 22 (529
   nonqualified), 23 or 31 (IT-225), 25 (inflation refund check), 26 (public pension), 28 (U.S. bond interest), 29
   (pension exclusion), 30 (529 contributions). Each nonzero line is either in scope by a D5 decision or a refusal.
7. **Line 33 against $107,650.** Above it, the recapture worksheets apply (in scope either way).
8. **Line 34 box.** Itemized: outside the target.
9. **Lines 40 and 48.** Nonzero: the household credits applied (federal AGI was under $32,000 or $22,500).
10. **Lines 41, 42, 45, 51, 53.** Nonzero: a credit or tax on IT-112-R or IT-201-ATT; refused.
11. **Lines 54a to 54e.** Nonzero: MCTMT (D7).
12. **Line 59.** The amount reported (0 or a chart amount): which way D3 should go.
13. **Line 60, 78a.** Voluntary contributions or a 529 deposit (D13).
14. **Lines 63 to 68, 70, 70a, 71.** Nonzero: a credit outside the target; refused.
15. **Lines 69 and 69a.** Expected nonzero for a full-year City resident who is not a dependent (the fixed $63 or $125
    and the rate reduction). Zero would mean item C Yes or income over the limits.
16. **Lines 72 to 75.** Which kinds of withholding appear (W-2 only, or also 1099-R, 1099-G, W-2G) and whether
    estimated payments were made (D2).
17. **Line 81.** Nonzero: an estimated tax penalty (D12).

---

## 8. Open items the text leaves undecided (for the ambiguity register at authoring)

1. Line 25 against line 4 (section 3.4; D6).
2. The 69a "income (see below)" reading (section 5.3; D14).
3. Rounding: where whole dollars are taken, and the direction of "round the result to the fourth decimal place" (D8).
4. Item C against the federal "can be claimed" exception (D9).
5. Lines 65 and 70, "or could you have claimed it based on your federal adjusted gross income?" (D10).
6. The asterisks of household credit tables 5 and 6 (section 5.2), no effect found.
7. Whether line 17 must equal `f1040.line9` and line 19 `f1040.line11a` exactly or after whole-dollar rounding (D4,
   D8).

## 9. Verified versus inferred

**Verified** (quoted from the archived pages and checked by script): every double-quoted string above, at its
locator; the federal ids named (present in `forms/2025/` on this branch: `f1040.line1z`, `line2a`, `line2b`, `line3b`,
`line4b`, `line5b`, `line6b`, `line7a`, `line9`, `line10`, `line11a`, `line27a`, `f1040.status`, `s1.line1`, `line2a`,
`line3`, `line7`, `line9`, `line26`, `sa.itemizes`, `sa.dependent`, `sb.line7a`, `div.box12`, `interest.amount`,
`dependent.claimed`, `f8962.deps`, `scope.schedule1`).

**Inferred** (marked where made): the federal-line mapping of IT-201 lines 2 to 18 from labels; line 17 equal to
`f1040.line9`; a blank line 37 read as zero; the coverage of the tax computation worksheets; `dependent.claimed` as
item H's "entitled to claim"; the design fits to project atoms; that school-tax "income" subtracts the taxable IRA
amount on line 9.
