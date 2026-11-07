# Render comparison — ny_it201

The rendered English of every printed line of `Form IT-201 (2025), Resident Income Tax Return — New York State and New York City` (`rendered/ny/2025/ny_it201.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-04 |
| line-scoped reviews | 3 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 81d9fe83915746ba73187579ffca2b953cfb6545ea4e32efd364d62173e181a5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 390d22ff0e196470cf6119d363b160934f85d1c37fcc6196dd053b2d9797cb11 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 446aa9d889a2b5621e01ece80ccbb9df74d330db1e7cb0822188e8736c9e8bce |
| lines judged | 168 |
| match / mismatch / unclear / missing | 161 / 6 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 3, 4, 5, 6, 7, 8, 9, 10, 15, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: All others:; Calculation of NYC school tax credit (rate reduction amount) for head of household ④; Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤; Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③; Joint returns; Line 40: New York State household credit; New York City household credit table 4—Filing status ① only (Single); New York City household credit table 5—Filing status ②, ④, and ⑤; New York City tax rate schedule; New York State household credit table 1—Filing status ① only (Single); New York State household credit table 2—Filing status ②, ④, and ⑤; New York State standard deduction table; New York State tax rate schedule; Table 1 - Full-year New York City residents: New York City school tax credit table; Tax computation worksheet 1; Tax computation worksheet 10; Tax computation worksheet 12; Tax computation worksheet 13; Tax computation worksheet 14; Tax computation worksheet 15; Tax computation worksheet 2; Tax computation worksheet 3; Tax computation worksheet 4; Tax computation worksheet 5; Tax computation worksheet 6; Tax computation worksheet 7; Tax computation worksheet 8; Tax computation worksheet 9; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it270i | Form IT-270-I, Instructions for Form IT-270, New York City Income Tax Elimination Credit, for tax year 2025 (no printed edition line; address /pdf/2025/inc/, PDF metadata Title '... Tax Year 2025'); PDF modified 2025-10-27 | 1 | whole document | 66b713fa6ae58aafa2189310ed7d140b64c05d2c8bf2958a9651af7751ae15d5 | - | cc437e692bd1fcdbcc44f0e850e95f1cacee9a0e3285396d87e580ca559e082c |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| ny_it2 | Form IT-2 (2025), Summary of W-2 Statements; final 2025 edition (footer 'IT-2 (2025) (back)'); PDF modified 2025-09-26 | 1, 2 | whole document | 4884d0d4403f8d1f3bd71a6834951e51fca1ca288ff3ecbab3c6866a286c10b8 | 2 | a6e61a9d7a0cd5464a36232dae9d0f4d5ca5380323f1117a2077f7e621049739 |
| i1040gi | 2025; printed date 2026-02-25 | 40, 42, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 42 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **MATCH**

Model: Item C asks whether you can be claimed as a dependent, and the instructions say to mark Yes 'even if the other taxpayer did not claim you'. The helper asks exactly that.

### H (count) — Number of dependents listed in item H
Status: **MATCH**

Model: Counts the dependents entered in item H. Line 36 multiplies 'the number of dependents listed in item H' by 1,000.

### 1 — Wages, salaries, tips, etc.
Status: **UNCLEAR**

Restated: Round f1040 line 1z to the nearest multiple of (half up) $1.

Model: The form prints line 1 as 'Wages, salaries, tips, etc.' under 'Federal income and adjustments' with 'Whole dollars only', but the pages given contain no line 1 instruction. Nothing here says the amount is federal Form 1040 line 1z or how to round to whole dollars (half up or otherwise). The refusals are consistent with the text given.

Ruling: interface gap; ny_it201i p. 7, Lines 1 through 19, "The amount entered on line 1 (wages, salaries, tips, etc.) should be the same as the amount reported on federal Form 1040, line 1z." The line-scoped request (rerun because line 1's refusals read the restructured ny_it201.ask.state_resident) gave only the pages its citations name, and line 1 cites only the form page, so p. 7 was not given; the restatement follows it, rounded half up by amb.ny.2025.whole_dollars (IT-201-I p. 2, whole dollars). The model found the refusals consistent with the text. Citation gap: BUG-0439. Project stands.
Reviewed in: pass d4a19f82147a

### 2 — Taxable interest income
Status: **MATCH**

Model: 'Taxable interest income' is federal Form 1040 line 2b, in whole dollars.

### 3 — Ordinary dividends
Status: **MATCH**

Model: 'Ordinary dividends' is federal Form 1040 line 3b.

### 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter on line 2
Status: **MATCH**

Model: 'Taxable refunds, credits, or offsets of state and local income taxes' is Schedule 1 line 1.

### 5 — Alimony received
Status: **MATCH**

Model: 'Alimony received' is Schedule 1 line 2a.

### 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **MATCH**

Model: 'Business income or loss' is Schedule 1 line 3.

### 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 1040)
Status: **MATCH**

Model: 'Capital gain or loss' is federal Form 1040 line 7a.

### 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **MISMATCH**

Restated: Enter $0 (ny.zero).

Model: The form asks for 'Other gains or losses (submit a copy of federal Form 4797)'. The program always enters $0, and no refusal names Form 4797 gains. Only the line 19 check against federal AGI would catch a nonzero amount.

Ruling: model error; the line is zero because the federal return it copies cannot hold Form 4797 gains or losses: this tool refuses it on the federal return (scope.schedule1, "Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately"; the federal encoding has no Schedule 1 line 4 ("Other gains or (losses). Check if any from Form(s): ... 4797"); f1040s1 p. 1), and the New York return is computed only from a computed federal return. The rendering's note says so. Not a defect.

### 9 — Taxable amount of IRA distributions
Status: **MATCH**

Model: 'Taxable amount of IRA distributions' is federal Form 1040 line 4b.

### 10 — Taxable amount of pensions and annuities
Status: **MATCH**

Model: 'Taxable amount of pensions and annuities' is federal Form 1040 line 5b.

### 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **MISMATCH**

Restated: Enter $0 (ny.zero).

Model: The form asks for 'Rental real estate, royalties, partnerships, S corporations, trusts, etc. (submit copy of federal Schedule E)'. The program always enters $0, and no refusal names Schedule E income.

Ruling: model error; the line is zero because the federal return it copies cannot hold Schedule E income: this tool refuses it on the federal return (scope.schedule1, "Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately"; the federal encoding has no Schedule 1 line 5 ("Rental real estate, royalties, partnerships, S corporations, trusts, etc. Attach Schedule E"); f1040s1 p. 1), and the New York return is computed only from a computed federal return. The rendering's note says so. Not a defect.

### 12 — Rental real estate included in line 11
Status: **MISMATCH**

Restated: Enter $0 (ny.zero).

Model: The form asks for 'Rental real estate included in line 11'. This is fixed at $0 with no refusal for rental income, so it is wrong whenever line 11 should include rental real estate.

Ruling: model error; line 12 is the rental real estate included in line 11, and line 11 is always zero because the federal return refuses Schedule E (scope.schedule1; no federal Schedule 1 line 5), so line 12 is zero too. Not a defect.

### 13 — Farm income or loss
Status: **MISMATCH**

Restated: Enter $0 (ny.zero).

Model: The form asks for 'Farm income or loss (submit a copy of federal Schedule F)'. The program always enters $0, and no refusal names farm income.

Ruling: model error; the line is zero because the federal return it copies cannot hold Schedule F income: this tool refuses it on the federal return (scope.schedule1, "Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately"; the federal encoding has no Schedule 1 line 6 ("Farm income or (loss). Attach Schedule F"); f1040s1 p. 1), and the New York return is computed only from a computed federal return. The rendering's note says so. Not a defect.

### 14 — Unemployment compensation
Status: **MATCH**

Model: 'Unemployment compensation' is Schedule 1 line 7.

### 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **MATCH**

Model: 'Taxable amount of Social Security benefits' is federal Form 1040 line 6b.

### 16 — Other income
Status: **MATCH**

Model: 'Other income' is Schedule 1 line 9, total other income.

### 17 — Add lines 1 through 11 and 13 through 16
Status: **MATCH**

Model: The form says 'Add lines 1 through 11 and 13 through 16'. The restatement adds the same lines and leaves out line 12.

### 18 — Total federal adjustments to income
Status: **MATCH**

Model: 'Total federal adjustments to income' is Schedule 1 line 26.

### 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **MATCH**

Model: The form says 'subtract line 18 from line 17'.

### (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **MATCH**

Model: Line 19 is labelled 'Federal adjusted gross income', so comparing it with Form 1040 line 11a is consistent with the form.

### 20 — Interest income on state and local bonds and obligations (but not those of NYS or its loca
Status: **MATCH**

Model: Zero unless the filer has out-of-state bond interest. That case is refused.

### 21 — Public employee 414(h) retirement contributions from your wage and tax statements
Status: **MATCH**

Model: Zero unless the filer has 414(h) contributions. That case is refused.

### 22 — New York’s 529 college savings program distributions
Status: **MATCH**

Model: Zero unless the filer made a nonqualified New York 529 withdrawal. That case is refused.

### 23 — Other (Form IT-225, line 9)
Status: **MATCH**

Model: Zero unless Form IT-225 modifications apply. That case is refused.

### 24 — Add lines 19 through 23
Status: **MATCH**

Model: The form says 'Add lines 19 through 23'.

### 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line 4)
Status: **MATCH**

Model: Zero, and the program refuses whenever line 4 is above zero or an inflation refund check was included. That covers both the form's 'from line 4' and the instructions' inflation-check reading.

### 26 — Pensions of NYS and local governments and the federal government
Status: **MATCH**

Model: The tool enters $0 and refuses whenever line 9 or 10 shows pension or IRA income and the filer reports a NYS, local or federal government pension, which covers what the line 26 instruction allows to be subtracted. The question also names the listed authorities, the ORP and the domestic-relations-order spouses.
Reviewed in: pass aafab4291976

### 27 — Taxable amount of Social Security benefits (from line 15)
Status: **MATCH**

Model: The form says 'Taxable amount of Social Security benefits (from line 15)'.

### 28 — Interest income on U.S. government bonds
Status: **MATCH**

Model: The tool enters $0 and refuses whenever lines 2, 3, 6 or 11 show income and the filer included interest on U.S. government obligations or dividends from a fund holding them. That covers the instruction's 'interest income from U.S. government bonds or other U.S. government obligations on lines 2, 6, or 11' and its qualifying mutual-fund dividends.
Reviewed in: pass aafab4291976

### 29 — Pension and annuity income exclusion
Status: **MATCH**

Model: The tool enters $0 and refuses whenever line 9 or 10 shows pension income that is not a government pension and the recipient was 59½ or older during 2025 or received it as a beneficiary. This covers every case where the instruction allows an exclusion ('59½ before January 1, 2025' or 'became 59½ during 2025').
Reviewed in: pass aafab4291976

### 30 — New York’s 529 college savings program deduction/earnings
Status: **MATCH**

Model: Zero unless the filer has New York 529 contributions or withdrawals. That case is refused.

### 31 — Other (Form IT-225, line 18)
Status: **MATCH**

Model: Zero unless Form IT-225 subtractions apply. That case is refused.

### 32 — Add lines 25 through 31
Status: **MATCH**

Model: The form says 'Add lines 25 through 31'.

### 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **MATCH**

Model: The form says 'subtract line 32 from line 24'.

### (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **MATCH**

Model: Matches the standard deduction table: Single (item C No) 8,000; joint 16,050; separate 8,000; head of household 11,200; qualifying surviving spouse 16,050.

### (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **MATCH**

Model: The table gives 'Single and you marked item C Yes' as $3,100.

### 34 — Enter your standard deduction
Status: **MATCH**

Model: Picks the standard deduction for the filer's status and item C answer. Itemizing is refused through the Form IT-196 gate.

### 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **MATCH**

Model: The form says 'Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)'.

### 36 — Dependent exemption amount (multiply the number of dependents listed in item H by 1,000)
Status: **MATCH**

Model: The form says 'multiply the number of dependents listed in item H by 1,000', and the exemption is $1,000.

### 37 — Taxable income (subtract line 36 from line 35)
Status: **MATCH**

Model: Line 36 is subtracted from line 35. The instructions leave the line blank if line 36 is more than line 35, which comes to the same zero.

### 38 — Taxable income (from line 37 on page 2)
Status: **MATCH**

Model: The instructions say to enter the taxable income on both line 37 and line 38.

### (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **MATCH**

Model: The instructions say to use the 2025 New York State Tax Table when line 38 is below $65,000.

### (39) (ny_it201.tax_schedule) — New York State tax from the New York State tax rate schedule
Status: **MATCH**

Model: The rate schedule bands, base amounts and rates in the glossary match the printed schedules for all filing statuses.

### (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable income, t
Status: **MATCH**

Model: The instructions say to use the 2025 New York State Tax Table, or 'if line 38 is $65,000 or more, use the New York State tax rate schedule.' The restatement uses the table when line 38 is under $65,000 and the schedule otherwise, which is the same rule.
Reviewed in: pass b59076746e74

### (39) (ny_it201.tcw.w1) — Tax computation worksheet 1
Status: **MATCH**

Model: Worksheet 1 has a 5.5% flat rate, the Stop at $157,650, the excess over $107,650 divided by $50,000 and rounded to four decimals, and line 9 as line 4 plus line 8. The restatement follows all of these.

### (39) (ny_it201.tcw.w7) — Tax computation worksheet 7
Status: **MATCH**

Model: Worksheet 7 has the same structure as worksheet 1, with a 6% rate.

### (39) (ny_it201.tcw.w12) — Tax computation worksheet 12
Status: **MATCH**

Model: Worksheet 12 has the same structure as worksheet 1, with a 6% rate.

### (39) (ny_it201.tcw.w2) — Tax computation worksheet 2
Status: **MATCH**

Model: Worksheet 2 prints Recapture Base 333, Incremental Benefit 807 and excess over $161,550, all as restated.

### (39) (ny_it201.tcw.w3) — Tax computation worksheet 3
Status: **MATCH**

Model: Worksheet 3 prints Recapture 1,140, Incremental 2,747 and excess over $323,200, all as restated.

### (39) (ny_it201.tcw.w4) — Tax computation worksheet 4
Status: **MATCH**

Model: Worksheet 4 prints Recapture 3,887, Incremental 60,350 and excess over $2,155,350, all as restated.

### (39) (ny_it201.tcw.w5) — Tax computation worksheet 5
Status: **MATCH**

Model: Worksheet 5 prints Recapture 64,237, Incremental 32,500 and excess over $5,000,000, all as restated.

### (39) (ny_it201.tcw.w8) — Tax computation worksheet 8
Status: **MATCH**

Model: Worksheet 8 prints Recapture 568, Incremental 1,831 and excess over $215,400, all as restated.

### (39) (ny_it201.tcw.w9) — Tax computation worksheet 9
Status: **MATCH**

Model: Worksheet 9 prints Recapture 2,399, Incremental 30,172 and excess over $1,077,550, all as restated.

### (39) (ny_it201.tcw.w10) — Tax computation worksheet 10
Status: **MATCH**

Model: Worksheet 10 prints Recapture 32,571, Incremental 32,500 and excess over $5,000,000, all as restated.

### (39) (ny_it201.tcw.w13) — Tax computation worksheet 13
Status: **MATCH**

Model: Worksheet 13 prints Recapture 787, Incremental 2,289 and excess over $269,300, all as restated.

### (39) (ny_it201.tcw.w14) — Tax computation worksheet 14
Status: **MATCH**

Model: Worksheet 14 prints Recapture 3,076, Incremental 45,261 and excess over $1,616,450, all as restated.

### (39) (ny_it201.tcw.w15) — Tax computation worksheet 15
Status: **MATCH**

Model: Worksheet 15 prints Recapture 48,337, Incremental 32,500 and excess over $5,000,000, all as restated.

### (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.9%
Status: **MATCH**

Model: Worksheets 6, 11 and 16 say 'Multiply line 1 by 10.9% (0.109)', where line 1 is the taxable income from line 38.

### (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the taxable inco
Status: **MATCH**

Model: The taxable-income bands match worksheets 1 to 5: $161,550 or less; over $161,550 to $323,200; over $323,200 to $2,155,350; over $2,155,350 to $5,000,000; over $5,000,000. Each worksheet's AGI floor is implied because line 38 cannot exceed line 33, and the AGI conditions over $107,650 and up to $25,000,000 are handled by the parent choices.
Reviewed in: pass b59076746e74

### (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **MATCH**

Model: The bands match worksheets 7 to 10: $215,400 or less; over $215,400 to $1,077,550; over $1,077,550 to $5,000,000; over $5,000,000. The AGI conditions are handled by the parent choices.
Reviewed in: pass b59076746e74

### (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **MATCH**

Model: The bands match worksheets 12 to 15: $269,300 or less; over $269,300 to $1,616,450; over $1,616,450 to $5,000,000; over $5,000,000. The AGI conditions are handled by the parent choices.
Reviewed in: pass b59076746e74

### (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **MATCH**

Model: The worksheet groups are 'Married filing jointly and qualifying surviving spouse', 'Single and married filing separately' and 'Head of household', and the mapping follows them. The program reads the filing status from the federal return rather than from IT-201 item A; the mapping is correct either way.
Reviewed in: pass b59076746e74

### (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **MATCH**

Model: Worksheets 6, 11 and 16 apply 'If your New York adjusted gross income (line 33) is more than $25,000,000'. Otherwise the worksheet for the filer's filing status applies.
Reviewed in: pass b59076746e74

### 39 — NYS tax on line 38 amount
Status: **MATCH**

Model: This follows 'Is line 33 (your New York adjusted gross income) $107,650 or less? If Yes, ... Tax Table ... or rate schedule ... If No, see Tax computation – New York adjusted gross income of more than $107,650.'
Reviewed in: pass b59076746e74

### (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negative amount
Status: **MATCH**

Model: Note 1 says federal adjusted gross income is line 19, and code A6 is refused. Flooring at zero does not change any lookup, because the first row of each table covers 0 or negative amounts (Note 2).

### (column) — The number of dependents listed in item H, plus one for you (and one for your spouse if ma
Status: **MATCH**

Model: The column is 'the number of dependents listed on Form IT-201, item H, plus one for you (and one for your spouse if Married filing joint return)'.

### (table 2, column 1) — New York State household credit table 2, column 1
Status: **MATCH**

Model: Table 2, column 1 values (90, 75, 65, 60, 60, 50, 40, 20) are looked up by federal AGI.

### (table 5, column 1) — New York City household credit table 5, column 1
Status: **MATCH**

Model: Table 5, column 1 values (30, 25, 15, 10) are looked up by federal AGI.

### (table 2, column 2) — New York State household credit table 2, column 2
Status: **MATCH**

Model: Table 2, column 2 lookup.

### (table 5, column 2) — New York City household credit table 5, column 2
Status: **MATCH**

Model: Table 5, column 2 lookup.

### (table 2, column 3) — New York State household credit table 2, column 3
Status: **MATCH**

Model: Table 2, column 3 lookup.

### (table 5, column 3) — New York City household credit table 5, column 3
Status: **MATCH**

Model: Table 5, column 3 lookup.

### (table 2, column 4) — New York State household credit table 2, column 4
Status: **MATCH**

Model: Table 2, column 4 lookup.

### (table 5, column 4) — New York City household credit table 5, column 4
Status: **MATCH**

Model: Table 5, column 4 lookup.

### (table 2, column 5) — New York State household credit table 2, column 5
Status: **MATCH**

Model: Table 2, column 5 lookup.

### (table 5, column 5) — New York City household credit table 5, column 5
Status: **MATCH**

Model: Table 5, column 5 lookup.

### (table 2, column 6) — New York State household credit table 2, column 6
Status: **MATCH**

Model: Table 2, column 6 lookup.

### (table 5, column 6) — New York City household credit table 5, column 6
Status: **MATCH**

Model: Table 5, column 6 lookup.

### (table 2, column 7) — New York State household credit table 2, column 7
Status: **MATCH**

Model: Table 2, column 7 lookup.

### (table 5, column 7) — New York City household credit table 5, column 7
Status: **MATCH**

Model: Table 5, column 7 lookup.

### (table 2) — New York State household credit table 2 for the number of people (column 7 for 7 or more)
Status: **MATCH**

Model: Picks the column for a count of 1 to 7. Counts over 7 (Note 3) are refused through the over-7 gate.

### (table 5) — New York City household credit table 5 for the number of people (column 7 for 7 or more)
Status: **MATCH**

Model: Picks the column for a count of 1 to 7. Counts over 7 are refused.

### (table 1) — New York State household credit table 1 (single)
Status: **MATCH**

Model: Table 1 (Single only) is looked up by federal AGI: 75, 60, 50, 45, 40, 20, then none over 28,000.

### (table 4) — New York City household credit table 4 (single)
Status: **MATCH**

Model: Table 4 (Single only) gives 15 up to $10,000, 10 up to $12,500, and none above.

### (40) — The state household credit table for the filing status
Status: **MATCH**

Model: Single uses table 1; statuses 2, 4 and 5 use table 2. Married filing separately (table 3) is zero only where no credit is allowed and is otherwise refused.

### (48) — The city household credit table for the filing status
Status: **MATCH**

Model: Single uses table 4; statuses 2, 4 and 5 use table 5. Married filing separately (table 6) is refused where a credit is allowed.

### 40 — NYS household credit
Status: **MATCH**

Model: The instructions say 'If you marked the Yes box at item C ... you do not qualify for this credit', and otherwise to use the tables.

### 41 — Resident credit
Status: **MATCH**

Model: Zero unless the filer paid tax to another state or province. That case is refused, routing to Form IT-112-R.

### 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **MATCH**

Model: Zero unless other credits apply. That case is refused, routing to Form IT-201-ATT.

### 43 — Add lines 40, 41, and 42
Status: **MATCH**

Model: The form says 'Add lines 40, 41, and 42'.

### 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **MATCH**

Model: The form says 'Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)'.

### 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **MATCH**

Model: Zero unless other taxes apply. That case is refused, routing to Form IT-201-ATT Part 2.

### 46 — Total New York State taxes (add lines 44 and 45)
Status: **MATCH**

Model: The form says 'add lines 44 and 45'.

### 47 — NYC taxable income
Status: **MATCH**

Model: The instructions say to enter the line 38 amount unless an itemized Charitable Gifts Trust contribution was claimed. Itemizing is refused, so that exception cannot arise.

### (47a) (ny_it201.city_tax_table) — New York City resident tax from the 2025 New York City Tax Table
Status: **MATCH**

Model: The instructions say to use the 2025 New York City Tax Table if line 47 is less than $65,000.

### (47a) (ny_it201.city_tax_schedule) — New York City resident tax from the New York City tax rate schedule
Status: **MATCH**

Model: The city rate schedule bands, bases (369/858/1,813; 665/1,545/3,264; 443/1,030/2,176) and rates match the printed schedule.

### 47a — NYC resident tax on line 47 amount
Status: **MATCH**

Model: The instructions ask 'Is line 47 ... less than $65,000?' If Yes, use the table; if No, use the rate schedule.

### 48 — NYC household credit
Status: **MATCH**

Model: Item C Yes means no credit; otherwise tables 4 and 5 apply, and table 6 and counts over 7 are refused.

### 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **MATCH**

Model: The form says 'Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)'.

### 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **MATCH**

Model: The part-year city resident tax is zero because part-year city residents are refused (Form IT-360.1).

### 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **MATCH**

Model: Zero unless other city taxes apply, which is refused. The one-spouse-resident case is refused through the spouse gate.

### 52 — Add lines 49, 50, and 51
Status: **MATCH**

Model: The form says 'Add lines 49, 50, and 51'.

### 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **MATCH**

Model: Zero unless city nonrefundable credits apply. That case is refused.

### 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **MATCH**

Model: The form says 'Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)'.

### 54a — MCTMT net earnings base for Zone 1
Status: **MISMATCH**

Restated: Enter $0 (ny.zero).

Model: The screening question is asked only of people with more than one Schedule C or Schedule C profit over $50,000, so other self-employment earnings get $0 with no refusal. The instructions say MCTMT net earnings include amounts on 'federal Schedule SE (Form 1040), Part 1, line 6', including IRC § 1402 income such as 'services performed by a United States citizen employed by a foreign government, the United Nations, or other international organization', which need not come from a Schedule C.

Ruling: scope; self-employment income other than Schedule C is refused on the federal return before New York is reached (a refused federal return is a refused New York return, interview/ny/2025.yaml targets_from): scope.schedule1 refuses partnerships and other Schedule K-1 income, farm income (Schedule F), church employee income and income as a minister; scope.other_income refuses "wages or tips not on a Form W-2" and "other earned income (Form 1040 lines 1b to 1d and 1f to 1h)" (the salary of a U.S. citizen employed by a foreign government or an international organization comes without a Form W-2); person.se_screen refuses "other self-employment income not on a Schedule C" and income "earned as a U.S. citizen employed by a foreign government". Within the tool Schedule C is the only source, which ny_it201.mctmt_people reads (its note says so).
Reviewed in: pass aafab4291976

### 54b — MCTMT net earnings base for Zone 2
Status: **MISMATCH**

Restated: Enter $0 (ny.zero).

Model: The same screen is used as for line 54a, so Zone 2 self-employment earnings from sources other than Schedule C get $0 without a refusal. The instructions treat IRC § 1402 income reported on 'federal Schedule SE (Form 1040), Part 1, line 6' as net earnings 'subject to the MCTMT'.

Ruling: scope; as line 54a: every source of self-employment income other than Schedule C is refused federally, so the condition's reading of Schedule C alone drops no Zone 2 amount the tool can reach.
Reviewed in: pass aafab4291976

### 54c — MCTMT for Zone 1
Status: **MATCH**

Model: The instructions say 'Multiply the amount on line 54a by 0.60% (0.0060)'.

### 54d — MCTMT for Zone 2
Status: **MATCH**

Model: The instructions say 'Multiply the amount on line 54b by 0.34% (0.0034).' Rounding to whole dollars agrees with the form's 'Whole dollars only' and with the example '$57,000 x 0.0034 = $194'.
Reviewed in: pass b59076746e74

### 54e — Total MCTMT (add lines 54c and 54d)
Status: **MATCH**

Model: The form says 'add lines 54c and 54d'.

### 55 — Yonkers resident income tax surcharge
Status: **MATCH**

Model: Zero, because Yonkers living quarters or wages are refused.

### 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **MATCH**

Model: Zero, because Yonkers wages are refused.

### 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **MATCH**

Model: Zero, because Yonkers part-year residence is refused.

### 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 54e through
Status: **MATCH**

Model: The form says 'add lines 54 and 54e through 57'.

### (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **MATCH**

Model: The chart gives 'up to $15,000 ... $3'.

### (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **MATCH**

Model: The chart gives '$15,001 - $30,000 ... 6'.

### (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **MATCH**

Model: The chart gives '30,001 - 50,000 ... 10'.

### (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **MATCH**

Model: The chart gives '50,001 - 75,000 ... 15'.

### (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **MATCH**

Model: The chart gives '75,001 - 100,000 ... 18'.

### (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **MATCH**

Model: The chart gives '100,001 - 150,000 ... 26'.

### (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **MATCH**

Model: The chart gives '150,001 - 200,000 ... 34'.

### (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **MATCH**

Model: The chart gives '0.0175% (0.000175) of income' for incomes over $200,000.

### (chart) (ny_it201.sut.cap) — $125
Status: **MATCH**

Model: The chart gives '$125, whichever amount is smaller'.

### (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **MATCH**

Model: Takes the smaller of the 0.0175% product and $125, as the chart says.

### (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; zero or a n
Status: **MATCH**

Model: The bands are keyed on federal AGI from line 19 at the printed whole-dollar break points.

### 59 — Sales or use tax (do not leave blank)
Status: **MATCH**

Model: The instructions say 'If you do not owe any sales or use tax, you must enter 0'; otherwise use the chart. The part-year abode and Form ST-141 cases are refused.

### 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **MATCH**

Model: Zero unless the filer wants to make voluntary contributions. That case is refused (Form IT-227).

### 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and voluntary
Status: **MATCH**

Model: The form says 'add lines 46, 58, 59, and 60'.

### 62 — Enter amount from line 61
Status: **MATCH**

Model: The form says 'Enter amount from line 61'.

### 63 — Empire State child credit
Status: **MATCH**

Model: Zero when there is no child under 17, and refused otherwise, matching the instruction to complete Form IT-213 only with a qualifying child under 17.

### 64 — NYS/NYC child and dependent care credit
Status: **MATCH**

Model: The tool enters $0 and refuses whenever the filer had care expenses or benefits and 'Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you actually claimed it)?' is answered yes. That is the instruction's own test for completing Form IT-216.
Reviewed in: pass aafab4291976

### 65 — NYS earned income credit (EIC)
Status: **MATCH**

Model: Refused if the federal EIC was claimed or federal AGI is below the EIC limit ('could you have claimed it based on your federal adjusted gross income'). Otherwise zero.

### 66 — NYS noncustodial parent EIC
Status: **MATCH**

Model: Zero unless child support was paid through a Support Collection Unit. That case is refused.

### 67 — Real property tax credit
Status: **MATCH**

Model: Zero unless the filer might qualify for the real property tax credit. That case is refused (Form IT-214).

### 68 — College tuition credit
Status: **MATCH**

Model: Zero unless college tuition was paid. That case is refused (Form IT-272).

### (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions included i
Status: **MATCH**

Model: Income here 'means your federal adjusted gross income from Form IT-201, line 19, minus distributions from an individual retirement account ... from Form IT-201, line 9'.

### (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **MATCH**

Model: Table 1 gives $63 for statuses 1, 3 and 4, and $125 for statuses 2 and 5.

### 69 — NYC school tax credit (fixed amount)
Status: **MATCH**

Model: Item C Yes or income over $250,000 means no credit; otherwise the Table 1 full-year amount applies.

### (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **MATCH**

Model: Up to the first bracket amount the credit is '0.171% of taxable income'.

### (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **MATCH**

Model: The excess is measured over $12,000 for single and separate, $21,600 for joint and surviving spouse, and $14,400 for head of household.

### (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **MATCH**

Model: The schedule says '0.228% of the excess over' the bracket amount.

### (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **MATCH**

Model: The schedule base amounts are $21 for single and separate, $37 for joint and surviving spouse, and $25 for head of household.

### (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **MATCH**

Model: The credit is the base amount 'plus 0.228% of the excess'.

### (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **MATCH**

Model: Chooses the low or high formula by whether city taxable income is over the bracket amount.

### 69a — NYC school tax credit (rate reduction amount)
Status: **MATCH**

Model: Item C Yes means no credit. Income over $500,000 is refused, and otherwise the schedule applies to line 47.

### 70 — NYC earned income credit
Status: **MATCH**

Model: This uses the same EIC gate as line 65 and is refused where the filer could qualify; otherwise zero.

### 70a — NYC income tax elimination credit
Status: **MATCH**

Model: The credit requires dependents and federal AGI no more than $5,000 above the threshold. The top thresholds are 91,902 and 88,361, plus 5,000, which gives 96,902 and 93,361. The program refuses in that range and is zero otherwise.

### 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **MATCH**

Model: Zero unless other refundable credits apply. That case is refused.

### 72 — Total New York State tax withheld
Status: **MATCH**

Model: Totals New York State withholding from the Form IT-2 W-2 records in whole dollars. Withholding reported on Forms 1099-R, 1099-G and W-2G is refused.

### 73 — Total New York City tax withheld
Status: **MATCH**

Model: Totals New York City withholding from the Form IT-2 records. Withholding on other forms is refused.

### 74 — Total Yonkers tax withheld
Status: **MATCH**

Model: Zero, because any W-2 showing Yonkers withholding is refused.

### 75 — Total estimated tax payments and amount paid with Form IT-370
Status: **MATCH**

Model: The input wording covers estimated payments, applied 2024 overpayments, estate or trust allocations and Form IT-370 payments, and excludes unincorporated business tax, as the instructions do.

### 76 — Total payments (add lines 63 through 75)
Status: **MATCH**

Model: The form says 'add lines 63 through 75'; the restatement lists every line including 69a and 70a.

### (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **MATCH**

Model: The form says 'if line 76 is less than line 62, subtract line 76 from line 62'.

### (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 72 to 75)
Status: **MATCH**

Model: Prepayments are withholding plus estimated tax payments, which are lines 72 to 75.

### (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **MATCH**

Model: The instructions use '100% of your 2024 New York income tax based on a 12-month return'.

### (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **MATCH**

Model: The instructions use '110% of your 2024 New York income tax' for high-AGI filers.

### (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **MATCH**

Model: 110% applies 'if your 2024 New York adjusted gross income was more than $150,000 (or $75,000 if you are married filing separately for 2025)'.

### 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment on line 77
Status: **MATCH**

Model: Zero, and the program refuses whenever a penalty may be owed (Form IT-2105.9).

### 82 — Other penalties and interest
Status: **MATCH**

Model: Zero, and late filing or payment cases are refused.

### (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **MATCH**

Model: The form says 'if line 76 is more than line 62, subtract line 62 from line 76'.

### 77 — Amount overpaid
Status: **MATCH**

Model: The instructions say to 'subtract the penalty from the overpayment and enter the net overpayment on line 77'.

### 79 — Amount of line 77 that you want applied to your 2026 estimated tax
Status: **MATCH**

Model: When line 77 shows an overpayment, the tool uses the filer's chosen 'amount of overpayment from line 77 that you want applied to your ... estimated tax for 2026'; otherwise it enters zero. This matches the line 79 instruction.
Reviewed in: pass aafab4291976

### 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **MATCH**

Model: The tool computes 'subtract line 79 from line 77', floored at zero, and refuses when line 79 is more than line 77. This matches the line 78 text and instruction.
Reviewed in: pass aafab4291976

### 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195, line 4)
Status: **MATCH**

Model: The tool enters $0 and refuses whenever a refund exists and the filer wants a NYS 529 deposit via Form IT-195. That is the only case where line 78a takes an amount ('Enter on line 78a the amount from Form IT-195, line 4').
Reviewed in: pass aafab4291976

### 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **MATCH**

Model: The form says 'subtract line 78a from line 78'.

### 80 — Amount you owe
Status: **MATCH**

Model: The instructions say to enter 'the amount of tax you owe plus any estimated tax penalty ... and any other penalties and interest'.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| C | 2f4cfc9d431b0aebac77b25abb69510a4a1c812968120d5bfa95309f7b5a70d8 |
| H (count) | 0c8c87a494445eedac6b11398976eaa3cc695158ad2d7d62ac07fde93f319b62 |
| 1 | b82216fde0ece13b54ed01a359eff700095b60d0893c828617d2cfae397e68bd |
| 2 | 41a22296c262da3dae545c48ee34e0f1f178cb656d50b89b46b262cac4e8812b |
| 3 | ec9f1eece2ab7d441953cd351e87aea12bb92fc22ece65ed1f45d255fdff67fe |
| 4 | e1d3337da945c87972767038058bedf0ab6eef7a7fc10340c3622f29f03e99ff |
| 5 | 235dd3d6b2d7b9373f979dfef950e012f942a6e0a125603c4809ee690d712246 |
| 6 | 90d88b945c84a4fa55deec45942df8ded46685519be1159e194d81131951a2bc |
| 7 | 82878111e894a0c2004d43356934f07bac5d7e8f2e7ee4dec372f85418870044 |
| 8 | 6f160cf0e4c77dd6a181f583dafdb27927047a023c3bfc494088abace52fb537 |
| 9 | d97d6666d0cdb46cec05d3972a3e516f4fa1ebb03582f1d5bb4130fb7212d223 |
| 10 | 4b80cf7fc52861a084bcdb382925656131fa1c39857710b601d457aab7552a9f |
| 11 | 727ca2184449f1657e5b53a38aa4398bc08085b62d016cb37247916ddd9ccb08 |
| 12 | 0395ac8976a63d93a5362b42d969940f459e1dd2d3110f9d107b670d9d4a0c26 |
| 13 | 4ec1d54b039900ad9ea6933aa4d08f174c02f00535843d7760c0f68736fb9c7b |
| 14 | f2e176edc8c5592ca3ca6e1917bb32bb9bb18c62297265e75d27fda732d7f271 |
| 15 | 6968d1daf494ca8e847660489861948862d0563ece3c7bd8f78c0ec38e50357d |
| 16 | 4879f5d4641ca8a93f394cec8939fc80fa2e91beb132f6cd83c33c4317e0fcac |
| 17 | 2dd88a1cd98337186525093ddb5df722d837e0ec48c8969c8ea5a4315e69d0bb |
| 18 | 68c2887413c1d5fabba2464c31aca95b30c51525af6b38f3ee0dfd0316c83a24 |
| 19 | b0aa3430c68b45677572a3564afe889901b01ac11bd0d8d7857c92c693075be7 |
| (check) | e7b435db21cbeac2bafd631ffe088b75c31a59e2a427e92c2a1bebb82a0f9b6f |
| 20 | eb49d2043b7ab3f162c42a5509904ff35b61dcbe914297deb7e3c6a489bed467 |
| 21 | e01caf9bd3722539ce10fa1333b1a97b9cdf4008e32003289683113531d0876c |
| 22 | b25b8e11fd3673b4378bf161581aa0e94220e828cbd8149e12dccd6258cffdd0 |
| 23 | 9462caffa68f1e9961478ad54d8387e58fd23f5bec240a1d08fd58d271ed0759 |
| 24 | 8c9a6ce3ad8284582054a2a18d11a3530b7d42fd1eceb4ffc225cf6f95bb5315 |
| 25 | ba0407c3752f220d0a58de49ad8ce27624bf03fab0477bcb3873e53f2eefdea7 |
| 26 | a1d30f523fb437a8c3c79bb0ed3698b61d70ded981c7f25ec3fea74d863adb7a |
| 27 | ef46a52e6b14e33021b324fe149004c417bc54ee7800843188ba1fc4fba78e36 |
| 28 | 10da1d6ef569ec0386da996fd8b7f172ca2ae495adb26b41e78e60e3b7548991 |
| 29 | 2f8d71cff9a7f3c5f522ef1f106f1060930ddbc398d85ac73067f91fece1ac25 |
| 30 | 40dc0624b2968f29c94dc17fefcc0c41e378546a1691f0ecdc91605f75018338 |
| 31 | 55c1f5580047d968273a02c5f223c44c911eb6cd1ad6d6f3a0ec8ba21cf54147 |
| 32 | f594bf709a4c5f0afd174d32acc1943f10ecc5b329502bdd0a5c8af0954befc6 |
| 33 | 7b96b7c994a8e9a524d0193eb82a7a320ca68169b98c81a7b8f3f5cf2cfaf050 |
| (table) (ny_it201.std_deduction) | 0e8766c3c819e055d3d598b209b3e55c2835cd45cf104996847a451f3ecd7c3b |
| (table) (ny_it201.std_deduction_dependent) | 0fcde989e3b289b6a1609ebb5c9889f90e37528033509cc51d2e0c05e7da9310 |
| 34 | e0683f78f75a43ac73f781aa9b352ffa3c7311880dc48320cf8dd4e056e3cc8c |
| 35 | 654c67a879b75f8d7359e6f35b59180300efab6569e481f75c706e0fbbf6aaa0 |
| 36 | 19baf153857b46aba808e84884fc62df0f4d214854e1aad69053202256f3f80c |
| 37 | 26fc983509b26bf9a2ce7a2f1ae231b2f728a34cabf782b09e4df36ded036819 |
| 38 | 3dd5b97685a42f476fc377301827435eb8cd7a5c230cec8bf7870d08ea43e87c |
| (39) (ny_it201.tax_table) | b64a324f7f9afbb628f2e2f41c6408e524670eb6d0ad50fbe49222a1e50f5730 |
| (39) (ny_it201.tax_schedule) | 29bcfa6923dd528f07b2df3c79020d21f1b10af51361ba6ff0388b0179cead5a |
| (39) (ny_it201.tax_low) | 0a015228fd30bece32c79c19f6afec747232321c92a0e3d5260306dfec26d5ae |
| (39) (ny_it201.tcw.w1) | 209751d3fcc49f0250ab41532b45d7d79d5e5ef24e2cea693b9e1dd701c6d758 |
| (39) (ny_it201.tcw.w7) | 7acb0d534c38913cb03ecde61832c65ebd652c8030662d459a990f420501a886 |
| (39) (ny_it201.tcw.w12) | 4c6dddbcad460c7be5a3ef847fcf8b709b56ee20e76994534c4261fe0e867a1a |
| (39) (ny_it201.tcw.w2) | 16e9f9efa1f7d4e23d928f9202f078d977e61b42423719744261a7a2bcb11593 |
| (39) (ny_it201.tcw.w3) | ae6f9f70c57cf1699f633c678b908e9cb7c68062f11ad60628b69788dfc77ad7 |
| (39) (ny_it201.tcw.w4) | 6f6dc9fbdaaf2e4f3aa0799855d21089d86015e09bc6aed7e15f0feae1cbb55f |
| (39) (ny_it201.tcw.w5) | 1565d255c220d38de72ef1c4742ab2716ac181ce2b4aec1fc08e6378dc9e6f7f |
| (39) (ny_it201.tcw.w8) | f59c5c29efe4d708e3bfd1f648851591cb5db59a22360b13fce8c883dc303110 |
| (39) (ny_it201.tcw.w9) | 286d36196c149e92eb67b769e5ee05adb2608bb5857e20df0b037156ebe551fe |
| (39) (ny_it201.tcw.w10) | 6c6b85a11476bb55731a12673d7e0ea694a70ab830bf9c721c5dff12b5f0ee14 |
| (39) (ny_it201.tcw.w13) | ee403b0f4ed53c4ab5f2933c9355ed5b611de9d0fccdee0b7725127b2bc5e8f7 |
| (39) (ny_it201.tcw.w14) | 6f269b48b7cd75641edef9829ae8297b41ed728ba89ef391e103e51838b79ae9 |
| (39) (ny_it201.tcw.w15) | fb16da287b7d05c9c285e4e6fc8a18b52e72feed718690ea796812b28b28ceab |
| (39) (ny_it201.tcw.top) | 1f46d30522a768618abd742027e27833134cc916aa8f14e5ee3b951a0a6a103a |
| (39) (ny_it201.tcw.mfj) | 8745ec3fc6ca6a97e208b77942c31202757ec09601b5fbffd465f1622c002d42 |
| (39) (ny_it201.tcw.single) | 8745ec3fc6ca6a97e208b77942c31202757ec09601b5fbffd465f1622c002d42 |
| (39) (ny_it201.tcw.hoh) | 8745ec3fc6ca6a97e208b77942c31202757ec09601b5fbffd465f1622c002d42 |
| (39) (ny_it201.tcw.by_status) | 1a5586a8598f3c464d57180e53c15ba5c242348b528a5fd9c29870fda42970d7 |
| (39) (ny_it201.tax_high) | bd49c6fe1d68ffdfea8d051d504637bb6e9e7f5f301fa55ed26e0bd341fd6e0b |
| 39 | b01d0f039f30bbfd4500ef40ad8d36d40a2ddae40e12d5b786607aad96da3d22 |
| (Note 1) | c2232bfddb8e1503259af7718a9e339e36b83ae47bd9e757d31c74a52cf924b9 |
| (column) | bf4968e8b23937a8c339f0a41929770c2dcfa778a0ff2f693977a941806753f2 |
| (table 2, column 1) | 762f3e134de576ae4a7d7e36d261483fe77cd0ded71299a39bc0acbd688c5ae1 |
| (table 5, column 1) | 9a76d6b116983a75167d52314ac1b8a11cf0b9f64623a6b5dbdb03c710916c00 |
| (table 2, column 2) | e3b8c5f4ee650c6c9979251e44f0995708c3b6783525fe2aa69e75a9c7190a61 |
| (table 5, column 2) | 98f57b50050445e4088ea45395f220970d885bf2fb4f83fa8609cd71e64e9166 |
| (table 2, column 3) | c0065b659f44792cbb22267cf0f0139978aa449da878303fa63db52001c63a30 |
| (table 5, column 3) | c87d8034ba11103a9521265578675773e292119163f61a632ee7ff38ae3c815c |
| (table 2, column 4) | 6b620c220df3e262905e3ec8b4350bcd567a3a30140b6af2bc5a3c5c803d6127 |
| (table 5, column 4) | 34bcd83fa227f79777c4b654831ca93290f3b02a6de662bd780e048ace520076 |
| (table 2, column 5) | 8fc9806b243480a8d1ee0b6044fe70bdaa91c217d7af11418251832236947edc |
| (table 5, column 5) | 905efca37e84043612097d2f19f2a774a692ff6c37e6b0247335ab1f4b25309b |
| (table 2, column 6) | bd7f58622acd85318606d1abd7f753fa00ee1d32fabc2328ae9eae19fc818df9 |
| (table 5, column 6) | e0f61c2b9f928db7b6fc6ee5c1b97ebf85c36b570572855b2be4fbc4a0c3f650 |
| (table 2, column 7) | 3a9116d65a58a930644aa6368e1d3d56f44729194bc666d58588a124c91f9b37 |
| (table 5, column 7) | 942686ed0c2a8d9111f2bb3cfadb37edd76b5e90f947de37988083401508fab4 |
| (table 2) | 2a900f8f5ce3803220cdc2431b06cf50ad4697ae3526385c3a46ac33041fe00d |
| (table 5) | 6c3e73bf37007dcde1f39ee96a559290a2f63947e359cce7876e46e142aaf363 |
| (table 1) | 148b4499fd3728f81ff374338dbfdd86035beffb6ab3205ace66b04f5c86dc4d |
| (table 4) | 3bada7525cd785b2bc159137d40feb4a1d7e118d0bce8c44b5023bfe8e5edf6d |
| (40) | 5b7b0c67337989723dbdc71cc86b9847b5ed126547cbde9341d020162b85c8bc |
| (48) | be511286c5c784fd8d72020f389fccbbb129504aed32cb20b32446ec3aac31cc |
| 40 | e4964f3319baf2c14ebf16bf74edbe8f23a19839eb9dbcbb0a9849d016fc1245 |
| 41 | 075d46d01371a5ddcd7001399bd6fd86e2fd64dee162009a078db661e35e5696 |
| 42 | 38e7e54fbb206e02ea396710bf968ace785c38da186476e2966f9dfa145165a6 |
| 43 | 0ce88c0c67a3d1a4c17d47409bdb3950bae1670b9c7809c9044bf8a22d001994 |
| 44 | 3cd7a1684f99ef0f7b695ee4ef8035b18d064b2baec6f51ddfcd4495b1b6b0b3 |
| 45 | cf184c7edef7915511928ac48e8dd74b4029be254fa88bb36dafb9331625719b |
| 46 | 3a4b70ebaa11c78e77a31aa2289cbde65f222bd14dda945373f8def7d7c3ef1f |
| 47 | 596853293d9a5f37f7a8548f7af108d090cd5fd4b1d57abd17088a9002c59ca8 |
| (47a) (ny_it201.city_tax_table) | a7fa356eefc0bcfdec2a0c5004f0c51b39bd516823e6749b0e748546dc612c80 |
| (47a) (ny_it201.city_tax_schedule) | f307de98fbb6466a67c1e78bb7fe74deb1c590cd502323d04626dd2591d234cf |
| 47a | 05e571c7eda86eea3ee225d8e9917433078f45ba8b9e0789163160f85dbceb24 |
| 48 | ff3fbd5ae6aa0580837b4020155b48891ac4370dfc4d1c7f02ee58f7e5fe684b |
| 49 | 8eeb7186e42775f3ec6e0cff74306a2a6a677e6cbbbaf6925fad91c0d8879ff3 |
| 50 | 459b49222e30a4359e91a309b6f34d09333434b80aa65f4551682fbb70343c9c |
| 51 | fc54bacc0650aca8b740602356f61d1cb244af2e71e5e0f980bcd6f99d549474 |
| 52 | 7690406c9c23247e330709f2bf007a36a5eacf7431410f2da6d6535a0e50ebc4 |
| 53 | 466cc37329c0a2b8c09874334c0fd61ac0401db563dd73b902beb25a6541458b |
| 54 | 7e1e452513fae92f3ff51828f5e7e174032e1bda227d2052f1aabc31af278e89 |
| 54a | 0cb2702f7081d5653cdb88626d5282009bd8cce70b70816a3230cd224991999b |
| 54b | 7bc3a7ce99e59311d3b023163a612624395fac872f75e417b749422633a9b8d2 |
| 54c | dc290918b70f6f5b9e9ec1999a3444b509104fd6616e8c4e2eb6fd2dddf86131 |
| 54d | 4b47ec5976c61ebbfc50b9ba99d0b9b0885a0f6976b916584125700949cafebc |
| 54e | 363a24922a6e8efe1fe270587a0bb9349804e9bf92bb0a759a12c506911d2ac7 |
| 55 | 90eac345d77c2d4bbf8b7041316a446d26651a61cf0f2492263ab98ee61da23b |
| 56 | 5ce2f693c23229dbcd06dcf713ab834255c141e446b9122f22e56357e6a7765a |
| 57 | 330b403b9a9df312a0f0956563620e80938aab53d39b40366b76edba6b7033c3 |
| 58 | f24e1e35714e29d46e688c7005d638ae0690988ed1643c63f154e34a352740e8 |
| (chart) (ny_it201.sut.b1) | 2af0018d75dbbeb4bb04675d7af8db0c72aaaeb73f5c401501bdf9769107eecd |
| (chart) (ny_it201.sut.b2) | e2a78e6ecedf4dcc1b849c4ffdab0aa624be0351922a2c30f0d19ddc16db5cd4 |
| (chart) (ny_it201.sut.b3) | 2cc15c22c03d8be35b211be5c2d74cfab31df2c48eec1748a2f2bb5bfb437487 |
| (chart) (ny_it201.sut.b4) | a62ab9a69ee9b824675f1d81dfc23ca900c182e6929bf67ae87b78e76420c9f7 |
| (chart) (ny_it201.sut.b5) | 56e73292419e3e87e81836ae91fd80fd0d02cf170d1c1fd41c1acf6b6cc46fa2 |
| (chart) (ny_it201.sut.b6) | 53020f44a85ade725145672d5436f46866e1832cea48a58d7b5ae7aad3c09dc7 |
| (chart) (ny_it201.sut.b7) | 74a19403e68438b64cb04189d8a9b669270bd305462bf78e2f312b67c9d234ea |
| (chart) (ny_it201.sut.top_product) | 73ea64cb38c487244314563ce9746ba8ba31454ddffd2a07261afe7cf23e7ebd |
| (chart) (ny_it201.sut.cap) | 4df4f43d41a4eb23cb9a8a1dad254cae661bb0b7a26cfe803d2a510506e4c74e |
| (chart) (ny_it201.sut.top) | 9af06e0ee4723749c98eb27fb954f505f8faf8afdfebf41c127de3e283950f4d |
| (chart) (ny_it201.sut.chart) | 20dcd6d7211eb560c45f956f59aa83f0dfd429ffad3808a2830adadbb0e9752d |
| 59 | db33a8aff0191f7f63aac4d97e8e865ca77d87ab10105fdbc3e42ef6fac4ded5 |
| 60 | 15c6c3523f008134cec04ca119978e35f294fdd72220059944267153f7f8bb43 |
| 61 | 95411e1d41538d66f1651ea42f62ece8d3f365a6cdfe2dce6a0fcac46810e83f |
| 62 | 624417f0c5415c0364412c313e174c575d0f60f18edb757bafe6cef37871cf5a |
| 63 | 116e4c60c910ef8aa80ff6cf65e23c5fd7fe1b775e02b00d1655445396f6594f |
| 64 | 6969c713ff6bce01679a0879d435f94ebdc1053c4ab8423a21430e8c3ca7e38c |
| 65 | 9e31cadedda4bf6b230eb458cacc032a09ccd052221ec1304cd46c228ecdfd4a |
| 66 | cf60c0a98c5c05ec04a370d0a624eb29cc64db709fb89aa6f704ec61e0df3e10 |
| 67 | bcdd51d96ce219344ab65342ea21ccff7ccdb239f4a7abc717d638e06674dba1 |
| 68 | 36e1662b373cef13281406fd4929ac8d620a6a7e2e762aea223f0a7115776f18 |
| (69) (ny_it201.stc_income) | de1338d480c5b810312817bdaa6a5606ab07a34e682b98b42fca2f9d1e6755ce |
| (69) (ny_it201.stc_fixed_amount) | 80e4e2f2e9ac6f0a884ce75d1933e434933d02746b7c88132e94c79f57afb892 |
| 69 | eab359f7e0086463d5fcaac50379e2d8799d82ab7131acb7136de210fa909f62 |
| (69a) (ny_it201.stc_rr_low) | 850101ea8025450936011493501f8c8efa608dd9cf54fe0943d3c676e9532167 |
| (69a) (ny_it201.stc_rr_excess) | 041d753e26891e16b3f97e8147560e3393698cb0786be76d0b6ac8d725434354 |
| (69a) (ny_it201.stc_rr_excess_product) | e9b801362d2eef5ef0fd9a793e13900eb1b9bac6fdaf6761f0d902b70ad21f5b |
| (69a) (ny_it201.stc_rr_base) | 8b76330641a4c0450c8a5f2af2cb216187253609b2204a9e77a05a56d26997c2 |
| (69a) (ny_it201.stc_rr_high) | e9b801362d2eef5ef0fd9a793e13900eb1b9bac6fdaf6761f0d902b70ad21f5b |
| (69a) (ny_it201.stc_rr) | 8c5bf23f63c83a37aec3e27a01fb326a6b830b2f21ebc3d68a0bafddf2f9d2a9 |
| 69a | 92ae8fc1a0cc75b4c395ebd35847f61e4f3b9235041a621dfb5bfbc0f00a9f54 |
| 70 | c1b77882bfa478597244335ac2467c270683611a99bd0edc816291b96e9130cb |
| 70a | 67cd8ff3610b8af9e0e65ce00d0a23f3618f35a40567f56c441582890222445e |
| 71 | 2ad8ca4d4503d4801c04677fcd31020bd46fafb81af8441cb7093d5c6f99d010 |
| 72 | 87f84ef2d5d528ce3c4b59f019a1901dccd500c0776b0107e12c675b1c4f7f97 |
| 73 | 3b771e9381d3b525af3fa86e0940c9cee195ae859a2c2c4684aec6a79d8e0d49 |
| 74 | f45d3e3ae95f61d7e71e605f811ebe4c2dfd15ae8508dde2fcd878c224e877f0 |
| 75 | 500ad39c749f24a3aba113cc8dd750892edffd9022a235336300674b545beb3e |
| 76 | 3c50701dcacee9a92285d767e87be7f4d37df38776106854869debf46fadb3cd |
| (80) | 2b3063a9debbcc2519fe45d4fe608ae2ca2be17ed73c0512f63e2d3129115380 |
| (81) (ny_it201.prepayments) | ce53892b5d06e37d8f63e8fe2f2cb96ea011220f80be38ea75e34d57f8bb0771 |
| (81) (ny_it201.safe_harbor_100) | 2113469f220b9d81c6751e5376e3edacd0e4e7d5dfd01ac8fdbcdb437983a976 |
| (81) (ny_it201.safe_harbor_110) | 32ba9c529ca72a8e1d720511f5fcb8da09494f7709363cb044845b484bc02438 |
| (81) (ny_it201.safe_harbor) | e8d092202a2f419d209bc471182b66a14517c0301529042d56cc23f22adf0113 |
| 81 | 5161eb3dc2812cdfe28c9d5d828de9f7d57425cc391b88d179e6c24ffd092c33 |
| 82 | a8b44b754142c484f8a5b288f15843a649fea7a6f96afeb173b4f2012c3963ad |
| (77) | b620cd8da4d6b8bb0b16851566574d7b3c0ecfdbe41656a6a003565b43b50dcf |
| 77 | 39167c32d56a1003b448f8bfec8ae7098ccd9febb46ea4b93e75aa4c2e24a3b0 |
| 79 | 4c3717f5ac7363450544036df39fddf2253e2ba454ce23b566a6163560d6ec0c |
| 78 | f08ea0aa827d718b485cc1bb05fdc2ee50db17c837651617732c9a5828448c26 |
| 78a | bf5b3713b257994c48ecef4d585529abbd38d8f935780e46d5cad6d80af9fd60 |
| 78b | 24d520cf3f6dc798998e1f90b5a40dd7f38843ae1de48b354a3da321cb38a4f6 |
| 80 | c3e95064e42b75d697f018c796f3a9261573236c0005b609cf5c2dedb9708bb5 |
| (rest of the document) | eff327fea59ac4f2d56d292426436dddf9389d4a6daf829d71258d67638e5517 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass b59076746e74

| field | value |
| --- | --- |
| date | 2026-11-05 |
| review scope | lines (39) (ny_it201.tax_low), (39) (ny_it201.tcw.mfj), (39) (ny_it201.tcw.single), (39) (ny_it201.tcw.hoh), (39) (ny_it201.tcw.by_status), (39) (ny_it201.tax_high), 39, 54b, 54d |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b59076746e74eb5f71ed30f5218c2f4f594339fc67072a1440a30b613d8c3515 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 390d22ff0e196470cf6119d363b160934f85d1c37fcc6196dd053b2d9797cb11 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 78491d0b825c2dd6aae0973f4bf73c953e66dddff17768fddf61c86bc6bf8b48 |
| receipt | .transcription/ny_it201.render.lines-95d9d8dfcfa8 |
| lines judged | 9 |
| match / mismatch / unclear / missing | 9 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 12, 15, 17, 32 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 15, 17, 32 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: Tax computation worksheet 1; Tax computation worksheet 12; Tax computation worksheet 13; Tax computation worksheet 14; Tax computation worksheet 2; Tax computation worksheet 3; Tax computation worksheet 4; Tax computation worksheet 6; Tax computation worksheet 7; Tax computation worksheet 8; Tax computation worksheet 9; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |

##### Raw response

```yaml
```yaml
lines:
  - key: "(39) (ny_it201.tax_low)"
    status: MATCH
    reason: "The instructions say to use the 2025 New York State Tax Table, or 'if line 38 is $65,000 or more, use the New York State tax rate schedule.' The restatement uses the table when line 38 is under $65,000 and the schedule otherwise, which is the same rule."
  - key: "(39) (ny_it201.tcw.mfj)"
    status: MATCH
    reason: "The taxable-income bands match worksheets 1 to 5: $161,550 or less; over $161,550 to $323,200; over $323,200 to $2,155,350; over $2,155,350 to $5,000,000; over $5,000,000. Each worksheet's AGI floor is implied because line 38 cannot exceed line 33, and the AGI conditions over $107,650 and up to $25,000,000 are handled by the parent choices."
  - key: "(39) (ny_it201.tcw.single)"
    status: MATCH
    reason: "The bands match worksheets 7 to 10: $215,400 or less; over $215,400 to $1,077,550; over $1,077,550 to $5,000,000; over $5,000,000. The AGI conditions are handled by the parent choices."
  - key: "(39) (ny_it201.tcw.hoh)"
    status: MATCH
    reason: "The bands match worksheets 12 to 15: $269,300 or less; over $269,300 to $1,616,450; over $1,616,450 to $5,000,000; over $5,000,000. The AGI conditions are handled by the parent choices."
  - key: "(39) (ny_it201.tcw.by_status)"
    status: MATCH
    reason: "The worksheet groups are 'Married filing jointly and qualifying surviving spouse', 'Single and married filing separately' and 'Head of household', and the mapping follows them. The program reads the filing status from the federal return rather than from IT-201 item A; the mapping is correct either way."
  - key: "(39) (ny_it201.tax_high)"
    status: MATCH
    reason: "Worksheets 6, 11 and 16 apply 'If your New York adjusted gross income (line 33) is more than $25,000,000'. Otherwise the worksheet for the filer's filing status applies."
  - key: "39"
    status: MATCH
    reason: "This follows 'Is line 33 (your New York adjusted gross income) $107,650 or less? If Yes, ... Tax Table ... or rate schedule ... If No, see Tax computation – New York adjusted gross income of more than $107,650.'"
  - key: "54b"
    status: MATCH
    reason: "If neither spouse has net earnings from self-employment over $50,000 allocated to either zone, the instructions say 'skip lines 54a through 54e', so $0 is correct. The refusal names the excluded case, where the MCTMT applies."
  - key: "54d"
    status: MATCH
    reason: "The instructions say 'Multiply the amount on line 54b by 0.34% (0.0034).' Rounding to whole dollars agrees with the form's 'Whole dollars only' and with the example '$57,000 x 0.0034 = $194'."
```
```

#### Pass aafab4291976

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 26, 28, 29, 54a, 54b, 64, 79, 78, 78a |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | aafab4291976fa5385147217b2c472a6191c5620e1329eda8f9c10f81dc4ebb4 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 390d22ff0e196470cf6119d363b160934f85d1c37fcc6196dd053b2d9797cb11 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | ca877a7318f657df6bfb31a2d547ce43aa29912069432cb8425352afa69f90f7 |
| receipt | .transcription/ny_it201.render.lines-adb75db56cdc |
| lines judged | 9 |
| match / mismatch / unclear / missing | 7 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 9, 12, 15, 16, 19, 23 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 9, 15, 16, 19, 23 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |
| ny_it216i | 2025 | 1 | cited pages | aaccbcdb1a41b6e6221e3b0f908cb845e48bb0435b736ce2cd8ed75239deb6ac | 1 | 64200221fb39e0126f8748f9cd859793e2faf9c24c3f4b9a0134ee079251128b |
| i2441 | 2025 | 1 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |

##### Raw response

```yaml
```yaml
lines:
  - key: "26"
    status: MATCH
    reason: "The tool enters $0 and refuses whenever line 9 or 10 shows pension or IRA income and the filer reports a NYS, local or federal government pension, which covers what the line 26 instruction allows to be subtracted. The question also names the listed authorities, the ORP and the domestic-relations-order spouses."
  - key: "28"
    status: MATCH
    reason: "The tool enters $0 and refuses whenever lines 2, 3, 6 or 11 show income and the filer included interest on U.S. government obligations or dividends from a fund holding them. That covers the instruction's 'interest income from U.S. government bonds or other U.S. government obligations on lines 2, 6, or 11' and its qualifying mutual-fund dividends."
  - key: "29"
    status: MATCH
    reason: "The tool enters $0 and refuses whenever line 9 or 10 shows pension income that is not a government pension and the recipient was 59½ or older during 2025 or received it as a beneficiary. This covers every case where the instruction allows an exclusion ('59½ before January 1, 2025' or 'became 59½ during 2025')."
  - key: "54a"
    status: MISMATCH
    reason: "The screening question is asked only of people with more than one Schedule C or Schedule C profit over $50,000, so other self-employment earnings get $0 with no refusal. The instructions say MCTMT net earnings include amounts on 'federal Schedule SE (Form 1040), Part 1, line 6', including IRC § 1402 income such as 'services performed by a United States citizen employed by a foreign government, the United Nations, or other international organization', which need not come from a Schedule C."
  - key: "54b"
    status: MISMATCH
    reason: "The same screen is used as for line 54a, so Zone 2 self-employment earnings from sources other than Schedule C get $0 without a refusal. The instructions treat IRC § 1402 income reported on 'federal Schedule SE (Form 1040), Part 1, line 6' as net earnings 'subject to the MCTMT'."
  - key: "64"
    status: MATCH
    reason: "The tool enters $0 and refuses whenever the filer had care expenses or benefits and 'Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you actually claimed it)?' is answered yes. That is the instruction's own test for completing Form IT-216."
  - key: "79"
    status: MATCH
    reason: "When line 77 shows an overpayment, the tool uses the filer's chosen 'amount of overpayment from line 77 that you want applied to your ... estimated tax for 2026'; otherwise it enters zero. This matches the line 79 instruction."
  - key: "78"
    status: MATCH
    reason: "The tool computes 'subtract line 79 from line 77', floored at zero, and refuses when line 79 is more than line 77. This matches the line 78 text and instruction."
  - key: "78a"
    status: MATCH
    reason: "The tool enters $0 and refuses whenever a refund exists and the filer wants a NYS 529 deposit via Form IT-195. That is the only case where line 78a takes an amount ('Enter on line 78a the amount from Form IT-195, line 4')."
```
```

#### Pass d4a19f82147a

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 1 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d4a19f82147a2fa50c4acf85c62c47576ad8a4b94eafbe7f6836b37842621009 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 390d22ff0e196470cf6119d363b160934f85d1c37fcc6196dd053b2d9797cb11 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 5d2a50a2fc3286f123a4b29beb74d56769c0bbd8ccc9e88d0b0471d97eb31c1e |
| receipt | .transcription/ny_it201.render.lines-6b86b273ff34 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 0 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 3, 4, 5, 13, 14, 30, 31 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 3, 4, 5, 30, 31 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |

##### Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: UNCLEAR
    reason: "The form prints line 1 as 'Wages, salaries, tips, etc.' under 'Federal income and adjustments' with 'Whole dollars only', but the pages given contain no line 1 instruction. Nothing here says the amount is federal Form 1040 line 1z or how to round to whole dollars (half up or otherwise). The refusals are consistent with the text given."
```
```

## Raw response

```yaml
```yaml
lines:
  - key: "C"
    status: MATCH
    reason: "Item C asks whether you can be claimed as a dependent, and the instructions say to mark Yes 'even if the other taxpayer did not claim you'. The helper asks exactly that."
  - key: "H (count)"
    status: MATCH
    reason: "Counts the dependents entered in item H. Line 36 multiplies 'the number of dependents listed in item H' by 1,000."
  - key: "1"
    status: MATCH
    reason: "Instructions: line 1 'should be the same as the amount reported on federal Form 1040, line 1z', in whole dollars. The refusals exclude part-year, nonresident-spouse, Yonkers, special-accrual, special-code and decedent returns."
  - key: "2"
    status: MATCH
    reason: "'Taxable interest income' is federal Form 1040 line 2b, in whole dollars."
  - key: "3"
    status: MATCH
    reason: "'Ordinary dividends' is federal Form 1040 line 3b."
  - key: "4"
    status: MATCH
    reason: "'Taxable refunds, credits, or offsets of state and local income taxes' is Schedule 1 line 1."
  - key: "5"
    status: MATCH
    reason: "'Alimony received' is Schedule 1 line 2a."
  - key: "6"
    status: MATCH
    reason: "'Business income or loss' is Schedule 1 line 3."
  - key: "7"
    status: MATCH
    reason: "'Capital gain or loss' is federal Form 1040 line 7a."
  - key: "8"
    status: MISMATCH
    reason: "The form asks for 'Other gains or losses (submit a copy of federal Form 4797)'. The program always enters $0, and no refusal names Form 4797 gains. Only the line 19 check against federal AGI would catch a nonzero amount."
  - key: "9"
    status: MATCH
    reason: "'Taxable amount of IRA distributions' is federal Form 1040 line 4b."
  - key: "10"
    status: MATCH
    reason: "'Taxable amount of pensions and annuities' is federal Form 1040 line 5b."
  - key: "11"
    status: MISMATCH
    reason: "The form asks for 'Rental real estate, royalties, partnerships, S corporations, trusts, etc. (submit copy of federal Schedule E)'. The program always enters $0, and no refusal names Schedule E income."
  - key: "12"
    status: MISMATCH
    reason: "The form asks for 'Rental real estate included in line 11'. This is fixed at $0 with no refusal for rental income, so it is wrong whenever line 11 should include rental real estate."
  - key: "13"
    status: MISMATCH
    reason: "The form asks for 'Farm income or loss (submit a copy of federal Schedule F)'. The program always enters $0, and no refusal names farm income."
  - key: "14"
    status: MATCH
    reason: "'Unemployment compensation' is Schedule 1 line 7."
  - key: "15"
    status: MATCH
    reason: "'Taxable amount of Social Security benefits' is federal Form 1040 line 6b."
  - key: "16"
    status: MATCH
    reason: "'Other income' is Schedule 1 line 9, total other income."
  - key: "17"
    status: MATCH
    reason: "The form says 'Add lines 1 through 11 and 13 through 16'. The restatement adds the same lines and leaves out line 12."
  - key: "18"
    status: MATCH
    reason: "'Total federal adjustments to income' is Schedule 1 line 26."
  - key: "19"
    status: MATCH
    reason: "The form says 'subtract line 18 from line 17'."
  - key: "(check)"
    status: MATCH
    reason: "Line 19 is labelled 'Federal adjusted gross income', so comparing it with Form 1040 line 11a is consistent with the form."
  - key: "20"
    status: MATCH
    reason: "Zero unless the filer has out-of-state bond interest. That case is refused."
  - key: "21"
    status: MATCH
    reason: "Zero unless the filer has 414(h) contributions. That case is refused."
  - key: "22"
    status: MATCH
    reason: "Zero unless the filer made a nonqualified New York 529 withdrawal. That case is refused."
  - key: "23"
    status: MATCH
    reason: "Zero unless Form IT-225 modifications apply. That case is refused."
  - key: "24"
    status: MATCH
    reason: "The form says 'Add lines 19 through 23'."
  - key: "25"
    status: MATCH
    reason: "Zero, and the program refuses whenever line 4 is above zero or an inflation refund check was included. That covers both the form's 'from line 4' and the instructions' inflation-check reading."
  - key: "26"
    status: MATCH
    reason: "Zero unless the filer has a government pension. That case is refused."
  - key: "27"
    status: MATCH
    reason: "The form says 'Taxable amount of Social Security benefits (from line 15)'."
  - key: "28"
    status: MATCH
    reason: "Zero unless the filer has U.S. government obligation interest. That case is refused."
  - key: "29"
    status: MATCH
    reason: "Zero unless the pension and annuity exclusion may apply. That case is refused."
  - key: "30"
    status: MATCH
    reason: "Zero unless the filer has New York 529 contributions or withdrawals. That case is refused."
  - key: "31"
    status: MATCH
    reason: "Zero unless Form IT-225 subtractions apply. That case is refused."
  - key: "32"
    status: MATCH
    reason: "The form says 'Add lines 25 through 31'."
  - key: "33"
    status: MATCH
    reason: "The form says 'subtract line 32 from line 24'."
  - key: "(table) (ny_it201.std_deduction)"
    status: MATCH
    reason: "Matches the standard deduction table: Single (item C No) 8,000; joint 16,050; separate 8,000; head of household 11,200; qualifying surviving spouse 16,050."
  - key: "(table) (ny_it201.std_deduction_dependent)"
    status: MATCH
    reason: "The table gives 'Single and you marked item C Yes' as $3,100."
  - key: "34"
    status: MATCH
    reason: "Picks the standard deduction for the filer's status and item C answer. Itemizing is refused through the Form IT-196 gate."
  - key: "35"
    status: MATCH
    reason: "The form says 'Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)'."
  - key: "36"
    status: MATCH
    reason: "The form says 'multiply the number of dependents listed in item H by 1,000', and the exemption is $1,000."
  - key: "37"
    status: MATCH
    reason: "Line 36 is subtracted from line 35. The instructions leave the line blank if line 36 is more than line 35, which comes to the same zero."
  - key: "38"
    status: MATCH
    reason: "The instructions say to enter the taxable income on both line 37 and line 38."
  - key: "(39) (ny_it201.tax_table)"
    status: MATCH
    reason: "The instructions say to use the 2025 New York State Tax Table when line 38 is below $65,000."
  - key: "(39) (ny_it201.tax_schedule)"
    status: MATCH
    reason: "The rate schedule bands, base amounts and rates in the glossary match the printed schedules for all filing statuses."
  - key: "(39) (ny_it201.tax_low)"
    status: MATCH
    reason: "The instructions say to use the tax table, or the rate schedule 'if line 38 is $65,000 or more'."
  - key: "(39) (ny_it201.tcw.w1)"
    status: MATCH
    reason: "Worksheet 1 has a 5.5% flat rate, the Stop at $157,650, the excess over $107,650 divided by $50,000 and rounded to four decimals, and line 9 as line 4 plus line 8. The restatement follows all of these."
  - key: "(39) (ny_it201.tcw.w7)"
    status: MATCH
    reason: "Worksheet 7 has the same structure as worksheet 1, with a 6% rate."
  - key: "(39) (ny_it201.tcw.w12)"
    status: MATCH
    reason: "Worksheet 12 has the same structure as worksheet 1, with a 6% rate."
  - key: "(39) (ny_it201.tcw.w2)"
    status: MATCH
    reason: "Worksheet 2 prints Recapture Base 333, Incremental Benefit 807 and excess over $161,550, all as restated."
  - key: "(39) (ny_it201.tcw.w3)"
    status: MATCH
    reason: "Worksheet 3 prints Recapture 1,140, Incremental 2,747 and excess over $323,200, all as restated."
  - key: "(39) (ny_it201.tcw.w4)"
    status: MATCH
    reason: "Worksheet 4 prints Recapture 3,887, Incremental 60,350 and excess over $2,155,350, all as restated."
  - key: "(39) (ny_it201.tcw.w5)"
    status: MATCH
    reason: "Worksheet 5 prints Recapture 64,237, Incremental 32,500 and excess over $5,000,000, all as restated."
  - key: "(39) (ny_it201.tcw.w8)"
    status: MATCH
    reason: "Worksheet 8 prints Recapture 568, Incremental 1,831 and excess over $215,400, all as restated."
  - key: "(39) (ny_it201.tcw.w9)"
    status: MATCH
    reason: "Worksheet 9 prints Recapture 2,399, Incremental 30,172 and excess over $1,077,550, all as restated."
  - key: "(39) (ny_it201.tcw.w10)"
    status: MATCH
    reason: "Worksheet 10 prints Recapture 32,571, Incremental 32,500 and excess over $5,000,000, all as restated."
  - key: "(39) (ny_it201.tcw.w13)"
    status: MATCH
    reason: "Worksheet 13 prints Recapture 787, Incremental 2,289 and excess over $269,300, all as restated."
  - key: "(39) (ny_it201.tcw.w14)"
    status: MATCH
    reason: "Worksheet 14 prints Recapture 3,076, Incremental 45,261 and excess over $1,616,450, all as restated."
  - key: "(39) (ny_it201.tcw.w15)"
    status: MATCH
    reason: "Worksheet 15 prints Recapture 48,337, Incremental 32,500 and excess over $5,000,000, all as restated."
  - key: "(39) (ny_it201.tcw.top)"
    status: MATCH
    reason: "Worksheets 6, 11 and 16 say 'Multiply line 1 by 10.9% (0.109)', where line 1 is the taxable income from line 38."
  - key: "(39) (ny_it201.tcw.mfj)"
    status: MATCH
    reason: "Worksheets 1 to 5 are chosen by taxable income at the printed limits of 161,550, 323,200, 2,155,350 and 5,000,000."
  - key: "(39) (ny_it201.tcw.single)"
    status: MATCH
    reason: "Worksheets 7 to 10 are chosen at the printed limits of 215,400, 1,077,550 and 5,000,000."
  - key: "(39) (ny_it201.tcw.hoh)"
    status: MATCH
    reason: "Worksheets 12 to 15 are chosen at the printed limits of 269,300, 1,616,450 and 5,000,000."
  - key: "(39) (ny_it201.tcw.by_status)"
    status: MATCH
    reason: "The worksheet groups are 'Married filing jointly and qualifying surviving spouse', 'Single and married filing separately' and 'Head of household'. The restatement maps statuses to the same groups."
  - key: "(39) (ny_it201.tax_high)"
    status: MATCH
    reason: "The flat 10.9% worksheet applies 'If your New York adjusted gross income (line 33) is more than $25,000,000'."
  - key: "39"
    status: MATCH
    reason: "The instructions ask 'Is line 33 ... $107,650 or less?' If Yes, use the table or schedule; if No, use the tax computation worksheets."
  - key: "(Note 1)"
    status: MATCH
    reason: "Note 1 says federal adjusted gross income is line 19, and code A6 is refused. Flooring at zero does not change any lookup, because the first row of each table covers 0 or negative amounts (Note 2)."
  - key: "(column)"
    status: MATCH
    reason: "The column is 'the number of dependents listed on Form IT-201, item H, plus one for you (and one for your spouse if Married filing joint return)'."
  - key: "(table 2, column 1)"
    status: MATCH
    reason: "Table 2, column 1 values (90, 75, 65, 60, 60, 50, 40, 20) are looked up by federal AGI."
  - key: "(table 5, column 1)"
    status: MATCH
    reason: "Table 5, column 1 values (30, 25, 15, 10) are looked up by federal AGI."
  - key: "(table 2, column 2)"
    status: MATCH
    reason: "Table 2, column 2 lookup."
  - key: "(table 5, column 2)"
    status: MATCH
    reason: "Table 5, column 2 lookup."
  - key: "(table 2, column 3)"
    status: MATCH
    reason: "Table 2, column 3 lookup."
  - key: "(table 5, column 3)"
    status: MATCH
    reason: "Table 5, column 3 lookup."
  - key: "(table 2, column 4)"
    status: MATCH
    reason: "Table 2, column 4 lookup."
  - key: "(table 5, column 4)"
    status: MATCH
    reason: "Table 5, column 4 lookup."
  - key: "(table 2, column 5)"
    status: MATCH
    reason: "Table 2, column 5 lookup."
  - key: "(table 5, column 5)"
    status: MATCH
    reason: "Table 5, column 5 lookup."
  - key: "(table 2, column 6)"
    status: MATCH
    reason: "Table 2, column 6 lookup."
  - key: "(table 5, column 6)"
    status: MATCH
    reason: "Table 5, column 6 lookup."
  - key: "(table 2, column 7)"
    status: MATCH
    reason: "Table 2, column 7 lookup."
  - key: "(table 5, column 7)"
    status: MATCH
    reason: "Table 5, column 7 lookup."
  - key: "(table 2)"
    status: MATCH
    reason: "Picks the column for a count of 1 to 7. Counts over 7 (Note 3) are refused through the over-7 gate."
  - key: "(table 5)"
    status: MATCH
    reason: "Picks the column for a count of 1 to 7. Counts over 7 are refused."
  - key: "(table 1)"
    status: MATCH
    reason: "Table 1 (Single only) is looked up by federal AGI: 75, 60, 50, 45, 40, 20, then none over 28,000."
  - key: "(table 4)"
    status: MATCH
    reason: "Table 4 (Single only) gives 15 up to $10,000, 10 up to $12,500, and none above."
  - key: "(40)"
    status: MATCH
    reason: "Single uses table 1; statuses 2, 4 and 5 use table 2. Married filing separately (table 3) is zero only where no credit is allowed and is otherwise refused."
  - key: "(48)"
    status: MATCH
    reason: "Single uses table 4; statuses 2, 4 and 5 use table 5. Married filing separately (table 6) is refused where a credit is allowed."
  - key: "40"
    status: MATCH
    reason: "The instructions say 'If you marked the Yes box at item C ... you do not qualify for this credit', and otherwise to use the tables."
  - key: "41"
    status: MATCH
    reason: "Zero unless the filer paid tax to another state or province. That case is refused, routing to Form IT-112-R."
  - key: "42"
    status: MATCH
    reason: "Zero unless other credits apply. That case is refused, routing to Form IT-201-ATT."
  - key: "43"
    status: MATCH
    reason: "The form says 'Add lines 40, 41, and 42'."
  - key: "44"
    status: MATCH
    reason: "The form says 'Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)'."
  - key: "45"
    status: MATCH
    reason: "Zero unless other taxes apply. That case is refused, routing to Form IT-201-ATT Part 2."
  - key: "46"
    status: MATCH
    reason: "The form says 'add lines 44 and 45'."
  - key: "47"
    status: MATCH
    reason: "The instructions say to enter the line 38 amount unless an itemized Charitable Gifts Trust contribution was claimed. Itemizing is refused, so that exception cannot arise."
  - key: "(47a) (ny_it201.city_tax_table)"
    status: MATCH
    reason: "The instructions say to use the 2025 New York City Tax Table if line 47 is less than $65,000."
  - key: "(47a) (ny_it201.city_tax_schedule)"
    status: MATCH
    reason: "The city rate schedule bands, bases (369/858/1,813; 665/1,545/3,264; 443/1,030/2,176) and rates match the printed schedule."
  - key: "47a"
    status: MATCH
    reason: "The instructions ask 'Is line 47 ... less than $65,000?' If Yes, use the table; if No, use the rate schedule."
  - key: "48"
    status: MATCH
    reason: "Item C Yes means no credit; otherwise tables 4 and 5 apply, and table 6 and counts over 7 are refused."
  - key: "49"
    status: MATCH
    reason: "The form says 'Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)'."
  - key: "50"
    status: MATCH
    reason: "The part-year city resident tax is zero because part-year city residents are refused (Form IT-360.1)."
  - key: "51"
    status: MATCH
    reason: "Zero unless other city taxes apply, which is refused. The one-spouse-resident case is refused through the spouse gate."
  - key: "52"
    status: MATCH
    reason: "The form says 'Add lines 49, 50, and 51'."
  - key: "53"
    status: MATCH
    reason: "Zero unless city nonrefundable credits apply. That case is refused."
  - key: "54"
    status: MATCH
    reason: "The form says 'Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)'."
  - key: "54a"
    status: MATCH
    reason: "Zero unless self-employment earnings over $50,000 are allocated to either MCTMT zone. That case is refused."
  - key: "54b"
    status: MATCH
    reason: "Zero. The MCTMT gate on line 54a covers Zone 2 and refuses lines 54a to 54e."
  - key: "54c"
    status: MATCH
    reason: "The instructions say 'Multiply the amount on line 54a by 0.60% (0.0060)'."
  - key: "54d"
    status: MATCH
    reason: "The instructions say 'Multiply the amount on line 54b by 0.34% (0.0034)'."
  - key: "54e"
    status: MATCH
    reason: "The form says 'add lines 54c and 54d'."
  - key: "55"
    status: MATCH
    reason: "Zero, because Yonkers living quarters or wages are refused."
  - key: "56"
    status: MATCH
    reason: "Zero, because Yonkers wages are refused."
  - key: "57"
    status: MATCH
    reason: "Zero, because Yonkers part-year residence is refused."
  - key: "58"
    status: MATCH
    reason: "The form says 'add lines 54 and 54e through 57'."
  - key: "(chart) (ny_it201.sut.b1)"
    status: MATCH
    reason: "The chart gives 'up to $15,000 ... $3'."
  - key: "(chart) (ny_it201.sut.b2)"
    status: MATCH
    reason: "The chart gives '$15,001 - $30,000 ... 6'."
  - key: "(chart) (ny_it201.sut.b3)"
    status: MATCH
    reason: "The chart gives '30,001 - 50,000 ... 10'."
  - key: "(chart) (ny_it201.sut.b4)"
    status: MATCH
    reason: "The chart gives '50,001 - 75,000 ... 15'."
  - key: "(chart) (ny_it201.sut.b5)"
    status: MATCH
    reason: "The chart gives '75,001 - 100,000 ... 18'."
  - key: "(chart) (ny_it201.sut.b6)"
    status: MATCH
    reason: "The chart gives '100,001 - 150,000 ... 26'."
  - key: "(chart) (ny_it201.sut.b7)"
    status: MATCH
    reason: "The chart gives '150,001 - 200,000 ... 34'."
  - key: "(chart) (ny_it201.sut.top_product)"
    status: MATCH
    reason: "The chart gives '0.0175% (0.000175) of income' for incomes over $200,000."
  - key: "(chart) (ny_it201.sut.cap)"
    status: MATCH
    reason: "The chart gives '$125, whichever amount is smaller'."
  - key: "(chart) (ny_it201.sut.top)"
    status: MATCH
    reason: "Takes the smaller of the 0.0175% product and $125, as the chart says."
  - key: "(chart) (ny_it201.sut.chart)"
    status: MATCH
    reason: "The bands are keyed on federal AGI from line 19 at the printed whole-dollar break points."
  - key: "59"
    status: MATCH
    reason: "The instructions say 'If you do not owe any sales or use tax, you must enter 0'; otherwise use the chart. The part-year abode and Form ST-141 cases are refused."
  - key: "60"
    status: MATCH
    reason: "Zero unless the filer wants to make voluntary contributions. That case is refused (Form IT-227)."
  - key: "61"
    status: MATCH
    reason: "The form says 'add lines 46, 58, 59, and 60'."
  - key: "62"
    status: MATCH
    reason: "The form says 'Enter amount from line 61'."
  - key: "63"
    status: MATCH
    reason: "Zero when there is no child under 17, and refused otherwise, matching the instruction to complete Form IT-213 only with a qualifying child under 17."
  - key: "64"
    status: MATCH
    reason: "Zero unless the filer would qualify for the federal child and dependent care credit. That case is refused."
  - key: "65"
    status: MATCH
    reason: "Refused if the federal EIC was claimed or federal AGI is below the EIC limit ('could you have claimed it based on your federal adjusted gross income'). Otherwise zero."
  - key: "66"
    status: MATCH
    reason: "Zero unless child support was paid through a Support Collection Unit. That case is refused."
  - key: "67"
    status: MATCH
    reason: "Zero unless the filer might qualify for the real property tax credit. That case is refused (Form IT-214)."
  - key: "68"
    status: MATCH
    reason: "Zero unless college tuition was paid. That case is refused (Form IT-272)."
  - key: "(69) (ny_it201.stc_income)"
    status: MATCH
    reason: "Income here 'means your federal adjusted gross income from Form IT-201, line 19, minus distributions from an individual retirement account ... from Form IT-201, line 9'."
  - key: "(69) (ny_it201.stc_fixed_amount)"
    status: MATCH
    reason: "Table 1 gives $63 for statuses 1, 3 and 4, and $125 for statuses 2 and 5."
  - key: "69"
    status: MATCH
    reason: "Item C Yes or income over $250,000 means no credit; otherwise the Table 1 full-year amount applies."
  - key: "(69a) (ny_it201.stc_rr_low)"
    status: MATCH
    reason: "Up to the first bracket amount the credit is '0.171% of taxable income'."
  - key: "(69a) (ny_it201.stc_rr_excess)"
    status: MATCH
    reason: "The excess is measured over $12,000 for single and separate, $21,600 for joint and surviving spouse, and $14,400 for head of household."
  - key: "(69a) (ny_it201.stc_rr_excess_product)"
    status: MATCH
    reason: "The schedule says '0.228% of the excess over' the bracket amount."
  - key: "(69a) (ny_it201.stc_rr_base)"
    status: MATCH
    reason: "The schedule base amounts are $21 for single and separate, $37 for joint and surviving spouse, and $25 for head of household."
  - key: "(69a) (ny_it201.stc_rr_high)"
    status: MATCH
    reason: "The credit is the base amount 'plus 0.228% of the excess'."
  - key: "(69a) (ny_it201.stc_rr)"
    status: MATCH
    reason: "Chooses the low or high formula by whether city taxable income is over the bracket amount."
  - key: "69a"
    status: MATCH
    reason: "Item C Yes means no credit. Income over $500,000 is refused, and otherwise the schedule applies to line 47."
  - key: "70"
    status: MATCH
    reason: "This uses the same EIC gate as line 65 and is refused where the filer could qualify; otherwise zero."
  - key: "70a"
    status: MATCH
    reason: "The credit requires dependents and federal AGI no more than $5,000 above the threshold. The top thresholds are 91,902 and 88,361, plus 5,000, which gives 96,902 and 93,361. The program refuses in that range and is zero otherwise."
  - key: "71"
    status: MATCH
    reason: "Zero unless other refundable credits apply. That case is refused."
  - key: "72"
    status: MATCH
    reason: "Totals New York State withholding from the Form IT-2 W-2 records in whole dollars. Withholding reported on Forms 1099-R, 1099-G and W-2G is refused."
  - key: "73"
    status: MATCH
    reason: "Totals New York City withholding from the Form IT-2 records. Withholding on other forms is refused."
  - key: "74"
    status: MATCH
    reason: "Zero, because any W-2 showing Yonkers withholding is refused."
  - key: "75"
    status: MATCH
    reason: "The input wording covers estimated payments, applied 2024 overpayments, estate or trust allocations and Form IT-370 payments, and excludes unincorporated business tax, as the instructions do."
  - key: "76"
    status: MATCH
    reason: "The form says 'add lines 63 through 75'; the restatement lists every line including 69a and 70a."
  - key: "(80)"
    status: MATCH
    reason: "The form says 'if line 76 is less than line 62, subtract line 76 from line 62'."
  - key: "(81) (ny_it201.prepayments)"
    status: MATCH
    reason: "Prepayments are withholding plus estimated tax payments, which are lines 72 to 75."
  - key: "(81) (ny_it201.safe_harbor_100)"
    status: MATCH
    reason: "The instructions use '100% of your 2024 New York income tax based on a 12-month return'."
  - key: "(81) (ny_it201.safe_harbor_110)"
    status: MATCH
    reason: "The instructions use '110% of your 2024 New York income tax' for high-AGI filers."
  - key: "(81) (ny_it201.safe_harbor)"
    status: MATCH
    reason: "110% applies 'if your 2024 New York adjusted gross income was more than $150,000 (or $75,000 if you are married filing separately for 2025)'."
  - key: "81"
    status: MATCH
    reason: "Zero, and the program refuses whenever a penalty may be owed (Form IT-2105.9)."
  - key: "82"
    status: MATCH
    reason: "Zero, and late filing or payment cases are refused."
  - key: "(77)"
    status: MATCH
    reason: "The form says 'if line 76 is more than line 62, subtract line 62 from line 76'."
  - key: "77"
    status: MATCH
    reason: "The instructions say to 'subtract the penalty from the overpayment and enter the net overpayment on line 77'."
  - key: "79"
    status: MATCH
    reason: "The form asks for the 'Amount of line 77 that you want applied to your 2026 estimated tax'."
  - key: "78"
    status: MATCH
    reason: "The form says 'subtract line 79 from line 77'. Line 79 larger than line 77 is refused."
  - key: "78a"
    status: MATCH
    reason: "Zero, and a 529 deposit is refused (Form IT-195)."
  - key: "78b"
    status: MATCH
    reason: "The form says 'subtract line 78a from line 78'."
  - key: "80"
    status: MATCH
    reason: "The instructions say to enter 'the amount of tax you owe plus any estimated tax penalty ... and any other penalties and interest'."
```
```
